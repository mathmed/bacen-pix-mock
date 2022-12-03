from re import UNICODE, compile, match, sub
from typing import Dict
from unicodedata import normalize


def convert_snake_case_dict_items_to_camel_case(dict: Dict) -> Dict:
    new_dict = {}
    for key, value in dict.items():
        new_dict[convert_snake_case_to_camel_case(key)] = value
    return new_dict


def convert_camel_case_to_snake_case(text: str) -> str:
    return sub(r'(?<!^)(?=[A-Z])', '_', text).lower()


def convert_snake_case_to_camel_case(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


def clean_str_accent(value: str) -> str:
    try:
        text = unicode(value, 'utf-8')
    except NameError:
        pass
    text = normalize('NFD', value)\
        .encode('ascii', 'ignore')\
        .decode('utf-8')

    return str(text)


def normalize_phone(phone: str) -> str:
    return phone.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')


def normalize_document(document: str) -> str:
    return document.replace('.', '').replace('-', '').replace(' ', '').replace('/', '')


def is_valid_phone(phone: str) -> bool:
    is_valid = match(r'^\+[1-9][0-9]\d{1,14}$', phone)
    return bool(is_valid)


def is_valid_cpf(cpf: str) -> bool:
    is_valid = match(r'^[0-9]{11}$', cpf)
    return bool(is_valid)


def is_valid_cnpj(cnpj: str) -> bool:
    is_valid = match(r'^[0-9]{14}$', cnpj)
    return bool(is_valid)


def is_valid_uuid(uuid: str) -> bool:
    is_valid = match(
        r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', uuid)
    return bool(is_valid)


def is_valid_email(email: str) -> bool:
    is_valid = match(
        r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)
    return bool(is_valid)


def is_valid_hour(hour: str) -> bool:
    is_valid = match(r'^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$', hour)
    return bool(is_valid)


def clean_special_chars(text: str) -> str:

    if not text:
        return text

    try:
        emoji_pattern = compile("["
                                u"\U0001F600-\U0001F64F"  # emoticons
                                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                u"\U00002500-\U00002BEF"  # chinese char
                                u"\U00002702-\U000027B0"
                                u"\U00002702-\U000027B0"
                                u"\U000024C2-\U0001F251"
                                u"\U0001f926-\U0001f937"
                                u"\U00010000-\U0010ffff"
                                u"\u2640-\u2642"
                                u"\u2600-\u2B55"
                                u"\u200d"
                                u"\u23cf"
                                u"\u23e9"
                                u"\u231a"
                                u"\ufe0f"
                                u"\u3030"
                                "]+", UNICODE)

        special_chars_pattern = r"[<>&'\"]"
        formatted_text = sub(emoji_pattern, '', text)
        return sub(special_chars_pattern, '', formatted_text)

    except Exception:
        pass
    return text


def abbreviate_name(name: str, str_len=25) -> str:

    try:
        sub_name = name.encode('utf-8')

        clean_name = str(normalize('NFKD', sub_name.decode(
            'utf-8')).encode('ASCII', 'ignore').decode('utf-8'))

        if len(clean_name) <= str_len:
            return clean_name

        name_list = clean_name.split(' ')

        first_name = name_list[0]
        last_name = name_list[len(name_list) - 1]
        median_names = []

        median_original_names = [
            name for name in name_list[1:len(name_list) - 1] if len(name) > 2]

        aux_composite_name = [first_name, last_name]

        for name in median_original_names:
            if len(' '.join(aux_composite_name + [name])) > str_len:
                break
            aux_composite_name.append(name)
            median_names.append(name)

        median_names = ' ' + ' '.join(median_names) if median_names else ''
        composite_name = f'{first_name}{median_names} {last_name}'

        if len(composite_name) > str_len:
            composite_name = composite_name[:str_len]

        return str(composite_name)
    except Exception:
        return name


def abbreviate_city_name(name, str_len=15) -> str:
    sub_name = name.encode('utf-8')
    clean_name = str(normalize('NFKD', sub_name.decode(
        'utf-8')).encode('ASCII', 'ignore').decode('utf-8'))

    if len(clean_name) <= str_len:
        return clean_name

    splitted_name = clean_name.split(' ')
    splitted_name = list(filter(None, splitted_name))
    last_name = splitted_name[-1]
    new_splitted_name = [f'{item[0]}' for item in splitted_name]
    if 'd' in new_splitted_name:
        new_splitted_name.remove('d')
    new_splitted_name[-1] = last_name
    new_name = ' '.join(new_splitted_name)

    # Caso trata do nome da cidade Esperantinopolis
    return new_name[:-1] if len(new_name) > str_len else new_name


def validate_cpf(cpf: str) -> bool:

    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in cpf if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum(cpf[num] * ((i + 1) - num) for num in range(i))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True


def validate_cnpj(cnpj: str) -> bool:

    cnpj = "".join(char for char in cnpj if char.isdigit())
    first_validator_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_validator_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    #  Verifica se o CNPJ tem todos os números iguais, ex: 11.111.111/1111-11
    if cnpj == cnpj[::-1]:
        return False

    # digitos verificadores
    verifying_digit = cnpj[-2:]

    # calculating the first digit
    _sum = 0
    _id = 0
    for _number in cnpj:

        # to do not raise indexerrors
        try:
            first_validator_list[_id]
        except Exception:
            break

        _sum += int(_number) * int(first_validator_list[_id])
        _id += 1

    _sum = _sum % 11
    first_digit = 0 if _sum < 2 else 11 - _sum
    first_digit = str(first_digit)

    # calculating the second digit
    # suming the two lists
    _sum = 0
    _id = 0

    # suming the two lists
    for _number in cnpj:

        # to do not raise indexerrors
        try:
            second_validator_list[_id]
        except Exception:
            break

        _sum += int(_number) * int(second_validator_list[_id])
        _id += 1

    # defining the digit
    _sum = _sum % 11
    second_digit = 0 if _sum < 2 else 11 - _sum
    second_digit = str(second_digit)

    # returnig
    return verifying_digit == first_digit + second_digit


def to_camel_case(snake_str: str) -> str:
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def format_payload_response(object: object) -> Dict:
    item = {}
    for key, value in object.__dict__.items():
        item[to_camel_case(key)] = value
    return item
