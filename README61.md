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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e49ff036-c5c9-3b2e-b5e0-fe2f89c7053e | -13.43049 | -46.96739 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dde1d1e7-1cc6-3a60-976b-cac35011b492 | -12.89885 | -48.11073 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a288a806-fec6-35f1-9370-d4b3b01a9a53 | -10.3306 | -46.78015 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d6adf4c-18da-3322-a097-5c14b722be69 | -9.46367 | -60.30725 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8edf314d-b19e-3d92-bbd9-31ffe15ba8ac | -9.07395 | -66.06572 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49c3ce71-6d96-39b2-8811-2ae5d9254127 | -12.8173 | -48.13734 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a639ceb-b419-3085-b044-6fe2d8557132 | -10.32069 | -62.62095 | 2025-08-28 04:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b1d4206f-c98b-31f7-bb0f-fe67bd1903f5 | -9.12193 | -65.78134 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 199401d8-daf7-3945-b239-996ce8ba5ba8 | -10.48182 | -57.96017 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c2d278e-abeb-3fa6-bf78-068c5e6cd769 | -12.99882 | -56.9027 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61eb2681-5338-3289-8e6a-352244d789d9 | -14.27834 | -53.06979 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee935ba0-78a2-314a-8bef-16de671ba2ce | -8.9048 | -62.47272 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9cd5a56-cbef-3028-9a57-4355013d01db | -8.35031 | -62.92889 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d36b3717-70b2-3a59-a195-f84f3c03e5ad | -10.47386 | -57.93917 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c34e6f65-d683-3b6d-a9ba-4d2be18a0337 | -14.12407 | -53.97255 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23754c75-aafa-3911-a3b7-2535a138b200 | -11.23074 | -55.06194 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92680ba8-bf1d-3dd7-bfd7-6a73fc28ea95 | -13.35244 | -51.78989 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae031966-d1c0-3ef1-8634-02466ef68b12 | -15.67096 | -52.73177 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03f1a223-ec97-3b12-80b1-55aed3d45876 | -15.67774 | -52.7375 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3fcd292-cc33-3b81-baae-8ed9f17a7dc9 | -10.70769 | -47.02018 | 2025-08-28 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51358e39-a120-300d-bb7b-8b48b3b756f4 | -12.2277 | -64.23068 | 2025-08-28 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b61552f-b5f1-3093-bd1e-bc309063db51 | -8.34336 | -62.93927 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3beb09f5-eaab-3bc6-a258-60ca7b26c432 | -9.49151 | -62.38567 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db24456f-635c-3b97-8411-41067447b8b2 | -10.54497 | -46.69823 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 44e1a109-296c-393f-8c28-30b6dcda6c16 | -9.1591 | -59.59199 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd56dfdf-db90-3046-a7eb-aac674242970 | -13.38071 | -51.75492 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57aeee01-61ff-3639-94cf-df67967909e4 | -11.64765 | -46.39051 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffe7f0ae-6456-3a4d-80cd-be539c40cb03 | -12.7874 | -48.17987 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8cef835-36e5-385e-9ede-94c72cb03859 | -10.59357 | -54.89559 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fbe8982-a535-30c9-b879-537c0b337227 | -14.31418 | -60.35978 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 654e750c-28c0-3177-9f88-68329d3e6700 | -15.62645 | -52.75292 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a56bef5-1725-33b2-a43d-1f8b0e1badc1 | -12.81622 | -48.10696 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13f6a828-f726-3203-80e7-b835732ebf54 | -13.53631 | -46.93217 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3941f863-546f-32cd-9c1f-9eb82f2898e8 | -10.81075 | -60.77099 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 4583d4ed-6b75-35ad-94c9-f4175164049e | -9.26971 | -59.77246 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ffef753-7d8a-35a3-8e88-5d6fe95ce517 | -9.54404 | -68.57495 | 2025-08-28 04:59:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b08488b-2391-3bae-8304-6d0dbc82d96b | -9.78728 | -64.25813 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19525326-c862-33c9-a3c2-e1aae12ed276 | -9.11527 | -65.78442 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| f4b1be11-0eb9-33b8-8e91-ce0946989574 | -11.57314 | -46.38992 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ada051b3-bf8d-354e-b16b-406de0e829ee | -13.37553 | -51.76403 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 383fb6c7-f58f-3944-be78-8f895bae0a06 | -10.5375 | -46.67501 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 510b8a9f-fad2-3dc8-b5e4-c1ec8be128f8 | -14.44405 | -53.19523 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29f45667-d7e7-3997-b760-c8fc638ada63 | -9.40991 | -60.56864 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8052a24b-5745-3e71-830b-889b029f9720 | -9.11085 | -65.74401 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42f3dd32-0b19-3ff1-8444-9360a9477c30 | -13.42404 | -46.97662 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3130f2e-e744-373b-9f41-dc4d0bd0acdb | -11.33068 | -43.52413 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40946549-6726-3b66-a5dc-9aedf4565d4d | -9.54734 | -65.68922 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 930c1a64-79de-36be-ab8b-67d77b349ee7 | -11.8059 | -51.41231 | 2025-08-28 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cf7e86a-200e-30b9-b182-fd871f2bfb88 | -14.76528 | -55.94761 | 2025-08-28 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bf9cfbe-b0d8-3128-901e-bc0f3e37f649 | -11.57272 | -47.62268 | 2025-08-28 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7761a1af-b0af-3519-a76f-5d1071073b78 | -10.81612 | -60.76435 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| a5c4ef8d-44a9-3a6e-8c5f-47bdc8232fdb | -15.08973 | -48.51764 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 58e4b6ac-e8eb-39e6-803b-8e3fab72acfa | -12.86854 | -48.11829 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8a256e1d-ed06-3d5a-8452-7ff3d488bbba | -13.35415 | -54.39242 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da7823ac-6982-36d5-82b4-8a35ff0461df | -12.78754 | -48.18085 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 580d4840-b0a2-35e5-a953-8c16dcb866cf | -15.08487 | -48.5173 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ffe0280-6fe8-31cf-a5e4-6ab14d1079e4 | -9.92491 | -54.71396 | 2025-08-28 04:59:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 091ebdaf-c1ea-3b02-8f9e-af6c24150068 | -9.4143 | -60.51904 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b12ed665-7f0c-3a99-bff3-d376042a6e9d | -13.60153 | -48.22041 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2a80020-555b-3bd9-9b0c-7a7d04e6725b | -13.98328 | -46.33767 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5ade387a-fc91-3c6a-a314-44ed1ab3b2af | -13.61923 | -48.23545 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ec739231-7fe8-3bcd-9345-0fc1b3a1c296 | -15.61353 | -52.72128 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0aabd0ba-76bf-3936-8e2f-678d31d713f8 | -9.24841 | -64.41563 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6a503de5-de8c-3e3a-874d-1aa98d0c79ca | -14.27178 | -53.06446 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 8e9cab0b-6dbd-3ad9-8007-8250037f9c41 | -15.09745 | -48.61143 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c793d5c-be77-36ca-9209-579fd77d09c3 | -8.8811 | -60.75768 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fbdb422-80b7-3f49-bb3a-5411652aef96 | -10.7127 | -47.02092 | 2025-08-28 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1d8e6db-92e8-3252-94b8-109f885d4ff5 | -12.88278 | -48.11997 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7635fce-bf9e-37b1-857e-954d01c5859a | -10.47617 | -57.95086 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 958e94d1-70cd-3b05-bb3c-4b5c34f4dd56 | -9.18518 | -60.80898 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5237228a-57c0-3cb0-aacb-f2a2c0441012 | -10.47414 | -57.95962 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc858d84-6650-3e11-89fb-77ba513c7990 | -10.47814 | -57.93903 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 6195a473-a735-3fda-abbe-18e28d14e7c7 | -9.41365 | -60.5228 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43c48685-8ad1-3548-b80a-3aba32ee722b | -10.25287 | -64.49147 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 728420a1-1d84-3061-85ae-c71c83ceeed3 | -12.78403 | -48.16992 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1296cde5-1db0-3af4-b08b-1fdbde2c8f4d | -8.93271 | -65.9332 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99fc019c-dc39-342d-9bfb-f75fbc5547c2 | -8.34234 | -62.94493 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5df1e69a-4a27-3ebf-8b02-4d6bd8989c20 | -9.40868 | -60.50264 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6620858e-965a-37ae-9b9e-008d5dfc1fb8 | -10.84247 | -60.80733 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237186bf-1931-393a-a119-82f996d45005 | -9.13111 | -65.28717 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| fdf617f6-d065-3f71-9cf6-811501d5c65e | -10.30564 | -46.81364 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| feb0dec3-f315-3662-b88b-1c32cc1389e7 | -9.40512 | -60.57172 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 720f5bc4-bb93-3aea-963d-2b432ee4120c | -9.15672 | -59.53534 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 017ebf36-af18-3812-bf0a-223fb98acc18 | -14.12751 | -53.9731 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 661969b6-2cad-33f2-9249-2ba26624866a | -13.47637 | -46.85421 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e446c42-4640-3b54-8dd8-7252ab25b7ff | -11.33584 | -43.53548 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 584bff0d-bf7a-3907-bde3-9cbfcb75d69d | -13.38003 | -51.75975 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a70bda7f-9508-33cd-8547-c88b00970fae | -13.98287 | -46.34126 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e801ec00-ebf4-3a0d-9649-e0d6ac42b09e | -8.95164 | -65.94848 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f3a59c03-4ea0-351d-9afe-4b0fff7a4dd6 | -9.41149 | -60.51083 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bb536a2-6791-3807-b7ff-964810106bbe | -13.50764 | -46.85878 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90b45297-66d5-3fe0-9481-c0bb2a21c6a2 | -12.86372 | -48.11771 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 299c00ca-42e1-3785-b8ff-e0022089abb7 | -9.11687 | -65.77599 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 3f57ce21-93f9-3af7-bd83-915d71d64c58 | -9.40325 | -60.50944 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fd16d99-6585-3504-93e5-dd719f075247 | -11.3276 | -43.52691 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 046d449a-56c6-3771-9631-41a6a5ca42b2 | -14.31998 | -60.37244 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be3afa37-e173-3e45-8c26-9b70375ae648 | -10.47609 | -57.94764 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c817a6a0-aeb0-33e2-976b-0481a7220cf3 | -9.18478 | -60.86189 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c208cf26-1d23-3b9b-992e-f5ebf80ea2dc | -15.63447 | -52.74949 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ac36dda-a45a-355e-acab-6d725b474428 | -14.96117 | -54.79608 | 2025-08-28 04:59:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README62.md)
