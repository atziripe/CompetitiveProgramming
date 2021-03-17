#include <stdio.h>
#include <stdlib.h>

void merge(int arr[], int l, int m, int r){
    int i,j,k; //Iteradores
    int n1 = m-l+1;
    int n2 = r -m ;

    //Crear arreglos temporales
    int L[n1], R[n2];

    //Llenando los arreglos temp
    for(i = 0; i < n1; i++)
        L[i] = arr[l+i];
    for(j = 0; j < n2; j++)
        R[j] = arr[m+1+j];
    
    //Inicializamos de nuevo los iteradores
    i = 0; //Recorre L
    j = 0; //Recorre R
    k = l; //Recorre array completo

    //Comparando item x item en L y R
    while(i < n1 && j < n2){
        if(L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        }
        else{
            arr[k]=R[j];
            j++;
        }
        k++;
    }
    //Se agregan numeros sobrantes
    while(i < n1){
        arr[k] = L[i];
        i++;
        k++;
    }
    while(j < n2){
        arr[k] = R[j];
        j++;
        k++;
    }

}
void mergeSort(int array[], int l, int r){
    int m = 0;
    if(l < r){
        m = (l+(r-1))/2;

        mergeSort(array, l, m);
        mergeSort(array, m+1, r);

        merge(array,l,m,r);
    }
}
int main(int argc, char const *argv[]){
    int *array;
    int n = 0;
    if(argc != 2){
		printf("\nIndique el tamanio del algoritmo - Ejemplo: [user@equipo]$ %s 100\n",argv[0]);
		exit(1);
	} else
        n = atoi(argv[1]);
    array = (int*)malloc(sizeof(int)*n);
    for(int i = 0; i < n; i++)
        scanf("%d", array+i);
    mergeSort(array,0,n-1);
    for(int i = 0; i < n; i++)
        printf("%d ", *(array+i));
    return 0;
}