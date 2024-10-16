
def Strongest_Extension(class_name, extensions):
    strongest_extension = None
    strongest_strength = float('-inf')

    for extension in extensions:
        cap_count = sum(1 for char in extension if char.isupper())
        sm_count = sum(1 for char in extension if char.islower())
        strength = cap_count - sm_count

        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    return f"{class_name}.{strongest_extension}"
