#!/usr/local/bin/python3.4
k2, k3, k5, k6 = map(int, input().split())
minimal256 = min(k6, k5, k2)
sum_ = 256 * minimal256
k2 -= minimal256
minimal32 = min(k3, k2)
sum_ += minimal32 * 32

print(sum_)
