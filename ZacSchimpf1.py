"""
    Zac Schimpf
    CSCI 1620 001/851
    Professor Owora
    Final - Project 1
    29/4/2024
"""

from csv import writer
import gui


class Voter:
    def __init__(self) -> None:
        """
        Main logic structure that establishes candidates, accepts votes, and prints results
        """
        self.VOTE_OPTIONS = ["Jane", "Jesse", "John"]
        self._vote_results = {}

    def export_to_csv(self, user_input: list) -> None:
        """
        Formats export data and passes to output.csv in the cwd
        :param user_input: A list[] of votes cast by the user
        """
        self.set_results(user_input)

        with open("output.csv", 'w', newline='') as outbound_file:
            csv_writer = writer(outbound_file, delimiter=',')
            csv_writer.writerow(["Candidate", "Votes", "Percent"])
            for key in self._vote_results:
                csv_writer.writerow([key, self._vote_results[key][0], self._vote_results[key][1]])

    def set_results(self, user_input: list) -> None:
        """
        Analyzes data by counting quantities and percentages
        :param user_input: A list[] of votes cast by the user
        """
        for option in self.VOTE_OPTIONS:
            self._vote_results[option] = 0

        for vote in user_input:
            self._vote_results[vote] += 1

        self._vote_results = {candidate: votes for candidate, votes in sorted(
            self._vote_results.items(), key=lambda current_value: current_value[1], reverse=True)}

        total_votes = 0
        for key in self._vote_results:
            total_votes += self._vote_results[key]
        for key in self._vote_results:
            percent = self._vote_results[key] / total_votes
            self._vote_results[key] = [self._vote_results[key], f'{percent:.2f}']

    def __str__(self) -> str:
        """
        Console-level output of candidate results
        :return: String formatted data
        """
        output = "Candidate" + "\t" + "Votes" + "\t" + "Percent" + "\n"
        for key in self._vote_results:  # double-tabbed to accommodate header width
            output += (key
                       + "\t\t" + str(self._vote_results[key][0])
                       + "\t\t" + str(self._vote_results[key][1]) + "\n")

        return output


if __name__ == "__main__":
    election = Voter()

    app = gui.GUI(election.VOTE_OPTIONS)
    app.mainloop()

    election.export_to_csv(app.get_user_input())
    print(election.__str__())
