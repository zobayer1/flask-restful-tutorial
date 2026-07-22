# -*- coding: utf-8 -*-
from myapi import manage


def test_command_env_exits_with_success(runner):
    """Test fails if `myapi env` does not execute with success status"""
    result = runner.invoke(manage.cli, ["env"])
    env_vars = ["FLASK_ENV", "FLASK_SECRET", "LOGGING_ROOT", "LOGGING_CONFIG"]
    for var in env_vars:
        assert var in result.output
    assert result.exit_code == 0
