import random
letters = "a","t","g","c"
letter_a="t","g","c"
letter_t= "a", "g", "c"
letter_g="a","t","c"
letter_c="a","t","g"
originaltext =["a","t","g","c","a","t","g","c","a","t"]

with open("inputt.txt", 'w') as file:
    pass

i=0
while i<10:
    n = 0
    while n < 4:
        listnumber = []
        while True:
            formutating = (random.randint(0, 9))
            if formutating in listnumber:
                print(listnumber)
                pass
            else:
                listnumber.append(formutating)
                break
        print(listnumber)
        if originaltext[formutating] == "a":
            originaltext[formutating] = random.choice(letter_a)
        elif originaltext[formutating] == "t":
            originaltext[formutating] = random.choice(letter_t)
        elif originaltext[formutating] == "g":
            originaltext[formutating] = random.choice(letter_g)
        elif originaltext[formutating] == "c":
            originaltext[formutating] = random.choice(letter_c)
        n = n + 1
    mutateword = ""
    for ana in originaltext:
        mutateword += ana
    def insert_sequence():
        int = (random.randint(0, 9))
        result_str = ''.join(random.choice(letters) for a in range(500))
        str1_split1 = result_str[:int]
        str1_split2 = result_str[int:]
        new_string = str1_split1 + mutateword + str1_split2
        with open('inputt.txt', 'a') as f:
            f.write(new_string)
            f.write("\n")
        return new_string
    i=i+1
    insert_sequence()


