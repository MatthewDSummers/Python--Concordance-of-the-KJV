import os
import json
# The function will search the JSON file for the specific word(s) in each verse contained within the JSON,
# and it will show the results in the terminal in an easily readable format as well as return a list containing the results 
def concordance(term):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'john3.json')

    with open(file_path, 'r') as f:
        data = json.load(f)
        results = []
        for word in data:
            if term in word[u'verse']:
                word[u'verse'] = word[u'verse'].replace(term, term.upper())
                results.append((word[u'name'], word[u'verse']))
        for x in results:
            print(x[0])
            print(x[1])
            print("\n")
        return results

print(concordance("For God so loved the world"))
# the above will print:
# "John 3:16
# FOR GOD SO LOVED THE WORLD, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life."

print(concordance("whosoever believeth"))
# the above will print:
# John 3:15
# That WHOSOEVER BELIEVETH in him should not perish, but have eternal life.

# John 3:16
# For God so loved the world, that he gave his only begotten Son, that WHOSOEVER BELIEVETH in him should not perish, but have everlasting life.