@echo off
setlocal EnableDelayedExpansion

REM === Auto-navigation for GitHub zip extraction ===
REM If this script is being run from a wrapper folder, cd into the correct folder and re-run
for %%F in (Djinn-Constellation-Hub-main Djinn-Constellation-Hub Djinn-Constellation-Hub-v2.0.0) do (
    if exist "%%F\setup_djinn_federation.bat" (
        cd "%%F"
        call setup_djinn_federation.bat
        exit /b
    )
)
REM Try any single subdirectory with the setup script
for /d %%D in (*) do (
    if exist "%%D\setup_djinn_federation.bat" (
        cd "%%D"
        call setup_djinn_federation.bat
        exit /b
    )
)
REM If not found, continue as normal (if we're in the right folder)

REM === RAP-4+ Config-Driven Federation Setup ===
REM Reads federation_setup.cfg and automates onboarding for all models/agents

REM Log file
set LOGFILE=logs\setup.log
if not exist logs mkdir logs
if exist %LOGFILE% del %LOGFILE%

REM Status tracking
set SUMMARY=

REM Read config and process each entry
for /f "usebackq tokens=1-5 delims=, " %%A in ("federation_setup.cfg") do (
    set NAME=%%A
    set METHOD=%%B
    set URL=%%C
    set HASH=%%D
    set SCRIPT=%%E
    set STATUS=NotChecked
    echo === Processing !NAME! with method !METHOD! >> %LOGFILE%
    if /i "!METHOD!"=="ollama" (
        echo Checking for !NAME!:latest ...
        ollama list | findstr "!NAME!"
        if !errorlevel! neq 0 (
            echo Not present. Pulling from Ollama... >> %LOGFILE%
            ollama pull !NAME!:latest >> %LOGFILE% 2>&1
            if !errorlevel! neq 0 (
                echo ❌ Failed to pull !NAME! from Ollama. >> %LOGFILE%
                set STATUS=Error
            ) else (
                echo ✅ Pulled !NAME!. >> %LOGFILE%
                set STATUS=Pulled
            )
        ) else (
            echo ✅ !NAME! is present. >> %LOGFILE%
            set STATUS=Present
        )
    ) else if /i "!METHOD!"=="batch" (
        echo Checking for !NAME!:latest ...
        ollama list | findstr "!NAME!"
        if !errorlevel! neq 0 (
            echo Not present. Importing via !SCRIPT!... >> %LOGFILE%
            if exist !SCRIPT! (
                call !SCRIPT! !NAME! >> %LOGFILE% 2>&1
                if !errorlevel! neq 0 (
                    echo ❌ Failed to import !NAME! with !SCRIPT!. >> %LOGFILE%
                    set STATUS=Error
                ) else (
                    echo ✅ Imported !NAME! via !SCRIPT!. >> %LOGFILE%
                    set STATUS=Imported
                )
            ) else (
                echo ❌ Script !SCRIPT! not found for !NAME!. >> %LOGFILE%
                set STATUS=Error
            )
        ) else (
            echo ✅ !NAME! is present. >> %LOGFILE%
            set STATUS=Present
        )
    ) else if /i "!METHOD!"=="cloud" (
        echo Checking for !NAME! file presence ...
        if exist !NAME!.bin (
            echo ✅ !NAME!.bin is present. >> %LOGFILE%
            set STATUS=Present
        ) else (
            echo Not present. Downloading from !URL!... >> %LOGFILE%
            curl -L --retry 3 --retry-delay 5 -o !NAME!.bin !URL! >> %LOGFILE% 2>&1
            if !errorlevel! neq 0 (
                echo ❌ Failed to download !NAME! from cloud. >> %LOGFILE%
                set STATUS=Error
            ) else (
                echo ✅ Downloaded !NAME! from cloud. >> %LOGFILE%
                set STATUS=Downloaded
            )
        )
    ) else if /i "!METHOD!"=="file" (
        echo Checking for file !URL! ...
        if exist !URL! (
            echo ✅ File !URL! is present. >> %LOGFILE%
            set STATUS=Present
            REM Attempt auto-import to Ollama if a script is provided
            if not "!SCRIPT!"=="" if exist !SCRIPT! (
                echo Attempting to auto-import !URL! using !SCRIPT!... >> %LOGFILE%
                call !SCRIPT! !NAME! !URL! >> %LOGFILE% 2>&1
                if !errorlevel! neq 0 (
                    echo ⚠️ Auto-import of !NAME! from !URL! failed with !SCRIPT!. >> %LOGFILE%
                ) else (
                    echo ✅ Auto-imported !NAME! from !URL! using !SCRIPT!. >> %LOGFILE%
                )
            )
        ) else (
            REM === If .bin is missing, check for .Modelfile ===
            set MODELFILENAME=!NAME!.Modelfile
            set MODELFILEREL=.
            set MODELFILEROOT=!MODELFILENAME!
            set MODELFILEMODS=djinn-federation\modelfiles\!MODELFILENAME!
            set MODELFILENAMEFOUND=
            if exist !MODELFILEROOT! set MODELFILENAMEFOUND=!MODELFILEROOT!
            if exist !MODELFILEMODS! set MODELFILENAMEFOUND=!MODELFILEMODS!
            REM Warn if both exist
            if exist !MODELFILEROOT! if exist !MODELFILEMODS! echo ⚠️ Multiple .Modelfile files found for !NAME!. Using !MODELFILENAMEFOUND!. >> %LOGFILE%
            if defined MODELFILENAMEFOUND (
                echo 📝 Found .Modelfile for !NAME!: !MODELFILENAMEFOUND! >> %LOGFILE%
                echo Attempting to create Ollama model !NAME! from !MODELFILENAMEFOUND!... >> %LOGFILE%
                ollama create !NAME! -f !MODELFILENAMEFOUND! >> %LOGFILE% 2>&1
                if !errorlevel! neq 0 (
                    echo ❌ Failed to create !NAME! from .Modelfile. >> %LOGFILE%
                    set STATUS=Error
                ) else (
                    echo ✅ Created !NAME! from .Modelfile. >> %LOGFILE%
                    set STATUS=Imported
                )
            ) else (
                echo ❌ File !URL! and .Modelfile for !NAME! are both missing. >> %LOGFILE%
                set STATUS=Error
            )
        )
    )
    set SUMMARY=!SUMMARY!!NAME!: !STATUS!\n
)

REM === Summary Table ===
echo.
echo ================= Federation Model/Agent Setup Summary ================
echo !SUMMARY!
echo =======================================================================

echo 🜂 DJINN FEDERATION RAP-4+ AUTOMATED SETUP COMPLETE! 🜂
endlocal
echo.
echo 🚀 STEP 1: Building DJINN-ified Constellation Coordinators...
call build_constellation_coordinators.bat
if %errorlevel% neq 0 (
    echo ❌ Failed to build constellation coordinators
    pause
    exit /b 1
)

echo.
echo 🚀 STEP 2: Checking for base models...
echo.
echo 📋 Required base models:
echo   - tinydolphin:latest
echo   - dolphin-phi:latest  
echo   - phi3:latest
echo.

ollama list | findstr "tinydolphin\|dolphin-phi\|phi3"
if %errorlevel% neq 0 (
    echo ⚠️  Some base models may not be available
    echo 💡 Run 'ollama pull tinydolphin:latest' if needed
    echo 💡 Run 'ollama pull dolphin-phi:latest' if needed
    echo 💡 Run 'ollama pull phi3:latest' if needed
)

echo.
echo 🚀 STEP 3: Checking specialized DJINN agents and revolutionary models...
echo.
echo 📋 Required specialized agents:
echo   - djinn-council-enhanced-v2:latest
echo   - idhhc-companion:latest
echo   - djinn-companion:latest
echo   - djinn-cosmic-coder:latest
echo   - djinn-deep-thinker:latest
echo   - djinn-logic-master:latest
echo   - djinn-enterprise-architect:latest

echo.
echo Checking specialized agents:
for %%A in (djinn-council-enhanced-v2 idhhc-companion djinn-companion djinn-cosmic-coder djinn-deep-thinker djinn-logic-master djinn-enterprise-architect) do (
    echo Checking for %%A:latest ...
    ollama list | findstr "%%A"
    if %errorlevel% neq 0 (
        echo ⚠️  %%A is NOT present! Please ensure this model/agent is available before federation launch.
        echo     - For advanced AIs, see:
        echo         create_djinn_revolutionary_models.bat
        echo         shadow_automation.bat
        echo         import_shadow_models.bat
        echo     - Or refer to CLOUD_SETUP_GUIDE.md for manual steps.
    ) else (
        echo %%A is present.
    )
)

echo.
echo 🜂 DJINN FEDERATION SETUP COMPLETE! 🜂
echo.
echo 📋 Available DJINN-ified Constellation Coordinators and Models:
echo   ⚡ tinydolphin-constellation (636MB) - Ultra-Fast Task Coordinator
echo   🐬 dolphin-phi-constellation (1.6GB) - Primary Constellation Coordinator  
echo   🧠 phi3-constellation (2.2GB) - Complex Task Coordinator
echo   🌟 djinn-cosmic-coder (65GB) - MoE Multimodal Sorcery
echo   🧠 djinn-deep-thinker (32GB) - Ancient Wisdom
echo   ⚡ djinn-logic-master (11GB) - Sovereign Reasoning
echo   💻 djinn-enterprise-architect (22GB) - Corporate Mysticism
echo.
echo 🎯 To launch the Hierarchical Constellation Hub:
echo   cd djinn-federation\launcher
echo   python constellation_hub.py
echo.
echo 🜂 The mystical DJINN Federation is ready to serve! 🜂
echo.
pause