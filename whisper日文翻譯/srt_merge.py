import datetime
import os

now_path = r"C:\Users\user\Desktop\python_output\whisper_reading"

class srt_merge:
    def __init__(self) -> None:
        self.srt_num = "GTO_11"
        self.total_segments = 37  
        self.segment_duration = 90  
        
    def adjust_srt_time(self,srt_text, offset_seconds):
        new_srt = ""
        for line in srt_text.splitlines():
            if "-->" in line:
                start_time_str, end_time_str = line.split(" --> ")
                start_time = datetime.datetime.strptime(start_time_str, "%H:%M:%S,%f")
                end_time = datetime.datetime.strptime(end_time_str, "%H:%M:%S,%f")
                
                new_start_time = start_time + datetime.timedelta(seconds=offset_seconds)
                new_end_time = end_time + datetime.timedelta(seconds=offset_seconds)
                
                new_line = "{} --> {}".format(new_start_time.strftime("%H:%M:%S,%f")[:-3], new_end_time.strftime("%H:%M:%S,%f")[:-3])
                new_srt += new_line + "\n"
            else:
                new_srt += line + "\n"
        return new_srt
    
def main():
    sm=srt_merge()
    
    new_dir=os.path.join(now_path,sm.srt_num)
    os.chdir(new_dir)
    
    total_segments = sm.total_segments  
    segment_duration = sm.segment_duration  
    
    merged_srt_content = ""
    for i in range(total_segments+1):
        with open(f"{sm.srt_num}+output_whisper_{i}.srt", "r", encoding="utf-8") as srt_file:
            srt_content = srt_file.read()

            adjusted_srt = sm.adjust_srt_time(srt_content, i * segment_duration)
            merged_srt_content += adjusted_srt

    with open("merged_subtitles.srt", "w", encoding="utf-8") as merged_srt_file:
        merged_srt_file.write(merged_srt_content)

        
if __name__ == "__main__":
    main()