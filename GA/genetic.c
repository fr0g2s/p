#include "commons.h"
#include "genetic.h"

void make_first_generation(int n, int m){	// n개의 초기 유전체들로, m개씩 하나의 유전자 그룹으로 만든다.
	int *used = (int *)malloc(sizeof(int)*n);
	int rand_idx;
	
	curr_generation = (struct GENE**)malloc(sizeof(unsigned int)*(n/m));
	for(int i=0;i<n/m;i++){
		curr_generation[i] = (struct GENE*)malloc(sizeof(struct GENE));
		for(int j=0;j<3;j++){
			do{
				rand_idx = get_rand_num(RAND_NUMLEN);
				curr_generation[i]->n[j] = first_dilectric_set[rand_idx];
			}while(used[rand_idx] == 1);
			used[rand_idx] = 1;
		}
	}
#ifdef DEBUG
	puts("make_first_generation end");
#endif
	return;
}

void selection(){	// 적합도 검사 후, 우수한 유전자는 증식되고, 열등한 유전자는 도태된다.
	puts("selection");
}
void crossover(){	// 자신의 유전체와 다른 유전자의 유전체를 교환한다.
	puts("crossover");
}
void mutation(){	// 변이를 일으킨다.
	puts("mutation");
}

void procreate(){	// 유전 연산을 통해 다음 세대를 생성한다.
	selection();
	crossover();
	mutation();
}
void calc_fit(int target_value){
	int tot;
	for(int i=0;i<N/3;i++){
		tot = 0;
		for(int j=0;j<3;j++){
			tot += curr_generation[i]->n[j];
		}
		curr_generation[i]->fit = abs(target_value-tot);	// 적응도값이 낮을 수록 목표치에 가깝다. 즉, 증식할 확률이 높다.
	}
	show_gene(N, 3);
}

void change_generation(){	// 세대 교체를 위해 curr_generation이 next_generation을 가진다.
	puts("change_generatio");
}

void show_gene(int n, int m){
	puts("== FIRST GENERATION ==");
	for(int i=0;i<n/m;i++){
		printf("{");
		for(int j=0;j<m;j++){
			printf("%d", curr_generation[i]->n[j]);
			if(j!=m-1) printf(", ");
		}
		printf("} : %d\n", curr_generation[i]->fit);
	}
	puts("=======================");
}