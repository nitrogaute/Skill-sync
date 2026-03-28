# Move Test Procedure

Run these checks from `C:\Users\gauteb\Documents Local\Skill-sync` to confirm everything works after moving the project off OneDrive.

## 1. Git integrity (root repo)

```bash
cd "C:\Users\gauteb\Documents Local\Skill-sync"
git status
git remote -v
git fetch --dry-run
```

**Expected:**
- Branch `master`, up to date with `origin/master`
- Remote: `https://github.com/nitrogaute/Skill-sync.git`
- Fetch completes without errors

## 2. Git integrity (claude-skills submodule)

```bash
cd claude-skills
git status
git remote -v
git fetch --dry-run
```

**Expected:**
- Branch `main`, up to date with `origin/main`
- Remote: `https://github.com/nitrogaute/claude-skills.git`
- Fetch completes without errors

## 3. Verify install.sh runs from new location

```bash
cd "C:\Users\gauteb\Documents Local\Skill-sync\claude-skills"
bash install.sh work
```

**Expected:**
- `universal: linked 36 skills`
- `work: linked 1 skills`

## 4. Verify junctions point to new path

Open PowerShell and run:

```powershell
Get-ChildItem "$env:USERPROFILE\.copilot\skills" |
  Where-Object { $_.Attributes -match 'ReparsePoint' } |
  Select-Object -First 5 |
  ForEach-Object {
    $t = (Get-Item $_.FullName).Target
    "$($_.Name) -> $t"
  }
```

**Expected:** All targets should contain `Documents Local\Skill-sync\claude-skills\` (not `OneDrive`).

Repeat for `.claude\skills`:

```powershell
Get-ChildItem "$env:USERPROFILE\.claude\skills" |
  Where-Object { $_.Attributes -match 'ReparsePoint' } |
  Select-Object -First 5 |
  ForEach-Object {
    $t = (Get-Item $_.FullName).Target
    "$($_.Name) -> $t"
  }
```

## 5. Verify skills load in VS Code Copilot

1. Open VS Code
2. Open a Copilot chat (Ctrl+Shift+I or click the Copilot icon)
3. Type: "List the skills you have available"
4. Confirm skills appear (docx, pptx, xlsx, drawio, etc.)

## 6. Verify skills load in Claude Code (if used)

```bash
claude
/skills
```

**Expected:** Skills list appears with all installed skills.

## 7. Verify local skill installs (optional)

```bash
cd "C:\Users\gauteb\Documents Local\Skill-sync\claude-skills"
bash install.sh local km
bash install.sh local hydepoint
bash install.sh local gtb
```

Then verify local junctions:

```powershell
Get-ChildItem "$env:USERPROFILE\OneDrive - KONGSBERG\Documents\AI SKILLS\km" |
  Where-Object { $_.Attributes -match 'ReparsePoint' } |
  Select-Object -First 3 |
  ForEach-Object {
    $t = (Get-Item $_.FullName).Target
    "$($_.Name) -> $t"
  }
```

**Expected:** Targets point to `Documents Local\Skill-sync\claude-skills\local\km\...`.

## 8. Verify git push works

```bash
cd "C:\Users\gauteb\Documents Local\Skill-sync\claude-skills"
git stash       # stash any uncommitted changes
git pull        # verify pull works
git stash pop   # restore changes
```

Repeat for the root repo:

```bash
cd "C:\Users\gauteb\Documents Local\Skill-sync"
git pull
```

---

## All checks passed?

If every step above succeeds, the old project at `c:\Users\gauteb\OneDrive - KONGSBERG\Documents\Coding Projects\Skill-sync` can be safely deleted.

**To delete the old location**, open an elevated terminal and run:

```powershell
Remove-Item "c:\Users\gauteb\OneDrive - KONGSBERG\Documents\Coding Projects\Skill-sync" -Recurse -Force
```
