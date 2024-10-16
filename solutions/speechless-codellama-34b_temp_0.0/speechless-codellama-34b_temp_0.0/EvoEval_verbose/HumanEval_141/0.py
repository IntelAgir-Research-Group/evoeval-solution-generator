
def file_name_check(file_name):
    if sum((c.isdigit() for c in file_name)) > 3:
        return 'No'
    if file_name.count('.') != 1:
        return 'No'
    (name, ext) = file_name.split('.')
    if not name or not name[0].isalpha():
        return 'No'
    if ext not in ['txt', 'exe', 'dll']:
        return 'No'
    return 'Yes'