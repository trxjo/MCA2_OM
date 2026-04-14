import random
import math

def is_prime_miller_rabin(n, rounds=40):
    """Test de primalidad probabilístico Miller-Rabin."""
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(rounds):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_by_digits(digits):
    """Genera un número primo aleatorio con exactamente 'digits' dígitos decimales."""
    low = 10 ** (digits - 1)
    high = 10 ** digits - 1
    while True:
        candidate = random.randint(low, high)
        if candidate % 2 == 0:
            candidate += 1
        if is_prime_miller_rabin(candidate):
            return candidate

def extended_gcd(a, b):
    """Algoritmo extendido de Euclides. Retorna (g, x, y) con a*x + b*y = g."""
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def mod_inverse(e, phi):
    """Inverso modular de e módulo phi."""
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise ValueError("e y phi no son coprimos")
    return x % phi

def rsa_keygen_digits(k_digits):
    """
    Genera claves RSA con módulo de aproximadamente k_digits dígitos.
    Retorna: ((n, e), (n, d), p, q)
    """
    # Distribución de dígitos para p y q
    digits_p = k_digits // 2
    digits_q = k_digits - digits_p

    p = generate_prime_by_digits(digits_p)
    q = generate_prime_by_digits(digits_q)
    while q == p:
        q = generate_prime_by_digits(digits_q)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Exponente público estándar (no pequeño)
    e = 65537
    while math.gcd(e, phi) != 1:
        e += 2  # siguiente impar

    d = mod_inverse(e, phi)
    return (n, e), (n, d), p, q


if __name__ == "__main__":
    print("Generación de claves RSA con k = 6 dígitos\n")
    public, private, p, q = rsa_keygen_digits(6)

    print(f"p = {p}  (primo de {len(str(p))} dígitos)")
    print(f"q = {q}  (primo de {len(str(q))} dígitos)")
    print(f"n = p * q = {public[0]}  (tiene {len(str(public[0]))} dígitos)")
    print(f"φ(n) = (p-1)*(q-1) = {(p-1)*(q-1)}")
    print(f"e = {public[1]}  (elegido no pequeño)")
    print(f"d = {private[1]}")
    print(f"\nClave pública:  (n = {public[0]}, e = {public[1]})")
    print(f"Clave privada:  (n = {private[0]}, d = {private[1]})")

    # Verificación de cifrado/descifrado con un mensaje pequeño
    mensaje = 42
    cifrado = pow(mensaje, public[1], public[0])
    descifrado = pow(cifrado, private[1], private[0])
    print(f"\nPrueba con mensaje = {mensaje}:")
    print(f"  Cifrado   = {cifrado}")
    print(f"  Descifrado = {descifrado}")
    print("  Éxito" if descifrado == mensaje else "  Fallo")