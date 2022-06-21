

def _split_filename(path):
    entries = path.split("/")
    dir = ("/").join(entries[:-1])
    file = entries[-1]
    return dir, file