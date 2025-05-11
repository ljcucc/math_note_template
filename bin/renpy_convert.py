import argparse
import os
import re
from pathlib import Path

import ziamath as zm
import cairosvg

def latex_to_png(expr_str, output_path):
    print(expr_str)
    expr = zm.Latex(expr_str, color='white')
    png_bytes = cairosvg.svg2png(expr.svg())
    with open(output_path, 'wb') as f:
        f.write(png_bytes)


def convert_latex(text, output_dir, counter):
    def replace_latex(match):
        nonlocal counter
        latex_expr = match.group(1).strip()
        filename = f"equ{counter}.png"
        filepath = os.path.join(output_dir, filename)
        latex_to_png(latex_expr, filepath)
        counter += 1
        return f"{{image=latex/{filename}}}"

    # Inline and display math ($...$ or $$...$$)
    latex_pattern = re.compile(r"\$\$?(.+?)\$\$?", re.DOTALL)
    return latex_pattern.sub(replace_latex, text), counter


def parse_markdown_blocks(md_text):
    blocks = []
    current_type = None
    current_lines = []

    for line in md_text.splitlines():
        type_match = re.match(r":::\s*(\w+)", line)
        if type_match:
            if current_type:
                blocks.append((current_type, "\n".join(current_lines).strip()))
                current_lines = []
            current_type = type_match.group(1)
        elif line.strip() == ":::":  # End of block
            if current_type:
                blocks.append((current_type, "\n".join(current_lines).strip()))
                current_type = None
                current_lines = []
        elif current_type:
            current_lines.append(line)
    return blocks


def map_block_to_renpy(block_type):
    block_type = block_type.replace("Said", "Talking")  # Normalize 'Said' to 'Talking'
    if block_type.startswith("teacher"):
        mood = block_type[len("teacher"):].lower().replace("env", "")
        return f"    show b {mood} at teacher_pos"
    elif block_type.startswith("reader"):
        mood = block_type[len("reader"):].lower().replace("env", "")
        return f"    show a {mood} at reader_pos"
    else:
        return None


def process_blocks(blocks, output_dir):
    counter = 1
    result = [
      "label book:"
    ]

    for block_type, text in blocks:
        renpy_cmd = map_block_to_renpy(block_type)

        # Convert LaTeX to PNG and replace
        processed_text, counter = convert_latex(text, output_dir, counter)

        if renpy_cmd:
            result.append(renpy_cmd)
        speaker = "b" if "teacher" in block_type.lower() else "a"
        lines = processed_text.splitlines()
        output_line = ""
        for line in lines:
            if line.strip():
                escaped_line = (
                    line.strip()
                    .replace("\\...", "...")
                    .replace('"', '\\"')
                    .replace("[", '\\[')
                    .replace("]", '\\]')
                )
                if(escaped_line[-1] == "\\"):
                  escaped_line = escaped_line[:-1]
                output_line += escaped_line
        result.append(f'    {speaker} "{output_line}"')

    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(description="Convert Markdown + LaTeX to Ren'Py script")
    parser.add_argument('--latex-store', required=True, help='Path to store LaTeX PNGs')
    parser.add_argument('--input', required=True, help='Input Markdown file')
    parser.add_argument('--output', required=True, help='Output Ren\'Py script file')
    args = parser.parse_args()

    Path(args.latex_store).mkdir(parents=True, exist_ok=True)

    with open(args.input, encoding="utf-8") as f:
        md_text = f.read()

    blocks = parse_markdown_blocks(md_text)
    renpy_script = process_blocks(blocks, args.latex_store)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(renpy_script)

    print(f"Conversion complete! Output saved to {args.output}")


if __name__ == "__main__":
    main()
