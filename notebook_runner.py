import argparse
import os
from nbformat import read, write, NO_CONVERT
from nbclient import NotebookClient

#paths
NOTEBOOK_PATHS = {
    ("pavia", 5): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\pavia\hyperspec_final_local_pavia_5sample.ipynb",
    ("pavia", 10): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\pavia\hyperspec_final_local_pavia_10sample.ipynb",
    ("pavia", 20): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\pavia\hyperspec_final_local_pavia_20sample.ipynb",
    ("pavia", 40): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\pavia\hyperspec_final_local_pavia_40sample.ipynb",
    ("botswana", 5): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\botswana\hyperspec_final_local_botswana_5sample.ipynb",
    ("botswana", 10): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\botswana\hyperspec_final_local_botswana_10sample.ipynb",
    ("botswana", 20): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\botswana\hyperspec_final_local_botswana_20sample.ipynb",
    ("botswana", 40): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\botswana\hyperspec_final_local_botswana_40sample.ipynb",
    ("indian_pines", 5): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\indian_pines\hyperspec_final_local_indian_pines_5sample.ipynb",
    ("indian_pines", 10): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\indian_pines\hyperspec_final_local_indian_pines_10sample.ipynb",
    ("indian_pines", 20): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\indian_pines\hyperspec_final_local_indian_pines_20sample.ipynb",
    ("indian_pines", 40): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\indian_pines\hyperspec_final_local_indian_pines_40sample.ipynb",
    ("KSC", 5): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\KSC\hyperspec_final_local_KSC_5sample.ipynb",
    ("KSC", 10): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\KSC\hyperspec_final_local_KSC_10sample.ipynb",
    ("KSC", 20): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\KSC\hyperspec_final_local_KSC_20sample.ipynb",
    ("KSC", 40): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\KSC\hyperspec_final_local_KSC_40sample.ipynb",
    ("paviaU", 5): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\paviaU\hyperspec_final_local_paviaU_5sample.ipynb",
    ("paviaU", 10): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\paviaU\hyperspec_final_local_paviaU_10sample.ipynb",
    ("paviaU", 20): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\paviaU\hyperspec_final_local_paviaU_20sample.ipynb",
    ("paviaU", 40): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\paviaU\hyperspec_final_local_paviaU_40sample.ipynb",
    ("salinas", 5): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\salinas\hyperspec_final_local_salinas_5sample.ipynb",
    ("salinas", 10): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\salinas\hyperspec_final_local_salinas_10sample.ipynb",
    ("salinas", 20): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\salinas\hyperspec_final_local_salinas_20sample.ipynb",
    ("salinas", 40): r"C:\Users\vella\Documents\GitHub\FYP2425_LOCAL\hyperspec_final_local\salinas\hyperspec_final_local_salinas_40sample.ipynb",
}


def notebook_runner(input_nb_path: str, output_nb_path: str, run_dir: str):
    #read notebook
    with open(input_nb_path, "r", encoding="utf-8") as f:
        nb = read(f, as_version=NO_CONVERT)

    #creating client notebook
    client = NotebookClient(
        nb,
        timeout=4000,
        kernel_name="python3",
        #kernel working dir set to run_dir
        resources={'metadata': {'path': run_dir}}
    )

    print(f"[INFO] Restarting kernel for fresh execution of '{input_nb_path}'")
    print(f"[INFO] Kernel working directory set to: {run_dir}")

    #starting kernel and exec each code cell
    with client.setup_kernel():
        for i, cell in enumerate(nb.cells):
            if cell.cell_type == "code":
                try:
                    client.execute_cell(cell, cell_index=i, execution_count=None)
                    print(f"Executed cell {i+1} successfully.")
                except Exception as e:
                    print(f"ERROR ENCOUNTERED in cell {i+1}:\n{e}")
                    raise

    #saving copy of notebook
    with open(output_nb_path, "w", encoding="utf-8") as f:
        write(nb, f)
    print(f"\nNotebook saved to {output_nb_path}\n")


def run_notebook_n_times(
    input_nb_path: str, 
    base_output_dir: str, 
    dataset: str, 
    sample: int, 
    n_runs: int = 5
):
    os.makedirs(base_output_dir, exist_ok=True)

    for i in range(1, n_runs + 1):
        run_dir = os.path.join(base_output_dir, f"run_{i}")
        os.makedirs(run_dir, exist_ok=True)

        notebook_filename = f"{dataset}_{sample}_run_{i}.ipynb"
        out_path = os.path.join(run_dir, notebook_filename)

        print("===========================================")
        print(f"=== Starting run #{i} for {dataset}, {sample} samples")
        print(f"Run directory: {run_dir}")
        
        notebook_runner(input_nb_path, out_path, run_dir)

def main():

    num_runs = 5

    #base dir
    base_save_dir = r"D:\experiments_final"

    #looping over each dataset and number of samples
    for (dataset, sample), notebook_path in NOTEBOOK_PATHS.items():
        print("====================================================")
        print(f"Now running dataset='{dataset}', samples={sample}")
        print(f"Notebook path: {notebook_path}")

        ds_sample_output_dir = os.path.join(base_save_dir, f"{dataset}_{sample}")

        run_notebook_n_times(
            input_nb_path=notebook_path,
            base_output_dir=ds_sample_output_dir,
            dataset=dataset,
            sample=sample,
            n_runs=num_runs
        )

    print("All notebooks finished.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run all notebooks in NOTEBOOK_PATHS, each 5 times, each run in its own subdirectory."
    )
    args = parser.parse_args()
    main()