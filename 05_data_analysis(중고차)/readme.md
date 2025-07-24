# 🚗 중고차 가격 예측 모델 (Used Car Price Prediction)

## 📌 프로젝트 개요
본 프로젝트는 중고차의 다양한 특성(주행거리, 연식, 연료 타입 등)을 바탕으로 **중고차의 시세(`price_in_aed`)를 예측**하는 회귀 모델을 개발하는 것을 목표로 합니다. 다양한 모델을 비교 실험하여 가장 효과적인 예측 방식을 도출하였습니다.

---

## 🧰 사용한 기술 스택 및 라이브러리

- Python (pandas, numpy, matplotlib, seaborn)
- Scikit-learn (Linear Models, Preprocessing, Metrics)
- XGBoost

---

## 🗂️ 데이터 개요

- **데이터 출처**: Dubizzle 중고차 시세 데이터셋
- **주요 컬럼**:
  - `price_in_aed` (타겟)
  - `year`, `kilometers`, `fuel_type`, `transmission`, 등 총 15개 특성
- **전처리 과정**:
  - `price_in_aed` 이상치는 **중앙값으로 대체**
  - `year`, `kilometers`는 **IQR 기준 이상치 제거**
  - 문자열 변수는 **Label Encoding** 처리
  - 수치형 변수만을 대상으로 상관관계 분석 진행

---

## 🔧 향후 개선 방향

- 다항회귀는 고차항으로 인한 과적합 위험 존재 → **교차검증 및 정규화 Ridge 적용 고려**
- **XGBoost 튜닝**을 통한 성능 향상 시도
  - `max_depth`, `learning_rate`, `n_estimators` 등 조정
- 모델 앙상블 또는 Stacking 기법 도입 가능성 검토
- SHAP 또는 Permutation Importance 기반 **피처 중요도 분석**


