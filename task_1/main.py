def total_salary(path: str) -> tuple | None:
    """
    Calculate total and average salary from a text file.
    
    The file should contain employee data in format: name,salary (one per line)
    Example: Alex Korp,3000
    
    Args:
        path (str): Path to the salary file
        
    Returns:
        tuple: (total_salary, average_salary) or (None, None) if error occurs
    """
    try:
        # Open and read the file, split each line by comma
        with open(path, 'r', encoding='utf-8') as file:
            data = [el.strip().split(',') for el in file.readlines()]

        # Convert to list of dictionaries with name and salary
        dictionary = [{'name': name, 'salary': int(salary)} for name, salary in data]

        # Calculate total and average salary
        total = sum(el['salary'] for el in dictionary)
        average = total // len(data)

    except FileNotFoundError:
        # File does not exist
        print(f'Error: file "{path}" not found')
        return None, None
    
    except ValueError:
        # Invalid data format (missing comma, non-numeric salary, etc.)
        print(f'Error: file "{path}" is corrupted')
        return None, None
    
    except ZeroDivisionError:
        # Empty file (no employees to process)
        print(f'file "{path}" is empty')
        return None, None 

    return total, average


total, average = total_salary('task_1\salary_file.txt')

# Check if calculation was successful before printing result
if total is not None and average is not None:
    print(f"Total salary amount: {total}, Average salary: {average}")