@echo off
title FilesCleaner Make By carfty.



color a
echo Make By carfty
echo Press the enter key to start working.
pause

color c
rd /s /q C:\Windows\temp
del /s /f /q c:\windows\temp\*.*
rd /s /q c:\windows\temp
md c:\windows\temp
del /s /f /q C:\WINDOWS\Prefetch
del /s /f /q %temp%\*.*
rd /s /q %temp%
md %temp%

color a

echo FilesCleaner successful delete temp
echo FilesCleaner successful temp
echo FilesCleaner successful delete Prefetch
echo FilesCleaner successful Prefetch
echo FilesCleaner successful delete temps
echo FilesCleaner successful temps

powershell -Command "& {Add-Type -AssemblyName System.Windows.Forms; [System.Windows.Forms.MessageBox]::Show('Files Cleaner successful', 'Files Cleaner successful Make By carfty.', 'OK', [System.Windows.Forms.MessageBoxIcon]::Information);}"

exit


