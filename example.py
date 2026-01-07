"""
Sample Python file for testing GitHub Actions workflow.

This module demonstrates basic Python functionality.
"""


def hello_world():
    """Print a greeting message."""
    print("Hello, World!")
    print("Welcome to LearnPython repository")


def add_numbers(a, b):
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def main():
    """Main function to demonstrate the module."""
    hello_world()
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")


if __name__ == "__main__":
    main()
