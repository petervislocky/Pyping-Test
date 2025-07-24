import random


class ReferenceText:


    words = {
        'easy': [
            'the', 'and', 'is', 'you', 'that', 'it', 'in', 'of', 'to', 'a', 'was', 'for', 'apple',
            'house', 'green', 'water', 'train', 'smile', 'light', 'music', 'on', 'table', 'happy',
            'quick', 'dream', 'stone', 'laugh', 'chair', 'world', 'sleep', 'phone', 'clock', 'voice'
        ],
        'medium': [
            'picture', 'thunder', 'journey', 'blanket', 'capture', 'forward', 'message', 'bicycle',
            'puzzle', 'improve', 'careful', 'recycle', 'feather', 'airport', 'perfect', 'library',
            'plastic', 'courage', 'holiday'
        ],
        'hard': [
            'quarantine', 'silhouette', 'kaleidoscope', 'subconscious', 'reminiscent', 'hypocrisy',
            'miscellaneous', 'picturesque', 'jeopardize', 'bureaucracy', 'acquiesce', 'iridescent',
            'pseudonym', 'entrepreneur', 'reconnaissance', 'catastrophe', 'juxtaposition',
            'conscientious', 'belligerent', 'dichotomy'
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
        if difficulty_setting == 'easy':
            self.difficulty.append('easy')
        elif difficulty_setting == 'medium':
            self.difficulty.extend(['easy', 'medium'])
        elif difficulty_setting == 'hard':
            self.difficulty.extend(['easy', 'medium', 'hard'])
        else:
            print('Error retrieving difficulty settings')
