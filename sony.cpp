int fib_iter(int n) // n = 3이라면?
{
if (n == 0) return 0;
if (n == 1) return 1;
int pp = 0;
int p = 1;
int result = 0;
for (int i = 2; i <= n; i++) {
result = p + pp;
pp = p; // n-2
p = result; // n-1
}
return result;
}
// result = 1, pp = 1, p = 1
// result = 2, pp = 1, p = 2
