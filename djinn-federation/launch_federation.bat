@echo off
echo 🜂 DJINN FEDERATION LAUNCHER
echo ================================
echo.
echo This launches all three systems as a federation:
echo - Djinn Council (Meta-Intelligence)
echo - IDHHC Companion (Operational HUD)  
echo - Djinn Companion (Dialogue Controller)
echo.
echo They will communicate via bridge protocol.
echo.

:menu
echo Choose your federation mode:
echo 1. Launch Federation Bridge (All systems)
echo 2. Launch Djinn Council only
echo 3. Launch IDHHC Companion only
echo 4. Launch Djinn Companion only
echo 5. Test Federation Communication
echo 6. Exit
echo.
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto federation
if "%choice%"=="2" goto council
if "%choice%"=="3" goto idhhc
if "%choice%"=="4" goto companion
if "%choice%"=="5" goto test
if "%choice%"=="6" goto exit
goto menu

:federation
echo.
echo 🜂 LAUNCHING DJINN FEDERATION...
echo Starting all three systems with bridge protocol...
echo.
echo Council: ollama run Yufok1/djinn-council
echo IDHHC: ollama run Yufok1/idhhc-companion  
echo Companion: ollama run Yufok1/djinn-companion
echo.
echo Use the bridge protocol for inter-system communication.
echo.
pause
goto menu

:council
echo.
echo 🜂 LAUNCHING DJINN COUNCIL...
ollama run Yufok1/djinn-council
goto menu

:idhhc
echo.
echo 🜂 LAUNCHING IDHHC COMPANION...
ollama run Yufok1/idhhc-companion
goto menu

:companion
echo.
echo 🜂 LAUNCHING DJINN COMPANION...
ollama run Yufok1/djinn-companion
goto menu

:test
echo.
echo 🜂 TESTING FEDERATION COMMUNICATION...
echo Testing bridge protocol between systems...
echo.
echo This would test the communication between:
echo - Council meta-judgment
echo - IDHHC operational functions
echo - Companion dialogue control
echo.
pause
goto menu

:exit
echo.
echo 🜂 Federation session ended.
pause 