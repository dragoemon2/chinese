import numpy as np
import pprint

ARR = np.array([
    "ā á ǎ à".split(),
    "ō ó ǒ ò".split(),
    "ē é ě è".split(),
    "ī í ǐ ì".split(),
    "ū ú ǔ ù".split(),
    "ǖ ǘ ǚ ǜ".split(),
], dtype=str).T


class Word:
    def __init__(self, front:str, back:str, comment:str, *args):
        self.front = front
        self.back = back
        self.comment = comment

        args

    def pattern(self):
        if len(self.front) != 2:
            return None
        
        if self.front[1] == "儿":
            return None
        
        pattern = []
        
        for c in self.back:
            for i, l in enumerate(ARR):
                if c in l:
                    pattern.append(i+1)
        
        if len(pattern) == 1:
            pattern.append(0)


        return tuple(pattern)
    
    def __str__(self):
        return f'"{self.front}", "{self.back}", "{self.comment}"'


data = []
for i in range(4, 12):
    with open(f"words/{i}.csv", 'r') as f:
        text = f.read()
    lines = text.replace('"', '').split("\n")[1:]
    data += [line.split(",") for line in lines]

    for datus in data:
        if '/' in datus[1]:
            data.remove(datus)

            datus1 = datus.copy()
            datus2 = datus.copy()

            datus1[1], datus2[1] = datus[1].split("/")

            data.append(datus1)
            data.append(datus2)
        
words = [Word(*datus) for datus in data]

dictionary = {}

for word in words:
    key = word.pattern()
    if key is None:
        continue

    if key not in dictionary:
        dictionary[key] = []

    dictionary[key].append(str(word))


for key, array in dictionary.items():
    with open(f"sorted_by_sound/{key}.csv", "w") as f:
        f.write('"漢字","拼音","意味"\n' + "\n".join(array))

pprint.pprint(dictionary)
    

    