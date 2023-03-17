# Solved The Hashtag Generator
# 3/16/32023
def generate_hashtag(s):
    if s == '':
        return False
    stringsplit = s.split()
    if len(stringsplit) == 1:
        stringsplit.insert(0, "#")
        newstring = "".join(stringsplit)
        if len(newstring) > 140:
            return False
        return newstring.title()
    else:
        stringsplit.insert(0, "#")
        container = []
        for items in stringsplit:
            container.append(items.title())
            newstring = "".join(container)
        if len(newstring) > 140:
            return False
    return newstring

