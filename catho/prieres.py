"""Prières en français, chapelet, traditions, lexique et quiz."""

PRIERES = {
    "Notre Père": (
        "Notre Père, qui es aux cieux,\n"
        "que ton nom soit sanctifié,\n"
        "que ton règne vienne,\n"
        "que ta volonté soit faite sur la terre comme au ciel.\n"
        "Donne-nous aujourd'hui notre pain de ce jour.\n"
        "Pardonne-nous nos offenses,\n"
        "comme nous pardonnons aussi à ceux qui nous ont offensés.\n"
        "Et ne nous laisse pas entrer en tentation\n"
        "mais délivre-nous du Mal.\n"
        "Amen."
    ),
    "Je vous salue Marie": (
        "Je vous salue, Marie, pleine de grâce ;\n"
        "le Seigneur est avec vous.\n"
        "Vous êtes bénie entre toutes les femmes\n"
        "et Jésus, le fruit de vos entrailles, est béni.\n"
        "Sainte Marie, Mère de Dieu,\n"
        "priez pour nous pauvres pécheurs,\n"
        "maintenant et à l'heure de notre mort.\n"
        "Amen."
    ),
    "Gloire au Père": (
        "Gloire au Père, et au Fils, et au Saint-Esprit,\n"
        "comme il était au commencement, maintenant et toujours,\n"
        "et dans les siècles des siècles.\n"
        "Amen."
    ),
    "Je crois en Dieu (Symbole des Apôtres)": (
        "Je crois en Dieu, le Père tout-puissant,\n"
        "créateur du ciel et de la terre.\n"
        "Et en Jésus-Christ, son Fils unique, notre Seigneur,\n"
        "qui a été conçu du Saint-Esprit,\n"
        "est né de la Vierge Marie,\n"
        "a souffert sous Ponce Pilate,\n"
        "a été crucifié, est mort et a été enseveli,\n"
        "est descendu aux enfers,\n"
        "le troisième jour est ressuscité des morts,\n"
        "est monté aux cieux,\n"
        "est assis à la droite de Dieu le Père tout-puissant,\n"
        "d'où il viendra juger les vivants et les morts.\n"
        "Je crois en l'Esprit Saint,\n"
        "à la sainte Église catholique,\n"
        "à la communion des saints,\n"
        "à la rémission des péchés,\n"
        "à la résurrection de la chair,\n"
        "à la vie éternelle.\n"
        "Amen."
    ),
    "L'Angélus": (
        "L'ange du Seigneur apporta l'annonce à Marie,\n"
        "et elle conçut du Saint-Esprit. — Je vous salue Marie…\n\n"
        "« Voici la servante du Seigneur,\n"
        "qu'il me soit fait selon votre parole. » — Je vous salue Marie…\n\n"
        "Et le Verbe s'est fait chair,\n"
        "et il a habité parmi nous. — Je vous salue Marie…\n\n"
        "Priez pour nous, sainte Mère de Dieu,\n"
        "afin que nous soyons rendus dignes des promesses du Christ.\n\n"
        "Prions : Que ta grâce, Seigneur notre Père, se répande en nos cœurs ; "
        "par le message de l'ange, tu nous as fait connaître l'incarnation de ton Fils bien-aimé, "
        "conduis-nous par sa passion et par sa croix jusqu'à la gloire de la résurrection. "
        "Par Jésus, le Christ, notre Seigneur. Amen."
    ),
    "Souvenez-vous (attribuée à saint Bernard)": (
        "Souvenez-vous, ô très miséricordieuse Vierge Marie,\n"
        "qu'on n'a jamais entendu dire qu'aucun de ceux qui ont eu recours à votre protection,\n"
        "imploré votre assistance ou réclamé vos suffrages, ait été abandonné.\n"
        "Animé d'une pareille confiance, ô Vierge des vierges, ô ma Mère, je cours vers vous,\n"
        "et gémissant sous le poids de mes péchés, je me prosterne à vos pieds.\n"
        "Ô Mère du Verbe incarné, ne méprisez pas mes prières,\n"
        "mais écoutez-les favorablement et daignez les exaucer.\n"
        "Amen."
    ),
    "Invocation de la Médaille miraculeuse (rue du Bac)": (
        "Ô Marie conçue sans péché,\n"
        "priez pour nous qui avons recours à vous."
    ),
    "Acte d'amour du saint curé d'Ars": (
        "Je vous aime, ô mon Dieu, et mon seul désir est de vous aimer jusqu'au dernier soupir de ma vie.\n"
        "Je vous aime, ô Dieu infiniment aimable, et j'aime mieux mourir en vous aimant que de vivre un seul instant sans vous aimer.\n"
        "Je vous aime, Seigneur, et la seule grâce que je vous demande, c'est de vous aimer éternellement.\n"
        "Mon Dieu, si ma langue ne peut dire à tout moment que je vous aime,\n"
        "je veux que mon cœur vous le répète autant de fois que je respire."
    ),
    "Prière de Charles de Foucauld (prière d'abandon)": (
        "Mon Père, je m'abandonne à toi, fais de moi ce qu'il te plaira.\n"
        "Quoi que tu fasses de moi, je te remercie.\n"
        "Je suis prêt à tout, j'accepte tout.\n"
        "Pourvu que ta volonté se fasse en moi, en toutes tes créatures,\n"
        "je ne désire rien d'autre, mon Dieu.\n"
        "Je remets mon âme entre tes mains.\n"
        "Je te la donne, mon Dieu, avec tout l'amour de mon cœur,\n"
        "parce que je t'aime,\n"
        "et que ce m'est un besoin d'amour de me donner,\n"
        "de me remettre entre tes mains sans mesure,\n"
        "avec une infinie confiance,\n"
        "car tu es mon Père."
    ),
}

