import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as md_file:
        text = md_file.read()
        html = markdown.markdown(text, extensions=['extra', 'codehilite', 'tables'])

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html)
    print(f"✅ Converted '{input_file}' to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py input.md output.html")
    else:
        convert_markdown_to_html(sys.argv[1], sys.argv[2])
