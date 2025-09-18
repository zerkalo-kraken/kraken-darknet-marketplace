import requests

def where_am_i():
    try:
        response = requests.get("https://ipinfo.io/json", timeout=5)
        data = response.json()
        loc = data.get("city", "неизвестно") + ", " + data.get("country", "?")
        print("Ты сейчас в:", loc, "🌍")
    except Exception:
        print("Не удалось определить местоположение (но ты точно где-то в матрице)")

# where_am_i()
