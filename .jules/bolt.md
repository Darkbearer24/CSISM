## 2024-05-22 - Broken React Environment
**Learning:** The repository contains a React structure (`src/`) but is missing `package.json` and `src/main.tsx`. The live site seems to be `public/index.html` (verified via `vercel.json` routing). `CSISM/` folder which is supposed to contain static assets is empty.
**Action:** Focused optimization efforts on `public/index.html` as it is the only functional part of the codebase. Verification must be done on the static HTML, not the React app.

## 2024-05-22 - Broken Python Handler & Cold Start
**Learning:** `api/enquiry.py` contained duplicate `send_email` definitions, causing the active one to fail with `UnboundLocalError` (missing global declaration) and `NameError` (scope issues). Also, environment variables were loaded on every request.
**Action:** Refactored to single `send_email`, fixed scope, and moved config to module-level constants for cold start optimization. Always check for duplicate function definitions in legacy files.
