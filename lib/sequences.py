def print_fibonacci(length):
    if length == 0:
        print([])  
        return
    elif length < 0:
        print("Length must be a positive integer.")
        return
    
    
    fibonacci_sequence = [0, 1]
    
    
    for i in range(2, length):
        next_value = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_value)
    
    
    if length == 1:
        fibonacci_sequence = [0]
    

    print(fibonacci_sequence)

