class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, sub):
        return (hasattr(sub, 'swipe') and callable(sub.swipe)
                and
                hasattr(sub, 'sharpen') and callable(sub.sharpen))


#Sword plays role of virtual base class
class Sword(metaclass=SwordMeta):
    pass

class BroadSword:

    def swipe(self):
        print("Swoosh!")

    def sharpen(self):
        print("Shrink!")


class SamuraiSword:

    def swipe(self):
        print("Slice!")
    
    def sharpen(self):
        print("Shrink!")


class Rifle:

    def fire(self):
        print("Bang!")

