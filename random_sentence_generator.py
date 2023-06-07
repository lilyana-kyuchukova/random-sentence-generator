import random

names = ["Lilly", "Stephen", "Faisal", "James", "Gery", "Brian", "Peter", "Michell", "Jane", "Steve"]
places = ["London", "Sofia", "Plovdiv", "Varna", "Burgas", "Paris", "Kaspichan", "D. Nanagornishte", "Ghent", "Vratza"]
verbs = ["performs", "cleans", "drinks", "plays with", "brings", "eats", "holds", "sees"]
nouns = ["stones", "cake", "apple", "laptop", "bikes", "blood", "coffee", "table", "cat", "dog", "horse"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly", "gently", "angrily", "happily", "horribly"]
details = ["near the river", "at home", "in the park", "in the toilet", "in the office", "by the train station"]


def get_random_word(words):
    return random.choice(words)


flag = True

while flag:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")

    play_again = input("Play again? [Y] / [N] ")

    if play_again == "N":
        print("Byeee")
        flag = False
