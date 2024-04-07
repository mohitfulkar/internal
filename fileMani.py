def count_words(text): 
    words = text.split() 
    return len(words) 
def count_characters(text): 
    return len(text) 
 
def count_vowels(text): 
    vowels = 'aeiouAEIOU' 
    return sum(1 for char in text if char in vowels) 
 
def count_lines(text): 
    lines = text.split('\n') 
    return len(lines) 
 
def reverse_words(text): 
    words = text.split() 
    reversed_words = [word[::-1] for word in words] 
    return ' '.join(reversed_words) 
 
def main(): 
    filename = input("Enter the name of the file: ") 
     
    try: 
        with open(filename, 'r') as file: 
            content = file.read() 
            print(f"Number of words: {count_words(content)}") 
            print(f"Number of characters: {count_characters(content)}") 
            print(f"Number of vowels: {count_vowels(content)}") 
            print(f"Number of lines: {count_lines(content)}") 
            print("Words reversed:") 
            print(reverse_words(content)) 
    except FileNotFoundError: 
        print(f"Error: File '{filename}' not found.") 
 
if __name__ == "__main__": 
    main() 