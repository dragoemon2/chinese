import pypinyin
import os



def _check(pin: str, cpins):
    if not cpins:
        if pin == "":
            return True
        else:
            return False

    cp1s = cpins[0]
    for cp1 in cp1s:
        if pin.startswith(cp1):
            if _check(pin[len(cp1):], cpins[1:]):
                return True
    
    return False



def check(text: str):
    text = text.split("\n" ,1)[-1].replace('"', '').replace(" ","").replace("'","")
    content = [line.split(",")[:2] for line in text.split("\n")]
    for word, pin in content:
        cpins = pypinyin.pinyin(word, heteronym=True)
        if not _check(pin.lower(), cpins):
            yield word, pin, cpins


        


for fp in os.listdir("."):
    if fp.rsplit(".",1)[-1] == "csv":
        with open(fp, "r") as f:
            text = f.read()
        
        for a,b,c in check(text):
            if "(" in a:
                continue
            print(f"{fp},{a}: {b} → {c}") 
        
        