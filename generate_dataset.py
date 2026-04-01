import chess
import random
import sys

def get_label(board):
    if board.is_checkmate():
        return "Checkmate"
    if board.is_check():
        return "Check"
    return "Nothing"

def generate_dataset(filename, num_positions):
    print(f"Generating {num_positions} unique positions for {filename}...")
    with open(filename, "w") as f:
        count = 0
        while count < num_positions:
            board = chess.Board()
            # Play a random game (depth 5 to 60 moves)
            for _ in range(random.randint(5, 60)):
                if board.is_game_over():
                    break
                moves = list(board.legal_moves)
                if not moves:
                    break
                board.push(random.choice(moves))
                
                label = get_label(board)
                
                # BALANCING LOGIC:
                # "Nothing" is too common. Only keep 10% of "Nothing" positions.
                # Always keep "Check" and "Checkmate".
                if label != "Nothing" or random.random() < 0.1:
                    # Write simple FEN + Label
                    f.write(f"{board.fen()} {label}\n")
                    count += 1
                    if count >= num_positions:
                        break
    print("Done.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_dataset.py <filename> <amount>")
        sys.exit(1)
    
    generate_dataset(sys.argv[1], int(sys.argv[2]))
