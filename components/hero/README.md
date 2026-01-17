# Hero Component (BEM, Accessible, Mobile-First)

## Files
- `hero.html` — semantic structure with ARIA and headings
- `hero.css` — component-scoped styles using BEM naming
- `hero.js` — progressive enhancement for smooth reveal

## Features
- Mobile-first responsive layout
- Accessible: clear heading (`h1`), strong contrast, focus-visible on CTA
- Keyboard friendly: CTA focus styles; reduced-motion respected
- Cross-browser compatible

## Usage
1. Copy markup from `hero.html` to your page where the hero should appear.
2. Append styles from `hero.css` to your global stylesheet or link separately.
3. Include `hero.js` if you want the reveal animation enhancement.

## Testing
- Validate HTML/CSS with W3C tools
- Screen reader: ensure hero title announces correctly
- Responsive: verify at 360px, 768px, 1024px, 1280px+
- Browser: Chrome, Firefox, Safari, Edge

