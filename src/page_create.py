from convert import md_to_html_nodes

import os
import shutil


def extract_title(markdown):
    """Extract the title from the markdown file."""
    title = None
    for line in markdown.split('\n'):
        if line.startswith('# '):
            title = line[2:]
            if not title:
                break
            return title.strip()

    raise ValueError("No title found in the markdown file.")


def generate_page(from_path, template_path, dest_path):
    open_message = f"""
    Opening {from_path}
    To {dest_path}
    Using {template_path}
    """
    print(open_message)

    with open(from_path, 'r') as f:
        markdown = f.read()

    with open(template_path, 'r') as f:
        template = f.read()

    title = extract_title(markdown)

    html_node = md_to_html_nodes(markdown)

    html_str = html_node.to_html()

    # Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    template = template.replace('{{ Title }}', title)
    template = template.replace('{{ Content }}', html_str)

    # ensure the destination directory is created if it doesnt exist
    dest_dir = '/'.join(dest_path.split('/')[:-1])
    os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(template)
    print(f"Page generated at {dest_path}")


# Create a generate_pages_recursive(dir_path_content, template_path, dest_dir_path) function. It should:
#
#     Crawl every entry in the content directory
#     For each markdown file found, generate a new .html file using the same template.html. The generated pages should be written to the public directory in the same directory structure.


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # keeping the structure of the content directory in the public directory

    for item in os.listdir(dir_path_content):
        s = os.path.join(dir_path_content, item)
        d = os.path.join(dest_dir_path, item)
        if os.path.isdir(s):
            generate_pages_recursive(s, template_path, d)
        else:
            if s.endswith('.md'):
                generate_page(s, template_path, d.replace('.md', '.html'))
            else:
                print(f"Copying {s} to {d}")
                shutil.copy(s, d)
                print(f"Copying {s} to {d}")
