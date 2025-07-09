@echo off
REM Unified test runner for Djinn Constellation Hub
set LOGFILE=logs\test_output.log
if not exist logs mkdir logs

echo Running all Djinn Constellation Hub tests...
pytest tests\test_*.py --maxfail=3 --disable-warnings --tb=short > %LOGFILE% 2>&1

echo.
echo All tests complete. See %LOGFILE% for details.
pause
