def get_engineer_status(completed_lessons: int) -> str:
    # БАГ: Если уроков ровно 10, функция должна вернуть "Junior",
    # но из-за знака > она вернет "Beginner".
    if completed_lessons >= 10:
        status = "Junior"
    else:
        status = "Beginner"
    return status


# Проверяем граничное значение
print(get_engineer_status(10))
