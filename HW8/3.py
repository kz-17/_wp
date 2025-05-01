def classify_even_odd(numbers):
    result = {
        "even": [num for num in numbers if num % 2 == 0], 
        "odd": [num for num in numbers if num % 2 != 0]  
    }
    return result
