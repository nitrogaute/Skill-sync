---
name: home-assistant
description: "Home Assistant REST API patterns for controlling smart home devices, reading sensors, managing automations, and energy monitoring. Use when the user asks about lights, climate, energy, sensors, automations, or any smart home control."
---

# Home Assistant Integration

## Connection

```bash
# Load credentials
source ~/.home-assistant-mcp/env
# $HOMEASSISTANT_URL = http://homeassistant.local:8123
# $HOMEASSISTANT_TOKEN = long-lived access token

# Base curl pattern (reuse everywhere)
HA_CURL="curl -s -H 'Authorization: Bearer $HOMEASSISTANT_TOKEN' -H 'Content-Type: application/json'"
```

## Reading State

### Get a single entity
```bash
source ~/.home-assistant-mcp/env
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states/sensor.energy_price"
```

Response: `{"entity_id": "...", "state": "1.23", "attributes": {...}, "last_changed": "..."}`

### Get all states (large response -- filter with jq)
```bash
source ~/.home-assistant-mcp/env
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '.[].entity_id' | head -50
```

### Search for entities by domain
```bash
# All lights
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '[.[] | select(.entity_id | startswith("light."))]'

# All sensors
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '[.[] | select(.entity_id | startswith("sensor."))]'

# All climate devices
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '[.[] | select(.entity_id | startswith("climate."))]'
```

## Calling Services

### Pattern
```bash
source ~/.home-assistant-mcp/env
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "ENTITY_ID"}' \
  "$HOMEASSISTANT_URL/api/services/DOMAIN/SERVICE"
```

### Common Services

**Lights:**
```bash
# Turn on
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room"}' \
  "$HOMEASSISTANT_URL/api/services/light/turn_on"

# Turn on with brightness (0-255) and color temp
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room", "brightness": 180, "color_temp": 350}' \
  "$HOMEASSISTANT_URL/api/services/light/turn_on"

# Turn off
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "light.living_room"}' \
  "$HOMEASSISTANT_URL/api/services/light/turn_off"
```

**Climate / Heating:**
```bash
# Set temperature
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "climate.living_room", "temperature": 22}' \
  "$HOMEASSISTANT_URL/api/services/climate/set_temperature"

# Set HVAC mode (heat, cool, auto, off)
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "climate.living_room", "hvac_mode": "heat"}' \
  "$HOMEASSISTANT_URL/api/services/climate/set_hvac_mode"
```

**Switches / Plugs:**
```bash
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "switch.garage_heater"}' \
  "$HOMEASSISTANT_URL/api/services/switch/turn_on"
```

**Scripts:**
```bash
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/services/script/turn_on" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "script.good_night"}'
```

**Automations:**
```bash
# Trigger an automation manually
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "automation.morning_routine"}' \
  "$HOMEASSISTANT_URL/api/services/automation/trigger"

# Enable/disable automation
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"entity_id": "automation.morning_routine"}' \
  "$HOMEASSISTANT_URL/api/services/automation/turn_on"

# Reload automations after config changes
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/services/automation/reload"
```

## History & Statistics

### Entity history (last 24h)
```bash
# Last 24 hours for a specific entity
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/history/period?filter_entity_id=sensor.energy_price" | jq '.[0] | length'
```

### Specific time range
```bash
# ISO format timestamps
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/history/period/2026-04-10T00:00:00?end_time=2026-04-11T00:00:00&filter_entity_id=sensor.energy_price"
```

### Long-term statistics (energy, temperatures)
```bash
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"type": "recorder/statistics_during_period", "start_time": "2026-04-01T00:00:00", "end_time": "2026-04-11T00:00:00", "statistic_ids": ["sensor.energy_price"], "period": "day"}' \
  "$HOMEASSISTANT_URL/api/template" 2>/dev/null || echo "Use WebSocket for statistics"
```

## Energy Monitoring

### Current energy price
```bash
source ~/.home-assistant-mcp/env
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states/sensor.energy_price" | jq '{price: .state, unit: .attributes.unit_of_measurement}'
```

### Power consumption
```bash
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '[.[] | select(.entity_id | test("sensor.*power|sensor.*energy|sensor.*consumption")) | {id: .entity_id, state: .state, unit: .attributes.unit_of_measurement}]'
```

## Templates (computed values)

```bash
# Render a template on the server
curl -s -X POST -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"template": "{{ states.sensor.energy_price.state }} {{ states.sensor.energy_price.attributes.unit_of_measurement }}"}' \
  "$HOMEASSISTANT_URL/api/template"
```

## Discovery (first session tasks)

When starting a new session with an unknown HA setup, run these to understand what's available:

```bash
source ~/.home-assistant-mcp/env

# 1. List all domains in use
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '[.[].entity_id | split(".")[0]] | unique'

# 2. List all services available
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/services" | jq '.[].domain' | sort -u

# 3. Count entities per domain
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq 'group_by(.entity_id | split(".")[0]) | map({domain: .[0].entity_id | split(".")[0], count: length}) | sort_by(-.count)'

# 4. List all automations
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/states" | jq '[.[] | select(.entity_id | startswith("automation.")) | {id: .entity_id, friendly_name: .attributes.friendly_name, state: .state}]'

# 5. Check HA version and config
curl -s -H "Authorization: Bearer $HOMEASSISTANT_TOKEN" \
  "$HOMEASSISTANT_URL/api/config" | jq '{version: .version, location_name: .location_name, latitude: .latitude, longitude: .longitude, elevation: .elevation}'
```

## Important Notes

- **2026.x uses plural keys**: triggers/actions/conditions (not trigger/action/condition) in automation YAML
- **Token location**: `~/.home-assistant-mcp/env` (source it, never hardcode)
- **Network**: HA is on local network at `homeassistant.local:8123` (Raspberry Pi)
- **Always source env first**: Every curl command needs the token
- **jq is essential**: Raw API responses are large, always filter with jq
- **Rate limiting**: No rate limits on local API, but batch requests where possible
