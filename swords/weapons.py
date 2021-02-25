from abc import ABCMeta

class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))


#Sword plays role of virtual base class
class Sword(metaclass=ABCMeta):

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

