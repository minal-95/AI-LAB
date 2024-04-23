def minimax(depth, nodeIndex, isMax, scores, alpha, beta):
    # Terminating condition. i.e. leaf node is reached
    if depth == 3:
        return scores[nodeIndex]

    if isMax:
        best = -float('inf')

        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, scores, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, scores, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            # Alpha Beta Pruning
            if beta <= alpha:
                break

        return best

# Driver code
scores = [3, 5, 6, 9, 1, 2, 0, -1] # Assuming a specific tree leaf values
alpha = -float('inf')
beta = float('inf')
bestVal = minimax(0, 0, True, scores, alpha, beta)
print("The optimal value is :", bestVal)

