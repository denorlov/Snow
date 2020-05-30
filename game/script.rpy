label start:
    # дождь
#    show big
#    show bg swamp dead

#    show lightning_animated
#    show rain_animated

    # снег
#    show sno3 at snow3
#    show sno2 at snow2
#    show sno1 at snow1

    # облака
#    scene sky_with_clouds

    # светляки
    show blossoms

    # Add the repulsor to the screen.
    show expression repulsor as repulsor

    "..."

    hide repulsor

    # Clean up.
    python:
        del repulsor
        del repulsor_sprites
        del repulsor_pos

    "Просто сиди и смотри"

#    window hide
#    pause

    return