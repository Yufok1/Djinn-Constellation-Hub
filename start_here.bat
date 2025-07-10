@echo off
setlocal

REM === Universal DJINN Setup Launcher ===
REM This script finds and runs the real setup_djinn_federation.bat, even if nested due to GitHub zip extraction.

REM Try current folder first
if exist "setup_djinn_federation.bat" (
    call setup_djinn_federation.bat
    goto :end
)

REM Try common nested folder names (GitHub zip extraction)
for %%F in (Djinn-Constellation-Hub-main Djinn-Constellation-Hub Djinn-Constellation-Hub-v2.0.0) do (
    if exist "%%F\setup_djinn_federation.bat" (
        cd "%%F"
        call setup_djinn_federation.bat
        goto :end
    )
)

REM Try any single subdirectory with the setup script
for /d %%D in (*) do (
    if exist "%%D\setup_djinn_federation.bat" (
        cd "%%D"
        call setup_djinn_federation.bat
        goto :end
    )
)

REM If not found, fail gracefully
:fail
    echo ❌ Could not find setup_djinn_federation.bat in this folder or any subdirectory.
    echo Please check your extraction or download.
    pause
    goto :end

:end
endlocal
