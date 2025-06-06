import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from summarizer import summarize_text

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "summaries"
LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "events.log")

# Create log directory if not present
os.makedirs(LOG_FOLDER, exist_ok=True)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TxtFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".txt"):
            filename = os.path.basename(event.src_path)
            logging.info(f"New file detected: {filename}")
            print(f"[+] New file detected: {filename}")
            with open(event.src_path, "r") as f:
                content = f.read()
            summary = summarize_text(content)

            summary_filename = filename.replace(".txt", "_summary.txt")
            output_path = os.path.join(OUTPUT_FOLDER, summary_filename)

            with open(output_path, "w") as out:
                out.write(summary)
            print(f"[✓] Summary saved to {output_path}")
            logging.info(f"Summary saved: {output_path}")

def start_watching():
    observer = Observer()
    event_handler = TxtFileHandler()
    observer.schedule(event_handler, INPUT_FOLDER, recursive=False)
    observer.start()
    print("[*] Watching folder for new .txt files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
