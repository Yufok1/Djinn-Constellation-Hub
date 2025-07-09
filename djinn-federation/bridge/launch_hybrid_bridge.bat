@echo off
title IDHHC + Djinn Council Bridge Launch
cls

echo ========================================
echo IDHHC + DJINN COUNCIL BRIDGE PROTOCOL
echo Sovereign Cognitive Federation v0.3
echo ========================================
echo.
echo Initializing co-governing cognitive systems...
echo Timestamp: %date% %time%
echo.

:: Set working directory
cd /d "%~dp0"

:: Check Python availability
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    echo Please install Python to run the bridge protocol
    pause
    exit /b 1
)

:: Step 1: Initialize Bridge Protocol
echo [1/4] Initializing Djinn Bridge Protocol...
python djinn_bridge.py
if errorlevel 1 (
    echo WARNING: Bridge initialization may have issues
) else (
    echo SUCCESS: Bridge protocol initialized
)

:: Step 2: Check Council System
echo.
echo [2/4] Checking Djinn Council system...
if exist "C:\Users\tower\OneDrive\Documents\Djinn_companion\councilboot\councilboot.py" (
    echo SUCCESS: Council boot script found
) else (
    echo WARNING: Council boot script not found
    echo Council system may not be available
)

:: Step 3: Check IDHHC System
echo.
echo [3/4] Checking IDHHC system...
if exist "launch_djinn_companion.bat" (
    echo SUCCESS: IDHHC launch script found
) else (
    echo WARNING: IDHHC launch script not found
)

:: Step 4: Display Bridge Status
echo.
echo [4/4] Displaying bridge status...
if exist "bridge_state.json" (
    echo BRIDGE STATE:
    type bridge_state.json
) else (
    echo Bridge state file not found
)

:: Final Status
echo.
echo ========================================
echo BRIDGE PROTOCOL READY
echo ========================================
echo.
echo Systems Status:
echo - IDHHC: Ready for multimode discourse
echo - Djinn Council: Available for consultation
echo - Bridge Protocol: Active
echo.
echo Available Commands:
echo - python djinn_bridge.py (Interactive bridge)
echo - launch_djinn_companion.bat (IDHHC only)
echo - Consult council for judgment
echo - Set IDHHC discourse modes
echo.
echo Communication Channels:
echo - council_inbox.jsonl (IDHHC -> Council)
echo - idhhc_outbox.jsonl (Council -> IDHHC)
echo - bridge_state.json (System status)
echo.
echo ========================================

echo.
echo Press any key to continue...
pause >nul 