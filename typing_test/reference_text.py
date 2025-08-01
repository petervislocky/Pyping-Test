import json
import random


def load_json(path: str):
    """helper method to load words in from JSON"""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON: {e}")


class ReferenceText:
    """
    instantiating this class generates a list, separated by char,
    of random words from the words list, based on the difficulty
    setting given and stores it in an instance var to be retrieved by
    the getter
    """

    words = load_json("words.json")

    def __init__(self, word_count: int, difficulty_setting: str):
        self.word_count = word_count  # remember to handle improper value
        self.difficulty = []
        self.get_difficulty_setting(difficulty_setting)
        self.selected_words = self.gen_reference_text()
        self.selected_chars = list(self.selected_words)

    def gen_reference_text(self):
        """
        makes random choices from the words dictionary based on the
        difficulty selected
        """
        selected_words = []

        for _ in range(self.word_count):
            diff_level = random.choice(self.difficulty)
            # have to include the else incase words JSON isn't found
            word = random.choice(self.words[diff_level]) if self.words else ""
            selected_words.append(word)

        return " ".join(selected_words)

    def get_selected_chars(self):
        """
        getter method for getting the reference text list that's been
        generated
        """
        return self.selected_chars

    def get_difficulty_setting(self, difficulty_setting: str):
        """
        logic for controlling what words get added to the reference
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
