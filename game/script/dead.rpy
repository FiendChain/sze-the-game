label dead:
    scene black
    sze "I dead"
    menu:
        "Return to Last Choice":
            return
        "Return to start":
            # theoretically if you died like 5000 times, you will run out of ram and your pc is die.
            scene bg ded
            with fade
            "The Lord of Light has granted me another chance..."
            jump start

label deadrestart:
    scene bg ded
    sze "I dead"
    jump start
    
    
# HSPs +3 strength, -1 intel
# fish and chips +2 intel
# pho +1 strength +1 intel +1 thirst
# pork rolls +2 charm
# vegan shite = +3 fort -1 strength -1 dikfriendship