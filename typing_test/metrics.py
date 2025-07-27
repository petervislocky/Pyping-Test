def wpm(chars: int, time: float):
    return (chars / 5) / time


def mistakes_count(backspace_count: int, ref_length: int, typed_length: int):
    return (ref_length / (typed_length + backspace_count)) * 100
