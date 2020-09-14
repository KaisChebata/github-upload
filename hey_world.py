try:
    with open('greetings_text.txt', 'r') as file_readr:
        greetings_msg = file_readr.read().strip()
    
except FileNotFoundError as file_error:
    print(f'{file_error}')


print(greetings_msg)

