def wpm(chars, time):
    return (chars / 5) / time

def mistakes_count(backspace_count, ref_length, typed_length):
    return (ref_length / (typed_length + backspace_count)) * 100
