def count_words(filename):
    """Count the approximate number of words in a file."""
    for filenames in filename:
        word_frequency = 0
        with open(filenames) as f_obj:
            for line in f_obj:
                word_frequency += line.lower().count('the')
        print("The file " + filenames + " has about " + str(word_frequency) + " occurences of the word \"the\".")

file_names = ['The_Great_Push.txt', 'The_life_story_of_an_otter.txt']
count_words(file_names)
