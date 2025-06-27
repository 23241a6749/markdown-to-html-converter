# 📝 Markdown to HTML Converter

A simple command-line tool that reads a Markdown (`.md`) file and converts it into a clean, well-formatted HTML (`.html`) file.

---

## 🚀 Features

- Converts `.md` files to `.html` with ease
- Supports standard Markdown syntax:
  - Headers (`#`, `##`, etc.)
  - Bold and Italics
  - Ordered and unordered lists
  - Links
  - Inline code and code blocks
- Lightweight and beginner-friendly
- Clean and readable HTML output

---

## 🧰 Requirements

- Python 3.x
- [`markdown`](https://pypi.org/project/Markdown/)

Install the required dependency using:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
markdown-to-html/
├── converter.py           # Main CLI tool
├── sample.md              # Sample input Markdown file
├── output.html            # HTML output file
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── assets/                # Screenshots or screen recordings (optional)
```

---

## ⚙️ How to Use

1. Clone this repository or download the files:

```bash
git clone https://github.com/yourusername/markdown-to-html-converter.git
cd markdown-to-html-converter
```

2. Place your Markdown file (e.g., `sample.md`) in the project directory.

3. Run the converter tool using:

```bash
python converter.py sample.md output.html
```

4. Open `output.html` in your browser to view the converted result.

---

## 🧪 Example

### ✅ Input (`sample.md`)

```markdown
# Markdown to HTML Converter

This is a **bold** statement and this is *italicized*.

## Features

- Headers
- Lists
- **Bold**, *Italics*
- [Links](https://example.com)
- Inline `code`

```python
print("Hello, world!")
```
```

### 🌐 Output (`output.html`)

```html
<h1>Markdown to HTML Converter</h1>
<p>This is a <strong>bold</strong> statement and this is <em>italicized</em>.</p>
<h2>Features</h2>
<ul>
  <li>Headers</li>
  <li>Lists</li>
  <li><strong>Bold</strong>, <em>Italics</em></li>
  <li><a href="https://example.com">Links</a></li>
  <li><code>code</code></li>
</ul>
<pre><code class="language-python">print("Hello, world!")</code></pre>
```

---

## 📸 Screenshots

> Add your screenshots or screen recordings in the `assets/` folder and embed them below.

![Terminal Screenshot]![image](https://github.com/user-attachments/assets/984f1dd1-ebd8-4374-8638-1a579321b7f0)

![Output Screenshot]![image](https://github.com/user-attachments/assets/9dc4caa9-8bdd-4342-976e-9e28be613b72)


---


## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---
