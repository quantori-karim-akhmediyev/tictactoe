class GameError(Exception):
    pass


class InvalidMoveError(GameError):
    pass


class InvalidCoordinatesError(GameError):
    pass


class InvalidPlayerError(GameError):
    pass


class InvalidCommandError(GameError):
    pass


class InvalidFileError(GameError):
    pass


class InvalidGameError(GameError):
    pass


class InvalidWinnerError(GameError):
    pass


class InvalidBoardError(GameError):
    pass
