import whisper
from whisper.utils import get_writer

def create_subtitles(input_video, output_format="srt"):
    # Load the model (options: 'tiny', 'base', 'small', 'medium', 'large')
    model = whisper.load_model("small.en")
    
    print("Transcribing... this might take a while.")
    result = model.transcribe(input_video)
    
    output_directory = "."
    writer = get_writer(output_format, output_directory)
    
    # Save the subtitle file
    writer(result, input_video, {"max_line_width": None, "max_line_count": None, "highlight_words": False})
    print(f"Subtitles saved as {input_video}.{output_format}")

if __name__ == "__main__":
    video_file = input("insert the video path") # Replace with your file path
    create_subtitles(video_file)