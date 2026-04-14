# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| 4.0+ (main branch) | ✅ |
| < 4.0 | ❌ |

## Reporting a Vulnerability

If you discover a security vulnerability in this course's content or infrastructure, please report it responsibly:

### What to Report

- **Code examples with security anti-patterns**: Hardcoded credentials, API keys, or secrets in educational examples
- **Dependency vulnerabilities**: Known CVEs in `requirements.txt`
- **Infrastructure issues**: Exposed secrets, misconfigured CI/CD, or unauthorized access vectors
- **Content vulnerabilities**: Examples that teach insecure practices without proper warnings

### How to Report

1. **DO NOT** open a public GitHub issue for security vulnerabilities
2. Email the instructor directly: **dsaavedra88@gmail.com**
3. Include in your report:
   - Description of the vulnerability
   - File path and line number
   - Steps to reproduce (if applicable)
   - Suggested fix (optional)

### Response Timeline

| Severity | Response Time | Resolution Target |
|----------|--------------|-------------------|
| Critical (exposed secrets) | 24 hours | 48 hours |
| High (CVE in dependencies) | 48 hours | 1 week |
| Medium (educational anti-pattern) | 1 week | 2 weeks |
| Low (documentation improvement) | 2 weeks | 1 month |

### Scope

This policy covers:
- All course content (`content/`, `labs/`, `quizzes/`)
- Infrastructure configuration (`.github/workflows/`, `_quarto.yml`)
- Dependencies (`requirements.txt`)
- Generated content (`docs/`)

This policy does NOT cover:
- Third-party platform vulnerabilities (Exercism, HackerRank, etc.)
- Browser or OS-level security issues
- Issues in dependencies of dependencies (transitive deps)

## Security Best Practices for Students

When working through this course:

1. **NEVER commit API keys or secrets** to version control
2. **Use `.env` files** for sensitive configuration (see `.env.example`)
3. **Keep dependencies updated** — run `pip-audit` regularly
4. **Use strong passwords** in exercises — never reuse real credentials
5. **Work in isolated environments** — virtual environments, sandbox VMs

---

**Last updated**: 2026-04-13  
**Contact**: dsaavedra88@gmail.com
