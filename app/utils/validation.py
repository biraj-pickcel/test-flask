import validators

def is_valid_url(url:str):
    result = validators.url(url)
    print(isinstance(result, validators.ValidationError))
    if isinstance(result, validators.ValidationError):
        return False

    return True