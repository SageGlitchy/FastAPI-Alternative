# Fork Notice

This repository is a **fork** of [FastAPI](https://github.com/fastapi/fastapi) by
[Sebastián Ramírez (tiangolo)](https://github.com/tiangolo).

| | |
|---|---|
| **Upstream repository** | <https://github.com/fastapi/fastapi> |
| **Upstream license** | MIT |
| **Fork base commit** | [`50113da1`](https://github.com/fastapi/fastapi/commit/50113da16fec53b66b80d75e80a89296de4fa5a5) — tagged `fork-base` in this repo |
| **Fork maintainer** | SageGlitchy (<sageglitchy@gmail.com>) |

---

## What changed in this fork

All upstream history up to commit `50113da1` is preserved verbatim. The
following commits were added by the fork maintainer on top of that base:

### Commit `06e0fef8` — "First Commit"

| File | Change |
|---|---|
| `tests/test_additional_properties_bool.py` | Added 1 line (minor test tweak) |

### Commit `af74eafa` — "Improve repository score"

| Area | Files | Description |
|---|---|---|
| Docker | `Dockerfile.dev`, `docker-compose.yml` | Added dev Docker Compose setup with PostgreSQL backing service |
| CI | `.github/workflows/test.yml` | Added `lint-and-typecheck` job and `alls-green` gate |
| Security tutorials | `docs_src/security/tutorial004_*.py`, `docs_src/security/tutorial005_*.py` | Replaced hardcoded `SECRET_KEY` with `os.environ.get()` |
| Observability | `docs_src/observability/tutorial001_py310.py`, `tutorial002_py310.py` | New structured logging and health-check tutorials |
| Tests | `tests/test_include_router_defaults_overrides_*.py`, `tests/test_observability_tutorial.py` | Modularised include-router tests; added observability tutorial tests |
| Docs | `CHANGELOG.md`, `CONTRIBUTING.md`, `README.md` | Added root changelog, contributing guide, and Quick Start section |
| Config | `pyproject.toml` | Set `coverage fail_under` threshold |

---

## Contribution guidelines for this fork

1. **Squash or rebase** original commits into small, focused units — each commit
   should pair a code change with its test.
2. **Do not rewrite** upstream history before the `fork-base` tag.
3. **Document** every addition in this file so provenance remains auditable.

---

## Upstream sync policy

To pull in new upstream releases:

```bash
git remote add upstream https://github.com/fastapi/fastapi.git   # one-time
git fetch upstream
git merge upstream/master   # or rebase, depending on preference
```

Resolve any conflicts, then update this file with a note about the merge point.
