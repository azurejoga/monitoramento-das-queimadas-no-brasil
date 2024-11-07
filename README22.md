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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a55410cd-38c3-355d-80f6-2790e8f441ac | -5.62347 | -43.95604 | 2024-11-07 03:29:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a5242f6b-793f-3dbb-8e3a-3c726320fdb3 | -6.07475 | -44.72258 | 2024-11-07 03:29:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2cb24b16-e066-3077-a50d-f78dec18b6c1 | -5.44647 | -43.57978 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e34e1697-970b-3232-ad85-d2d938dbdb9c | -5.44327 | -43.58401 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3c52307e-b398-378b-840a-df60eca50fdb | -5.73728 | -38.32613 | 2024-11-07 03:29:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 07e9e017-69ca-3d4f-a820-62d57df0086c | -6.69464 | -37.47126 | 2024-11-07 03:29:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a8b3bdf6-db27-360a-9c43-06e08a0a8072 | -4.5092 | -42.87271 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0332601-8f91-326c-a96d-587bb464cb97 | -5.45191 | -45.53114 | 2024-11-07 03:29:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 924fdb19-5c26-3fd2-81a7-cded1fcf9800 | -6.95066 | -36.25827 | 2024-11-07 03:29:00 | NOAA-21 | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 27e63a98-2c1a-3d8e-9129-c86b54b70f22 | -5.23005 | -44.91216 | 2024-11-07 03:29:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8760b87c-a406-339c-aed6-c7b0528b23a0 | -6.69564 | -37.46824 | 2024-11-07 03:29:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec2ea6ed-7b34-305a-91db-413d58a1b43f | -5.5196 | -43.66389 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9765d6bf-edbc-32a1-9b11-7338524c7d2f | -5.93866 | -43.77612 | 2024-11-07 03:29:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9381ac23-697d-339e-bd19-ae77c6e20271 | -6.07584 | -44.71652 | 2024-11-07 03:29:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 201cdc0b-cb8b-3542-9913-853bf72c0826 | -5.5548 | -43.70404 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d8085313-28ee-3944-99ac-47eb7ee0c2fc | -5.0342 | -46.83 | 2024-11-07 03:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 91525de4-a178-385d-b738-873292dfa771 | -5.9788 | -45.3621 | 2024-11-07 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 178.3 |
| 2f18ab2b-9c31-30a6-aa2b-2dc59022619e | -5.9975 | -45.3607 | 2024-11-07 03:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| a9d6bfaa-7327-3825-a1e2-9954bfa44b40 | -2.82 | -52.9409 | 2024-11-07 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c21e77cf-ed9c-3284-b2c1-372e5782636b | -2.6228 | -51.3038 | 2024-11-07 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| f9b2ca6f-71c0-3004-a916-96e1983de8f2 | -3.6602 | -50.2501 | 2024-11-07 03:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 39563dad-242d-3c32-8199-9fca3eb49621 | -3.0207 | -53.443 | 2024-11-07 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bfada59e-9d8d-37f6-97ac-459ad2cab567 | -2.8352 | -48.6648 | 2024-11-07 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 97abc903-5ca1-3052-bb4d-5e6db8917614 | -2.82 | -52.9613 | 2024-11-07 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ef5bf540-2ddf-3d04-81ec-19353efabb84 | -3.0396 | -53.2805 | 2024-11-07 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 323aa934-48bb-345c-811c-ad1f3cff9cb8 | -2.8351 | -48.6862 | 2024-11-07 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7827f7bb-02fa-3d1e-a5bf-ed1e4464f916 | -3.7218 | -48.9979 | 2024-11-07 03:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d4cac957-35a6-309a-a40b-b4fc8a050b79 | -2.8536 | -48.6856 | 2024-11-07 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a50b3035-7ffc-36bc-9bd2-35d9c8ddbbb4 | -3.0207 | -53.4227 | 2024-11-07 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3d154559-3561-399f-b119-ffe30018a960 | -3.7033 | -48.9986 | 2024-11-07 03:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7a8e4214-9e1e-3568-a9ef-e7fcb1e74ea9 | -2.8537 | -48.6642 | 2024-11-07 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 301448aa-2902-3ea6-a6ae-d9b39de3f251 | -5.034 | -46.8521 | 2024-11-07 03:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f34f4272-39d1-3751-83a8-e68d70ee371e | -1.1466 | -53.7177 | 2024-11-07 03:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 9efabda0-7938-344b-acbd-1320514414f8 | -11.51939 | -43.27063 | 2024-11-07 03:32:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 980c7edd-ccb8-36d6-9def-d3de7cfbd373 | -9.82487 | -36.37615 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 79806fa0-197d-3e3f-8fbc-85714be6af5a | -10.68696 | -37.11776 | 2024-11-07 03:32:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a0785b7e-4c9c-36f0-b219-6fd140d8b309 | -9.63513 | -37.81659 | 2024-11-07 03:32:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 33fccf2d-834b-36ae-865f-8a30b6af2e3e | -13.51921 | -43.0041 | 2024-11-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3af21660-25db-394a-bb40-3e61b6c34762 | -8.30831 | -43.61235 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 31c5bb7a-cfc0-3fad-b031-110e8a85f681 | -7.18159 | -39.10413 | 2024-11-07 03:32:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| feb5f706-6ceb-3851-b1dd-5121344ec285 | -8.6918 | -36.2367 | 2024-11-07 03:32:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b690aaed-1630-3f39-a5a5-efe4da12921b | -10.68617 | -37.12237 | 2024-11-07 03:32:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 91497bf3-8901-36d3-811b-8fff5bee52f3 | -12.1803 | -43.53453 | 2024-11-07 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7625d252-99f2-383e-9fa7-f05587f9a698 | -9.82056 | -36.38139 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b9db1c5-c05a-38ba-9951-6f8d780f6bcc | -6.96493 | -39.82999 | 2024-11-07 03:32:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| cd422236-d6f1-3c1a-9519-41ecf46ee7d7 | -8.30915 | -43.62027 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e77f05d-47e2-3439-9a78-6191c03dd983 | -8.31004 | -43.61561 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0458bef-30be-39ff-870b-a21fae4fb37f | -8.30744 | -43.61703 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4957a17a-a46c-3bfb-8db6-7df7e9238b69 | -7.67989 | -41.34669 | 2024-11-07 03:32:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e2a9161d-28e2-30e3-a2aa-7961421a67b1 | -8.50134 | -42.07816 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f51a6757-03bf-3dbe-836e-c47aaee62d89 | -8.50167 | -42.08697 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b7aa1755-a494-38d5-8765-695d4223ecda | -9.73727 | -43.5914 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9747c50-3d5a-368c-b823-3d02a5191ae5 | -13.5198 | -43.00372 | 2024-11-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 686e9659-6823-38a6-aaee-3c5bf0fcf024 | -10.45188 | -44.89407 | 2024-11-07 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ee95edc-0527-306d-a2e9-c23c9326855a | -5.98677 | -45.36908 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| a60c87e7-1813-3387-a99b-1b544332ce8c | -9.15148 | -43.13717 | 2024-11-07 03:32:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35c3d7b6-28b2-3696-a96a-abd49c5a1d87 | -8.31423 | -43.62611 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a98c8134-0d26-328e-a17e-994d878c6052 | -9.75046 | -43.58135 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd2b0305-2801-3bda-ac46-2b9556ec9d7a | -8.34678 | -43.61779 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3bda347-eb42-3c50-8cb0-4aeec9c55b03 | -10.51043 | -40.16916 | 2024-11-07 03:32:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1193a2e4-a346-393d-a9f5-2b445181e427 | -11.26565 | -41.03968 | 2024-11-07 03:32:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef2c8959-9ebc-33e1-b952-0411607afee4 | -7.68048 | -41.34342 | 2024-11-07 03:32:00 | NOAA-21 | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc7590bf-6681-3cca-a977-5f6786695214 | -6.50388 | -44.67818 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 093576d7-72ee-398f-bc62-dcfc9e0e6c49 | -8.30823 | -43.62506 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00b8f0fa-797b-33e4-8ebb-d5a4bf98664c | -10.5034 | -36.84935 | 2024-11-07 03:32:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 80108082-7c51-356b-aa64-1c3caae839a2 | -5.97869 | -45.37444 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| a79fa95c-cac9-3ffa-8750-031f7af0d641 | -9.7439 | -43.58821 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09e960a3-a89b-30b0-a220-0453639ddc07 | -5.98569 | -45.37546 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| eb2a2378-6295-348e-b5f3-344f986440d3 | -9.74463 | -43.58028 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5c318891-4e22-3dd2-b937-a3ea8eda8ff8 | -9.74623 | -43.57563 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6bcbde3-938f-34f8-841b-a93eca476fc6 | -9.82414 | -36.38049 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 06927ae6-93a1-3f15-8918-4bb9d5aa9e31 | -6.50278 | -44.6843 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e80d9a95-fb01-36ea-a707-b9c03ece1297 | -6.6932 | -43.0601 | 2024-11-07 03:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5d391d8-9355-3699-99f9-b124f74697c4 | -6.96109 | -39.82383 | 2024-11-07 03:32:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| eff7bc69-2021-304b-996e-c89924ea4d72 | -6.07896 | -44.7239 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8b5e8d11-ed69-3e24-8835-ee2f00fa0a5f | -8.49707 | -42.08164 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8c766bb-4a96-3102-8b5d-8a53905d0f54 | -7.77307 | -34.93822 | 2024-11-07 03:32:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0cda9aac-4c86-348e-84e3-a6cabbdf129c | -9.15619 | -35.60098 | 2024-11-07 03:32:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 32a05dbd-2751-3d31-acb0-d3fdad8ce5af | -6.48758 | -44.68483 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12fb6cca-8125-3820-a06a-713e0b58260c | -6.53662 | -44.46041 | 2024-11-07 03:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f74ac736-05d4-3c0f-8b06-2d4c9345a28c | -9.74301 | -43.58867 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1a33262-c4f5-3618-8361-f199925042de | -6.96014 | -39.82739 | 2024-11-07 03:32:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9650126b-d0a1-3061-b9b1-d2fd4d4152ae | -8.31174 | -43.6274 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e5a8d00-3c83-3dd5-895e-58e5a0c4afff | -10.69508 | -37.04791 | 2024-11-07 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ac54eef-c838-38e0-83d1-424b27ebc9b6 | -8.50136 | -42.10948 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 465d6ea7-9a1a-3102-857f-042a2be3f544 | -8.12342 | -35.45542 | 2024-11-07 03:32:00 | NOAA-21 | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e151e125-e4d4-35f6-9df4-44290aac11d6 | -7.55665 | -38.77185 | 2024-11-07 03:32:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 13bc3d0b-01f3-34d8-a331-fdd52a5a7e95 | -6.48864 | -44.68731 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c4fa5e6-2b17-37e4-bc58-7838a38e614a | -9.14542 | -37.09764 | 2024-11-07 03:32:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ecb5358-1c68-308d-9de4-d4639f3ef71c | -10.45432 | -44.89466 | 2024-11-07 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c3dfce7-4dfc-3b14-bdd7-6f19b7d195a5 | -8.3092 | -43.60747 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3057da99-e69e-3dcd-b23e-4c7f3099a7d2 | -12.17956 | -43.53836 | 2024-11-07 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 291b8cfe-68ca-3e14-938c-e035ee82a722 | -8.30396 | -43.61501 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9073fc04-6059-3cb2-a92a-caa3963afe27 | -6.50176 | -44.68172 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 95df091c-3493-3845-9084-345b28872855 | -8.3528 | -43.61872 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| da168d3f-9ddb-3d95-a0bd-22ed482b12d8 | -9.29766 | -43.12333 | 2024-11-07 03:32:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86a404df-69ae-3573-b944-0cddfa7459ac | -8.49985 | -42.08655 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 349fb144-94b2-3851-a8c1-ea89a11ec58a | -6.69397 | -43.05576 | 2024-11-07 03:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41252662-e9ad-3734-a68c-f97badc12ee4 | -11.51384 | -43.26956 | 2024-11-07 03:32:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f3b54d9-8c35-37e6-a37d-c8e69f6bcadd | -9.30337 | -43.12437 | 2024-11-07 03:32:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README23.md)
