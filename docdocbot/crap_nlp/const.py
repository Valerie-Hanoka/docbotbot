#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
const.py is part of the project docbotbot
Author: Valérie Hanoka

"""

# Token separator
TOK_SEP = 'ʬ'

# Sentence sepatator
SENT_SEP = 'ʭ'

# Stopwords list
STOP_WORDS = [
    "#docstoctoc",
    "#doctoctoc",
    "a",
    "a",
    "afin",
    "ah",
    "ai",
    "ai",
    "aie",
    "aient",
    "aies",
    "ait",
    "alors",
    "après",
    "as",
    "attendu",
    "au",
    "au",
    "au-delà",
    "au-devant",
    "aucun",
    "aucune",
    "audit",
    "auprès",
    "auquel",
    "aura",
    "aurai",
    "auraient",
    "aurais",
    "aurait",
    "aurait",
    "auras",
    "aurez",
    "auriez",
    "aurions",
    "aurons",
    "auront",
    "aussi",
    "aussi",
    "autour",
    "autre",
    "autre",
    "autres",
    "autrui",
    "aux",
    "aux",
    "auxdites",
    "auxdits",
    "auxquelles",
    "auxquels",
    "avaient",
    "avais",
    "avait",
    "avant",
    "avec",
    "avec",
    "avez",
    "avez",
    "aviez",
    "avions",
    "avoir",
    "avons",
    "ayant",
    "ayez",
    "ayons",
    "b",
    "bah",
    "banco",
    "ben",
    "bien",
    "bonjour",
    "bé",
    "c",
    "c",
    "c'",
    "c'est",
    "c'était",
    "ca",
    "car",
    "car",
    "ce",
    "ce",
    "ceci",
    "cela",
    "celle",
    "celle-ci",
    "celle-là",
    "celles",
    "celles-ci",
    "celles-là",
    "celui",
    "celui-ci",
    "celui-là",
    "celà",
    "cent",
    "cents",
    "cependant",
    "certain",
    "certaine",
    "certaines",
    "certains",
    "ces",
    "cet",
    "cette",
    "cette",
    "ceux",
    "ceux-ci",
    "ceux-là",
    "cf.",
    "cg",
    "cgr",
    "chacun",
    "chacune",
    "chaque",
    "chez",
    "chez",
    "ci",
    "cinq",
    "cinquante",
    "cinquante-cinq",
    "cinquante-deux",
    "cinquante-et-un",
    "cinquante-huit",
    "cinquante-neuf",
    "cinquante-quatre",
    "cinquante-sept",
    "cinquante-six",
    "cinquante-trois",
    "cl",
    "cm",
    "cm²",
    "comme",
    "comme",
    "comment",
    "contre",
    "d",
    "d",
    "d'",
    "d'après",
    "d'un",
    "d'une",
    "dans",
    "dans",
    "de",
    "de",
    "depuis",
    "depuis",
    "derrière",
    "des",
    "des",
    "desdites",
    "desdits",
    "desquelles",
    "desquels",
    "deux",
    "devant",
    "devers",
    "dg",
    "différentes",
    "différents",
    "dire",
    "dis",
    "dit",
    "dites",
    "divers",
    "diverses",
    "dix",
    "dix-huit",
    "dix-neuf",
    "dix-sept",
    "dl",
    "dm",
    "doit",
    "donc",
    "donc",
    "dont",
    "douze",
    "du",
    "du",
    "dudit",
    "duquel",
    "durant",
    "dès",
    "déjà",
    "déjà",
    "e",
    "e",
    "eh",
    "elle",
    "elle",
    "elles",
    "en",
    "en",
    "en-dehors",
    "encore",
    "enfin",
    "en train"
    "entre",
    "entre",
    "envers",
    "es",
    "est",
    "est",
    "et",
    "et",
    "eu",
    "eu",
    "eue",
    "eues",
    "euh",
    "eurent",
    "eus",
    "eusse",
    "eussent",
    "eusses",
    "eussiez",
    "eussions",
    "eut",
    "eux",
    "exemple",
    "eûmes",
    "eût",
    "eûtes",
    "f",
    "f",
    "faire",
    "fais",
    "fait",
    "fait",
    "faites",
    "faut",
    "fi",
    "flac",
    "fors",
    "furent",
    "fus",
    "fusse",
    "fussent",
    "fusses",
    "fussiez",
    "fussions",
    "fut",
    "fûmes",
    "fût",
    "fûtes",
    "h",
    "ha",
    "han",
    "hein",
    "help",
    "hem",
    "heu",
    "hg",
    "hier",
    "hl",
    "hm",
    "hm³",
    "holà",
    "hop",
    "hormis",
    "hors",
    "huit",
    "hum",
    "hé",
    "i",
    "ici",
    "il",
    "il",
    "ils",
    "j",
    "j",
    "j'",
    "j'ai",
    "j'avais",
    "j'étais",
    "jamais",
    "je",
    "je",
    "jusqu'",
    "jusqu'au",
    "jusqu'aux",
    "jusqu'à",
    "jusque",
    "juste",
    "k",
    "km",
    "km²",
    "l",
    "l",
    "l'",
    "l'autre",
    "l'on",
    "l'un",
    "l'une",
    "la",
    "la",
    "laquelle",
    "le",
    "le",
    "lequel",
    "les",
    "les",
    "lesquelles",
    "lesquels",
    "leur",
    "leurs",
    "lez",
    "lors",
    "lorsqu'",
    "lorsque",
    "lui",
    "lui",
    "là",
    "lès",
    "m",
    "m",
    "m'",
    "ma",
    "ma",
    "maint",
    "mainte",
    "maintes",
    "maints",
    "mais",
    "mais",
    "malgré",
    "me",
    "me",
    "merci",
    "mes",
    "mes",
    "mgr",
    "mil",
    "mille",
    "milliards",
    "millions",
    "ml",
    "mm",
    "mm²",
    "moi",
    "moi",
    "moins",
    "mon",
    "mon",
    "moyennant",
    "mt",
    "m²",
    "m³",
    "même",
    "mêmes",
    "n",
    "n",
    "n'avait",
    "n'y",
    "ne",
    "neuf",
    "ni",
    "non",
    "nonante",
    "nonobstant",
    "nos",
    "notre",
    "nous",
    "nul",
    "nulle",
    "nº",
    "néanmoins",
    "o",
    "octante",
    "oh",
    "on",
    "on",
    "ont",
    "ont",
    "onze",
    "or",
    "ou",
    "ou",
    "oui",
    "outre",
    "où",
    "p",
    "par",
    "par",
    "par-delà",
    "parbleu",
    "parce",
    "parmi",
    "pas",
    "pas",
    "passé",
    "pendant",
    "personne",
    "peu",
    "peut",
    "peux",
    "plus",
    "plus_d'un",
    "plus_d'une",
    "plusieurs",
    "plusieurs",
    "plutôt",
    "poke",
    "possible",
    "pour",
    "pour",
    "pourquoi",
    "pourquoi",
    "pourtant",
    "pourvu",
    "près",
    "puisqu'",
    "puisque",
    "q",
    "qu",
    "qu",
    "qu'",
    "qu'elle",
    "qu'elles",
    "qu'il",
    "qu'ils",
    "qu'on",
    "quand",
    "quand",
    "quant",
    "quarante",
    "quarante-cinq",
    "quarante-deux",
    "quarante-et-un",
    "quarante-huit",
    "quarante-neuf",
    "quarante-quatre",
    "quarante-sept",
    "quarante-six",
    "quarante-trois",
    "quatorze",
    "quatre",
    "quatre-vingt",
    "quatre-vingt-cinq",
    "quatre-vingt-deux",
    "quatre-vingt-dix",
    "quatre-vingt-dix-huit",
    "quatre-vingt-dix-neuf",
    "quatre-vingt-dix-sept",
    "quatre-vingt-douze",
    "quatre-vingt-huit",
    "quatre-vingt-neuf",
    "quatre-vingt-onze",
    "quatre-vingt-quatorze",
    "quatre-vingt-quatre",
    "quatre-vingt-quinze",
    "quatre-vingt-seize",
    "quatre-vingt-sept",
    "quatre-vingt-six",
    "quatre-vingt-treize",
    "quatre-vingt-trois",
    "quatre-vingt-un",
    "quatre-vingt-une",
    "quatre-vingts",
    "que",
    "que",
    "quel",
    "quel",
    "quelle",
    "quelle",
    "quelles",
    "quelqu'",
    "quelqu'un",
    "quelqu'une",
    "quelque",
    "quelques",
    "quelques-unes",
    "quelques-uns",
    "quels",
    "qui",
    "qui",
    "quiconque",
    "quinze",
    "quoi",
    "quoi",
    "quoiqu'",
    "quoique",
    "qqu",
    "qq",
    "qlq",
    "r",
    "revoici",
    "revoilà",
    "rien",
    "s",
    "s",
    "s'",
    "sa",
    "sa",
    "sans",
    "sauf",
    "se",
    "se",
    "seize",
    "selon",
    "sept",
    "septante",
    "sera",
    "serai",
    "seraient",
    "serais",
    "serait",
    "seras",
    "serez",
    "seriez",
    "serions",
    "serons",
    "seront",
    "ses",
    "ses",
    "si",
    "si",
    "sinon",
    "six",
    "soi",
    "soient",
    "sois",
    "soit",
    "soit",
    "soixante",
    "soixante-cinq",
    "soixante-deux",
    "soixante-dix",
    "soixante-dix-huit",
    "soixante-dix-neuf",
    "soixante-dix-sept",
    "soixante-douze",
    "soixante-et-onze",
    "soixante-et-un",
    "soixante-et-une",
    "soixante-huit",
    "soixante-neuf",
    "soixante-quatorze",
    "soixante-quatre",
    "soixante-quinze",
    "soixante-seize",
    "soixante-sept",
    "soixante-six",
    "soixante-treize",
    "soixante-trois",
    "sommes",
    "son",
    "son",
    "sont",
    "sont",
    "sous",
    "soyez",
    "soyons",
    "suis",
    "suis",
    "suite",
    "sur",
    "sur",
    "sus",
    "svp",
    "t",
    "t",
    "t'",
    "ta",
    "tacatac",
    "tandis",
    "te",
    "tel",
    "telle",
    "telles",
    "tels",
    "tes",
    "toi",
    "ton",
    "touitteur",
    "toujours",
    "tous",
    "tout",
    "toute",
    "toutefois",
    "toutes",
    "treize",
    "trente",
    "trente-cinq",
    "trente-deux",
    "trente-et-un",
    "trente-huit",
    "trente-neuf",
    "trente-quatre",
    "trente-sept",
    "trente-six",
    "trente-trois",
    "trois",
    "très",
    "tu",
    "twitter",
    "u",
    "un",
    "un",
    "une",
    "une",
    "unes",
    "uns",
    "v",
    "vers",
    "via",
    "vingt",
    "vingt-cinq",
    "vingt-deux",
    "vingt-huit",
    "vingt-neuf",
    "vingt-quatre",
    "vingt-sept",
    "vingt-six",
    "vingt-trois",
    "vis-à-vis",
    "voici",
    "voilà",
    "vos",
    "vos",
    "votre",
    "votre",
    "vous",
    "vous",
    "w",
    "x",
    "y",
    "y",
    "z",
    "zéro",
    "à",
    "à",
    "ç'",
    "ça",
    "ça",
    "ès",
    "étaient",
    "étais",
    "était",
    "étant",
    "étiez",
    "étions",
    "été",
    "été",
    "étée",
    "étées",
    "étés",
    "êtes",
    "être",
    "être",
]
