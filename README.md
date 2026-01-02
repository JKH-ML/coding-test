### coding-test
코딩 관련 공부한 내용을 저장하고 관리하는 저장소입니다. 효율적인 관리를 위해 git 관리 자동화 기능을 넣었습니다.

### Why?
매번 커밋 메세지를 작성하고 git push를 입력하는 행위는 귀찮고, 일관된 형식을 유지하는 번거롭기 때문에 이를 자동화해서 관리합니다.

### How it works
- `bun run ac`를 입력하면  `scripts/auto-commit.ts`이 실행되고 `gemini api`를 활용해 자동으로 커밋 메세지를 생성합니다.
- 커밋 메세지 생성에 성공하면 자동으로 `git push`가 이루어져 github에 변경사항을 저장합니다.

### Reference
- [한빛미디어] 이것이 취업을 위한 코딩 테스트다 with 파이썬 (나동빈 저)
- [이코테 2021 유튜브 강의](https://www.youtube.com/playlist?list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC)
- [코딩테스트 대비 문제집](https://github.com/tony9402/baekjoon)