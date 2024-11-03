def single_root_words(root_word, *other_words):
    same_words = []
    low_1 = root_word.lower()
    for i in other_words:
        low_2 = i.lower()
        if low_1 in low_2:
            same_words.append(i)
        elif low_2 in low_1:
            same_words.append(i)
    print(same_words)
single_root_words('Дед', 'ДеДовский', 'бабушкин', 'дедок')