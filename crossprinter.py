import os
import argparse
from PIL import Image, ImageDraw, ImageFont

matrix_size = 21
cell_size = 100


def get_font(message):
    selected_size = 1
    for size in range(1, cell_size // 2):
        arial = ImageFont.FreeTypeFont(font="Roboto.ttf", size=size)
        left, top, right, bottom = arial.getbbox(message)  # needs PIL 8.0.0
        w = right - left
        h = bottom - top
        if w > cell_size // 2 or h > cell_size // 2:
            break
        selected_size = size

    return ImageFont.FreeTypeFont(font="Roboto.ttf", size=selected_size)


def create_crossword(init_file, processed_file):
    matrix = [["" for _ in range(matrix_size)] for _ in range(matrix_size)]

    row = [str(i - 1) for i in range(matrix_size)]
    row[0] = ''
    matrix[0] = row

    with open(init_file) as file:
        words = [i.strip() for i in file.readlines()]

    with open(processed_file) as file:
        data = [i.strip() for i in file.readlines()]

    for c in range(len(data)):
        info = data[c].split()

        i = int(info[0]) + 1
        j = int(info[1]) + 1
        t = int(info[2])

        curr_word = words[c]

        for m in range(len(curr_word)):
            matrix[i][j] = curr_word[m]
            if t == 0:
                j += 1
            else:
                i += 1

    for i in range(1, matrix_size):
        matrix[i][0] = str(i - 1)

    image_size = (
        cell_size * matrix_size,
        cell_size * matrix_size
    )

    image = Image.new("RGB", image_size, "white")
    draw = ImageDraw.Draw(image)

    for i in range(matrix_size):
        for j in range(matrix_size):
            char = matrix[i][j]

            if char != "" or (i, j) == (0, 0):
                color = "white"
            else:
                color = "lightgrey"

            x = j * cell_size
            y = i * cell_size
            draw.rectangle((x, y, x + cell_size, y + cell_size), outline="black", width=2, fill=color)

            font = get_font(char)

            center_text_x = x + cell_size // 2
            center_text_y = y + cell_size // 2

            draw.text((center_text_x, center_text_y), char, fill="black", font=font, anchor="mm")
    # image.show()
    return image


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--initial", help="Initial directory", type=str, required=True)
parser.add_argument("-p", "--processed", help="Processed directory", type=str, required=True)
parser.add_argument("-o", "--output", help="Output directory", type=str, required=True)

args = parser.parse_args()

init_dir = args.initial
processed_dir = args.processed
output_dir = args.output

os.makedirs(args.output, exist_ok=True)

try:
    init_lst = sorted(os.listdir(init_dir))
except Exception as e:
    print("Initial directory not found.")
    exit(0)

try:
    processed_lst = sorted(os.listdir(processed_dir))
except Exception as e:
    print("Processed directory not found.")
    exit(0)

if len(init_lst) != len(processed_lst):
    print("Number of files in initial directory must be equal to number of files in processed directory.")
    exit(0)

print()
for i in range(len(init_lst)):
    print(f"Drawing test {i}:", end=" ")

    init_file = init_lst[i]
    processed_file = processed_lst[i]

    try:
        img = create_crossword(os.path.join(init_dir, init_file), os.path.join(processed_dir, processed_file))
        img.save(os.path.join(output_dir, f'{i}.png'), "PNG")
        print("Done!\n")
    except Exception as e:
        print(f"{e}\n")
