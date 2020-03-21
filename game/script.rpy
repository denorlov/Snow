default speed = 10

screen volume_controls():
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            bar:
                value VariableValue("speed", 100, 1.0)
                changed Jump("start")
                xsize 500
                style "slider"
            textbutton "применить":
                action Jump("start")

image big = "Big.png"
image sno1 = "snow1.png"
image sno2 = "snow2.png"
image sno3 = "snow3.png"

transform snow1:
    xalign 0.0 yalign 1.0
    linear speed + 5.5 yalign 0.0
    repeat

transform snow2:
    xalign 0.0 yalign 1.0
    linear speed + 6.5 yalign 0.0
    repeat

transform snow3:
    xalign 0.0 yalign 1.0
    linear speed + 7.5 yalign 0.0
    repeat

# Игра начинается здесь:
label start:
    window hide

    show big
    show sno3 at snow3
    show sno2 at snow2
    show sno1 at snow1

    window hide

    show screen volume_controls
    pause

    return
