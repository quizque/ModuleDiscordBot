from os import listdir

###
### This file needs big time rework...
### Lots of hacks and I dont even know if there is a work around for it
###

# Loads all modules inside of the Modules folder
# returns -> Modules dictonary
def loadAll():
    
    # Get all the files in the 'Modules' file
    module_files = listdir("Modules")

    # Store the modules
    organzied_modules = {}
    
    # For all the found modules
    for module in module_files:

        # Attempt to load the module
        mod = load(module)

        # Skip if it doesn't exist
        if mod == None:
            continue

        # Merge with the modules dictonary
        merge(mod, organzied_modules)

    # Return the loaded, organized modules
    return organzied_modules
        

# Loads given module
# module_file -> name of module (string)
# returns -> module dictonary
def load(module_file):

    # Store the module
    organzied_module = {}

    # If the file is not a module, skip it.
    if module_file[-3:] != ".py":
        return None
    
    # Get the module name
    module_name = module_file[:-3]

    # Weird workout
    module_list = []

    # No idea if this is good, prob illegal
    exec(f"from Modules import {module_name}")
    exec(f"module_list.append({module_name})")

    # Store the module cause weird workaround
    module = module_list[0]

    # For all the events the module is in
    for events in module.EVENTS:
        
        # Add it to the dictonary if it already exists
        if events in organzied_module:
            organzied_module[events].append(module)
            continue

        # If it doesn't exist, create it and add it
        organzied_module[events] = []
        organzied_module[events].append(module)

    # Return the loaded module
    return organzied_module


# Merge a single loaded module dictonary into another module dictonary
# module -> module dictonary
# modules -> module dictonary
# returns -> module dictonary
def merge(module, modules):

    tmp = modules

    # For all fo the modules
    for name, event in module.items():

        # If it exists, append it
        if name in tmp:
            tmp[name].append(event[0])
            continue


        # If it doesn't, create it and append it
        tmp[name] = []
        tmp[name].append(event[0])
    
    return tmp