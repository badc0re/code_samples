from service.client import SolverClient

sc = SolverClient("127.0.0.1", 8000)
result = sc.fibbonachi(10)
assert result == 55
print("Smoke test done.")
