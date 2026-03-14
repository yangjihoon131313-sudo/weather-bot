import requests
import telepot

# 1. 설정 (8692840932:AAFqdNYzSnkS55yfCU6MIc9Oqj5X0kBPFSc)
bot = telepot.Bot('8692840932:AAFqdNYzSnkS55yfCU6MIc9Oqj5X0kBPFSc')
my_id = '8729807039'
api_key = 'b9ac19b181505ee88113611052e4c242'

# 2. 데이터 가져오기
lat, lon = 37.5665, 126.9780
weather_res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=kr').json()
air_res = requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}').json()

# 3. 날씨 정보 추출
temp = weather_res['main']['temp']
desc = weather_res['weather'][0]['description']
pm10 = air_res['list'][0]['components']['pm10']

# 4. 미세먼지 등급 판별
if pm10 <= 30: pm_grade = "좋음"
elif pm10 <= 80: pm_grade = "보통"
elif pm10 <= 150: pm_grade = "나쁨"
else: pm_grade = "매우 나쁨"

# 5. [추가된 부분] 기온별 옷차림 추천
if temp >= 28: outfit = "민소매, 반팔, 반바지 (시원한 소재)"
elif temp >= 23: outfit = "반팔, 얇은 셔츠, 면바지"
elif temp >= 20: outfit = "얇은 가디건, 긴팔 티셔츠, 면바지"
elif temp >= 17: outfit = "니트, 맨투맨, 청바지"
elif temp >= 12: outfit = "재킷, 가디건, 트렌치코트"
elif temp >= 9: outfit = "코트, 가죽 재킷, 야상"
elif temp >= 5: outfit = "울 코트, 두꺼운 니트, 스카프"
else: outfit = "패딩, 두꺼운 코트, 목도리, 장갑"

# 6. 최종 메시지 구성
msg = (
    f"☀️ [서울 날씨 비서]\n"
    f"━━━━━━━━━━━━━━\n"
    f"☁️ 날씨: {desc}\n"
    f"🌡 현재 기온: {temp}°C\n"
    f"😷 미세먼지: {pm_grade}\n"
    f"👕 추천 옷차림: {outfit}\n"
    f"━━━━━━━━━━━━━━"
)

bot.sendMessage(my_id, msg)