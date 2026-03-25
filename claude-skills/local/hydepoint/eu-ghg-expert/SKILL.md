---
name: eu-ghg-expert
description: EU Innovation Fund GHG emission avoidance methodology v5.0. Use when calculating greenhouse gas reductions for EII, RES, ES, MOB, or CCUS projects, or preparing monitoring/reporting plans for Innovation Fund applications.
---

# EU GHG InnovFund Expert

## Project Categories

**Energy Intensive Industry (EII)** - EU ETS Annex I sectors, product benchmarks, upstream/indirect/process emissions, component manufacturing

**Renewable Energy (RES)** - Renewable electricity/heating/cooling production, non-Annex I consumption, component manufacturing (max 5yr use period)

**Energy Storage (ES)** - Intra-daily electricity storage, long-term energy storage, innovative storage components, grid auxiliary services

**Mobility (MOB)** - Transport services, innovative vehicle/vessel/aircraft manufacturing, maritime/aviation/road, non-CO2 climate impacts

**CCUS** - CCS credit calculations, CCU product lifecycle, pipeline/road/rail/maritime transport, Enhanced Hydrocarbon Recovery

## Calculation Principles

**System Boundary**: Project emissions vs. reference emissions. Includes direct + indirect (grid) + upstream emissions. Excludes construction/decommissioning.

**Core Formula**:
```
GHG Emission Avoidance = Reference Emissions - Project Emissions
```

**Manufacturing Projects**:
```
Annual GHG Avoidance = N x UP x (Reference - Project Emissions)
```
- N = components manufactured and sold
- UP = use period (max 5 years or component lifetime, whichever lower)
- Cost-share adjustment: `Adjusted = Base Avoidance x CS_component`

## Monitoring Requirements

Key principles:
- Annual monitoring throughout operation
- Hourly profiles for grid electricity (where applicable)
- Actual vs. assumed parameters
- Supporting documentation required (invoices, test results, certificates)

**Monitored**: quantities of inputs/outputs, fuel consumption by type, electricity/heat use, GHG emissions, biomass origin/sustainability, RFNBO/LCF compliance

**Not monitored (deemed constant)**: fossil fuel emission factors (EU defaults), grid electricity factors, upstream emissions for conventional fuels, component cost-share

## Biomass & Alternative Fuels

**Biomass**: Must meet RED sustainability criteria. Track origin/type per batch. Use RED Annex V/VI default emission factors.

**RFNBOs**: Liquid/gaseous fuels from renewable non-biomass sources. Must comply with RED. Includes renewable hydrogen and synthetic fuels.

**Low-Carbon Fuels**: 70% GHG reduction threshold vs. fossil comparator. Includes recycled carbon fuels. Compliance with Directive (EU) 2024/1788.

## Data Hierarchy

1. Direct measurement
2. Mass/energy balance calculations
3. EU/national default values
4. IPCC default values
5. Industry benchmarks
6. Supplier data (with verification)

Sources: EU ETS benchmarks (2019/331), RED defaults, IPCC 2006, JEC Well-to-Tank, country-specific grid factors.

## Special Considerations

**Grid Electricity Attribution**: Direct line = specific source. PPAs = temporal + geographical correlation. Co-located RES + storage = curtailment credit. Grid withdrawal = average factor.

**Non-CO2 Impacts**: Aviation (contrails, NOx, aerosols - optional), Maritime (black carbon - mandatory), Geothermal (working fluid leakage), Fugitive emissions (refrigerants, process gases).

**EHR**: `CCS_credit x (1 - HC_produced / CO2_injected)`

## GHG Calculation Workflow

1. **Determine category** (EII/RES/ES/MOB/CCUS)
2. **Define system boundaries** - emission sources, reference scenario, upstream/indirect scope
3. **Calculate reference emissions** - EU ETS benchmarks for EII, conventional comparators for others
4. **Calculate project emissions** - direct + indirect + upstream + fugitive
5. **Determine avoidance** - subtract, apply manufacturing multipliers and cost-share if applicable
6. **Prepare monitoring plan** - parameters, frequency, data sources, reporting procedures

## References

- [monitoring-parameters.md](references/monitoring-parameters.md) - Parameter lists for all categories (Appendix 3)
- [definitions.md](references/definitions.md) - 64 technical definitions (Appendix 4)
- [emission-factors.md](references/emission-factors.md) - Common emission factors
- [regulatory-references.md](references/regulatory-references.md) - EU legislation and standards

## Regulatory Basis

- EU InnovFund GHG Methodology v5.0 (01.12.2025)
- Directive (EU) 2018/2001 (RED)
- Directive (EU) 2024/1788 (Low-Carbon Fuels)
- Directive 2003/87/EC (EU ETS)
- IPCC 2006 Guidelines
