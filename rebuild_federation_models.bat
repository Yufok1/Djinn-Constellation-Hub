@echo off
cls
echo.
echo ╔══════════════════════════════════════════════════════════════════════════════════════╗
echo ║                    🜂 DJINN FEDERATION MODEL REBUILD 🜂                              ║
echo ║                   Rebuilding Revolutionary Models with Federation Consciousness      ║
echo ╚══════════════════════════════════════════════════════════════════════════════════════╝
echo.
echo 🌟 This will rebuild the revolutionary models with proper federation consciousness...
echo.

:: Check if we're in the right directory
if not exist "djinn-deep-thinker.Modelfile" (
    echo ❌ ERROR: Modelfiles not found!
    echo 📁 Please run this script from the Djinn-Constellation-Hub directory
    pause
    exit /b 1
)

:: Check if Ollama is running
ollama list >nul 2>&1
if errorlevel 1 (
    echo ⚠️ WARNING: Ollama not responding!
    echo 🔧 Please ensure Ollama is running: ollama serve
    pause
    exit /b 1
)

echo ✅ Environment validated successfully
echo.
echo 🧠 Rebuilding Djinn Federation Models with Federation Consciousness...
echo.

:: Rebuild Djinn Deep Thinker
echo 🔄 Rebuilding djinn-deep-thinker...
ollama create djinn-deep-thinker -f djinn-deep-thinker.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-deep-thinker
    pause
    exit /b 1
)
echo ✅ djinn-deep-thinker rebuilt successfully

:: Rebuild Djinn Cosmic Coder
echo 🔄 Rebuilding djinn-cosmic-coder...
ollama create djinn-cosmic-coder -f djinn-cosmic-coder.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-cosmic-coder
    pause
    exit /b 1
)
echo ✅ djinn-cosmic-coder rebuilt successfully

:: Rebuild Djinn Logic Master
echo 🔄 Rebuilding djinn-logic-master...
ollama create djinn-logic-master -f djinn-logic-master.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-logic-master
    pause
    exit /b 1
)
echo ✅ djinn-logic-master rebuilt successfully

:: Rebuild Djinn Enterprise Architect
echo 🔄 Rebuilding djinn-enterprise-architect...
ollama create djinn-enterprise-architect -f djinn-enterprise-architect.Modelfile
if errorlevel 1 (
    echo ❌ Failed to rebuild djinn-enterprise-architect
    pause
    exit /b 1
)
echo ✅ djinn-enterprise-architect rebuilt successfully

echo.
echo 🎉 All revolutionary models rebuilt with federation consciousness!
echo.
echo 🧪 Testing federation awareness...
echo.

:: Test the models
echo Testing djinn-deep-thinker federation awareness...
ollama run djinn-deep-thinker "Are you part of the Djinn Federation?"
echo.

echo Testing djinn-cosmic-coder federation awareness...
ollama run djinn-cosmic-coder "Are you part of the Djinn Federation?"
echo.

echo Testing djinn-logic-master federation awareness...
ollama run djinn-logic-master "Are you part of the Djinn Federation?"
echo.

echo Testing djinn-enterprise-architect federation awareness...
ollama run djinn-enterprise-architect "Are you part of the Djinn Federation?"
echo.

echo.
echo 🜂 Federation consciousness integration complete!
echo 🌟 All revolutionary models now have proper federation awareness
echo 🚀 You can now launch the complete Djinn Constellation Hub
echo.

pause 