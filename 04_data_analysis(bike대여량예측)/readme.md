
---

## 📊 사용 데이터

- **컬럼 예시**:
  - `hour`, `temperature`, `humidity`, `windspeed`
  - `season`, `holiday`, `workingday`, `weather` 등
  - `count`: 대여량 (예측 대상)

---

## 🧪 사용한 모델

| 모델                | 특징                           |
|---------------------|--------------------------------|
| Linear Regression   | 기본 선형 회귀                 |
| Ridge               | L2 정규화                      |
| Lasso               | L1 정규화 및 변수 선택         |
| ElasticNet          | L1 + L2 혼합                   |
| Random Forest       | 트리 기반 앙상블 모델          |
| Polynomial Regression | 비선형 모델 확장 (다항회귀) |

---

## 🧼 전처리 및 특징

- **결측치 처리**: 평균값 대체 (`bmi` 등)
- **스케일링**: `StandardScaler` 사용
- **문자형 변수 인코딩**: `LabelEncoder`, `get_dummies` 등
- **교차 검증**: `RidgeCV`, `LassoCV`, `ElasticNetCV`, `cross_val_score` 사용

---

## 📈 성능 평가 지표

- **RMSE (Root Mean Squared Error)**
- **R² (결정계수)**

```python
from sklearn.metrics import mean_squared_error, r2_score

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
