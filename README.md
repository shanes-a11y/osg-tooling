# osg-tooling

Tooling and automation for the OSG Lead Mentor workspace.

## Keep Alive CI

Prevents [osgboutiquehunter.streamlit.app](https://osgboutiquehunter.streamlit.app) from going to sleep due to inactivity.

Streamlit Community Cloud hibernates apps after ~12 hours of no traffic. A plain HTTP request is not enough — the app renders via WebSocket, so a headless Chromium browser is used to simulate a real visit.

**Schedule:** every 6 hours (00:00, 06:00, 12:00, 18:00 UTC)

**How it works:**
1. Playwright launches a headless Chromium browser and visits the app URL
2. Waits 8 seconds for Streamlit to fully render via WebSocket
3. Checks the rendered page body for error indicators (`"Oh no"`, `"Error running app"`)
4. Fails the job (triggering a GitHub email notification) if an error is detected

**Manual trigger:** Actions → Streamlit Keep Alive → Run workflow
