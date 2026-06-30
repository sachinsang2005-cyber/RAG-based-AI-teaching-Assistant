import whisper
import os

# print(whisper.__file__)
# print("Module:", whisper)
# print("File:", getattr(whisper, "__file__", "No file"))
# print("Attributes:", dir(whisper))


model=whisper.load_model("base")
files = os.listdir("audios")

for file in files:
    result=model.transcribe(f"audios/{file}")
    print(result["text"])



    # result = model.transcribe(
    # f"audios/{file}",
    # language="hi",
    # task="translate")