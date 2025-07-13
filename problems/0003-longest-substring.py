def length_of_longest_substring_string_solution(input_string: str) -> int:
    current_set = set()
    current_string = ""
    longest_length = 0
    for c in input_string:
        if c in current_set:
            longest_length = max(longest_length, len(current_set))
            old_and_new_str = current_string.split(c)
            current_string = old_and_new_str[1]
            for c_del in old_and_new_str[0] + c:
                current_set.remove(c_del)
        current_set.add(c)
        current_string = current_string + c
    longest_length = max(longest_length, len(current_set))
    return longest_length

def length_of_longest_substring_sliding_windows_solution(input_string: str) -> int:
    seen = set()
    left = 0
    max_len = 0
    for right in range(len(input_string)):
        while input_string[right] in seen:
            seen.remove(input_string[left])
            left += 1
        seen.add(input_string[right])
        max_len = max(max_len, right - left + 1)
    return max_len


def test_one():
    result = length_of_longest_substring_string_solution("abcabccbb")
    assert result == 3

def test_two():
    result = length_of_longest_substring_string_solution("bbbbb")
    assert result == 1

def test_three():
    result = length_of_longest_substring_string_solution("pwwkew")
    assert result == 3

def test_four():
    result = length_of_longest_substring_string_solution(" ")
    assert result == 1

def test_five():
    result = length_of_longest_substring_string_solution("jbpnbwwd")
    assert result == 4