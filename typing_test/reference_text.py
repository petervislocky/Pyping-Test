from typing import Any
import json
import random


def load_json(path: str) -> dict[str, Any] | None:
    """Helper method to load words in from JSON"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON: {e}")


class ReferenceText:
    """
    Instantiating this class generates a list, if `word_count` is given
    (not None), separated by char, of random words from the words JSON,
    based on the difficulty setting given and stores it in an instance
    var to be retrieved by the getter.

    `gen_reference_text` can be called again on the instance to add
    more words to the list.
    """

    words = load_json("words.json")

    def __init__(self, word_count: int | None, difficulty_setting: str):
        self.word_count = word_count
        self.difficulty = []
        self._get_difficulty_setting(difficulty_setting)
        # Initially I handled the word gen here by calling
        # `gen_reference_text` within the class but this was allows me
        # to generate more text (for timed mode) by calling
        # `gen_reference_text` outside the class and adding the new text
        # below
        self.selected_words = []
        self.selected_chars = []

        if word_count is not None:
            self.gen_reference_text(word_count)

    # TODO: add a weighting system to prevent the same word back to back
    def gen_reference_text(self, count: int) -> None:
        """
        Makes random choices from the words json based on the difficulty
        selected.

        Appends selected words to `self.selected_words` and individual
        chars to `self.selected_chars`
        """
        for _ in range(count):
            diff_level = random.choice(self.difficulty)
            # have to include the else incase words JSON isn't found
            word = random.choice(self.words[diff_level]) if self.words else ""
            self.selected_words.append(word)

        self.selected_chars = list(" ".join(self.selected_words))

    def _get_difficulty_setting(self, difficulty_setting: str) -> None:
        """
        Logic for controlling what words get added to the reference
        text based on difficulty setting.

        Each setting includes the previous settings' associated words
        """
        match difficulty_setting:
            case "easy":
                self.difficulty.append("easy")
            case "medium":
                self.difficulty.extend(["easy", "medium"])
            case "hard":
                self.difficulty.extend(["easy", "medium", "hard"])
            case "veryHard":
                self.difficulty.extend(["easy", "medium", "hard", "veryHard"])
            case _:
                # using assert False here because this line should never execute unless something
                # has gone very wrong, any malformed difficulty setting should be caught in main()
                assert False, f"Unexpected difficulty setting, {difficulty_setting}"

    def get_selected_chars(self) -> list[str]:
        """
        Getter method for getting the reference text list that's been
        generated
        """
        return self.selected_chars
