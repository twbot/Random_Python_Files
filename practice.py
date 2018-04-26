#!/usr/bin/env python3

'''
Removes vowels from inputed string
'''
def vowels():
	vowels = ['a', 'e', 'i', 'o', 'u']
	word = list(input('Please input any word.\n'))
	for x in word:
		for vowel in vowels:
			if x == vowel:
				word.remove(x)
	str1 = ''.join(word)
	print(str1)

'''
Turns first half of string lowercase and
second half uppercase
'''
def silly_case():
	word = str(input('Please input any word: '))
	word_len = int((len(word))/2)
	word_1h = str(word[:word_len]).lower()
	word_2h = str(word[word_len:]).upper()
	print(word_1h + word_2h)

'''
1. Inputed string.lower()
2. counts number of times word occurs in a string
3. stores word as key in dict
4. stores number of times word occurs as value
'''
def count(string):
    word_count = {}
    string = string.lower()
    word_list = string.split(' ')
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
        	word_count[word] = 1
    return word_count

def format_string_with_dict(dictionary):
	#Example dictionary: me_dict = {'name': 'Tristan Brodeur', 'job' : 'Engineer'}
	string = 'I am {name} and I am a(n) {job}'
	print(string.format(**dictionary))

'''
Return teacher with most classes
The dictionary will be something like:
{'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
 'Kenneth Love': ['Python Basics', 'Python Collections']}
'''
def most_classes(teacher_dict):
    max_count = 0
    teacher_name = ''
    for teacher in teacher_dict:
        num_classes = 0
        for classes in teacher_dict[teacher]:
            num_classes += 1
        if num_classes > max_count:
            max_count = num_classes
            teacher_name = teacher
    return teacher_name

'''
Returns list of lists containing teacher name and number of classes
[<teacher name>, <number of classes taught>]
The dictionary will be something like:
{'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],
 'Kenneth Love': ['Python Basics', 'Python Collections']}
 '''
def stats(teacher_dict):
    teacher_list = []
    for teacher in teacher_dict:
        num_classes = len(teacher_dict[teacher])
        inner_list = [teacher, num_classes]
        teacher_list.append(inner_list)
    return teacher_list

def main():
	
if __name__ == '__main__':
	main()

