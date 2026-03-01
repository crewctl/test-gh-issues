import app


def test_greet(capsys):
    app.greet("Alice")
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice\!"


def test_divide():
    assert app.divide(10, 2) == 5.0


def test_divide_by_zero():
    # This should handle zero division gracefully
    try:
        app.divide(10, 0)
        assert False, "Should have raised an error"
    except ZeroDivisionError:
        pass


def test_find_max():
    assert app.find_max([3, 1, 4, 1, 5, 9]) == 9


def test_find_max_negative():
    # BUG: find_max fails with all-negative lists
    assert app.find_max([-3, -1, -4]) == -1


def test_is_palindrome():
    assert app.is_palindrome("racecar") is True
    assert app.is_palindrome("hello") is False


def test_is_palindrome_case_insensitive():
    # BUG: is_palindrome is case-sensitive
    assert app.is_palindrome("Racecar") is True


def test_count_words():
    assert app.count_words("hello world") == 2


def test_count_words_empty():
    # BUG: count_words returns 1 for empty string
    assert app.count_words("") == 0
