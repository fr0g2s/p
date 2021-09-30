/* 
	랜덤한 유전체가 n개 있을 때, 3개(m)를 골라 합이 20(target_value)에 가까운 숫자 쌍을 찾아야 한다.
 	사용되는 유전 연산은 
	1. 선택
	2. 교차
	3. 변이
	이렇게 3가지이다.
	
	- 3개는 고정이라 변수 말고 상수로 사용해도 될 듯
*/

#include "commons.h"
#include "genetic.h"

#define DEBUG 1

int get_rand_num(int digit){
    return rand()%digit;
}

void show_dielectric(){
	puts("== FIRST DILECTRIC ==");
	for(int i=0;i<N;i++){
		printf("%d", first_dilectric_set[i]);
		if(i!=N-1) printf(", ");
		else puts("");
	}
	puts("=====================");
}

void init_dilectric(int target_value){	// 초기 유전체들 생성
	srand(time(NULL));
	
	target_value += 5;	// 목표치+5까지의 숫자를 사용한다. target_value를 만족하지 못하는 수는 도태되는 걸 확인해보자.
	for(int i=0;i<N;i++){
		first_dilectric_set[i] = rand()%target_value;
	}
	show_dielectric();
#ifdef DEBUG
	puts("init_dilectric end");
#endif
}

int check_sum(int target_value){
	int sum;
	
	for(int i=0;i<N/3;i++){	// 해당 세대의 각 그룹i가 target_value를 만족하는가?
		sum = 0;
		for(int j=0;j<3;j++){	// 그룹 i에 속해있는 각 유전체n[j]의 합이 target_value를 만족하는가?
			sum += curr_generation[i]->n[j];
		}
	}
	if(sum != target_value)	return 0;
	return 1;
}


int main(void){
	int target_value;	// 달성해야하는 목적 값
	
	puts("target value?");
	scanf("%d", &target_value);
	
	init_dilectric(target_value);	//	환경 설정
	make_first_generation(N, 3);	// 10개의 유전체들을 3개씩 묶는다.
	
	while(check_sum(target_value) != FOUND_SOLUTION){
		calc_fit(target_value);	// 현재 세대 유전자의 적응도 계산
		procreate();	// 다음 세대 생성
		change_generation();	// 세대 교체
		curr_century++;
		
#ifdef DEBUG
		char ans[10];
		printf("continue? (Yes/No)");
		scanf("%s", ans);
		if(strncmp(ans,"No",2)==0) break;	
#endif
	}
	printf("current century: %llu\n", curr_century);
	
	return 0;
}

