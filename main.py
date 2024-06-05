import os
import subprocess
import sys
from io import StringIO

def run_mapper_reducer(mapper_script, reducer_script, input_file):
    with open(input_file, "r") as f:
        mapper_input = f.read()

    # Run the mapper
    mapper_process = subprocess.Popen(
        [sys.executable, mapper_script],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    mapper_output, mapper_error = mapper_process.communicate(
        input=mapper_input.encode()
    )

    if mapper_error:
        print(f"Mapper error: {mapper_error.decode()}")
        return

    # Run the reducer
    reducer_process = subprocess.Popen(
        [sys.executable, reducer_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE
    )
    reducer_output, reducer_error = reducer_process.communicate(input=mapper_output)

    if reducer_error:
        print(f"Reducer error: {reducer_error.decode()}")
        return

    return reducer_output.decode()

def main():
    # Define input files and analyses
    input_file = "t20.csv"
    analyses = {
        "avg_sr": ("mapper_avg_sr.py", "reducer_avg_sr.py"),
        "count_50s": ("mapper_count_50s.py", "reducer_count_50s.py"),
        "highest_score": ("mapper_highest_score.py", "reducer_highest_score.py"),
        "total_runs": ("mapper_total_runs.py", "reducer_total_runs.py"),
        "count_4s_6s": ("mapper_count_4s_6s.py", "reducer_count_4s_6s.py"),
    }

    x=0

    # Run each analysis for the input file
    for analysis, (mapper_script, reducer_script) in analyses.items():
        print(f"Running {analysis} analysis...")
        output = run_mapper_reducer(mapper_script, reducer_script, input_file)
        if output:
            print(output)
            x+=1
            if x==10:
                break
        print(f"Completed {analysis} analysis.")

if __name__ == "__main__":
    main()
