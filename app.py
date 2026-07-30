"""
Browser-Nutzung — Streamlit App
===============================
Web-Oberfläche für Browser-Use Demo: URL analysieren, Screenshots, Elemente extrahieren.
"""

from datetime import datetime
from typing import List

import pandas as pd
import streamlit as st

# ──────────────────────────────────────────────────────────────
# Konfiguration
# ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Browser-Nutzung",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────
# Demo-Daten & Hilfsfunktionen
# ──────────────────────────────────────────────────────────────

def generate_page_analysis(url: str) -> dict:
    """Simuliert eine Browser-Use Seitenanalyse."""
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    
    return {
        "url": url,
        "domain": domain,
        "title": f"Seite: {domain}",
        "status_code": 200,
        "load_time_ms": hash(url) % 2000 + 200,
        "content_length_kb": hash(url) % 5000 + 50,
        "has_https": url.startswith("https"),
        "analyzed_at": datetime.now().isoformat(),
    }


def generate_elements(url: str) -> List[dict]:
    """Simuliert extrahierte Seitenelemente."""
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    seed = hash(url) % 1000
    
    elements = [
        {"Typ": "Überschrift (H1)", "Inhalt": f"Willkommen auf {domain}", "Selektor": "h1"},
        {"Typ": "Absatz", "Inhalt": f"Dies ist eine Beispiel-Seite für {domain}. Hier finden Sie alle wichtigen Informationen.", "Selektor": "p.main"},
        {"Typ": "Link", "Inhalt": "https://example.com/mehr", "Selektor": "a.nav-link"},
        {"Typ": "Bild", "Inhalt": f"https://{domain}/logo.png", "Selektor": "img.logo"},
        {"Typ": "Button", "Inhalt": "Jetzt kaufen", "Selektor": "button.cta"},
        {"Typ": "Eingabefeld", "Inhalt": "placeholder: Suche...", "Selektor": "input.search"},
        {"Typ": "Liste", "Inhalt": "3 Einträge gefunden", "Selektor": "ul.results"},
        {"Typ": "Formular", "Inhalt": "Kontaktformular", "Selektor": "form#contact"},
    ]
    
    return elements


def generate_screenshot_placeholder() -> str:
    """Erzeugt einen farbigen Platzhalter für Screenshots."""
    return "📸 Screenshot wird in der Live-Version mit Browser-Use erstellt."


# ──────────────────────────────────────────────────────────────
# Streamlit UI
# ──────────────────────────────────────────────────────────────

st.title("🌐 Browser-Nutzung")
st.markdown("**Browser-Use Demo — Webseiten analysieren, Screenshots erstellen, Elemente extrahieren**")

# ── Seitenleiste ──────────────────────────────────────────────

with st.sidebar:
    st.header("⚙️ Browser-Einstellungen")
    
    url = st.text_input(
        "URL",
        value="https://example.com",
        placeholder="https://www.example.com",
        help="Geben Sie die zu analysierende URL ein.",
    )
    
    st.divider()
    
    st.markdown("### 🔧 Optionen")
    
    viewport_width = st.selectbox(
        "Viewport-Breite",
        options=[1920, 1440, 1024, 768, 375],
        index=0,
        format_func=lambda x: f"{x}px {'(Desktop)' if x >= 1024 else '(Tablet)' if x >= 768 else '(Mobil)'}",
    )
    
    viewport_height = st.selectbox(
        "Viewport-Höhe",
        options=[1080, 900, 800, 600],
        index=0,
        format_func=lambda x: f"{x}px",
    )
    
    wait_time = st.slider(
        "Wartezeit (Sekunden)",
        min_value=1,
        max_value=10,
        value=3,
        help="Wartezeit nach dem Laden der Seite.",
    )
    
    st.divider()
    
    st.markdown("### 🎯 Aktionen")
    take_screenshot = st.checkbox("Screenshot erstellen", value=True)
    extract_elements = st.checkbox("Elemente extrahieren", value=True)
    extract_links = st.checkbox("Alle Links sammeln", value=False)
    extract_text = st.checkbox("Text extrahieren", value=False)
    
    st.divider()
    
    if st.button("🌐 Seite analysieren", type="primary", use_container_width=True):
        st.session_state.browser_triggered = True
    else:
        if "browser_triggered" not in st.session_state:
            st.session_state.browser_triggered = False

# ── Hauptbereich ──────────────────────────────────────────────

tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Seitenanalyse",
    "📸 Screenshot",
    "🔍 Elemente",
    "📜 Verlauf",
])

# ── Tab 1: Seitenanalyse ──────────────────────────────────────

with tab1:
    if st.session_state.browser_triggered:
        with st.spinner(f"🌐 Analysiere {url}..."):
            analysis = generate_page_analysis(url)
            elements = generate_elements(url) if extract_elements else []
            st.session_state.page_analysis = analysis
            st.session_state.page_elements = elements
        
        st.success(f"✅ Seite analysiert: **{analysis['title']}**")
        
        # Übersicht
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Status", f"{analysis['status_code']} OK" if analysis['status_code'] == 200 else str(analysis['status_code']))
        with col2:
            st.metric("Ladezeit", f"{analysis['load_time_ms']} ms")
        with col3:
            st.metric("Größe", f"{analysis['content_length_kb']} KB")
        with col4:
            st.metric("HTTPS", "✅" if analysis['has_https'] else "❌")
        
        st.divider()
        
        # Details
        st.markdown("### 📋 Seiten-Details")
        details_df = pd.DataFrame([{
            "Eigenschaft": "URL",
            "Wert": analysis['url'],
        }, {
            "Eigenschaft": "Domain",
            "Wert": analysis['domain'],
        }, {
            "Eigenschaft": "Titel",
            "Wert": analysis['title'],
        }, {
            "Eigenschaft": "Viewport",
            "Wert": f"{viewport_width}x{viewport_height}",
        }, {
            "Eigenschaft": "Wartezeit",
            "Wert": f"{wait_time}s",
        }, {
            "Eigenschaft": "Analysiert am",
            "Wert": analysis['analyzed_at'],
        }])
        st.dataframe(details_df, use_container_width=True, hide_index=True)
        
        # Browser-Info
        st.markdown("### 🌐 Browser-Informationen")
        st.json({
            "browser": "Chromium (headless)",
            "version": "120.0.6099.109",
            "viewport": f"{viewport_width}x{viewport_height}",
            "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "javascript_enabled": True,
            "cookies_enabled": True,
        })
    else:
        st.info("👈 Geben Sie eine URL ein und klicken Sie auf **Seite analysieren**.")
        
        st.markdown("### 💡 Beispiel-Analyse")
        demo_analysis = generate_page_analysis("https://example.com")
        st.json(demo_analysis)
        st.caption("Beispieldaten — starten Sie eine echte Analyse.")

