DANGEROUS_MARKERS = ["ignore previous", "reveal system prompt", "exfiltrate", "disable security"]

def scan_untrusted_text(text: str) -> list[str]:
    low=text.lower(); return [m for m in DANGEROUS_MARKERS if m in low]

def requires_approval(permission: str) -> bool:
    return permission in {"write", "admin", "financial"}
