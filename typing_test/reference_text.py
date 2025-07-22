import random


class ReferenceText:

    words = [
    'the', 'and', 'is', 'you', 'that', 'it', 'in', 'of', 'to', 'a', 'was', 'for', 'on',
    'with', 'as', 'at', 'be', 'by', 'he', 'she', 'we', 'they', 'are', 'not', 'this', 'have',
    'had', 'from', 'but', 'or', 'his', 'her', 'an', 'if', 'then', 'will', 'so', 'no', 'do', 'can',
    'window', 'kitchen', 'summer', 'travel', 'happy', 'morning', 'garden', 'animal', 'people',
    'number', 'father', 'mother', 'school', 'letter', 'friend', 'music', 'water', 'winter',
    'future', 'always', 'never', 'simple', 'market', 'energy', 'problem', 'answer', 'picture',
    'system', 'group', 'process', 'country', 'architecture', 'phenomenon', 'consideration', 
    'hypothesis', 'conclusion', 'significant', 'literature', 'environment', 'consequence',
    'opportunity', 'fundamental', 'development', 'psychology', 'communication', 'technology',
    'strategy', 'analytical', 'proportion', 'generation', 'analysis', 'philosophy', 'perspective',
    'expression', 'motivation', 'civilization'
    ]

    def __init__(self, word_count):
        """
        Params: int of how many words to use for the reference text

        init method for this class generates a list, separated by char,
        of random words from the words list and stores it in an instance
        var to be retrieved by the getter
        """
        self.word_count = word_count
        self.selected_words = self.gen_reference_text()
        self.selected_chars = list(self.selected_words)

    def gen_reference_text(self):
        """
        makes random choices from the words list 'word_count' times,
        joins them into a string, and returns them
        """
        selected_words = random.choices(self.words, k=self.word_count)
        return ' '.join(selected_words)

    def get_selected_chars(self):
        """
        getter method for getting the reference text list that's been 
        generated
        """
        return self.selected_chars