# ── Tab 2: Screenshot ─────────────────────────────────────────

with tab2:
    if "page_analysis" in st.session_state:
        analysis = st.session_state.page_analysis
        
        st.markdown(f"### 📸 Screenshot: {analysis['domain']}")
        
        if take_screenshot:
            # Screenshot-Platzhalter mit farbigem Hintergrund
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 12px;
                padding: 60px 20px;
                text-align: center;
                color: white;
                font-size: 18px;
                margin: 20px 0;
            ">
                <div style="font-size: 64px; margin-bottom: 16px;">📸</div>
                <div style="font-size: 24px; font-weight: bold; margin-bottom: 8px;">
                    {analysis['domain']}
                </div>
                <div style="font-size: 14px; opacity: 0.9;">
                    Viewport: {viewport_width}×{viewport_height} | Ladezeit: {analysis['load_time_ms']}ms
                </div>
                <div style="font-size: 12px; opacity: 0.7; margin-top: 12px;">
                    Screenshot wird in der Live-Version mit Browser-Use + Playwright erstellt
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Screenshot-Metadaten
            st.markdown("### 📋 Screenshot-Informationen")
            st.json({
                "format": "PNG",
                "full_page": False,
                "viewport": f"{viewport_width}x{viewport_height}",
                "timestamp": analysis['analyzed_at'],
                "file_size_estimate": f"{analysis['content_length_kb'] * 3} KB",
            })
        else:
            st.info("Aktivieren Sie 'Screenshot erstellen' in der Seitenleiste.")
    else:
        st.info("Analysieren Sie zuerst eine Seite (Tab 1).")

# ── Tab 3: Elemente ────────────────────────────────────────────

with tab3:
    if "page_elements" in st.session_state and st.session_state.page_elements:
        elements = st.session_state.page_elements
        
        st.markdown(f"### 🔍 Extrahierte Elemente ({len(elements)})")
        
        # Filter
        element_types = list(set(e["Typ"] for e in elements))
        selected_types = st.multiselect(
            "Element-Typ filtern",
            options=element_types,
            default=element_types,
        )
        
        filtered = [e for e in elements if e["Typ"] in selected_types]
        
        if filtered:
            df = pd.DataFrame(filtered)
            st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Element-Statistik
        st.markdown("### 📊 Element-Statistik")
        type_counts = {}
        for e in elements:
            main_type = e["Typ"].split(" (")[0]
            type_counts[main_type] = type_counts.get(main_type, 0) + 1
        
        df_stats = pd.DataFrame({
            "Element-Typ": list(type_counts.keys()),
            "Anzahl": list(type_counts.values()),
        })
        st.bar_chart(df_stats.set_index("Element-Typ"), use_container_width=True)
        
        # Links (falls aktiviert)
        if extract_links:
            st.markdown("### 🔗 Alle Links")
            links = [
                {"Text": f"Link {i+1}", "URL": f"https://{st.session_state.page_analysis['domain']}/page{i+1}"}
                for i in range(5)
            ]
            st.dataframe(pd.DataFrame(links), use_container_width=True, hide_index=True)
    else:
        st.info("Analysieren Sie zuerst eine Seite mit aktivierter Element-Extraktion (Tab 1).")

# ── Tab 4: Verlauf ────────────────────────────────────────────

with tab4:
    st.markdown("### 📜 Analyse-Verlauf")
    
    if "analysis_history" not in st.session_state:
        st.session_state.analysis_history = []
    
    if "page_analysis" in st.session_state:
        # Aktuelle Analyse zum Verlauf hinzufügen
        current = st.session_state.page_analysis
        if not st.session_state.analysis_history or st.session_state.analysis_history[-1]["url"] != current["url"]:
            st.session_state.analysis_history.append(current)
    
    if st.session_state.analysis_history:
        history_df = pd.DataFrame([{
            "Zeitpunkt": h["analyzed_at"],
            "URL": h["url"],
            "Domain": h["domain"],
            "Status": h["status_code"],
            "Ladezeit (ms)": h["load_time_ms"],
            "Größe (KB)": h["content_length_kb"],
        } for h in reversed(st.session_state.analysis_history)])
        
        st.dataframe(history_df, use_container_width=True, hide_index=True)
        
        if st.button("🗑️ Verlauf löschen"):
            st.session_state.analysis_history = []
            st.rerun()
    else:
        st.info("Noch keine Analysen im Verlauf. Starten Sie eine Analyse in Tab 1.")

# ── Footer ────────────────────────────────────────────────────

st.divider()
st.caption(f"🌐 Browser-Nutzung v1.0 | Powered by Browser-Use | {datetime.now().strftime('%d.%m.%Y %H:%M')}")
