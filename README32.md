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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17b966e1-5e4f-37a9-b23d-99c1b2b5e580 | -3.23335 | -46.8811 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5a668cab-6945-3382-9d59-7e3b2db625ec | -5.42818 | -50.04776 | 2025-11-05 05:01:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4351fc1-b65c-33e6-951a-c29bd23cf661 | -2.79366 | -50.30804 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 17d93f27-8a6f-3b86-966c-d09c3c897a0c | -2.88147 | -52.61495 | 2025-11-05 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7b30277-c96b-3c5d-ab5f-e34f529e6028 | -3.28038 | -50.76637 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2b3a09-e0fe-3b8f-9ea9-e38bc85e310d | -3.82719 | -51.2221 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b0b02e8-f163-302f-ba3c-1947c1928982 | -4.46068 | -43.22196 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| db1888d7-d0da-3742-a133-d36c8802da9f | -2.37946 | -53.97411 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b9dafb1-9c5c-3964-b15b-6cf0d3415a4c | -4.71681 | -46.43597 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b6ac40a-1c58-39a2-b90f-f352d60d842d | -5.1609 | -49.87951 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9aeb7634-b965-31c6-8e45-71298ea6da07 | -3.30932 | -53.83661 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f5b1131-9f65-370e-a5f0-8e4366809027 | -4.29466 | -43.79741 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 893dfc58-e8e2-3901-b508-1a6f0281c827 | -3.49145 | -43.62489 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da1a7dee-b0dd-3f7d-8812-7303e6f9be22 | -2.82044 | -45.14736 | 2025-11-05 05:01:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 12e69259-19a7-3327-918b-e9a0c06b89f6 | -3.39045 | -54.27736 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcddfae5-e0af-39dc-bde5-5bc41aa417af | 0.71222 | -51.37171 | 2025-11-05 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4d5b2bf-569a-3524-8715-d6c1afa73100 | -3.31931 | -53.83815 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e294458-7efb-359f-b722-3f36d18ce874 | -4.45936 | -43.21705 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 118d5cdf-505b-34a7-bdc0-1a872ebe53b9 | -3.83918 | -55.97226 | 2025-11-05 05:01:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4835cc82-4e12-35e3-911b-9f96fac6494f | -3.6072 | -50.6245 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c1b59ea-0ba7-364e-978e-cacead2108b2 | -1.42583 | -55.23935 | 2025-11-05 05:01:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9882aabd-8163-338f-ac56-fcd1d18369cb | -2.42427 | -49.2987 | 2025-11-05 05:01:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4cc403ed-8c61-3f5b-832a-fd2d834d6dc3 | -2.83727 | -49.40492 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fbe134e-48c5-3090-bb53-e2e08d925117 | -1.28493 | -49.14779 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b808b7b-48e3-33bd-ac24-569e6661cfe8 | -3.50325 | -51.55024 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26780970-3f2d-31a7-bec0-ba086e557853 | -3.44387 | -50.21103 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 470004c6-97cf-3756-993c-1fc16c37e506 | -1.26855 | -49.14524 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d0c00c3-be3c-31e4-91bb-c2b0e402c928 | -3.06937 | -47.77457 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b173ac4c-883d-3c6f-8a29-287b674788e5 | -2.88205 | -52.61116 | 2025-11-05 05:01:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c042de6-fbc6-3a1b-a347-c4aec5204b9c | -5.23403 | -49.78642 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc959469-a373-34cc-a46e-88049ecb9e12 | -3.49009 | -43.6344 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c734fd18-1188-3ff3-a7ad-0b0e6e78c58e | -3.8776 | -53.52808 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33c5806c-a28d-3144-8834-2125fa6270d9 | -2.66949 | -54.66782 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 821bad38-000a-30d8-aeb4-130d506a577e | -2.79394 | -50.31454 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5781e672-b500-350c-9011-bc7cd9bf5c11 | -3.47782 | -43.63237 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bbde720e-bf48-32f8-9607-50a1f09c8494 | -3.49433 | -50.45928 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4f47e2a9-b578-349f-80e7-e0a6f55273bf | -2.63703 | -48.50189 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e07b9a5d-791c-39c8-8cad-c8fbb6086530 | -1.61483 | -55.12075 | 2025-11-05 05:01:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dacde6f9-8740-3731-80bb-f0d7793f6320 | -2.66437 | -54.76529 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d30e589a-5f68-3179-85c2-2a6bc0318e2a | -1.38306 | -48.85145 | 2025-11-05 05:01:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe6ae376-0960-3d40-8f42-b3811b8aa7b5 | -4.47062 | -43.22952 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8276c566-d9d3-3cf0-828d-309c2b2ae14a | -3.4464 | -50.21791 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3b6d849-31d2-306f-9286-7ee1b66671bb | -2.44662 | -49.03442 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95653745-4de1-3176-9e78-276cd34a1f0e | -3.72383 | -54.2122 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 382a874a-c400-31d2-a4af-a81b9eb60f7c | -3.58687 | -50.16382 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d33fad3a-f5f5-3af0-b906-e4b7c2929232 | -3.48602 | -43.61896 | 2025-11-05 05:01:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 59b06f96-586d-3088-8693-f4bcd9ddb160 | -3.4353 | -50.24052 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d93bb337-c1a4-3dae-9e5e-a0d05d71d943 | -2.81981 | -45.15231 | 2025-11-05 05:01:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3d2a00e8-7596-3b15-9ef9-0cde378ba9ca | -4.58057 | -43.34095 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d1a87c4-2a41-3e32-922c-0ad92dc6259b | -1.25626 | -49.14331 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93a5c207-9065-35c7-926f-23508be90a7c | -4.46986 | -43.23479 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c2dc81cb-7cff-3674-8fee-f5864e25b9a0 | -3.31155 | -53.84413 | 2025-11-05 05:01:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b337fcf6-f201-3317-b0bc-749ba4453691 | -1.73448 | -55.46234 | 2025-11-05 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf924be1-519b-3c9a-9947-e1b51cdd4210 | -2.64205 | -54.8215 | 2025-11-05 05:01:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 785b88aa-d3e5-3fbc-9685-c62ed98d0c6f | -2.36459 | -53.98243 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 935e9a56-1d76-3852-8ee0-bf6b84580198 | -6.64459 | -42.28309 | 2025-11-05 05:01:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b564cf2c-c498-3501-8dc7-3a720a7f347e | -2.81093 | -49.14284 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8d686cb-06e4-3fde-96f0-8f851a82191e | -1.25682 | -49.13965 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbfc85e2-0983-3be7-ada4-ace77d3a1183 | -2.79441 | -50.28464 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf3ffd93-3244-3e5c-8144-49da52884b22 | -3.97065 | -43.78289 | 2025-11-05 05:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34963ddf-8b83-367d-8252-ad10dae91751 | -2.78933 | -50.31885 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 45a3c0ce-7e20-3b91-94ef-6d6de3d28421 | -4.41518 | -48.93946 | 2025-11-05 05:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8c1a768a-2b99-3265-8dd8-f8cbc0e64a57 | -4.5869 | -43.34202 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4fddce55-1a39-3454-8af2-bae0f03a0327 | -4.59594 | -45.62666 | 2025-11-05 05:01:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55ec997e-4803-3f45-80a5-9e29c48125b9 | -5.92644 | -43.37042 | 2025-11-05 05:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 04080b85-502c-34b1-88c5-702b21e7de3a | -4.46139 | -43.2167 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e27302cf-487e-342d-9183-8bb0feb2f8bd | -2.6197 | -49.2281 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d41201b5-865c-3e39-b6f7-e7bb53d2a27f | -3.49359 | -50.46407 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d241dc46-14c9-3771-b08f-733dada91f91 | -2.0807 | -48.36851 | 2025-11-05 05:01:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d153c89-3ad9-3913-b9fc-0c4febf82289 | -3.90844 | -56.05107 | 2025-11-05 05:01:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| be373fde-096e-3d88-985a-56c374a89d9d | -2.44881 | -49.01537 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a28d489-8ee0-3de8-a006-bffd388a2a40 | -3.79367 | -51.31657 | 2025-11-05 05:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 161e76d2-411f-3299-9174-105ae0633aaa | -4.29557 | -43.78826 | 2025-11-05 05:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83a502b6-d254-37f0-bc59-ea998f0e6f2a | -3.06827 | -47.77575 | 2025-11-05 05:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2cb38c0-8d5a-39e0-b0f7-a4c7a3e49de0 | -3.37261 | -44.24193 | 2025-11-05 05:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d7059617-2135-3b59-8fd3-975177409586 | -2.88038 | -54.42649 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e8cf65-c8d1-3e0e-a8ef-b2578ba2abbc | -2.97647 | -48.70519 | 2025-11-05 05:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 327ca801-ab71-3620-b0dc-81fa233f5d1e | -2.91128 | -54.29386 | 2025-11-05 05:01:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92540e50-5cb3-3be4-adb0-1943108d5738 | -4.45501 | -43.21565 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 87f0ab52-4ead-3689-bf64-bf5c892eed35 | -1.26036 | -49.14396 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3aacc67c-4424-316f-a1cd-166808657ed0 | -5.47832 | -43.57783 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 0665c804-1a57-3031-b4ab-b31bfefb49cf | -2.72789 | -47.38475 | 2025-11-05 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3c683e2-48f8-33d3-af5c-58f1a7072618 | -4.92163 | -46.7245 | 2025-11-05 05:01:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef2f0ee9-5f6b-30d6-8da0-90922ca322ca | -4.57422 | -43.33998 | 2025-11-05 05:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccc1ba1a-7794-33d1-9378-e3f849b34179 | -2.61912 | -49.23186 | 2025-11-05 05:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eec30f1a-c577-3231-95a1-0d1e098e2083 | -3.97019 | -49.46605 | 2025-11-05 05:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dfe4beb-52c3-3878-8d5a-06d6fe3984bc | -3.10978 | -51.02815 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ec3e117-6cba-385a-9ee4-326182f53a53 | -3.2412 | -50.79647 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 210e8eba-d616-35fe-b7e2-159fc59d759e | -4.18297 | -46.41254 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f5d3dab-9096-34f3-a95f-fa49b8c5df39 | -4.863 | -44.61426 | 2025-11-05 05:01:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a35a99eb-2388-313a-9956-46849a179da3 | -4.96617 | -49.87534 | 2025-11-05 05:01:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee2fb0a5-99e5-382a-afb8-889820aa7b3b | -3.60539 | -50.62255 | 2025-11-05 05:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c78ecf83-7ac5-3983-8543-758313341dfb | -3.24049 | -50.80107 | 2025-11-05 05:01:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c117e8f7-b240-35fd-9e06-d584ea1b3f11 | -3.63548 | -49.89103 | 2025-11-05 05:01:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2ee9e87-dc64-359e-8f8b-e5ae8a2eff48 | -2.72641 | -47.39468 | 2025-11-05 05:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c847bd61-ba1f-389c-a3b0-2cba29b60763 | -4.67084 | -46.30684 | 2025-11-05 05:01:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a67c2303-c6ed-33fc-96cd-a8127ace4fb0 | -5.48019 | -43.58542 | 2025-11-05 05:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 02fecec4-3222-3290-926e-8cbeab6abbeb | -3.13101 | -44.47949 | 2025-11-05 05:01:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8282208-b49e-3863-b627-42cb53cac841 | -2.37892 | -53.97757 | 2025-11-05 05:01:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69254f5a-57f6-3f34-af83-336325b7c53c | -1.30484 | -49.15464 | 2025-11-05 05:01:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README33.md)
