screen say_text(text1):
    drag:
        drag_name "say"
        yalign 1.0
        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        window id "window":
            xmaximum 600

            has vbox

            label "Hint" xmaximum 400
            text text1
            textbutton "Закрыть" action Return()
