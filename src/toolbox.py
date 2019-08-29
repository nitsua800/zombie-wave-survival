import pygame
import math
import image_util

def getRotatedImage(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    new_rect = new_image.get_rect(center=rect.center)
    return new_image, new_rect
def angleBetweenPoints (x1, y1, x2, y2):
    x_difference = x2 - x1
    y_difference = y2 - y1
    angle = math.degrees(math.atan2(-y_difference, x_difference))
    return angle

class SoundManager:
    __instance = None
    _sound_library = {}

    @staticmethod
    def getInstance():
        if SoundManager.__instance == None:
            SoundManager()
        return SoundManager.__instance
    
    def __init__(self):
        if SoundManager.__instance != None:
            raise Exception("This class is a singleton.")
        else:
            SoundManager.__instance = self
            self.sound_library = {}
    
    def playSound(self, name):
        sound = self.sound_library.get(name)
        if sound == None:
            canonicalized_path = image_util.getImage(name)
            sound = pygame.mixer.Sound(canonicalized_path)
            self.sound_library[name] = sound
        sound.play()
