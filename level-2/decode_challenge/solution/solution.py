import base64
m='aG9zdG5hbWVfbGlzdD1nZXRfaG9zdG5hbWVfZnJvbV9zaGEocXVlcnlfcGFyYW1zPWFtcF9xdWVyeV9wYXJhbXMp'
decoded_text = base64.b64decode(m).decode('utf-8')
print()
print(decoded_text)