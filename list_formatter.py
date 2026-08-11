import pyperclip
import argparse


infile_path = "characters.txt"
outfile_path = "command.txt"
DISCORD_CHAR_LIMIT = 2000



parser = argparse.ArgumentParser(description="Format a list of items into a specific command format.")
parser.add_argument("--prefix", "-p", type=str, help="The prefix to use for the first item.")
parser.add_argument("--suffix", "-s", type=str, default="", help="The suffix to use at the end of the list.")
parser.add_argument("--limit", "-l", type=int, help="The maximum number of items to process.")
parser.add_argument("--separator", "-sep", type=str, default="$", help="The separator to use between items.")
parser.add_argument("--copy", "-c", action="store_true")

args = parser.parse_args()


with open(infile_path, "r", encoding="utf-8") as infile, \
    open(outfile_path, "w", encoding="utf-8") as outfile:
    
    for line in infile:
        if count >= args.limit:
            outfile.write(args.suffix)
            break

        line = line.rstrip()
        line = f"{args.prefix} {line}\n" if count == 0 else f"{args.separator}{line}\n"

        outfile.write(line)
        count += 1


print(f"""command written in "{outfile_path}" """)
if not parser.copy: return


# Read the output file and copy to clipboard
with open(outfile_path, "r", encoding="utf-8") as outfile:
    content = outfile.read()
    pyperclip.copy(content)

    copy_string = ""
    for line in outfile:
        line = line.rstrip()
        if len(copy_string + line) >= DISCORD_CHAR_LIMIT:
            pyperclip.copy(copy_string)
            pass if input("Partially copied to clipboard. Continue?") == 'y' else break
            copy_string = f"{args.prefix} {line.split(args.separator)}"
        else:
            copy_string += line

print("Command fully copied to clipboard!")
    
    
