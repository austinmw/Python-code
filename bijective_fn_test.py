n=int(input())
ns=list(map(int, input().split()))
is_onto=len(ns)==len(set(ns))
print("YES" if is_onto else "NO")
