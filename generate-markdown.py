import os
import re

PROBLEM_DIR = "problems"
OUTPUT_DIR = "solutions"

md_files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".md")]

os.makedirs(OUTPUT_DIR, exist_ok=True)

MARKDOWN_TEMPLATE = """# {id}. {title}

- **Difficulty:** _[add difficulty here]_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/{slug}/)

---

## 🧩 Description

[Paste the problem description here or keep this as a placeholder.]

---

## 💡 Approach

[Write a brief explanation of your approach.]

```python
{code}
```

---

## 📈 Complexity

- **Time Complexity:** O(_?_)

- **Space Complexity:** O(_?_)

---
"""


def format_title(title):
    return " ".join(word.capitalize() for word in title.split('-'))


def generate_md_files():
    for filename in os.listdir(PROBLEM_DIR):
        md_filename = filename.replace(".py", ".md")
        if filename.endswith(".py") and re.match(r"^\d{4}-.*\.py$", filename) and md_filename not in md_files:
            problem_id, *slug_parts = filename.replace(".py", "").split("-")
            slug = "-".join(slug_parts)
            title = format_title(slug)
            filepath = os.path.join(PROBLEM_DIR, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read().strip()

            md_content = MARKDOWN_TEMPLATE.format(
                id=problem_id,
                title=title,
                slug=slug,
                code=code
            )

            with open(os.path.join(OUTPUT_DIR, md_filename), "w", encoding="utf-8") as md_file:
                md_file.write(md_content)

            print(f"✅ Created: {md_filename}")


if __name__ == "__main__":
    generate_md_files()
