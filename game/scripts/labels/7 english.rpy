init python:

    # 7 english
    labels.extend([
        {
            "name": "english1",
            "jump": ["eng1ascension"],
            "pos": (15, 0),
            "colour": colour.red,
        },
        {
            "name": "eng1ascension",
            "jump": ["english1top", "english1flight3", "dead"],
            "pos": (15, 1),
            "colour": colour.red,
        },
        {
            "name": "english1flight3",
            "jump": ["english1top", "dead"],
            "pos": (15, 2),
            "colour": colour.red,
        },
        {
            "name": "english1top",
            "jump": "mthext1day1",
            "pos": (15, 3),
            "colour": colour.red,
        },
        {
            "name": "eng1waitforschlammie",
            "jump": "mthext1day1",
            "pos": (15, 4),
            "colour": colour.red,
        },
    ])