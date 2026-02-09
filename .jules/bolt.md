## 2024-05-22 - Broken React Environment
**Learning:** The repository contains a React structure (`src/`) but is missing `package.json` and `src/main.tsx`. The live site seems to be `public/index.html` (verified via `vercel.json` routing). `CSISM/` folder which is supposed to contain static assets is empty.
**Action:** Focused optimization efforts on `public/index.html` as it is the only functional part of the codebase. Verification must be done on the static HTML, not the React app.

## 2024-05-22 - Serverless State Management Pitfall
**Learning:** The Python handler `api/enquiry.py` attempted to reuse a global SMTP connection but failed to declare `global _smtp_client` before checking it, causing `UnboundLocalError`. Also, environment variables were being fetched inside the function scope, which is inefficient.
**Action:** Always verify variable scope when implementing "warm start" optimizations in serverless functions. Move immutable configuration (like env vars) to module scope to benefit from caching.
