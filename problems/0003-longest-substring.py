def length_of_longest_substring_string_solution(input_string: str) -> int:
    current_set: set[str] = set()
    current_string: str = ""
    longest_length: int = 0

    for char in input_string:
        if char in current_set:
            longest_length = max(longest_length, len(current_set))
            old_and_new_str = current_string.split(char)
            current_string = old_and_new_str[1]
            for char_to_del in old_and_new_str[0] + char:
                current_set.remove(char_to_del)
        current_set.add(char)
        current_string = current_string + char
    longest_length = max(longest_length, len(current_set))

    return longest_length

def length_of_longest_substring_sliding_windows_solution(input_string: str) -> int:
    seen: set[str] = set()
    left: int = 0
    max_len: int = 0

    for right in range(len(input_string)):
        while input_string[right] in seen:
            seen.remove(input_string[left])
            left += 1
        seen.add(input_string[right])
        max_len = max(max_len, right - left + 1)

    return max_len


def test_length_of_longest_substring_string_solution_case1() -> None:
    assert length_of_longest_substring_string_solution("abcabccbb") == 3

def test_length_of_longest_substring_string_solution_case2() -> None:
    assert length_of_longest_substring_string_solution("bbbbb") == 1

def test_length_of_longest_substring_string_solution_case3() -> None:
    assert length_of_longest_substring_string_solution("pwwkew") == 3

def test_length_of_longest_substring_string_solution_case4() -> None:
    assert length_of_longest_substring_string_solution(" ") == 1

def test_length_of_longest_substring_string_solution_case5() -> None:
    assert length_of_longest_substring_string_solution("jbpnbwwd") == 4

def test_length_of_longest_substring_sliding_windows_solution_case1() -> None:
    assert length_of_longest_substring_sliding_windows_solution("abcabccbb") == 3

def test_length_of_longest_substring_sliding_windows_solution_case2() -> None:
    assert length_of_longest_substring_sliding_windows_solution("bbbbb") == 1

def test_length_of_longest_substring_sliding_windows_solution_case3() -> None:
    assert length_of_longest_substring_sliding_windows_solution("pwwkew") == 3

def test_length_of_longest_substring_sliding_windows_solution_case4() -> None:
    assert length_of_longest_substring_sliding_windows_solution(" ") == 1

def test_length_of_longest_substring_sliding_windows_solution_case5() -> None:
    assert length_of_longest_substring_sliding_windows_solution("jbpnbwwd") == 4
