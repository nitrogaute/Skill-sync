# Sotto QA Skill

> **MANDATORY before telling Gaute "fikset" for ANY Sotto change.**
> No exceptions. If you skip this, bugs ship.

## Quick Reference

| What | Where |
|------|-------|
| Dashboard | https://sotto-dashboard.vercel.app |
| Spec | ~/clawd/projects/sotto/SPEC.md |
| Baselines | ~/clawd/projects/sotto/e2e-audit/baselines/ |
| Scripts | ~/clawd/skills/sotto-qa/*.py |
| Auth key | localStorage `sb-ukwzbvfstvfavptxiyrn-auth-token` |
| Browser | OpenClaw browser tool, profile="openclaw" |
| Deploy hook | `curl -s -X POST "https://api.vercel.com/v1/integrations/deploy/prj_K26OpiinVUZWMyecFtJta0O0DzlY/vyzupYJ1JP"` |
| Supabase | `mcporter call supabase.execute_sql --args '{"project_id":"ukwzbvfstvfavptxiyrn","query":"..."}'` |

---

## 🚨 THE RULE

**You MUST complete the full Pre-Deploy + Post-Deploy checklist before saying "fikset" to Gaute.**

If ANY check fails → fix it first. Do NOT tell Gaute it's done until everything passes.

---

## Phase 1: Pre-Deploy Verification

Run these BEFORE pushing to production:

### 1.1 Local Build
```bash
cd ~/clawd/projects/sotto
npm run build
```
Build must succeed with zero errors. Warnings are OK.

### 1.2 Critical Path Smoke Test (localhost)
```bash
cd ~/clawd/projects/sotto && npm run dev &
```
Using browser tool (profile="openclaw"), navigate to http://localhost:3000 and verify:
1. App loads, redirects to today view
2. Task checkbox toggles done state
3. Clicking task text opens detail dialog
4. Detail dialog scrolls on mobile viewport
5. Quick capture (⌘N or + button) creates a task

### 1.3 Push & Deploy
```bash
cd ~/clawd/projects/sotto
git add -A && git commit -m "fix: <description>" && git push
```
Then trigger deploy:
```bash
curl -s -X POST "https://api.vercel.com/v1/integrations/deploy/prj_K26OpiinVUZWMyecFtJta0O0DzlY/vyzupYJ1JP"
```
Wait ~60s, then verify https://sotto-dashboard.vercel.app loads.

---

## Phase 2: Full Regression Suite

Run after deploy completes. Use OpenClaw browser tool with profile="openclaw".

### 2.1 All 15 Views Load

Navigate to each view and verify it renders without error:

```
today, week, tasks, projects, topics, notes, meetings, people, 
okrs, documents, trym, graph, finances, health, weekly-review
```

**Method:** Use browser tool to navigate to `https://sotto-dashboard.vercel.app`, then for each view:
1. Take snapshot, find the nav item, click it
2. Wait for content to load
3. Take screenshot at both viewports
4. Verify no error boundaries / blank screens

**Views are accessed via:**
- Sidebar nav items (desktop)
- Bottom tab bar + More sheet (mobile)  
- Or directly: `window.__sotto_setActiveView('<view-id>')` via browser evaluate

### 2.2 Universal Task Behavior

Test on Today view (has tasks visible):

1. **Checkbox toggle:** Click a task checkbox → verify green checkmark + strikethrough appears
2. **Text opens detail:** Click task text (not checkbox) → verify ObjectDetailDialog opens
3. **Detail dialog content:** Verify title, status, priority, description, tags, relations sections visible
4. **Close dialog:** Press Escape or click outside → dialog closes

### 2.3 Detail Dialog Scrolling (Mobile)

Set viewport to 375×812:
1. Open a task with description/subtasks
2. Verify dialog body scrolls (not clipped)
3. Verify no horizontal overflow
4. Verify bottom content (tags, relations, delete button) is reachable by scrolling

### 2.4 Quick Capture

1. Press ⌘N (or find + button on mobile)
2. Quick Capture dialog opens with tabs: Task | Note | Idea | Topic | Link
3. Type a task title, submit with ⌘Enter
4. Verify task appears in task list
5. Verify toast notification "Task created"

### 2.5 Inline Editing

On Tasks view (list mode):
1. Click a task title → enters edit mode (input field)
2. Change title, press Enter
3. Verify title updated
4. Reload page → verify title persisted

### 2.6 Status Change Persistence

1. Find a task with status "todo"
2. Click status icon to cycle to "in-progress"
3. Verify visual change (icon updates)
4. **Reload the page**
5. Verify task still shows "in-progress"
6. Cycle back to original state

### 2.7 Screenshot Matrix

For each of the 15 views, capture:
- **Mobile:** 375×812 viewport
- **Desktop:** 1440×900 viewport

Save to `~/clawd/projects/sotto/e2e-audit/screenshots/<date>/`

Naming: `<view>-<viewport>.png` (e.g., `today-mobile.png`, `today-desktop.png`)

---

## Phase 3: Visual Regression

### 3.1 Taking Baselines
Run when UI is in known-good state:
```bash
cd ~/clawd/skills/sotto-qa
python3 take-baselines.py
```
Or manually: screenshot all 15 views at both viewports, save to `~/clawd/projects/sotto/e2e-audit/baselines/`

### 3.2 Comparing After Changes
```bash
cd ~/clawd/skills/sotto-qa
python3 compare-screenshots.py
```
This compares current screenshots against baselines and reports pixel diff percentages.

**Thresholds:**
- < 1% diff → PASS (minor rendering variance)
- 1-5% diff → REVIEW (check manually)
- > 5% diff → FAIL (unexpected visual change)

### 3.3 Updating Baselines
After intentional UI changes, update baselines:
```bash
cp ~/clawd/projects/sotto/e2e-audit/screenshots/<date>/*.png ~/clawd/projects/sotto/e2e-audit/baselines/
```

---

## Phase 4: Mobile-Specific Tests

Set browser viewport to 375×812 (iPhone X):

### 4.1 Scrollability
For each view:
1. Navigate to view
2. Evaluate: `document.documentElement.scrollHeight > document.documentElement.clientHeight` (should be true for views with content)
3. Scroll to bottom → verify content is reachable
4. No stuck/fixed content blocking scroll

### 4.2 Detail Dialog Full-Screen
1. Open any object's detail dialog
2. Verify dialog takes full width
3. Scroll within dialog → all sections reachable
4. Close dialog → view scrolls normally

### 4.3 Touch Targets
Evaluate in browser:
```javascript
// Check all interactive elements have >= 44px touch targets
const elements = document.querySelectorAll('button, a, [role="button"], input, [role="checkbox"]');
const tooSmall = [];
elements.forEach(el => {
  const rect = el.getBoundingClientRect();
  if (rect.width > 0 && rect.height > 0 && (rect.width < 44 || rect.height < 44)) {
    tooSmall.push({ tag: el.tagName, class: el.className.slice(0,50), w: rect.width, h: rect.height });
  }
});
return tooSmall;
```
Log violations. Critical violations (nav buttons, checkboxes) must be fixed.

### 4.4 No Horizontal Overflow
```javascript
document.documentElement.scrollWidth > document.documentElement.clientWidth
```
Must return `false` on every view.

### 4.5 No Clipped Content
Visually inspect screenshots for:
- Text cut off at edges
- Buttons partially hidden
- Cards overflowing container

---

## Phase 5: Persistence Tests

Use Supabase MCP to verify DB state.

### 5.1 Create Task
1. Create task via Quick Capture with unique title (e.g., "QA-TEST-{timestamp}")
2. Query DB:
```sql
SELECT id, title, properties->>'status' as status FROM objects WHERE title LIKE 'QA-TEST-%' ORDER BY created_at DESC LIMIT 1;
```
3. Verify row exists with correct title

### 5.2 Toggle Done
1. Check the task's checkbox (mark done)
2. Reload page
3. Verify task shows as done in UI
4. Query DB: verify `properties->>'status' = 'done'`

### 5.3 Edit Title
1. Inline-edit the task title to "QA-TEST-EDITED-{timestamp}"
2. Reload page
3. Verify new title in UI
4. Query DB: verify `title = 'QA-TEST-EDITED-...'`

### 5.4 Delete
1. Open task detail → click Delete → confirm
2. Reload page
3. Verify task gone from UI
4. Query DB: verify row deleted

### 5.5 Cleanup
Always delete QA test objects after testing:
```sql
DELETE FROM objects WHERE title LIKE 'QA-TEST-%';
```

---

## Phase 6: Post-Deploy Checklist

**MANDATORY. Copy this checklist and fill it out before saying "fikset":**

```
## Sotto Deploy Verification — [DATE]

- [ ] `npm run build` passes locally
- [ ] Git committed and pushed
- [ ] Vercel deploy triggered and completed
- [ ] All 15 views load on production (no blank screens)
- [ ] Task checkbox toggles work
- [ ] Task text click opens detail dialog
- [ ] Detail dialog scrolls on mobile (375×812)
- [ ] Quick capture creates task successfully
- [ ] Status change persists after reload
- [ ] No horizontal overflow on mobile
- [ ] Screenshots saved to e2e-audit/screenshots/
- [ ] Specific fix verified (describe what was fixed and how it was tested)
```

**Only after ALL boxes are checked → tell Gaute "fikset".**

---

## Helper Scripts

### run-regression.py
Full Playwright regression — runs all views, interactions, persistence checks.
```bash
cd ~/clawd/skills/sotto-qa && python3 run-regression.py
```

### take-baselines.py
Captures baseline screenshots for all views at both viewports.
```bash
cd ~/clawd/skills/sotto-qa && python3 take-baselines.py
```

### compare-screenshots.py
Compares current screenshots against baselines, reports diffs.
```bash
cd ~/clawd/skills/sotto-qa && python3 compare-screenshots.py
```

---

## Using OpenClaw Browser Tool (Quick Reference)

```
# Open dashboard
browser: action=open, profile="openclaw", targetUrl="https://sotto-dashboard.vercel.app"

# Set mobile viewport (evaluate JS to resize)
browser: action=act, request={kind:"evaluate", fn:"() => { /* use snapshot at mobile dims */ }"}

# Take screenshot
browser: action=screenshot, profile="openclaw"

# Take snapshot (get page structure)
browser: action=snapshot, profile="openclaw"

# Click element by ref
browser: action=act, request={kind:"click", ref:"<ref>"}

# Type text
browser: action=act, request={kind:"type", ref:"<ref>", text:"hello"}

# Press key
browser: action=act, request={kind:"press", key:"Meta+n"}

# Evaluate JS
browser: action=act, request={kind:"evaluate", fn:"() => document.title"}

# Navigate to view via JS
browser: action=act, request={kind:"evaluate", fn:"() => window.__sotto_setActiveView('tasks')"}
```

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Auth redirect to /login | Re-inject auth token via localStorage |
| `__sotto_setActiveView` undefined | Deploy not ready — wait and retry |
| Screenshot blank | Add wait after navigation |
| Supabase query fails | Check RLS — use service role key |
| Build fails | Check for TypeScript errors, missing imports |
| Vercel deploy stuck | Check Vercel dashboard or re-trigger hook |
