import sys

if len(sys.argv) < 3:
    real_file = "test_set_unseen.txt"
    pred_file = "results.txt"
else:
    real_file = sys.argv[1]
    pred_file = sys.argv[2]

print(f"Comparing {real_file} with {pred_file}...")

try:
    with open(real_file) as f1, open(pred_file) as f2:
        real_lines = f1.readlines()
        pred_lines = f2.readlines()
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(1)

total = len(real_lines)
if total == 0:
    print("Error: Real file is empty")
    sys.exit(1)

correct = 0

# Ensure we don't go out of bounds if files have different lengths
limit = min(len(real_lines), len(pred_lines))

for i in range(limit):
    real = real_lines[i]
    pred = pred_lines[i]
    
    # Real line: "rnbqk... Check" -> Label is the last word
    parts = real.strip().split()
    if not parts:
        continue
        
    real_label = parts[-1]
    # Handle "Check White"/"Check Black" cases from Epitech files if present
    if real_label in ["White", "Black"] and len(parts) >= 2:
        real_label = parts[-2]
        
    pred_label = pred.strip()
    if "->" in pred_label:
        pred_label = pred_label.split("->")[-1].strip()
    
    if real_label == pred_label:
        correct += 1
    # Check vs Checkmate edge case (Acceptable mistake)
    elif real_label == "Check" and pred_label == "Checkmate":
        pass # Wrong but understandable
    elif real_label == "Checkmate" and pred_label == "Check":
        pass # Wrong but understandable
    else:
        # print(f"WRONG: Real={real_label} vs Pred={pred_label}")
        pass

print(f"Accuracy: {correct}/{limit} = {correct/limit*100:.2f}%")
