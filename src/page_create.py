from convert import markdown_to_html_node

import os


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

    html_node = markdown_to_html_node(markdown)

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
