# Contents

- **confusion_matrices**
  - A folder containing subfolders for each dataset-sampling regime combination, in which there are the confusion matrices of each model from each experimental run. 
- **hyperspec_final_local**
  - This is the file containing all of the notebooks which serve as independant experiments. This is what notebook_runner.py script uses.
- **copy_of_result_notebooks**
  - A file containing a copy of ONLY the notebooks resulting from each 120 experiment run. (The saved model embeddings are too large to be pushed with Git.)
- **notebook_runner.py**
  - A python script which automates the running of 120 independant experimental runs, using the aforementioned notebooks, and then saves each resulting notebook + all model embeddings + indices + confusion matrix for each model/model+classifier
