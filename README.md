# job-scraper-bot

Daily scraper for entry-level software developer jobs at startups.  
Run every day at 12 PM CST, emails job openings to your inbox.

## Setup

1. **Create GitHub repo** named `job-scraper-bot`.  
2. Copy the project files above into the repo.  
3. On GitHub, go to **Settings → Secrets and variables → Actions**:
   - TODO: Add `EMAIL_ADDRESS` (your Gmail)
   - TODO: Add `EMAIL_PASSWORD` (Gmail App Password)
4. Commit and push. Workflow will run automatically at noon CST!

## Extend

- Scrape additional sites (YC, LinkedIn, etc.)
- Improve parsing with pagination or filtering
- Send via Slack or SMS
