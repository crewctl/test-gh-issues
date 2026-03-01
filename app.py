def greet(name):
    """Greet a user by name."""
    print("Hello, " + name + "\!")


def divide(a, b):
    """Divide a by b."""
    return a / b


def find_max(numbers):
    """Find the maximum number in a list."""
    max_num = 0
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num


def is_palindrome(s):
    """Check if a string is a palindrome."""
    return s == s[::-1]


def count_words(text):
    """Count words in a text string."""
    words = text.split(" ")
    return len(words)


if __name__ == "__main__":
    greet("World")
    print(divide(10, 2))
    print(find_max([3, 1, 4, 1, 5, 9]))
    print(is_palindrome("racecar"))
    print(count_words("hello world foo bar"))
