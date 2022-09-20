class Must_read:
    with open("data.csv", "r") as file:
        print(file.read())
        file.close()


if __name__ == '__main__':
    Must_read()
