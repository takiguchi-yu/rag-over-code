## Embeddings

Vector Store に任意のソースコードを Embedding します。

### LLM ダウンロード

Hugging Face から CodeLlama をダウンロードします。

```sh
wget https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF/resolve/main/codellama-13b-instruct.Q4_K_M.gguf
```

### 参考ページ

- https://qiita.com/mohki7/items/f485df92af79bad7ab07#augmented-language-models
- https://qiita.com/takeo-furukubo/items/e5d43fa734e4338b895f
- https://qiita.com/utanesuke/items/6efc03eca94f7de3b9cd
- https://python.langchain.com/docs/use_cases/code_understanding
- https://python.langchain.com/docs/modules/data_connection/document_transformers/code_splitter
- https://python.langchain.com/docs/integrations/vectorstores/chroma
- https://fintan.jp/page/10301/
- https://github.com/cristobalcl/LearningLangChain/blob/master/notebooks/04%20-%20QA%20with%20code.ipynb
- https://blog.gopenai.com/nlp-embeddings-embedding-models-and-comparison-86d28b547d64
