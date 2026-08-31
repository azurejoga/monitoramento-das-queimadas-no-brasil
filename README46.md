# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 253f6caa-571e-3515-bc72-d3d910bdf64c | -9.05792 | -65.42416 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f6385a0-60b6-311a-89b8-95db920b6e40 | -13.97254 | -54.40298 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5f2b07bd-29cc-3513-882d-1a2257b9b60f | -14.23421 | -52.85374 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1cd41b36-8927-3ee7-8020-cddc65fa9f97 | -10.13084 | -45.73659 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f431e69c-4e84-3f38-86aa-eaa3806af84d | -11.19279 | -53.99324 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66502859-1e8d-3563-8f97-bbb53b83d35d | -14.58405 | -54.10388 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 820e4e38-f233-3e4a-b44d-23bdaa5d0696 | -14.98307 | -48.15417 | 2026-08-31 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4dd87d72-6f0e-3e1a-86a7-82513ca644c2 | -11.2312 | -45.09855 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7eea6ed9-45a6-3065-8848-310f6748ddea | -9.14775 | -61.09884 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86b93cbb-239c-3afd-8986-3010c67f9674 | -11.51725 | -46.94554 | 2026-08-31 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dcc5781-db57-32f4-898d-d3d03b0ffda5 | -12.13451 | -47.22859 | 2026-08-31 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa556502-97ed-3d3a-b3c4-1be1dd8c6501 | -8.58968 | -66.97096 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 886d959d-b0cb-357e-ad25-590cc63503e9 | -9.17721 | -59.63451 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 333b8fb2-6af7-3887-8669-c51a80fa4d58 | -13.93642 | -54.41254 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 181c5eac-8200-3cf8-ab7e-4ed0c2f186d7 | -10.76273 | -50.85248 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f95bb961-eee9-3f1d-b0f0-f9b0fcd561e0 | -9.00146 | -65.439 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88ee1b19-d364-352f-a70f-fc6bd4f0ca24 | -8.9551 | -62.36933 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9504a631-ad99-344c-8c34-9fc4295a5e53 | -11.33128 | -45.19903 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b39b8277-fd5c-38bd-870b-9a2c62a07f8b | -11.21451 | -45.0919 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8757cb9f-fe39-35ac-a5e4-84a7cd4946a4 | -11.47888 | -58.51198 | 2026-08-31 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f1d9cf93-e319-39c1-9490-fcf8539a0a23 | -10.04708 | -48.67353 | 2026-08-31 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d58be722-3a68-3fbb-8e85-3c7bc8ed238b | -12.17751 | -50.5309 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea3af67b-5ef5-390e-8c8a-b3d6c1f9ad5e | -10.79817 | -50.51413 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 885176ba-e1e0-3963-8551-295449040d22 | -10.49638 | -59.60835 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff759de2-94fb-3d7e-8fba-1d0320576a38 | -12.90101 | -45.8422 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b55e66ab-7cc2-3a43-89f7-662afb9aec87 | -11.37377 | -45.1838 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe8b051e-5495-366c-830a-3d1be37077ef | -9.14271 | -61.10225 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 046d0e53-ed50-3b62-8d7b-5c7f18bb9e27 | -8.14827 | -63.99891 | 2026-08-31 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb8159c3-6b07-3ef8-bf3c-9c5b6bef57c3 | -11.32908 | -45.16902 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e5bb2f7-0256-36af-b0c4-f0f77f43ac9a | -14.14315 | -52.81136 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7bb889a-eb76-3b78-abb5-ea0c5e21672c | -9.40312 | -51.61143 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69543026-f887-3c49-bfc2-6d5baedccb6a | -9.2106 | -59.55596 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dabbe77-3076-3ab3-9fd1-70c0d2283176 | -10.84058 | -48.34311 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 58be8eb2-07d7-335d-b0af-9f6e28bc55d4 | -14.60066 | -54.11054 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f7e0d5e2-37c1-3ee5-a451-65458270f289 | -9.93743 | -60.51262 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80de8648-641b-39b9-9532-a965595eae0a | -11.88451 | -45.81675 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 309aee8f-e33c-34d4-988f-8027fdda463c | -12.39581 | -46.45075 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 972f4518-aefa-3733-88a4-b381b76fa75b | -10.14169 | -45.70795 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a49d6b7-afe8-331e-97bc-d6b1d0ea8468 | -9.8495 | -64.99112 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b17e1b8d-3ae1-3515-b77c-bca0ff3b6bd3 | -9.21478 | -59.40657 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ecc24320-4099-33b5-b03a-e048a6e411fa | -14.23784 | -52.85426 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99a622c4-46a0-3e40-9631-ea005e339890 | -8.71342 | -52.36745 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1aa365e-b538-384a-a9d9-11ad81ef29c7 | -11.92666 | -45.06225 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81d7859d-9c52-3452-ab29-dbbc88149c33 | -13.43129 | -57.06413 | 2026-08-31 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 246c5072-3bc5-3186-8d24-dd179377b86a | -9.80404 | -46.43885 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6c59ec1-7f6a-3b88-b730-2a595f9c1310 | -15.66448 | -45.91559 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 51242dcb-0f8a-3b29-8cae-8f2c60e53117 | -12.09868 | -45.05548 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c7bf12d-5e08-3af7-8165-320ed8100d27 | -9.15225 | -59.54278 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26ea7a94-0da9-3e3a-9327-212ffc6427c6 | -8.5598 | -54.78914 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd9394fe-248b-3797-96ce-2474072f2e7f | -14.58342 | -54.0842 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 402251b5-5fe3-3513-bd04-b441eafe74b8 | -11.49965 | -50.3288 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2803c6dc-a15b-3605-8c1c-1340394e0591 | -9.96586 | -46.31159 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20b4621c-1b35-3b4f-80ad-2fc42f01a896 | -9.01009 | -60.59497 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5850b67c-e509-3a73-b7b7-d3fd33f69016 | -9.15623 | -59.37662 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a7e957b-7470-37dd-8c37-6530b99d6c23 | -7.44022 | -61.42834 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca21a9f2-fb58-3572-882d-66176428a722 | -11.03098 | -57.24073 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45ce8932-2210-35f5-a799-cb482b5cac97 | -14.46884 | -53.35652 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b5a7dd5-f5da-3762-add3-3195b61e3b0b | -14.22756 | -52.84854 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4a2e767-cf89-3d42-9232-d4933e0eaca2 | -11.0406 | -57.24615 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c87c4b01-57c1-34df-8792-86f3485691e8 | -9.20325 | -51.57214 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83879479-f58b-320f-bed8-4bc094e6ad98 | -14.16136 | -52.78781 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 077d9291-e2e1-3c50-af45-5ce817c4098c | -10.16058 | -45.73406 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c040780a-b42c-3136-b28f-f30fd7a44199 | -11.33335 | -45.18188 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edc237e7-583e-323e-9569-740f620e29e2 | -10.75645 | -54.00466 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ef51079-7852-3bf0-b832-3d9732e1cb87 | -11.33234 | -45.19027 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c87b64be-9a7a-33c9-8be2-8dd9e9cf99f7 | -14.46236 | -53.35124 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9be336d8-0d06-3fff-92c3-83ed38e968de | -10.8342 | -45.31339 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c42a176d-d0e2-3ce8-83f7-5f6ed3001b6f | -9.15699 | -59.53844 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70184b39-31fe-3bdb-a23c-10fa59560896 | -10.54529 | -46.2071 | 2026-08-31 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b3159aa-d8f9-3188-bbe6-dceaba42aa21 | -11.36755 | -45.18712 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6f1ae26-a056-3c6f-8efb-e92f1d7f7e97 | -9.72269 | -64.99831 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db285ced-aa9e-38d0-b827-70ebb7ea0d29 | -14.44498 | -52.52356 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 012940ff-8d28-3e41-861d-9c0a5bd94f13 | -11.92614 | -45.06684 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b5455d8-bda1-3422-9b94-3de06b646fe9 | -15.20192 | -46.23217 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8f39eea-3a8d-3323-97da-862ccf58705b | -10.80109 | -50.50264 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee71567e-d875-3dc8-98a5-52475d5e3d46 | -14.29643 | -52.89227 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d4fc155-16cb-3d85-9866-2439cf5a7a0d | -11.23881 | -45.1321 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3746867-64aa-3032-bd4b-eb2a4e329796 | -10.74037 | -54.04284 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6064c5e7-0fe7-342c-b54f-d47ec834c2ca | -14.59434 | -54.10565 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 988cedf1-c3ac-3a39-82a9-45570a800547 | -10.75591 | -54.00827 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88eef969-4a8f-3870-9430-8dd1fb44fff8 | -9.22283 | -59.57843 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69e2e053-7e0b-3360-bd28-5ad172b14a81 | -11.34733 | -61.55207 | 2026-08-31 04:59:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fdf5426-2d73-396a-8308-eb1c9c1c0630 | -11.18355 | -55.10012 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 294923c7-2e94-3c93-9d5c-9b66112f6769 | -9.85643 | -64.98478 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8e7f157-a90b-3ce0-8b51-5f72e07041f5 | -11.18301 | -55.10362 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6346e331-d837-3c18-b784-3b89252c7641 | -8.97125 | -62.38792 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 90ce590b-e42f-315a-92bb-0ba2dd309648 | -7.44733 | -60.74077 | 2026-08-31 04:59:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a20d5801-3eaa-3916-b876-e6a8a53a7136 | -7.60676 | -61.36917 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| dcc4c25e-7708-35f1-814b-f7614634f1d1 | -14.4663 | -52.19712 | 2026-08-31 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c985ac57-f653-39a9-a909-8650fe5dec5a | -9.59605 | -60.52631 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcbe7f30-7650-3d6b-aa65-4bcff11d4bfa | -8.09064 | -63.83861 | 2026-08-31 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e30af0e-9fce-35d9-bba5-700f0c9bc6aa | -14.4632 | -52.19189 | 2026-08-31 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5900bb1f-05b6-32e7-abea-f7130562e7e7 | -11.32763 | -45.18112 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a8b5234-1fa8-3ce5-b2a0-410250d5d678 | -9.89097 | -60.27197 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4f5422d2-eed2-3c2f-851e-246700aa5335 | -8.67902 | -66.52193 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c3287998-766f-3299-9cf9-ce282dcd78c2 | -13.46832 | -51.40881 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4f4e4ad5-e01f-3be5-8976-1050e0ccc126 | -9.929 | -60.48829 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30540edd-2f0b-31e3-8023-18afa9cc3715 | -9.48856 | -66.63056 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 247c85b6-99a4-348f-8e7a-05f6de0d85c7 | -14.39148 | -52.56323 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63cbc527-1b28-3995-a4cb-bcf358abddf3 | -9.17163 | -56.98618 | 2026-08-31 04:59:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README47.md)
