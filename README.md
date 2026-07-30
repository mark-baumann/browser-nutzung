# 🌐 Browser-Nutzung

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Browser-Use](https://img.shields.io/badge/Browser--Use-Automation-green.svg)](https://github.com/browser-use/browser-use)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

**Browser-Automation für KI-Agenten** — Web-Interaktion, DOM-Extraktion, Screenshots und strukturierte Datenextraktion mit Browser-Use.

## 📋 Beschreibung

Dieses Repository demonstriert die Nutzung von Browser-Automation für KI-Agenten. Es bietet eine Streamlit-App zur interaktiven URL-Analyse, Element-Extraktion und Screenshot-Erstellung — sowie eine umfangreiche Test-Suite für Browser-Use-Features wie DOM-Visibility, Coordinate-Clicking, File-System-Integration und Security-Flags.

- **URL-Analyse** — Seitenmetadaten, Ladezeit, HTTPS-Status
- **Element-Extraktion** — Überschriften, Links, Bilder, Buttons, Formulare
- **Screenshot-Automation** — Vollbild- und Element-Screenshots
- **Browser-Use-Integration** — CI-getestete Browser-Automation

## ✨ Features

- 🔍 **Seitenanalyse** — Automatische Extraktion von Titel, Status, Ladezeit
- 📸 **Screenshots** — Vollbild- und Element-Screenshots
- 🏷️ **DOM-Extraktion** — Strukturierte Extraktion von Überschriften, Links, Bildern, Formularen
- 🧪 **Umfangreiche CI-Tests** — 50+ Testdateien für Browser-Use-Features
- 🔒 **Security-Tests** — IP-Blocking, Sensitive-Data, Download-Sanitization
- 🖥️ **Streamlit-App** — Interaktive Demo für alle Features
- 📄 **Datei-Support** — DOCX, PDF, Bild-Extraktion aus Webseiten

## 🚀 Installation

```bash
# Repository klonen
git clone https://github.com/mark-baumann/browser-nutzung.git
cd browser-nutzung

# Virtuelle Umgebung erstellen
python3 -m venv .venv
source .venv/bin/activate

# Abhängigkeiten installieren
pip install -r requirements.txt

# Browser-Use und Playwright
pip install browser-use
playwright install chromium
```

## 🎮 Nutzung

### Streamlit-App

```bash
streamlit run app.py
```

Die App bietet:
- **URL-Analyse** — Beliebige URL eingeben und Metadaten analysieren
- **Element-Extraktion** — DOM-Elemente strukturiert extrahieren
- **Screenshots** — Seiten-Screenshots erstellen und anzeigen
- **Browser-Konfiguration** — Headless-Modus, Viewport, Timeout

### Tests

```bash
# Alle Tests
pytest tests/ -v

# Nur CI-Tests
pytest tests/ci/ -v

# Security-Tests
pytest tests/ci/security/ -v
```

## 🏗️ Tech-Stack

| Komponente | Technologie |
|---|---|
| **Sprache** | Python 3.10+ |
| **Automation** | Browser-Use, Playwright |
| **Daten** | Pandas, NumPy |
| **UI** | Streamlit |
| **Testing** | pytest |

## 📁 Projektstruktur

```
browser-nutzung/
├── app.py                  # Streamlit-App
└── tests/
    ├── ci/                 # CI-Tests (50+ Dateien)
    │   ├── test_browser_use_cli.py
    │   ├── test_dom_visibility.py
    │   ├── test_coordinate_clicking.py
    │   ├── test_fallback_llm.py
    │   ├── test_agent_planning.py
    │   ├── security/
    │   │   ├── test_sensitive_data.py
    │   │   ├── test_ip_blocking.py
    │   │   └── test_security_flags.py
    │   └── ...
    └── scripts/
        ├── debug_iframe_scrolling.py
        └── test_frame_hierarchy.py
```

## 👤 Autor

**Mark Baumann** — [GitHub](https://github.com/mark-baumann)

---

*Für Fragen oder Beiträge: Issue erstellen oder Pull Request öffnen.*
