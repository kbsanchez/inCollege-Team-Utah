from indexed import IndexedOrderedDict as IOdict
from colorama import Fore, Style
from typing import Callable, Dict


class Menu:
    """base class for all menus"""
    def __init__(self) -> None:
        self.title: str = str()
        self.subtitle: str = str()
        self.entry_text: str = str()
        self.exit_text: str = str()
        self.generic_err: str = str()
        self.prompt: str = "Select an option from the menu: "
        self.return_option_text: str = "Go back\n"
        self.invalid_input_err: str = f"{Fore.RED}Invalid Selection{Style.RESET_ALL}\n"  # makes text red
        self.options: Dict[str, Callable] = IOdict()
        self.options[self.return_option_text] = self._end

    def __repr__(self) -> str:
        self.options.move_to_end(self.return_option_text, False) # return option must always be first
        output: str = f"\n{self.title}\n{self.subtitle}\n"  # menu header
        for i, key in enumerate(self.options.keys()):  # menu options
            output += f"{i} - {key}\n"
        return output

    def _read(self) -> Callable:  # TODO Joseph 9/29: Use strings directly
        """get user menu selection"""
        try:
            selection: int = int(input(self.prompt))
            assert selection >= 0
            return self.options.values()[selection]
        except (ValueError, AssertionError, IndexError):
            print(self.invalid_input_err)
            return self._do_nothing

    def _do_nothing(self) -> None:
        """do nothing"""
        pass

    def _end(self) -> bool:
        """exit the menu"""
        print(self.exit_text)
        return True

    def run(self) -> None:
        """run the menu"""
        done: bool = False
        print(self.entry_text)
        while not done:
            print(self)
            action: Callable = self._read()
            done = action()
        print(self.exit_text)
