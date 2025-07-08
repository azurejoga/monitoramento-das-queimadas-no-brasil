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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99d6b6c9-df49-3d64-8a9a-9d4e12248d29 | -7.19942 | -43.13534 | 2025-07-08 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4415fd6b-f375-3eb3-afe6-a30a42bd4f86 | -7.48543 | -43.94187 | 2025-07-08 05:04:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 150c15de-9a2a-3493-9ae5-df79117397bf | -13.01803 | -46.29502 | 2025-07-08 05:04:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c14b2e89-68b9-35fc-a0b9-5d72c680aab0 | -11.42536 | -45.10071 | 2025-07-08 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f7b673df-a18e-3b9e-bf95-98ea8491f8d1 | -15.57081 | -47.85677 | 2025-07-08 05:06:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6230904-3eda-373e-84f9-6e5973f58a14 | -15.24812 | -51.53305 | 2025-07-08 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 269ff7f8-61fe-3f91-814f-e86e60c6c64d | -12.58167 | -56.97937 | 2025-07-08 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f61c4225-1f14-33ab-86e3-0fb789138821 | -12.02644 | -57.07732 | 2025-07-08 05:06:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a4bcbb1-f4ea-3ed6-b02d-6812ae74e96d | -18.39988 | -55.60097 | 2025-07-08 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 76d64b81-ad82-387e-be23-221902e07105 | -18.40194 | -55.59959 | 2025-07-08 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 865d63db-18ce-3658-b8a7-3cd7279d2454 | -11.72394 | -62.82108 | 2025-07-08 05:06:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74d4ce47-a9f2-3cd2-9fed-a98ce7a203c1 | -17.6758 | -52.90381 | 2025-07-08 05:06:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2021e5b-1700-36f4-a252-f528f2d65988 | -15.93374 | -57.67032 | 2025-07-08 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d68324a-dd32-3120-9778-bbe2fd894abc | -14.27275 | -53.23303 | 2025-07-08 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79345934-cbd2-3e09-be1e-8fe4e665649e | -18.29 | -54.28721 | 2025-07-08 05:06:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea733816-6cd2-3051-803b-b2c2225077db | -16.06966 | -53.74963 | 2025-07-08 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6981a352-160c-337d-aea7-82d694a7e8ee | -12.58112 | -56.9829 | 2025-07-08 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 554c42e0-9627-37c8-82ca-8aefcb54ac7a | -12.8324 | -62.16293 | 2025-07-08 05:06:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4e4789-b4af-3093-bd98-c3103f5f7f16 | -13.4072 | -47.89143 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 193e0895-56cf-3455-bade-e87f8609e031 | -16.46929 | -54.54405 | 2025-07-08 05:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd6690ed-74cd-3448-a927-2deaf4e82f53 | -13.36872 | -47.78936 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1bea87c-2bb7-3952-a2f4-03c50d4ad6a4 | -14.26888 | -53.23242 | 2025-07-08 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9f958d1-c3da-3ef4-be65-ede5c24942d7 | -11.71978 | -62.82027 | 2025-07-08 05:06:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1af0dea-3bd4-37d7-9cf2-317973d81663 | -14.18781 | -45.51192 | 2025-07-08 05:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce53bf41-2215-3c8c-bac6-f24b6f5b87b4 | -13.40682 | -47.89467 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3cc19477-f362-3dce-ac88-97e360466238 | -12.58057 | -56.98643 | 2025-07-08 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7898291-830b-3be7-9079-17d360f2ecc8 | -14.83826 | -48.24054 | 2025-07-08 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76166ab0-44c6-3981-a05a-c1777be0b6f6 | -12.57891 | -56.97532 | 2025-07-08 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c88e53e7-7f2b-36c1-b567-f4dcf289e3f0 | -15.69514 | -53.32568 | 2025-07-08 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 890f537d-bcdd-3133-92a7-c72a7aa045cf | -15.69467 | -53.32652 | 2025-07-08 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19de7bfc-1387-3bc6-842e-696ee493aa22 | -15.95958 | -52.20935 | 2025-07-08 05:06:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efee82a8-7cdf-3008-b7a6-32a74adeab0d | -13.4026 | -47.88337 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b9306ad-35c7-372f-b037-32a5bb21cfe6 | -15.25745 | -51.5299 | 2025-07-08 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 905deb3b-60e8-3d13-94e4-3a6facba0918 | -15.25688 | -51.53426 | 2025-07-08 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ce6d600-04da-3022-ab95-eb20596eb3c5 | -13.36825 | -47.79321 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95967f9b-54d4-3e37-b505-6ce5a901e142 | -13.40759 | -47.88813 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 920f6996-ea68-3461-a426-4538f5f4fb96 | -13.64979 | -46.8126 | 2025-07-08 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5746bd2f-9883-39bb-9156-86f78164f250 | -18.42225 | -54.71078 | 2025-07-08 05:06:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02c12ca6-adeb-3b09-b3c8-09d267586e1b | -12.58333 | -56.99049 | 2025-07-08 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9406350f-c733-3fda-8fe7-8f2b83cff6bb | -18.2297 | -44.19901 | 2025-07-08 05:06:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27fa31b2-bb64-39b2-be8b-23f6396bef1b | -16.06737 | -53.75239 | 2025-07-08 05:06:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1100b0e-89a8-3f3b-9bc0-05167d364de6 | -11.87933 | -58.71466 | 2025-07-08 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22088061-1bd9-30d2-97ac-3b099bf9d6f3 | -13.41267 | -47.89207 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21521cba-05ba-35be-9323-8cc428539e4b | -14.18977 | -45.50939 | 2025-07-08 05:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b96b947-0da5-3a53-aed4-2b2488842971 | -14.18841 | -45.50658 | 2025-07-08 05:06:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c947675-59f3-3500-877e-cfc575fde784 | -14.84052 | -48.23328 | 2025-07-08 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be72c7db-8797-3807-84d0-626400fa5dbb | -12.02919 | -57.08137 | 2025-07-08 05:06:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 103d01d5-71d0-3f5b-90da-39070c7a3083 | -18.51982 | -47.1561 | 2025-07-08 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51dfaac7-0fe2-33ad-88db-d8eddbe00563 | -13.40212 | -47.88748 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3deda114-abe5-3650-b62f-0ca936524d27 | -13.64931 | -46.81688 | 2025-07-08 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3297551-e17c-30a1-9e70-44d7554549b6 | -13.40851 | -47.88033 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6fc7bbb-cfe4-3dd6-b951-c07f26fa62d7 | -12.02533 | -57.08434 | 2025-07-08 05:06:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af7632e9-5722-33ca-86d8-f2467388b94b | -12.74739 | -60.10614 | 2025-07-08 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ce61fa8-0b7e-3ad9-bd57-c3d501f65f95 | -12.02588 | -57.08083 | 2025-07-08 05:06:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aa47a05-7d1d-3b5a-986f-ce68b4cef500 | -13.40172 | -47.89088 | 2025-07-08 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ce75189-6d33-3371-8951-2ea24de1a1be | -13.22695 | -57.13084 | 2025-07-08 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 50786754-0210-3731-a020-ab1521b6031d | -21.87488 | -52.89262 | 2025-07-08 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b509e13-2691-3058-ae45-fdfb6167bac6 | -19.59286 | -47.61771 | 2025-07-08 05:08:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5590625-be6d-38c5-8e50-a99f776ac7a5 | -19.08547 | -56.05045 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d623a42f-78ee-3fcd-a224-f4813b040e1b | -20.77722 | -49.8606 | 2025-07-08 05:08:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 51a1c5b3-0ae5-3071-8c47-4e992abe850f | -23.55574 | -54.80144 | 2025-07-08 05:08:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 927572c3-2ff3-376e-be10-ac29597bcf05 | -21.04317 | -56.0009 | 2025-07-08 05:08:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38d50243-d4e9-3cf8-9141-581b2534d3a5 | -21.04018 | -55.99584 | 2025-07-08 05:08:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5979f20a-b4e2-3eef-8af2-8a918dbbb338 | -18.65287 | -55.71764 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 45653923-719f-384b-82e0-2cd307802075 | -18.63738 | -55.72395 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f8a2bee5-7b62-3abd-a5f2-2d959a875f1a | -24.24023 | -50.74036 | 2025-07-08 05:08:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c86f616-c395-3d7c-a06f-2dd98b5b4f2b | -18.63798 | -55.71969 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 99f38f76-bddd-32b4-8311-3e85e5a872a6 | -21.87495 | -52.8898 | 2025-07-08 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e20498d0-e696-364a-a8fd-7f36f9a0b1de | -18.65343 | -55.73949 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 211e116c-3303-322f-8d86-e32427252104 | -18.64095 | -55.72451 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c7bbcfd3-4c18-3fb1-a72d-b1642a4e2d0d | -20.77652 | -49.86729 | 2025-07-08 05:08:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 289b6011-611f-370d-8113-515af42d32a4 | -21.29972 | -48.56269 | 2025-07-08 05:08:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d873117-3762-39b7-934b-3f0012cd3ed1 | -18.65403 | -55.73523 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 45b6d147-8e86-3cc0-87ec-118f2472d7db | -19.089 | -56.051 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ff321c15-d721-3a46-a8ae-dc2957ecca43 | -19.19944 | -55.75464 | 2025-07-08 05:08:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 97e36e67-759a-3864-9bf1-1eb7f44ec408 | -21.21863 | -55.94664 | 2025-07-08 05:08:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea63e47b-f3d8-32a0-a553-3a1ac1be1088 | -19.01994 | -57.67977 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b5558fe9-fbb6-3583-a312-a8b69d2fa591 | -18.64035 | -55.72877 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a9825796-795b-39e2-97d7-7c9bc16a7f76 | -20.77513 | -49.61641 | 2025-07-08 05:08:00 | NOAA-20 | NEVES PAULISTA | SÃO PAULO | Brasil | 3532504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a20d7f9c-2a26-36d2-9970-44cca9c18c9e | -20.4626 | -44.74115 | 2025-07-08 05:08:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1ec4af36-c48f-337d-8e96-4554466d6896 | -18.64929 | -55.71709 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fda9b036-aac4-32aa-bd6e-be3e7d78e43a | -21.04742 | -55.997 | 2025-07-08 05:08:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d3fbc3c-d9fb-3144-a21c-726d2dcd75c0 | -20.72327 | -56.6543 | 2025-07-08 05:08:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cedfd7f3-8be5-3571-8a94-bc4210778b7d | -20.72676 | -56.65492 | 2025-07-08 05:08:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afb4a1d1-b016-3701-9f97-d927f92a1b28 | -21.79147 | -52.76165 | 2025-07-08 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18a78286-e293-37ac-80f3-d384655e322a | -21.79096 | -52.76614 | 2025-07-08 05:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b52a7441-0c0b-3487-ae48-a16d7aa25314 | -21.04434 | -55.9994 | 2025-07-08 05:08:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26f6545b-3272-312a-8502-f5e7e23f6117 | -19.59241 | -47.62251 | 2025-07-08 05:08:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3481f3af-212f-3e97-8c8d-8765c6ef482a | -20.77687 | -49.86396 | 2025-07-08 05:08:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2a80f2de-1cac-3d3c-a8fa-692206fc9384 | -18.64332 | -55.73358 | 2025-07-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e11739b8-39ca-3446-9a0a-39afcf6e7028 | -19.75243 | -53.99635 | 2025-07-08 05:08:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a9f2d1f7-97ae-3f45-961e-c23207ed8926 | -21.03956 | -56.00032 | 2025-07-08 05:08:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e46afb0b-0eb7-3844-a1c5-d341fa2ddec1 | -21.3055 | -48.56311 | 2025-07-08 05:08:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eaa0d431-66c2-3249-9341-5c6614c7f6b2 | -11.4397 | -45.0923 | 2025-07-08 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 6b6d0f72-1e31-3b7d-b04a-5bdd11645837 | -11.4393 | -45.1154 | 2025-07-08 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 41ce8409-7032-3114-b8ee-da527e17621c | -10.6299 | -49.4504 | 2025-07-08 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 4345ab68-358c-3dc2-9a48-932649f79fe5 | -10.6486 | -49.47 | 2025-07-08 05:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 49958ded-f210-3216-949c-ede2713828be | -11.4201 | -45.1181 | 2025-07-08 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6bfdb596-954d-3207-809b-8de2fbdd026b | -5.3986 | -43.2467 | 2025-07-08 05:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bbfc97a7-7ada-35fd-88a2-d8592e028b85 | -11.4205 | -45.095 | 2025-07-08 05:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |


[Clique aqui para ver as próximas entradas](README20.md)
