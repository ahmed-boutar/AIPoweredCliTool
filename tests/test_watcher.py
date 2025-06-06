import os
import shutil
from watcher import TxtFileHandler, OUTPUT_FOLDER, INPUT_FOLDER
from watchdog.events import FileCreatedEvent

def test_on_created_creates_summary(tmp_path):
    # Setup test dirs
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "summaries"
    input_dir.mkdir()
    output_dir.mkdir()
    
    # Patch global paths
    import watcher as watcher
    watcher.INPUT_FOLDER = str(input_dir)
    watcher.OUTPUT_FOLDER = str(output_dir)

    # Create dummy file
    test_file = input_dir / "test_input.txt"
    test_file.write_text("This is a test file for summarization.")

    # Trigger event
    handler = TxtFileHandler()
    event = FileCreatedEvent(str(test_file))
    handler.on_created(event)

    # Check output
    summary_file = output_dir / "test_input_summary.txt"
    assert summary_file.exists()
    assert summary_file.read_text().strip() != ""
