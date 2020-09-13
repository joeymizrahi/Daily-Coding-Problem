def solution(numbers, k):
    """Given a list of numbers, return whether any two sums to k. 
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    Bonus: Can you do this in one pass?
    """
    s = set()
    for num in numbers:
        if k-num in s:
            return True
        s.add(num)
    return False


assert solution([10, 15, 3, 7], 17) == True
assert solution([-1, 14, 3, 7], 13) == True
assert solution([-1, 15, 3, 7], 17) == False
assert solution([17, 0], 17) == True
