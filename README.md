# 0-1 Knapsack Problem: DP vs GA

Python을 사용하여 0-1 배낭 문제(Knapsack Problem)를 해결하는 알고리즘 프로젝트입니다. 이 프로젝트의 핵심은 소규모 데이터에 대한 동적 계획법(DP)의 최적해 탐색과, 대규모 데이터에서 유전 알고리즘(GA)을 활용한 메타 휴리스틱 근사해 탐색 성능을 직접 구현하고 비교하는 것입니다.

---

### ✨ Key Features
* **Dynamic Programming (DP):** 점화식을 활용하여 소규모 데이터셋(10개)에서 100% 정확한 최적해(Global Optimum)를 도출합니다.
* **Genetic Algorithm (GA):** 교차(Crossover)와 돌연변이(Mutation) 연산을 통해 대규모 데이터셋(500개)에서 합리적인 시간 내에 우수한 해를 찾습니다.
* **Custom Repair Logic:** GA 학습 중 배낭 용량을 초과하는 염색체가 생성될 경우, 무게 대비 가치가 낮은 아이템부터 선별적으로 제거하여 항상 유효한 해(Feasible solution)로 복원하는 기능이 적용되었습니다.

---

### 🧠 Algorithm Architecture
* **DP Solver (`No2_Dynamic.py`):** 2차원 테이블 초기화 + 가치 최댓값 계산 + 역추적(Backtracking)을 통한 선택 아이템 배열 추출
* **GA Solver (`No2_Genetic.py`):** 개체군 초기화(200개) + 적합도(Fitness) 평가 + 룰렛 휠 선택(Roulette Wheel) + 단일점 교차 + 비트 반전 돌연변이(Rate: 0.01)
* **Data Parser:** 제공된 텍스트 파일(`.txt`)에서 총 배낭 용량(Capacity) 및 개별 아이템의 번호, 무게(Weight), 가치(Profit) 데이터를 자동 파싱합니다.

---

### 📐 Core Logic Implementation
동적 계획법(DP)에서는 배낭의 임시 용량이 $w$일 때, $i$번째 물건을 담을지 말지 결정하기 위해 아래와 같은 점화식 수식을 기반으로 테이블을 채워나갑니다.

$$DP[i][w] = \max(p_i + DP[i-1][w-w_i], DP[i-1][w])$$

---

### 📊 Execution & Results
* **Dataset:** 10 items (Capacity: 300) / 500 items (Capacity: 13743)
* **DP 결과:** 소규모 데이터에서 정확한 최대 가치와 선택된 아이템 번호를 반환합니다.
* **GA 결과:** 대규모 데이터에서 지정된 세대(1000 Generations)를 거쳐 수렴한 최대 가치와 선택된 총 아이템 개수를 반환합니다.
* 두 스크립트 모두 종료 시 총 실행 시간(Run time)을 초 단위로 콘솔에 함께 출력하여 알고리즘 간의 효율성을 비교할 수 있습니다.

---

### 🚀 How to Run
1. 파이썬 내장 모듈(`random`, `time`)만을 사용하므로 별도의 외부 라이브러리 설치가 필요 없습니다.
2. 실행하려는 스크립트(`No2_Dynamic.py` 또는 `No2_Genetic.py`)를 터미널에서 실행하여 알고리즘을 시작합니다.
3. 실행이 완료되면 콘솔에서 탐색된 최대 가치(MAX Value), 선택된 아이템, 그리고 알고리즘 수행 시간을 확인합니다.
