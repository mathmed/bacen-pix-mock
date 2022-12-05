from unittest import TestCase

import pytest
from faker import Faker
from faker.providers import phone_number, ssn

from .strings import *

faker = Faker('pt_BR')
faker.add_provider(phone_number)
faker.add_provider(ssn)


def test_should_return_correct_normalized_phone():
    result = normalize_phone('55 (84) 9 12345678')
    assert result == '5584912345678'


def test_should_return_correct_normalized_cpf():
    result = normalize_document('123.456.789-10')
    assert result == '12345678910'


def test_should_return_correct_normalized_cnpj():
    result = normalize_document('12.345.678/9101-12')
    assert result == '12345678910112'


def test_should_return_true_on_valid_digit_cpf():
    result = validate_cpf(normalize_document(faker.cpf()))
    assert result is True


def test_should_return_true_on_valid_digit_cnpj():
    result = validate_cnpj(normalize_document(faker.cnpj()))
    assert result is True


def test_should_return_false_on_valid_digit_cpf():
    result = validate_cpf(normalize_document(faker.word()))
    assert result is False


def test_should_return_false_on_same_digit_cpf():
    result = validate_cpf(normalize_document('111.111.111-11'))
    assert result is False


def test_should_return_false_on_invalid_verification_cpf_code():
    result = validate_cpf(normalize_document('123.456.789-19'))
    assert result is False


def test_should_return_false_on_valid_digit_cnpj():
    result = validate_cnpj(normalize_document(faker.word()))
    assert result is False


@pytest.mark.parametrize('value, result', [
    ('Ácêntô assím póde não', 'Acento assim pode nao'),
    ('São José dos Campos', 'Sao Jose dos Campos'),
    ('Caicó', 'Caico'),
])
def test_should_clean_accents(value, result):
    assert clean_str_accent(value) == result


@pytest.mark.parametrize('value, result', [
    ('00:00', True),
    ('34:00', False),
    ('00:60', False),
    ('24:00', False),
    ('24:01', False),
    ('25:00', False),
    ('23:01', True),
])
def test_should_is_valid_hour(value, result):
    assert is_valid_hour(value) == result


def test_clean_special_chars_should_return_correct_value():

    # Manter acentos
    text = 'Ácêntô assím póde não'
    assert clean_special_chars(text) == text

    # Remover emojis
    text = 'Olá!🙂😎🤡😘😌🥰🤭!'
    assert clean_special_chars(text) == 'Olá!!'

    # Texto normal
    text = 'Olá! esse; teste, deve ser enviado?'
    assert clean_special_chars(text) == text

    # Special
    text = "Aqui<> deu ruim&, 'varios' carcte&\""
    assert clean_special_chars(text) == 'Aqui deu ruim, varios carcte'

    # Exception
    assert clean_special_chars(None) is None

    # Empty string
    assert clean_special_chars('') == ''

    # Exception
    assert clean_special_chars(True) == True


@pytest.mark.parametrize('value, result', [
    ('São Paulo', 'Sao Paulo'),
    ('São José dos Campos', 'S J Campos'),
    ('Caicó', 'Caico'),
    (' Aurora   do  Tocantins ', 'A Tocantins')
])
def test_abbreviate_city_name_greater_than_fifteen(value, result):
    assert abbreviate_city_name(value) == result


@pytest.mark.parametrize('value, result', [
    ('Jon Doe', 'Jon Doe'),
    (True, True),
    ('Igor Raul Benício Caldeira', 'Igor Raul Caldeira'),
    ('Danilo Filipe Erick Figueiredo', 'Danilo Filipe Figueiredo'),
    ('Danilo Filipe Contrarrevolucionário', 'Danilo Contrarrevoluciona'),
])
def test_abbreviate_name_greater_than_fifteen(value, result):
    assert abbreviate_name(value) == result


@pytest.mark.parametrize('value, result', [
    ({'any_any': 'value'}, {'anyAny': 'value'}),
    ({'any': 'value'}, {'any': 'value'}),
    ({'anyAny': 'value', 'any_any2': 'value'},
     {'anyAny': 'value', 'anyAny2': 'value'})
])
def test_convert_snake_case_dict_items_to_camel_case_should_return_correct_dict(value, result):
    TestCase().assertDictEqual(to_dict_camel_case(value), result)
