student_list = [
    "  john doe ",
    "JANE SMITH",
    "   ",
    "alice wonderland",
    "bOb rOsS  "
]

def format_roster(names):
    cleaned_list=[name.strip().upper() for name in names if name.strip()]
    return cleaned_list
cleaned_roster = format_roster(student_list)
print(cleaned_roster)







