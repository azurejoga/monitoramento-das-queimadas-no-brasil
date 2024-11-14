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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a31bf255-e1af-3778-9c07-4fd4819a1f28 | -2.64554 | -46.16999 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| fa475abb-5f97-3810-a931-0ec547781594 | -2.22329 | -48.36976 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ef47a5-12df-3eb8-bd5b-3e9bc78611d2 | -2.15584 | -50.71396 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3b075484-56c1-3570-aa85-fc3581f6b4e3 | -2.88154 | -51.7933 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 07916800-7290-39eb-9a56-ff8065314b2a | -4.48159 | -44.69372 | 2024-11-14 04:40:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae1c6d8-c9ac-39af-ab87-5da577636c3f | -2.25141 | -48.36705 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f58f6c93-e101-387f-886f-7285c4443854 | -2.66345 | -46.80494 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ba3b5f-d200-3d97-8f1b-629297111a96 | -2.65316 | -46.82613 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa5cdc3e-b458-381f-bdd2-b3e85e53b59e | -3.92871 | -47.33413 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afe5c03b-afa0-3cdb-a4bb-8baabcbdc049 | -2.87797 | -51.79275 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2ccbbb5f-bba1-3ee9-96f0-ea938862401a | -2.37365 | -46.50053 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecbfb6ba-faed-3c7c-8b81-a342aeca1a74 | -3.63426 | -48.921 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68f8e63c-1df6-3a67-ab17-b80ab0e61958 | -2.90375 | -48.30305 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aff438b1-1851-38fa-ad9c-0ab8def13129 | -1.20865 | -51.77644 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad19c692-0d6e-3f6c-adcb-3cb353a095f0 | -2.44775 | -48.98131 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b752b360-f6aa-3578-95dd-5f60b17da401 | -4.15487 | -46.24804 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e73ca59-a00e-379f-b45d-73db3c023355 | -1.7483 | -51.13816 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0351ebf6-aa41-3e3b-94ec-6a6fdc52697e | -1.99539 | -52.0885 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd91e4a8-66c9-37b2-846c-74e2908963e7 | -3.74506 | -50.45205 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 456cfd06-3a2a-34f1-be68-771688c18d9b | -2.4275 | -48.8728 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a6ade7aa-1bf7-315b-9a2d-d25833099805 | -2.11266 | -48.2076 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0b5891f-30f6-3404-930f-514ade653d37 | -3.11556 | -51.28074 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dd1f041-a1b6-3e3c-a562-f4a8d39120c5 | -2.82701 | -49.44974 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81428297-7633-3a37-acc9-d6da4a6ef710 | -1.56707 | -52.0238 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdf88c17-9302-3c60-b01d-247311828e68 | -4.2726 | -48.2272 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2e37e54-d347-3d04-b6a0-85080f51b3f1 | -1.63163 | -53.26936 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5fc00fa-c9ee-37cc-9ce1-f0192b05526b | -1.33366 | -51.42033 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e1433d0-8346-3c2e-a9fe-a0345ecfc594 | -4.00681 | -45.56878 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 40212917-8cbe-3f25-9e29-94117e735c91 | -1.03309 | -48.84722 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a1f14bb-e092-3af1-8d6a-7ef8d96b21e6 | -1.7979 | -52.17484 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9b94aad3-503a-3ca5-8fbf-5ff4cf9f322d | -2.69568 | -51.79453 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58456f54-b8aa-3278-b7a5-c515bf334695 | -4.2931 | -48.07214 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bec0758f-fb66-3581-aef1-063320800cb6 | -4.59008 | -46.62669 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9eca6cc2-a79d-34f6-9035-6f1566d3da18 | -3.17269 | -50.45521 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2db52c60-865c-374d-b5cc-d314f233aaab | -4.77516 | -45.73592 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| abb232ff-ce76-3637-b89d-a326587c6078 | -2.16102 | -50.52571 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a120f33-3156-33c5-a20f-87aee4d1c3cb | -3.1763 | -45.44288 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05025dc5-2f83-3023-8ab0-b3ba3bd67c22 | -2.33101 | -51.98569 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec396a19-9a81-33e8-aab0-9536d0801862 | -2.14186 | -48.74014 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a95068-120d-3173-bd50-f269f9244ee7 | -3.02663 | -47.99503 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 999db52a-e413-3ecb-85ca-b43f72d3fb70 | -2.17552 | -48.39407 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04260ac0-2ca8-3b5e-b250-f88191c21fcc | -4.21584 | -50.69865 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d44a5f1-4f31-37b1-a9aa-aaa11aac557b | -1.56364 | -51.85365 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff6eb6ab-08f3-3663-a055-5655bc238133 | -0.338 | -52.02429 | 2024-11-14 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0ee8360-45e0-3111-bc9e-13832cea603d | -4.31035 | -47.75842 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f493032-04ac-3cde-9e89-b062fb4cc7cf | -2.21945 | -48.37268 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c82a7a-faa5-3231-a8da-72477646b3b5 | -2.81592 | -46.65945 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46bf2c61-5ec7-3da0-b873-c4bec3d4695b | -4.11414 | -49.07393 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2f700b1-5dfa-39a4-9bf5-b11b1bd90f10 | -2.24037 | -46.84016 | 2024-11-14 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9960e420-a703-33ee-a912-14b05fe9d4e3 | -4.75509 | -49.08646 | 2024-11-14 04:40:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64ed6f73-2b74-3056-9dbb-d54329eeb25c | -4.00996 | -46.41466 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd7e9a5-23a2-3861-bf56-46b88fa20dae | -3.82324 | -48.86642 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7111be9f-9db5-34a8-95d3-9749e1362ba3 | -2.24481 | -48.38362 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91064e01-8a5c-3004-9059-05d5311cdd99 | -2.40688 | -48.93988 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c84abaec-812e-33de-8828-f2d109f0066f | -4.2887 | -48.23326 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 078280a4-d51f-32a2-860b-ea56cc9ca40b | -3.27269 | -50.57766 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4f4e5ff-cbd3-3587-801d-f0edebca36b9 | -3.46271 | -49.19329 | 2024-11-14 04:40:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb6161ea-69cb-3b22-aba6-9f1fb1bd5e96 | -2.19591 | -46.35802 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9261f24f-d9ff-3470-8b47-0d44e45dc8d9 | -3.05267 | -50.32955 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d380b30f-3e40-3987-884d-3c5247920380 | -2.66857 | -46.81718 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 771201d5-7f84-375a-98a4-5740b34775c6 | -4.11185 | -46.1053 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a5c457e-1157-306b-902f-0a1fa19ecefb | -3.04497 | -48.00856 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f67a275-71f6-3f26-88e7-046d03043683 | -3.03267 | -47.97809 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0f093d5-f91b-3d2d-9607-739f5d01527d | -3.03659 | -48.50001 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdebbc8c-3047-3dea-a45a-5a826e750a49 | -4.04135 | -47.21972 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e8bb8c9-d505-3afe-ab39-72d0773e634d | -6.26999 | -46.91204 | 2024-11-14 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f93bcd-5a35-33c1-8153-e0457ddee91e | -6.02761 | -48.04103 | 2024-11-14 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3f0a5a0-d742-3df9-b0d2-dbfa70480b40 | -4.28304 | -48.20372 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| dcb7aa45-7b09-3be3-8d2b-a924925cd18a | -4.34395 | -46.5516 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 085c261a-126c-35c6-af17-033b80a3346a | -5.15264 | -46.08785 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2889292c-60d2-3ee5-8974-7d4e95c39b89 | -2.71085 | -47.72758 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36ba7b98-04f5-302c-b4b3-9a7da3e7e0b9 | -2.65076 | -46.18285 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b7008cb8-d46b-3289-a445-ff7e2c3572a0 | -2.30896 | -49.08596 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d786d03e-06b2-3666-a685-f1b1720613e5 | -3.01433 | -47.96453 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f28853b8-9175-335f-9811-b0cbd5e74fee | -3.04257 | -50.32799 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 394606b1-3bfb-3bb0-85cd-cf7f09a9b3bb | -2.63755 | -49.53042 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 12746d41-6627-325d-bac9-808f92855413 | -3.24867 | -46.53591 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83c77bd4-4c17-3a03-8d83-2fd1b3b01462 | -4.43935 | -45.95115 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3936602d-33ce-3094-92c8-55f80766ff6e | -2.66287 | -46.80865 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81090e26-9883-33b9-b17a-7f7308690030 | -2.34783 | -53.88241 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9b5cdc4-1b72-36cc-934a-def7c86035f4 | -2.9046 | -46.8564 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ebf3257-e4d9-36a2-9822-10544bb6eb30 | -3.28823 | -45.37012 | 2024-11-14 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0c57f620-fd52-31f8-9467-339c0e3ffee0 | -3.34628 | -45.87535 | 2024-11-14 04:40:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2174a827-a7c2-3410-8c24-58c43dc6bfd2 | -3.02215 | -47.98005 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0121eca7-f2c7-3795-ad15-7819fe61e1de | -2.21193 | -53.71525 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 697b053a-e9c5-3cfd-aacf-85ff9e573754 | -2.2063 | -53.7504 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ee691db-5b89-3676-a007-75bddb9ef086 | -4.15177 | -45.77349 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0f68faf-f6fa-355f-9748-e8a984d6d44c | -1.53803 | -51.11446 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db954b61-2417-3067-99fd-edb1366d7782 | -2.66229 | -46.83514 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf500f3-fcc8-3a21-a1f4-5656021536bb | -3.22242 | -50.58844 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7dae80b-794a-3ac9-838a-3d368375462a | -1.21821 | -51.78654 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dcd7239-d138-39ac-9b43-31b90bf10e7d | -3.62713 | -48.92342 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea386c3b-353b-31b3-b2c7-46ab0c661840 | -2.30413 | -49.11691 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d2b3264-212f-35bc-958b-1980fa9fb2cc | -2.90003 | -46.86329 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 74c9054d-565f-3c7a-9631-f8c36b298115 | -2.90429 | -48.29959 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56b74325-46d4-3e36-9d9e-90c8dee3262b | -1.97094 | -46.58732 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12ac2e4e-68f5-3f05-aeb9-f6e4bc27f3e9 | -4.28537 | -48.23275 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 952b5a80-a36a-3725-9cfd-e155a7b382ed | -2.36629 | -48.84871 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c0f835ba-90cc-3900-a364-c285a49ce54f | -1.61487 | -52.52134 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5fc17d6-0b6e-3fe2-b1ad-6ab501288f36 | -2.37972 | -48.52415 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README31.md)
