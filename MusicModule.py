from playsound import playsound


def play(speed=1):
    if speed < 1:
        playsound('Media/Sample_half.mp3')
    elif speed < 5:
        playsound('Media/Sample.mp3')
    elif speed < 20:
        playsound('Media/Sample_2.mp3')
    else:
        playsound('Media/Sample_3.mp3')
