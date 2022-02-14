### MLflow

#### Experiment 생성
```
mlflow experiments create --experiment-name my-first-experiment
```

- [결과] 해당 폴더에 mlruns 폴더 생성

#### Experiment 리스트 확인
```
mlflow experiments list
```
- [필수] MLProject 파일 생성

#### Experiment Run
```
mlflow run logistic_regression --experiment-name my-first-experiment --no-conda
```

#### UI 실행(MLflow 로컬 5000번 포트로 띄우기)
```
mlflow ui
```

#### autolog 적용
```
mlflow run logistic_regression_with_autolog --experiment-name my-first-experiment --no-conda
```

#### parameter 적용
```
mlflow run logistic_regression_with_autolog_and_param --experiment-name my-first-experiment --no-conda
```

#### hyperparameter tuning
```
mlflow run svc_with_hyperparams_tuning --experiment-name my-first-experiment --no-conda
```

#### mlflow 서버로 배포하기
- mlflow server 명령어로 Backend Store URI 지정
```
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root $(pwd)/artifacts
```
- 환경변수 지정
```
export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
```
- Experiments 생성 및 Run
```
mlflow experiments create --experiment-name my-experiment
```
```
mlflow run svm --experiment-name my-experiment --no-conda
```
