from click.testing import CliRunner
from cli import watch_folder

def test_cli_runs():
    runner = CliRunner()
    result = runner.invoke(watch_folder, catch_exceptions=False)
    assert result.exit_code == 0 or result.exit_code == 1