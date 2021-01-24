int add(int a, int b)
{
    return a + b;
}

void sequence(void *p, int n)
{
    unsigned char *buf = (unsigned char *)p;
    int i;

    for (i = 0; i < n; i++)
    {
        buf[i] = i + 1;
    }
}
