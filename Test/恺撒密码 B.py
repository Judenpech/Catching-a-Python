def main():
    s = input("")
    output = ""
    for c in s:
        if 65 <= ord(c) <= 90:
            t = (ord(c) + 3) % 90
            if t < 65:
                t += 64
            output += chr(t)
        elif 97 <= ord(c) <= 122:
            t = (ord(c) + 3) % 122
            if t < 97:
                t += 96
            output += chr(t)
        else:
            output += c
    print(output)


main()
