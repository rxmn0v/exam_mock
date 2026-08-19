def count_vowels_and_consonants(text: str) -> dict:
    text = text.strip().lower()

    vowels = ["a", "e", "i", "o", "u"]

    vowels_count = 0
    cons_count = 0

    for i in text:
        if i in vowels:
            vowels_count += 1
        elif i.isalpha():
            cons_count += 1

    count_v_c = {
        "unli": vowels_count,
        "undosh": cons_count
    }

    return count_v_c


print(count_vowels_and_consonants("Salom Dunyo!"))