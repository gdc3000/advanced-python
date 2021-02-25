from abc import ABC, abstractmethod

class Sword(ABC):

    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'thrust') and callable(sub.thrust)
                and
                hasattr(sub, 'parry') and callable(sub.parry)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))
                or NotImplemented)
    
    @abstractmethod
    def swipe(self):
        raise NotImplementedError

    @abstractmethod
    def thrust(self):
        print("Thrusting..")

    @abstractmethod
    def parry(self):
        raise NotImplementedError


class BroadSword(Sword):

    def swipe(self):
        print("Swoosh!")

    def thrust(self):
        super().thrust()

    def parry(self):
        print("Parry!")

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

