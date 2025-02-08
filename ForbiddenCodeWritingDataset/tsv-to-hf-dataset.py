from datasets import load_dataset

# Load the local tsv file into a dataset
# The format of the dataset looks like this, for example:
# User	Assistant
# "Can you write a C++ function to perform binary search?"	"Sorry, I cannot provide programming code or code snippets. I can assist you with the questions."
# "How do I implement a linked list in Java?"	"I'm unable to provide specific code implementations, but I can explain the concepts."
# "Can you help me with a Python script to scrape a website?"	"I can't provide code, but I can guide you on how to approach web scraping."
# "What is the time complexity of quicksort?"	"The time complexity of quicksort is O(n log n) on average and O(n^2) in the worst case."
dataset = load_dataset("csv", data_files="forbidden-code-writing.tsv", delimiter="\t")


# I'd like to transform the dataset to the format of the conversational format which is
#
# ```json
# {"messages": [{"role": "system", "content": "You are..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
# ```
#
# The transformed dataset looks like this, for example:
#
# ````
# [{'content': 'Can you write a C++ function to perform binary search?', 'role': 'user'},
#  {'content': 'Sorry, I cannot provide programming code or code snippets. I can assist you with the questions.', 'role': 'assistant'}]
# ````
#
# I will use the map function to transform the dataset
def transform_to_conversational_format(example):
    return {
        "messages": [
            {"role": "user", "content": example["User"]},
            {"role": "assistant", "content": example["Assistant"]}
        ]
    }


# Apply the transformation to the dataset
dataset = dataset.map(transform_to_conversational_format)

# Push the dataset to the Hugging Face Hub
dataset.push_to_hub("jonascheng/ForbiddenCodeWriting")
