def is_comment(item):
    return isinstance(item, str) and item.startswith("#") #example of python short circuiting, second conditional won't be evaluated if isintance is false


def execute(program):
    """Executes a stack program

    Args:
        program: Any stack like containing where each item in the stack
            is a callable operator or non-callable operands. The top-most
            items in teh stack may be string beginning with # fro 
            the purpose of documentation. Stack-like means support for:

                item = stack.pop() #Remove and return the top item
                stack.append()  # Push an item to the top
                if stack:       #false when empty
    """
    # Find the starst of the 'program' by skipping
    # any item which is a comment
    while program:  #evaluates to false if empty
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break
    else: #no break    #used for "search failure handling since this only executes if all lines are comments."
        print("Empty program!")
        return

    # Evaluate the actual program
    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print("Error: ", e)
                break
            program.append(result)
            pending.clear()
        else:
            pending.append(item)
    else:
        print("Program successful.")
        print("Result: ", pending)

    print("Finished")


if __name__ == '__main__':
    import operator

    program = list(reversed((
        "# A short stack program to add",
        "# and multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))

    execute(program)
