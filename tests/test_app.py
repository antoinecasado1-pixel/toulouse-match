from datetime import date

import pytest
from streamlit.testing.v1 import AppTest

from catho import liturgie, prieres, saints


@pytest.mark.parametrize("annee,attendu", [
    (2024, date(2024, 3, 31)),
    (2025, date(2025, 4, 20)),
    (2026, date(2026, 4, 5)),
    (2027, date(2027, 3, 28)),
    (2038, date(2038, 4, 25)),
])
def test_paques(annee, attendu):
    assert liturgie.paques(annee) == attendu


@pytest.mark.parametrize("annee,attendu", [
    (2024, date(2024, 12, 1)),
    (2025, date(2025, 11, 30)),
    (2026, date(2026, 11, 29)),
    (2022, date(2022, 11, 27)),
])
def test_avent(annee, attendu):
    assert liturgie.premier_dimanche_avent(annee) == attendu


def test_epiphanie_et_bapteme():
    assert liturgie.epiphanie(2026) == date(2026, 1, 4)
    assert liturgie.bapteme_du_seigneur(2026) == date(2026, 1, 11)
    assert liturgie.epiphanie(2023) == date(2023, 1, 8)
    assert liturgie.bapteme_du_seigneur(2023) == date(2023, 1, 9)


@pytest.mark.parametrize("jour,nom,couleur", [
    (date(2026, 1, 5), "Temps de Noël", "blanc"),
    (date(2026, 2, 18), "Carême", "violet"),
    (date(2026, 3, 15), "Carême – dimanche de Laetare", "rose"),
    (date(2026, 3, 29), "Semaine sainte – Rameaux", "rouge"),
    (date(2026, 4, 3), "Triduum pascal – Vendredi saint", "rouge"),
    (date(2026, 4, 5), "Temps pascal", "blanc"),
    (date(2026, 5, 24), "Pentecôte", "rouge"),
    (date(2026, 7, 14), "Temps ordinaire", "vert"),
    (date(2026, 12, 3), "Avent", "violet"),
    (date(2026, 12, 13), "Avent – dimanche de Gaudete", "rose"),
    (date(2026, 12, 26), "Temps de Noël", "blanc"),
])
def test_temps_liturgique(jour, nom, couleur):
    t = liturgie.temps_liturgique(jour)
    assert (t.nom, t.couleur) == (nom, couleur)


def test_donnees_coherentes():
    for s in saints.SAINTS:
        date(2024, *s["fete"])  # date valide
    for q in prieres.QUIZ:
        assert q["rep"] in q["choix"] and len(q["choix"]) == 4
    assert saints.prochain_saint(12, 31)["fete"] == (1, 3)


def test_toutes_les_pages():
    at = AppTest.from_file("../streamlit_app.py", default_timeout=30).run()
    assert not at.exception
    pages = at.sidebar.radio[0].options
    for page in pages:
        at.sidebar.radio[0].set_value(page).run()
        assert not at.exception, page


def test_quiz_score():
    at = AppTest.from_file("../streamlit_app.py", default_timeout=30).run()
    at.sidebar.radio[0].set_value("❓ Quiz").run()
    for radio in at.main.radio:
        i = int(radio.key[1:])
        radio.set_value(prieres.QUIZ[i]["rep"])
    at.main.button[-1].click().run()
    assert not at.exception
    assert any("Score : 10 / 10" in h.value for h in at.subheader)
