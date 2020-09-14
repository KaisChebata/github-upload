try:
    with open('greetings_text.txt', 'r') as file_readr:
        greetings_msg = file_readr.read().strip()
    
except FileNotFoundError as file_error:
    print(f'{file_error}')

print('this is where we should greetings')
name = input('tell us your name, and give greetings ... ')
print(f'I am {name}, {greetings_msg}')

