import os

def save_text(text, path="outputs/generated_record.txt"):
    os.makedirs("outputs", exist_ok=True)
    with open(path, "w") as f:
        f.write(text)

