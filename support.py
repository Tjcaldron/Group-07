from os import walk
import pygame


def import_folder(path):
    surface_list = []
    
    for _,__, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
            
        return surface_list
    
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
    
    # for _,__, wav_files in walk(path):
    #     for wav in wav_files:
    #         full_path = path + '/' + wav
    #         wav_playlist = pygame.wav.load(full_path).convert_alpha()
    #         music_playlist.append(wav_playlist)
            
    #     return music_playlist
    pass