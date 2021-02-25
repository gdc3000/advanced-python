from abc import ABC

class Sword(ABC):

    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))
                or NotImplemented)
    
    def thrust(self):
        print("Thrusting..")


class BroadSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shrink!")


@Sword.register
class LightSaber:

    def swipe(self):
        print("Ffffffffkrshhzwooom...woom")


class SamuraiSword:

    def swipe(self):
        print("Slice!")
    
    def sharpen(self):
        print("Shrink!")


class Rifle:

    def fire(self):
        print("Bang!")

