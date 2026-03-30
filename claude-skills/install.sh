#!/usr/bin/env bash
set -euo pipefail

# Claude Skills Installer (cross-platform: macOS, Linux, Windows/Git Bash)
#
# Global install — links skills into ~/.claude/skills/ AND ~/.copilot/skills/
#   ./install.sh work       # universal + work (work machines)
#   ./install.sh personal   # universal + personal (personal machines)
#
# Agent install — links skills into agent project directories
#   ./install.sh trym       # universal + personal + trym-specific → clawd/skills/
#   ./install.sh nova       # nova-specific → ClaudeClaw/.claude/skills/
#
# Local install — links skills into OneDrive "AI SKILLS" folder
#   ./install.sh local km        # KM skills
#   ./install.sh local hydepoint # HydePoint skills
#
# On macOS/Linux: creates symlinks
# On Windows (Git Bash/MSYS): creates directory junctions (no admin needed)

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"

# Detect OS
is_windows() {
    [[ "$OSTYPE" == msys* ]] || [[ "$OSTYPE" == cygwin* ]] || [[ "$OSTYPE" == mingw* ]] || [[ -n "${WINDIR:-}" ]]
}

CLAUDE_SKILLS_DIR="$HOME/.claude/skills"
COPILOT_SKILLS_DIR="$HOME/.copilot/skills"

# Local skills target: OneDrive AI SKILLS folder
if is_windows; then
    LOCAL_SKILLS_BASE="$(cygpath "$USERPROFILE/OneDrive - KONGSBERG/Documents/AI SKILLS")"
else
    LOCAL_SKILLS_BASE="$HOME/OneDrive - KONGSBERG/Documents/AI SKILLS"
fi

cmd="${1:-}"
arg="${2:-}"

if [[ -z "$cmd" ]]; then
    echo "Usage:"
    echo ""
    echo "  Global (one-time per machine):"
    echo "    ./install.sh work       # universal + work skills"
    echo "    ./install.sh personal   # universal + personal skills"
    echo ""
    echo "  Agent (project-specific agent installs):"
    echo "    ./install.sh trym       # universal + personal + trym skills → clawd/skills/"
    echo "    ./install.sh nova       # nova skills → ClaudeClaw/.claude/skills/"
    echo ""
    echo "  Local (into AI SKILLS folder):"
    echo "    ./install.sh local km        # KM skills"
    echo "    ./install.sh local hydepoint # HydePoint skills"
    echo ""
    echo "  Global target:  ~/.claude/skills/ + ~/.copilot/skills/"
    echo "  Agent targets:  ~/clawd/skills/, ~/ClaudeClaw/.claude/skills/"
    echo "  Local target:   $LOCAL_SKILLS_BASE/<set>/"
    exit 1
fi

# Link a single skill directory into a target directory.
# On Windows: uses directory junctions via PowerShell. On Mac/Linux: uses symlinks.
link_one() {
    local source="$1"   # full path to skill dir
    local target="$2"   # full path to target dir (including skill name)

    if is_windows; then
        local win_source win_target
        win_source="$(cygpath -w "$source")"
        win_target="$(cygpath -w "$target")"

        # Remove existing junction, directory, or broken symlink
        if [[ -d "$target" ]] || [[ -L "$target" ]]; then
            powershell -NoProfile -Command "Remove-Item -Path '${win_target}' -Recurse -Force" 2>/dev/null || rm -f "$target" 2>/dev/null || true
        fi

        powershell -NoProfile -Command "New-Item -ItemType Junction -Path '${win_target}' -Target '${win_source}' | Out-Null" 2>/dev/null
    else
        # Unix: symlink
        if [[ -L "$target" ]]; then
            rm "$target"
        elif [[ -d "$target" ]]; then
            echo "    SKIP $(basename "$target") (real directory exists)"
            return 1
        fi
        ln -s "$source" "$target"
    fi
}

