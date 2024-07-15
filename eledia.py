import os
import re

def eledia_text(id, dir):
    def find_eledia_files(dir):
        eledia_files = []
        for root, _, files in os.walk(dir):
            for file in sorted(files):
                if file.endswith('.eledia'):
                    eledia_files.append(os.path.join(root, file))
        return eledia_files

    def extract_text_from_file(file_path, id):
        with open(file_path, 'r') as file:
            for line in file:
                match = re.match(rf'^{id}: (.+)', line)
                if match:
                    return match.group(1)
        return None

    eledia_files = find_eledia_files(dir)
    result_texts = []

    for file in eledia_files:
        text = extract_text_from_file(file, id)
        if text:
            result_texts.append(text)

    return ' '.join(result_texts)

if __name__ == "__main__":
    print(eledia_text(1, r'c:\Users\tadib\eledia\eledia_test'))
