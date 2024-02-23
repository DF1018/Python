import datetime
import os
import openai
import subprocess
import time

# 更改当前工作目录
now_path = r"C:\Users\user\Desktop\python_output\whisper_reading"
os.chdir(now_path)
openai.api_key = ""


class whisper_openai:
    def __init__(self):
        self.video_name = "GTO_12.mp4"
        self.start_seconds = 0
        self.end_seconds = 90
        self.segment_duration = 90
     
    def get_audio_duration(self,file_path):
        command = [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            file_path
        ]
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        duration = float(result.stdout)
        return duration

    # 将秒转换为时分秒格式
    def seconds_to_time_str(self,seconds):
        return str(datetime.timedelta(seconds=seconds))

    def cut_video(self,video_name:str,start_seconds_str:str,end_seconds_str:str,output_path:str) -> None:
        command = [
            "ffmpeg",
            "-i",video_name,
            "-ss",start_seconds_str,
            "-to",end_seconds_str,
            "-vn","-acodec", "pcm_s16le","-ar","44100","-ac","2",
            output_path
        ]
        subprocess.run(command, shell=True)
        
    
    def whisper_main(self,input_wav)-> str:
        video_file = open(input_wav, "rb")
        transcript = openai.Audio.transcribe("whisper-1", video_file, response_format="srt")
        video_file.close()
        return transcript

def main():
    wo=whisper_openai()

    start_seconds=wo.start_seconds
    end_seconds=wo.end_seconds
    
    wo=whisper_openai()
    video_name_basename =  os.path.splitext(wo.video_name)[0]
    
    if os.path.isdir(video_name_basename):
        print("目錄存在。")
    else:
        print("目錄不存在。")
        os.makedirs(video_name_basename)
    
    total_duration_seconds = wo.get_audio_duration(wo.video_name)
    print(total_duration_seconds)

    segment_index = 0
    while start_seconds < total_duration_seconds:
        # 转换秒为时分秒格式
        start_time_str = wo.seconds_to_time_str(start_seconds)
        end_time_str = wo.seconds_to_time_str(min(end_seconds, total_duration_seconds))
        
        output_filename = f"output_whisper_{segment_index}"
        output_wav_path=f"{video_name_basename}/{output_filename}.wav"
        output_srt_path = f"{video_name_basename}/{video_name_basename}+{output_filename}.srt"
        
        wo.cut_video(wo.video_name,start_seconds_str=start_time_str,end_seconds_str=end_time_str,output_path=output_wav_path)
        print(output_wav_path)
        
        transcript=wo.whisper_main(output_wav_path)
        
        srt_file = open(output_srt_path,"a+",encoding='utf-8')
        srt_file.write(transcript)
        os.remove(output_wav_path)
        
        start_seconds += wo.segment_duration
        end_seconds += wo.segment_duration
        segment_index += 1

        print("whisper讀取完成")
        
    
        
if __name__ == "__main__":
    main()