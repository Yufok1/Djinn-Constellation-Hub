@echo off
REM === Minimal Installer and Test Runner (Windows) ===
setlocal EnableDelayedExpansion

REM Pre-flight checks
where ollama >nul 2>nul || (echo ERROR: ollama not found. Please install Ollama. & exit /b 1)
where curl >nul 2>nul || (echo ERROR: curl not found. Please install curl. & exit /b 1)

REM Run setup
echo Running federation setup...
call setup_djinn_federation.bat

REM Show log summary
if exist logs\setup.log (
    echo === Setup Log Summary ===
    type logs\setup.log
)

REM Run tests if present
if exist run_all_tests.bat (
    echo Running all federation tests...
    call run_all_tests.bat
) else (
    echo No test runner found (run_all_tests.bat missing).
)

echo Installer and test run complete.
endlocal
