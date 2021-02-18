class EntriesMeta(type):

    def __new__(mcs, name, bases, namespace, **kwargs):
        print("Entires.__new__(mcs, name, bases, namespace, **kwargs)")
        print(" kwargs =", kwargs)
        num_entries = kwargs['num_entries']
        print(" num_entries =", num_entries)
        namespace.update({chr(i): i for i in range(ord('a'), ord('a')+num_entries)})
        print(" namespace =", namespace)
        cls = super().__new__(mcs, name, bases, namespace)
        return cls
