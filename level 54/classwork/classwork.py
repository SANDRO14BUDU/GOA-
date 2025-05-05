def get_number(prompt):
    try:
        return float(input(prompt))
    except:
        raise ValueError("შეიყვანე მხოლოდ რიცხვი.")

def divide_numbers():
    try:
        num1 = get_number("მრიცხველი: ")
        num2 = get_number("სახარი: ")
        if num2 == 0:
            raise ValueError("ნულზე გაყოფა აკრძალულია.")
        print("შედეგი:", num1 / num2)
    except ValueError:
        print("შეცდომა: მონაცემი არასწორია ან ნულზე გაყოფა სცადე.")
    finally:
        print("ოპერაცია დასრულდა.")

divide_numbers()
