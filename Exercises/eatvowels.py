#eatvowels.py
def eatVowels(s):
    return ''.join([c for c in s if c.lower() not in 'aeiou'])

def main():
    print(eatVowels('Apple sauce'))

main()
