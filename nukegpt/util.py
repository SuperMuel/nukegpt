from typing import Iterable


class CountryNotFoundException(Exception):
    def __init__(self, country_name: str):
        self.country_name = country_name
        super().__init__(f"Country '{country_name}' not found.")


def _convert_country_name_str(cc, name: str) -> str:
    cc_name = cc.convert(names=name, to="name_short")
    if cc_name == "not found":
        raise CountryNotFoundException(name)
    return cc_name


def convert_country_names(cc, names: str | Iterable[str]) -> set[str]:
    """Convert countries returned by LLM to a set of countries short_names we know exist.

    Args:
        cc: The country converter object.
        names: The names to convert. Can be a single string or an iterable of strings.

    Returns: A set of country short_names.

    Raises:
        CountryNotFoundException: If a country is not found

        # examples
        >>> convert_country_names(cc, [])
        set()
        >>> convert_country_names(cc, "")
        Traceback (most recent call last):
        ...
        CountryNotFoundException: Country '' not found.
        >>> convert_country_names(cc, "ElonMusksLand")
        Traceback (most recent call last):
        ...
        CountryNotFoundException: Country 'ElonMusksLand' not found.
        >>> convert_country_names(cc, "Russia")
        {'Russia'}
        >>> convert_country_names(cc, "RU")
        {'Russia'}
        >>> convert_country_names(cc, ["Russia", "RU"])
        {'Russia'}
        >>> convert_country_names(cc, ["Russia", "FR"])
        {'Russia', 'France'}
    """

    if isinstance(names, str):
        names = [names]

    return set(_convert_country_name_str(cc, name) for name in names)
