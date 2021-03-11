#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# nickculbert, 2021-Mar-10, added main body
#------------------------------------------#

# -- DATA -- #

import pickle
strFileName = 'CDInventory.txt'
lst_Inventory = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    
    methods:
        None.
        
    """
    
    # -- Constructor -- #
    
    def __init__(self, cd_id, cd_title, cd_artist):
        
        # -- Attributes -- #
        
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    # -- Properties -- #
    
    # Getters
    @property
    def cd_id(self):
        return self.__cd_id
    
    @property
    def cd_title(self):
        return self.__cd_title
    
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    # Setters
    @cd_id.setter
    def cd_id(self, value):
        self.__cd_id = value
    
    @cd_title.setter
    def cd_title(self, value):
        self.__cd_title = value
        
    @cd_artist.setter
    def cd_artist(self, value):
        self.__cd_artist = value
    

# -- PROCESSING -- #

class FileIO:
    """Processes data to and from file:

    properties:
        None.
        
    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    # -- Methods -- #
    
    @staticmethod
    def load_inventory(file_name, lst_Inventory):
        """Ingests data from file to a list of CD objects

        Reads the pickled data from file identified by file_name and assigns
        that data to the field lst_Inventory.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            lst_Inventory (list of CDs): holds the inventory during runtime
        """
        lst_Inventory.clear()
        try:
            with open(file_name, 'ab+') as file:
                file.seek(0)
                lst_Inventory = pickle.load(file)
        except EOFError:
            print('\nYour CD Inventory is empty!\n')
        except Exception as e:
            print('There was an error...\n'
                  f'Error encountered: {e}\n')
        finally:
            return lst_Inventory
        
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Pickles current inventory data to text file

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of CDs): holds the inventory during runtime

        Returns:
            None.
        """
        with open(file_name, 'ab') as file:
            pickle.dump(lst_Inventory, file)

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling user Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('==== Menu === \n\n'
              '[l] load Inventory from file \n'
              '[a] Add CD\n[i] Display Current Inventory \n'
              '[s] Save Inventory to file \n'
              '[x] exit \n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input
            out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Please choose an operation: ').lower().strip()
        print()  # extra space for layout
        return choice

    @staticmethod
    def get_new_CD():
        """Gets user input for adding a new CD

        Args:
            None.

        Returns:
            cd_id (integer): CD's ID
            cd_title (string): CD's title
            cd_artist (string): artist's name
        """
        cd_id = ''
        while type(cd_id) == str:
            try:
                cd_id = int(input('Enter ID: ').strip())
            except ValueError as e:
                print('Fail! You did not enter an integer.\n'
                      f'Error encountered: {e}\n'
                      'Please enter an integer....')
            except Exception as e:
                print('There was an error...\n'
                      f'Error encountered: {e}\n')
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return cd_id, cd_title, cd_artist

# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
lst_Inventory = FileIO.load_inventory(strFileName, lst_Inventory)

while True:

# Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # let user exit program
    if strChoice == 'x':
        break
    
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue,'
              ' all unsaved data will be lost'
              ' and the Inventory re-loaded from file.')
        strYesNo = input('Type \'yes\' to continue'
                         ' and reload from file.'
                         ' Type anything else to cancel the reload: ')
        if strYesNo.lower() == 'yes':
            print('\nreloading...\n')
            lst_Inventory = FileIO.load_inventory(strFileName, lst_Inventory)
        else:
            input('Canceling...Inventory data NOT reloaded.'
                  ' Press [ENTER] to continue to the menu.')
        IO.show_inventory(lst_Inventory)
        continue
    
    # let user add data to the inventory
    elif strChoice == 'a':
        cd_id, cd_title, cd_artist = IO.get_new_CD()
        newCD = CD(cd_id, cd_title, cd_artist)
        lst_Inventory.append(newCD)
        IO.show_inventory(lst_Inventory)
        continue
    
    # show user current inventory
    elif strChoice == 'i':
        print()
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for CD in lst_Inventory:
            print(f'{CD.cd_id}\t{CD.cd_title} (by:{CD.cd_artist})')
        print('======================================')
        print()
        continue
    
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lst_Inventory)
        strYesNo = input('Save inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lst_Inventory)
            print('Inventory saved!\n')
        else:
            input('The inventory was NOT saved to file.'
                  ' Press [ENTER] to return to the menu.\n')
        continue
    
    else:
        print('General Error')

