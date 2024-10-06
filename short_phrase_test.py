class TestExample:
    phrase_check = input('Set a phrase: ')
    a = len(phrase_check)
    number_of_characters = 15
    assert a < number_of_characters, f"The phrase must be shorter than {number_of_characters} characters"
