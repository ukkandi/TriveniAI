from PIL import Image
import pytesseract
import os

def extract_text(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)

def clean_text(text):
    # Remove stray returns and collapse extra spaces
    paragraphs = [p for p in text.replace('\r','').split('\n\n') if p.strip()]
    return '\n\n'.join(' '.join(p.split()) for p in paragraphs)

def chunk_text(cleaned):
    chunks, lines = [], cleaned.split('\n')
    curr_header, curr_lines = None, []
    for line in lines:
        if line.isupper():
            if curr_lines:
                chunks.append((curr_header or "GENERAL", ' '.join(curr_lines)))
            curr_header, curr_lines = line, []
        else:
            curr_lines.append(line)
    if curr_lines:
        chunks.append((curr_header or "GENERAL", ' '.join(curr_lines)))
    return chunks

if __name__ == "__main__":
    sample = "samples/flyer1.jpg"
    if not os.path.exists(sample):
        print("Missing sample:", sample); exit(1)

    raw = extract_text(sample)
    print("RAW TEXT:\n", raw, "\n")

    cleaned = clean_text(raw)
    print("CLEANED TEXT:\n", cleaned, "\n")

    print("CHUNKS:")
    for header, text in chunk_text(cleaned):
        print(f"== {header} ==\n{text}\n")

