from collections import defaultdict

#A function to sort a list of words by its string length
def compare_by_length(a,b):
	ret_value = 0
	if len(a) == len(b):
		return ret_value
	else:
		ret_value = -1 if len(a) < len(b) else 1
	return ret_value

def find_max_chain(word, word_dict):
	
	max_len = 0

	#Check for single character word
	if len(word) == 1:
		word_dict[word] = 1
		return 1, word_dict

	#Iterate over all the characters 
	for i in range(len(word)):
		
		#Store the word without the i^th character in temp
		temp = word[:i] + word[i+1:]
		
		#Longest possible chain is 1 greater than the longest possible 
		#chain without the removed character
		l = 1 + word_dict.get(temp,0)
		
		if l > max_len:
			max_len = l
	
	word_dict[word] = max_len
	
	return max_len, word_dict

# Complete the function below.


def  longestChain(words):

	#word_dict is used to store the longest chain possible for a valid word
	word_dict = defaultdict()
	longestChain = 0
	
	#Empty string to handle if an empty string is given part of the list
	#Then even a single character can be removed to have a valid word, that is empty string
	emptystring = 0

	#Sorting the given wordlist. Since, a valid substring of a longer substring 
	#must have been encountered while processing a shorter string

	sorted_word_list = sorted(words, cmp = compare_by_length)

	for word in sorted_word_list:

        #If empty string is part of the strings
		if word == '':
			emptystring = 1
			continue

		#Find the max_chain_length for this word
		this_chain_length, word_dict = find_max_chain(word,word_dict)
		
		#If it's the largest found yet, update the longestChain value
		if this_chain_length > longestChain:
			longestChain = this_chain_length

	return longestChain + emptystring

print longestChain(['aaa','aaaa'])
print longestChain(['a','a'])
print longestChain(['',' a'])
print longestChain(['a','a','b',''])
print longestChain(['a','abcjhjdj','asjjhsdjhdsjhsjhjfhsd','asas','ab','aba'])

print 'aba'.replace('a','',1)


