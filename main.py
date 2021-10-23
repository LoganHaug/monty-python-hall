import gameshow

def main():
    test = gameshow.Gameshow(runs=1000000)
    test.simulate()

if __name__ == "__main__":
    main()
