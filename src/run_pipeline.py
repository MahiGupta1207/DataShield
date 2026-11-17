import subprocess
import sys
def run_script(script_name):
    print('\nRunning:',script_name)
    subprocess.run(
        [sys.executable,script_name],
        check=True
    )
    print(script_name,'completed successfully!!')
if __name__=="__main__":
    run_script("src/ingest_data.py")
    run_script("src/validate_data.py")
    run_script("src/load_to_mysql.py")
    print("\nDataShield pipeline completed successfully!")