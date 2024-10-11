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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb16523-1309-31fa-8fa8-d5712ec4ed9f | -11.4011 | -60.395901 | 2024-10-11 01:39:32 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca8b0862-bc3e-38e6-866e-5687abbc782a | -11.4027 | -60.402901 | 2024-10-11 01:39:32 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c5ec471f-b979-30c2-a325-ada6f8e4c8e4 | -11.4043 | -60.409801 | 2024-10-11 01:39:32 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 220ee648-b5cd-3489-b59a-0804f5a78ae4 | -11.4138 | -60.451599 | 2024-10-11 01:39:32 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 85992b6c-9cd8-343e-ad1f-bb8cba32a03d | -11.3945 | -60.412102 | 2024-10-11 01:39:32 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| af764388-637e-3894-87e4-432121f49921 | -11.3543 | -60.553001 | 2024-10-11 01:39:34 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c19138be-8169-3349-a541-53620f02973c | -11.3558 | -60.560001 | 2024-10-11 01:39:34 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac15e75f-51d5-3fc5-85c2-fc419800b26e | -11.3445 | -60.555302 | 2024-10-11 01:39:34 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8822ba69-1fb3-353b-9944-1bb21f99977e | -11.346 | -60.562199 | 2024-10-11 01:39:34 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0b7cdd8f-ff81-39a7-8793-2ffb154bd68d | -11.271 | -60.367298 | 2024-10-11 01:39:34 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 799a4ad8-e900-3b37-9181-a3a71d574626 | -11.2726 | -60.374298 | 2024-10-11 01:39:34 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9be52322-2260-37b1-8118-2aa7ca9d659a | -11.2742 | -60.381199 | 2024-10-11 01:39:34 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 182c1584-5263-3cf9-8fb3-ff2d9e3338c0 | -11.2675 | -60.3974 | 2024-10-11 01:39:34 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 01c4d723-6600-3533-92a5-faaee073586a | -11.2691 | -60.404301 | 2024-10-11 01:39:34 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d26793df-78d3-3e0a-876f-299797dc1e3b | -11.2707 | -60.411301 | 2024-10-11 01:39:34 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 10877b3f-3135-3f77-8905-c19d8ec929c6 | -11.2577 | -60.399601 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03223bcc-68e4-3b71-9a3d-f628a9a457e1 | -11.2593 | -60.406601 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 60976d91-4e40-379b-8aaf-fea77acbbd7c | -11.2751 | -60.476101 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c7ad3dec-6444-3711-9060-3086a3155330 | -11.2766 | -60.483101 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9219613a-1053-32a3-a901-5383c74e58ab | -11.2782 | -60.490002 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7065633-3667-3f46-9c39-56afcf37bb6d | -11.2798 | -60.497002 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 49411944-20ff-3027-928f-e6953f8a9870 | -11.294 | -60.559502 | 2024-10-11 01:39:35 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf26a743-999f-3592-a2c1-dcc6c6c6833c | -11.2653 | -60.478298 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 83af0c0e-4997-33f7-bcff-290bac03d479 | -11.2669 | -60.485298 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54d127c7-571a-34aa-bb5c-cd57375f930e | -11.2684 | -60.492199 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e4c4ec3d-3f9a-39e6-9590-d601532be01c | -11.27 | -60.499199 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9556ebc0-cf39-3f75-9a54-39e259419874 | -11.2873 | -60.575699 | 2024-10-11 01:39:35 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6884184c-33cd-33b3-9dc5-da6fef134d91 | -11.2586 | -60.494499 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b0d05714-4f35-35f9-9384-f6478dbbb792 | -11.2602 | -60.501499 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8e456e06-90fd-383f-8ccf-0e23ddf919ce | -11.2854 | -60.612701 | 2024-10-11 01:39:35 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a6381fef-c509-3958-bb8f-95b1820b1f68 | -11.2359 | -60.4851 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 09dd3396-b0da-3c3d-bbbb-45b7c8af982a | -11.2516 | -60.5546 | 2024-10-11 01:39:35 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6c25b8eb-ade2-31a4-a955-96f9578dc821 | -11.2532 | -60.5616 | 2024-10-11 01:39:35 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5842f68f-9603-35c5-afd1-9901670d50aa | -11.2277 | -60.494301 | 2024-10-11 01:39:35 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1442129d-c8af-3071-aa09-a179cdd7e2d9 | -11.2254 | -60.575199 | 2024-10-11 01:39:36 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4f7323cc-7d7c-337a-99ce-e0e6797c1f2a | -11.227 | -60.582199 | 2024-10-11 01:39:36 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 57596ea3-211a-3060-98f3-b25f05c583d2 | -11.2285 | -60.5891 | 2024-10-11 01:39:36 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5df76e71-d093-3890-8402-1c59fa03f67f | -11.1758 | -60.447701 | 2024-10-11 01:39:36 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e79871e-b05f-3df2-9d61-9e7f3fb1a3ef | -11.1774 | -60.454601 | 2024-10-11 01:39:36 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1f53f81-8e19-3ffe-9283-7c7f438cea5e | -11.1941 | -60.6189 | 2024-10-11 01:39:36 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8f4ad93-e413-3174-a728-8f7260f9095b | -11.1956 | -60.6259 | 2024-10-11 01:39:36 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99f6bef1-82e7-30b3-956a-ffb0aca72d7d | -11.1729 | -60.616501 | 2024-10-11 01:39:37 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0baad7e6-08e2-3320-8b32-3859ee1fd989 | -11.1745 | -60.623402 | 2024-10-11 01:39:37 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1fafed53-bf60-3946-91a2-a28bbaec625b | -11.1584 | -60.5979 | 2024-10-11 01:39:37 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc8142e-c508-379c-ad03-5c5194f60935 | -11.1599 | -60.604801 | 2024-10-11 01:39:37 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e378e730-4e1b-3789-98d7-e4bc8006fb92 | -11.1486 | -60.600101 | 2024-10-11 01:39:37 | METOP-C | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99509a66-bd52-3397-a5d5-012984a97cdc | -10.3344 | -57.495399 | 2024-10-11 01:39:39 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 47e3fff5-c4e9-369e-8aa9-2f6f92c30617 | -10.3364 | -57.5037 | 2024-10-11 01:39:39 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f34df96d-8b73-33d2-bc0c-7b0f22eb8aa4 | -8.8608 | -53.005798 | 2024-10-11 01:39:45 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06d090df-86f3-3d18-b6d5-b7ff00e32f15 | -9.9495 | -58.094002 | 2024-10-11 01:39:47 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7fbeb6-b404-353f-9b86-eca0b360c0de | -9.9514 | -58.101898 | 2024-10-11 01:39:47 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e889e4bc-4b79-3f08-bcb3-c295964119d6 | -9.9533 | -58.109798 | 2024-10-11 01:39:47 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01a6606c-d6b4-3c44-a043-995ee5869ed0 | -9.9397 | -58.096298 | 2024-10-11 01:39:47 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f9aa704-ba37-3a2e-9add-662d50b7513e | -9.9416 | -58.104198 | 2024-10-11 01:39:47 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9d385c3-e750-3cc2-89d3-1a2426541853 | -9.657 | -56.951599 | 2024-10-11 01:39:47 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb1a8c3c-1f11-384d-8990-62f73f652ba7 | -9.405 | -56.2915 | 2024-10-11 01:39:49 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d04573e-66d9-318b-970d-1a2a1069a569 | -10.4316 | -60.982899 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c236258f-dd29-3ff2-9fa8-46a27af980a5 | -10.4331 | -60.989899 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 297fc9fc-7a51-3bdf-ae2e-2cfe6f8632c7 | -10.4347 | -60.996799 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9e59e32-1bfb-3bda-ac81-46d14341f3d6 | -10.4363 | -61.0037 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8230323-d778-3106-8d37-fedadf82872c | -10.4218 | -60.9851 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 363886ef-38ed-3e76-96b8-cbb8ee0b4bc7 | -10.4233 | -60.9921 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1c5d329-6a7f-36a0-9a33-8f6dc7ef0b80 | -10.4249 | -60.999001 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79f0386c-7f87-3864-9448-a36af6842c34 | -10.4265 | -61.005901 | 2024-10-11 01:39:50 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1497839d-2709-3f94-8d47-f70d04313358 | -10.4195 | -61.249001 | 2024-10-11 01:39:51 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96f7ade4-c41a-36d0-8791-0107553b1f2d | -10.4211 | -61.256001 | 2024-10-11 01:39:51 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0ff261e-cdf7-31d9-95c3-08873fe53783 | -10.4226 | -61.263 | 2024-10-11 01:39:51 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fe32d0e-edd1-31fb-ba0e-2cc392e03407 | -10.4003 | -61.2094 | 2024-10-11 01:39:51 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 148d859b-799e-30eb-831c-3069dfe33d58 | -10.3756 | -61.237 | 2024-10-11 01:39:52 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7154d944-9baa-372e-8314-2c3e0d500129 | -10.3772 | -61.243999 | 2024-10-11 01:39:52 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9556a79d-12e9-3693-a856-f87ef501c3cf | -10.3642 | -61.232201 | 2024-10-11 01:39:52 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3ce3e99-179b-3ef0-8c93-d5a27ac5cc66 | -10.3658 | -61.239201 | 2024-10-11 01:39:52 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65697eb5-d0b6-3aa4-bffd-5c851a1dbe85 | -10.3674 | -61.246201 | 2024-10-11 01:39:52 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2b807b8-cebb-3d2a-81f2-b5d7613ee879 | -10.3689 | -61.253101 | 2024-10-11 01:39:52 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5844d696-d6d2-3e7e-a11a-368e8e277aab | -10.0588 | -61.111401 | 2024-10-11 01:39:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21aa5546-d3ed-3cd0-8f5b-634ab1c93a4c | -10.0604 | -61.118301 | 2024-10-11 01:39:57 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ebc6d529-2ec5-3baa-b9f7-a5b24fadb91d | -10.6996 | -64.101601 | 2024-10-11 01:39:57 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0efcc96e-09be-36be-9d5c-141fbb39e73e | -10.7015 | -64.110298 | 2024-10-11 01:39:57 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3f13ed38-f80a-3ed4-b39d-f5008fc84d31 | -10.7033 | -64.119003 | 2024-10-11 01:39:57 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e9569442-dcf4-3894-a71e-d503f5f58034 | -10.6917 | -64.112396 | 2024-10-11 01:39:57 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 233a9bae-9d77-3d4d-98c1-ea4951d0ce36 | -10.5816 | -63.983002 | 2024-10-11 01:39:58 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b41705a-07fb-31ff-bf1c-d6f3321c47b0 | -10.5835 | -63.991501 | 2024-10-11 01:39:58 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c4eb049-b9eb-319e-970c-054dbc0c5d3f | -10.5853 | -64.000099 | 2024-10-11 01:39:58 | METOP-C | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21bac559-5588-3741-b012-f629097d6c82 | -10.5811 | -64.027901 | 2024-10-11 01:39:59 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7db4ee12-4906-3ba2-b01e-e99e1209029e | -10.5829 | -64.036499 | 2024-10-11 01:39:59 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 25e41c7c-7111-3095-8d56-73c03414569f | -10.5713 | -64.029999 | 2024-10-11 01:39:59 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7adbd5ae-1e48-31dd-8e38-069d006deec7 | -10.5731 | -64.038597 | 2024-10-11 01:39:59 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 37cec51d-527b-3ff2-a31a-569cb990c2b6 | -10.575 | -64.047203 | 2024-10-11 01:39:59 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b2daf933-a025-3182-8d06-284d3ae8ddd7 | -10.6097 | -64.397903 | 2024-10-11 01:39:59 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f1577d74-35c4-3ac9-847f-45d5e3b5faf3 | -8.447 | -55.451302 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23563a49-5a58-391c-b6bd-e12611ffc11d | -8.4344 | -55.442101 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 091db06b-849e-32d0-b811-86cc1548c680 | -8.4372 | -55.453602 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b273ddd4-4a38-342e-b9c0-dbcae572bfa8 | -8.44 | -55.465099 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a46768cf-2a35-32a6-9a0b-8bb9e0d3aab8 | -8.4429 | -55.476601 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8883b321-155e-318a-9fd9-7822f3a7844b | -10.2667 | -63.3382 | 2024-10-11 01:40:01 | METOP-C | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cba9f9aa-12cd-3129-8d93-51f9c1226d62 | -10.2685 | -63.346199 | 2024-10-11 01:40:01 | METOP-C | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d2aa3c25-67b9-3d53-96e5-e730eb5c32c1 | -8.4275 | -55.456001 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91cb9718-16dc-31a2-a732-aa7d6a5dc7c6 | -8.4303 | -55.467499 | 2024-10-11 01:40:01 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b215d84-7a2b-38f4-bfe4-56b62cebd785 | -10.5959 | -64.954399 | 2024-10-11 01:40:02 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e48e0290-5e6f-3514-82ac-4851247c23c6 | -8.2891 | -55.354198 | 2024-10-11 01:40:03 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README24.md)
