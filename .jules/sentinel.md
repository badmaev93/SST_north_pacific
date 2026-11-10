## 2024-05-15 - XSS in HTML mapping tooltips
**Vulnerability:** XSS vulnerability in mapping tooltips via unsanitized properties (`nodataMsg`, `unit`, `lat`, `lon`, `val`).
**Learning:** Even internal mapping values and formatting labels can introduce DOM-based XSS when injected directly with `innerHTML`.
**Prevention:** Use `textContent` and standard DOM creation methods for element properties that accept dynamic strings.
## 2023-11-06 - Supply Chain Attack Prevention
**Vulnerability:** Third-party scripts were loaded via a CDN (`cdn.jsdelivr.net`) using unpinned major versions (`@7`, `@3`) and lacked Subresource Integrity (SRI) attributes (`integrity`, `crossorigin`).
**Learning:** This exposes the application to supply-chain attacks if the CDN is compromised or if a malicious version is published, as the browser would automatically execute the unverified script.
**Prevention:** Always pin exact versions for external scripts and include the `integrity` attribute with the cryptographic hash of the expected file content, along with `crossorigin="anonymous"`.
## 2024-05-16 - Unsupported Meta Tag Security Headers
**Vulnerability:** Adding `X-Content-Type-Options` as a meta tag.
**Learning:** Security headers like `X-Content-Type-Options: nosniff` cannot be implemented using `<meta http-equiv="X-Content-Type-Options">` tags in HTML, as modern browsers only respect them when delivered as actual HTTP response headers.
**Prevention:** Avoid adding unsupported security headers as meta tags in static HTML environments, as it constitutes security theater without real benefit.
