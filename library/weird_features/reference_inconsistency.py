def f():
    return 1


def main() -> None:
    print(f())
    a = [1,2,3]
    b = a # b is now a reference to a
    print(id(a))
    print(id(b))
    a += [4]
    print(b)

    s ="hello"
    t = s # t is now a reference to s
    print(id(s))
    print(id(t))
    s += " world"
    print(t)
    print(s)
    print(id(s))
    print(id(t))

if __name__ == "__main__":
    main()