import csv
import Constants

from pathlib import Path

class Scores:
    """
    Class providing reading and updating scores
    """

    def __init__(self, board_name):
        self.board_name = board_name
        self._scores = None


    def get_scores(self):
        if self._scores is None:
            self._scores = self._get_scores_for_board()
        return self._scores


    def add_score(self, user, score):
        self._scores = self.get_scores()
        if self.is_score_rated(score):
            self._scores.append((user, score))
            self._scores.sort(key = lambda x: x[1])
            self._scores = self._scores[:10]

            path = self._get_file_path()
            directory = Path("Scores")
            if not Path.exists(directory):
                Path(directory).mkdir(parents = True, exist_ok = True) 
                if not path.exists():
                    path.touch()

            text = '\n'.join(','.join(map(str, t)) for t in self._scores)
            path.write_text(text, encoding = Constants.encoding)


    def is_score_rated(self, score):
        scores = self.get_scores()
        return len(scores) < 10 or any(score < x[1] for x in scores)

            
    def _get_scores_for_board(self):
        path = self._get_file_path()
        if path.exists():
             with path.open(mode = 'r', encoding = Constants.encoding) as file:
                reader = csv.reader(file)
                return [(row[0], int(row[1])) for row in reader]
        return list()


    def _get_file_path(self):
        return Path(f"Scores/{self.board_name}")


    def clear_scores(self):
        path = self._get_file_path()
        path.write_text("", encoding = Constants.encoding)