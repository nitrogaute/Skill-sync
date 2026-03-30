---
name: linkedin
description: LinkedIn automation via browser control - read feed, messages, notifications, post content, and manage connections.
homepage: https://linkedin.com
metadata: {"clawdbot":{"emoji":"💼","requires":{"browser":true}}}
---

# linkedin 💼

LinkedIn automation using Clawdbot's browser tool. No CLI required — directly controls your browser session.

## Overview

This skill uses browser automation to interact with LinkedIn. It requires:
- An active LinkedIn session in your browser
- Clawdbot's browser tool with `profile="chrome"` (uses your existing Chrome session) or `profile="clawd"` (isolated browser)

**Recommended:** Use `profile="chrome"` with the Chrome extension relay for seamless access to your logged-in LinkedIn session.

## Authentication

LinkedIn uses cookie-based sessions. Two approaches:

### Chrome Extension Relay (Recommended)
1. Click the Clawdbot Browser Relay toolbar icon on your LinkedIn tab
2. Badge turns ON = tab attached
3. Use `profile="chrome"` in browser commands

### Isolated Browser (clawd profile)
1. Use `profile="clawd"` to launch isolated browser
2. Navigate to LinkedIn and log in manually
3. Session persists until browser closes

## Quick Reference

| Action | Key Selectors / URLs |
|--------|---------------------|
| Feed | `linkedin.com/feed` |
| Notifications | `linkedin.com/notifications` |
| Messages | `linkedin.com/messaging` |
| My Profile | `linkedin.com/in/me` |
| Search | `linkedin.com/search/results/all/?keywords=...` |
| Post Modal | Click "Start a post" button |
| Connections | `linkedin.com/mynetwork` |

## Commands & Usage

### Check Notifications

```
# Navigate to notifications
browser action=navigate targetUrl="https://www.linkedin.com/notifications" profile="chrome"

# Take snapshot to read notifications
browser action=snapshot profile="chrome"
```

**What to look for:**
- Notification cards with sender name, action type, and timestamp
- Filter tabs: All, My Posts, Mentions

### Read Messages / Inbox

```
# Navigate to messaging
browser action=navigate targetUrl="https://www.linkedin.com/messaging" profile="chrome"

# Snapshot to see conversations
browser action=snapshot profile="chrome"

# Click on a conversation (use ref from snapshot)
browser action=act profile="chrome" request={"kind":"click","ref":"<conversation-ref>"}

# Read the full conversation thread
browser action=snapshot profile="chrome"
```

**Message structure:**
- Left sidebar: conversation list with names and previews
- Main area: active conversation thread
- Bottom: compose box

### Send a Message

```
# With conversation open, find the message input
browser action=snapshot profile="chrome"

# Type message (find the textbox ref)
browser action=act profile="chrome" request={"kind":"type","ref":"<message-input-ref>","text":"Hello! Thanks for connecting."}

# Press Enter or click Send
browser action=act profile="chrome" request={"kind":"press","key":"Enter"}
```

### Read Feed

```
# Navigate to feed
browser action=navigate targetUrl="https://www.linkedin.com/feed" profile="chrome"

# Snapshot to read posts
browser action=snapshot profile="chrome"

# Scroll for more content
browser action=act profile="chrome" request={"kind":"press","key":"PageDown"}
browser action=snapshot profile="chrome"
```

**Feed post structure:**
- Author name and headline
- Post content (text, images, videos, documents)
- Engagement counts (likes, comments, reposts)
- Action buttons: Like, Comment, Repost, Send

### View a Profile

```
# Navigate to profile by URL
browser action=navigate targetUrl="https://www.linkedin.com/in/username" profile="chrome"

# Or view your own profile
browser action=navigate targetUrl="https://www.linkedin.com/in/me" profile="chrome"

# Snapshot to read profile
browser action=snapshot profile="chrome"

# Scroll for experience, education, etc.
browser action=act profile="chrome" request={"kind":"press","key":"PageDown"}
browser action=snapshot profile="chrome"
```

