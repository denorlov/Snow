image blossoms = Fixed(
    SnowBlossom(im.FactorScale(im.Alpha("images/firefly1.png", 0.8), 0.6), count=25, yspeed=(-150,-75), xspeed=(-100,100)),
    SnowBlossom(im.FactorScale(im.Alpha("images/firefly1.png", 0.8), 0.6), count=25, xspeed=(-100,100)),
    SnowBlossom(im.FactorScale("images/firefly1.png", 1.1), count=150, start=5, xspeed=(-30,30), yspeed=-50, fast=True),
    SnowBlossom(im.FactorScale("images/firefly.png", 0.5), count=125, horizontal=True, fast=True)
)

