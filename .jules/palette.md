## 2024-03-24 - Semantic Landmarks & Accessible Sliders
**Learning:** Using generic `<div>` tags for major page sections (sidebar, main content area, footer controls) prevents screen readers from understanding the page structure. Furthermore, range sliders that use index values internally announce useless numbers (0, 1, 2) instead of the actual data (e.g., years) unless `aria-valuetext` is dynamically updated.
**Action:** Replace structural `<div>`s with `<nav>`, `<main>`, and `<footer>` where appropriate. When a range input acts as an array index selector, always update its `aria-valuetext` via JS so screen readers announce the semantic value (e.g., the year).

## 2024-11-10 - Skip-to-content Link and Keyboard Scrolling Support
**Learning:** In a single-page application with a fixed sidebar or header, keyboard users can be forced to tab through many non-essential interactive elements (like the sidebar) before reaching the primary content. Moreover, a scrollable container (e.g., `overflow-y: scroll`) without focusable elements cannot be scrolled via the keyboard, rendering its content inaccessible to keyboard-only users.
**Action:** Always include a hidden-by-default, focusable skip-to-content link (`<a href="#main-id" class="skip-link">`) at the beginning of the `<body>`. Additionally, always add `tabindex="0"` to the main scrollable content area so it can be focused and scrolled with arrow keys or Page Down/Up. Provide clear `:focus-visible` styling for the container to orient the user.

## 2024-11-13 - Focusable Disabled Elements
**Learning:** Native `disabled` attributes on interactive elements (like buttons) completely remove them from the keyboard focus order and prevent mouse events. This means screen reader and keyboard-only users cannot navigate to them to discover they exist, let alone trigger hover/focus tooltips explaining *why* they are disabled.
**Action:** Instead of using the native `disabled` attribute, use `aria-disabled="true"`. Update styling to target `[aria-disabled="true"]` and update JavaScript logic to prevent the action if `aria-disabled` is true, ensuring the element remains keyboard focusable.
