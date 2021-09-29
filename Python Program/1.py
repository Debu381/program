def fun(string):
    # Pattern:capture all letters where lowercase letters follow on single uppercase
    # or beginning of a string
    pattern=r"((?:[A-Z]|^[a-z]){1}[a-z]*)"
    # find all matches
    match = re.findall(pattern,string)
    
    # append to single result
    result = ""
    for i in match:
        result += i
        # Space as word divider
        result += " "
    
    return(result)

print(fun("camelCase"))