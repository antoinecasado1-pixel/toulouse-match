"""Calcul du calendrier liturgique (rite romain, usages de France)."""

from dataclasses import dataclass
from datetime import date, timedelta


def paques(annee: int) -> date:
    """Date de Pâques (calendrier grégorien), algorithme de Meeus/Jones/Butcher."""
    a = annee % 19
    b, c = divmod(annee, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mois, jour = divmod(h + l - 7 * m + 114, 31)
    return date(annee, mois, jour + 1)


def premier_dimanche_avent(annee: int) -> date:
    """Le 1er dimanche de l'Avent tombe entre le 27 novembre et le 3 décembre."""
    noel = date(annee, 12, 25)
    # Dimanche précédant strictement Noël, puis trois semaines avant.
    quatrieme = noel - timedelta(days=(noel.weekday() + 1) % 7 or 7)
    return quatrieme - timedelta(weeks=3)


def epiphanie(annee: int) -> date:
    """En France, l'Épiphanie est fêtée le dimanche entre le 2 et le 8 janvier."""
    j2 = date(annee, 1, 2)
    return j2 + timedelta(days=(6 - j2.weekday()) % 7)


def bapteme_du_seigneur(annee: int) -> date:
    epi = epiphanie(annee)
    if epi.day >= 7:
        return epi + timedelta(days=1)  # lundi
    return epi + timedelta(days=7)


def fetes_mobiles(annee: int) -> dict[str, date]:
    p = paques(annee)
    return {
        "Épiphanie du Seigneur": epiphanie(annee),
        "Baptême du Seigneur": bapteme_du_seigneur(annee),
        "Mercredi des Cendres": p - timedelta(days=46),
        "Dimanche des Rameaux": p - timedelta(days=7),
        "Jeudi saint": p - timedelta(days=3),
        "Vendredi saint": p - timedelta(days=2),
        "Dimanche de Pâques": p,
        "Lundi de Pâques (férié)": p + timedelta(days=1),
        "Dimanche de la Divine Miséricorde": p + timedelta(days=7),
        "Ascension (fériée)": p + timedelta(days=39),
        "Pentecôte": p + timedelta(days=49),
        "Lundi de Pentecôte (férié)": p + timedelta(days=50),
        "Sainte Trinité": p + timedelta(days=56),
        "Saint-Sacrement (Fête-Dieu)": p + timedelta(days=63),
        "Sacré-Cœur de Jésus": p + timedelta(days=68),
        "1er dimanche de l'Avent": premier_dimanche_avent(annee),
    }


FETES_FIXES = {
    (1, 1): "Sainte Marie, Mère de Dieu",
    (2, 2): "Présentation du Seigneur (Chandeleur)",
    (3, 19): "Saint Joseph",
    (3, 25): "Annonciation du Seigneur",
    (6, 24): "Nativité de saint Jean-Baptiste",
    (6, 29): "Saints Pierre et Paul",
    (8, 6): "Transfiguration du Seigneur",
    (8, 15): "Assomption de la Vierge Marie, patronne principale de la France (fériée)",
    (9, 14): "La Croix glorieuse",
    (11, 1): "Toussaint (fériée)",
    (11, 2): "Commémoration de tous les fidèles défunts",
    (12, 8): "Immaculée Conception",
    (12, 25): "Nativité du Seigneur – Noël (fériée)",
}


@dataclass
class Temps:
    nom: str
    couleur: str


COULEURS = {
    "violet": "#6a1b9a",
    "blanc": "#f5f0e1",
    "vert": "#2e7d32",
    "rouge": "#c62828",
    "rose": "#f48fb1",
}


def temps_liturgique(jour: date) -> Temps:
    """Temps liturgique et couleur habituelle pour un jour donné."""
    a = jour.year
    p = paques(a)
    cendres = p - timedelta(days=46)
    pentecote = p + timedelta(days=49)
    avent = premier_dimanche_avent(a)

    if jour == p - timedelta(days=21):
        return Temps("Carême – dimanche de Laetare", "rose")
    if jour == avent + timedelta(weeks=2):
        return Temps("Avent – dimanche de Gaudete", "rose")
    if jour in (p - timedelta(days=7), p - timedelta(days=2), pentecote):
        noms = {p - timedelta(days=7): "Semaine sainte – Rameaux",
                p - timedelta(days=2): "Triduum pascal – Vendredi saint",
                pentecote: "Pentecôte"}
        return Temps(noms[jour], "rouge")

    if jour >= avent and jour < date(a, 12, 25):
        return Temps("Avent", "violet")
    if jour >= date(a, 12, 25) or jour <= bapteme_du_seigneur(a):
        return Temps("Temps de Noël", "blanc")
    if cendres <= jour < p - timedelta(days=7):
        return Temps("Carême", "violet")
    if p - timedelta(days=7) <= jour < p - timedelta(days=3):
        return Temps("Semaine sainte", "violet")
    if p - timedelta(days=3) <= jour < p:
        return Temps("Triduum pascal", "blanc" if jour == p - timedelta(days=3) else "violet")
    if p <= jour < pentecote:
        return Temps("Temps pascal", "blanc")
    return Temps("Temps ordinaire", "vert")
