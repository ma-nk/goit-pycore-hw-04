def total_salary(path):
    user_salaries = []
    try:
        with open(path, 'r') as f:
            salary_file = f.readlines()
            for line in salary_file:
                row_line = line.split(",")
                user_salaries.append(int(row_line[1]))
        return sum(user_salaries), sum(user_salaries) / len(user_salaries)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None


path = input("print path >>>")
print(total_salary(path))