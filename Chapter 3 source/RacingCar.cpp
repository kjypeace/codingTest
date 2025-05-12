//struct Car
//{
//	char gamerID[ID_LEN];	// ������ID
//	int fuelGauge;		// ���ᷮ
//	int curSpeed;		// ����ӵ�
//
//	void ShowCarState()
//	{
//		cout << "������ID: " << gamerID << endl;
//		cout << "���ᷮ: " << fuelGauge << "%" << endl;
//		cout << "����ӵ�: " << curSpeed << "km/s" << endl << endl;
//	}
//	void Accel()
//	{
//		if (fuelGauge <= 0)
//			return;
//		else
//			fuelGauge -= FUEL_STEP;
//
//		if (curSpeed + ACC_STEP >= MAX_SPD)
//		{
//			curSpeed = MAX_SPD;
//			return;
//		}
//
//		curSpeed += ACC_STEP;
//	}
//	void Break()
//	{
//		if (curSpeed < BRK_STEP)
//		{
//			curSpeed = 0;
//			return;
//		}
//
//		curSpeed -= BRK_STEP;
//	}
//};