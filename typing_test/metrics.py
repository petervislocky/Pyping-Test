def wpm(typed_chars: int, time_minutes: float) -> float:
    return (typed_chars / 5) / time_minutes


def adjusted_wpm(typed_chars: int, mistakes: int, time_minutes: float) -> float:
    return ((typed_chars - mistakes) / 5) / time_minutes


def accuracy(backspace_count: int, ref_length: int, typed_length: int) -> float:
    """
    Used for perfect mode only.
    Relies on the length of `reference_text`
    """
    return (ref_length / (typed_length + backspace_count)) * 100


# TODO: add backspace count to this because I just realized this will
# only count the mistakes that are not backspaced, so counting
# backspaces will account for that, but ill make it only take off half
# a percent so as not to punish as heavily as a mistake or something
# like that
def timed_accuracy(typed_text: list[str], reference_text: list[str]) -> float:
    """
    Used for timed mode only.

    Adds 1 to `correct` for every char in `typed_text` that matches the
    corresponding char in `reference_text` if `reference_text` is not
    done yet.

    Divides num of correct keys by the lenght of `typed_text` and * by
    100 to get the accuracy percentage.
    """
    correct = sum(
        1
        for i, char in enumerate(typed_text)
        if i < len(reference_text) and char == reference_text[i]
    )
    total = len(typed_text)
    return (correct / total) * 100


def find_mistakes(typed_text: list[str], reference_text: list[str]) -> int:
    """Function to find and count mistakes"""
    mistakes = 0
    for i, char in enumerate(reference_text):
        if i >= len(typed_text):
            break
        if typed_text[i] != char:
            mistakes += 1
    return mistakes
