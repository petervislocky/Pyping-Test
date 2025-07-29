def wpm(typed_chars: int, time_minutes: float):
    return (typed_chars / 5) / time_minutes


def adjusted_wpm(typed_chars: int, mistakes: int, time_minutes: float):
    return ((typed_chars - mistakes) / 5) / time_minutes


def accuracy(backspace_count: int, ref_length: int, typed_length: int):
    return (ref_length / (typed_length + backspace_count)) * 100
