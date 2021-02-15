

# Load config with given filename
# fileName -> name of file (string)
# returns -> config dictonary
def load(fileName):

    # Create the config dictonary
    config = {}

    # Incase the file doesn't exist
    try:

        # Open the file
        with open(fileName) as f:

            # Read each line in the file
            for line in f.readlines():
                
                # Remove garbage from line
                f_line = line.strip()

                # If the line is empty or has comment, skip the line
                if len(f_line) == 0 or f_line[0] == "#":
                    continue
                
                # Split the line using '=' as a delimiter
                varible = f_line.split("=")

                # Store the varible into given the config
                config[varible[0].strip()] = varible[1].strip()

    # If we run into an error during this, return nothing
    except:
        return None

    # Return the config once we are done everything
    return config

# Check a given configuarations varibles
# config -> config dictonary
# returns -> true or false if its valid
def check(config):

    # Attempts to check if the varibles exist
    # Bit hacky, not sure if there is a better way
    try:

        config["token"]
        config["verbose"]

        return True
    
    # If it errors, then one of them doesn't exist
    except:
        return False

# Writes the example config if it doesn't exist
# fileName -> name of file (string)
def writeExample(fileName):

    # Open the file for writing (overwrite if it exists)
    with open(fileName, "w") as f:
        f.write("# Discord bot token goes here\ntoken=\n\n# Verbose level goes here\n# Choices are LOW=0, MED=1, HIGH=2\nverbose=2") 