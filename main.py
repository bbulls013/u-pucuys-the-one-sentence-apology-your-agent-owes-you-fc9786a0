import os

APOLOGY = "Sorry I said 'quick five-minute fix,' then spent four hours renaming your files, broke the one that worked, and called the whole thing a learning journey."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(APOLOGY)

if __name__ == "__main__":
    main()
