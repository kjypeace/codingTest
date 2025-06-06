#include <iostream>
using namespace std;

#define ID_LEN		20
#define MAX_SPD		200
#define FUEL_STEP	2
#define ACC_STEP	10
#define BRK_STEP	10

struct Car
{
	char gamerID[ID_LEN];	// 소유자ID
	// **최대 19자 + 널 종료문자('\0')**까지 저장할 수 있는
	// 문자열 저장 공간입니다.
	// "run99"는 실제로 "r", "u", "n", "9", "9", "\0" 이렇게 6개의 문자를 가짐.
	int fuelGauge;			// 연료량
	int curSpeed;			// 현재속도

	void ShowCarState()
	{
		cout<<"소유자ID: "<<gamerID<<endl;
		// cout << "출력할 내용";
		// <<endl;
		cout<<"연료량: "<<fuelGauge<<"%"<<endl;
		cout<<"현재속도: "<<curSpeed<<"km/s"<<endl<<endl;
	}
	void Accel()
	{
		if(fuelGauge<=0)
			return;
		else
			fuelGauge-=FUEL_STEP;

		if(curSpeed+ACC_STEP>=MAX_SPD)
		{
			curSpeed=MAX_SPD;
			return;
		}
	
		curSpeed+=ACC_STEP;
	}
	void Break()
	{
		if(curSpeed<BRK_STEP)
		{
			curSpeed=0;
			return;
		}

		curSpeed-=BRK_STEP;
	}
};

int main(void)
{
	Car run99={"run99", 100, 0};
	run99.Accel();
	run99.Accel();
	run99.ShowCarState();
	run99.Break();
	run99.ShowCarState();

	Car sped77={"sped77", 100, 0};
	sped77.Accel();
	sped77.Break();
	sped77.ShowCarState();
	return 0;
}