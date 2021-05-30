# SMCC
핵심 xhr파일이 url로 response되고 url의 값이변화되는 규칙이있다.<br>X주차 수업, Y번째 문제로 한다면<br>
```
https://www.scholars.kr/pc/dictation_play_data.php?bookno=XXXX&bpage=YYYY
``` 
이런식으로 URL을 요청이된다 URL내부는 ```json``` 형식이고 그 값을 dictionary형태로 변환
## ex)
``` json
{"etxt":"How many things do you throw away everyday?","ktxt":"","epara":"","kmean":"","filename1":"b511206442413.mp3"}
```


## 매커니즘
1. 현재 해야되는 학습이 몇주차인지알아내고 bookno에 저장
2. 학습 시작후 현재 몇번째 문제이고, 총 몇문제인지 알아냄
3. >현재문제의 답을 알아내는 함수를 총 문제의 갯수만큼 순서대로 반복 
    >>반복하면서 자동으로 변환된 dictionary에서 etxt의 값을 슬라이싱후 복사
    >>>복사한 내용을 답 칸에 자동으로 붙혀놓고 Enter키를 send하기