# Link all skill dirs from source_dir into one or more target dirs
link_skills() {
    local source_dir="$1"
    shift
    local target_dirs=("$@")

    if [[ ! -d "$source_dir" ]]; then
        echo "  '$(basename "$source_dir")' not found, skipping"
        return
    fi

    for td in "${target_dirs[@]}"; do
        mkdir -p "$td"
    done

    local count=0
    for skill_dir in "$source_dir"/*/; do
        [[ -d "$skill_dir" ]] || continue
        local skill_name
        skill_name="$(basename "$skill_dir")"

        local all_ok=true
        for td in "${target_dirs[@]}"; do
            if ! link_one "$skill_dir" "$td/$skill_name"; then
                all_ok=false
            fi
        done

        if $all_ok; then
            count=$((count + 1))
        fi
    done
    echo "  $(basename "$source_dir"): linked $count skills"
}

case "$cmd" in
    work)
        echo "Installing global skills (work)"
        echo "  -> $CLAUDE_SKILLS_DIR"
        echo "  -> $COPILOT_SKILLS_DIR"
        echo ""
        link_skills "$REPO_DIR/global/universal" "$CLAUDE_SKILLS_DIR" "$COPILOT_SKILLS_DIR"
        link_skills "$REPO_DIR/global/work" "$CLAUDE_SKILLS_DIR" "$COPILOT_SKILLS_DIR"
        ;;
    personal)
        echo "Installing global skills (personal)"
        echo "  -> $CLAUDE_SKILLS_DIR"
        echo "  -> $COPILOT_SKILLS_DIR"
        echo ""
        link_skills "$REPO_DIR/global/universal" "$CLAUDE_SKILLS_DIR" "$COPILOT_SKILLS_DIR"
        link_skills "$REPO_DIR/global/personal" "$CLAUDE_SKILLS_DIR" "$COPILOT_SKILLS_DIR"
        ;;
    trym)
        TRYM_SKILLS_DIR="$HOME/clawd/skills"
        echo "Installing agent skills (Trym)"
        echo "  -> $TRYM_SKILLS_DIR"
        echo ""
        link_skills "$REPO_DIR/global/universal" "$TRYM_SKILLS_DIR"
        link_skills "$REPO_DIR/global/personal" "$TRYM_SKILLS_DIR"
        link_skills "$REPO_DIR/agents/trym" "$TRYM_SKILLS_DIR"
        ;;
    nova)
        NOVA_SKILLS_DIR="$HOME/ClaudeClaw/.claude/skills"
        echo "Installing agent skills (Nova)"
        echo "  -> $NOVA_SKILLS_DIR"
        echo ""
        link_skills "$REPO_DIR/agents/nova" "$NOVA_SKILLS_DIR"
        ;;
    local)
        if [[ -z "$arg" ]]; then
            echo "Usage: ./install.sh local <km|hydepoint|...>"
            echo ""
            echo "Available local skill sets:"
            for d in "$REPO_DIR"/local/*/; do
                [[ -d "$d" ]] || continue
                local_name="$(basename "$d")"
                local skill_count=0
                for sd in "$d"/*/; do
                    [[ -d "$sd" ]] && skill_count=$((skill_count + 1))
                done
                echo "  $local_name ($skill_count skills)"
            done
            exit 1
        fi
        local_source="$REPO_DIR/local/$arg"
        if [[ ! -d "$local_source" ]]; then
            echo "Error: '$arg' not found in local/"
            echo "Available: $(ls "$REPO_DIR/local/" | tr '\n' ' ')"
            exit 1
        fi
        local_target="$LOCAL_SKILLS_BASE/$arg"
        echo "Installing local skills ($arg) to $local_target"
        echo ""
        link_skills "$local_source" "$local_target"
        ;;
    *)
        echo "Unknown command: $cmd"
        echo "Use: work, personal, trym, nova, or local <folder>"
        exit 1
        ;;
esac

echo ""
echo "Done."
