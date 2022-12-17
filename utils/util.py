def safe_int(input: str, default: int) -> int:
    """
        returns int
    """
    try:
        if (input.isdigit()):
            return int(str)
        else:
            return default
    except:
        return default
    
def within_valid_values(input_value:str, valid_values:set[str], default_value:str) -> str:
    if input_value in valid_values:
        return input_value
    return default_value
