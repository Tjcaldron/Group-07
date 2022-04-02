from os import walk
import pygame

"""
Creates a pathway to call our files into game

"""
def import_folder(path):
    surface_list = []
    
    for _,__, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
            
        return surface_list
