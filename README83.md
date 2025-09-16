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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 042e9365-b72c-3749-b1b6-3601eebb1e9b | -9.63802 | -58.94362 | 2025-09-16 05:44:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e76313a-ed4b-331e-8c69-0ce97800e81b | -8.85009 | -62.93271 | 2025-09-16 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8522be68-07ea-3d2b-b1a4-939762d9c5fa | -9.3109 | -65.58243 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e99d4fd8-32c1-34de-8d0c-06ecfb506ab1 | -10.36912 | -61.26084 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 79fce7fe-9220-3ca0-af3b-929cd1cbd8b7 | -12.41271 | -63.88857 | 2025-09-16 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82ff39e-2591-3067-8441-4b8ee7624690 | -7.90849 | -71.74284 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09c70ec4-06c9-3496-b47d-89900e3378ba | -9.49651 | -60.49589 | 2025-09-16 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c277570-7bc5-38ce-b7aa-3d9a758713cf | -9.68639 | -62.00077 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70223ad0-0361-3ba9-9d0b-b3ee6a03469e | -10.36613 | -61.25299 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85b30132-5aa5-3099-bc5f-bb067ee75d8d | -9.18839 | -62.52386 | 2025-09-16 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 802e5406-1a01-31d6-a713-025f032e11ba | -9.73734 | -55.37123 | 2025-09-16 05:44:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c98da63a-a910-352c-afed-1055c1cd9778 | -9.16399 | -61.16794 | 2025-09-16 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72de685d-beaa-3a77-9661-22f89295a17e | -9.31036 | -65.58591 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9668c9a-3519-3a59-a9a9-260d97f76190 | -15.87565 | -59.38688 | 2025-09-16 05:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87ba03d0-2b8e-35d7-82dd-e8789bf133be | -9.48006 | -54.43951 | 2025-09-16 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 970d87df-ba01-32dc-a163-16c46cdff3bc | -9.7662 | -63.41301 | 2025-09-16 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f65d72d5-985f-37bf-8c8a-0387b1c73361 | -9.74922 | -55.37263 | 2025-09-16 05:44:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7672f31-a22f-3fb8-9f3a-b61a7553d0cc | -9.30384 | -61.94493 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 082c9525-6f25-395d-876b-a859f61c1b7c | -9.98619 | -64.99359 | 2025-09-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86b8a632-086d-32e3-9284-ad90f2c2f6b3 | -8.03399 | -71.361 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36856a68-0900-3b67-9c26-85324d1d1631 | -9.98284 | -64.99307 | 2025-09-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 685a1802-def8-3a8a-a8cf-421ebb3176ee | -9.30759 | -65.58191 | 2025-09-16 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5141a787-9413-3ad9-9c4d-36952072d54e | -13.28498 | -54.24286 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 0b15ba7a-b906-3de4-bc56-eca2ab172e46 | -10.1539 | -64.25293 | 2025-09-16 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10556f04-42e0-3693-99a6-b037d862b52a | -13.28561 | -54.2371 | 2025-09-16 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| b2bd95ca-7290-3069-8544-bbcde2ad7118 | -9.00727 | -67.49066 | 2025-09-16 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 00de22ea-e0ef-3e25-a1f5-7f9620b4e57a | -8.06307 | -71.30319 | 2025-09-16 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc5f140-242b-33d1-87ac-ff3996cae43c | -9.47773 | -54.43958 | 2025-09-16 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d83f839-286f-3449-a3d3-219721f838a4 | -9.694 | -62.00192 | 2025-09-16 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1896dfc-2cc0-3b18-9169-5fb4015b1328 | -9.98565 | -64.99718 | 2025-09-16 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ae8d838-565c-3c0e-94ba-cf5b62fd8a3f | -15.87071 | -59.38633 | 2025-09-16 05:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f698a541-eda8-3799-be4e-f8a969d4a311 | -9.48889 | -55.96789 | 2025-09-16 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12abb5a2-a9c4-3cf1-ae00-94c268ac51d2 | -9.74328 | -55.37191 | 2025-09-16 05:44:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6a64245c-2000-3f17-b30d-166de7d5d9b6 | -9.49596 | -60.49977 | 2025-09-16 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20627d09-70b0-3560-ab08-c1bf7ad425d2 | -10.36561 | -61.25662 | 2025-09-16 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56645aeb-ea78-3e15-9898-777ddcdb3e99 | -16.70331 | -54.96579 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 412245d8-149b-3805-89a3-93bb488d07a4 | -16.48033 | -55.10484 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 89aeb6f3-8430-3307-97db-ce74cea5be42 | -16.71091 | -54.97234 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9be0412-2869-3a77-96c2-23d29e410073 | -16.70426 | -54.97214 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf9f5bb5-c463-342e-8b79-6263f2963c15 | -16.47421 | -55.10234 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 865a58a6-1546-3035-a26d-a3f2dc0fa899 | -15.99909 | -59.41662 | 2025-09-16 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38695952-de9a-3e83-8a80-0eab4d37ca75 | -16.4809 | -55.09873 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d42829ab-abe6-3890-83ca-5ab5280acbc5 | -16.47382 | -55.10392 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 557e589d-c33a-326d-8914-44607415ac62 | -16.47979 | -55.11066 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4c2b38cd-a9ff-3a60-a0e4-64b8f3555dd0 | -16.70286 | -54.97073 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ef9f7272-1f80-364b-9f72-ccbf68d33050 | -16.48014 | -55.1091 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 038bb973-2f90-3596-a6a1-327b7e97d255 | -15.99982 | -59.41055 | 2025-09-16 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b47795a-edcf-3655-babc-fe6177a9cefd | -16.48072 | -55.10323 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3241150b-1507-30e5-895a-1b220911202a | -16.69818 | -54.9661 | 2025-09-16 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e1e77e3-ceae-31eb-92ed-f86cf3bc5d6e | -16.673 | -49.7615 | 2025-09-16 06:00:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 6532d4b0-4202-383f-8523-9351b03e6df0 | -13.299 | -54.2414 | 2025-09-16 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 1ce96ac9-5be3-3685-a367-96b5330624dc | -13.2798 | -54.2435 | 2025-09-16 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5b0afe19-36e1-3a6c-bd7a-f140fce87885 | -13.299 | -54.2414 | 2025-09-16 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 0af854db-6363-31bf-bd50-9abed8036d79 | -13.2993 | -54.2207 | 2025-09-16 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 5c5d4306-72ee-3779-b7d4-3ba1556cf729 | -13.2798 | -54.2435 | 2025-09-16 06:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| aff7de9e-e199-3527-90ae-7b5092ad52fa | -10.35978 | -61.25915 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65f948f2-1aec-307b-8c92-4e0cc275e6f1 | -8.65003 | -62.66991 | 2025-09-16 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a29fc11f-d7ae-3f22-88bc-3aa16d239472 | -7.90948 | -71.74049 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720b6a41-ce99-3442-bfb7-5147c2244598 | -10.36594 | -61.2586 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ad2b70-5dfb-34e7-9cea-77b0cefa3dc3 | -9.76966 | -63.41437 | 2025-09-16 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc506ed0-4ae5-3016-8029-d7e4bb92892a | -9.18977 | -62.5231 | 2025-09-16 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b71ccc0a-4813-3590-8981-9a6b03bb1965 | -7.80455 | -71.98056 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef15cb52-8972-359d-88e8-38890c8e9c74 | -9.6294 | -62.40751 | 2025-09-16 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31eff5fe-d37f-3407-b5ef-01cb028f74ad | -7.91281 | -71.74101 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 318486f1-8b82-3535-9375-efbc96da7d77 | -8.03308 | -71.36568 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a1900c2-12e9-30d6-a860-8289b512f62c | -7.8073 | -71.96315 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c04dbf40-1b9e-30ec-9582-e606493673b6 | -8.03363 | -71.36216 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7af719f-e455-37c9-95e5-31ed41d27ee3 | -10.36596 | -61.25966 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e53518e2-2a87-3178-a649-837dd38c5a52 | -7.91335 | -71.73753 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46f7cac6-6762-3ac2-bee6-cbe8d205677f | -10.36532 | -61.26465 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a338eb7-df2b-3434-abbf-fd5aa4d62732 | -9.693 | -62.0057 | 2025-09-16 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0ac444c-4f23-31c0-a3b7-35a3336722c9 | -10.35978 | -61.25795 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 360e6fb9-cc75-3ce5-a2b1-f6526babaafc | -10.36533 | -61.26365 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fe8bac3-9788-34a9-abcd-93564e4dca01 | -9.6872 | -62.00489 | 2025-09-16 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c05024cf-e520-32fe-89c3-da608092a125 | -7.91003 | -71.737 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c0dbfe5-d849-3902-afeb-149013270d73 | -7.90893 | -71.74397 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9a23de7-f198-327b-8318-12cb1345b783 | -9.18928 | -62.52678 | 2025-09-16 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d400398-c50a-3999-980b-c9f467433c6a | -9.98354 | -64.99664 | 2025-09-16 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ef0be1d-1025-3fdc-8231-45530caa974a | -9.76437 | -63.41359 | 2025-09-16 06:10:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb6745b9-05fd-39bf-ada0-e1866b97b4a5 | -7.80123 | -71.98003 | 2025-09-16 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a542054-5916-3b84-ad5c-62bbd29942d0 | -7.32144 | -72.5985 | 2025-09-16 06:10:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 323a9a65-82c1-3585-8c15-fbd80d155208 | -10.3721 | -61.26046 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0365af55-cf89-3f37-ab6b-ff4313bfde64 | -8.64455 | -62.66917 | 2025-09-16 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf779081-2fa0-3ae2-b6a5-23275a2dea9f | -9.68772 | -62.00079 | 2025-09-16 06:10:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 434eec34-104e-3350-b769-481206565d48 | -10.37208 | -61.25947 | 2025-09-16 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 864101e2-242b-3487-9b29-2f96c2645c1f | -15.86876 | -59.39595 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ec2f4ef2-9df9-3a45-99a8-c8fde01664cd | -15.86953 | -59.38721 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a249ce15-093a-3bfa-8771-d34697d878ef | -15.87686 | -59.38763 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2d9d0b5-f177-3148-9d98-02db5abacdd1 | -15.99909 | -59.43433 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1b849c4-57a3-3b51-b0da-6e1674b74fc5 | -15.99981 | -59.42622 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb55cbc1-7d66-3aca-89ec-13e924f24df3 | -15.83577 | -59.43223 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d3b9e10-62e8-37c2-8795-50e63cc06343 | -15.87638 | -59.39138 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb6406f1-277e-3854-b320-436f29d9eeee | -12.40853 | -63.88807 | 2025-09-16 06:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c331eecb-e498-32c2-b2e6-ec1681d1e27d | -15.86904 | -59.39101 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cc93038b-58ce-3431-a5d3-318c2bfd6e3e | -12.40812 | -63.89141 | 2025-09-16 06:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 647baf8f-1624-30a9-a090-f29d47019938 | -15.82916 | -59.42416 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dedc7c8f-c358-311d-a8c5-74ca61974f4e | -15.86822 | -59.39984 | 2025-09-16 06:12:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 82edf114-70a2-3656-a148-344cb97add14 | -13.2798 | -54.2435 | 2025-09-16 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 639d25d3-f894-3825-a680-917172375013 | -13.2801 | -54.2228 | 2025-09-16 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 314506ad-0904-381c-a89b-e77645f02085 | -13.299 | -54.2414 | 2025-09-16 06:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |


[Clique aqui para ver as próximas entradas](README84.md)
