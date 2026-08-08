
---

# 9. `docs/SECURITY.md`

Because you're building a scraper, **this one is not optional** if you want production-quality engineering.

```markdown
# Security Requirements

## 1. SSRF Protection

The scraper must never be allowed to access internal services.

Block:

```text
localhost
127.0.0.1
0.0.0.0
::1
private IPv4 ranges
private IPv6 ranges
link-local addresses
cloud metadata endpoints