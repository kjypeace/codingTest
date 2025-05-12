//#include <iostream>
//#include <vector>
//#include <algorithm>
//using namespace std;
//int main() {
//    int n, m;
//    cin >> n >> m;
//    int result = 0;
//    for (int i = 0; i < n; i++) {
//        vector<int> data(m); // 1.
//        for (int j = 0; j < m; j++) {
//            cin >> data[j];
//            // 사용자로부터 입력을 받아서, data[j]에 저장하라는 뜻
//        }
//        // 현재 줄에서 가장 작은 수
//        int min_value = *min_element(data.begin(), data.end());
//        // 지금까지의 result와 비교해서 더 큰 값을 저장
//        result = max(result, min_value);
//    }
//    cout << result << endl;
//    return 0;
//}
//
//// 2 4
//// 7 3 1 8
//// 3 3 3 4
//
//// 1.
//// int m = 5;
//// vector<int> data(m);  // 크기가 5인 벡터 만들기
//// data = [0, 0, 0, 0, 0]
////          ↑  ↑  ↑  ↑  ↑
////         0번 1번 2번 3번 4번 인덱스
//// 2.
