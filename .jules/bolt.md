## 2024-05-22 - Broken React Environment
**Learning:** The repository contains a React structure (`src/`) but is missing `package.json` and `src/main.tsx`. The live site seems to be `public/index.html` (verified via `vercel.json` routing). `CSISM/` folder which is supposed to contain static assets is empty.
**Action:** Focused optimization efforts on `public/index.html` as it is the only functional part of the codebase. Verification must be done on the static HTML, not the React app.
