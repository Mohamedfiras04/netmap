import platform
import subprocess

def is_active(ip):
    system = "-n" if platform.system() == "Windows" else "-c"
    test = subprocess.run(["ping", system, "1", ip],
        capture_output=True, text=True,
        encoding="utf-8", errors="ignore")       # ← Encoding + Fehler ignorieren!
    if test.stdout is None:                        # ← falls leer
        return False
    print ("TTL" in test.stdout)
    return "TTL" in test.stdout              # "TTL" nur bei echter Antwort!
# Teste eine IP, bei der SICHER KEIN Gerät ist:
is_active("192.168.0.99")