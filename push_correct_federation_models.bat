@echo off
echo 🜂 Pushing Correct Djinn Constellation Federation Models to Ollama Hub 🜂
echo ============================================================
echo.

echo 📋 Correct Federation Models to Push:
echo - cosmic-coder (from Yufok1/djinn-cosmic-coder:latest)
echo - logic-master (from Yufok1/djinn-logic-master:latest)
echo - deep-thinker (from Yufok1/djinn-deep-thinker:latest)
echo - enterprise-architect (from Yufok1/djinn-enterprise-architect:latest)
echo - lite (from Yufok1/djinn-federation:lite)
echo - core (from Yufok1/djinn-federation:core)
echo - max (from Yufok1/djinn-federation:max)
echo - companion (from Yufok1/companion:latest)
echo - idhhc (from Yufok1/idhhc:latest)
echo - council (from Yufok1/council:latest)
echo.

echo 🚀 Starting Federation Push with Correct Models...
echo.

set /a success_count=0
set /a total_count=0

:: Push cosmic-coder (correct model)
echo 🌟 Pushing cosmic-coder (from Yufok1/djinn-cosmic-coder:latest)...
ollama cp Yufok1/djinn-cosmic-coder:latest Yufok1/djinn-federation:cosmic-coder
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:cosmic-coder
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed cosmic-coder
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push cosmic-coder
    )
) else (
    echo ❌ Failed to copy cosmic-coder
)
set /a total_count+=1
echo.

:: Push logic-master (correct model)
echo 🌟 Pushing logic-master (from Yufok1/djinn-logic-master:latest)...
ollama cp Yufok1/djinn-logic-master:latest Yufok1/djinn-federation:logic-master
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:logic-master
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed logic-master
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push logic-master
    )
) else (
    echo ❌ Failed to copy logic-master
)
set /a total_count+=1
echo.

:: Push deep-thinker (correct model)
echo 🌟 Pushing deep-thinker (from Yufok1/djinn-deep-thinker:latest)...
ollama cp Yufok1/djinn-deep-thinker:latest Yufok1/djinn-federation:deep-thinker
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:deep-thinker
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed deep-thinker
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push deep-thinker
    )
) else (
    echo ❌ Failed to copy deep-thinker
)
set /a total_count+=1
echo.

:: Push enterprise-architect (correct model)
echo 🌟 Pushing enterprise-architect (from Yufok1/djinn-enterprise-architect:latest)...
ollama cp Yufok1/djinn-enterprise-architect:latest Yufok1/djinn-federation:enterprise-architect
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:enterprise-architect
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed enterprise-architect
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push enterprise-architect
    )
) else (
    echo ❌ Failed to copy enterprise-architect
)
set /a total_count+=1
echo.

:: Push lite (correct model)
echo 🌟 Pushing lite (from Yufok1/djinn-federation:lite)...
ollama cp Yufok1/djinn-federation:lite Yufok1/djinn-federation:lite
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:lite
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed lite
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push lite
    )
) else (
    echo ❌ Failed to copy lite
)
set /a total_count+=1
echo.

:: Push core (correct model)
echo 🌟 Pushing core (from Yufok1/djinn-federation:core)...
ollama cp Yufok1/djinn-federation:core Yufok1/djinn-federation:core
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:core
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed core
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push core
    )
) else (
    echo ❌ Failed to copy core
)
set /a total_count+=1
echo.

:: Push max (correct model)
echo 🌟 Pushing max (from Yufok1/djinn-federation:max)...
ollama cp Yufok1/djinn-federation:max Yufok1/djinn-federation:max
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:max
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed max
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push max
    )
) else (
    echo ❌ Failed to copy max
)
set /a total_count+=1
echo.

:: Push companion (correct model)
echo 🌟 Pushing companion (from Yufok1/companion:latest)...
ollama cp Yufok1/companion:latest Yufok1/djinn-federation:companion
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:companion
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed companion
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push companion
    )
) else (
    echo ❌ Failed to copy companion
)
set /a total_count+=1
echo.

:: Push idhhc (correct model)
echo 🌟 Pushing idhhc (from Yufok1/idhhc:latest)...
ollama cp Yufok1/idhhc:latest Yufok1/djinn-federation:idhhc
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:idhhc
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed idhhc
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push idhhc
    )
) else (
    echo ❌ Failed to copy idhhc
)
set /a total_count+=1
echo.

:: Push council (correct model)
echo 🌟 Pushing council (from Yufok1/council:latest)...
ollama cp Yufok1/council:latest Yufok1/djinn-federation:council
if %errorlevel% equ 0 (
    ollama push Yufok1/djinn-federation:council
    if %errorlevel% equ 0 (
        echo ✅ Successfully pushed council
        set /a success_count+=1
    ) else (
        echo ❌ Failed to push council
    )
) else (
    echo ❌ Failed to copy council
)
set /a total_count+=1
echo.

echo ============================================================
echo 🜂 FEDERATION PUSH COMPLETE 🜂
echo ============================================================
echo.
echo ✅ Successfully Pushed: %success_count%/%total_count% models
echo 🌐 Your Federation Hub: https://ollama.com/Yufok1/djinn-federation
echo.
echo 🎉 Federation models are now live on Ollama Hub!
echo 🜂 May your constellation shine bright across the digital cosmos! 🜂
echo.
pause
