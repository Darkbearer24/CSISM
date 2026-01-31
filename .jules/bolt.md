## 2024-05-22 - Broken React Environment
**Learning:** The repository contains a React structure (`src/`) but is missing `package.json` and `src/main.tsx`. The live site seems to be `public/index.html` (verified via `vercel.json` routing). `CSISM/` folder which is supposed to contain static assets is empty.
**Action:** Focused optimization efforts on `public/index.html` as it is the only functional part of the codebase. Verification must be done on the static HTML, not the React app.

## 2026-01-31 - Duplicate Functions in Serverless Handler
**Learning:** `api/enquiry.py` contained duplicate definitions of `send_email`. The second one overwrote the first but relied on local variables from the first (which were lost), causing `UnboundLocalError`. This highlights the danger of copy-paste refactoring in Python files without proper linting.
**Action:** Always check for duplicate function definitions in legacy Python files. When refactoring serverless handlers, verify global/local variable scope carefully, especially for connection reuse patterns.
