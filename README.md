# Sales bot
## NOTE
This repo is just a quick POC developed in a few hours and needs a lot more work.

### Tools and Technologies
* [Langchain](https://github.com/hwchase17/langchain/blob/master/docs/getting_started/getting_started.md)
* [Bloom LLM](https://huggingface.co/bigscience/bloom)
* [Streamlit](https://streamlit.io/)

### Context and Inputs
* Bundles available on https://www.dynamicmath.ca/pricing were scraped and given to the model as input
* The model was provided with context including bundle name, price, access, number of videos, min and max grades, and more.
```
Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

bundle_name: 6-month
Price: $49.95
marketing_tag_line: Great value
Access: lifetime
no_of_videos: 450
min_grade: 4
max_grade: 10
dynamic_math_book_included: no
has_special_price_for_extra_books: no
access_to_new_resources: yes
is_curriculum_aligned: yes

bundle_name: Complete
Price: $99.00
marketing_tag_line: Best value
Access: 1 year
no_of_videos: 450
min_grade: 4
max_grade: 10
dynamic_math_book_included: yes
has_special_price_for_extra_books: yes
access_to_new_resources: yes
is_curriculum_aligned: yes

bundle_name: monthly
Price: $9.95
marketing_tag_line: Flexible, afforadable
Access: lifetime
no_of_videos: 450
min_grade: 4
max_grade: 10
dynamic_math_book_included: No
has_special_price_for_extra_books: no
access_to_new_resources: yes
is_curriculum_aligned: yes

bundle_name: annual
Price: $79.95
marketing_tag_line: Most popular
Access: lifetime
no_of_videos: 450
min_grade: 4
max_grade: 10
dynamic_math_book_included: no
has_special_price_for_extra_books: no
access_to_new_resources: yes
is_curriculum_aligned: yes
```

### Model Performance
* The open source LLM model, Bloom did not perform as well as more sophisticated models.
* Future work includes testing the model with ChatGPT and enhancing prompts through prompt engineering.

### Sales Process
* The salesbot is designed to help potential customers buy one of the bundles
* The bot uses the AI model to answer questions and provide information on the available bundles

### App
<img width="513" alt="Screenshot 2023-05-12 at 3 22 30 PM" src="https://github.com/praneethys/marketing-chatbot/assets/61710414/83fd764e-c963-4c21-8061-c698cbf3854b">



