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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 880c66e4-b9bd-37e7-b02c-43bb241325ad | -0.77522 | -62.8747 | 2024-10-25 05:53:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a051ef5-ef53-343f-ae2d-6c6f41ac2fdf | -0.76917 | -62.88837 | 2024-10-25 05:53:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c65a1dad-2eb5-3467-b55d-168e215d7121 | -0.77759 | -62.88482 | 2024-10-25 05:53:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ff62500-11e9-37dc-9fc2-e6d3821b8fc3 | -0.77375 | -62.88421 | 2024-10-25 05:53:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af34bfbb-d12d-3fb3-925f-31098fb27d87 | -0.77065 | -62.87886 | 2024-10-25 05:53:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d27d4f4-a95f-3d91-9773-b5bcfaac0ebc | -9.00067 | -67.03239 | 2024-10-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7bfc8c-f51a-37f0-a2ec-4b2c94ebdd9c | -8.93228 | -67.18273 | 2024-10-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb8100da-e2a1-3b9a-a42b-250b06d403cd | -8.93172 | -67.18642 | 2024-10-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ca36d1d-2cc1-32e2-852c-97fdfed484ea | -8.9215 | -67.18484 | 2024-10-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a900fa22-406c-306b-99cb-0dc755b7fd85 | -8.9181 | -67.18431 | 2024-10-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 374e18a3-7ed6-348e-814b-2cdd37e00639 | -8.91754 | -67.18801 | 2024-10-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5a246f0-b2dd-3ea6-8869-eb87895e31cc | -9.44015 | -67.14003 | 2024-10-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e2625de-d12c-3160-b5a4-75b8e7671418 | -9.43958 | -67.14378 | 2024-10-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76dfbbf0-f9e5-3837-a100-2d4173b31e23 | -9.43902 | -67.14753 | 2024-10-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d06f5c02-a52b-321b-8cea-1e0f7057c0a3 | -9.43616 | -67.14325 | 2024-10-25 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 735f3896-c6ef-3c1e-a3ce-f2ba93570d07 | -8.83968 | -67.25919 | 2024-10-25 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b1701400-0d39-3480-bad4-b7b1b13e3dad | -9.51418 | -68.59296 | 2024-10-25 05:55:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88d6474f-a5c9-3d9d-9491-3096357c0053 | -10.76485 | -68.33042 | 2024-10-25 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dc1369f-8b6c-324f-a18f-aff5123ea58a | -10.76429 | -68.51276 | 2024-10-25 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a74e17eb-92a1-377c-824b-40473cbe0e07 | -10.50687 | -68.617 | 2024-10-25 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e681567-03d4-3153-8ed9-9d67814d6d9d | -10.47143 | -68.31747 | 2024-10-25 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bacb516b-45f0-3097-9eed-185e25a1f1e7 | -10.32399 | -68.67857 | 2024-10-25 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855201be-9b34-3d9a-9c74-cdd47f8860e4 | -10.27216 | -68.70635 | 2024-10-25 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0a8f976-5462-37c6-8558-d4501e4fca12 | -10.04148 | -68.43902 | 2024-10-25 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29e9e9e9-0395-38af-9a6d-b3c0d8d0f87d | -10.04093 | -68.44254 | 2024-10-25 05:55:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06d71ab0-a3a5-380e-8075-e0c7ab45a95c | -1.18619 | -53.6676 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 70c1f38c-f379-3e66-9fee-c12db5f73f87 | -1.18215 | -53.66187 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a4ed824e-4ca9-3182-a83d-bb38b1d49b7c | -1.18105 | -53.66889 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3d8ee2bb-b568-3993-ae82-de46610dd2f3 | -1.17998 | -53.67564 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 939f32ee-fc38-3981-9607-27779a844336 | -1.17927 | -53.66559 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 815bdbfb-b839-3b67-840b-eb222ea5a24a | -1.14164 | -54.10328 | 2024-10-25 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 57cc02d4-968f-37cb-bb94-009310143315 | -1.0734 | -53.66508 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 185a4007-0699-3189-8191-12e99338242d | -1.06944 | -53.65944 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1860944-35e4-34a3-b497-e172bcda421a | -1.06638 | -53.66381 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7848cfe7-97f3-311c-9903-844870ca07e7 | -1.21257 | -54.19547 | 2024-10-25 05:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2afcaf6-6aaa-3bb6-afb0-9228a7399161 | -1.18793 | -53.67105 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abef88cc-d042-393a-828b-91da14de408f | -1.18513 | -53.67464 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3a38d768-3e0c-39a1-91fd-66ba5732f540 | -1.17825 | -53.67236 | 2024-10-25 05:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| aa2865c9-c2ac-3f21-9a5f-1240896b59b2 | -1.07542 | -53.66729 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6badef6f-80e9-3132-b30c-2b2abfd51507 | -1.07444 | -53.65815 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e43ccd81-5cd2-356d-b008-4ac0b5d6103d | -1.07248 | -53.6712 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f60b158b-7fe0-3798-9b45-543a78b2abb1 | -1.06836 | -53.66634 | 2024-10-25 05:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce79ecb5-1012-38e1-9525-e941b547de61 | -12.02686 | -57.08512 | 2024-10-25 05:55:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b9898c98-dd8b-34f8-ab7f-6fa7094c00f1 | -12.02496 | -57.08405 | 2024-10-25 05:55:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 81c967c1-36aa-3da5-9427-614ae0c23119 | -12.02435 | -57.08976 | 2024-10-25 05:55:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 79ca55bc-6475-364e-b3f1-aee27bf0fc1c | -11.90031 | -56.41088 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee97c39f-79c2-3207-8058-c372065c9654 | -11.89986 | -56.40913 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0e187bdb-53d7-3024-9e49-9b274f6bb42c | -11.89344 | -56.41001 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 75e0013a-799c-3108-9968-b10d5775896e | -11.89299 | -56.40828 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f62eae1b-cbaa-3d21-bbf2-c2b7455ff757 | -11.89275 | -56.41656 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27b0d8d1-80d1-3e26-b208-bdc2fb9321e1 | -11.89226 | -56.41481 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d1182d36-f936-3bad-9174-cbe5bbbc4c49 | -11.88644 | -56.21627 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e672f2d3-d56d-306d-980d-503bdf5d0756 | -11.8795 | -56.21542 | 2024-10-25 05:55:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 079ed118-6bde-3f14-a69a-1e1c4d0a3d70 | -5.24969 | -55.96448 | 2024-10-25 05:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32980182-7c7c-3b88-aa2a-88a7522e39fa | -5.24894 | -55.96989 | 2024-10-25 05:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e6cba6c9-e947-37bd-aabe-78d413a2af15 | -5.24319 | -55.96354 | 2024-10-25 05:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ed9a767-3413-3bfc-b244-1f56cb6b7c55 | -5.24245 | -55.96893 | 2024-10-25 05:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d120808-5021-35d4-9c8f-544c280cd3b2 | -6.54893 | -58.4733 | 2024-10-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4c76334-717c-3eb3-8d69-d59a39a7f0a8 | -6.54621 | -58.47456 | 2024-10-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2983c598-cd10-3097-a1e2-b13e5b762eb7 | -6.54671 | -58.47079 | 2024-10-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82948f0e-aea4-3cda-9158-a7f78ddf7e9e | -6.54327 | -58.4726 | 2024-10-25 05:55:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8315065-829c-36ea-966e-86fc3ef2dc8e | -10.39246 | -58.42092 | 2024-10-25 05:55:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3f38f02-8af3-3b03-abe1-ac69180d7116 | -7.09185 | -59.27945 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67ec74fe-7716-3d4a-b229-c9399c44c644 | -7.08931 | -59.27997 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2bcfc15-8709-30f8-89d6-d372fe94184e | -7.0233 | -59.78513 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 818dacb8-4000-38f2-aa4d-47276277a9b5 | -6.76247 | -59.12041 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f68ef7f-9b0c-39d9-b38f-3472673cec59 | -6.76199 | -59.12389 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbcfd331-69fb-3c9e-b356-093684403874 | -6.75752 | -59.11625 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef052b25-e1a6-37c6-851a-9f6211c6c391 | -6.75704 | -59.11972 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8543f3b4-a2b8-3b52-8823-af3f27cfe61b | -6.75209 | -59.11549 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3b82f57-f570-351c-990f-7b608416f291 | -6.75161 | -59.11895 | 2024-10-25 05:55:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fafac677-bf5c-3ed2-b152-a73aaf2ae283 | -6.53171 | -60.03663 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ffa4a9b-3362-3eb1-9b50-a65af8e5e6f9 | -6.52709 | -60.03269 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83b1149a-9878-3f1e-95d0-ba504cb8c319 | -6.52666 | -60.03573 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5046f9a1-86b9-392d-a13e-0b40125f75b7 | -6.52623 | -60.03876 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 693a3fc0-60bd-3b3a-9813-b7312696b4dd | -6.52202 | -60.03186 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00d18460-3bb8-3947-9265-dc93c6ea24ad | -6.5216 | -60.03485 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 380ef9ab-3ffa-3a8a-8da2-ddc179ae41f2 | -6.52117 | -60.03785 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6d451265-2e03-32f6-91b0-ee213d11dd9c | -6.52075 | -60.04087 | 2024-10-25 05:55:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 69c25c7c-01f3-3693-ae59-d9e85c85beb7 | -10.42494 | -61.2896 | 2024-10-25 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ebd9b69-d4f3-31e2-bc8f-2664b550baf3 | -10.42416 | -61.29549 | 2024-10-25 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03d2a40e-e8e0-30a9-9ebf-77672681b323 | -10.36265 | -61.21525 | 2024-10-25 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78fd5962-5b48-3593-96c1-a007123650fb | -4.52069 | -61.14183 | 2024-10-25 05:55:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 299204a9-1a20-30eb-97da-64147013582f | -4.51613 | -61.14115 | 2024-10-25 05:55:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 161be7ed-2d9b-3056-8f2e-1522a014b7d1 | -7.79816 | -61.35319 | 2024-10-25 05:55:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fe4cae7-c2ab-38c0-86f9-cbf0a5e384f4 | -9.80816 | -61.51926 | 2024-10-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38a5b23b-c965-3d9e-93d3-29653acd82bb | -9.80334 | -61.5186 | 2024-10-25 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3334805c-616b-3da8-9cb8-0b300a1e76e3 | -10.20584 | -61.39732 | 2024-10-25 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7512d405-6b4c-3091-a28c-b7e09a84a9bd | -5.64706 | -63.16991 | 2024-10-25 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9bb165f-dfc3-38dd-bfe4-29c6251ea3e9 | -6.53385 | -62.9449 | 2024-10-25 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4844cac1-79bb-3ce0-8cb1-169f5ea5f8f8 | -6.52914 | -62.94807 | 2024-10-25 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb57ec2e-df60-35b5-85d1-60f98d13dbf3 | -6.52858 | -62.95186 | 2024-10-25 05:55:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 438bd057-fd58-31d0-8ab4-0b55484bca4d | 0.12566 | -62.56216 | 2024-10-25 05:55:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f0b80db-2c45-36f6-b812-17120a64fa5f | 0.11793 | -62.56338 | 2024-10-25 05:55:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be388fe0-6c8a-3010-a2a1-f040abdca361 | -9.37661 | -64.45148 | 2024-10-25 05:55:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c22fdb05-85f6-36ba-8fd4-b2582fd649b0 | -3.30124 | -67.94094 | 2024-10-25 05:55:00 | NOAA-21 | AMATURÁ | AMAZONAS | Brasil | 1300060 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2aedaa5-984a-3894-aeae-2396bb66c119 | -8.47324 | -69.69576 | 2024-10-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e7c885d-5e47-3ea3-841b-b0154a70f8fe | -8.46992 | -69.69524 | 2024-10-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 404374ac-908d-31f8-844b-b97f9dfacb25 | -8.4666 | -69.6947 | 2024-10-25 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 610a09be-1de9-335c-a888-b947853280d1 | -10.73645 | -69.24271 | 2024-10-25 05:55:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README109.md)
