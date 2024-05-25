"""Demonstrate dictionary comprehensions."""

def main():
	document = '\tAs a kid, I dreamed of exploring the Amazon jungle. ' \
		'My friends and I watched a TV show about Amazon explorers and ' \
		'their adventures.\n\tThey became tangled in huge webs and fought ' \
		'huge spiders. Every creature seemed larger than life.\n' \
		'\tWhen we finished watching the show, we explored the woods next ' \
		'to our neighborhood and imagined we were exploring the Amazon. ' \
		'We fashioned machetes from aluminum window frames and chopped ' \
		'our way through the brush as best we could. To us kids, the ' \
		'machetes were real and our adventures were just as exciting. ' \
		'Thankfully, the spiders were small.'
	
	# Print document to console for reference
	print(document)
	print('*' * 60)
	
	# Split the document into paragraphs
	paragraph_list = document.split('\n')

	# Use the enumerate() function to extract the indices and values from list
	paragraph_dict = {(key + 1):value for key, value in enumerate(paragraph_list)}
	
	# Print the key and value of each dictionary entry
	for key, value in paragraph_dict.items():
		print(f'Paragraph {key}: {value}')


		



if __name__ == '__main__':
	main()