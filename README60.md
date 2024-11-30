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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1327b71f-dc32-3b01-9dfc-23baf1674818 | -4.65065 | -43.92719 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22830e54-cddd-335d-9ee2-2cbc87c59e0a | -2.66764 | -46.59884 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab9e42d1-490a-39e6-9ffd-7d4d37b52925 | -1.17911 | -53.41705 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54841a71-b7c8-395c-9906-98d8db32ec5f | -3.18105 | -50.29493 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 795c7cd7-f8df-3ffc-a566-32377d369d08 | -0.58391 | -51.70051 | 2024-11-30 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f7f185ac-1db3-3a8c-a36e-939d97df2cab | -3.31471 | -46.65531 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 509264ce-6a07-3984-88a0-2ed25db49367 | -2.12714 | -46.41759 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84ea9c7b-9199-3d8a-8c5b-43cebbe5a827 | -1.09607 | -53.38565 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 396ab499-e49d-3b7b-9260-fc6a93f666ef | -5.89695 | -42.32674 | 2024-11-30 04:40:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 31688240-50bb-3a46-879f-983a1721060c | -3.30811 | -50.37656 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c02989ca-a02c-3e24-bc51-bf2a1658d3e2 | -1.69264 | -52.18204 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 280356f7-1b13-3ee0-9fca-d970376991f1 | -3.30979 | -50.27835 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f944e1c2-577d-333a-b461-e9eccc44e338 | -0.99475 | -51.71162 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3fb5211-a814-3679-b0c2-3898c794b918 | -2.8104 | -48.66575 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 395176f9-2a2f-3a83-bc88-74930b00f5b2 | -2.82624 | -54.02975 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13130591-d5fe-33f5-ac81-36776e395ca5 | -3.47658 | -53.80864 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b9116e7-0225-3b65-921e-2538df7fce87 | -2.76616 | -55.3336 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 907c5137-8fe3-30e4-866d-83db67ccc8a6 | -2.53413 | -47.97184 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 926788e3-8986-3141-8ca2-bf10c4a7fe0e | -2.27841 | -46.44058 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba3d6e5-9f5b-3184-8dcc-e7dff8ec606b | -2.96574 | -48.03911 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4160bb51-de18-38af-aab5-d4eff601c0ea | -3.05682 | -48.52478 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b60a5863-90ae-3e94-92a1-bc5f3c87a2de | -2.72602 | -46.2409 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ffc9a3f-f082-3157-b253-c7c27eedb462 | -3.80903 | -46.68528 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 570d965f-83a0-3270-9a9c-d37cd2cbb9ea | -2.83049 | -48.47163 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ef53eb72-8862-37bd-8d95-040e7b8face1 | -2.22891 | -53.69218 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 299a7cda-5662-3d78-a6c3-461be3cb9369 | -2.06434 | -50.29799 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e40ffe98-f515-35b7-8c5a-72e868f0a3b9 | -1.08702 | -53.39117 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a49ced2-f9ac-38da-b7ad-7b8c9efad3c8 | -3.20096 | -53.42599 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b83c38e-0624-3032-9eac-f4328358bdfc | -3.98755 | -49.97025 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c899c346-497d-3cd5-b7a7-9da6263c7a53 | -3.50581 | -53.82898 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a7e8017e-c886-3c32-be06-29821801e67e | -5.22459 | -44.91212 | 2024-11-30 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3eec41db-772e-356e-bd2f-bd4f746c9894 | -1.49016 | -52.32871 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 42317771-bef7-3cd1-b443-1bf934ff7304 | -2.17458 | -48.57683 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b28769db-f95f-384f-8031-60665d554cc8 | -3.17163 | -49.16256 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f159c4c9-4c20-3552-a13b-1a9ab7a3fb20 | -2.44847 | -53.62541 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c51e4278-4b29-3dd6-86c0-7f6982935617 | -3.3552 | -49.09959 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d89ed9e-8643-3980-b1dd-bdc256de7d8e | -2.19505 | -50.57892 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cbf81b6-f78f-371a-90b0-53326634d31d | -1.58851 | -51.25986 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4d30ae9-8a47-3f84-8dd8-580a641b4b04 | -1.21163 | -51.73887 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b70695ab-2fda-301e-84f4-de7942647230 | -2.41811 | -50.34529 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9acd825e-835a-3d06-b984-3173f5b9841d | -3.96721 | -48.09309 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ad47dd3-8a9a-32ac-a422-a4070cc49d14 | -3.73401 | -49.87318 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2e08db02-9b06-35b9-96cf-2a830b061406 | -3.49476 | -53.82191 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa606617-a234-3499-95d3-144072d313bd | -0.96141 | -51.65635 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1eac608c-034e-30d8-9054-3629518410ce | -3.68362 | -44.69953 | 2024-11-30 04:40:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed299c79-05e0-314b-bba5-f6cb5fdf121f | -5.31204 | -47.48988 | 2024-11-30 04:40:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d394b67-731d-3530-a2b3-8b6ce7c584a7 | -1.68221 | -48.46134 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09c97c73-76fc-3cc7-9150-b8727a8b4c8d | -1.32399 | -51.66989 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 67bb1df9-2322-3d96-82ef-217caa7880e9 | -3.34772 | -50.18983 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd83661-7341-3618-9983-4ebd7d70f10f | -2.62625 | -46.20673 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22d372a4-71ac-3a8a-8e41-7847a7efce1a | -3.89579 | -50.07771 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e74ac675-14b9-31aa-bdbe-4cba3991d30d | -3.6192 | -51.53692 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 476468d1-64da-3417-95d2-a1b63851670b | -3.28385 | -50.55302 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c6a1e49-e9cd-337f-9142-4ca5bb3284dd | -3.07011 | -50.57215 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78099150-b7bd-375a-b909-b2b20c7d40cc | -3.63176 | -54.1627 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed938460-d5f9-3243-9e90-1ab15fa02539 | -2.34317 | -53.86488 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff12f697-34cf-36ad-9b6e-9f9a17439b7a | -2.23827 | -50.48066 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8cd2b3-dd24-3a35-9b56-7334dd08060b | -3.33268 | -50.2201 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c86e5527-4b01-35d1-aaac-31d3f792dcef | -3.67632 | -50.17618 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f4c3516-3d25-3cc2-9818-587ce9746301 | -4.20056 | -50.68845 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 55523a57-7a83-316e-a2a2-54e47fced2a1 | -2.67917 | -46.2828 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b9aaf3f-b0e2-3216-96cf-e395f5d46021 | -3.16134 | -53.24366 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d5ed5b2-ccd4-3a13-93e8-f821e922d98c | -4.67993 | -46.37028 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 57d273e5-9366-3baa-b2fc-352a7df15a1d | -2.76047 | -49.22427 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a54aba2a-272b-34b2-98ce-2f59f7e21b8b | -2.94766 | -48.59246 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 282598a5-8f4b-35e4-b176-faa445722dab | -2.0037 | -51.17461 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8a94532-de55-3626-bd83-a5e98855922f | -3.86254 | -50.15882 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e35e6ff-954b-380c-9928-3dea2f0cfd80 | -3.26566 | -45.37505 | 2024-11-30 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d56584a1-2c8d-30da-9e48-2dc860f4b6c1 | -4.21134 | -46.8498 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ffdbaf-c83e-3478-985c-045bcf430373 | -3.27778 | -50.43784 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bd69a4d-dbee-3e0e-b295-5e40570dc6ed | -2.85306 | -46.69222 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32e4bd63-56b6-3551-9d8a-b79b86214dba | -3.55773 | -46.34478 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d389143-1756-3f32-ae50-f4ff81e55183 | -2.44243 | -46.51094 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1a12f43-42c6-32c2-91f3-864a46cf6f8f | -1.06521 | -53.22062 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e168ea8-c540-3809-aa73-9f28197f1036 | -3.86309 | -50.15532 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdc5188d-ca83-3bd6-b08e-2a50121b5cb0 | -2.57124 | -47.36015 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1d8d0a5-e09a-3ea5-8879-04b0c6a17c07 | -1.20534 | -53.88397 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebd4b741-a1be-38c3-9ac0-d53944aba82a | -1.90261 | -48.66467 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4598e326-9392-35ca-a6b7-cada1e359f80 | -3.74304 | -50.27016 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b5a8a74-5916-3172-8ee0-6039152adc27 | -2.87415 | -53.98968 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d833fc7c-74e1-32a2-8afb-677f6d917fdc | -2.23138 | -53.62527 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fea15ef2-844f-37d6-b013-6bc1109f2c9c | -2.04471 | -51.19614 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8cdaaf11-0390-3264-92bf-175c78dd90b9 | -1.19384 | -51.75753 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7c5df31-beb4-331b-95b7-e47914ac1601 | -4.47436 | -50.42103 | 2024-11-30 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d359dbdc-94dc-3fa8-9d28-366d77785cac | -2.46495 | -49.04755 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29191c59-bade-361d-9ab6-2c202d39481c | -2.46602 | -46.56508 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c10eaef5-13fd-3d2e-ac2c-0f2f02e37480 | -2.28417 | -50.57054 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b625aa4f-33d5-3a1f-b0d1-d3a7fe6d7d22 | -2.76697 | -48.55347 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| faa55021-35d0-35b7-b875-39abbe6024dc | -3.09253 | -51.40534 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a83cd59-b845-3fb5-90fa-14c0ca344231 | -2.70697 | -46.12909 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17217faa-944c-365f-8718-c22dd44e9e97 | -4.11386 | -49.07767 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b39752bf-bacd-3af8-a62c-101a2da83abe | -2.71805 | -47.55074 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22b34052-76cb-36bc-b1d7-245c55b30e0d | -4.01499 | -49.01307 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1155cc62-962a-33e0-84c0-a842a784ea07 | -2.15 | -50.62096 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a3b5f0a4-7f4b-32ee-bf25-da3f7faf8d2c | -3.89707 | -46.49427 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 159fd863-9ede-31d5-9e67-eb6183986539 | -2.69545 | -48.66199 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d959b68-1746-3919-9df4-5363586be9e2 | -2.25784 | -53.45945 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9da378f6-5a46-3259-a017-d3895cbd0350 | -3.28717 | -50.62023 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c148bf50-9f94-367f-8e76-2e684d2a8970 | -3.2511 | -50.58495 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a811423-1355-3a45-8e16-41e0d43f3a9e | -2.86954 | -53.99261 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README61.md)
