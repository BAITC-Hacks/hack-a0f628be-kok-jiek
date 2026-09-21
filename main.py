import re
from pathlib import Path


def words(text):
    return set(re.findall(r"[а-яa-z0-9]+", text.lower().replace("ё", "е")))


faq = []
path = Path(__file__).with_name("faq.txt")

for line in path.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    question, keywords, answer = line.split("|", 2)
    faq.append((words(keywords), answer.strip()))

print("Привет! Спроси про время, команду, трек, сдачу или призы.")
print("Чтобы закончить, напиши «выход».")

while True:
    try:
        user_input = input("\nТы: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nПока!")
        break

    if user_input.lower() == "выход":
        print("Пока!")
        break

    if not user_input:
        continue

    user_words = words(user_input)
    best_score = 0
    best_answer = "не знаю"

    for keywords, answer in faq:
        score = len(user_words & keywords)
        if score > best_score:
            best_score = score
            best_answer = answer

    print("Бот:", best_answer)
