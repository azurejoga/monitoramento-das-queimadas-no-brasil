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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98d7af93-156f-321e-9fac-c6ff09bb6a24 | -0.1626 | -51.52868 | 2024-11-07 04:16:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 035dbc7c-11f5-3413-99e5-710b20dac136 | -1.10977 | -47.27746 | 2024-11-07 04:16:00 | NOAA-20 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00aa78ae-7e9f-3f4c-bbc5-78257da640ec | -0.84496 | -52.8436 | 2024-11-07 04:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c145782-f088-3b3a-8976-7395551f413c | 0.53664 | -50.80303 | 2024-11-07 04:16:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ad48bdd-a871-3031-a759-7b6e679174ca | -5.30097 | -50.56684 | 2024-11-07 04:18:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80b6ee93-456d-3374-894a-fa34f090ae91 | -5.01681 | -44.35879 | 2024-11-07 04:18:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 424553fc-ed9f-38e8-8928-bc2de74b3bd1 | -5.28674 | -45.72441 | 2024-11-07 04:18:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd6fae4f-13d3-37b0-9602-302f5e4b7b3d | -8.11945 | -44.41741 | 2024-11-07 04:18:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7409294-597c-3dab-a058-745d8077b095 | -5.01573 | -44.36567 | 2024-11-07 04:18:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08144f4a-5518-34f6-9b86-c656482f0c85 | -3.52893 | -51.59676 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7972c61-1559-311d-916c-023f064ed28b | -5.03086 | -46.83946 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 20182410-ed0a-3468-a1b7-cc522a35fa15 | -2.53888 | -47.28782 | 2024-11-07 04:18:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b7f301c-eccb-390d-b5a0-4b763ec0be67 | -3.70243 | -51.38327 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 373ca61f-0fce-3dc7-89d9-0ec5f1e28ee6 | -2.60038 | -48.20493 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90c904e4-22c3-3362-8e2e-b8feba87f7a1 | -7.34064 | -42.48657 | 2024-11-07 04:18:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5a29d4b3-fe31-3ca9-b5ef-a9fb8c73690b | -3.8125 | -48.98404 | 2024-11-07 04:18:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 369267b4-f804-38ad-a646-c134dccdaa42 | -5.50671 | -43.79132 | 2024-11-07 04:18:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7cf8b6a-230e-3e75-a1ee-4170216a8e9c | -3.72741 | -52.27237 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 435ebc37-ba13-3894-83ac-14fb08a17ee5 | -1.16397 | -53.72661 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5cc60b76-5c7c-3e2d-9bd3-f3696b56d76d | -3.41353 | -50.30073 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64c5a21e-7d92-37d6-8b22-9f59b99c75b7 | -1.3873 | -52.19856 | 2024-11-07 04:18:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78c52cc5-6a17-32fc-a4c6-c78904178879 | -5.11384 | -43.14787 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0f65613-e900-3464-b667-25dcc38b88a1 | -1.62102 | -52.24851 | 2024-11-07 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 839eec1f-cb28-38d6-aa91-3abb10864cc9 | -3.12346 | -51.10778 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae2a7f08-c969-349a-925c-ae10f8ff06a8 | -4.25979 | -50.69577 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5085f15b-3d71-3134-abdc-05b513a369d3 | -2.81174 | -52.96151 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6c1acf3-2733-36c0-8524-91e4cc48e043 | -3.01059 | -53.43456 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09bfd34a-a21b-3c0e-86ff-7a92569baa91 | -8.3483 | -43.61572 | 2024-11-07 04:18:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 348cf029-d4e2-3285-9f75-ec261d56c621 | -2.81026 | -52.93766 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dce61c08-ef1b-3e54-a30f-e28401dcf7dd | -2.60973 | -51.75844 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db543dd5-2adb-3ae5-b55e-7fd6bd9bad6f | -2.85309 | -51.77408 | 2024-11-07 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cff7ac6c-8502-3b54-afe7-3392874ceb93 | -3.31726 | -51.56976 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e3dd13c8-dfc3-38a9-8122-c3df5f29ed93 | -3.03113 | -53.2695 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8221ad44-d9be-3ca2-b482-1d0e7bc1a613 | -4.73878 | -43.24974 | 2024-11-07 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8254f7b-dc0e-3880-8ac7-7dc6c311387a | -3.23528 | -50.45443 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d7457ef9-195c-33c3-9f3a-c8992cdeeeda | -2.83076 | -49.80234 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb0284e5-1aa1-3b6a-ae55-0476685ef37e | -3.44638 | -50.09588 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25dc9fb1-b627-319a-a601-d2aa0c916bd1 | -3.01398 | -53.44328 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e06917a7-0b4d-3724-a3d5-bca7c991076e | -3.43478 | -50.25203 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d832562-3b13-39cf-b4cb-0d018aa4b446 | -2.89551 | -49.37079 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b57afacb-8ade-3a70-8bbe-d0f65e63eb26 | -3.20627 | -50.63175 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b1605b-97f5-3cac-bb7b-a93f087ec9c4 | -3.01458 | -53.43961 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0f787010-9966-3443-a44f-8683e005bc4a | -5.37181 | -46.26372 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7678d18f-b923-378b-a361-55f12ae75964 | -4.34478 | -46.78207 | 2024-11-07 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| caeeb8d5-e757-3255-a0dd-d047e398c38c | -2.50297 | -49.11533 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c3fd8b2a-9ec1-3127-8207-9dacfb7398dd | -3.89787 | -50.09008 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 454ee61f-bcf6-36c7-9498-4313b3b7a930 | -5.0407 | -46.84505 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4dc6edee-1e55-35be-80e6-5599b3bf835c | -3.06122 | -52.50394 | 2024-11-07 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef1e49f7-93be-340c-b1f7-3880dfb7bdaa | -5.98157 | -45.56633 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 287ee103-e8bf-3312-aace-854a4fa84e52 | -2.06383 | -48.14305 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a40d5249-da5e-30ab-b5a2-6373f195d7a0 | -7.81891 | -48.62333 | 2024-11-07 04:18:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35c28c1b-bd09-38b5-a03e-0dc804785ab5 | -3.81406 | -50.63403 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6f8156b-f394-3fe9-ad09-b20b704fc536 | -2.17907 | -48.32431 | 2024-11-07 04:18:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08e1a2d2-b453-32cf-8aaa-bedaa238594d | -2.61446 | -51.30782 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e92c922-aa00-3aae-95f2-c1bb61e088f0 | -3.7414 | -50.06232 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3567bb87-42d4-36fb-acf9-2bd4c4bc2c07 | -6.08195 | -44.71779 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1ddb7ce0-23bc-3a0a-919f-b9924648d3a4 | -5.02963 | -46.84716 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f49383b7-88ae-386e-ad98-198ae02532ee | -2.26144 | -46.46437 | 2024-11-07 04:18:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49b388cc-e3ae-34fb-bb42-2611a0a0d67b | -2.81396 | -52.94815 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ac983e67-f591-3011-b2d0-c80343463f08 | -4.93641 | -46.77336 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f38d751-7418-3a8d-9c44-9842cc266433 | -5.02614 | -46.8466 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 120a83d8-b6d2-3583-8f45-75b82b3d90c9 | -3.43508 | -50.25542 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 643d1754-dfa5-316e-9f6f-1cad6d32c94b | -3.44744 | -52.0066 | 2024-11-07 04:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5e88706-90ee-373c-9869-e7568a35b898 | -4.9362 | -43.63852 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 609cd2da-26ba-3bfa-9689-f42b9dce9c4d | -5.15531 | -46.06076 | 2024-11-07 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 425162c8-af8b-34ed-8ec1-62f72ff8efa0 | -3.45548 | -50.3765 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 655bf6f9-8c2e-377e-b974-f548e7bf4d32 | -5.70388 | -45.94403 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5c48a77-845d-3914-b63d-774582744de2 | -3.38949 | -51.24251 | 2024-11-07 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d7ace7e3-a3c5-39d5-be6d-1fc87ebf0f7c | -3.03937 | -48.03575 | 2024-11-07 04:18:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92dbf0f8-54b9-3b6a-913b-efd2e3d24bd3 | -3.00974 | -53.43485 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fcff41a-6de0-342a-974d-ce8222465918 | -6.17124 | -44.86206 | 2024-11-07 04:18:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c8ee776-920e-3263-a166-b6e02c1320b3 | -2.67007 | -49.88233 | 2024-11-07 04:18:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 006251f4-018d-3b17-b732-14fd5eb81204 | -3.53838 | -47.38523 | 2024-11-07 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e488b4f3-acf3-3b59-8be8-c86cd3693ffd | -7.54058 | -42.62228 | 2024-11-07 04:18:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9492b0fd-2407-3307-ab17-4110a56ef6af | -4.55887 | -48.01935 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa96eec9-e1ab-3878-a5f1-a2aa92d014e9 | -4.2365 | -48.54734 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3011909-eb40-3b9b-b5e9-b44f1b462796 | -7.37829 | -42.9277 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8ce3641-54a2-31fa-9757-4687923aa92c | -3.20417 | -49.2383 | 2024-11-07 04:18:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e3486d81-4f62-39e6-9066-c0d36a4913c9 | -3.27063 | -50.34891 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16a91e7b-2228-37e5-8ccf-97e7376efd32 | -5.33755 | -46.19437 | 2024-11-07 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 091de7f2-58dc-3703-b3ca-0c680447dbca | -5.52116 | -46.53728 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 922369dc-ac04-3d98-9675-0e024369ce50 | -3.43579 | -50.25121 | 2024-11-07 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9eebcc2b-480b-3868-b58f-90c7ef1cc197 | -7.54126 | -42.84863 | 2024-11-07 04:18:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aedb3722-94d4-3843-b045-8f34c4e69a75 | -2.22752 | -46.86436 | 2024-11-07 04:18:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de68d5b8-0ed2-38eb-b95a-b73fb1c15c74 | -5.36047 | -46.424 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39e15bff-0194-3fa4-9adb-715d73c0a5f9 | -5.98558 | -45.36961 | 2024-11-07 04:18:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| de26925a-7d72-3394-8ead-a7b99f2bc5a2 | -5.71997 | -43.81761 | 2024-11-07 04:18:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ae81493-dd03-3cda-8138-09d55db1fdb5 | -2.76725 | -53.22882 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1497620-2d97-3116-bda2-4ede6289c53b | -2.61891 | -51.30615 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 78d64493-8a6f-3cce-970d-429d1a47c824 | -4.4 | -50.69481 | 2024-11-07 04:18:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f89db1a-8903-330d-8413-8dbfdd5cc532 | -3.11266 | -53.12585 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6614e6fa-ba59-3b9a-97db-23d0b53cc400 | -2.05995 | -48.14243 | 2024-11-07 04:18:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91f4ee0c-0fe4-37b0-a21a-ea12a7e5b8ca | -3.01517 | -53.43596 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75d70699-19ec-3e0d-98d2-b2b4628c3c9c | -4.34992 | -48.62477 | 2024-11-07 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a5706f2-d31b-3b60-b458-2191e752d187 | -3.15349 | -50.20966 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 58420f7b-a46b-34d2-8c00-0488545c6819 | -8.18783 | -42.83396 | 2024-11-07 04:18:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7b3a9c8-3fbc-308b-a51c-fbd0db3d6820 | -2.433 | -53.66898 | 2024-11-07 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39f49f51-ccba-3704-b3b3-d9c486cc1d9e | -3.29158 | -53.11457 | 2024-11-07 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 014844f2-9f09-34ed-b574-75099c7d4868 | -5.03722 | -46.84445 | 2024-11-07 04:18:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d067d83-cacc-3fdd-9815-730d1a0aec27 | -3.24044 | -50.45074 | 2024-11-07 04:18:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README26.md)
