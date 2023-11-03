@echo off

REM Clean old build directories
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist kwslogger.egg-info rmdir /s /q kwslogger.egg-info

REM Build the package
python setup.py sdist bdist_wheel
if errorlevel 1 (
    echo "Failed to build the package."
    REM Cleanup after error
    goto cleanup_and_exit
)

REM Upload to PyPI
pip install .
if errorlevel 1 (
    echo "Failed to install the new package."
    REM Cleanup after error
    goto cleanup_and_exit
)

REM Clean build directories after successful building and uploading
:cleanup
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist kwslogger.egg-info rmdir /s /q kwslogger.egg-info

echo "Successfully built and installed the package!"
exit /b

:cleanup_and_exit
REM Clean everything in case of error
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist kwslogger.egg-info rmdir /s /q kwslogger.egg-info
echo "Cleanup done due to an error."
exit /b