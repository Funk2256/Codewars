def is_uppercase(test_strings):
    for char in test_strings:
        if char.islower():
            return False
    return True


"""is_uppercase = str.isupper"""

print(is_uppercase('Ci/` $R+ozJPI&,3[GWD"<L5}MOVUp;Ew)0q)#7eabQ1]f?x'))
