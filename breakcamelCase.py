# Solved The Break camelCase
# 3/19/2023
def solution(s):
    if s == "":
        return ""
    stringsplit = list(s)
    container = [stringsplit[0]]
    for item in stringsplit[1:]:
        if item == item.upper():
            container.extend([" ", item])
        else:
            container.append(item)
    return "".join(container)

    # listcomp

    # if s == "":
    #     return ""
    # else:
    #     return "".join([" "+letter if letter == letter.upper() else letter for letter in list(s)])
