# Swarm manage v1 : Web을 통한 도커 관리 서비스
Swarm manage v1은 도커스웜 클러스터 환경에서 웹을 통해 도커를 편리하게 관리할 수 있는 서비스 입니다. <br/>  
[데모영상](https://youtu.be/SJI4mX-b7ug)<br/>
![mainpage]()

## 기술 스택
- Infra : Docker Swarm Mode
- BE : Django
- FE : HTML, CSS, JS
- Monitoring : Prometheus, Grafana

## 구현 기능
- 스택
  * 스택 생성
  + 스택 리스트 조회
  + 스택 상세정보 조회
  + 스택 삭제
- 서비스
  * 서비스 리스트 조회
  + 서비스 상세정보 조회
  + 이미지 업데이트
  + 스케일 조정
  + 서비스 롤백
- 네트워크
  * 네트워크 생성
  + 네트워크 리스트 조회
  + 네트워크 상세정보 조회
  + 네트워크 삭제
- 볼륨
  * 볼륨 생성
  + 볼륨 리스트 조회
  + 볼륨 상세정보 조회
  + 볼륨 삭제
- 로그인
  * 도커허브 로그인
- 모니터링
  * 스웜클러스터 노드의 CPU, 메모리 사용량 확인
  
## 시스템 아키텍처
![system]()

