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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa1962e-299f-30c8-9675-6f805fe091bc | -6.95327 | -38.61478 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 300852bd-4723-3f1a-a040-1f7b20802d06 | -4.75233 | -45.78253 | 2025-12-11 03:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a6c9542-7cce-32e2-9814-c8fe39d024ba | -6.94309 | -38.61316 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a06056be-c17b-3bb4-9ece-c61f4ef94f4b | -6.42021 | -35.1178 | 2025-12-11 03:46:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e0240503-c1e4-3b6f-a440-f38e3d1f86d9 | -6.43714 | -39.13913 | 2025-12-11 03:46:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2a3563d-d8d7-3a32-897c-35e5de2f40c0 | -3.23149 | -47.47757 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 555a6072-d63c-34c7-af5b-35a852285d1d | -6.94531 | -38.62101 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 650cd791-887a-3dac-ac8c-a74d844d15c9 | -4.12169 | -42.91523 | 2025-12-11 03:46:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a5179986-1c51-3064-86f5-3066b5b3eb96 | -6.1949 | -39.38082 | 2025-12-11 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 49007da6-8e85-3f62-b8ae-76ed9ca1e64a | -6.55769 | -35.2093 | 2025-12-11 03:46:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 096c1c60-6d40-3fe0-9c74-49e0e820a9aa | -6.83937 | -38.58131 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b087876c-3b41-3da1-b9c4-df96351e292e | -2.31337 | -46.48301 | 2025-12-11 03:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10436158-fdd6-38a7-a246-7dacd11b8470 | -2.46474 | -45.32303 | 2025-12-11 03:46:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a30d346d-239f-3998-bac8-400b79dc3c97 | -3.23307 | -47.46854 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 340a6d7a-d660-37ec-808b-e8e13a8c39a3 | -3.17864 | -48.03056 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fae42dc-9d20-319f-aba0-30804eeeabf1 | -5.36026 | -38.06129 | 2025-12-11 03:46:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 19b7a5e0-c607-398d-bda9-0f9a16243141 | -5.24578 | -35.48082 | 2025-12-11 03:46:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 357bae99-83b9-33e6-940f-5689ef65fd28 | -5.67316 | -39.60009 | 2025-12-11 03:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 51c2439f-d74f-3cc2-bd70-df0acc3ff129 | -4.39612 | -45.40929 | 2025-12-11 03:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| addf9b3d-a716-3984-8090-88ed747df208 | -5.00463 | -41.2875 | 2025-12-11 03:46:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 38d60818-c36f-3bee-b540-e3157bee27da | -4.30161 | -44.63476 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0da858e9-2a3d-3d6d-998b-8ca465069868 | -3.3963 | -42.10453 | 2025-12-11 03:46:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e65d3057-d733-32cd-be8d-66eb73f0ba13 | -4.21063 | -44.47327 | 2025-12-11 03:46:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 21ec6edf-1876-3875-9d8f-f8b131447e10 | -4.68493 | -43.25919 | 2025-12-11 03:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b6bb7c1-904f-3a1e-a15d-8693faa63b85 | -4.93849 | -43.95671 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4e919ed0-f461-3312-85af-2cc5c0d50d8c | -3.18725 | -48.02881 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37f578d0-df4f-3cf8-8d15-59dd38082c61 | -6.60692 | -39.52546 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ef29d29-5e32-3f5a-a692-d0d83cad26a6 | -6.25662 | -40.75394 | 2025-12-11 03:46:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7899f2b7-ee25-31d0-ada0-713d4fa8cf0d | -3.17224 | -48.0296 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb9823ac-8f72-3aca-8dca-8dd77469d7f9 | -3.8456 | -47.82697 | 2025-12-11 03:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 403a7e03-5450-3fd5-897e-f4f99d20601f | -6.94367 | -38.60952 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ded4110f-8bbf-34d2-8f2d-20b41b23c037 | -6.19841 | -39.38139 | 2025-12-11 03:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c789c00-f882-318e-87f0-5c0e31c018e9 | -6.93846 | -38.42617 | 2025-12-11 03:46:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d605bb6a-95de-37e4-8124-2d50a75c4523 | -4.60147 | -45.69547 | 2025-12-11 03:46:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a234abc-d77d-3f2e-af7e-a165f148977a | -6.19331 | -44.62081 | 2025-12-11 03:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 754984b0-0ba8-3e14-a3fd-16c868ce4c9c | -5.19405 | -35.61678 | 2025-12-11 03:46:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d8e5a28a-568d-3ef2-a5f0-36550b4e76fb | -3.36225 | -45.34057 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69d41810-d880-38e9-9f93-2560b3cdff6e | -6.94192 | -38.62047 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6dc62a47-080a-3b5f-ac5f-7b4c6e9fedb7 | -5.57736 | -43.75354 | 2025-12-11 03:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77d7d72d-ad03-3036-8b5a-9c4cc6b1b9ad | -5.89276 | -38.17878 | 2025-12-11 03:46:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3da3a873-45b0-37e6-bb57-96400f8ae33d | -5.21036 | -43.4133 | 2025-12-11 03:46:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c2e110e-0be1-340a-a868-4d25f358c2d9 | -5.33927 | -38.69566 | 2025-12-11 03:46:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21c45227-a266-3928-bca5-4e7b680bfb77 | -4.54435 | -44.04674 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3f2e1e1d-c8d0-389e-9d29-6dca1ed11827 | -6.42305 | -35.12198 | 2025-12-11 03:46:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 071bd85a-a6a9-3a20-a16d-9e64b2b34c98 | -3.62707 | -44.64565 | 2025-12-11 03:46:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c2316c-e0b5-393f-b912-d4b82c38c4a9 | -4.06484 | -47.65883 | 2025-12-11 03:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3bcc939-b2d4-39fd-91a1-7d1ed97f02d4 | -4.42682 | -44.50429 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47683c15-6858-3708-b640-4db088faade4 | -6.90649 | -38.0972 | 2025-12-11 03:46:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f8b9fb5-5342-349b-ac1a-4a983a2ff0d7 | -5.35969 | -38.0649 | 2025-12-11 03:46:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b9b52520-face-396a-99e1-16bea2f42866 | -3.40675 | -44.17301 | 2025-12-11 03:46:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc4fb160-4318-3455-b680-6f0e9c1f141e | -3.84718 | -47.82962 | 2025-12-11 03:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 207d8532-2efc-3d53-8970-4bd2d11f5114 | -3.37737 | -44.72559 | 2025-12-11 03:46:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fddbab1a-6fab-399d-a43a-7f2ec34bf2a7 | -3.18087 | -48.02773 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 085374d7-1e01-37c3-a7aa-a2848e21241a | -3.88512 | -42.52243 | 2025-12-11 03:46:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 05228c1a-1233-3868-b275-7dfc9c5bbca5 | -2.47018 | -45.32386 | 2025-12-11 03:46:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b51e233a-d911-363c-958d-7ac6a9e86754 | -6.41965 | -35.12143 | 2025-12-11 03:46:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc9d4e83-bc9c-345d-99ac-3356a30e8581 | -6.96474 | -38.58659 | 2025-12-11 03:46:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 204aa073-d912-3b5f-8165-3fd1804984ce | -4.12436 | -42.91181 | 2025-12-11 03:46:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1e4594d-24c5-3a15-a798-a65645c4d605 | -6.55597 | -35.21314 | 2025-12-11 03:46:00 | NOAA-21 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8ff76309-887b-310f-b1d5-cf6b0fc5b5bd | -3.39617 | -45.41816 | 2025-12-11 03:46:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a36e53c2-d473-3e4d-8269-e099064375b4 | -2.31406 | -46.47883 | 2025-12-11 03:46:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00e0a15c-a790-32e2-b8d7-3e367d9c4357 | -3.11093 | -45.22606 | 2025-12-11 03:46:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62f9e8e2-cc6b-315c-bd6b-b76b872eb5e2 | -4.31423 | -44.5004 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1686d861-8ece-3aa9-9391-7bc94bca406a | -6.60021 | -39.54463 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 97ce0d98-a7c9-3dc4-912a-48756f6e41e5 | -3.49186 | -44.8876 | 2025-12-11 03:46:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 540790e2-3014-344b-8e0e-0ba1ece7b4b2 | -3.10561 | -45.22512 | 2025-12-11 03:46:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a06a91e-0f46-3efb-8ad6-55f4efed46d2 | -3.17952 | -48.02524 | 2025-12-11 03:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 223c727c-6123-3920-94d5-566c95c5b83a | -4.59665 | -45.69131 | 2025-12-11 03:46:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9fe9f01-24ca-309e-9f68-91417a32df3b | -5.82223 | -35.38106 | 2025-12-11 03:46:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f815b8c4-d8cb-34a6-9399-00cae5b811a7 | -7.1204 | -40.2263 | 2025-12-11 03:46:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a378031f-6132-30f8-9594-cfb9bda90f23 | -3.2446 | -44.91499 | 2025-12-11 03:46:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fbc7824-7462-3dd2-b243-c47b674b3b50 | -5.1606 | -37.69632 | 2025-12-11 03:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 1ae7ec76-2887-383f-ac27-bdae8b9a005c | -3.95556 | -41.522 | 2025-12-11 03:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c9cb6505-4521-3041-9198-515c86f33019 | -6.54101 | -40.32659 | 2025-12-11 03:46:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 152ab3fb-71a0-3cd4-a0e3-c411c00ce193 | -4.54916 | -44.04755 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3cedff2b-6e95-37fa-817e-d12e0ed55547 | -6.03149 | -44.32838 | 2025-12-11 03:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2455a52c-b135-3abd-acfc-b2102798ff43 | -3.81317 | -45.18895 | 2025-12-11 03:46:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2c9270c-c55d-32fa-b57a-387e9674ab8c | -6.50436 | -41.49249 | 2025-12-11 03:46:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 805c35a7-9a05-3fdb-a60e-e80e174ad81f | -3.34797 | -46.21182 | 2025-12-11 03:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2317c9e1-208f-3c68-9dd9-a13ebf608377 | -6.5458 | -39.47926 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e97c4d95-ca9e-3b02-9794-830b0ce92282 | -6.82549 | -39.38626 | 2025-12-11 03:46:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 988853a5-c9d4-3645-8e38-3b4433322e9b | -6.55496 | -39.32847 | 2025-12-11 03:46:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4f4d16e0-19e2-38bd-936e-3b1fedec4e36 | -4.24826 | -42.64803 | 2025-12-11 03:46:00 | NOAA-21 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a882dd85-b217-3b08-8d60-dd2ed2f3ef57 | -3.68898 | -40.74165 | 2025-12-11 03:46:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3cff6d7-96e0-368c-bbbf-d6c367e02dbb | -3.69577 | -38.67731 | 2025-12-11 03:46:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71e41191-7489-3938-8ac1-383b2d6427d5 | -6.56445 | -40.20707 | 2025-12-11 03:46:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f92774a3-5e32-3188-8703-51803a904d77 | -4.12618 | -42.91595 | 2025-12-11 03:46:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 255d5f4e-b527-3e8a-bab7-c2b28a649d5e | -3.24414 | -44.91382 | 2025-12-11 03:46:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cc1f84e-3fa4-3dcb-a02b-233d5911da2a | -4.68115 | -43.2538 | 2025-12-11 03:46:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 178ae342-79d6-3091-85c6-722366be7348 | -3.75601 | -45.49723 | 2025-12-11 03:46:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b13ee14f-c9e7-38c6-8468-7c780425c649 | -4.23159 | -45.39613 | 2025-12-11 03:46:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9fcbca9-7ed9-3df9-a456-7519c52816eb | -4.31374 | -44.50326 | 2025-12-11 03:46:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b958819b-2b07-398e-af07-bb70b9589e34 | -4.93755 | -43.95823 | 2025-12-11 03:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 823cdc97-7688-3078-812c-5e6954b964c8 | -9.82298 | -36.05194 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ab72395d-f496-339e-a901-0c0cbd4845b8 | -9.37903 | -40.75417 | 2025-12-11 03:49:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e363967-c2e1-3d7a-8efe-54f27ea743fa | -2.21769 | -45.41173 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aa19237-a42c-3b2f-b7b0-75547c18ad6d | -1.19762 | -47.53683 | 2025-12-11 03:49:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3afbd26-b39f-389a-a90b-8fa43a21d489 | -9.82975 | -36.05299 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 191da313-696a-35b8-8800-67d7cbde425c | -9.82637 | -36.05247 | 2025-12-11 03:49:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| c5158e9a-a86a-3cf0-a829-e09970708089 | -2.28367 | -45.59631 | 2025-12-11 03:49:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README7.md)
