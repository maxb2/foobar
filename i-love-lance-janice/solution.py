global cipher
cipher = {"a": "z",
            "b": "y",
            "c": "x",
            "d": "w",
            "e": "v",
            "f": "u",
            "g": "t",
            "h": "s",
            "i": "r",
            "j": "q",
            "k": "p",
            "l": "o",
            "m": "n",
            "n": "m",
            "o": "l",
            "p": "k",
            "q": "j",
            "r": "i",
            "s": "h",
            "t": "g",
            "u": "f",
            "v": "e",
            "w": "d",
            "x": "c",
            "y": "b",
            "z": "a"}

def solution(x):
    xlist = list(x)
    message = ""
    for x in xlist:
        try:
            s = cipher[x]
        except:
            s = x
        message += s
    return message