def find_perfect_square(N):
    for i in range (N):
        if i*i == N:
            return True
        
        if i*i > N :
            return False 

print(find_perfect_square(16))