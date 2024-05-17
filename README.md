# Word/Phrase List Sorter

## Description

The **Word/Phrase List Sorter** is a utility designed to sort lists of words or phrases. This program allows users to sort words alphabetically, either considering or ignoring case sensitivity, and choose the sorting order: ascending or descending. Users can input lists directly or specify the path to a text file containing the list of words.

## Features

- **Sorting of Words or Phrases**: The program sorts a provided list of words or phrases alphabetically.
- **Sorting Options**:
  - **Sorting Order**: Users can choose to sort in ascending or descending order.
  - **Case Sensitivity**: Option to sort with or without considering case sensitivity.
- **Data Input**: Users can input a list of words as a comma-separated string or provide a path to a text file with the list.
- **Word Limit**: The program supports sorting lists containing up to 1000 words.

## How to Use

1. **Run the program.**
2. **Select the option** to sort a list of words or phrases.
3. **Choose the sorting order**: ascending or descending.
4. **Decide** whether to consider case sensitivity or not.
5. **Enter the list** of words/phrases or specify the path to a text file.
6. **Receive the sorted list.**

## Example Usage

Upon running, the program will prompt you to choose between sorting a list or exiting. Next, you will choose the sorting parameters and input the list of words or the file path. The program will process the input and return the sorted list.

## ⚠️ Limitations

- The list should contain **no more than 1000 words**.
- If only one word is input, the program will attempt to interpret it as a **path to a text file**.
- The program provides **error messages** if the input is invalid or the file is not found.

## Key Constants

- `MAX_WORDS_LIMIT = 1000`: The maximum number of words in the list.
- `WELCOME = 'Welcome to the Word/Phrase List Sorter!'`: Welcome message.
- `ENTER_CHOICE = 'Enter your choice (1 or 2): '`: Prompt for choice of action.
- `INVALID_CHOICE = '\nInvalid choice. Please enter a valid option\n'`: Message for invalid choice.
- `ENTER_LIST_OR_PATH = '\nEnter a list of words or phrases, or specify the path to a .txt file containing your list: '`: Prompt to enter a list or file path.
- `MORE_THAN_1_WORD = '\nThe list should have more than 1 word.'`: Message if fewer than two words are entered.

---

The **Word/Phrase List Sorter** is a convenient tool for sorting words and phrases, helping you easily organize your lists in the desired order.
