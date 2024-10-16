
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.lower() if c.isupper() else c.upper() if c.islower() else c for c in s)