MYSTERES = {
    "Mystères joyeux (lundi et samedi)": [
        "L'Annonciation", "La Visitation", "La Nativité",
        "La Présentation de Jésus au Temple", "Le Recouvrement de Jésus au Temple"],
    "Mystères lumineux (jeudi)": [
        "Le Baptême de Jésus", "Les Noces de Cana", "L'Annonce du Royaume",
        "La Transfiguration", "L'Institution de l'Eucharistie"],
    "Mystères douloureux (mardi et vendredi)": [
        "L'Agonie à Gethsémani", "La Flagellation", "Le Couronnement d'épines",
        "Le Portement de la Croix", "La Crucifixion"],
    "Mystères glorieux (mercredi et dimanche)": [
        "La Résurrection", "L'Ascension", "La Pentecôte",
        "L'Assomption de Marie", "Le Couronnement de Marie"],
}

# weekday() -> clé de MYSTERES
MYSTERE_DU_JOUR = {
    0: "Mystères joyeux (lundi et samedi)",
    1: "Mystères douloureux (mardi et vendredi)",
    2: "Mystères glorieux (mercredi et dimanche)",
    3: "Mystères lumineux (jeudi)",
    4: "Mystères douloureux (mardi et vendredi)",
    5: "Mystères joyeux (lundi et samedi)",
    6: "Mystères glorieux (mercredi et dimanche)",
}

