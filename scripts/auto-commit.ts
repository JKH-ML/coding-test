import "dotenv/config";
import { $ } from "bun";
import { GoogleGenAI } from "@google/genai";

const apiKey = process.env.GEMINI_API_KEY;

if (!apiKey) {
  console.error("GEMINI_API_KEY가 설정되지 않았습니다.");
  process.exit(1);
}

const ai = new GoogleGenAI({ apiKey });

async function main() {
  // 1. 스테이징된 변경사항 확인
  const diff = await $`git diff --staged`.text();

  if (!diff.trim()) {
    console.log("스테이징된 변경사항이 없습니다.");
    return;
  }

  // 2. 프롬프트 구성
  const prompt = `
다음 git diff를 분석해서 한 줄 커밋 메시지를 작성해줘.
변경사항은 개인 학습 기록이다.
자연스러운 한국어로 작성해줘.

git diff:
${diff}
`;

  // 3. Gemini SDK 호출
  let message: string | undefined;

  try {
    const result = await ai.models.generateContent({
      model: "gemini-2.5-flash",
      contents: prompt,
    });

    message = result.text?.trim();
  } catch (err) {
    console.error("Gemini API 호출 실패");
    console.error(err);
    return;
  }

  if (!message) {
    console.error("커밋 메시지 생성 실패");
    return;
  }

  console.log("생성된 커밋 메시지:", message);

  // 4. commit 성공 시에만 push
  try {
    await $`git commit -m ${message}`;
    console.log("커밋 성공");

    await $`git push`;
    console.log("푸시 성공");
  } catch (err) {
    console.error("Git 명령 실패. push는 실행되지 않음.");
    console.error(err);
  }
}

main();
