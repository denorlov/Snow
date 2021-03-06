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
    parallel:
        yalign 1.0
        linear speed + 6.5 yalign 0.0
        repeat
    parallel:
        xalign 0.0
        linear speed + 6.5 xalign +0.8
        repeat

transform snow3:
    parallel:
        yalign 1.0
        linear speed + 7.5 yalign 0.0
        repeat
    parallel:
        xalign 0.0
        linear speed + 7.5 xalign -0.8
        repeat
