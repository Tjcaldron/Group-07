from pygame import mixer

mixer.init()


class Playlist():
    
    class Sounds():
        
        def eng_module(self):
            eng_bckgnd_music= mixer.music.load('sound\english_bckgnd_lofi.wav')
            play_eng = mixer.music.play(-1)
            self.eng_playlist = eng_bckgnd_music, play_eng
            return self.eng_playlist
        def math_module(self):
            math_bckgnd_music= mixer.music.load('sound\math_bckgnd_classical.wav')
            play_math = mixer.music.play(-1)
            self.math_playlist = math_bckgnd_music, play_math
            return self.math_playlist
        def science_module(self):
            pass
    
# math_back_loop = pygame.mixer.Sound("filepath.wav")
# If NOT WAV, won't work 