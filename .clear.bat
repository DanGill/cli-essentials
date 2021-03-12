@echo off
echo Removing /dist, /scprint.egg-info, /build
rd /s /q "dist"
rd /s /q "scprint.egg-info"
rd /s /q "build"
echo Build Removed...
pause > nul