**Profile sections:**
- Header: photo, name, headline, location, connection status
- About
- Experience
- Education
- Skills
- Recommendations

### Post Content (Text)

```
# Navigate to feed
browser action=navigate targetUrl="https://www.linkedin.com/feed" profile="chrome"

# Snapshot to find "Start a post" button
browser action=snapshot profile="chrome"

# Click "Start a post"
browser action=act profile="chrome" request={"kind":"click","ref":"<start-post-button-ref>"}

# Wait for modal and snapshot
browser action=snapshot profile="chrome"

# Type post content
browser action=act profile="chrome" request={"kind":"type","ref":"<post-textarea-ref>","text":"Excited to share my latest project! 🚀\n\nWe built an amazing tool that..."}

# Click Post button
browser action=act profile="chrome" request={"kind":"click","ref":"<post-button-ref>"}
```

### Post Content (With Image)

```
# After opening post modal, click media button (photo icon)
browser action=act profile="chrome" request={"kind":"click","ref":"<add-media-ref>"}

# Upload file
browser action=upload profile="chrome" paths=["/path/to/image.jpg"]

# Add text and post
browser action=act profile="chrome" request={"kind":"type","ref":"<post-textarea-ref>","text":"Check out this photo!"}
browser action=act profile="chrome" request={"kind":"click","ref":"<post-button-ref>"}
```

### Search People

```
# Navigate to search
browser action=navigate targetUrl="https://www.linkedin.com/search/results/people/?keywords=software%20engineer%20san%20francisco" profile="chrome"

# Snapshot results
browser action=snapshot profile="chrome"

# Click on a result to view profile
browser action=act profile="chrome" request={"kind":"click","ref":"<person-result-ref>"}
```

**Search filters available:**
- People: `/search/results/people/`
- Companies: `/search/results/companies/`
- Jobs: `/search/results/jobs/`
- Posts: `/search/results/content/`
- Groups: `/search/results/groups/`

### Search Companies

```
# Navigate to company search
browser action=navigate targetUrl="https://www.linkedin.com/search/results/companies/?keywords=artificial%20intelligence" profile="chrome"

# Snapshot to read results
browser action=snapshot profile="chrome"

# Click company to view page
browser action=act profile="chrome" request={"kind":"click","ref":"<company-ref>"}
```

### Send Connection Request

```
# On someone's profile, find Connect button
browser action=snapshot profile="chrome"

# Click Connect
browser action=act profile="chrome" request={"kind":"click","ref":"<connect-button-ref>"}

# Optional: Add a note
browser action=snapshot profile="chrome"
browser action=act profile="chrome" request={"kind":"click","ref":"<add-note-button-ref>"}
browser action=act profile="chrome" request={"kind":"type","ref":"<note-textarea-ref>","text":"Hi! I enjoyed your recent post about AI. Would love to connect!"}

# Send request
browser action=act profile="chrome" request={"kind":"click","ref":"<send-button-ref>"}
```

### Manage Connection Requests

```
# Navigate to network page
browser action=navigate targetUrl="https://www.linkedin.com/mynetwork/invitation-manager/" profile="chrome"

# Snapshot to see pending requests
browser action=snapshot profile="chrome"

# Accept or ignore requests
browser action=act profile="chrome" request={"kind":"click","ref":"<accept-button-ref>"}
```

### Like a Post

```
# Find the Like button on a post
browser action=snapshot profile="chrome"

# Click Like
browser action=act profile="chrome" request={"kind":"click","ref":"<like-button-ref>"}
```

### Comment on a Post

```
# Click the Comment button to open comment box
browser action=act profile="chrome" request={"kind":"click","ref":"<comment-button-ref>"}

# Snapshot to find comment input
browser action=snapshot profile="chrome"

# Type comment
browser action=act profile="chrome" request={"kind":"type","ref":"<comment-input-ref>","text":"Great insights! Thanks for sharing."}

# Submit comment (Enter or click Post)
browser action=act profile="chrome" request={"kind":"press","key":"Enter"}
```

