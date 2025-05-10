# Contents

- **hyperspec_final_local**
  - This is the file containing all of the notebooks which serve as independant experiments. This is what notebook_runner.py script uses.
- **notebook_runner.py**
  - A python script which automates the running of 120 independant experimental runs, using the aforementioned notebooks, and then saves each resulting notebook + all model embeddings + indices + confusion matrix for each model/model+classifier
- **copy_of_result_notebooks**
  - A file containing a copy of ONLY the notebooks resulting from each 120 experiment run. (The saved model embeddings are too large to be pushed with Git.) 

# How to reproduce the experiments
- Clone this repository to a directory
- Open 'notebook_runner.py' with your IDE
- Set the directories for each notebook samples-per-class configuration accordingly
- Set the directory to which you would like to save the results (ensure that the storage medium being used has 125Gb unallocated)
- Save the changes made to 'notebook_runner.py'
- Launch Anaconda Prompt (if using Conda as environment for Jupyter Notebook)
- In the terminal window, enter 'cd [directory to which you cloned the repo]'
- Once the current directory is accordingly set, type the command 'python notebook_runner.py' and press the 'Enter' key
- The experiments will run accordingly until completion.
