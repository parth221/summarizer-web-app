from django.shortcuts import render
from transformers import AutoTokenizer, AutoModelWithLMHead
tokenizer = AutoTokenizer.from_pretrained("t5-small")
model = AutoModelWithLMHead.from_pretrained("t5-small")

# Create your views here.
def index(request):
    return render(request, 'index.html')
def services(request):
    if request.method == 'POST':
        text = request.FILES['myfile'].read()
        text = str(text)
        text =''.join(x for x in text if ord(x) < 128)
        preprocess_text = text.strip().replace("\n", "")
        tokenized_text = tokenizer.encode(preprocess_text, return_tensors="pt")

        summary_ids = model.generate(
            tokenized_text,
            max_length=400,
            num_beams=2,
            repetition_penalty=2.5,
            length_penalty=1.0,
            early_stopping=False
        )

        output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return render(request, 'results.html', {"data": output})
    return render(request, 'services.html')

def result_sum(request):
    return render(request,'results.html')