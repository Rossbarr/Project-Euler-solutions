nums = {1 : 1, 2 : 2, 4 : 3}

def next_num(x: int):
    if x % 2 == 0:
        result = x/2
    else:
        result = 3*x + 1
    
    return result

def recursive_part(num: int, nums: dict):
    if nums.setdefault(num, False):
        return nums[num]

    seq_length = recursive_part(next_num(num), nums) + 1
    nums[num] = seq_length
    return seq_length

def collatz_length(nums: dict):
    longest_seq_length = 0
    longest_seq_num = 0

    i = 1
    while i < 1000000:
        print(i)
        seq_length = recursive_part(i, nums)
        if seq_length > longest_seq_length:
            longest_seq_length = seq_length
            longest_seq_num = i
        i += 1

    return longest_seq_num, longest_seq_length

print(collatz_length(nums))
