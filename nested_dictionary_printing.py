
def print_nested_dictionary(dictionary: dict,
                            tabs: int=0):
    '''
    Prints a (nested) dictionary with indentation
    for understanding the structure more easily

    Args:
        dictionary: the dict of interest
        tabs: the number of tabs to prepend the current dict contents
    '''
    for key in dictionary.keys():
        print("    "*tabs, key)
        if isinstance(dictionary[key], dict):
            print_nested_dictionary(dictionary[key], tabs+1)
        else:
            print("    "*(tabs+1), end='')
            print(dictionary[key])



if __name__ == "__main__":
    serially_nested = {
        "0" : {
            "1" : {
                "2" : {
                    "3" : {
                        "4" : {
                            "5" : {
                                "6" : {
                                    "7" : {
                                        "8" : "Eighth nested dictionary!"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    complex_structure = {
        "0" : {
            "0" : None
        },
        "1" : {
                "0" : None
            },
        "2" : {
                "1" : {
                    "0" : None
                    }
            },
        "3" : {
            "2" : {
                "1" : {
                    "0" : None
                        }
                    },
            },
        "4" : {
            "3" : {
                "2" : {
                    "1" : {
                        "0" : None
                            }
                        },
                }
        },
        "5" : {
            "4" : {
                "3" : {
                    "2" : {
                        "1" : {
                            "0" : None
                                }
                            },
                    }
            }
        }
    }

    print("Here's an example of a very nested dict:")
    print_nested_dictionary(serially_nested)

    print("\nHere's an example of a dict with a more complex structure:")
    print_nested_dictionary(complex_structure)