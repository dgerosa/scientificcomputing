import requests

username = "dgerosa"
prefix = "astrostatistics_bicocca_"
current_year = 2024   # starting point, can be current or last known year
max_year = 2100       # safety max to avoid infinite loops

def find_latest_year(prefix, current_year, max_year, username):
    latest_year = current_year
    for year in range(current_year + 1, max_year + 1):
        repo_name = f"{prefix}{year}"
        url = f"https://api.github.com/repos/{username}/{repo_name}"
        response = requests.get(url)
        if response.status_code == 200:
            latest_year = year
        else:
            break
    return latest_year

latest_year = find_latest_year(prefix, current_year, max_year, username)
latest_repo = f"{prefix}{latest_year}"
redirect_url = f"https://github.com/{username}/{latest_repo}"

print(f"Latest repo found: {latest_repo}")

html = f"""<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Redirecting...</title>
    <meta http-equiv="refresh" content="0; url={redirect_url}" />
    <style>
      body {{
        font-family: sans-serif;
        margin-top: 2em;
        color: #333;
      }}
    </style>
  </head>
  <body>
    <p>Redirecting you to <a href="{redirect_url}">{redirect_url}</a>...</p>
  </body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

print(f"index.html generated with redirect to {redirect_url}")