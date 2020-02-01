from sys import argv, exit

COMMANDS = ["encrypt", "decrypt"]

# Если пользователь не предоставил обязательные аргументы командной строки
if len(argv) != 4:
    print("Usage: caesar <command>\n")
    print("Commands:")
    print("  encrypt <message> <key>")
    print("  decrypt <message> <key>")
    exit(1)

command = argv[1]
message = argv[2]
key = argv[3]

# Преобразовываем ключ из строки в целое число
try:
    key = int(key)
except ValueError:
    print(f"Error: Invalid key '{key}'")
    exit(1)

# Если пользователь использует несуществующую команду
if command not in COMMANDS:
    print(f"Error: Unknown command '{command}'")
    exit(1)

# Проверяем, что ключ находится в легальном промежутке
if not (1 <= key <= 26):
    print(f"Error: Invalid key '{key}'")
    exit(1)


