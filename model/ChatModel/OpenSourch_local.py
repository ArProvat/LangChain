from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['hf_home'] = r'D:\CSE'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        max_new_tokens=128,
        temperature=0.5
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Tell about CSE.")
print(result.content)
