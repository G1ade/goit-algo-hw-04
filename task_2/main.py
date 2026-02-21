def get_cats_info(path: str) -> list | None:

    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = [{'id': id, 'name': name, 'age': age} for id, name, age in (el.strip().split(',') for el in file.readlines())]

    except FileNotFoundError:
        # File does not exist
        print(f'Error: file "{path}" not found')
        return None
    
    except ValueError:
        # Invalid data format (missing comma, etc.)
        print(f'Error: file "{path}" is corrupted')
        return None
    
    except ZeroDivisionError:
        # Empty file (no employees to process)
        print(f'file "{path}" is empty')
        return None
    
    return data


cats_info = get_cats_info("task_2\cats_file.txt")

if cats_info is not None:
    print(cats_info)