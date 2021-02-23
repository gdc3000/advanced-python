import functools

def invariant(predicate):
    """Create a class decorator which checks a class invariant.

    Args:
        predicate: A callable to which, after every method invocation, the object
            on which the method was called will be passed. The predicate should evaluate
            to True if the class invariant has been maintained, or False if it has been
            violated.
        
    Returns:
        A class decorator for checking the class invariant tested by the supplied
            predicate function.
    """

    def invariant_checking_class_decorator(cls):
        """A class decorator for checking invariants."""

        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_invariant_checking_proxy(cls, name, predicate)
        
        return cls

    return invariant_checking_class_decorator


def _wrap_method_invariant_checking_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)

    @functools.wraps(method)
    def invariant_checking_class_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(predicate.__doc__, self))
        return result
    
    setattr(cls, name, invariant_checking_class_decorator)


def not_below_absolute_zero(temperature):
    """Temperature not below absolute zero"""
    return temperature._kelvin >= 0
    

@invariant(not_below_absolute_zero)
class Temperature:

    def __init__(self, kelvin):
        self._kelvin = kelvin