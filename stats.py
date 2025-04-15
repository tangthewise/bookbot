def count_words(from_text):
    result = 0

    contents_array = from_text.split()

    result = len(contents_array)

    return result

def count_characters(from_text):
    found_characters = {}

    for character in from_text.lower():        
        if character.isalpha():
            if not(character in found_characters.keys()):
                found_characters[character] = 0
        
            found_characters[character] += 1

    
    return found_characters

def sort_count_ascending(character_count):

    return {key: val for key, val in sorted(character_count.items(), key = lambda ele: ele[1], reverse=True)}

