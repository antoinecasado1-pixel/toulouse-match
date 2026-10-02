import random
from datetime import date

import pandas as pd
import streamlit as st

from catho import histoire, lieux, liturgie, prieres, saints

st.set_page_config(page_title="France catholique", page_icon="⛪", layout="wide")

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]
JOURS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]


def date_fr(d: date) -> str:
    return f"{JOURS[d.weekday()]} {d.day} {MOIS[d.month - 1]} {d.year}"


def fete_fr(fete: tuple[int, int]) -> str:
    mois, jour = fete
    return f"{'1er' if jour == 1 else jour} {MOIS[mois - 1]}"


def pastille(couleur: str) -> str:
    return (f"<span style='display:inline-block;width:1em;height:1em;border-radius:50%;"
            f"border:1px solid #888;vertical-align:middle;background:{liturgie.COULEURS[couleur]}'></span>")


def fiche_saint(s: dict) -> None:
    st.markdown(f"**{s['nom']}** — *{s['titre']}*  \n"
                f"Fête : {fete_fr(s['fete'])} · {s['epoque']} · {s['region']}")
    st.write(s["resume"])


# --------------------------------------------------------------------------- pages

def page_accueil() -> None:
    st.title("⛪ France catholique")
    st.caption("Apprendre la foi catholique à travers l'histoire, les saints et les lieux de France.")
    aujourdhui = date.today()
    temps = liturgie.temps_liturgique(aujourdhui)

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Aujourd'hui")
        st.markdown(f"**{date_fr(aujourdhui).capitalize()}**")
        st.markdown(f"{pastille(temps.couleur)} {temps.nom} — couleur liturgique : {temps.couleur}",
                    unsafe_allow_html=True)
        fixe = liturgie.FETES_FIXES.get((aujourdhui.month, aujourdhui.day))
        if fixe:
            st.success(f"Fête : {fixe}")
        mystere = prieres.MYSTERE_DU_JOUR[aujourdhui.weekday()]
        st.markdown(f"📿 Chapelet du jour : **{mystere.split(' (')[0]}**")
    with c2:
        st.subheader("Saint de France à l'honneur")
        du_jour = saints.saints_du_jour(aujourdhui.month, aujourdhui.day)
        if du_jour:
            for s in du_jour:
                fiche_saint(s)
        else:
            st.caption("Aucun saint de notre liste n'est fêté aujourd'hui. Prochaine fête :")
            fiche_saint(saints.prochain_saint(aujourdhui.month, aujourdhui.day))

    st.divider()
    st.subheader("Patrons de la France")
    for nom, desc in histoire.PATRONS:
        st.markdown(f"- **{nom}** : {desc}")

    st.divider()
    m = st.columns(4)
    m[0].metric("Saints présentés", len(saints.SAINTS))
    m[1].metric("Lieux saints", len(lieux.LIEUX))
    m[2].metric("Dates d'histoire", len(histoire.CHRONOLOGIE))
    m[3].metric("Questions de quiz", len(prieres.QUIZ))


def page_calendrier() -> None:
    st.title("📅 Calendrier liturgique")
    annee = st.number_input("Année", min_value=1900, max_value=2200, value=date.today().year, step=1)
    st.info(f"Pâques {annee} : **{date_fr(liturgie.paques(annee))}**")

    lignes = [{"Fête": nom, "Date": d, "Jour": date_fr(d)} for nom, d in liturgie.fetes_mobiles(annee).items()]
    lignes += [{"Fête": nom, "Date": date(annee, m, j), "Jour": date_fr(date(annee, m, j))}
               for (m, j), nom in liturgie.FETES_FIXES.items()]
    lignes += [{"Fête": s["nom"], "Date": date(annee, *s["fete"]), "Jour": date_fr(date(annee, *s["fete"]))}
               for s in saints.SAINTS]
    df = pd.DataFrame(lignes).sort_values("Date")
    st.dataframe(df[["Jour", "Fête"]], hide_index=True, use_container_width=True, height=600)

    st.subheader("Quel temps liturgique ?")
    jour = st.date_input("Choisir une date", value=date.today(), format="DD/MM/YYYY")
    t = liturgie.temps_liturgique(jour)
    st.markdown(f"{pastille(t.couleur)} **{t.nom}** — couleur : {t.couleur}", unsafe_allow_html=True)
    with st.expander("Les couleurs liturgiques"):
        st.markdown(
            "- **Violet** : Avent et Carême, temps de préparation et de pénitence.\n"
            "- **Blanc** : Noël, Pâques, fêtes du Christ, de Marie et des saints non martyrs.\n"
            "- **Vert** : temps ordinaire, couleur de l'espérance.\n"
            "- **Rouge** : Rameaux, Vendredi saint, Pentecôte, apôtres et martyrs.\n"
            "- **Rose** : dimanches de Gaudete (Avent) et Laetare (Carême).")


