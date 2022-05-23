# 데이터베이스 팀 프로젝트

- 프로젝트 기간 : 2022.03 ~ 2022.05
- 주제 : COVID-19 기간 동안의 트위터 이용자들의 기록의 감성분석 모델별 분석 후 결과값 비교

- 팀원 : 박영준, 김종백, 김신호
- 데이터 수집 : Kaggle의 'COVID-19' All Vaccines Tweet의 데이터셋 활용
    - 기간 : 2020.12.12 ~ 2021.11.24
    - 주요 백신 : Sinopharm, Sinovac, Moderna, Oxford/Astra-Zeneca, Covaxin and Sputnik V vaccines
    - 주요 언어 : 영어
- 전처리
    - 트윗 데이터의 특수문자, 영어 이외의 이모지, 긴 반복문, 하이퍼링크, 짧은 단어, stopword 제거, 명사 추출
- EDA
    - 2020~2022년의 각 년도별 및 전체 기간 동안의 단어 빈도수 확인 및 리뷰 길이 확인
- 사용한 감성분석 모델
    - Sentiwordnet
    - Vader
    - SenticNet
- 시각화
    - Wordcloud
    - Network analysis

