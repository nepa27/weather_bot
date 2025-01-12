def get_emoji(emoji):
    codes = [f"\\U{ord(char):08X}" for char in emoji]
    formatted_code = ''.join(codes)
    return formatted_code
