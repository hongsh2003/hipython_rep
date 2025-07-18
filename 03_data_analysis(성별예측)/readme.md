# 🧠 성별 예측 분류 모델 프로젝트

이 프로젝트는 고객 데이터를 기반으로 성별(Gender)을 예측하기 위한 다양한 머신러닝 분류 모델을 구현하고 비교 분석하였습니다.

<br/>

## 📊 사용 데이터

- 변수:
  - `총구매액`
  - `최대구매액`
  - `환불금액`
  - `주구매상품`
  - `주구매지점`
  - `내점일수`
  - `내점당구매건수`
  - `주말방문비율`
  - `구매주기`
- 목표 변수:
  - `성별` (0: 여성, 1: 남성)

<br/>

## 🔧 사용 모델

| 모델 | 라이브러리 |
|------|------------|
| Logistic Regression | scikit-learn |
| Decision Tree | scikit-learn |
| Random Forest | scikit-learn |
| XGBoost | xgboost |

<br/>


## 🧪 주요 코드 기능

- 데이터 전처리 및 결측치 처리
- Label Encoding & Feature Scaling
- 훈련/테스트 데이터 분리
- 각 모델 훈련 및 예측
- 성능 지표 평가 (`accuracy`, `precision`, `recall`, `f1-score`, `confusion matrix`)
- 모델별 성능 비교 테이블 시각화

<br/>


