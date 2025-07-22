def happy_number(n: int) -> bool:
    slow = fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))
        if fast == 1:
            return True
        elif fast == slow:
            return False

def get_next_num(n: int) -> int:
    total_sum = 0
    while n > 0:
        digit = n % 10
        total_sum += digit * digit
        n //= 10
    return total_sum