########################################################################################################################
screen fortmap:
    modal True
    use diary_nav
    imagemap:
        ground loadImage("screen_bg_map.png")
        hover  loadImage("screen_bg_map_selected.png")
        idle   loadImage("screen_bg_map_unavailable.png")

        if "rowe" in game.allowedAreas:
            hotspot (945, 85, 85, 75) clicked Return(1)
        if "kilgour" in game.allowedAreas:
            hotspot (827, 175, 205, 37) clicked Return(2)
        if "rquad" in game.allowedAreas:
            hotspot (840, 80, 100, 45) clicked Return(3)
        if "library" in game.allowedAreas:
            hotspot (784, 123, 115, 33) clicked Return(4)
        if "gym" in game.allowedAreas:
            hotspot (730, 104, 60, 83) clicked Return(5)
        if "food" in game.allowedAreas:
            hotspot (650, 160, 90, 35) clicked Return(6)
        if "valley" in game.allowedAreas:
            hotspot (350, 150, 250, 170) clicked Return(7)
        if "oval" in game.allowedAreas:
            hotspot (320, 305, 350, 190) clicked Return(8)
        if "currycourts" in game.allowedAreas:
            hotspot (225, 507, 203, 163) clicked Return(9)
        if "bcourts" in game.allowedAreas:
            hotspot (500, 500, 200, 180) clicked Return(10)
        if "carpark" in game.allowedAreas:
            hotspot (700, 480, 186, 202) clicked Return(11)
        if "fortstreet" in game.allowedAreas:
            hotspot (890, 475, 72, 207) clicked Return(12)
        if "bridge" in game.allowedAreas:
            hotspot (1225, 325, 126, 60) clicked Return(13)
        if "place" in game.allowedAreas:
            hotspot (1080, 240, 108, 119) clicked Return(14)
        if "wilkins" in game.allowedAreas:
            hotspot (966, 273, 95, 77) clicked Return(15)
        if "quad" in game.allowedAreas:
            hotspot (910, 320, 62, 56) clicked Return(16)
        if "cohen" in game.allowedAreas:
            hotspot (755, 405, 133, 54) clicked Return(17)
        if "hall" in game.allowedAreas:
            hotspot (800, 305, 102, 88) clicked Return(18)
        if "lquad" in game.allowedAreas:
            hotspot (775, 245, 103, 55) clicked Return(19)
        if "lkilgour" in game.allowedAreas:
            hotspot (660, 225, 117, 67) clicked Return(20)
        if "uqad" in game.allowedAreas:
            hotspot (890, 220, 108, 56) clicked Return(21)