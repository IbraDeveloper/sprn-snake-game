from pygame import mixer

mixer.init()

click_sound = mixer.Sound("sound/click-button.mp3")
eat_sound = mixer.Sound("sound/eat.mp3")
game_over_sound = mixer.Sound("sound/game-over.mp3")



def play_click():
    click_sound.play()
    
def play_eat():
    eat_sound.play()
    
def play_game_over():
    game_over_sound.play()