## URL Patterns

| Page | URL Pattern |
|------|-------------|
| Feed | `linkedin.com/feed` |
| Profile | `linkedin.com/in/{username}` |
| Company | `linkedin.com/company/{company-slug}` |
| Job | `linkedin.com/jobs/view/{job-id}` |
| Search People | `linkedin.com/search/results/people/?keywords={query}` |
| Search Companies | `linkedin.com/search/results/companies/?keywords={query}` |
| Search Jobs | `linkedin.com/search/results/jobs/?keywords={query}` |
| Messages | `linkedin.com/messaging` |
| Specific Chat | `linkedin.com/messaging/thread/{thread-id}` |
| Notifications | `linkedin.com/notifications` |
| My Network | `linkedin.com/mynetwork` |
| Invitations | `linkedin.com/mynetwork/invitation-manager/` |
| Settings | `linkedin.com/psettings/` |

## Tips & Best Practices

### Rate Limiting
LinkedIn actively monitors automation. To avoid restrictions:
- Add delays between actions (1-3 seconds)
- Don't spam connection requests
- Vary your activity patterns
- Keep session active but not hyperactive

### Finding Elements
Use `browser action=snapshot` liberally. LinkedIn's UI is dynamic:
- Modals appear/disappear
- Infinite scroll loads new content
- Elements may have dynamic refs

### Handling Popups
LinkedIn shows various popups (premium ads, surveys, etc.):
```
# Look for close/dismiss buttons in snapshot
browser action=snapshot profile="chrome"
browser action=act profile="chrome" request={"kind":"click","ref":"<dismiss-button-ref>"}
```

### Session Management
- Chrome profile: Session persists across browser closes
- Clawd profile: Session lost when browser closes; must re-login

### Multi-Language Support
LinkedIn UI adapts to user language settings. Element text will match your profile language.

## Workflow Examples

### Daily Check Routine
```
1. browser action=navigate targetUrl="https://www.linkedin.com/notifications" profile="chrome"
2. browser action=snapshot profile="chrome"
   → Read and report notifications
3. browser action=navigate targetUrl="https://www.linkedin.com/messaging" profile="chrome"
4. browser action=snapshot profile="chrome"
   → Report unread messages
5. browser action=navigate targetUrl="https://www.linkedin.com/feed" profile="chrome"
6. browser action=snapshot profile="chrome"
   → Summarize top posts
```

### Research a Company
```
1. browser action=navigate targetUrl="https://www.linkedin.com/company/openai" profile="chrome"
2. browser action=snapshot profile="chrome"
   → Company overview
3. browser action=act profile="chrome" request={"kind":"click","ref":"<people-tab-ref>"}
4. browser action=snapshot profile="chrome"
   → See employees
```

### Find and Connect with People
```
1. browser action=navigate targetUrl="https://www.linkedin.com/search/results/people/?keywords=product%20manager%20fintech" profile="chrome"
2. browser action=snapshot profile="chrome"
   → Review results
3. For each interesting profile:
   a. Click to open profile
   b. Review their background
   c. Send connection request with personalized note
```

## Troubleshooting

### "Not logged in" or login page shown
- Ensure you're logged into LinkedIn in your browser
- For Chrome relay: re-attach the tab (click toolbar icon)
- For clawd profile: navigate to LinkedIn and log in

### Elements not found
- LinkedIn's DOM is complex; re-snapshot after any navigation
- Modal states change available elements
- Try scrolling to load more content

### Actions not working
- LinkedIn may have updated their UI
- Check if a modal is blocking interaction
- Verify the correct ref from latest snapshot

### Rate limited or restricted
- Slow down your automation
- Wait a few hours before resuming
- Don't mass-send connection requests

---

**TL;DR**: Use `profile="chrome"` with attached tab, navigate via URLs, snapshot to read, click/type to interact. Be gentle with rate limits. 💼
