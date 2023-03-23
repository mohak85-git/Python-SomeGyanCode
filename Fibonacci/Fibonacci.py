def fib(n: int) -> int:
    """_summary_

    Args:
        n (int): _description_

    Returns:
        int: _description_
    """
    val1 = 0
    val2 = 1
    result = None
    if n < 2:
        result = n
    else:
        for x in range(n-1):
            result = val1 + val2
            val1 = val2
            val2 = result
            
    return result


for i in range(21):
    print(f"{i}th fibonacci is {fib(i)}")
