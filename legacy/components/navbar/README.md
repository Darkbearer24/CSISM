# Navbar Component (BEM, Accessible, Mobile-First)

## Files
- `navbar.html` — semantic HTML5 structure with ARIA attributes
- `navbar.css` — component-scoped styles using BEM naming
- `navbar.js` — progressive enhancement for toggling and keyboard support

## Features
- Mobile-first responsive layout with sticky top bar
- Accessible: `role="navigation"`, `aria-label`, `aria-controls`, `aria-expanded`
- Keyboard support: Escape to close, focus management on open
- BEM naming for modularity and reuse
- Cross-browser compatible and reduced-motion support

## Usage
1. Copy the content of `navbar.html` into your page near the `<body>` top.
2. Include styles:
   - Option A: Append `navbar.css` into your global stylesheet.
   - Option B: Link `navbar.css` as a separate stylesheet.
3. Include script:
   - Option A: Inline a small script adapted from `navbar.js`.
   - Option B: Bundle `navbar.js` in your assets pipeline.

## States
- Hover, focus-visible styles for links and buttons
- `aria-expanded="true"` on toggle opens menu (`data-open="true"` on menu)

## Testing
- Validate HTML/CSS with any W3C validator
- Screen reader check (NVDA, VoiceOver)
- Responsive check: 360px, 768px, 1024px, 1280px+
- Browser check: Chrome, Firefox, Safari, Edge

## Notes
- Keep brand image alt text descriptive
- Ensure color contrast ratios meet WCAG AA

