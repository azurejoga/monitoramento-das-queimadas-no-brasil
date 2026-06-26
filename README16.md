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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9c5da07-3fbc-3dfb-96cb-70a3ecbb9f6c | -10.39382 | -56.76036 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c21283c1-55c8-3b0b-8ded-8132f42d97ae | -14.62886 | -54.45858 | 2026-06-26 05:38:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 503ab720-a0a6-3e4f-a79e-8500936e281e | -12.07884 | -54.60683 | 2026-06-26 05:38:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9170ebde-e2bc-3cdd-9f54-f4f191a1bad9 | -12.76988 | -59.00372 | 2026-06-26 05:38:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a279aa75-7b1f-3b12-be17-08c2befdbde8 | -10.39312 | -56.76566 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c6aa0588-ba7d-3ce9-8155-72052043d799 | -12.17032 | -59.75812 | 2026-06-26 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 087a8ee6-c8e2-39e3-8f3a-5fe9e61eded1 | -10.77897 | -54.10791 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0184495-0220-3128-b3db-9d95c7e12f55 | -12.62924 | -57.88895 | 2026-06-26 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 034d53f1-a322-3a40-8a50-d59ea3eae019 | -12.62463 | -57.88837 | 2026-06-26 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 23a46e70-9ef3-3000-98c6-a217f4ca16ea | -11.91594 | -57.10263 | 2026-06-26 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b12e17f4-ea73-30ae-865f-1d55d93f0917 | -10.28143 | -60.53988 | 2026-06-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 138442e8-bfcc-37fa-99a2-42343ae785dc | -10.02022 | -59.3496 | 2026-06-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 639f2a0b-e25c-3ffa-b589-703d4018426c | -10.16205 | -56.62668 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da03a9f9-ac72-3c4c-a234-5f92806910d8 | -10.77954 | -54.10909 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4131687c-8180-3f0a-bc54-5ac26787816a | -10.39792 | -56.76646 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a0e8be1e-e049-394d-bb1c-e236833881a3 | -10.39242 | -56.77096 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cbb8502-a4b3-3cc9-b215-d10159809a08 | -12.55511 | -54.58686 | 2026-06-26 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5ed4ba3-838c-318c-8b6c-b76ce457c6fe | -10.38485 | -56.71649 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5640023c-5124-3e9e-9327-54b624465181 | -13.73425 | -54.04779 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d03db16-ca1a-31d0-84bb-4eff8b246b7f | -11.41396 | -54.43731 | 2026-06-26 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff5642f7-1811-37d5-9ee9-33fb66bc10bc | -13.7379 | -54.05032 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a82707c-996d-351d-bdb2-79912a970d46 | -11.92076 | -57.10323 | 2026-06-26 05:38:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e878b972-9cc7-32ca-9c6b-82960ab3b744 | -11.87365 | -51.72647 | 2026-06-26 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0109fb26-f0d3-3e93-bd86-e7939979f2f5 | -12.55464 | -54.59095 | 2026-06-26 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e6a8fa5-bb81-388a-b592-21933e48d261 | -9.89668 | -57.4006 | 2026-06-26 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4fe2464-eaa6-3ff6-9a12-12227073e108 | -16.12458 | -58.4936 | 2026-06-26 05:38:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e4b2fa89-e17a-31df-b51e-1d1fb40c342f | -13.73238 | -54.04504 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a71e955a-b60a-3a7d-9760-c7a4c395ef43 | -13.73474 | -54.04313 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56e6198c-64d4-3969-9dc4-3ae4a0811e93 | -12.55417 | -54.59502 | 2026-06-26 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cde1c853-d30d-366f-99c8-99fd8ff71f4d | -13.72741 | -54.03479 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95e8a749-157a-37c0-b667-2ebd2dd44908 | -14.34922 | -54.52826 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fc71fb5-f4f6-32f2-a2ce-b33cdc32a425 | -12.62401 | -57.89314 | 2026-06-26 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| df1de609-d58f-33d8-89c8-044f54f95a50 | -11.64292 | -52.86284 | 2026-06-26 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d80e2a44-1fc6-3720-9748-7689eef1678c | -10.58035 | -57.32249 | 2026-06-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da7e1907-9b82-36fc-ac84-24f11053f9d6 | -13.06205 | -53.35613 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5651fdf4-c73c-3b83-a15c-49cfdaf4c451 | -11.41967 | -54.43809 | 2026-06-26 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71e4a447-c7cc-3674-9c98-aeb87ccfab54 | -12.76934 | -59.00781 | 2026-06-26 05:38:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0d9cef5-fcf4-3e3d-8863-56b153ca2012 | -13.25833 | -54.42697 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 53fb3532-6ad5-382b-8c96-823a6adff5bd | -13.26466 | -54.4236 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c64eb639-d89d-3512-9ed7-6f1c2f900f84 | -11.51635 | -56.13221 | 2026-06-26 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a942620e-3a8f-3cad-882b-8f9377cc03ca | -10.27768 | -60.53931 | 2026-06-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db61ea6c-7f55-35cb-b5f5-e19b459f866c | -13.25785 | -54.43118 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| fc254476-e264-312b-8312-d2571b814d64 | -9.90126 | -57.40127 | 2026-06-26 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| add1d39b-5419-31f1-9edb-ba835e3c8e24 | -10.16486 | -56.60509 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7307c7b1-bb06-36c9-91af-c71f21a41895 | -13.25881 | -54.42284 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bbdc847f-a0c2-3242-b0b3-c568a2cacf59 | -10.02424 | -59.35017 | 2026-06-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20d59dbf-476c-3346-a7e9-4048ed58cf79 | -10.01972 | -59.35313 | 2026-06-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb9eda93-eece-3bb3-ad24-73ccac4be78c | -11.63658 | -52.86213 | 2026-06-26 05:38:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 736ba80e-625f-3c19-8edb-ed82e016f48b | -10.15999 | -56.60447 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75ec3a8d-ce47-3943-9d12-002650e377b2 | -12.62862 | -57.89371 | 2026-06-26 05:38:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac75ab4f-d77c-3851-a81e-9f70ae7c0a0f | -13.26418 | -54.42776 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1dde810d-ad5a-3a66-b172-3bd9e21eaf01 | -9.94151 | -65.01476 | 2026-06-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 066d9da5-3dfd-3440-b93e-be84fd0cbea6 | -14.63431 | -54.46375 | 2026-06-26 05:38:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69105718-fbf6-34a3-aa59-b4db69ece528 | -10.16416 | -56.61047 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af419ddc-3bb8-39c8-b1bf-b446677ce947 | -11.21257 | -54.3413 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef1d96df-475e-3f69-9236-62f4c08d6c90 | -10.93832 | -56.85352 | 2026-06-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1b41604-9cdd-3c43-8b9c-be70a12767b9 | -13.73573 | -54.03374 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1cd8d65-d511-3566-9109-7b781b86315d | -9.78872 | -56.94438 | 2026-06-26 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0badc74b-d4ab-3716-99ef-460651e44b23 | -11.21355 | -54.33312 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25ec0ef6-3f4b-3bee-a2a7-a5fc780627f8 | -8.98545 | -63.88487 | 2026-06-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 10f5a41a-cbd4-3564-8d15-2f6a47ba1748 | -13.72584 | -54.0488 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f705cdb2-3ce4-3fe2-ba0b-151ec090397d | -11.94248 | -57.70402 | 2026-06-26 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53e6bc58-8a18-3015-b0c4-49ddcdb3e7b9 | -10.78003 | -54.10495 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9285f1c-6dd6-392b-8339-a941fd6b4847 | -10.38417 | -56.72172 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a8b2c4e-295a-3419-ba1a-439068341718 | -11.21306 | -54.33723 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6be84cc3-8c77-33f1-a4d3-07275c685251 | -13.73524 | -54.0384 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41eea5d3-c090-305e-9c4c-d8a88e6823ad | -12.54644 | -57.20737 | 2026-06-26 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28896cc6-41bf-39ad-a1ea-5511bee01f6d | -11.87141 | -51.72782 | 2026-06-26 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 020543ee-c4bc-3580-97f4-d23293f507f5 | -13.73343 | -54.03562 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fa69ba4-9819-313f-bb41-d5fc7ba8a929 | -11.89175 | -51.73066 | 2026-06-26 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 857dafff-caba-30f1-a50a-135f9541b81a | -9.89211 | -57.39995 | 2026-06-26 05:38:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6a63e32-cd30-3655-8bb7-5884aba53b5c | -10.39722 | -56.77174 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbef743f-1dab-3f5e-bdfc-1102ab1b9643 | -13.27004 | -54.42847 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b40b1de8-8fb3-3f0a-84f6-3d80b4e50526 | -13.26944 | -54.4288 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b42d535-dd5d-30f4-8b77-9e90dde06e5c | -12.76507 | -59.00718 | 2026-06-26 05:38:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f170fb4-d798-3154-98c8-0cdc392529a2 | -14.3497 | -54.52381 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3410c642-c343-3570-b7cb-8fb1a2bf32a3 | -10.39862 | -56.76116 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d67534ae-a458-3cf4-ba77-70d956f9c68e | -10.7795 | -54.10374 | 2026-06-26 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95ce6351-394a-3814-b449-26910a86ef8e | -10.38971 | -56.71693 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc7dbacb-21a9-39db-b2dc-7d1b9d05967a | -13.2753 | -54.42953 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b68eb958-debc-300b-bae4-d2fae8e6782a | -11.51673 | -56.12917 | 2026-06-26 05:38:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a189259f-dff3-32f0-b529-421fae4aa5d4 | -13.73186 | -54.04965 | 2026-06-26 05:38:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 828dc455-adf6-35c3-a564-1569fad070c6 | -11.89399 | -51.72946 | 2026-06-26 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 82ccded0-120e-3dc7-91e8-f061881475f1 | -13.26369 | -54.43198 | 2026-06-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5510d2af-19c4-3efa-8705-53d5b603b2c1 | -10.38902 | -56.72218 | 2026-06-26 05:38:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da3c7d77-f271-3086-8d92-f78b44dbe257 | -5.7945 | -45.0586 | 2026-06-26 05:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 081f8dcc-06a4-39b4-893a-cc77608c0473 | -5.7758 | -45.0599 | 2026-06-26 05:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f5972eb7-ac64-31b6-b107-ccc39e3f2373 | -5.7758 | -45.0599 | 2026-06-26 05:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b78e8096-5b7c-3c5f-89ae-f5b86ce41a8c | -7.75012 | -44.60689 | 2026-06-26 05:57:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 55c2c8f3-3f48-3caa-bcba-14f174c6159d | -5.78849 | -45.03264 | 2026-06-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| bb21121c-4446-3cc2-a90d-cba9f2f0e942 | -5.77102 | -45.05379 | 2026-06-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| dce140a6-5218-3201-8179-3729d34c2f26 | -5.78477 | -45.05589 | 2026-06-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| bc0ecb4a-a34c-3c0a-9f07-af821695e90b | -6.98137 | -42.89407 | 2026-06-26 05:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.0 |
| b354a2ea-d4f2-37cc-947c-066c2611d825 | -5.77601 | -45.06209 | 2026-06-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 6d3ea6ac-acc4-374a-b416-9b77210a0f7f | -7.74693 | -44.62613 | 2026-06-26 05:57:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 29e063df-5506-3142-b907-e63ce010077f | -6.97011 | -42.89233 | 2026-06-26 05:57:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 7b909717-4a74-3a43-8a4c-948ff0efe650 | -6.49928 | -42.21554 | 2026-06-26 05:57:00 | AQUA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| fe2c5bc7-1ae0-3c32-8b92-d0f37a3d6c2d | -5.77995 | -45.03877 | 2026-06-26 05:57:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| cc2e6f33-64e5-3e44-91d8-ac38caac6fd4 | -15.59675 | -48.34197 | 2026-06-26 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| f8e29aeb-6a41-3f03-9fbc-a6bed1a611f0 | -15.59506 | -48.33559 | 2026-06-26 05:59:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |


[Clique aqui para ver as próximas entradas](README17.md)
