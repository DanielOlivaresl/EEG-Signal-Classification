import os

def create_markdown_file(file_name):
    if not os.path.exists(file_name):  # Check if the file already exists
        with open(file_name, 'w') as file:
            # Basic Markdown structure
            file.write("# Title\n\n")
            file.write("## Subheading\n\n")
            file.write("This is a sample Markdown file.\n")
            file.write("You can add more sections here.\n")
        print(f"{file_name} created successfully.")
    else:
        print(f"{file_name} already exists.")


for i in range(1,29):
    create_markdown_file(f"sprints/sprint{i}/reporteDaniel.md")
    create_markdown_file(f"sprints/sprint{i}/reporteCarlos.md")
    create_markdown_file(f"sprints/sprint{i}/reporteHugo.md")