image rain_animated:
    "rain1.png"
    0.2
    "rain1.png"
    xzoom -1
    0.2
    "rain2.png"
    0.3
    "rain3.png"
    xzoom -1
    0.2
    repeat

image lightning_rev:
    "lightning.png"
    xzoom -1

image lightning_animated:
    choice 0.5:
        "lightning.png"
        alpha  0.0
        linear 0.3 alpha  1.0
        linear 0.3 alpha  0.0
        0.5

    choice 1.5:
        "lightning_rev"
        alpha  0.0
        linear 0.3 alpha  1.0
        linear 0.3 alpha  0.0
        0.5

    repeat
