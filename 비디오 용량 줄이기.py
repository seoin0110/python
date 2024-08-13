from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np
# 원본 비디오 파일 경로
input_path = "E07.240620.720p-NEXT.mp4"
# 출력 비디오 파일 경로
output_path = "E07.mp4"

# 비디오 클립 로드
clip = VideoFileClip(input_path)

# 비디오 출력 옵션 설정
bitrate = "500k"  # 원하는 비트레이트 설정

# 출력 파일로 저장
clip.write_videofile(output_path, codec="libx264", audio_codec="aac", bitrate=bitrate)
