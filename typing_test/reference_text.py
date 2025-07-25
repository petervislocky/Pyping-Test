import random


class ReferenceText:


    words = {
        'easy': [
            'the', 'and', 'is', 'you', 'that', 'it', 'in', 'of', 'to', 'a', 'was', 'for', 'apple',
            'house', 'green', 'water', 'train', 'smile', 'light', 'music', 'on', 'table', 'happy',
            'quick', 'dream', 'stone', 'laugh', 'chair', 'world', 'sleep', 'phone', 'clock',
            'voice', 'sun', 'blue', 'run', 'dog', 'cat', 'car', 'bird', 'milk', 'jump', 'hand',
            'book', 'tree', 'play', 'ball', 'fish', 'baby', 'cup', 'star', 'fire', 'food'
        ],
        'medium': [
            'picture', 'thunder', 'journey', 'blanket', 'capture', 'forward', 'message', 'bicycle',
            'puzzle', 'improve', 'careful', 'recycle', 'feather', 'airport', 'perfect', 'library',
            'plastic', 'courage', 'holiday', 'canvas', 'bridge', 'gather', 'damage', 'handle',
            'signal', 'shadow', 'rescue', 'yellow', 'danger', 'honest', 'castle', 'nature',
            'rocket', 'animal', 'wander', 'harvest', 'luggage', 'passion', 'mirror'
        ],
        'hard': [
            'calendar', 'diamond', 'elephant', 'factory', 'garage', 'history', 'internet',
            'justice', 'kitchen', 'language', 'magnet', 'necktie', 'octopus', 'picture',
            'question', 'rescue', 'science', 'traffic', 'vacuum', 'weather', 'balance', 'capture',
            'density', 'freedom', 'journey', 'library', 'monitor', 'network', 'package', 'quality',
            'recycle', 'storage', 'victory'
            ],
        'veryHard': [
            'quarantine', 'silhouette', 'kaleidoscope', 'subconscious', 'reminiscent', 'hypocrisy',
            'miscellaneous', 'picturesque', 'jeopardize', 'bureaucracy', 'acquiesce', 'iridescent',
            'pseudonym', 'entrepreneur', 'reconnaissance', 'catastrophe', 'juxtaposition',
            'conscientious', 'belligerent', 'dichotomy', 'parliament', 'transcendent',
            'phenomenon', 'benevolent', 'exacerbate', 'idiosyncrasy', 'metamorphosis',
            'camaraderie', 'magnanimous', 'existential', 'unfathomable', 'anachronism', 'labyrinth'
            'circumstances', 'inconspicuous', 'malfeasance', 'disingenuous', 'egregious',
            'surreptitious', 'vindicated'
        ]
    }

    def __init__(self, word_count, difficulty_setting):
        """
        Params: int of how many words to use for the reference text

        init method for this class generates a list, separated by char,
        of random words from the words list and stores it in an instance
        var to be retrieved by the getter
        """
        self.word_count = word_count # remember to handle improper value
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
            word = random.choice(self.words[diff_level])
            selected_words.append(word)

        return ' '.join(selected_words)

    def get_selected_chars(self):
        """
        getter method for getting the reference text list that's been 
        generated
        """
        return self.selected_chars
    
    def get_difficulty_setting(self, difficulty_setting):
        match difficulty_setting:
            case 'easy':
                self.difficulty.append('easy')
            case 'medium':
                self.difficulty.extend(['easy', 'medium'])
            case 'hard':
                self.difficulty.extend(['easy', 'medium', 'hard'])
            case 'veryHard':
                self.difficulty.extend(['easy', 'medium', 'hard', 'veryHard'])
            case _:
                # using assert False here because this line should never execute unless something
                # has gone very wrong, any malformed difficulty setting should be caught in main()
                assert False, f'Unexpected difficulty setting, {difficulty_setting}'
