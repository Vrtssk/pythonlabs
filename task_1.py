def formatFullName(lastName, firstName, middleName):
    lastName = lastName.strip().capitalize()
    firstInitial = firstName.strip()[0].upper()
    middleInitial = middleName.strip()[0].upper()
    return f"{lastName} {firstInitial}.{middleInitial}."


def main():
    lastName = input("Введите фамилию: ")
    firstName = input("Введите имя: ")
    middleName = input("Введите отчество: ")
    print(f"ФИО в формате 'Фамилия И.О.': {formatFullName(lastName, firstName, middleName)}")


if __name__ == "__main__":
    main()
