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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 085a945e-a2e7-3864-843b-c886acf2eb05 | -1.65595 | -52.73302 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67460421-6f94-33d9-98ca-2058ed53383c | -2.88358 | -53.98746 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 064dc567-710b-3466-b864-da404b1b97f8 | -1.57202 | -51.24601 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d8f895e9-70c1-31d6-9279-f6177c44eaf0 | -2.84275 | -46.87472 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ec2ab707-3827-3cc2-a4a5-bdf8b7dd9174 | -4.72291 | -45.64449 | 2024-11-30 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa19a1cc-7539-3d45-b512-d0bb7ec7d44a | -3.08211 | -53.28267 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 19fee728-8454-382a-ad9c-cf9165e26b68 | -4.22116 | -47.21747 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21d7d5b7-1f9f-3992-bd59-a7ba7b774482 | -2.61341 | -46.54468 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b21c2d49-de3e-315a-a5f9-6fd756b383d2 | -3.82225 | -46.6001 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bd1d321-db6f-3655-ab89-6c9341ac01bb | -3.80146 | -46.68807 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33aa847e-d864-3531-8528-21612b512ac7 | -3.90896 | -46.43999 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fc7ad7c-f10e-3f21-9b76-c62167a4a1d2 | -2.83817 | -46.85878 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dc12735-0f7e-3020-aaae-e5c8730cc44e | -1.64536 | -53.87198 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| afb1b287-7400-371c-97d4-32528a7d94c4 | -3.50158 | -50.29026 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23ae396d-f698-3616-a7ac-c71739ece889 | -3.98737 | -46.70734 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| caf96fa0-9ee5-3065-924c-baeb751d6890 | -3.78316 | -49.36381 | 2024-11-30 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a6af17f-a228-32d4-8b9f-b038d55697cb | -1.5914 | -51.26433 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 199d3787-b451-3213-8dad-7451816b425d | -3.10602 | -49.45216 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c50d03b0-93a7-3098-8034-c4e82b424fc5 | -4.20377 | -46.6905 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19e5e34e-41d9-32a8-a5a0-1e18cfda0560 | -3.37671 | -50.17982 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1f36670-49fc-3c69-b57d-740428a4952b | -2.76324 | -49.22822 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fafa9850-143b-3454-adb4-f0a7486525b9 | -1.58153 | -53.85447 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0db4ea56-0fe8-3c3c-b138-6cb8931e2ff2 | -3.22347 | -54.18149 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8cc2ae1-775c-323c-af03-7c00eb525f27 | -3.59432 | -50.37012 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65e9f328-b3b7-3487-b06c-97036678379a | -2.35466 | -46.87742 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf1ff771-b903-38b5-b72d-c6bd8ee9dfb2 | -3.28837 | -48.76553 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a15534e7-e183-3849-a808-6463d6cc4668 | -2.95542 | -51.6944 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e68f3c26-c4c3-3e96-bc0f-05d56f03dc70 | -2.20162 | -48.33823 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4250ddb-6e2e-3499-b901-71f177058498 | -4.88363 | -41.30207 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3ff02662-c789-3d19-80d3-e3d75533db15 | -4.00534 | -50.35133 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3432c2d-7f99-3196-b5cf-8e100f259b64 | -1.66205 | -47.71894 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85b70432-4825-30b4-8250-ec1219ca4439 | -2.67743 | -46.60424 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 68a9af23-8597-3ce4-a655-39e08412d969 | -3.69998 | -47.13926 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe2ab5af-b31c-3b47-ae86-aab5c4413261 | -3.04895 | -48.48829 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5194d68d-dbc5-30c8-99b1-9324c7f5f2ee | -3.04826 | -49.51756 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd8f11b-ba7d-3b6a-9363-9424b1f358f0 | -3.86533 | -50.16284 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e31dd167-e6d2-31a3-ad21-f0186fa552a7 | -2.19562 | -50.57525 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4847c81e-9e03-352e-af6c-e63c8e4f1a4e | -2.65013 | -46.12159 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2cc2c5d-edb6-3314-bfdb-efbe01209b32 | -1.68444 | -46.78771 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9b6db1d4-7a19-31b6-b9b8-1ff36a61d324 | -3.29298 | -50.36324 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc314bc-a461-3e98-85c2-6fad8e795efd | -1.34411 | -52.13232 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 72c967c7-9817-3189-aeaf-3bdd7786cf40 | -2.75946 | -47.89965 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c77a5f0-f5d1-39cb-b3ce-342c11b0de7b | -3.07615 | -48.66523 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0606dfb2-9bf2-3d1f-afed-08b9d2ebc2f0 | -3.09388 | -54.55067 | 2024-11-30 04:40:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59442dfc-2af0-3890-b21e-a2f937aa2907 | -1.87486 | -46.46599 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85fd8f14-18e7-362a-9e3f-3552e36a97fc | -2.19251 | -48.39671 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830dafe6-372f-3f5d-b574-edc8af0b7004 | -3.77766 | -51.67654 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6795af79-47d4-3b52-8603-02b4d7287c3a | -3.36273 | -46.66652 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29ae241d-5a17-343a-9535-da6777f81d76 | -2.51913 | -48.46173 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4cb12c01-2259-3f02-88db-4c927fd47de6 | -2.61452 | -46.56041 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eca985f5-3ba4-3077-8663-3117f6c25e5b | -2.06691 | -51.19161 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9cdd13e-e4eb-3da7-bc15-6e0ef006549e | -2.55202 | -47.30578 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e5b54f8-bdfe-3789-83d0-c56e324811f7 | -2.47501 | -50.37995 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bf28fbc-4f6f-3048-b80f-b27602200ed4 | -2.43958 | -48.6465 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9f2edf8-eddd-3b8f-8d48-e60fcd28a339 | -3.28453 | -48.76846 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 294f59bd-edbb-3446-87aa-f4c12bbdce47 | -2.38396 | -47.88826 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce37c337-1ae2-3005-9139-78adcb4d8135 | -3.3952 | -50.31762 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a00ead9c-3e52-319d-9a2c-c9182e2aecbd | -2.17977 | -46.60381 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d41097eb-6ab4-3ac5-9f19-07d69194d0f9 | -2.93947 | -49.45039 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9235cc3-462a-3070-9f7c-e050a7991931 | -1.24473 | -53.35363 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7efe2d9-95f4-3c7a-a26d-7aaea72dedae | -2.8028 | -48.56251 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba570c6c-5816-386a-b9c3-a530cab7556e | -2.44342 | -50.42691 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a18535c3-f4a1-342f-84ca-17cee4c1b22c | -3.58573 | -50.5116 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9bb985b0-12bf-3438-ba0c-67af5b9f95bf | -3.69542 | -47.12339 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24fdd2e8-1230-3c50-a60b-37d44b01a84d | -6.9258 | -45.20905 | 2024-11-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7de18380-427a-3c64-bc81-aeeb3e3a7f74 | -1.06796 | -51.79533 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09f02b3a-69cf-35e3-b4f5-717d66ecff93 | -3.27408 | -48.77037 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9b186d-4998-3a57-b5c9-fdc9794de1b7 | -3.36714 | -50.38626 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb4134da-421e-3f85-9ca0-0ca732e1a280 | -2.98458 | -54.084 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99aba643-7e0b-35c4-b91d-ed977ccf0ae3 | -2.98494 | -53.2851 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 256c153a-0155-36ec-9603-38962b66861f | -3.84192 | -46.52617 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fc9e5c6a-e1a5-39cf-96f3-30787bd30570 | -2.37065 | -48.62879 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5217174e-7217-3bf7-9e89-ec49b0c0b9ae | -3.41589 | -50.42683 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b4bde4a-852c-3aa5-82fe-a8bf5dc155b5 | -1.16362 | -53.56741 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65c79c3c-433d-3100-93aa-5eacf797047d | -2.38358 | -53.65967 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb12cd5d-3cff-3d1b-b514-49f95dd9c5cc | -4.11092 | -47.20421 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39b6836a-4881-3842-b2fd-09556fab616b | -2.43084 | -54.02335 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 22ae534d-555c-3e14-9eaf-48bf136e2354 | -2.01876 | -51.19281 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 591b6ef5-e6d3-3301-bbad-997b65f9380e | -2.64977 | -46.57667 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d30c569-6985-3b66-b32f-4ffd1ba6717a | -4.11733 | -49.55387 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a903cb33-36f0-3a40-b9cd-d32a7639c767 | -3.24616 | -46.41665 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acc741a4-a84e-3eb9-9155-ea0e95c21090 | -2.71877 | -46.12278 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b16ff39e-f3c0-3f1b-b18b-80645bc65b84 | -3.692 | -47.12286 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e34312f-8a96-33bd-a153-bad57579e40a | -3.09571 | -54.04383 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d275af3a-cb14-3356-aac8-a17181321ab3 | -1.36139 | -54.9734 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acac9e89-6962-3163-b8b0-f01a2164b9d6 | -2.01234 | -48.06882 | 2024-11-30 04:40:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e27b048-0671-3071-94b0-324dbb4dd2bd | -3.67376 | -47.12762 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| add8b7bf-b946-35f6-83cc-2ddde6c6ecf8 | -2.57068 | -49.09276 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0546d4cf-d783-3713-9200-9e8e28f2dff4 | -1.14737 | -48.33538 | 2024-11-30 04:40:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 798badcd-fb42-3e40-b932-3902eebf1ebc | -4.04199 | -46.85203 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25eee7d5-f159-3b1f-92b2-61f4c2f37701 | -3.29187 | -50.34845 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29a45570-7dd0-3787-8951-da8aa3f81852 | -3.33799 | -53.20414 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d46ff5c-db2e-37b2-b397-fb74c6274ac3 | -4.0709 | -46.5435 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc1c6ed-597d-3fdf-bb23-37d9d1a3ecaa | -3.81481 | -47.46775 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26800e8c-72f1-3cbb-935f-6c7261e3781a | -1.43974 | -55.13243 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e14b6b8-c52b-3eb0-802e-159605d51064 | -2.61746 | -51.81313 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8aaccee6-edae-386c-98f0-a9140f1dba92 | -1.9674 | -52.89278 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b91d9e5-c50a-3946-8721-972cd6bef367 | -4.06483 | -46.67834 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c8bfb26-3028-3927-b795-a8288e0e5d27 | -4.8387 | -41.29822 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f92abf65-f0bb-3627-b7fe-5cfdf589752e | -1.97207 | -46.44978 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README63.md)
