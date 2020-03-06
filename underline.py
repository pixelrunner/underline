def underline (string_input, underline_symbol):
    string_output = ''
    if len(string_input) == 0:
        return ''
    else:
        while len(string_output) < len(string_input):
            string_output = string_output + underline_symbol
    return string_output
