from booksummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline
from booksummarizer.components.data_transformation import convert_examples_to_features

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
    def transform_data(self,text,page):
        processed_text=convert_to_pages(text)
        pages=[]
        for j in processed_text:
            pages.append(j.split[0])
        return pages[page[0]-1:page[1]]

    
    def predict(self,text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}

        pipe = pipeline("summarization", model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output