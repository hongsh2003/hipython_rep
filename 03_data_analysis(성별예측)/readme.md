# 🧠 성별 예측 분류 모델 프로젝트

이 프로젝트는 고객 데이터를 기반으로 성별(Gender)을 예측하기 위한 다양한 머신러닝 분류 모델을 구현하고 비교 분석하는 데 목적이 있습니다.

<br/>

## 📁 프로젝트 구조


<br/>

## 📊 사용 데이터

- 주요 변수:
  - `주구매상품`
  - `주구매지점`
  - `나이`, `구매횟수`, `구매금액` 등
- 목표 변수:
  - `성별` (0: 남성, 1: 여성)

<br/>

## 🔧 사용 모델

| 모델 | 라이브러리 |
|------|------------|
| Logistic Regression | scikit-learn |
| Decision Tree | scikit-learn |
| Random Forest | scikit-learn |
| XGBoost | xgboost |

<br/>

## 📈 성능 비교 (F1 기준)

| Model               | Accuracy | Precision | Recall | F1 Score |
|--------------------|----------|-----------|--------|----------|
| Random Forest       | 0.6357   | 0.6181    | 0.6357 | **0.5981** |
| XGBoost             | 0.6071   | 0.5912    | 0.6071 | 0.5929 |
| Decision Tree       | 0.5286   | 0.5298    | 0.5286 | 0.5292 |
| Logistic Regression | 0.6200   | 0.6042    | 0.6200 | 0.5256 |

✔️ **결론**: 랜덤 포레스트 모델이 가장 높은 F1 점수를 기록하여 성별 예측에 가장 적합한 모델로 확인되었습니다.

<br/>

## 🧪 주요 코드 기능

- 데이터 전처리 및 결측치 처리
- Label Encoding & Feature Scaling
- 훈련/테스트 데이터 분리
- 각 모델 훈련 및 예측
- 성능 지표 평가 (`accuracy`, `precision`, `recall`, `f1-score`, `confusion matrix`)
- 모델별 성능 비교 테이블 시각화

<br/>

## 🛠️ 설치 환경

```bash
pip install pandas scikit-learn xgboost matplotlib seaborn

