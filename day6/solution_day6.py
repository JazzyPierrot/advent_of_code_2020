
def split_batch(text):
    """
    Returns a genarator of passports read from a "text" (accepting
    `splitlines()` method), where each item is one string (with newlines
    stripped, and space separated values)
    """
    current_pass = []
    for l in text.splitlines():
        if l == "":
            yield " ".join(current_pass)
            current_pass = []
        else:
            current_pass.append(l.strip())
    yield " ".join(current_pass) #last pass
