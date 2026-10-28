"""CP1404 Practical: Programming Languages Class"""


class ProgrammingLanguage:
    """Represent a Programming Language Object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language Instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if a language is dynamic or not."""
        if self.typing == "Dynamic":
            return True
        return False
