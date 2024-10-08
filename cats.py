def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding="utf-8") as f:
            salary_file = f.readlines()
            for line in salary_file:
                cat = {}
                row_line = line.split(",")
                cat['id'] = row_line[0]
                cat['name'] = row_line[1]
                cat['age'] = row_line[2].strip()
                cats.append(cat)
        return cats
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return None

cats_info = get_cats_info("/Users/yuriim/Projects/pycharm/goit-pycore-hw-04/cats.txt")
print(cats_info)