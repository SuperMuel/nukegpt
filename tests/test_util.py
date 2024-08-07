from nukegpt.util import convert_country_names, CountryNotFoundException
import country_converter as coco
import pytest


@pytest.fixture
def cc():
    return coco.CountryConverter()


def test_convert_country_names_empty_list(cc):
    assert convert_country_names(cc, []) == set()


def test_convert_country_names_empty_string(cc):
    with pytest.raises(CountryNotFoundException):
        convert_country_names(cc, "")


def test_convert_country_names_invalid_country(cc):
    with pytest.raises(CountryNotFoundException):
        convert_country_names(cc, "ElonMusksLand")


def test_convert_country_names_invalid_ISO3(cc):
    with pytest.raises(CountryNotFoundException):
        convert_country_names(cc, "XXY")


def test_convert_country_names_single_string(cc):
    assert convert_country_names(cc, "Russia") == {"Russia"}


def test_convert_country_names_single_code(cc):
    assert convert_country_names(cc, "RU") == {"Russia"}


def test_convert_country_names_single_code_france(cc):
    assert convert_country_names(cc, "FR") == {"France"}


def test_convert_country_names_list_mixed(cc):
    assert convert_country_names(cc, ["Russia", "RU"]) == {"Russia"}


def test_convert_country_names_list_full_names(cc):
    assert convert_country_names(cc, ["Russia", "France"]) == {"Russia", "France"}


def test_convert_country_names_list_mixed_names(cc):
    assert convert_country_names(cc, ["Russia", "FR"]) == {"Russia", "France"}


def test_convert_country_names_list_mixed_set(cc):
    assert convert_country_names(cc, {"Russia", "FR"}) == {"Russia", "France"}


def test_convert_country_names_list_mixed_one_invalid(cc):
    with pytest.raises(CountryNotFoundException):
        convert_country_names(cc, ["Russia", "ElonMusksLand"])


def test_convert_country_names_lower_case(cc):
    assert convert_country_names(cc, "russia") == {"Russia"}


def test_convert_country_names_lower_case_ru(cc):
    assert convert_country_names(cc, "ru") == {"Russia"}