def page_saints() -> None:
    st.title("😇 Saints de France")
    regions = sorted({s["region"] for s in saints.SAINTS})
    c1, c2 = st.columns([2, 1])
    recherche = c1.text_input("Rechercher un saint", placeholder="ex. Thérèse, Lyon, patron…")
    region = c2.selectbox("Région", ["Toutes"] + regions)
    liste = sorted(saints.SAINTS, key=lambda s: s["fete"])
    if recherche:
        r = recherche.lower()
        liste = [s for s in liste if r in (s["nom"] + s["titre"] + s["resume"] + s["region"]).lower()]
    if region != "Toutes":
        liste = [s for s in liste if s["region"] == region]
    st.caption(f"{len(liste)} saint(s)")
    for s in liste:
        with st.expander(f"{s['nom']} — {fete_fr(s['fete'])}"):
            fiche_saint(s)


def page_lieux() -> None:
    st.title("🗺️ Sanctuaires et lieux saints")
    types = sorted({l["type"] for l in lieux.LIEUX})
    choix = st.multiselect("Types de lieux", types, default=types)
    selection = [l for l in lieux.LIEUX if l["type"] in choix]
    if selection:
        st.map(pd.DataFrame(selection)[["lat", "lon"]], zoom=4.5)
    for l in selection:
        with st.expander(f"{l['nom']} — {l['ville']}"):
            st.caption(l["type"])
            st.write(l["desc"])

    st.subheader("🐚 Chemins de Saint-Jacques-de-Compostelle en France")
    st.dataframe(pd.DataFrame(lieux.CHEMINS_COMPOSTELLE).rename(
        columns={"nom": "Voie", "depart": "Départ", "etapes": "Grandes étapes"}),
        hide_index=True, use_container_width=True)

    st.subheader("🚶 Grands pèlerinages")
    for p in lieux.PELERINAGES:
        st.markdown(f"**{p['nom']}** ({p['quand']}) — {p['desc']}")


def page_histoire() -> None:
    st.title("📜 Histoire de l'Église en France")
    periodes = list(dict.fromkeys(p for p, _, _ in histoire.CHRONOLOGIE))
    onglets = st.tabs(periodes)
    for onglet, periode in zip(onglets, periodes):
        with onglet:
            for p, annee, evenement in histoire.CHRONOLOGIE:
                if p == periode:
                    st.markdown(f"**{annee}** — {evenement}")


def page_apparitions() -> None:
    st.title("🌹 Apparitions mariales en France")
    st.caption("L'Église ne reconnaît une apparition qu'après une enquête de l'évêque du lieu ; "
               "même reconnue, elle n'oblige pas la foi des fidèles.")
    for a in histoire.APPARITIONS:
        with st.container(border=True):
            st.markdown(f"### {a['lieu']} — {a['annees']}")
            st.markdown(f"**Voyant(s)** : {a['voyants']}  \n**Statut** : {a['statut']}")
            st.write(a["message"])


def page_ordres() -> None:
    st.title("🕊️ Ordres religieux et docteurs de l'Église")
    st.subheader("Ordres et congrégations nés en France")
    df = pd.DataFrame(histoire.ORDRES).rename(
        columns={"nom": "Ordre", "date": "Fondation", "fondateur": "Fondateur", "charisme": "Charisme"})
    st.dataframe(df, hide_index=True, use_container_width=True)
    st.subheader("Docteurs de l'Église français")
    for nom, surnom, annee in histoire.DOCTEURS:
        st.markdown(f"- **{nom}** — {surnom}, proclamé docteur en {annee}")


