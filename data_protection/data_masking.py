def name_masking(name):
    words_list = name.split()

    # Skip the title if the name starts with one
    if words_list[0] == 'Mrs.':
        words_list = words_list[1:]

    first_letter = words_list[0][0]   # "Leanne" → "L"
    last_letter = words_list[1][0]    # "Graham" → "G"

    return first_letter + ". " + last_letter + "."  # "L. G."

def last_two_digits(phone):
    phone = phone.split("x")[0]
    # Keep only the digits: "1-770-736-8031" -> "17707368031"
    digits = ""
    for char in phone:
        if char.isdigit():
            digits += char

    # Replace all but the last two digits with "*"
    stars = "*" * (len(digits) - 2)
    return stars + digits[-2:]      # "17707368031" -> "*********31"
