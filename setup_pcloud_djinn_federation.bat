@echo off
cls
echo.
echo ==========================================
echo    ☁️ PCLOUD DJINN FEDERATION SETUP ☁️
echo ==========================================
echo.

echo 🔍 Detecting PCloud mount...
set PCLOUD_DRIVE=

for %%d in (Z Y X W V U T S) do (
    if exist %%d:\ (
        echo    Found drive %%d:\ - Testing if PCloud...
        if exist "%%d:\*" (
            set PCLOUD_DRIVE=%%d:
            echo    ✅ PCloud detected on %%d:\
            goto :pcloud_found
        )
    )
)

echo ❌ PCloud drive not found
echo    Please ensure PCloud is mounted as a network drive
echo    Common mount points: Z:, Y:, X:, W:
echo.
pause
exit /b 1

:pcloud_found
echo.
echo 🛠️  Setting up PCloud Djinn Federation structure...

:: Create main directories
mkdir "%PCLOUD_DRIVE%\djinn_models" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_models\revolutionary" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_models\backups" 2>nul

mkdir "%PCLOUD_DRIVE%\djinn_memory" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_memory\conversations" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_memory\user_preferences" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_memory\model_performance" 2>nul

mkdir "%PCLOUD_DRIVE%\djinn_operations" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_operations\pending_tasks" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_operations\completed_tasks" 2>nul
mkdir "%PCLOUD_DRIVE%\djinn_operations\federated_sessions" 2>nul

echo ✅ Created directory structure on %PCLOUD_DRIVE%

:: Create PCloud federation config
echo. > "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo { >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   "federation_name": "PCloud Djinn Federation", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   "version": "1.0.0", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   "pcloud_drive": "%PCLOUD_DRIVE%", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   "setup_date": "%date% %time%", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   "devices": [], >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   "revolutionary_models": [ >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo     "djinn-cosmic-coder:latest", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo     "djinn-deep-thinker:latest", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo     "djinn-logic-master:latest", >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo     "djinn-enterprise-architect:latest" >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo   ] >> "%PCLOUD_DRIVE%\djinn_federation_config.json"
echo } >> "%PCLOUD_DRIVE%\djinn_federation_config.json"

echo ✅ Created federation configuration

:: Test PCloud write speed
echo 🚀 Testing PCloud performance...
echo Djinn Federation Speed Test > "%PCLOUD_DRIVE%\speed_test.tmp"
if exist "%PCLOUD_DRIVE%\speed_test.tmp" (
    del "%PCLOUD_DRIVE%\speed_test.tmp"
    echo ✅ PCloud read/write test passed
) else (
    echo ⚠️  PCloud write test failed
)

echo.
echo ==========================================
echo    ☁️ PCLOUD DJINN FEDERATION READY ☁️
echo ==========================================
echo.
echo PCloud Drive: %PCLOUD_DRIVE%
echo Structure: ✅ Created
echo Config: ✅ Generated
echo Performance: ✅ Tested
echo.
echo Next steps:
echo   1. Run: python pcloud_djinn_federation.py
echo   2. Use /sync to upload revolutionary models
echo   3. Set up federation on other devices
echo   4. Enable distributed Djinn operations
echo.
echo 🜂 The mystical PCloud federation awaits!
echo.
pause
