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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82e67c7b-c593-3359-a4f7-a84f4568ac21 | -15.31993 | -52.99803 | 2025-10-25 05:12:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a632a9e8-fcdb-3128-8358-91f56bd81af6 | -12.87119 | -48.6011 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65e62d0b-70f3-34a1-8ddf-8fe0cf77e636 | -12.15112 | -55.43029 | 2025-10-25 05:12:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d9d9aee-dc4b-33cd-a9f5-7fd2f1b58656 | -12.38916 | -49.94938 | 2025-10-25 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0a7f893-70e1-3c11-aefd-1ad5847ed9e6 | -13.29171 | -47.4965 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9efe6170-bd30-37ed-a812-c786a637c52e | -14.92432 | -52.44519 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c76b3600-7dff-3c07-ba25-6f290dc1e7d6 | -14.1839 | -47.31698 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf52923b-e96c-3319-b1e7-c18420005146 | -13.5461 | -47.56914 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dae744a-5d8a-3a6c-a879-710d0df58b94 | -14.47518 | -47.90452 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e7bb44cf-548f-3a4e-90fa-742c9ffef0b6 | -12.11878 | -47.39357 | 2025-10-25 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| badc8bef-ffdd-3ab0-82cf-eeecaaf54ed7 | -11.51319 | -54.31928 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7589aa31-3ddc-3d66-aa13-6edd4cd31e29 | -14.80669 | -52.80494 | 2025-10-25 05:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45e0d2b4-a72c-393d-87e3-c0dbfad70452 | -13.33895 | -47.90946 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f333f50c-75c5-3a38-b866-38693ad0299b | -10.60392 | -57.77207 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1cf090a-9bbe-36cd-a753-d2ea9ccebeec | -13.88014 | -49.04802 | 2025-10-25 05:12:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9ba243a-cf20-3851-9f86-5c6877b28287 | -14.43624 | -48.06915 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9923176-cb4e-342f-9180-9467ab4fe157 | -12.4523 | -55.23518 | 2025-10-25 05:12:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4c162b93-c849-3020-9f0b-b883316f1d6f | -12.10645 | -52.49379 | 2025-10-25 05:12:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbaaafdf-e382-33aa-8370-44a93a137851 | -15.94051 | -56.11231 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1eb86f4d-3be2-3cf4-b069-c1f9ce7f9b79 | -15.245 | -47.92455 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 50871ca8-5225-3f48-bf84-ca9c051a80b4 | -14.89284 | -52.44135 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4737e24f-4f1f-308f-8534-c576fc3a8abb | -14.79039 | -59.2417 | 2025-10-25 05:12:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43f38e8e-dabe-3a6a-a3a4-dbb2de30f53f | -9.91986 | -60.77757 | 2025-10-25 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 992fbcc0-2d7c-3785-bac6-38270e67a7fc | -11.95872 | -55.2614 | 2025-10-25 05:12:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 690bc90f-cb38-313c-ad85-8a5fbed5546c | -12.38622 | -49.95121 | 2025-10-25 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79c5e582-44c1-3da6-becc-b50e84092b89 | -13.03537 | -47.39524 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ae142e2-b0c6-33f6-badc-96f18fe6622a | -12.53677 | -49.60435 | 2025-10-25 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d0fdae5-73d6-33a2-863a-46c264c25a69 | -15.09113 | -56.42356 | 2025-10-25 05:12:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3baa51a-bf7c-3d24-b3ba-7bbeb8e36a07 | -11.31268 | -55.204 | 2025-10-25 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2da573b-9b25-30eb-b798-17a28f83189e | -11.32749 | -53.92846 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47a78214-407b-3e59-b8d9-712f5ed54b3a | -13.90081 | -48.41816 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d43d43d-b27b-331d-b7a1-41c2de4702e8 | -12.12055 | -46.7085 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17613105-cc9d-325b-b464-962b5f5f033f | -10.84633 | -57.08206 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9655b0ec-814d-3406-b779-42579195a0a5 | -14.84499 | -52.43839 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48b07e80-97ee-3c7d-ab0a-6eabf0056435 | -14.4597 | -47.93512 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 216fa725-caea-3392-9d24-e6694b74aad3 | -12.15175 | -48.01867 | 2025-10-25 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3e77344-5889-3c33-8f60-ac943a8c7454 | -9.98718 | -59.95594 | 2025-10-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0580e8dd-dd8c-3b52-ba38-f60bbbb711ea | -11.85577 | -56.85733 | 2025-10-25 05:12:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3795176-bf9a-3b38-a83a-f39a1c4782ba | -12.81359 | -48.67494 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bea80b6-9a49-3eac-8ee8-c2f3af39791f | -11.32561 | -53.93156 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71c92290-1d66-3b43-8c60-d0e25e95dc74 | -14.87805 | -48.10036 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41dfe752-8649-354c-acab-0e42b9da55ee | -14.44532 | -48.07006 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43b42544-b5a8-3603-9589-63797f514ad2 | -14.86466 | -48.0863 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| f119e3c6-0d06-3d47-909a-da878b3f288f | -12.61048 | -62.09041 | 2025-10-25 05:12:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68d4bacb-5250-3553-b393-b6437bf585db | -15.2445 | -47.92931 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4bfd0c21-3a90-397f-a3ed-b9c06dd181a3 | -15.93688 | -56.11177 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e40ec3db-bd12-325a-894b-941be737148b | -14.4576 | -47.93417 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd3f6d69-6dad-3a69-9478-65c8e4a0412e | -14.17672 | -47.31158 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a28d64ab-c97b-35a0-b2b3-0acbd3e537fb | -14.56374 | -49.83971 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1abf3be4-8e90-3c1c-b880-696c15da220b | -14.43972 | -48.06593 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c07a50-49c9-3c95-9b37-e2fccad36c05 | -13.28576 | -47.49442 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 810ec5ae-6a7b-3311-bccc-e226215c2682 | -12.95719 | -48.50427 | 2025-10-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5833477-b74f-34f6-bf74-a052b92362dc | -14.91474 | -52.44873 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bc8d354-a702-32ce-a322-31e993dd4b22 | -14.20253 | -47.30622 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d06d69e1-499f-3eff-9536-584e5d9b06dd | -15.47498 | -50.45547 | 2025-10-25 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9d5b7e4-5252-3550-ae25-585e3a4e31df | -11.81468 | -57.94723 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a91242e-e085-3f02-abda-359b880c96c6 | -11.57199 | -51.4694 | 2025-10-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc57baf1-67bc-3d86-a38e-9363c714234c | -14.8642 | -48.09041 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4ca69299-94a9-361b-9d7b-944c8a8ee677 | -11.36523 | -54.32642 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64a24343-4457-31f7-83f9-2b5ed336b815 | -12.84019 | -48.64326 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ecc1889-6634-3af7-a415-82fa26b1b153 | -12.37592 | -63.87574 | 2025-10-25 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1ad9053-68b2-3492-8de6-0a8201081b62 | -9.92529 | -65.01097 | 2025-10-25 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca673770-0c26-39b4-bc3a-2ebb528e9cfe | -13.06245 | -50.28746 | 2025-10-25 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b6adeec-0f5f-3378-ba89-1cea8c3e7311 | -11.55455 | -54.51584 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b0cc48e-f54d-35ca-b5da-c0d449fa2a9f | -13.88525 | -49.05253 | 2025-10-25 05:12:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87f2e4b7-cb62-33e5-896d-16384e56dd44 | -13.91301 | -48.41417 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d317d52-21ae-30e9-b8c1-021557746927 | -16.64306 | -49.52111 | 2025-10-25 05:12:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 004f9020-e1fa-3314-802e-83f7a8bd7b2b | -12.47991 | -61.04824 | 2025-10-25 05:12:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab7ea6f1-b263-3f44-a1c3-24662924a7a6 | -12.95112 | -48.50674 | 2025-10-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dafacaa1-1e88-3cfb-8b91-7becaf2f5c51 | -12.87681 | -48.60207 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2392de2e-ffbe-3e80-81f1-a3037fa0174c | -15.82383 | -53.5973 | 2025-10-25 05:12:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53cb10ba-869f-3e81-95b3-cb4b66072048 | -14.86105 | -48.0891 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 60b5ad75-b7af-389b-8827-0734933637f4 | -15.82435 | -53.5932 | 2025-10-25 05:12:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4992fba7-b25d-328b-ade5-7e7dd04b0f95 | -14.8656 | -48.07789 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 15973123-7fe1-382a-8e3d-14cdb3e0a5c8 | -14.86196 | -48.08052 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 85970166-63d7-321d-be9e-73a21c9171eb | -10.99646 | -54.25535 | 2025-10-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e520758-fc5c-30ad-8557-32149655604c | -14.86752 | -48.08529 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d8ec8523-45e6-31c1-b2e1-a75cdddc8c99 | -14.78708 | -59.24115 | 2025-10-25 05:12:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62c23fcc-f235-368f-8037-4da40e8e0204 | -12.04757 | -54.23602 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f7a3569-209d-3b10-a163-9af367d9ca69 | -12.23281 | -60.32783 | 2025-10-25 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c67d40c-9c42-3e52-a908-fe601346b104 | -13.33076 | -47.92863 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c3e99cd-ac35-3a11-a01c-bd7a33c83a3d | -14.1728 | -47.30305 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65213358-d822-3f3d-b45f-f4dd2e3a6dc7 | -12.04373 | -54.23546 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cea60fb-ffb2-36ec-94e0-b271363aab4c | -14.56906 | -49.84043 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10ac3866-eb2b-3115-9004-8d5a05011696 | -11.71399 | -62.93543 | 2025-10-25 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5109bb09-3653-32b9-aabb-5d055cf4c914 | -16.565 | -49.25552 | 2025-10-25 05:12:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5aa6da0-5c9e-3f3d-a1ae-d68e0be018be | -14.54237 | -48.04117 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f0a671d-2c68-362f-8373-8bc77fff1c1f | -9.93297 | -59.91999 | 2025-10-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12bfe4ff-2ba1-39f5-9689-9ae5a6d968fd | -14.19017 | -47.3173 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 378622ce-abc1-3e3e-aa38-c9d512340df0 | -11.71785 | -62.93607 | 2025-10-25 05:12:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74277d83-412f-3873-b81c-490d87f3d18f | -9.92051 | -60.77357 | 2025-10-25 05:12:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45fc4d58-dc81-3d8a-8775-f0710b0624d7 | -16.21416 | -46.47682 | 2025-10-25 05:12:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f32fa08c-a9f9-3f85-a0d8-eee55a1475dc | -10.98677 | -58.45997 | 2025-10-25 05:12:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7545c0e4-eca6-3e36-b0c4-66bfb87152bb | -16.36891 | -49.93974 | 2025-10-25 05:12:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b6b7344-9606-3911-8bb7-f6bd3c2591ce | -14.8662 | -48.09776 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bb344f57-116d-3416-a814-8e3b32867294 | -16.22028 | -46.48374 | 2025-10-25 05:12:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7c0467b4-48e2-3664-ba90-aa1d64d5e826 | -12.29899 | -47.45835 | 2025-10-25 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd91c430-9d37-3e35-a659-4b759ad9d9e4 | -9.72565 | -67.47209 | 2025-10-25 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66a71e13-1cd5-300a-9da7-649dab23d42d | -12.12687 | -46.70921 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1498b765-f438-3af0-8634-c6a3ec64c2ea | -14.44486 | -48.07436 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README58.md)
