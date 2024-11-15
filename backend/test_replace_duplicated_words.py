import pytest
from main import replace_duplicated_words


@pytest.mark.parametrize(
    "input_message, expected_output",
    [
        ("Hello world world", "Hello world fake"),
        ("Hello hello HELLO", "Hello fake fake"),
        ("Hello, hello. Hello!", "Hello, fake. fake!"),
        ("Hello, world! hello, WORLD.", "Hello, world! fake, fake."),
        ("This is a unique sentence.", "This is a unique sentence."),
        ("", ""),
        ("Duplicate duplicate duplicate.", "Duplicate fake fake."),
    ]
)
def test_replace_duplicated_words(input_message, expected_output):
    assert replace_duplicated_words(input_message) == expected_output
