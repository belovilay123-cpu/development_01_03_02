def print_from_a_to_b(a, b):
    print(a)
    if a == b:
        return
    
    if a < b:
        print_from_a_to_b(a + 1, b)
    else:
        print_from_a_to_b(a - 1, b)
        