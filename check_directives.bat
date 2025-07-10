@echo off
echo.
echo 🌉 CHECKING CONSTELLATION DIRECTIVES FOR VOID
echo ================================================
echo.

python -c "from void_constellation_bridge import VOIDConstellationBridge; bridge = VOIDConstellationBridge(); bridge.display_pending_directives()"

echo.
echo ================================================
echo 💡 To process directives: python void_constellation_bridge.py
echo 🔗 To return to constellation: launch_constellation_complete.bat
echo.
pause