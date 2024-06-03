#include <iostream>   // Incluye la biblioteca estándar de entrada/salida

using namespace std;

// Definición de la clase Punto_OD
class Punto_OD {
    int o;  // Coordenada 'o' del punto
    int d;  // Coordenada 'd' del punto

public:
    // Constructor por defecto que inicializa 'o' y 'd' con valores aleatorios entre 0 y 99
    Punto_OD() {
        o = rand() % 100;
        d = rand() % 100;
    }
    
    // Constructor que inicializa 'o' y 'd' con valores proporcionados
    Punto_OD(int o1, int d) {
        o = o1;
        this->d = d;
    }
    
    // Método para obtener el valor de 'o'
    int getO() {
        return o;
    }
    
    // Método para obtener el valor de 'd'
    int getD() {
        return d;
    }
};

// Definición de la clase Matriz_OD
class Matriz_OD {
    int matriz[10][10];  // Matriz de 10x10 para almacenar conteos

public:
    // Constructor por defecto que inicializa todos los elementos de la matriz a 0
    Matriz_OD() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                matriz[i][j] = 0;
            }
        }
    }
  
    // Método para añadir un Punto_OD a la matriz
    void addPunto_OD(Punto_OD p) {
        // Incrementa el conteo en la celda correspondiente, escalando las coordenadas
        matriz[p.getO() / 10][p.getD() / 10] += 1;
    }
  
    // Método para calcular y retornar el punto con el mayor valor en la matriz
    Punto_OD calcMax() {
        int max = 0;  // Valor máximo encontrado
        int o = -1;   // Coordenada 'o' del punto máximo
        int d = -1;   // Coordenada 'd' del punto máximo

        // Recorre toda la matriz para encontrar el valor máximo
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                if (matriz[i][j] > max) {
                    max = matriz[i][j];
                    o = i;
                    d = j;
                }
            }
        }
        return Punto_OD(o, d);  // Retorna un Punto_OD con las coordenadas del máximo valor
    }
  
    // Método para calcular y retornar el promedio de los valores en la matriz
    double calcPromedio() {
        double prom = 0;

        // Suma todos los valores de la matriz
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                prom += matriz[i][j];
            }
        }
        return prom / 100;  // Retorna el promedio
    }
  
    // Método para obtener el valor en una celda específica de la matriz
    int getVal(int o, int d) {
        return matriz[o][d];
    }
  
    // Método para imprimir la matriz en la consola
    void print() {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                cout << matriz[i][j] << "\t";
            }
            cout << endl;
        }
    }
};

// Función principal del programa
int main() {
    srand(1234);  // Inicializa el generador de números aleatorios con una semilla fija
    Punto_OD lista[10000];  // Crea un arreglo de 10000 objetos Punto_OD
    Matriz_OD m;  // Crea una instancia de Matriz_OD

    // Inicializa cada Punto_OD en el arreglo con valores aleatorios
    for (int i = 0; i < 10000; i++) {
        lista[i] = Punto_OD();
    }

    // Añade cada Punto_OD del arreglo a la matriz
    for (int i = 0; i < 10000; i++) {
        m.addPunto_OD(lista[i]);
    }

    // Imprime la matriz completa
    m.print();

    // Calcula el punto con el mayor valor en la matriz
    Punto_OD max = m.calcMax();
    cout << "El punto con mayor valor es (" << max.getO() << "," << max.getD() << ") con valor " << m.getVal(max.getO(), max.getD()) << endl;

    // Calcula e imprime el promedio de los valores en la matriz
    cout << "El promedio de valores es " << m.calcPromedio() << endl;

    return 0;  // Termina la ejecución del programa
}


//Explicación del Flujo del Programa
//Inicialización del Generador Aleatorio: Se establece una semilla para el generador de números aleatorios con srand(1234).
//Creación de Puntos: Se crean 10000 objetos Punto_OD con coordenadas aleatorias.
//Población de la Matriz: Los puntos se añaden a una instancia de Matriz_OD, incrementando los valores en las celdas correspondientes.
//Impresión de la Matriz: Se imprime la matriz completa.
//Cálculo del Punto con Mayor Valor: Se determina y se imprime la celda con el mayor valor y su conteo.
//Cálculo del Promedio: Se calcula e imprime el promedio de los valores en la matriz.

//Usa https://www.onlinegdb.com/online_c++_compiler



