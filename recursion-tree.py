def list_files(parent_directory, current_filepath=""):
    filepaths = []

    for name, value in parent_directory.items():
        new_path = current_filepath + "/" + name

        if value is None:
            filepaths.append(new_path)
        else:
            filepaths.extend(list_files(value, new_path))

    return filepaths
