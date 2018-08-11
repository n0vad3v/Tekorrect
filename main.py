import pangu
import os
import sys

file_with_paths = []
files = os.listdir(sys.argv[1])

# Load absolute file paths into list
for file in files:
    file_with_paths.append(os.path.join(sys.argv[1], file))

for old_file_path in file_with_paths:
    new_file_content = pangu.spacing_file(old_file_path)
    # OverWrite the original files
    with open(old_file_path,'w') as f:
        f.write(new_file_content)

