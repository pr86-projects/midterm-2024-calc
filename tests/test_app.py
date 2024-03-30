"""
This module contains tests for the calculator App.
"""
from app import App

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    #with pytest.raises(SystemExit) as e:
    #    app.start()
    app.start()
    captured = capfd.readouterr()
    #assert e.type == SystemExit
    assert "Exiting application..." in captured.out
