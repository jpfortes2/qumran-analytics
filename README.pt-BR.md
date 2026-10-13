# Qumran Analytics — apresentação em português

**Análise computacional dos Manuscritos do Mar Morto (1QS), combinando visão computacional e reconhecimento de escrita hebraica manuscrita.**

> **Pesquisa em desenvolvimento — 13 de outubro de 2026.** O experimento de ajuste do modelo FT01_R02 foi concluído, mas a avaliação sobre o conjunto independente ainda não foi realizada.

## Objetivo

Investigar a aplicação de técnicas de pré-processamento de imagens, segmentação de linhas, organização de ground truth e reconhecimento de escrita manuscrita (HTR) ao manuscrito **Regra da Comunidade (1QS)**. O projeto combina procedimentos computacionais, documentação de proveniência e discussões de paleografia e crítica textual.

## Etapa atual

- **Treinamento:** 55 linhas, organizadas nos primeiros cinco lotes.
- **Validação principal:** quatro linhas selecionadas do sexto lote.
- **Teste reservado:** 11 linhas do sétimo lote, uma por coluna; aguardam transcrição especializada e avaliação independente.
- **Modelo:** Kraken 7.1.1 com arquitetura pré-treinada relacionada ao PP-OCRv6; experimento FT01_R02 executado por 30 épocas na GPU Tesla T4.
- **Métricas internas documentadas:** 59,18% para a avaliação do modelo inicial e 71,02% para o melhor checkpoint durante o treinamento. **Não correspondem a uma comparação confirmada de desempenho em teste independente.**

## Cuidados metodológicos

A seleção de apenas quatro linhas para validação torna a estimativa exploratória. Uma auditoria apontou regiões potencialmente sobrepostas entre treinamento e teste que ainda exigem verificação. As transcrições de treinamento foram apoiadas por materiais de referência e não equivalem a leituras paleográficas totalmente independentes.

Os materiais originais (imagens, transcrições de referência, checkpoints e pacotes de teste) não foram incluídos neste repositório público inicial para preservar direitos de uso e a integridade da avaliação.

Consulte o [README em inglês](README.md) para estrutura do código e [metodologia](docs/METHODOLOGY.md) para detalhes.
