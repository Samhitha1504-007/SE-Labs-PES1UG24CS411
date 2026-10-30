# Issues Found and Fixed

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell injection (B605) | Security - High | 56 | `os.system()` builds a shell command using the filename | Replaced with a normal `print()` |
| Weak hash (B324) | Security - High | 45 | MD5 is not secure | Changed to `hashlib.sha256` |
| Use of eval (B307) | Security - Medium | 40 | `eval()` can run any code passed to it | Pass a number (`tax_multiplier`) and multiply instead |
| Mutable default arg | Bug | 13 | `intake_log=[]` is shared across calls | Default to `None` and create the list inside the function |
| Bare except with pass | Bug | 24-25 | All errors are silently ignored | Catch only `KeyError` and return `False` |
| Line too long / no newline at end | Style | 7-9, 16, 72, 80 | PEP 8 violations from Flake8 | Split long lines, added final newline |