TRADITIONS = [
    ("Épiphanie – galette des rois", "Début janvier",
     "On tire les rois avec une galette contenant une fève, en souvenir des Mages venus adorer Jésus."),
    ("Chandeleur", "2 février",
     "Fête de la Présentation de Jésus au Temple, « lumière des nations » : procession aux chandelles, et crêpes à la maison."),
    ("Mardi gras et Carême", "Février – mars",
     "Dernier jour de fête avant les 40 jours de jeûne, de prière et de partage menant à Pâques."),
    ("Rameaux et cloches de Pâques", "Semaine sainte",
     "On fait bénir du buis le dimanche des Rameaux. Les cloches se taisent du Jeudi au Samedi saint : "
     "on dit aux enfants qu'elles « partent à Rome » et reviennent avec des œufs en chocolat."),
    ("Fête-Dieu", "Juin",
     "Processions du Saint-Sacrement à travers les rues, avec reposoirs et pétales de fleurs."),
    ("Assomption et vœu de Louis XIII", "15 août",
     "Jour férié et fête de la patronne de la France : processions mariales dans tout le pays."),
    ("Toussaint et défunts", "1er et 2 novembre",
     "On fête tous les saints, puis on prie pour les défunts en fleurissant les tombes de chrysanthèmes."),
    ("Saint-Martin", "11 novembre",
     "Jour de l'Armistice de 1918, signé le jour de la Saint-Martin ; nombreuses fêtes et lanternes dans l'Est."),
    ("Saint-Nicolas", "6 décembre",
     "En Lorraine et en Alsace, le saint évêque distribue friandises et pains d'épices aux enfants."),
    ("Fête des Lumières", "8 décembre",
     "Les Lyonnais posent des lumignons à leurs fenêtres en l'honneur de Marie depuis 1852."),
    ("Crèche et santons", "Avent – Noël",
     "La crèche provençale peuple Bethléem de santons : le meunier, le berger, le ravi…"),
    ("Messe de minuit", "24 décembre",
     "Célébration de la Nativité dans la nuit de Noël, souvent précédée de veillées et de chants traditionnels."),
]

LEXIQUE = {
    "Abbaye": "Monastère dirigé par un abbé ou une abbesse.",
    "Avent": "Les quatre semaines de préparation à Noël ; début de l'année liturgique.",
    "Basilique": "Titre honorifique donné par le pape à une église importante.",
    "Calvaire": "Croix monumentale ; en Bretagne, sculpture des scènes de la Passion dans les enclos paroissiaux.",
    "Carême": "Les quarante jours de pénitence entre le mercredi des Cendres et Pâques.",
    "Cathédrale": "Église où se trouve la cathèdre (le siège) de l'évêque.",
    "Concordat": "Accord entre le Saint-Siège et un État ; celui de 1801 s'applique encore en Alsace-Moselle.",
    "Diocèse": "Territoire confié à un évêque ; la France en compte une centaine.",
    "Ex-voto": "Objet ou plaque déposé dans un sanctuaire en remerciement d'une grâce reçue.",
    "Fille aînée de l'Église": "Surnom de la France, premier royaume barbare converti au catholicisme avec Clovis.",
    "Laïcité": "Principe de neutralité de l'État envers les religions, fondé en France sur la loi de 1905.",
    "Pardon": "En Bretagne, fête patronale avec procession, messe et réjouissances.",
    "Pèlerinage": "Voyage vers un lieu saint, accompli dans la prière.",
    "Reliques": "Restes corporels d'un saint, ou objets lui ayant appartenu, vénérés par les fidèles.",
    "Sacrements": "Les sept signes efficaces de la grâce : baptême, confirmation, eucharistie, pénitence, onction des malades, ordre, mariage.",
    "Sacré-Cœur": "Dévotion à l'amour du Christ, popularisée par Paray-le-Monial.",
    "Vierge noire": "Statue de Marie au visage sombre, comme au Puy, à Rocamadour ou à Chartres.",
    "Vœu de Louis XIII": "Consécration du royaume de France à la Vierge Marie en 1638.",
}

