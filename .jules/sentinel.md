## 2024-05-15 - XSS in HTML mapping tooltips
**Vulnerability:** XSS vulnerability in mapping tooltips via unsanitized properties (`nodataMsg`, `unit`, `lat`, `lon`, `val`).
**Learning:** Even internal mapping values and formatting labels can introduce DOM-based XSS when injected directly with `innerHTML`.
**Prevention:** Use `textContent` and standard DOM creation methods for element properties that accept dynamic strings.
