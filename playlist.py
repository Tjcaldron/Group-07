from os import walk
import pygame
# Mixer needs to be called for sound
# mixer.init()
# # mixer.music.load("sound\english_bckgnd_lofi.wav")
# mixer.music.play(-1)    
def import_playlist(path):
    """
    Test code implementation for audio...might need to be it's own
    separate file. Will follow same logic but needs to be separate. 
    This support file can only handle image paths with the surface func.
    Add to player file...Create: Def import_character_sounds...within
    player file. 1:11:29 ---1:21:30 check methods when udpated to see
    where to implement collision sounds.Continue1:48:55
    """
    music_playlist = []
    
    for _,__, wav_files in walk(path):
        for wav in wav_files:
            full_path = path + '/' + wav
            wav_playlist = pygame.wav.load(full_path).convert_alpha()
            music_playlist.append(wav_playlist)
            
        return music_playlist
    pass