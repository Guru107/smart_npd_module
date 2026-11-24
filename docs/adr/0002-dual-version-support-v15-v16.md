# 2. Support Frappe v15 and v16 on a single Python 3.14 floor

## Status

Accepted; Python floor amended to 3.13 (2026-11-24, see Amendment).

## Context

The starter targets both Frappe v15 (supported upstream until end-2027) and
v16 (current stable). The two majors have divergent runtime baselines: v15's
CI tests only Python 3.10 / Node 18 (its pyproject allows `>=3.10,<3.15`),
while v16 requires exactly Python 3.14 / Node 24. The test infrastructure
also diverged: v15 offers only `FrappeTestCase` (`frappe.tests.utils`), while
v16 replaced it with `UnitTestCase`/`IntegrationTestCase` (`frappe.tests`),
keeping the old class only as a deprecated shim scheduled for removal in v17.

The options were: (a) drop the Python floor to `>=3.10` and ruff
`target-version = "py310"` so the same code runs on v15's tested baseline;
(b) keep `requires-python = ">=3.14"` and ruff `py314`, running v15 on Python
3.14 — allowed by v15's pyproject but never exercised by v15's own CI;
(c) drop v15 support.

## Decision

Option (b): one Python floor (3.14), one ruff target (`py314`), and a
two-leg CI matrix (`version-15` + `version-16`, both on Python 3.14 /
Node 24). Cross-version code differences — starting with the test base
class — are handled by version-conditional shims inside the starter (an
app-level `SmartNPDModuleTestSuite` that imports `IntegrationTestCase` when
available and falls back to `FrappeTestCase`), plus `semantic_version`
runtime gates where the Marketplace guidelines prescribe them.

## Consequences

- The v15 CI leg runs a Python/MariaDB/Node combination that Frappe's own
  v15 CI never tests. That leg is our compatibility evidence, not upstream's;
  if it fails for framework reasons (not app reasons), v15 support gets
  re-scoped rather than worked around in app code.
- Consumers on genuine legacy stacks (Python 3.10) are not served; they can
  pin an earlier release of the starter or fork.
- If Frappe EOLs v15 (planned end-2027), the v15 leg and its shims are
  deleted, not extended.

## Amendment (2026-11-24): Python floor 3.13

The Smart NPD Module's v15 deployment bench runs Python 3.13, and an app with
`requires-python = ">=3.14"` does not install there. The floor is now 3.13:
`requires-python = ">=3.13"`, ruff `py313`, mypy `python_version = "3.13"`. The CI
`version-15` leg runs Python 3.13, `version-16` runs 3.14 (v16 requires it). The
test-base-class shim and the rest of this decision are unchanged.
