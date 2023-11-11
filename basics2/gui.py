def tree():
    pic = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ]

    for i in pic:
        for p in i:
            if p == 0:
                print(" ", end="")
            elif p == 1:
                print("*", end="")
        print("")


tree()
tree()
