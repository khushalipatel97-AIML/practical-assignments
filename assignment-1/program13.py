#13.  Write a program to read numbers from a file and calculate the average.
def calculate_average(file_path):
    total_sum = 0.0
    count = 0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 2. Clean and convert data
                cleaned_line = line.strip()
                if cleaned_line:  
                    total_sum += float(cleaned_line)
                    count += 1
                    
        if count == 0:
            return "The file is empty."
        return total_sum / count

   
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except ValueError:
        return "Error: The file contains text or invalid characters."

file_name = "demo1.txt"
result = calculate_average(file_name)
print(f"Average: {result}")
