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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 631c7eea-ed16-3b72-a286-0cfdb446a5fe | -2.46046 | -47.81153 | 2024-10-17 03:47:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83d1d2b8-4d45-3e8e-bf84-6fa628e98e33 | -2.42816 | -48.51375 | 2024-10-17 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68e82b2c-59d4-383f-8da5-dbfd6d53d88c | -2.42142 | -48.51255 | 2024-10-17 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a3ed99e-2de0-3efd-82bf-10512ca5f6c7 | -4.35747 | -48.48801 | 2024-10-17 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ee403f1-caf5-3cd2-a2d6-5749e529b7ad | -4.35654 | -48.4933 | 2024-10-17 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bf4f2cc-012c-320c-8067-2b39b1301497 | -4.28871 | -48.6216 | 2024-10-17 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e6ca609-db1d-3448-9cb9-bc45632c2c96 | -4.2867 | -48.61964 | 2024-10-17 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e427940a-d7a5-30c1-b296-c2c01571d500 | -3.90469 | -48.33768 | 2024-10-17 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ac17c88-5e81-30bb-91fb-c8a85602f857 | -3.89814 | -48.33667 | 2024-10-17 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e81b700-587e-3357-8570-fe1a5fce7204 | -2.84214 | -49.14667 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e8a7cfc6-38bf-31af-8a5d-c1025efb291a | -2.84097 | -49.15347 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e056be8f-ed81-3f37-b009-c7d1020399ac | -2.83688 | -49.14731 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a6213675-f2a3-3bbd-a031-0413f17399b1 | -2.83575 | -49.15416 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e9b6623e-8dfa-3552-bf3a-a7e36063aa96 | -2.83524 | -49.52567 | 2024-10-17 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| abfbd23f-1131-3ab5-ada0-344fae630494 | -2.83403 | -49.15218 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b3f71b73-f6cf-3205-b589-9137d8a7cfb0 | -2.83168 | -49.52482 | 2024-10-17 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 741c5ba4-1599-3ee7-9d1a-8fa42d2922ee | -2.8281 | -49.52457 | 2024-10-17 03:47:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 47e5921a-5ada-3e0a-96f0-fd1f09b5c22f | -2.63787 | -49.27221 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5e303d2e-8cc4-3b7b-b03a-f02c528074fe | -2.63022 | -49.07556 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69202597-dd67-3d6f-b42a-f84c7d176bbf | -2.62328 | -49.07434 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3347873-be0f-3c35-8559-3c6777f94afb | -2.61416 | -49.08614 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb723521-3833-3d53-bd58-bfb476b6c9b0 | -2.61309 | -49.09258 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b3bf86-04df-3441-8810-7cea2ad20874 | -2.61256 | -49.08445 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06621d38-9594-3a05-b8eb-efce028b0e76 | -2.61181 | -49.48861 | 2024-10-17 03:47:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 69bdee48-1285-3853-9ea9-feb5fcd2e1dc | -2.61145 | -49.09085 | 2024-10-17 03:47:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b6a4246-802f-3f5b-afec-13410c2295ce | -2.60899 | -49.48485 | 2024-10-17 03:47:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bb4be973-bddc-3ab2-aebe-97d39b09ea92 | -2.60781 | -49.4918 | 2024-10-17 03:47:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 26a2f6dd-21e7-3645-bb49-caf92a7b588d | -3.65498 | -50.19976 | 2024-10-17 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4fc3952-00da-366b-b8d3-495e98fcd74e | -3.64904 | -50.19104 | 2024-10-17 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cb7cf6e-6b91-31b7-a80b-3cf292052758 | -3.64877 | -50.1929 | 2024-10-17 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4ce2219-a6a8-3d87-b907-6fb60c8de184 | -3.64767 | -50.19854 | 2024-10-17 03:47:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a291453-0c09-3041-bcbe-3a28088cb598 | -6.75784 | -34.967 | 2024-10-17 03:49:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 80b7bab5-16c8-3d09-99a6-5e9a7dada30d | -6.75778 | -34.9665 | 2024-10-17 03:49:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d3735982-c13b-3268-a8f1-e0be5d1d35cd | -8.84323 | -35.65269 | 2024-10-17 03:49:00 | NPP-375D | XEXÉU | PERNAMBUCO | Brasil | 2616506 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9b787878-ae4b-36b8-9b85-a4e4a53ab5db | -18.77759 | -41.49934 | 2024-10-17 03:49:00 | NPP-375D | DIVINO DAS LARANJEIRAS | MINAS GERAIS | Brasil | 3122108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 843d065a-5978-3416-9aad-635e6b61760e | -18.60055 | -41.11353 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 240402c9-2fb8-3f61-bd29-b9ad38bb3781 | -18.5999 | -41.11745 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e12f3965-515e-3679-b6d1-d1c515c6adb2 | -18.59925 | -41.12136 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 505f8e0b-33ab-349d-9e3f-fecf2ef0b2fe | -18.59715 | -41.11288 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f7d3d732-250f-3fae-8f20-05bb5a2a477b | -18.59651 | -41.11677 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e0eb22e3-77b7-32fc-93fe-96a99e78e3e6 | -18.59586 | -41.12067 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d7b32fc0-a1a4-3041-a5e4-3006c8dbe981 | -18.59312 | -41.11609 | 2024-10-17 03:49:00 | NPP-375D | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a634e4f5-e649-38c6-a102-42d1c11e6572 | -18.39845 | -40.87796 | 2024-10-17 03:49:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a504e58a-800a-356b-85e2-c38d9b56f1d2 | -18.39783 | -40.88173 | 2024-10-17 03:49:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 14548232-9e76-35b3-aa84-8a92f7ff100e | -18.39507 | -40.87735 | 2024-10-17 03:49:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 443eb3ba-7017-34e6-a26f-6cda2e8a07f0 | -18.39444 | -40.88111 | 2024-10-17 03:49:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 00c35035-8e05-3b03-83e9-67837c18cb28 | -18.39106 | -40.8805 | 2024-10-17 03:49:00 | NPP-375D | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a84829b6-d97f-3639-979f-989decd0bcec | -18.09533 | -41.43457 | 2024-10-17 03:49:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e587e47-c9dc-38dc-8532-3a157a5c821e | -18.09255 | -41.42999 | 2024-10-17 03:49:00 | NPP-375D | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6b4a5df-8e0e-3165-83df-ea4fc40503ee | -6.39811 | -39.91002 | 2024-10-17 03:49:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 24822f49-81a8-30a4-87d0-014e8b7e0238 | -5.95056 | -39.67858 | 2024-10-17 03:49:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4321f76a-8514-3243-a931-503da3648005 | -7.10001 | -40.26711 | 2024-10-17 03:49:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b09363a6-63b5-3400-8e01-d9cf4c45ed58 | -7.09768 | -40.26808 | 2024-10-17 03:49:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6dabb802-7435-3491-8fe1-a190a9dc6d84 | -17.75224 | -42.8938 | 2024-10-17 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9028d71-8f8f-310d-a7fb-39effb6c321a | -17.67825 | -42.74195 | 2024-10-17 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0fe1315-4903-39ef-bd46-b6924143560b | -17.67459 | -42.74125 | 2024-10-17 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 313fc3cc-0ed0-38ad-a898-ba17ba8faf4b | -19.37877 | -42.408 | 2024-10-17 03:49:00 | NPP-375D | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2e8683b-4542-3162-a207-56e3c88f32ad | -19.14174 | -42.29174 | 2024-10-17 03:49:00 | NPP-375D | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b5c49856-de5a-3543-a37c-cfe357a0679c | -19.13822 | -42.29107 | 2024-10-17 03:49:00 | NPP-375D | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5cf2f92a-2501-31ad-97d1-d5dee703d665 | -18.55489 | -42.95131 | 2024-10-17 03:49:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c0ddfe4-724d-368d-ac9c-5ebf0c576815 | -18.55124 | -42.95061 | 2024-10-17 03:49:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 10be1190-d417-32c5-b23d-0a3b7aad9fd9 | -18.40177 | -42.19928 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce8f75fc-e7d8-3c93-9d39-8a5f333124e8 | -18.39899 | -42.19429 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bcf8d390-4c8d-3868-8179-280ef0dd5a50 | -18.39827 | -42.19847 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2e7f9e1f-c08a-33bc-a41d-069c9324a8e1 | -18.39475 | -42.19772 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dbc10fff-61e3-351f-b006-95b16a2541bf | -18.39399 | -42.20209 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 445efb8f-d8ee-3bc9-a351-94821f46b587 | -18.39121 | -42.19709 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d0ef6fe9-f211-3b40-97ee-9ae8aebc749f | -18.39045 | -42.20143 | 2024-10-17 03:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 13481407-2c0b-3b91-bbff-a62db504b451 | -18.34048 | -42.91473 | 2024-10-17 03:49:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a4e4131-5e9e-318f-ad58-6734180fc431 | -18.28636 | -42.79417 | 2024-10-17 03:49:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a2bc078-4ca4-31a3-a91b-309accb0490f | -18.28557 | -42.79865 | 2024-10-17 03:49:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60cc8ef7-d9a4-306e-b3c1-6d3a39fe7100 | -18.24844 | -42.60393 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a91dd2cd-c806-3328-9473-17acd490687f | -18.09958 | -42.92157 | 2024-10-17 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4a969c39-34bb-39ff-8fb8-7d387706207d | -18.08451 | -42.70777 | 2024-10-17 03:49:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| db677a2a-9579-3b90-a476-419065210f1c | -7.99147 | -40.96951 | 2024-10-17 03:49:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41d25685-f86b-3bb5-a0ca-76197114d29d | -7.99069 | -40.97414 | 2024-10-17 03:49:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8f294aab-63df-39f5-856d-94e780c72f33 | -7.50919 | -41.23745 | 2024-10-17 03:49:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f6c96e44-3e24-34a7-ac33-c4853a9a95ab | -7.23432 | -41.87566 | 2024-10-17 03:49:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c67b6fb8-2db6-3605-8779-509dc9783df4 | -7.96907 | -41.60358 | 2024-10-17 03:49:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee3c82a0-5319-3404-9da0-ff0448f8917b | -17.74677 | -43.91168 | 2024-10-17 03:49:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c71d5bbb-96cb-3aed-963f-dda5ab4dee55 | -17.74607 | -43.91328 | 2024-10-17 03:49:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f02e146-a19a-363a-954d-5849a10b81d0 | -19.03194 | -43.56844 | 2024-10-17 03:49:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d07e2353-b77d-38fd-b29d-17afe8394993 | -5.6455 | -43.23244 | 2024-10-17 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56df9fef-25fb-3397-9610-81cc367cf916 | -5.6549 | -43.00734 | 2024-10-17 03:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5a66a6fe-1d00-3524-8acf-d9eea4079f70 | -5.65415 | -43.01184 | 2024-10-17 03:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5b529cf4-fb7b-3cb9-9f8f-d915efe3c796 | -5.6463 | -43.23138 | 2024-10-17 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8953cbf-fdfb-313d-baf4-be0203d3d39b | -5.64549 | -43.23603 | 2024-10-17 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cdd2f77-230c-3a12-947d-e545192a0c23 | -5.64473 | -43.2371 | 2024-10-17 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6323e3e-a053-30e5-bb76-de2fb517d80d | -5.33044 | -43.07558 | 2024-10-17 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 737ee80a-2b1b-3a31-be64-a84aa8cbc1b5 | -5.3294 | -43.07789 | 2024-10-17 03:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8847669d-36cd-3f7a-8847-d444e9d91e47 | -6.34662 | -43.41359 | 2024-10-17 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb6beb51-28e3-320c-8cd2-857e1e156aa3 | -6.21447 | -43.28058 | 2024-10-17 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08008280-b212-3b9c-9c74-561a5d8058c8 | -7.19042 | -42.64904 | 2024-10-17 03:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 250f1e12-2ca8-3d5a-b6e8-e51aa11529c0 | -7.18974 | -42.65302 | 2024-10-17 03:49:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 8a340a7c-b70d-30c0-98dd-13f86e83dba6 | -6.79739 | -42.84452 | 2024-10-17 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d02130be-9417-30d0-8f16-001fee2a7610 | -6.72937 | -43.5615 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 86739348-bb47-35f9-806c-dba55545e180 | -6.72481 | -43.56065 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b779d950-add8-3019-9f5c-3413e0206acf | -6.72026 | -43.5598 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2cd98fb8-a866-3074-b5ca-d7e336ecb7d3 | -6.71945 | -43.56452 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a9849d6-81b1-385d-869e-4a69e1863020 | -6.68999 | -43.54459 | 2024-10-17 03:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README22.md)
