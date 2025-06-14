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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a1cdceb-2100-3094-a7fc-6cd7df84c309 | -5.7724 | -43.484699 | 2025-06-14 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6273b5b-e36a-3c3e-8905-3ac468c5a8bf | -7.22 | -43.121399 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f96deb0d-fc2c-3813-967a-8f20639266b9 | -9.5101 | -40.327499 | 2025-06-14 00:05:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fa7632ac-5e36-39d0-a027-26322549a9ca | -6.9485 | -42.9118 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a4d1c59-1d71-325c-9d6e-9ebb327606f0 | -7.2375 | -43.107498 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ed3114d6-8f9e-38e3-b607-98f9a240e297 | -7.6382 | -43.676601 | 2025-06-14 00:05:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2cf652-bb02-3618-8074-42181db45744 | -7.1798 | -43.546101 | 2025-06-14 00:05:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8b3817f-1998-3be4-ad65-0411fb8242e2 | -7.2302 | -43.5891 | 2025-06-14 00:05:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50b3015a-578b-3760-b3dc-6f762964e261 | -7.2473 | -43.1054 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3afbabc9-df01-324c-84a5-b2af31ee3709 | -6.2098 | -43.329399 | 2025-06-14 00:05:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a06dec8a-c428-3672-8168-ad62b040fb63 | -15.1031 | -49.619499 | 2025-06-14 00:05:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7619a9d3-09bb-361d-bdaa-2216c0199563 | -8.0806 | -43.120899 | 2025-06-14 00:05:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 221bdb1d-2694-3e24-8b28-ed772ed24cbc | -6.6089 | -43.886002 | 2025-06-14 00:05:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc94ee5-0da5-3951-986f-47819f626acf | -8.0708 | -43.123001 | 2025-06-14 00:05:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 15d80d2f-0ff2-354c-b831-2a92401442f4 | -7.2354 | -43.097801 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ff30c78-4cae-3ad5-b676-009811a20b41 | -6.5991 | -43.8881 | 2025-06-14 00:05:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97f634a7-b156-3ba2-9b5f-b572ffdcc201 | -6.9574 | -42.813 | 2025-06-14 00:05:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7cf1b5d3-6a78-338c-ae52-cb4234da4515 | -7.1775 | -43.5359 | 2025-06-14 00:05:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6fa5d9e0-6c33-3bd8-ae32-1c71d6ea628d | -6.9444 | -42.8932 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 88a20b86-fb5d-3a48-998c-a2373d368c57 | -6.9522 | -42.881802 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 20332abc-79e4-3c5e-868f-cd55a807046e | -7.2256 | -43.099998 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 581dd1a6-9748-38c2-b201-dea843252bc2 | -8.0686 | -43.113098 | 2025-06-14 00:05:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c8e7d735-9cc0-3cc5-8404-d9f8fd30b6a8 | -6.6014 | -43.898602 | 2025-06-14 00:05:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36d6d605-9b80-33fa-94eb-430873011fba | -9.4015 | -48.408798 | 2025-06-14 00:05:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6826243-bed2-36f7-b2d4-b13814cd640c | -7.2158 | -43.1021 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf39a549-336e-3bbe-a224-1a6c6d3d850a | -6.6038 | -43.909199 | 2025-06-14 00:05:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d769e5ba-2087-3ea8-b359-3bdde6bce547 | -6.9464 | -42.9025 | 2025-06-14 00:05:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 46321fef-38f9-398e-8571-9731b0fbcbaa | -5.7801 | -43.472801 | 2025-06-14 00:05:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e072fdd0-abd1-317f-87b7-57cd2a1569c4 | -14.2121 | -57.4098 | 2025-06-14 00:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7b3965b4-1cfa-3248-aa17-48196efbea9b | -11.8156 | -57.3612 | 2025-06-14 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 38c32f45-d0a3-3d72-9c1e-d5c1351bc6a7 | -10.9167 | -56.8336 | 2025-06-14 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 62e11fc1-a0e2-3c34-92fe-95c881397ba3 | -7.2214 | -43.1153 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 06b691b5-f229-335f-a964-7c7c8e89813b | -6.9416 | -42.8834 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| e742c4ee-f834-34b8-ac09-3ed6de376275 | -11.8158 | -57.3413 | 2025-06-14 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e35e74f6-64d5-301d-8b9f-33afc23f7230 | -6.6112 | -43.8941 | 2025-06-14 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b15a22a3-e0d9-3e04-9bf6-09ed6158ed09 | -12.6236 | -57.8926 | 2025-06-14 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c409f825-1843-3b83-8234-9e48840f1906 | -11.7967 | -57.3627 | 2025-06-14 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d494191e-5530-35f2-8815-e792300c66b0 | -7.2217 | -43.0917 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| f20a46f4-83e0-3617-a29c-a74b4bd7e348 | -11.0113 | -55.0764 | 2025-06-14 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 10f71ebc-bc20-331d-8146-67ca4e7489d0 | -10.9205 | -54.7795 | 2025-06-14 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1a6497df-d322-35d4-8419-750657488424 | -7.2405 | -43.0899 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 499388fe-1f96-3179-957c-cf52d3477c26 | -9.393 | -57.5147 | 2025-06-14 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8412894e-d3ac-387f-92be-6fb7e6bd2c5b | -11.7969 | -57.3428 | 2025-06-14 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| af38d191-b835-3c4a-a222-7a5f83e79254 | -10.9355 | -56.8322 | 2025-06-14 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| e432b719-df31-327f-8a25-41395547bdd8 | -6.9605 | -42.8816 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| e897a5bf-dbfb-3432-b0d2-8a2bbc1b0e3d | -13.8867 | -54.6312 | 2025-06-14 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 482704a4-eb3a-3859-9e52-d1701111cc25 | -13.887 | -54.6106 | 2025-06-14 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 1a373507-c831-3127-abad-0e610d645134 | -16.1967 | -46.4589 | 2025-06-14 00:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 69a87272-aa7f-3659-9511-251d63433d4f | -7.2403 | -43.1134 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 3181672e-7b85-3973-a132-d294b30b44fd | -9.3929 | -57.5344 | 2025-06-14 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9b0e72e2-c3d8-31bb-9cf0-887410bf40fe | -13.9062 | -54.6084 | 2025-06-14 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 438d99e4-2299-3f89-8639-2c487ded57d8 | -11.011 | -55.0967 | 2025-06-14 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| c9980391-95ff-3bd0-a66c-29c75b50b909 | -6.9602 | -42.9052 | 2025-06-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.6 |
| a3be7252-5ad7-35dd-bec1-e9fa2957d0fa | -10.9353 | -56.8522 | 2025-06-14 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| dd0c0c9e-c76f-31d9-aff9-ee9116d5d20b | -6.9416 | -42.8834 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 24ffe8e7-d6a0-3bd1-a087-e05d6c11f3b1 | -13.9062 | -54.6084 | 2025-06-14 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 33c3a817-3de0-3ef8-9f49-a9a2ed32f1b1 | -12.6236 | -57.8926 | 2025-06-14 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 316cfa59-b73e-327e-83d9-91066ee24a53 | -13.9059 | -54.6291 | 2025-06-14 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| fd3e46a6-b3fa-3718-bee7-257856bb3a82 | -21.452 | -54.5675 | 2025-06-14 00:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 74b46760-bd3a-3588-896c-83e15e0af078 | -10.9355 | -56.8322 | 2025-06-14 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| b93b7a16-a966-39c4-a9c7-11e704640bdf | -11.7969 | -57.3428 | 2025-06-14 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3cfece2e-0770-33a5-a6c2-ac43bafb9c9f | -11.8158 | -57.3413 | 2025-06-14 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 628cd6d9-8166-3e98-998f-fb4350c95ab7 | -6.9414 | -42.907 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 6cc5f31d-6cba-34ae-8865-1380043bffb8 | -11.011 | -55.0967 | 2025-06-14 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 81f4e154-49d3-3c25-acfe-b764ec8314ae | -13.887 | -54.6106 | 2025-06-14 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 08d12576-0f2e-3946-9d98-3fa48618f33e | -7.2403 | -43.1134 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 2fdf67d3-19ae-393d-86c9-d1e359b2f7a9 | -11.0113 | -55.0764 | 2025-06-14 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| e9be79df-3728-3f82-a717-bf73b097e7fb | -6.9602 | -42.9052 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 7d85f642-32e0-38d5-a6ce-4ffbc24a3f61 | -6.9605 | -42.8816 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.1 |
| b8c385ec-1cdd-354e-b2a4-aaf1a50404a6 | -7.2214 | -43.1153 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| 1dbfd050-f15c-34ef-a12f-8cfe8c9ef34a | -10.9167 | -56.8336 | 2025-06-14 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8a1db948-c34f-3c2d-aad3-75c58348551c | -14.2121 | -57.4098 | 2025-06-14 00:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f1ac2314-080e-3b87-859d-6c134bbabc56 | -11.8156 | -57.3612 | 2025-06-14 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 157db7ef-ff67-3b7b-b07c-8ae8bc14180e | -10.9205 | -54.7795 | 2025-06-14 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f4d13b05-c16a-31ae-a3cf-f8662b79a0d5 | -7.2217 | -43.0917 | 2025-06-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| ba3553b6-b772-3c3e-a6d4-a5fda91c0a0d | -9.393 | -57.5147 | 2025-06-14 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1c4ad454-96bf-34e9-9d33-e0b3eedb763e | -10.9353 | -56.8522 | 2025-06-14 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 113aa51a-ecc6-362b-a4d9-c50a90e22aba | -10.9167 | -56.8336 | 2025-06-14 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7c997c35-cf23-3c38-99c8-9c2ea296b32d | -10.9353 | -56.8522 | 2025-06-14 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6b1eef32-5aa7-3743-87e8-d0d340190459 | -7.2217 | -43.0917 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 15ce0567-5287-3006-a424-e658e59c9ba1 | -7.2214 | -43.1153 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| fd539f51-9615-368b-a7cc-ef57a01feb25 | -6.9416 | -42.8834 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| 4ab3f783-9bad-3760-9f0c-f545fdb73c65 | -11.8158 | -57.3413 | 2025-06-14 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ad6db57b-7d5f-3d26-a362-5f2266f8c8d5 | -13.9059 | -54.6291 | 2025-06-14 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d6a69114-53f8-37bb-99c2-3f4c61b97147 | -11.0113 | -55.0764 | 2025-06-14 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4ba7b9db-2684-364f-8e4e-f92213363012 | -6.9602 | -42.9052 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| b4d858e3-54f7-38ab-ad59-0eb61402604b | -12.6236 | -57.8926 | 2025-06-14 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 6c43bd8e-9aa6-394d-a27e-15dfa6dfe3be | -6.9414 | -42.907 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.1 |
| 8c665e34-b04b-322d-8777-d5c8449802b2 | -7.2403 | -43.1134 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 9a9af94b-6f25-3d7f-8841-1a9c0fe5bc87 | -14.2121 | -57.4098 | 2025-06-14 00:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 1ee0fac9-e3f3-3d6f-bab2-f8f6e79609e9 | -13.9062 | -54.6084 | 2025-06-14 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 30246729-21db-3a94-9d05-55a63aa955a3 | -6.9605 | -42.8816 | 2025-06-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| e6a62e36-ad91-3f94-a46a-3fb2a7b3f8db | -21.452 | -54.5675 | 2025-06-14 00:30:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 8708d977-a95d-3e6d-850f-47bea89d54ef | -11.7969 | -57.3428 | 2025-06-14 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7bd6f3c7-3704-3bba-899a-391873b433d8 | -10.9205 | -54.7795 | 2025-06-14 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 71e1c164-fb36-3028-a04b-62d03faa8ff4 | -16.1967 | -46.4589 | 2025-06-14 00:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 93fb139e-1e19-33e0-b984-8bb688f01411 | -11.011 | -55.0967 | 2025-06-14 00:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9bed64d7-67b2-3c3c-afb8-1e1c4b6dbd44 | -9.393 | -57.5147 | 2025-06-14 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 400125f3-759a-37ac-9311-0b903e23f4f4 | -10.9355 | -56.8322 | 2025-06-14 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 3b668741-aafc-3886-9dbd-8ff32c840846 | -13.887 | -54.6106 | 2025-06-14 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |


[Clique aqui para ver as próximas entradas](README3.md)
