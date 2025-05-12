//#include <bits/stdc++.h>
//using namespace std;
//
//int n, m, k;
//vector<int> v;
//
//int main() {
//    // N, M, K를 공백을 기준으로 구분하여 입력 받기
//    cin >> n >> m >> k;
//
//    // N개의 수를 공백을 기준으로 구분하여 입력 받기
//    for (int i = 0; i < n; i++) {
//        int x;
//        cin >> x;
//        v.push_back(x); // 1.
//    }
//
//    sort(v.begin(), v.end()); // 입력 받은 수들 정렬하기 // 2.
//    int first = v[n - 1]; // 가장 큰 수
//    int second = v[n - 2]; // 두 번째로 큰 수
//
//    // 가장 큰 수가 더해지는 횟수 계산
//    int cnt = (m / (k + 1)) * k;
//    cnt += m % (k + 1);
//
//    int result = 0;
//    result += cnt * first; // 가장 큰 수 더하기
//    result += (m - cnt) * second; // 두 번째로 큰 수 더하기
//
//    cout << result << '\n'; // 최종 답안 출력
//}
//
//// 1.
//// #include <iostream>
//// #include <vector>
//// int main() {
////     // 정수형 벡터 v 선언
////     std::vector<int> v;
////     // v에 10을 추가
////     v.push_back(10);  // 벡터 v의 끝에 10을 추가
////     // v에 20을 추가
////     v.push_back(20);  // 벡터 v의 끝에 20을 추가
////     // v에 30을 추가
////     v.push_back(30);  // 벡터 v의 끝에 30을 추가
////     // 벡터의 요소 출력
////     for (int i = 0; i < v.size(); ++i) {
////         std::cout << v[i] << " ";  // 벡터 v의 각 요소 출력
////     }
////     return 0;
//// }
//// 출력은
//// 10 20 30
//
//
//
//
//// 2.
//// sort(v.begin(), v.end())의 동작:
//// sort 함수는 v.begin()부터 v.end()까지의 범위에 있는 요소들을 정렬합니다.
//// 즉, v.begin()이 첫 번째 요소를 가리키고, v.end()는 범위의 끝을
//// 가리키기 때문에, 벡터의 모든 요소를 대상으로 정렬이 수행됩니다.