QUIZ = [
    {"q": "Qui a baptisé Clovis à Reims ?",
     "choix": ["Saint Martin", "Saint Remi", "Saint Denis", "Saint Hilaire"], "rep": "Saint Remi"},
    {"q": "Quelle est la patronne principale de la France ?",
     "choix": ["Sainte Jeanne d'Arc", "Sainte Geneviève", "Notre-Dame de l'Assomption", "Sainte Thérèse"],
     "rep": "Notre-Dame de l'Assomption"},
    {"q": "En quelle année ont eu lieu les apparitions de Lourdes ?",
     "choix": ["1830", "1846", "1858", "1871"], "rep": "1858"},
    {"q": "Quel saint a partagé son manteau avec un pauvre à Amiens ?",
     "choix": ["Saint Martin", "Saint Louis", "Saint Vincent de Paul", "Saint Bernard"], "rep": "Saint Martin"},
    {"q": "Où sainte Thérèse de l'Enfant-Jésus était-elle carmélite ?",
     "choix": ["Alençon", "Lisieux", "Nevers", "Paray-le-Monial"], "rep": "Lisieux"},
    {"q": "Quel est le surnom de la France dans l'Église ?",
     "choix": ["La sœur cadette", "La fille aînée de l'Église", "La mère des nations", "Le royaume de Marie"],
     "rep": "La fille aînée de l'Église"},
    {"q": "Quelle loi de 1905 a organisé la séparation des Églises et de l'État ?",
     "choix": ["Le Concordat", "La loi de séparation", "L'édit de Nantes", "La Constitution civile du clergé"],
     "rep": "La loi de séparation"},
    {"q": "À qui la Vierge a-t-elle confié la Médaille miraculeuse ?",
     "choix": ["Bernadette Soubirous", "Catherine Labouré", "Mélanie Calvat", "Marguerite-Marie Alacoque"],
     "rep": "Catherine Labouré"},
    {"q": "Quel ordre religieux saint Bruno a-t-il fondé ?",
     "choix": ["Les Cisterciens", "Les Chartreux", "Les Dominicains", "Les Trappistes"], "rep": "Les Chartreux"},
    {"q": "Qui est appelé « le saint curé d'Ars » ?",
     "choix": ["Jean-Marie Vianney", "Jean Eudes", "Vincent de Paul", "Pierre-Julien Eymard"],
     "rep": "Jean-Marie Vianney"},
    {"q": "Dans quelle ville se trouve la basilique Saint-Sernin ?",
     "choix": ["Bordeaux", "Toulouse", "Lyon", "Albi"], "rep": "Toulouse"},
    {"q": "Où saint Bernard a-t-il prêché la deuxième croisade en 1146 ?",
     "choix": ["Clermont", "Cluny", "Vézelay", "Chartres"], "rep": "Vézelay"},
    {"q": "Quel roi a fait construire la Sainte-Chapelle ?",
     "choix": ["Clovis", "Charlemagne", "Saint Louis", "Louis XIV"], "rep": "Saint Louis"},
    {"q": "À quelle sainte le Sacré-Cœur est-il apparu à Paray-le-Monial ?",
     "choix": ["Jeanne de Chantal", "Marguerite-Marie Alacoque", "Louise de Marillac", "Jeanne Jugan"],
     "rep": "Marguerite-Marie Alacoque"},
    {"q": "Quel message est apparu dans le ciel de Pontmain en 1871 ?",
     "choix": ["« Je suis l'Immaculée Conception »", "« Mais priez mes enfants »",
               "« Faites pénitence »", "« Venez à la source »"], "rep": "« Mais priez mes enfants »"},
    {"q": "Quel docteur de l'Église a été proclamé en 2022 ?",
     "choix": ["Saint Hilaire de Poitiers", "Saint Irénée de Lyon", "Saint Martin de Tours", "Saint Bernard"],
     "rep": "Saint Irénée de Lyon"},
    {"q": "D'où part la Via Podiensis vers Compostelle ?",
     "choix": ["Vézelay", "Arles", "Le Puy-en-Velay", "Paris"], "rep": "Le Puy-en-Velay"},
    {"q": "Quand Notre-Dame de Paris a-t-elle rouvert après l'incendie ?",
     "choix": ["2021", "2023", "2024", "2025"], "rep": "2024"},
    {"q": "Quelle fête célèbre-t-on le 2 février avec des crêpes ?",
     "choix": ["L'Épiphanie", "La Chandeleur", "Mardi gras", "L'Annonciation"], "rep": "La Chandeleur"},
    {"q": "Où repose le corps de sainte Bernadette ?",
     "choix": ["Lourdes", "Nevers", "Lisieux", "Tours"], "rep": "Nevers"},
]
