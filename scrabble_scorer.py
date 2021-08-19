# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:
        for point_value in old_point_structure:
            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

def transform(old_point_structure):
    new_dict = {}
    for (key, value) in old_point_structure.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(old_point_structure)

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
   word = input("Lets play some Scrabble! \nPlease enter a word to begin the game:")
   return word

def simple_scorer(word):
   score = 0
   for char in word.lower():
       score +=1
   return score

def vowel_bonus_scorer(word):
    vowels = ['a','e','i','o','u']
    score = 0
    for letter in word.lower():
        if letter in vowels:
            score += 3
        else:
            score += 1
    return score

def scrabble_scorer(word):
    score = 0

    for letter in word:
        if letter in new_point_structure:
            score += new_point_structure[letter]
    return score

#scoring_algorithms = ()
new_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'The traditional scoring algorithm.',
    'score_function': scrabble_scorer
}
simple_dict = {
    'name': 'Simple Score',
    'description': 'Each letter is worth 1 point. A function with a parameter for user input that returns a score.',
    'score_function': simple_scorer
}
vowel_dict = {
    'name': 'Bonus Vowels',
    'description': 'Vowels are 3 pts, consonants are 1 pt.',
    'score_function': vowel_bonus_scorer
}

scoring_algorithms = (
    simple_dict,
    vowel_dict,
    new_scrabble_scorer_dict,  
)

def scorer_prompt():
    #print("test run ")
    scoring_prompt = input('Which scoring method would you like to use?')
    algorithm_select = int (scoring_prompt)
    """user_selection = 3
    
    while user_selection > 2:
        for index, algorithim in enumerate(scoring_algorithms):
            print(f'{index} - {algorithim["name"]}: {algorithim["description"]}')
        user_selection = int(input('Enter 0, 1, or 2'))

    selected_method_dict = scoring_algorithms[user_selection]"""

    return scoring_algorithms[algorithm_select]



def run_program():
    word = initial_prompt()
    selected_method_dict = scorer_prompt()
    #scorer_prompt()
    score = selected_method_dict['score_function'](word)

    print(f'''The word you entered was "{word}".\nYou selected the "{selected_method_dict["name"]}" scoring algorithm which {selected_method_dict["description"]}.\nYour word is worth {score} points!''')