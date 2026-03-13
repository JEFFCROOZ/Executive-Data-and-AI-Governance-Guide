# Changelog

All notable changes to **The Data Leader** app are documented here.

---

## [1.2.0] — 2026-03-13

### Fixed — Module & Section Navigation State Reset

**Problem:** Clicking "Mark as Complete" or "Next Module →" on any Learning Path module caused the app to return to the Home screen instead of staying on the Learning Path.

**Root cause:** The sidebar radio widget was being re-initialised with `index=0` on every rerun unless a `nav_jump` key was explicitly set in session state. This meant any interaction that triggered a rerun — including progress tracking and module advancement — silently reset the active section to Home.

**Fix:**
- Gave the sidebar radio a persistent `key="_nav_radio"` so Streamlit preserves its value across reruns automatically.
- Applied `nav_jump` only when the Home screen CTA buttons are clicked, using a direct session state assignment (`st.session_state["_nav_radio"] = _nav_options[...]`) rather than an index override.
- Replaced the module selectbox `index=` pattern with the same keyed approach (`key="_module_select"`), so "Next Module →" correctly advances the dropdown without triggering a section reset.

**Affected interactions — all now confirmed working:**
| Interaction | Before | After |
|---|---|---|
| Mark as Complete | Returned to Home | Stays on current module ✓ |
| Next Module → | Returned to Home | Advances to next module ✓ |
| Mark Incomplete | Returned to Home | Stays on current module ✓ |
| Module selectbox change | Worked | Still works ✓ |

---

## [1.1.0] — 2026-03-13

### Added — Home Screen Navigation & Sidebar Re-expand Fix

**Problem:** Once the sidebar was collapsed via the `‹‹` arrow, there was no way to bring it back or navigate to another section. The Home screen had no escape hatch.

**Fix 1 — Sidebar re-expand arrow always visible:**
- Added explicit CSS targeting `[data-testid="collapsedControl"]` with `display: flex !important` and `visibility: visible !important` to prevent it from being swallowed by the existing Streamlit chrome-hiding rules (`header { visibility: hidden }`).
- Styled the expand arrow to match the dark sidebar theme (`var(--ink)` background, `#e2e8f0` icon stroke).

**Fix 2 — Home screen CTA buttons:**
- Added **📚 Start Learning** and **⚡ Quick Reference** buttons directly on the Home screen below the intro text.
- Both buttons write to `st.session_state["nav_jump"]` and call `st.rerun()`, driving the sidebar radio to the correct section without requiring the sidebar to be open.
- Used `st.session_state.pop()` so the jump fires once and clears itself, keeping the radio widget in sync on subsequent reruns.

---

## [1.0.0] — 2026-03-13

### Initial Release

- 5 learning modules covering Data Governance foundations, org structure, core problems, culture, and future frontiers — scoped to the sports & entertainment industry.
- 4 Quick Reference cards: Governance Vocabulary, Regulatory Guide, Maturity Signals, and Executive Conversation Questions.
- Dark sidebar navigation with per-module progress tracking and completion state.
- Custom CSS design system (DM Serif Display / DM Sans, card components, badge pills, reference tables).
- Streamlit Cloud-ready configuration (`.streamlit/config.toml`).
