import random

# 📘 Шаблоны сюжетных задач с заранее заданной грамматикой
story_templates = [
    {
        "template": "У Оли было {a} конфет. Она съела {b}. Сколько у неё осталось?",
        "answer_func": lambda a, b: a - b if a >= b else None
    },
    {
        "template": "Петя нашёл {a} яблок, а Маша — {b}. Сколько всего яблок?",
        "answer_func": lambda a, b: a + b
    },
    {
        "template": "Саша купил {a} карандашей, потом ещё {b}. Сколько теперь у него?",
        "answer_func": lambda a, b: a + b
    },
    {
        "template": "У Вики {a} наклеек. Она подарила {b}. Сколько осталось у Вики?",
        "answer_func": lambda a, b: a - b if a >= b else None
    },
    {
        "template": "Антон съел {a} печенек утром и {b} вечером. Сколько всего он съел?",
        "answer_func": lambda a, b: a + b
    },
    {
        "template": "Таня нашла {a} монеток, а потом нашла ещё {b}. Сколько теперь у Тани?",
        "answer_func": lambda a, b: a + b
    },
]

# 🎲 Генерация сюжетной задачи по шаблону
def generate_story_task():
    for _ in range(5):  # пробуем до 5 раз
        template = random.choice(story_templates)
        a = random.randint(2, 10)
        b = random.randint(1, 9)
        result = template["answer_func"](a, b)
        if result is None or result < 0:
            continue
        question = template["template"].format(a=a, b=b)
        return question, str(result)
    # fallback если всё пошло по жопе
    return "У Маши 2 яблока, у Пети 3. Сколько всего?", "5"

# 🔢 Генерация обычных примеров
def generate_task(level=1):
    if level == 1:
        # 50/50 — обычная или сюжетная задача
        if random.random() < 0.5:
            return generate_story_task()
        else:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            op = random.choice(["+", "-"])
            if op == "-" and a < b:
                a, b = b, a
            question = f"{a} {op} {b}"
            answer = str(eval(question))

    elif level == 2:
        op = random.choice(["+", "-", "*", "/"])
        a = random.randint(10, 99)
        b = random.randint(1, 99)

        if op == "-":
            if a < b:
                a, b = b, a
        elif op == "/":
            b = random.randint(1, 9)
            a = b * random.randint(1, 9)

        question = f"{a} {op} {b}"
        answer = str(int(eval(question)))

    elif level == 3:
        a = random.randint(2, 9)
        b = random.randint(10, 99)
        c = random.randint(2, 9)
        op1 = random.choice(["+", "-"])
        expr = f"({a} {op1} {b}) * {c}"
        try:
            result = eval(expr)
            if result > 1000:
                return generate_task(level)
            answer = str(int(result))
        except:
            return generate_task(level)

        question = expr

    else:
        return generate_task(1)

    return question, answer