def page_prieres() -> None:
    st.title("🙏 Prières et chapelet")
    onglet_prieres, onglet_chapelet = st.tabs(["Prières", "Chapelet"])
    with onglet_prieres:
        choix = st.selectbox("Choisir une prière", list(prieres.PRIERES))
        st.markdown(prieres.PRIERES[choix].replace("\n", "  \n"))
    with onglet_chapelet:
        st.markdown(
            "1. Signe de croix et **Je crois en Dieu**\n"
            "2. Un **Notre Père**, trois **Je vous salue Marie**, un **Gloire au Père**\n"
            "3. Pour chacune des 5 dizaines : annoncer le mystère, un **Notre Père**, "
            "dix **Je vous salue Marie**, un **Gloire au Père**\n"
            "4. Terminer par le **Salve Regina** ou le **Souvenez-vous**")
        du_jour = prieres.MYSTERE_DU_JOUR[date.today().weekday()]
        for nom, mysteres in prieres.MYSTERES.items():
            with st.expander(nom + (" — aujourd'hui" if nom == du_jour else ""), expanded=nom == du_jour):
                for i, m in enumerate(mysteres, 1):
                    st.markdown(f"{i}. {m}")


def page_traditions() -> None:
    st.title("🎄 Traditions et lexique")
    st.subheader("Fêtes et traditions catholiques françaises")
    for nom, quand, desc in prieres.TRADITIONS:
        st.markdown(f"**{nom}** · *{quand}* — {desc}")
    st.subheader("Petit lexique")
    recherche = st.text_input("Chercher un mot")
    for mot, definition in prieres.LEXIQUE.items():
        if not recherche or recherche.lower() in (mot + definition).lower():
            st.markdown(f"**{mot}** : {definition}")


def page_quiz() -> None:
    st.title("❓ Quiz")
    if "quiz_ordre" not in st.session_state or st.button("🔀 Nouveau quiz"):
        for i in st.session_state.get("quiz_ordre", []):
            st.session_state.pop(f"q{i}", None)
        ordre = random.sample(range(len(prieres.QUIZ)), 10)
        st.session_state.quiz_ordre = ordre
        st.session_state.quiz_resultat = None
        st.session_state.quiz_choix = {i: random.sample(prieres.QUIZ[i]["choix"], 4) for i in ordre}
    ordre = st.session_state.quiz_ordre

    with st.form("quiz"):
        reponses = {}
        for n, i in enumerate(ordre, 1):
            q = prieres.QUIZ[i]
            reponses[i] = st.radio(f"{n}. {q['q']}", st.session_state.quiz_choix[i], index=None, key=f"q{i}")
        if st.form_submit_button("Valider mes réponses"):
            st.session_state.quiz_resultat = reponses

    resultat = st.session_state.get("quiz_resultat")
    if resultat:
        score = sum(resultat[i] == prieres.QUIZ[i]["rep"] for i in ordre)
        st.subheader(f"Score : {score} / {len(ordre)}")
        if score == len(ordre):
            st.balloons()
        for n, i in enumerate(ordre, 1):
            q = prieres.QUIZ[i]
            if resultat[i] == q["rep"]:
                st.markdown(f"✅ {n}. {q['rep']}")
            else:
                st.markdown(f"❌ {n}. Bonne réponse : **{q['rep']}**")


PAGES = {
    "🏠 Accueil": page_accueil,
    "📅 Calendrier liturgique": page_calendrier,
    "😇 Saints de France": page_saints,
    "🗺️ Sanctuaires et pèlerinages": page_lieux,
    "📜 Histoire": page_histoire,
    "🌹 Apparitions mariales": page_apparitions,
    "🕊️ Ordres et docteurs": page_ordres,
    "🙏 Prières et chapelet": page_prieres,
    "🎄 Traditions et lexique": page_traditions,
    "❓ Quiz": page_quiz,
}

with st.sidebar:
    st.header("⛪ France catholique")
    page = st.radio("Rubriques", list(PAGES), label_visibility="collapsed")
    st.caption("« France, fille aînée de l'Église, es-tu fidèle aux promesses de ton baptême ? » — Jean-Paul II, 1980")

PAGES[page]()
