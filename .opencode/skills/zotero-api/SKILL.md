---
name: zotero-api
description: Guide for Zotero client-side JavaScript API. Use for running JS inside Zotero, developing plugins, or accessing the local database. NOT for Web API, Translators, SQLite, or Connector HTTP Server.
---

# Zotero Client JavaScript API

Internal API for code running inside the Zotero desktop application.

## Documentation

- **[JavaScript API](https://www.zotero.org/support/dev/client_coding/javascript_api)** - Internal API reference
- **[Plugin Development](https://www.zotero.org/support/dev/client_coding/plugin_development)** - Plugin guide
- **[Client Coding](https://www.zotero.org/support/dev/client_coding)** - All client dev options

## Other Client APIs

- **[SQLite Access](https://www.zotero.org/support/dev/client_coding/direct_sqlite_database_access)** - Direct database access (read-only recommended)
- **[Connector HTTP Server](https://www.zotero.org/support/dev/client_coding/connector_http_server)** - For browser connector communication
- **Word Processor APIs** - [LibreOffice](https://github.com/zotero/zotero-libreoffice-integration/), [Word Win](https://github.com/zotero/zotero-word-for-windows-integration), [Word Mac](https://github.com/zotero/zotero-word-for-mac-integration)

## Source

- **Repo**: https://github.com/zotero/zotero
- **Data**: `chrome/content/zotero/xpcom/data/`
- **UI**: `chrome/content/zotero/`

## Architecture

| Scope | Object | Purpose |
|-------|--------|---------|
| Window | `ZoteroPane` | UI interactions |
| Non-Window | `Zotero` | Database operations |

Extension access:
```html
<script src="chrome://zotero/content/include.js"></script>
```

## Notes

- API is under-documented; check source code when needed
- Back up data before batch operations
- Disable auto-sync during scripts
