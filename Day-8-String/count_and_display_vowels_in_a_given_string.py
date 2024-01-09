given_string = input("Enter a sentence: ")
count_of_vowels = 0 
for i in given_string:
    if(i in ['a','e','i','o','u','A','E','I','O','U']):
        count_of_vowels = count_of_vowels + 1
        
print("Number of Vowels in Given String are: ", count_of_vowels)
