class WordShort:
    def __init__(self, text_str):
        self.text_str = text_str

    def find_short(self):
        return_split_list = self.text_str.split(' ')
        min_char = min((word for word in return_split_list), key=len)
        return len(min_char)

    def print_find_len(self):
        return self.text_str


test_str = WordShort("bitcoin take over the world maybe who knows perhaps")

print(test_str.find_short())
