"""
    Zac Schimpf
    CSCI 1620 001/851
    Professor Owora
    Week 01 - Lab 01
    23/01/2024
"""


class Voter:
    def __init__(self) -> None:
        """
        Primary loop responsible for taking, tracking & printing votes
        :return: None
        """
        candidates = ["John", "Jane"]
        total_votes = []

        option = None
        while option != 'x':
            option = self.vote_menu()

            if option != 'x':
                # Shift value to account for list[] indexing
                current_vote = self.candidate_menu() - 1

                total_votes.append(candidates[current_vote])
                print("Voted " + candidates[current_vote])

        print(
            self.breaker() + '\n' +
            "John – " + str(total_votes.count("John")) +
            ", Jane – " + str(total_votes.count("Jane")) +
            ", Total – " + str(len(total_votes)) + '\n' +
            self.breaker()
        )


    def vote_menu(self) -> str:
        """
        Primary menu containing navigation options
        :return: Menu option, single-char string; e.g. 'v', 'x'
        """

        print(
            self.breaker() + '\n' +
            "VOTE MENU" + '\n' +
            self.breaker() + '\n' +
            "v: Vote" + '\n' +
            "x: Exit"
        )
        option = input("Option: ")
        return self.menu_validation(option)


    def menu_validation(self, option) -> str:
        """
        Clean & validate user's navigation option
        :param option: Raw user input, single-char string; e.g. 'v', 'x'
        :return: Validated option, single-char string; e.g. 'v', 'x'
        """

        option = option.strip().casefold()

        if option != 'v' and option != 'x':
            option = self.vote_menu_redo()

        return option


    def vote_menu_redo(self) -> str:
        """
        Primary menu redo prompt
        :return: raw user input
        """

        option = self.menu_validation(input("Invalid (v/x): "))
        return option


    def candidate_menu(self) -> str:
        """
        Secondary menu containing voter options
        :return: Voter choice string; e.g. "John", "Jane"
        """

        print(
            self.breaker() + '\n' +
            "CANDIDATE MENU" + '\n' +
            self.breaker() + '\n' +
            "1: John" + '\n' +
            "2: Jane"
        )
        option = input("Option: ")
        return self.candidate_validation(option)


    def candidate_validation(self, option) -> int:
        """
        Clean & validate user's navigation option
        :param option: Menu option, single-char string; e.g. '1', '2'
        :return: Voter choice int; e.g. 1, 2
        """

        option = option.strip().casefold()

        if option != '1' and option != '2':
            option = self.candidate_menu_redo()

        return int(option)


    def candidate_menu_redo(self) -> str:
        """
        Secondary menu redo prompt
        :return: raw user input
        """

        option = self.candidate_validation(input("Invalid (1/2): "))
        return option


    def breaker(self) -> str:
        """
        :return: Standardised size line break
        """

        breaker_len = 29
        breaker_char = '-'
        breaker_str = breaker_char * breaker_len
        return breaker_str


test = Voter()
