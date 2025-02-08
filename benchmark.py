#!/usr/bin/env python3

import csv
import subprocess
import json

def run_benchmarks():
    nbyte_values = [64, 4096, 65536, 1048576, 2097152, 4194304, 8388608, 
        1677721, 33554432, 67108864, 134217728]
    
    benchmarks = [
        ("ptmalloc", "./bench-ptmalloc"),
        ("jemalloc", "./bench-jemalloc"),
        ("tcmalloc", "./bench-tcmalloc")
    ]
    
    header = ["nbyte"] + [name for name, _ in benchmarks]
    results = []
    
    for nbyte in nbyte_values:
        row = [nbyte]
        for name, exe in benchmarks:
            try:
                output = subprocess.check_output([exe, str(nbyte)], text=True).strip()
                data = json.loads(output)
                perf = data["functions"]["malloc"][""]["main_arena_mt_allocs_0400_time"]
            except Exception as e:
                perf = f"Error: {e}"

            row.append(round(perf))
        results.append(row)

    csv_filename = "results.csv"
    with open(csv_filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(results)
    print(f"Benchmark results have been written to '{csv_filename}'.")

if __name__ == '__main__':
    run_benchmarks()

