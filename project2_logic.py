# lab 1 revamp
#logic file
import csv

class VotingSystem:
    def store_vote(self, ID: str, candidate: str) -> None:
        """
        Stores votes into "vote_data.csv". But first checks for errors in inputs.
        :param ID: ID number for voter
        :param candidate: Candidate the voter voted for
        :return: None
        """

        if len(ID) > 10:
            raise TypeError("ID must be 10 digits or less.")
        try:
            ID: str = int(ID)
        except ValueError:
            raise ValueError("ID must be digits.")

        if self.check_id(ID):
            raise ValueError("Already voted.")

        with open('vote_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([ID, candidate])

    def check_id(self, num: str) -> bool:
        """
        Checks whether or not the inputted ID already exists, basically if a voter already voted.
        :param num: Current ID number being checked
        :return: Boolean value
        """
        with open('vote_data.csv', 'r') as f:
            reader = csv.reader(f)
            for x in reader:
                if x[0] == str(num):

                    return True


        return False

    def get_results(self) -> dict:
        """
        Gets voting results from CSV file to utilize in a data structure
        :return: dict results
        """
        results: dict = {}
        with open('vote_data.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for data in reader:
                if data[1] in results:

                    results[data[1]] += 1
                else:
                    results[data[1]] = 1

        return results