def split_batch(text_iterator, sep):
    """
    Returns a genarator of strings read from a "text_iterator" (iterating over
    lines), where a batch consists of adjacent lines separated by an empty
    line. The generator yiels one string per batch, with several adjacent
    lines joined by the "sep" character.
    """
    current_group = []
    for l in text_iterator:
        if l.strip() == "":
            if current_group:
                yield sep.join(current_group)
            current_group = []
        else:
            current_group.append(l.strip())
    yield sep.join(current_group) # last batch
