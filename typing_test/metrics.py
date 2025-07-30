def wpm(typed_chars: int, time_minutes: float):
    return (typed_chars / 5) / time_minutes


def adjusted_wpm(typed_chars: int, mistakes: int, time_minutes: float):
    return ((typed_chars - mistakes) / 5) / time_minutes


def count_mistakes(typed_text: list[str], reference_text: list[str]):
    mistakes = 0
    for i, char in enumerate(typed_text):
        if i < len(reference_text) and char != reference_text[i]:
            mistakes += 1
    return mistakes


def accuracy(backspace_count: int, ref_length: int, typed_length: int):
    return (ref_length / (typed_length + backspace_count)) * 100


# TODO: Write a separate accuracy method for the timed test that doesn't
# use the length of reference_text and accounts for corrected mistakes
# as well as uncorrected ones
