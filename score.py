def get_maxscore() -> int:
    filename = "maxscore.txt"
    if filename in os.listdir():
        with open(filename, "r") as file:
            val = file.read()
            if val == "":
                maxscore = 0
            else:
                maxscore = int(val)
    else:
        maxscore = 0
    return maxscore


def set_score(maxscore) -> None:

    with open("maxscore.txt", "w") as file:
        file.write(str(maxscore))