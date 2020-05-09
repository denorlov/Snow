define rain_type = "" # might be "" or "1-"

image rev_lightning:
    "lightning.png"
    xzoom -1

image rain:
    "rain[rain_type]1.png"
    0.2
    "rain[rain_type]3.png"
    0.2
    "rain[rain_type]2.png"
    0.2
    repeat

image lightning:
    choice:        #weight of choice is 1
        "lightning.png"
        alpha  0.0
        0.5                 # show nothing for 0.5 seconds

    choice 0.1:   #weight of choice is 0.1
        "lightning.png"
        alpha  0.0
        linear 0.3 alpha  1.0
        linear 0.3 alpha  0.0

    choice 0.1:
        "rev_lightning"
        alpha  0.0
        linear 0.3 alpha  1.0
        linear 0.3 alpha  0.0

    repeat