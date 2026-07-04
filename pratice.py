import requests


def greet(who_to_greet):
    """Return a greeting for the given name."""

    greeting = f"hello, {who_to_greet}"
    return greeting


print(greet("world"))
print(greet("amey"))

r = requests.get("https://coreyms.com", timeout=10)
print(r.status_code)
