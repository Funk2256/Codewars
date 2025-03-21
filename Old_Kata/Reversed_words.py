text = "The greatest victory is that which requires no battle"


def reverseWords(text):
    pre_finally_text = (text.split(' ')[::-1])
    return (' '.join(pre_finally_text))


print(reverseWords(text))
