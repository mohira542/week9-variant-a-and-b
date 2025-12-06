def  sanitized_filenames(files):
    valid =  []
    for file in files:
        filename=file.strip().lower()
        cleaned= filename.replace(' ', '_')
        if  ".txt" in cleaned:
          valid.append(cleaned)
    return  valid

uploads = [
    "  My Resume.pdf ",  # Not a .txt file, skip
    "Vacation Photo.JPG", # Not a .txt file, skip
    "PROJECT specs.txt",
    "   ",
    "notes.txt"
]

# Run the function
safe_files = sanitized_filenames(uploads)
print(safe_files)



















