# this file is testing file to understand shelx and regular expression support (re)

import re
import shlex

test_text = "This 'is' t he testing python file."
test_location = "home/user main/mode file.txt"
# test_location_output = "home/"

print(re.split('\s', "this is 'my string' that --has=arguments )-or=something"))
print(re.split('\s', r"home/user main/mode file.txt"))
print(shlex.split(test_location))
print(shlex.split(rf'{test_location}'))
print(r"home/user main/mode file.txt")

# print(shlex.split(f'"{test_text}"'))
# print(test_text)



print("\n ----- \n")



def parse_mode_file(mode_path: str) -> list[list[str]]:
        """
    Args:
        mode_path (str)

    Returns:
        list[list[str]]
    """
        with open(mode_path) as mode_file:
                mode_str = mode_file.read.strip()

        print(mode_str)


parse_mode_file('C:\Users\laksh\OneDrive\Desktop\tech-sandbox\Python\test mode.txt')
