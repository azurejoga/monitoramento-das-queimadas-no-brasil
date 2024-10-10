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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3cf91be-9d48-3e9e-bf92-d4758e718580 | -2.67126 | -53.3474 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 43340c87-6752-37e7-b6a0-aa579846a107 | -2.67123 | -53.33991 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cbbde190-d9ca-3a97-81f3-adbc870e5d4c | -2.67058 | -53.35157 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 76f0aabe-087e-3695-b1fd-b8c58581b3ec | -2.67058 | -53.34407 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d3518928-3e3a-3d4a-a285-3ac65ab79c00 | -2.66992 | -53.34824 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 87435c64-b419-3a4f-9ce4-d71f73f5ebe3 | -2.6699 | -53.35574 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 61a06c22-4a66-36f9-a01e-d785d90e3673 | -2.66927 | -53.35241 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 145747cb-5892-3978-bd2c-20789de25f1b | -2.66696 | -53.34349 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 637fdb29-e61f-3a82-92c8-d0f9e498a141 | -2.66631 | -53.34766 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 1d70aa69-f346-3cd0-a846-d2d3c9b24f64 | -2.66565 | -53.35183 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 632ee7f1-07b7-35a0-bbd0-58484990c864 | -2.665 | -53.35601 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 52c7972b-ced4-3b2d-a083-def52dc7e837 | -2.66335 | -53.34292 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 0db7acfd-60c0-3a99-b319-eadfa4369490 | -2.66269 | -53.34709 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 484ba613-5654-3f0d-a6c2-95a54e342232 | -2.66204 | -53.35126 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| e17ba0cc-ffc1-3be9-8e15-1b4833b4a8fa | -2.66138 | -53.35543 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| b5d09226-fcea-3ec0-b87f-12e3b2a9fbb4 | -2.65908 | -53.34651 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 6c53c13f-76d2-3515-a45d-459d6f5cddbf | -2.65842 | -53.35068 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 70f096e9-8f8e-3ce0-ad51-e9b0b1efc6c8 | -2.65777 | -53.35485 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| bbc3a808-1712-382b-a122-d4b66eec0777 | -2.65711 | -53.35904 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 71091617-8ab1-3cd0-9b75-dcf05d444403 | -2.65546 | -53.34594 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 771c6aff-986d-3c4a-ad3c-24ca061ba81c | -2.6548 | -53.3501 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f6d646b9-b096-344d-b508-f9840e93eb70 | -2.65415 | -53.35427 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2bf0ecb7-1bd0-326a-91ff-e6f1bb83fecd | -2.65053 | -53.3537 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1c4ef4cd-0d01-3b58-81f5-638f63fc623e | -2.25286 | -53.47794 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 713a6488-a227-362b-83fb-12970a7abf3b | -2.24988 | -53.47314 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07a5f055-1d89-3474-8b57-1a76e797bb9a | -3.37527 | -53.29957 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44a16130-e1d8-341b-a464-716e1d3dd4c7 | -3.3549 | -53.38048 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2683a9ae-46ee-301f-9217-cdbafa8eca7f | -3.33426 | -53.39413 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dad75f2f-e96a-396d-b689-4bac646e4e0f | -3.33372 | -53.22271 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ce342122-652a-3bf9-b654-23da84c40c2b | -3.33308 | -53.22675 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a6dfc12c-dd0a-317f-b88e-e115262f21d8 | -3.33015 | -53.22215 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 559275d9-f34c-356a-8a2a-f20336ed07f6 | -3.32951 | -53.22618 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8158e5c7-bf7d-322b-9aee-2fd2d71aa47f | -3.32773 | -53.38889 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8497d29a-90f2-3772-993d-1d3482fd8cc8 | -3.32722 | -53.21754 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e1dfce7-b2fc-3a21-9f42-1215b7bcd27e | -3.32706 | -53.39303 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db5f3d8b-2a26-3b9c-9149-14c7f4ba3112 | -3.32658 | -53.2216 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22429bba-06cf-3f6a-8d82-d933240e0c56 | -3.32594 | -53.22564 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aac984ca-1744-3084-b790-4c4cc5243077 | -3.2311 | -53.27848 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d578f95a-9343-30da-bac2-0c7473a6ab8a | -3.23043 | -53.27297 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3fddddd-41fe-31f4-81fd-bbbf833d9c04 | -3.22978 | -53.277 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27c9a192-4ce3-36e0-bc08-6f7e4363d9b4 | -3.22912 | -53.28106 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50c28a73-162f-318a-aa6e-8af39819a9bd | -3.22815 | -53.27387 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa50a03b-33e2-3e84-8fa8-55503df41918 | -3.22752 | -53.27791 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d84b8b7-9a69-350a-80f0-83173ef51c5a | -3.22686 | -53.27241 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8516703-ca03-3c87-bea2-3d53c22f252d | -3.2262 | -53.27644 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b9e0cd1-1890-3d77-a10e-aaebe15af667 | -3.21912 | -53.00859 | 2024-10-10 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a027548f-d1e5-36dc-88ff-8acdb38e948c | -3.81172 | -52.30378 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e34b587a-b1a4-3974-bf78-a2170775e25c | -3.80415 | -52.41629 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69d01b7c-08a6-3e5f-af6d-243029a0f43f | -3.80355 | -52.42003 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 170d6d8c-02b5-30bd-b6c1-7dfa59a516f1 | -3.80102 | -52.41629 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d440920-7472-3d57-b3fd-70352bf8438a | -3.80072 | -52.41574 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94669229-8c15-3983-b807-1ef5005abe53 | -3.80023 | -52.33212 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2727f9b0-1240-3cc1-8460-781022205c3f | -3.73641 | -52.31465 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1962e91-b63f-3953-a4ce-0814b6bf3280 | -3.733 | -52.31408 | 2024-10-10 04:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 31eaf1f5-1ade-3695-9449-8e8e8ea09292 | -3.72362 | -52.26341 | 2024-10-10 04:42:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c2b8748-0ff3-3274-aca3-d5c7bd62fb1b | -2.23182 | -53.65629 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1281dc2-be49-3276-bfe6-15fd416e4836 | -2.19473 | -53.74513 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 586d171e-3cfb-3302-8e5e-075a70c36c69 | -1.92215 | -54.58585 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbdca324-2f00-339b-b927-7d6f90442dd0 | -1.91823 | -54.58519 | 2024-10-10 04:42:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5370424-feff-3b00-9458-d23fd4a76fc4 | -1.23039 | -54.15634 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5b758ee-e40e-3831-9e44-519d5e627c05 | -1.21321 | -54.54713 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c13b9a91-2ec4-37f0-a932-e756b716a3b2 | -1.20003 | -54.12334 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49e8260a-73fe-34b2-8f62-93b40fe113ec | -1.19695 | -54.09299 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bfb6b34-9481-39a7-b36f-aef0457722b5 | -1.19641 | -54.22171 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f15d6d1-5e04-33cf-85c1-66821c93cfc5 | -1.19618 | -54.12274 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd07034d-4c8e-3563-b19f-d50412b6f328 | -1.19467 | -54.10735 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b93f8a4-2d28-390d-a663-f710baf473be | -1.19389 | -54.11231 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dcafe040-5bbc-3475-8c55-82f38d7d1805 | -1.1931 | -54.09239 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 677b18ee-cd3b-370d-a5b8-3abc3f2b6771 | -1.19161 | -54.10179 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 199319b3-0f68-31d5-b7da-492399da6b3a | -1.19084 | -54.10664 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4600f77-3fe6-3517-ad48-cd6bf37b74de | -1.18777 | -54.10114 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c95dc176-5709-3853-817e-1ee98b707ebb | -1.16451 | -54.07417 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db2ea70a-ea5f-3d81-aa17-a3873d0630f2 | -1.16385 | -54.20172 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ea1ffd8-1e7b-360c-8c9c-b16db066529e | -1.16121 | -53.78081 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5f4a543-d9f0-37cc-9953-cb2ab5637820 | -1.15745 | -53.78014 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03318928-f551-3ff9-9e22-767d9fd5498a | -1.15677 | -53.78446 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dfd64f4-9977-34dd-832f-25f572b39d50 | -1.13374 | -54.10685 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d22be16-0220-3786-81c5-66ba3005f759 | -1.13209 | -54.22638 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0e75cb8-cf4b-386b-a42f-3bb284f574b9 | -1.1313 | -54.23125 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15ff11b8-d6bf-3f24-8321-7e9df245a02e | -1.1299 | -54.10622 | 2024-10-10 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 434233d0-fa6d-3b6a-9de0-8334173e3e40 | -1.128 | -53.64994 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afc16ad0-0e2f-32c2-880b-626b41704356 | -1.12778 | -53.44693 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1099b1a6-66c0-3ecd-a3c4-4667d6ebc228 | -1.12408 | -53.44633 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5784b643-ff33-3724-b1b5-a9b77bcb944d | -1.1234 | -53.45071 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9dfceb1-8bd8-3499-ab6a-706f68e8a511 | -1.12318 | -53.70409 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9018698f-b603-31ae-a70c-822d82489924 | -1.12038 | -53.44574 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8c3acad-4674-36e9-b00a-7b7b7f8ce011 | -1.11969 | -53.45013 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddc937ea-62ef-35e3-8522-b65c7a32c6ed | -1.11739 | -53.62042 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d939bcdc-9a2e-3c19-8159-d954d9256942 | -1.11593 | -53.62173 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a13c584-83e5-3d83-8b06-5b2f6db7ce3d | -1.11438 | -53.61531 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f6eeca8-0e8e-3ac7-91df-227d1451620b | -1.11369 | -53.61963 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dac366b-7b90-34eb-a9c6-4614215d0c33 | -1.11289 | -53.61663 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e74a06ad-9f2a-305f-8870-093b381fd9c6 | -1.11221 | -53.62098 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9c7eb18-77ec-34e4-bf23-661fcf655fa2 | -1.11065 | -53.61469 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90bf7488-0662-3677-89ea-41d570c3dd79 | -1.10994 | -53.61908 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78fddfdf-38a2-39a2-8cc1-f66841961978 | -1.10914 | -53.61612 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf0ae0fd-269b-392b-a988-2411a91226b2 | -1.10845 | -53.62054 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5bacbb2b-66a7-38ec-9568-ad650e9933eb | -1.10689 | -53.61421 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 351b5634-83b2-38a3-aad9-9d32965720c0 | -1.10618 | -53.61864 | 2024-10-10 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 628051e1-a463-35bd-b7b3-1e21f2da548f | -1.02935 | -53.73231 | 2024-10-10 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README94.md)
