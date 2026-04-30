import pyperclip
import argparse


infile_path = "characters.txt"
outfile_path = "command.txt"



parser = argparse.ArgumentParser(description="Format a list of items into a specific command format.")
parser.add_argument("--prefix", "-p", type=str, help="The prefix to use for the first item.")
parser.add_argument("--suffix", "-s", type=str, default="", help="The suffix to use at the end of the list.")
parser.add_argument("--limit", "-l", type=int, help="The maximum number of items to process.")
parser.add_argument("--separator", "-sep", type=str, default="$", help="The separator to use between items.")
args = parser.parse_args()


with open(infile_path, "r", encoding="utf-8") as infile, \
    open(outfile_path, "w", encoding="utf-8") as outfile:
    
    count = 0
    for line in infile:
        if count >= args.limit:
            outfile.write(args.suffix)
            break

        line = line.rstrip()
        
        if count == 0:
            outfile.write(f"{args.prefix} {line.rstrip()}\n")
        else:
            outfile.write(f"{args.separator}{line.rstrip()}\n")
        count += 1

# Read the output file and copy to clipboard
with open(outfile_path, "r", encoding="utf-8") as outfile:
    content = outfile.read()
    pyperclip.copy(content)

print(f"""command written in "{outfile_path}" """)
print("Contents copied to clipboard!")
    
    
