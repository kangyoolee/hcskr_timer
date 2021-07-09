#비동기 처리
import asyncio
import hcskr
async def main():
    await hcskr.asyncSelfCheck("이름","생년월일","지역","학교이름","학교종류","비밀번호(숫자4자리)")
asyncio.get_event_loop().run_until_complete(main())