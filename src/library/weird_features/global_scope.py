def main()-> None:
    for x in range(8):
        if x == 6:
            print(x, ": for x inside the loop")
    print(x, ": for x in global/scope")

if __name__ == "__main__":
    main()