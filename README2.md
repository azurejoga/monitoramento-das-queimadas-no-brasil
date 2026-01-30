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
| 4134a573-1ba6-3267-8059-27feb1c191e9 | -6.93599 | -35.134 | 2026-01-30 03:42:00 | NPP-375D | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ff14a234-9ea5-3410-9146-01e4299705e9 | -8.12657 | -43.14892 | 2026-01-30 03:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 422c68ac-9f9c-3287-8e8f-2ae39da201e6 | -9.50021 | -35.95523 | 2026-01-30 03:42:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b6bbdcf5-a939-38db-acc4-ebc5abe43b0f | -8.17242 | -34.98078 | 2026-01-30 03:42:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81cd8268-3540-3c27-9660-d5b4b7e19bbc | -5.24873 | -37.50251 | 2026-01-30 03:42:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b10d86c3-3691-3d18-9b72-e22b0f728560 | -9.54955 | -36.88776 | 2026-01-30 03:42:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f404e80-5d51-3d18-b8ba-3a0a3dee1ed1 | -8.98306 | -35.30477 | 2026-01-30 03:42:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 358bf4e3-fab5-38f6-87f8-06654f236f10 | -5.17791 | -44.41682 | 2026-01-30 03:42:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d672f147-89ab-30f6-8a4e-f123e1047f1c | -5.26335 | -37.72762 | 2026-01-30 03:42:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2e5a297f-e462-39ba-ab08-ce9c3d18bfac | -6.8718 | -36.24648 | 2026-01-30 03:42:00 | NPP-375D | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 320588cb-16d7-383e-8aaa-b42cfe656515 | -10.10404 | -36.15195 | 2026-01-30 03:42:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 31cd9fec-f56a-35f7-a09e-12a7718649dc | -9.50361 | -35.9558 | 2026-01-30 03:42:00 | NPP-375D | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7329303c-99dc-37e4-b4d2-639a18ff91c0 | -8.79545 | -35.14649 | 2026-01-30 03:42:00 | NPP-375D | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fe49b0b9-d1f8-318b-8a11-15d4b22b8a62 | -8.15696 | -43.1921 | 2026-01-30 03:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 76f48c2d-1961-3b10-b35a-ba5fc54b5cf1 | -5.26505 | -37.7251 | 2026-01-30 03:42:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 470b14a7-4dd2-31df-8e77-4642eb7ac119 | -8.15166 | -43.1912 | 2026-01-30 03:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 17b93cee-e8bc-3f0b-bcec-6a4b1c7c7fb7 | -8.98406 | -36.33263 | 2026-01-30 03:42:00 | NPP-375D | PALMEIRINA | PERNAMBUCO | Brasil | 2610103 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 60ff8f25-2f37-376a-95aa-b69a0f212e92 | -8.12597 | -43.15219 | 2026-01-30 03:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4cca0e1e-9c0b-3344-9751-9a95d2435b9f | -8.13184 | -43.14992 | 2026-01-30 03:42:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4b02f77-5b9f-37aa-839b-89c430629866 | -16.87224 | -40.69699 | 2026-01-30 03:44:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 16378318-2b55-30b7-9bfb-bdeaf96e82e2 | -11.02015 | -45.07032 | 2026-01-30 03:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2b13a16-7ab2-34c4-aa5f-5356fa58e604 | -11.0194 | -45.07416 | 2026-01-30 03:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 20295a83-1455-3550-8a6d-9657f4c6a977 | -16.87609 | -40.69785 | 2026-01-30 03:44:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5cf6279d-2b41-3939-81bc-924af6c9cabd | -16.87221 | -40.69493 | 2026-01-30 03:44:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a2aed646-1826-3979-9859-847d12492175 | -11.02089 | -45.06647 | 2026-01-30 03:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0e07ac6a-c023-38eb-a1aa-f60270e89218 | -11.02584 | -45.07142 | 2026-01-30 03:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 54e59d86-c31d-3ceb-8aed-626bbcb47ffb | -11.12413 | -38.38276 | 2026-01-30 03:44:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| dd74fbfe-a57d-3c58-af52-77428b1e1259 | -11.01523 | -45.06523 | 2026-01-30 03:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 917b7102-9582-3c37-bae0-4d1fe9d0f859 | -16.87607 | -40.69578 | 2026-01-30 03:44:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 0d2c5c63-12b2-3fc6-a91b-f8aa4edc2946 | -11.12783 | -38.38341 | 2026-01-30 03:44:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f5cfca8a-5a2d-3a7b-99ba-2fd59be4890e | -1.8058 | -54.4923 | 2026-01-30 03:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1e0ea3bd-03cc-33b6-a7bf-db4690cd85a7 | -1.8058 | -54.4923 | 2026-01-30 04:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 193ea019-40ff-304b-949b-ff0901299430 | -5.24646 | -37.49921 | 2026-01-30 04:01:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 30a5927a-85c9-3eed-8c9e-b88028893e0e | -3.26118 | -42.55431 | 2026-01-30 04:01:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5390956c-c4fd-342a-8c4a-27a103d284a0 | -4.67766 | -37.93785 | 2026-01-30 04:01:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a843140c-d582-309e-a2ad-eda88bba902b | -5.21875 | -37.3218 | 2026-01-30 04:01:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c3eeb6a4-3965-316c-8525-8a5e0627d0c9 | -5.4536 | -38.37856 | 2026-01-30 04:01:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 06d15e0f-ac74-35d7-9724-66c290a36e7e | -5.53555 | -45.95875 | 2026-01-30 04:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30bfcae0-8ce8-3819-a0bc-e52307721bf0 | -6.42496 | -43.53194 | 2026-01-30 04:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bff8a96-acf2-3944-ae3a-356a9b54ba53 | -9.47293 | -35.96299 | 2026-01-30 04:01:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e9674e8f-4630-35f0-88a5-ebe42ca84249 | -8.1607 | -43.19087 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fe94ab0-81cc-3c15-abb2-b05f545c41a6 | -9.5022 | -35.95659 | 2026-01-30 04:01:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 47adfed0-e0c0-330d-92b2-db17e0f96c5c | -8.12433 | -43.14788 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e83e10bd-17a0-3c75-97be-0ca6fdf5b7d2 | -8.15717 | -43.1903 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46232255-90a8-3855-a5f3-1cd2d068b633 | -7.89512 | -35.32026 | 2026-01-30 04:01:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 867afa2c-bcf4-34ff-b05b-bc389bca8f69 | -5.45697 | -38.37909 | 2026-01-30 04:01:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e7474d6c-15c1-3abf-8cda-59403d5fd241 | -3.25823 | -42.54956 | 2026-01-30 04:01:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ef98c64-9bcd-32af-aa5c-9fb1572f274e | -3.26547 | -42.55069 | 2026-01-30 04:01:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4005afa1-9225-328b-9a44-b4c87bfcd373 | -8.13137 | -43.14906 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a31f38c6-5cca-378f-805e-81cc82673ceb | -5.24993 | -37.49974 | 2026-01-30 04:01:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02c04710-036a-3a92-a6ff-126dd4d6f248 | -8.41528 | -36.02706 | 2026-01-30 04:01:00 | NOAA-20 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ff64008-00cf-3b24-a16f-a30be2546827 | -1.41608 | -45.65656 | 2026-01-30 04:01:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03c5681e-675e-3c58-991a-ba1329c0220d | -5.45304 | -38.38216 | 2026-01-30 04:01:00 | NOAA-20 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb2153fc-651c-3dcb-8bd5-4465f797bc5c | -4.96434 | -50.91462 | 2026-01-30 04:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feb76da9-48ad-3c11-b9df-8598d8e5542e | -4.365 | -37.89833 | 2026-01-30 04:01:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0aaebd78-7751-3092-9754-af2aaea6577b | -5.93491 | -44.45649 | 2026-01-30 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 652e6da8-84b0-32e0-9006-3461b45c3c17 | -3.25891 | -42.54538 | 2026-01-30 04:01:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c74d646-167c-3938-8189-0e3b8a490ec9 | -1.05669 | -47.1341 | 2026-01-30 04:01:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48922d4e-e7da-33e3-8112-b0dea2543fbb | -3.26186 | -42.55012 | 2026-01-30 04:01:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0922af71-9c2f-3d70-91b9-e4fca0bcbafd | -8.12366 | -43.15187 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e29d00bc-d70e-30e9-853a-7d4993951925 | -8.1501 | -43.18915 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ee9212a-f546-3200-a4d6-174fdd699d70 | -4.67709 | -37.94151 | 2026-01-30 04:01:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| adcac520-9158-398c-97f5-dd7cf160ada1 | -5.93462 | -44.45525 | 2026-01-30 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e939a3f8-4895-37a6-882f-20e486a06f0f | -4.52444 | -38.43365 | 2026-01-30 04:01:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a756a9fb-1b72-38b9-8239-121e3fe483ec | -3.91869 | -40.72583 | 2026-01-30 04:01:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7eebba0a-715e-3ab4-a6bd-1c1377dae419 | -1.41314 | -45.65359 | 2026-01-30 04:01:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f675d52-2b08-3572-acfc-d2be0948c2ad | -4.96517 | -50.91 | 2026-01-30 04:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0393b84-2e35-38bf-944f-36d151e4586e | -8.97983 | -36.33358 | 2026-01-30 04:01:00 | NOAA-20 | PALMEIRINA | PERNAMBUCO | Brasil | 2610103 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b453b7f7-6261-3ec6-a14f-8463a2a15d04 | -5.26427 | -37.72691 | 2026-01-30 04:01:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a73cfdea-ee86-37fd-913c-e1f84018e8fd | -8.12785 | -43.14847 | 2026-01-30 04:01:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 149bbbad-de7d-32c1-aec4-a3c285691ddd | -6.42514 | -43.53331 | 2026-01-30 04:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e110531a-fbe6-378c-b6d5-e844f4c65c12 | -1.05164 | -47.13332 | 2026-01-30 04:01:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf05722d-c4e6-3907-a374-db9e535bd3e8 | -5.9377 | -44.4609 | 2026-01-30 04:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3309107d-0d79-37db-adcb-915109eba178 | -5.17347 | -44.41581 | 2026-01-30 04:01:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48d2d3f0-d78e-3aba-9252-fd82e421aed7 | -15.8874 | -43.46777 | 2026-01-30 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 039fdbe5-2f6a-3ba6-bbab-3bd75723ea4c | -11.09619 | -44.81524 | 2026-01-30 04:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 276c53d6-a361-380e-b7e7-c05f42a6a342 | -11.88217 | -44.20506 | 2026-01-30 04:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42fc8d19-d2ed-3d39-be0e-24e63f4f4a40 | -15.89075 | -43.46836 | 2026-01-30 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcf41713-b2c4-3a42-a8f5-b690f69cf22c | -11.01843 | -45.07181 | 2026-01-30 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58e1e046-81fe-355d-b5d7-c70f169c6d0f | -11.1275 | -38.38105 | 2026-01-30 04:04:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b4ce532-65e7-3450-9593-93fa002a40fd | -16.87584 | -40.69619 | 2026-01-30 04:04:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c6d126cc-dbbf-33c7-877c-be5f36b90f9b | -11.02218 | -45.07248 | 2026-01-30 04:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f3bc166-1193-3305-ab76-47553c0288b6 | -13.66131 | -44.30335 | 2026-01-30 04:04:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a84b5f1f-1068-3c88-8cae-77b67623e516 | -20.99446 | -41.80194 | 2026-01-30 04:06:00 | NOAA-20 | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e691278-685e-384b-9c44-2c99a4c93633 | -16.89513 | -42.15559 | 2026-01-30 04:06:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e502d1f2-6d54-3704-91f5-09d3b9324df9 | -20.54208 | -41.71811 | 2026-01-30 04:06:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7d674ec4-3bec-3368-8afe-835210673a55 | -17.70225 | -40.07096 | 2026-01-30 04:06:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2fb6366f-bd95-31f1-945e-6a5cd2eca4fe | -28.63188 | -51.29622 | 2026-01-30 04:08:00 | NOAA-20 | IPÊ | RIO GRANDE DO SUL | Brasil | 4310439 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76f5fa2b-17db-34c8-a63b-a6bdd54613bc | 3.84726 | -60.52833 | 2026-01-30 04:50:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b5ec03a-9c18-38a4-8612-1a7f3863ab69 | 2.74547 | -60.214 | 2026-01-30 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56d9dc31-f13c-39c5-b278-efb62ac8bbb4 | 1.83368 | -60.83544 | 2026-01-30 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e71262ee-f0a2-3a10-a1f3-bc1850943d32 | 3.48135 | -60.07248 | 2026-01-30 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e93c051-401f-3efc-8e6d-ddc14ace95a1 | 3.53619 | -60.71712 | 2026-01-30 04:50:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db25ecb7-0d59-3060-a83b-953e9f6a7c65 | 2.75095 | -60.21322 | 2026-01-30 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e879c6ca-1c65-3b2a-822e-ea192a709950 | 3.53046 | -60.71794 | 2026-01-30 04:50:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3fca9431-763c-3811-a270-f66f40063534 | 3.84783 | -60.53224 | 2026-01-30 04:50:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a49ebff-1e5b-3ea7-82d6-5f500ad9ad69 | 2.74601 | -60.21754 | 2026-01-30 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0147a91-c7cc-3a79-a0fa-aacd04452b6a | 2.74654 | -60.22109 | 2026-01-30 04:50:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f435e027-ec06-3534-a3f5-a580fad92fa5 | 1.83425 | -60.83924 | 2026-01-30 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dbb177b-9070-3ced-aa52-46e755d5fc7a | -3.55577 | -54.72192 | 2026-01-30 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
