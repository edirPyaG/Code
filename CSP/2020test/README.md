# C++ with MSVC (cl) on Windows (ARM64)

Clicking "Run Code" (Code Runner) will:
- Initialize MSVC environment via `vcvarsall.bat arm64`
- Compile the active `.cpp` file with `cl`
- Run the produced `.exe`

If your Visual Studio path or target architecture differs, edit `.vscode/settings.json`:
- Change `C:\\VSstudio\\Community\\VC\\Auxiliary\\Build\\vcvarsall.bat` to your actual `vcvarsall.bat` path.
- Change `arm64` to `x64` (or `x86`) as needed.

Troubleshooting:
- If headers like `float.h` are missing, it means the environment wasn't initialized; ensure the `vcvarsall.bat` path is correct.
- If you prefer tasks, press `Ctrl+Shift+B` to run the preconfigured build task.