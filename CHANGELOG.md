# Changelog

All notable changes to FastAPI are documented in the
[full release notes](https://fastapi.tiangolo.com/release-notes/).

This file provides a high-level summary of recent releases. For the complete
history including all bug fixes, documentation updates, translations, and
internal changes, see [docs/en/docs/release-notes.md](docs/en/docs/release-notes.md).

## 0.141.1 (2026-07-29)

### Fixes

- Fix support for background tasks and headers from dependencies in `app.frontend()`.

### Docs

- Document `FASTAPI_ENV` in FastAPI CLI guide.

## 0.141.0 (2026-07-29)

### Features

- Add `app.frontend(check_dir="auto")`, to make local development more convenient with `fastapi dev`.

## 0.140.13 (2026-07-28)

### Fixes

- Fix `status_code` being ignored for SSE and JSONL streaming endpoints.

### Docs

- Fix `format_sse_event` docstring rendering of `\n\n` terminator.
- Add API reference page for `fastapi.sse`.

## 0.140.12 (2026-07-25)

### Fixes

- Fix SSE event parsing when data contains colons.

## 0.140.11 (2026-07-24)

### Fixes

- Fix frontend router to properly handle static file serving with custom paths.

---

For older releases, see the [full release notes](https://fastapi.tiangolo.com/release-notes/).
