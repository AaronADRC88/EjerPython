__author__ = 'aferreiradominguez'
s = int(input("Introduce numero:"))
print(1)


def primo(j):
    i = 2
    while i < j:
        resto = j % i
        if (resto == 0):
            return 0
        i = i + 1
    print(str(j))


j = 2
while j < s:
    a = primo(j)
    j = j + 1
