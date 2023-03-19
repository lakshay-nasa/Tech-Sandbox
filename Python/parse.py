import os

def parse_mode_file(mode_path: str) -> list[list[str]]:
    """
    Args:
        mode_path (str)

    Returns:
        List[List[str]]
    """
    with open(os.path.join(mode_path)) as mode_file:
        mode_str = mode_file.read().strip()
    if mode_str:
        commands = []
        for cmd in mode_str.strip().split('|'):
            # TODO: we should make language pairs install
            # modes.xml instead; this is brittle (what if a path
            # has | or ' in it?)
            cmd = cmd.replace('$2', '').replace('$1', '-g')
            commands.append([c.strip("'") for c in cmd.split()])
        return commands
    else:
        print(mode_path)



mode_path = os.path.join('/home', 'user main', 'modes', 'mode2.txt')
mode_commands = parse_mode_file(mode_path)

# Print out each command and its arguments
for cmd in mode_commands:
    print(cmd)