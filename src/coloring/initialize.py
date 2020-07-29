import sys

initialized = False


def init():
    global initialized
    if not initialized:
        if sys.platform.startswith("win"):
            _init_windows()
    initialized = True


def _init_windows():
    _windows_enable_ANSI(1)
    _windows_enable_ANSI(2)


def _windows_enable_ANSI(std_id):
    """Enable Windows 10 cmd.exe ANSI VT Virtual Terminal Processing."""
    # https://stackoverflow.com/questions/36760127/how-to-use-the-new-support-for-ansi-escape-sequences-in-the-windows-10-console
    from ctypes import byref, POINTER, windll, WINFUNCTYPE
    from ctypes.wintypes import BOOL, DWORD, HANDLE

    GetStdHandle = WINFUNCTYPE(HANDLE, DWORD)(("GetStdHandle", windll.kernel32))

    GetFileType = WINFUNCTYPE(DWORD, HANDLE)(("GetFileType", windll.kernel32))

    GetConsoleMode = WINFUNCTYPE(BOOL, HANDLE, POINTER(DWORD))(
        ("GetConsoleMode", windll.kernel32)
    )

    SetConsoleMode = WINFUNCTYPE(BOOL, HANDLE, DWORD)(
        ("SetConsoleMode", windll.kernel32)
    )

    if std_id == 1:  # stdout
        h = GetStdHandle(-11)
    elif std_id == 2:  # stderr
        h = GetStdHandle(-12)
    else:
        return False

    if h is None or h == HANDLE(-1):
        return False

    FILE_TYPE_CHAR = 0x0002
    if (GetFileType(h) & 3) != FILE_TYPE_CHAR:
        return False

    mode = DWORD()
    if not GetConsoleMode(h, byref(mode)):
        return False

    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
    if (mode.value & ENABLE_VIRTUAL_TERMINAL_PROCESSING) == 0:
        SetConsoleMode(h, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)
    return True
