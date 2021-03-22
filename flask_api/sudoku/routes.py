from sudoku_solver.sudoku import Sudoku

from .. import app


@app.route("/")
def index():
    return "Hello world"
