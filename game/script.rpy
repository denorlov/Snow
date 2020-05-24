image sky_with_clouds:
    contains:
        xalign 0.0
        yalign 0.0
        "bg fire sky.png"
    contains:
        pause 1.0
        HBox("clouds/Cloud 2.png", "clouds/Cloud 2.png")
        xalign 1.0
        yalign 0.01
        alpha 0.5
        linear 20 xpos 0.0
        repeat
    contains:
        xalign 0.0
        yalign 0.0
        "bg fire mountain.png"
    contains:
        HBox("clouds/Cloud 11.png", "clouds/Cloud 11.png")
        xalign 1.0
        yalign 0.01
        linear 12 xpos 0.0
        repeat
    contains:
        xalign 0.0
        yalign 0.0
        "bg fire mid mountain.png"
    contains:
        HBox("clouds/Cloud 1.png", "clouds/Cloud 1.png")
        xalign 1.0
        yalign 0.2
        alpha 0.9
        linear 15 xpos 0.0
        repeat
    contains:
        HBox("clouds/Cloud 14.png", "clouds/Cloud 11.png")
        xalign 1.0
        yalign 0.02
        linear 20 xpos 0.0
        repeat
    contains:
        HBox("clouds/Cloud 14.png", "clouds/Cloud 15.png")
        xalign 1.0
        yalign 0.04
        linear 24 xpos 0.0
        repeat
    contains:
        xalign 0.0
        yalign 0.0
        "bg fire bottom.png"

label start:
    # дождь
#    show big
#    show bg swamp dead

#    show lightning
#    show rain

    # снег
#    show sno3 at snow3
#    show sno2 at snow2
#    show sno1 at snow1

#    window hide
#    pause

    # облака
    scene sky_with_clouds
    "Просто сиди и смотри"
    return

