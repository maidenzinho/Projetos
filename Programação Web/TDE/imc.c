// imc.c
#include <stdio.h>

float calcular_imc(float peso, float altura) {
    if (altura <= 0) return 0;  // Para evitar divisão por zero
    return peso / (altura * altura);
}

// Wrapper para exportação
float calcular_imc_wrapper(float peso, float altura) {
    return calcular_imc(peso, altura);
}
