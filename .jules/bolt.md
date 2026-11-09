## 2024-06-25 - Using 32-bit ArrayBuffer views for canvas pixel manipulation
**Learning:** When manipulating `ImageData` in HTML Canvas, updating individual R, G, B, and A channels via the `Uint8ClampedArray` (e.g. `img.data[p] = r; img.data[p+1] = g; ...`) is slow due to array bounds checking and multiple assignments per pixel. Additionally, conditional branching inside per-pixel loops severely degrades performance in V8/SpiderMonkey.
**Action:** Instead, cast the `img.data.buffer` to a `Uint32Array` (e.g. `new Uint32Array(img.data.buffer)`) and use a precomputed 32-bit color look-up table (LUT) to assign the entire pixel in a single operation: `img32[i] = LUT32[raw[i]]`. Account for system endianness when precomputing the 32-bit integer colors. This eliminates branching and reduces assignments by 75%.

## 2025-01-20 - Memoizing D3 paths and topojson meshes for small multiples
**Learning:** In a dashboard with hundreds of small multiples (maps) of identical dimensions, computing the geographical topology mesh (`topojson.mesh`) and evaluating the D3 path (`d3.geoPath().projection()`) repeatedly for each canvas element becomes a massive CPU bottleneck, as stringifying complex SVG paths takes significant time.
**Action:** Extract the result of `topojson.mesh` to a global variable so it's only computed once. More importantly, cache the resulting SVG path `d` string keyed by the dimensions of the map (`pw` x `ph`). Subsequent maps of the same size simply reuse the cached string, completely skipping projection and path generation for subsequent multiples.

## 2025-01-20 - Reusing Canvas and ImageData objects to reduce GC pressure
**Learning:** In a dashboard with frequent canvas rendering (especially during timeline animations like `paintAnom` called every 600ms), creating a new `canvas` and `ImageData` buffer on every call results in thousands of allocations and severe garbage collection pressure, leading to jank.
**Action:** Declare scoped variables for the temporary offscreen canvas, 2D context, and `ImageData`. Instantiate them only once on the first call and reuse them for all subsequent paints. Since the maps in this application have fixed dimensions (`NLON`x`NLAT` for standard, `ANOM_NLON`x`ANOM_NLAT` for anomalies), the same shared buffer can be reused safely.

## 2025-01-20 - Reusing DOM elements in high-frequency event handlers
**Learning:** The `setTooltipContent` function was dynamically creating new DOM elements (`b`, `br`, `span`) and setting `innerHTML` on every `mousemove` event across the maps. This continuous allocation and deallocation of DOM nodes creates significant Garbage Collection (GC) pressure, causing the main thread to block and resulting in UI jank.
**Action:** Extract DOM element creation outside of high-frequency event handlers. Initialize the structural DOM nodes once when their container is created, and only update their `textContent` (or `style`) inside the event handler to eliminate unnecessary GC pauses.
