import subprocess,os

counter = 1000

def run_filecpu(path):
    global counter
    counter += 1
    subprocess.run(f'relog -f csv {path} -o {str(counter)}cpu.csv')

def run_filemem(path):
    global counter
    counter += 1
    subprocess.run(f'relog -f csv {path} -o {str(counter)}mem.csv')

def run_filenet(path):
    global counter
    counter += 1
    subprocess.run(f'relog -f csv {path} -o {str(counter)}net.csv')

def run_all_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".blg"):
            joined_file = os.path.join(folder_path, filename)
            if 'cpu' in filename.lower():
                run_filecpu(joined_file)
            elif 'mem' in filename.lower():
                run_filemem(joined_file)
            elif 'net' in filename.lower():
                run_filenet(joined_file)
