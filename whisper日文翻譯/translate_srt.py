from deep_translator import GoogleTranslator
import os

now_path = r"C:\Users\user\Desktop\python_output\whisper_reading"

class translate_srt:
    def __init__(self) -> None:
        self.srt_num = "GTO_11"

    def translate_srt(self,input_srt_path, output_srt_path, dest_lang='zh-TW'):
        translator = GoogleTranslator(source='auto', target=dest_lang)
        
        with open(input_srt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(output_srt_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.strip().replace(',', '').replace(':', '').isdigit() or '-->' in line:
                    f.write(line)
                elif line.strip():
                    try:
                        translated = translator.translate(line.strip())
                        print(translated)
       
                        if translated is None:
                            print(f"Translation returned None for line: {line.strip()}")
    
                            f.write(line.strip() + '\n')
                        else:
                            f.write(translated + '\n')
                    except Exception as e:
                        print(f"Error translating line: {line.strip()}. Error: {e}")

                        f.write(line.strip() + '\n')
                else:
                    f.write('\n')
def main():
    ts=translate_srt()
    new_dir = os.path.join(now_path,ts.srt_num)
    os.chdir(new_dir)
    
    ts.translate_srt('merged_subtitles.srt', 'translated_output.srt')

if __name__ == "__main__":
    main()