class FileNotExistError(Exception):
    """
FileNotExistError indicates that the file corresponding to the provided sha256 hash could not be found.
    This error is uncommon and typically indicates a server-side issue.
    Normally this error does not occur. If it does, it means that there is
    a problem with the server
    """

    pass


class FileRequiredError(Exception):
    """
FileRequiredError indicates that BinaryAI requires the original file, but it is not being provided.
    This error might occur if only the hash is provided to BinaryAI without the original file. Please ensure to provide the original file.
    This error might occur if you are only providing hash to the BinaryAI. Consider provide the original file as well.
    """

    pass
