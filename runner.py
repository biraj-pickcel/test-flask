import sys
import subprocess

# WHO IS THE HOST [ values: gunicorn | streamlit | flask-dev ]
host = sys.argv[1] if len(sys.argv) > 1 else "flask"

if host == "flask":
    subprocess.run(["pipenv", "run", "flask", "--app", "./app", "run"])
elif host == "flask-dev":
    subprocess.run(["pipenv", "run", "flask", "--app", "./app", "--debug", "run"])
else:
    print(f"unknown host '{host}'")
    exit(1)
