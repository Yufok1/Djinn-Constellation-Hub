@echo off
echo 🜂 Pushing Djinn Constellation Federation Models to Ollama Hub 🜂
echo ============================================================
echo.

echo 📋 Federation Models to Push:
echo - djinn-cosmic-coder
echo - djinn-logic-master
echo - djinn-deep-thinker
echo - djinn-enterprise-architect
echo - constellation-lite
echo - constellation-core
echo - constellation-max
echo - companion
echo - idhhc
echo - council
echo.

echo 🚀 Starting Federation Push...
echo.

set /a success_count=0
set /a total_count=0

:: Push djinn-cosmic-coder
echo 🌟 Pushing djinn-cosmic-coder...
ollama cp Yufok1/djinn-federation:djinn-cosmic-coder Yufok1/djinn-federation:cosmic-coder
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

:: Push djinn-logic-master
echo 🌟 Pushing djinn-logic-master...
ollama cp Yufok1/djinn-federation:djinn-logic-master Yufok1/djinn-federation:logic-master
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

:: Push djinn-deep-thinker
echo 🌟 Pushing djinn-deep-thinker...
ollama cp Yufok1/djinn-federation:djinn-deep-thinker Yufok1/djinn-federation:deep-thinker
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

:: Push djinn-enterprise-architect
echo 🌟 Pushing djinn-enterprise-architect...
ollama cp Yufok1/djinn-federation:djinn-enterprise-architect Yufok1/djinn-federation:enterprise-architect
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

:: Push constellation-lite
echo 🌟 Pushing constellation-lite...
ollama cp Yufok1/djinn-federation:constellation-lite Yufok1/djinn-federation:lite
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

:: Push constellation-core
echo 🌟 Pushing constellation-core...
ollama cp Yufok1/djinn-federation:constellation-core Yufok1/djinn-federation:core
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

:: Push constellation-max
echo 🌟 Pushing constellation-max...
ollama cp Yufok1/djinn-federation:constellation-max Yufok1/djinn-federation:max
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

:: Push companion
echo 🌟 Pushing companion...
ollama cp Yufok1/djinn-federation:companion Yufok1/djinn-federation:companion
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

:: Push idhhc
echo 🌟 Pushing idhhc...
ollama cp Yufok1/djinn-federation:idhhc Yufok1/djinn-federation:idhhc
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

:: Push council
echo 🌟 Pushing council...
ollama cp Yufok1/djinn-federation:council Yufok1/djinn-federation:council
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
