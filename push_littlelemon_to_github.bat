@echo off
setlocal
title Push Little Lemon Web Application API to GitHub

echo =====================================================
echo  Little Lemon Web Application API - GitHub Push
echo =====================================================
echo.
echo This script must be placed in the ROOT of your extracted
echo Django project, beside manage.py and README.md.
echo.
pause

where git >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or is not available in PATH.
    echo Install Git for Windows, reopen this window, and try again.
    pause
    exit /b 1
)

if not exist "manage.py" (
    echo ERROR: manage.py was not found in this folder.
    echo Move this BAT file into the extracted project root folder.
    pause
    exit /b 1
)

git init
if errorlevel 1 goto :failed

git branch -M main
if errorlevel 1 goto :failed

git remote get-url origin >nul 2>&1
if errorlevel 1 (
    git remote add origin https://github.com/PranavYehale/-Lemon-Web-Application-API.git
) else (
    git remote set-url origin https://github.com/PranavYehale/-Lemon-Web-Application-API.git
)
if errorlevel 1 goto :failed

echo.
echo Staging project files...
git add .
if errorlevel 1 goto :failed

echo.
echo Creating commit...
git diff --cached --quiet
if errorlevel 1 (
    git commit -m "Add Little Lemon Web Application API"
    if errorlevel 1 goto :failed
) else (
    echo No staged changes to commit. Continuing to push...
)

echo.
echo Pushing to GitHub...
git push -u origin main
if errorlevel 1 (
    echo.
    echo Push failed. Common causes:
    echo  - Sign in to GitHub when prompted by Git Credential Manager.
    echo  - The GitHub repository already has commits that are not in this folder.
    echo  - You do not have write access to the repository.
    echo.
    echo If the remote repository already has a README or other commits,
    echo do not force-push blindly. Run:
    echo   git pull origin main --allow-unrelated-histories
    echo Resolve any conflicts, commit, then run:
    echo   git push -u origin main
    pause
    exit /b 1
)

echo.
echo SUCCESS: Your project was pushed to:
echo https://github.com/PranavYehale/-Lemon-Web-Application-API
echo.
pause
exit /b 0

:failed
echo.
echo ERROR: A Git command failed. Read the message above, fix the issue,
echo then run this BAT file again.
pause
exit /b 1
