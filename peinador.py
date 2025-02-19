# Copyright (c) 2025 José Ignacio Peinador Sala  
#  
# Este software está disponible bajo una licencia dual:  
#  
# 1. Uso Académico:  
#    - Gratuito bajo los términos de la Licencia Pública General GNU (GPL) versión 3.  
#    - Ver archivo `LICENSE_GPL.txt` para más detalles.  
#  
# 2. Uso Comercial:  
#    - Requiere un acuerdo de licencia específico y el pago de royalties.  
#    - Contacte al autor para más información.
#
# 3. Este software fue desarrollado con la asistencia de DeepSeek Chat,  
# un modelo de inteligencia artificial desarrollado por DeepSeek.  
#  
# Agradecimientos especiales por su ayuda en la implementación,  
# pruebas y documentación del algoritmo.  
#  
# Todos los derechos reservados.
  
known_primes = []

def calcular_k_min(entry):
    p = entry["p"]
    original_k = entry["original_k"]
    es_menos_uno = entry["es_menos_uno"]
    
    # Excepción para p=11
    if p == 11:
        return 19
    
    if es_menos_uno:
        return p * original_k - original_k
    else:
        return p * original_k + original_k

def es_posicion_prima(k, es_menos_uno):
    for entry in known_primes:
        p = entry["p"]
        original_k = entry["original_k"]
        is_prime_menos_uno = entry["es_menos_uno"]
        
        k_min = calcular_k_min(entry)
        if k < k_min:
            continue
        
        if es_menos_uno:
            if is_prime_menos_uno:
                if (k - original_k) % p == 0:
                    return False
            else:
                if (k + original_k) % p == 0:
                    return False
        else:
            if is_prime_menos_uno:
                if (k + original_k) % p == 0:
                    return False
            else:
                if (k - original_k) % p == 0:
                    return False
    return True

def inicializar_primos_base():
    primos_base = [
        {"p": 5, "original_k": 1, "es_menos_uno": True},
        {"p": 7, "original_k": 1, "es_menos_uno": False},
        {"p": 11, "original_k": 2, "es_menos_uno": True},
        {"p": 13, "original_k": 2, "es_menos_uno": False},
        {"p": 17, "original_k": 3, "es_menos_uno": True},
        {"p": 19, "original_k": 3, "es_menos_uno": False},
    ]
    known_primes.extend(primos_base)

# Inicializar primos base
inicializar_primos_base()

if __name__ == "__main__":
    # Contadores para el resumen final
    total_primos = 0
    total_compuestos = 0
    
    # Contadores para las condiciones
    condiciones_iniciales = len(known_primes)  # 6 condiciones iniciales
    condiciones_finales = 0
    
    # Rango de k a evaluar
    k_max = 100
    
    # Verificar desde k=1 hasta k=k_max
    for k in range(1, k_max + 1):
        for es_menos_uno in [True, False]:
            n = 6 * k - 1 if es_menos_uno else 6 * k + 1
            resultado = es_posicion_prima(k, es_menos_uno)
            if resultado:
                # Calcular k_min antes de añadir la condición
                k_min_calculado = calcular_k_min({
                    "p": n,
                    "original_k": k,
                    "es_menos_uno": es_menos_uno
                })
                
                # Solo añadir la condición si k_min_calculado <= k_max
                if k_min_calculado <= k_max:
                    known_primes.append({
                        "p": n,
                        "original_k": k,
                        "es_menos_uno": es_menos_uno
                    })
                    condiciones_finales += 1  # Se añade una nueva condición
                    print(f"k={k}, 6k {'-1' if es_menos_uno else '+1'} = {n}: PRIMO ✅ (k_min={k_min_calculado})")
                else:
                    print(f"k={k}, 6k {'-1' if es_menos_uno else '+1'} = {n}: PRIMO ✅ (k_min={k_min_calculado} > {k_max}, NO SE AÑADE)")
                total_primos += 1
            else:
                print(f"k={k}, 6k {'-1' if es_menos_uno else '+1'} = {n}: COMPUESTO 🚫")
                total_compuestos += 1
    
    # Resumen final
    print("\nResumen Final:")
    print(f"Total de Primos: {total_primos}")
    print(f"Total de Compuestos: {total_compuestos}")
    print(f"Condiciones iniciales: {condiciones_iniciales}")
    print(f"Condiciones finales: {condiciones_finales}")
    print(f"Condiciones utilizadas (k_min <= {k_max}): {condiciones_finales}")
    # Cálculo dinámico del límite superior para la etiqueta
    limite_superior = 6 * k_max + 1
    print(f"Condiciones utilizadas (n <= {limite_superior}): {condiciones_finales + 2} = {condiciones_finales} + 2 (añadiendo los primos 2 y 3)")