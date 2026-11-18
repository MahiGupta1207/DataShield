import logging
import subprocess
import sys
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_script(script_name):

    print('\nRunning:', script_name)
    logging.info("Starting execution: %s", script_name)

    try:
        subprocess.run(
            [sys.executable, script_name],
            check=True
        )

        print(script_name, 'completed successfully!!')
        logging.info("Successfully completed: %s", script_name)

    except subprocess.CalledProcessError as error:
        print(script_name, 'failed!')
        logging.error("Execution failed: %s | Error: %s", script_name, error)
        raise

if __name__ == "__main__":

    logging.info("========== DataShield Pipeline Started ==========")
    print("\nDataShield pipeline started!")

    try:
        run_script("src/ingest_data.py")
        run_script("src/validate_data.py")
        run_script("src/load_to_mysql.py")

        print("\nDataShield pipeline completed successfully!")
        logging.info("DataShield pipeline completed successfully!")

    except subprocess.CalledProcessError:
        print("\nDataShield pipeline failed!")
        logging.error("DataShield pipeline failed!")
