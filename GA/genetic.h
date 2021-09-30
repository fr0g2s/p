#define N 10
#define NUMLEN 1*10	// 자릿수 * 10
#define RAND_NUMLEN 1*10
#define FOUND_SOLUTION 1

struct GENE{
	int n[3];	// 3개의 유전체
	int fit;	// 적응도	
	int rank;	// 우수 유전자 순위
};

int first_dilectric_set[N];	// 초기 유전체 후보 집합
struct GENE **curr_generation;	// 현재 세대
struct GENE **next_generation;	// 다음 세대
struct GENE **best_generation;	// target_value의 가장 근처에 도달했을 때의 유전자 그룹
unsigned long long int curr_century;
unsigned long long int best_century;	// target_value의 가장 근처에 도달했을 때의 세기

void make_first_generation(int, int);

void calc_fit(int);
void selection();
void crossover();
void mutation();

void procreate_next_generation();
void change_generation();
void show_gene(int, int);