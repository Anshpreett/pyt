from colorama import Fore, Back, Style, init

class ChessGame:
    piece_symbols = {
        'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
        'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙'
    }

    def __init__(self):
        self.board = {}
        self.reset_game()

    def reset_game(self):
        # Initialize the chessboard with pieces in their starting positions
        self.board = {
            'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'q', 'e8': 'k', 'f8': 'b', 'g8': 'n', 'h8': 'r',
            'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
            'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
            'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R'
        }

    def display_board(self):
        # Display the chessboard with color
        for j in range(8, 0, -1):
            row = [' '.join(self.piece_symbols.get(self.board.get(i + str(j), '  '), '  ') for i in 'abcdefgh')]
            colored_row = [Fore.BLACK + Fore.WHITE + piece + Fore.RESET for piece in row]
            print(' '.join(colored_row))

    def validate_move(self, start, end):
        # Check if the starting and ending squares are valid
        if not self.is_valid_square(start) or not self.is_valid_square(end):
            return False

        # Check if the move is legal for the selected piece
        piece = self.board[start]

        # Implement piece-specific move validation
        if piece[0].lower() == 'p':
            return self.validate_pawn_move(start, end)
        elif piece[0].lower() == 'r':
            return self.validate_rook_move(start, end)
        elif piece[0].lower() == 'n':
            return self.validate_knight_move(start, end)
        elif piece[0].lower() == 'b':
            return self.validate_bishop_move(start, end)
        elif piece[0].lower() == 'q':
            return self.validate_queen_move(start, end)
        elif piece[0].lower() == 'k':
            return self.validate_king_move(start, end)

        return False

    def validate_pawn_move(self, start, end):
        try:
            start_file, start_rank = start[0], int(start[1])
            end_file, end_rank = end[0], int(end[1])

        # Check if the pawn is moving forward
            if start_file == end_file:
            # For the initial move, allow two squares forward, otherwise only one
                if start_rank == 2 and end_rank - start_rank in (1, 2):
                    return True
                elif start_rank != 2 and end_rank - start_rank == 1:
                    return True
        # Check if the pawn is capturing diagonally
            elif abs(ord(start_file) - ord(end_file)) == 1 and end_rank - start_rank == 1:
                return True
        except (ValueError, IndexError):
            pass
    
        return False

    def validate_rook_move(self, start, end):
        # Example: Basic validation for rook
        # Check if the rook is moving horizontally or vertically
        return start[0] == end[0] or start[1] == end[1]

    def validate_knight_move(self, start, end):
        try:
            dx = abs(ord(start[0]) - ord(end[0]))
            dy = abs(int(start[1]) - int(end[1]))
            return (dx == 1 and dy == 2) or (dx == 2 and dy == 1) and self.is_valid_square(end)
        except (ValueError, TypeError):
            pass
        return False

    def validate_bishop_move(self, start, end):
        try:
        # Check if the bishop is moving diagonally
            if abs(ord(start[0]) - ord(end[0])) == abs(int(start[1]) - int(end[1])):
            # Check if the diagonal path is clear
                file_step = 1 if ord(end[0]) > ord(start[0]) else -1
                rank_step = 1 if int(end[1]) > int(start[1]) else -1

                file, rank = ord(start[0]) + file_step, int(start[1]) + rank_step
                while file != ord(end[0]) and rank != int(end[1]):
                    if self.board.get(chr(file) + str(rank)):
                        return False  # Path is not clear
                    file += file_step
                    rank += rank_step

                return True  # Diagonal move with a clear path

        except (ValueError, TypeError):
            pass
        return False

    def validate_queen_move(self, start, end):
        try:
        # Check if the queen is moving in a straight line
            if start[0] == end[0] or start[1] == end[1]:
            # Check if the straight path is clear
                step = 1 if start[0] == end[0] else 0
                direction = 1 if int(end[1]) > int(start[1]) else -1
                current = int(start[1]) + direction

                while current != int(end[1]):
                    if self.board.get(start[0] + str(current)):
                        return False  # Path is not clear
                    current += direction

                return True  # Straight-line move with a clear path

        # Check if the queen is moving diagonally
            if abs(ord(start[0]) - ord(end[0])) == abs(int(start[1]) - int(end[1])):
            # Check if the diagonal path is clear
                file_step = 1 if ord(end[0]) > ord(start[0]) else -1
                rank_step = 1 if int(end[1]) > int(start[1]) else -1

                file, rank = ord(start[0]) + file_step, int(start[1]) + rank_step
                while (file, rank) != (ord(end[0]), int(end[1])):
                    if self.board.get(chr(file) + str(rank)):
                        return False  # Path is not clear
                    file += file_step
                    rank += rank_step

                return True  # Diagonal move with a clear path

        except (ValueError, TypeError):
            pass
        return False

    def validate_king_move(self, start, end):
        # Example: Basic validation for king
        # Check if the king is moving one square in any direction
        try:
            dx = abs(ord(start[0]) - ord(end[0]))
            dy = abs(int(start[1]) - int(end[1]))
            return dx <= 1 and dy <= 1
        except ValueError:
            pass
        return False

    def update_board(self, start, end):
        # Update the board after a valid move
        if self.is_valid_square(start) and self.is_valid_square(end):
            piece = self.board[start]
            self.board[end] = piece
            del self.board[start]

    def play_game(self):
        # Main game loop
        while True:
            self.display_board()
            start = input("Enter the starting square: ")
            end = input("Enter the ending square: ")

            if not self.validate_move(start, end):
                print("Invalid move. Please try again.")
                continue

            self.update_board(start, end)

    @staticmethod
    def is_valid_square(square):
        try:
            file, rank = square[0], int(square[1])
            return file in 'abcdefgh' and 1 <= rank <= 8
        except (IndexError, ValueError):
            return False

# Example usage 
if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.play_game()