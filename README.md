# mysummary
Leitura de documentos e resumo de documentos

## Análise dos documentos de um processo

Processo público disponível em https://www.sipac.ufpi.br/public/jsp/processos/processo_detalhado.jsf?id=594067

O referido processo pussui 27 arquivos (pdf ou html) relacionados ao processo. 

Anexos em pdf ou despachos em html.

Exemplo de [dados de um processo](https://github.com/armandossrecife/mysummary/blob/main/extrair_informacoes_protocolo.ipynb)

Exemplo de [Extrator de Dados de Processos](https://github.com/armandossrecife/mysummary/blob/main/extrator_dados_processos.ipynb) 

## Possíveis Soluções

1. Usando a API do Google Gemini (limitações financeiras): [S1](https://github.com/armandossrecife/mysummary/blob/main/quick_process_text_summary.ipynb)
2. Abordagem mista (API do Google Gemini + Transformers): [S2](https://github.com/armandossrecife/mysummary/blob/main/quick_process_text_summary_using_transformers.ipynb)
3. Usando apenas o Transformers (Open source): [S3](https://github.com/armandossrecife/mysummary/blob/main/text_summary_only_transformers.ipynb)

## Conceitos, Métodos, Técnicas e Ferramentas

[Transformers](https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)) By [Hugging Face](https://huggingface.co/) - a biblioteca Transformers é um acervo em Python que contém implementações de código aberto de modelos de transformadores para tarefas de texto, imagem e áudio. É compatível com as bibliotecas de aprendizagem profunda [PyTorch](https://en.wikipedia.org/wiki/PyTorch) e [TensorFlow](https://en.wikipedia.org/wiki/TensorFlow) e inclui implementações de modelos notáveis como [BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) e [GPT-2](https://en.wikipedia.org/wiki/GPT-2).

Mais sobre a biblioteca Transformers em [link](https://huggingface.co/docs/transformers/en/index)

[Summarization](https://huggingface.co/tasks/summarization)

[Summarization Models](https://huggingface.co/models?pipeline_tag=summarization)

Uso do [summarization](https://huggingface.co/docs/transformers/en/tasks/summarization) para fazer o resumo de textos em inglês.

[text_summarization](https://huggingface.co/Falconsai/text_summarization)
