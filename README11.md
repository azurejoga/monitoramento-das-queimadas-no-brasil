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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fad4f1a-184b-324e-8bad-0863eed2ab8f | -10.75635 | -44.91244 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bb90eec-6b48-3887-8866-e12c63c7d29c | -10.91505 | -44.63131 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d27c3a5-4abb-3eb0-8f11-aca9381ea801 | -8.99175 | -37.54889 | 2025-11-13 03:23:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 494e0404-098f-345f-9d00-2d54ead92fa4 | -7.14814 | -41.70417 | 2025-11-13 03:23:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5c00c419-e895-3ec1-8cc5-3a48a90783c1 | -7.83023 | -41.77089 | 2025-11-13 03:23:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 81b860e5-ddce-3a9c-b8bf-b52710fe4f22 | -10.92176 | -44.63276 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 848ed7bc-7ef2-31cb-bcb0-96e76de22f91 | -7.52736 | -40.08264 | 2025-11-13 03:23:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 73a61a7a-2e82-33e6-b6f7-dc1442442970 | -11.01799 | -44.64181 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7416803f-1d0f-34f8-8dcd-a94ecc861c1b | -9.62798 | -44.5587 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ad97d41-d371-34ba-8fb7-c31665cca0b8 | -10.75503 | -44.91877 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25154399-1707-3e76-b2df-797d10165743 | -9.6431 | -44.55437 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9768a738-3a68-3ac9-a327-b37b1f80dcb1 | -10.68731 | -45.0044 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b86d872f-1f5a-38ca-90c0-a9c360112688 | -10.63008 | -45.2476 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffb92586-f763-305b-8415-f375c2271989 | -9.64351 | -44.55111 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac5203e8-ba96-35f5-b095-3bb7c9555584 | -10.91314 | -44.63063 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3f44a84-e470-3011-8031-9fdeefc36b25 | -8.74099 | -44.24205 | 2025-11-13 03:23:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffb0813b-abdf-3a2b-8a59-c7fdac1cd20d | -10.71454 | -45.15416 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 937a2ba7-155e-3c96-b977-2b50cb46a987 | -7.08149 | -41.58153 | 2025-11-13 03:23:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6cd3ebe-4239-38c1-aa83-1e16caf0e0ec | -10.91984 | -44.63214 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 379ec5d0-3be5-3cd1-9301-d315f39a5d1c | -7.8184 | -41.7802 | 2025-11-13 03:23:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c0e77237-5933-3456-b233-ef104b620e51 | -7.4592 | -44.74183 | 2025-11-13 03:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558ae210-6c0d-3ac8-bc94-498667b38507 | -7.82699 | -41.76755 | 2025-11-13 03:23:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b42edded-0bc5-39c3-930c-963886739f88 | -7.22038 | -39.95928 | 2025-11-13 03:23:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 232ac5e9-4334-3cd8-9189-b13576010ca3 | -9.63536 | -44.55637 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63091f54-d0be-339c-a8db-7a907085dce5 | -10.62307 | -45.24623 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4ce8e621-d64f-34a0-bc99-ae49ab68bcfc | -6.87634 | -42.853 | 2025-11-13 03:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| da9f6f55-f2fd-35d7-88be-9a0ae27b5eed | -7.52675 | -40.086 | 2025-11-13 03:23:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 29758eb0-bb6a-3da5-8dea-2b54ff9a5307 | -10.74692 | -44.92335 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3afc61e1-0d3e-378a-9cc5-c1d494d251d4 | -7.81748 | -41.77301 | 2025-11-13 03:23:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d4d7cac-b1b0-3d62-906f-42b6e13878a1 | -10.84945 | -44.9456 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67818773-ac31-3f57-8edb-a0a0c9bbbd54 | -12.10703 | -43.65233 | 2025-11-13 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42f40001-a29b-3b7c-b7f9-4d9bca6b8588 | -7.81833 | -41.76834 | 2025-11-13 03:23:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9d8bbb4f-5041-3a50-b307-fbf4b4ad1f2b | -7.45778 | -44.749 | 2025-11-13 03:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 122e5468-eaab-34cf-a9df-dfad38974928 | -6.54803 | -43.10636 | 2025-11-13 03:23:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab08d6c-a8c5-3e08-ad7b-2ce04dd47443 | -11.79711 | -44.20708 | 2025-11-13 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a5d9b4d-e1ce-3383-8a1f-ef665b147859 | -7.81333 | -41.7743 | 2025-11-13 03:23:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59f096a7-bf3b-3360-bb2e-66ad1c2a64de | -7.22101 | -39.95577 | 2025-11-13 03:23:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 178c087e-add5-30b6-b35b-5a67adb4301e | -7.82105 | -41.76625 | 2025-11-13 03:23:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 14a8161e-3477-3fe7-a6ec-226b5b72ad6f | -11.0247 | -44.64325 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3737982c-2272-3972-bd7d-e57c3a0823f3 | -9.63622 | -44.5532 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4a324d2-7471-37ed-9a77-a5be88565bbf | -10.62165 | -45.25309 | 2025-11-13 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c331cb2c-7fa2-3f83-a558-ee20e0fe6b34 | -9.62931 | -44.55222 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 858119c3-c51b-368b-b1aa-d9c0ad89a183 | -7.81919 | -41.76364 | 2025-11-13 03:23:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0585b2b4-84fc-391b-b3c2-6e84dbdbedd3 | -9.62845 | -44.55535 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b29c957-02a8-340c-95a6-9b6b085f33b6 | -9.62974 | -44.54881 | 2025-11-13 03:23:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ff4b039-5387-3117-bc74-c2e6fdc809be | -7.10659 | -42.37251 | 2025-11-13 03:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d84082e9-6912-3868-b8e6-1de06efc2cfb | -11.02113 | -44.6385 | 2025-11-13 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d279f0d-e092-330f-af75-4187ba9024a6 | -7.81422 | -41.76965 | 2025-11-13 03:23:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f0bf05d5-457c-33d8-9f2e-be1ff408acf5 | -10.36908 | -45.06034 | 2025-11-13 03:23:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e78abed8-ff14-3b48-84b9-d52c21992886 | -12.10995 | -43.64988 | 2025-11-13 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df6aeab8-014a-3d7b-a3c3-f02335ed400e | -11.81382 | -44.25727 | 2025-11-13 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74f3eb36-2b77-3448-b394-f6980387642e | -7.10034 | -42.37123 | 2025-11-13 03:23:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| eff01cc6-f1bb-3660-a8d6-514d2b87eef2 | -7.11475 | -42.72596 | 2025-11-13 03:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dd3d3770-31c6-3634-8450-3e0ba3bf7af2 | -12.10806 | -43.64729 | 2025-11-13 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e505f799-cff3-3664-ab55-f58a2535a7b7 | -14.09694 | -43.46546 | 2025-11-13 03:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9109da68-9e5d-36d9-b104-6f66c0586b49 | -18.16827 | -41.30871 | 2025-11-13 03:25:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f8d1d818-fc9f-3887-823e-2beee246cdbb | -17.32307 | -46.50611 | 2025-11-13 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c16aecf5-9b2e-3cd7-ba45-e125344c58d5 | -15.29835 | -43.89964 | 2025-11-13 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37460cb5-7045-346b-a7fc-0401b55a0e54 | -17.31644 | -46.50436 | 2025-11-13 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51b063ee-8b13-3adf-9bbe-4b30444d0f1b | -19.0531 | -40.3283 | 2025-11-13 03:25:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7764b539-c27d-302e-94b7-27b2e3fa1965 | -16.44752 | -45.01323 | 2025-11-13 03:25:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4805a67-1455-391b-aeb3-819ae80c79c9 | -18.16367 | -41.30662 | 2025-11-13 03:25:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b9a31e8d-1cc9-3415-bd72-dbe36d20fe06 | -17.32095 | -46.50327 | 2025-11-13 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8c6368aa-1570-3552-bd76-7c93fd33e7a6 | -16.44475 | -45.01141 | 2025-11-13 03:25:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2bb5d7e-a6cd-3de4-b96a-b7e0367f8e18 | -15.39509 | -43.07053 | 2025-11-13 03:25:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e043c8dc-fec5-35cd-9139-fc8379facfbd | -14.09789 | -43.46091 | 2025-11-13 03:25:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9119b1c9-ede3-32fd-bd36-d481a7b9188d | -16.44869 | -45.00782 | 2025-11-13 03:25:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 11d2e1b6-2367-3a3d-a33b-8e53487d755f | -20.45541 | -42.51194 | 2025-11-13 03:25:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 04298970-b269-3de7-878f-0035e9f6ed14 | -15.29244 | -43.89806 | 2025-11-13 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3789546a-5947-3fb2-93d8-fa1ec57161af | -15.39425 | -43.0746 | 2025-11-13 03:25:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 940411e1-255e-3015-99aa-68c7c4d76920 | -16.44595 | -45.00606 | 2025-11-13 03:25:00 | NOAA-20 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fad4d693-0722-38fc-9631-a24f5bc1ece2 | -22.46796 | -44.2025 | 2025-11-13 03:27:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 616c0e3e-f0f7-3b8e-ab1b-39a71ff4c25e | -22.46713 | -44.20625 | 2025-11-13 03:27:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f47c2a4e-d37c-335f-8523-d3a4874e3cd4 | -21.85431 | -45.01966 | 2025-11-13 03:27:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd6837ac-f4cc-3c7b-b49e-6829931cf312 | -22.64227 | -44.91436 | 2025-11-13 03:27:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b999f5b8-0488-3a2b-8aee-d4337e72e49a | -22.46188 | -44.20478 | 2025-11-13 03:27:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b93304f1-1d2b-3724-8a5e-9b51a4a149c8 | -21.48625 | -44.93611 | 2025-11-13 03:27:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2336bbcf-4928-3cef-9609-2c7b00df9fd3 | -22.64137 | -44.9183 | 2025-11-13 03:27:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c813a5d4-337d-338a-a050-29ff078ce370 | -21.49094 | -44.9416 | 2025-11-13 03:27:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 00fd047b-caa9-38d9-a3fe-f4bfb63dc1a5 | -21.85336 | -45.02383 | 2025-11-13 03:27:00 | NOAA-20 | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 42fe0c73-7d8a-3931-bd9f-190e0e4b3148 | -22.46878 | -44.1988 | 2025-11-13 03:27:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ae9447c2-ebba-3897-9071-befe209d6793 | -22.64604 | -44.92337 | 2025-11-13 03:27:00 | NOAA-20 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3e84bbf-a829-392a-9439-ecb859fa1523 | -3.8658 | -49.7998 | 2025-11-13 03:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b425c269-f991-3732-b996-4bcd6c95d633 | -3.0916 | -49.2759 | 2025-11-13 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 2bb2a290-f65f-3b27-a417-24b70bbe9397 | -4.7204 | -46.4497 | 2025-11-13 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e7a72808-3966-350f-93f5-8f2e38ff47c1 | -4.7206 | -46.4276 | 2025-11-13 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 148c691e-54c3-3603-b1ca-f9c3aada373c | -4.7018 | -46.4508 | 2025-11-13 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 60fc0527-4850-3c71-85e1-b79a25968239 | -12.6557 | -46.7407 | 2025-11-13 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d1218398-7c97-37ee-8f73-d2fd74f6a60f | -4.7018 | -46.4508 | 2025-11-13 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| b02407ab-b614-3df3-affb-41d6ec84ed89 | -4.7204 | -46.4497 | 2025-11-13 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 9d39400e-7a60-3335-b982-edab24df2e59 | -3.0916 | -49.2759 | 2025-11-13 03:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c2a7ce63-c1c4-3ce9-aae7-da4e66cc7340 | -12.6557 | -46.7407 | 2025-11-13 03:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| f032be71-3341-3cf6-a88a-fdeb4e46829b | -3.8658 | -49.7998 | 2025-11-13 03:40:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| e3a44996-e4e5-3749-8c42-ccafdaca6ce5 | -4.7206 | -46.4276 | 2025-11-13 03:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 514e5a0f-5744-347a-a766-aa48668787b5 | -4.7204 | -46.4497 | 2025-11-13 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 3fbc5a9a-4f6a-3765-a960-bd99c544ab0c | -4.7206 | -46.4276 | 2025-11-13 03:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 09383e21-2554-30cf-82b0-fa4770429483 | -12.6557 | -46.7407 | 2025-11-13 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0df80e80-baa4-337b-82c3-e088b9b71e2f | -3.0916 | -49.2759 | 2025-11-13 03:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 502c66f4-ab39-3d62-bad2-e917ac12d2ea | -3.8658 | -49.7998 | 2025-11-13 03:50:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 6986e06b-7aca-34ac-aeb4-e355648aaf7d | -3.8658 | -49.7998 | 2025-11-13 04:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |


[Clique aqui para ver as próximas entradas](README12.md)
