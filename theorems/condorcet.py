from utils import plt, np, ceil, comb, random, majority

def montecarlo(p, n, m):
    trials = int(1e6)
    r = majority(n, m)
    if r is None:
        return None
    if n % 2:
        return np.sum(np.sum((np.random.random(size=(trials, n)) < p).astype(int), axis=1) >= r) / trials
    else:
        return (np.sum(np.sum((np.random.random(size=(trials, n)) < p).astype(int), axis=1) >= r) / trials + ((1/2)*(comb(n, (n//2)) * (p**(n//2)) * ((1 - p)**(n-(n//2))))))

def deterministic(p, n, m):
    r = majority(n, m)
    if r == None: return None
    P = 0
    while r <= n:
        P += (comb(n, r) * (p**r) * ((1 - p)**(n-r)))
        r += 1
    if n % 2 == 0:
        P += (1/2) * (comb(n, (n//2)) * (p**(n//2)) * ((1 - p)**(n-(n//2))))

    return P

def plot(n_values, type, m):
    plt.figure(figsize=(10, 6))
    p_values = np.arange(0, 1.01, 0.01)
    for n in n_values:
        y_values = [deterministic(p, n, m) if type == 0 else montecarlo(p, n, m) for p in p_values]
        plt.plot(p_values, y_values, label=f'n={n}', color=np.random.rand(3,))
    plt.title('Probability of Correct Majority Decision by p and n')
    plt.xlabel('Probability of Correctness of Independent Voter (p)')
    plt.ylabel('Probability of Correct Majority Decision')
    plt.legend()
    plt.grid(True)
    plt.show()