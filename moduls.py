import questionary
import webbrowser

secim = questionary.select(
    "MODÜL SEÇİMİ YAPINIZ",
    choices=[
        "1 - A1",
        "2 - A2",
        "3 - B1",
        "4 - B2"
    ]
).ask()

if secim == "1 - A1":
    webbrowser.open("https://example.com/A1")
elif secim == "2 - A2":
    webbrowser.open("https://example.com/A2")
elif secim == "3 - B1":
    webbrowser.open("https://calculator-jctqjn5zjrrasjtf2jw5wi.streamlit.app/")
elif secim == "4 - B2":
    webbrowser.open("https://example.com/B2")