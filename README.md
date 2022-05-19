# 데이터베이스 팀 프로젝트

- 기간 : 2022.03 ~ 2022.05
- 주제 : COVID-19 기간 동안의 트위터 이용자들의 기록의 감성분석 모델별 분석 후 결과값 비교

- 팀원 : 박영준, 김종백, 김신호
- 트위터 데이터 크롤링
    - 2020.01.01~2022.04.18일까지의 COVID-19 관련 키워드에 해당하는 트윗 데이터 수집
    - 관련 키워드 목록 : [ 'Social distance', 'COVID',  'Fomite', 'Pandemic', 'Community spread',
        'Contact tracing', 'Epidemic', 'Outbreak', 'Martial law', 'Self-quarantine', 'Index case', 'Super-spreader','Isolation','Self-isolation', 'Contagious', 'Infectious', 'Virus' ]
- 전처리
    - 트윗 데이터의 특수문자, 영어 이외의 이모지, 긴 반복문, 하이퍼링크, 짧은 단어, stopword 제거
- EDA
    - 2020~2022년의 각 년도별 및 전체 기간 동안의 단어 빈도수 확인 및 리뷰 길이 확인
- 감성분석
    - Sentiwordnet
    - Vader
    - SenticNet
- 시각화
    - Wordcloud
    - network analysis

