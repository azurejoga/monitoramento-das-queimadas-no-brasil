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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7a3fbd4-9b1c-33e9-80ef-541c5f2d89a2 | -14.5336 | -48.4268 | 2025-09-29 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 115.9 |
| db9086ec-4247-395e-a381-2ddb7dcf5dd2 | -11.8485 | -51.7705 | 2025-09-29 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e4f00cfb-0606-390a-8af4-54ad5bd4490a | -11.8291 | -51.7937 | 2025-09-29 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 71ec80e7-671f-3e87-81d5-261dfe9343ba | -11.8294 | -51.7725 | 2025-09-29 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 535adb75-3fcf-3566-944d-91368a62bbd3 | -11.8482 | -51.7916 | 2025-09-29 04:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 11c863aa-9514-364e-8d2f-a0edfc9c7446 | -14.5526 | -48.4461 | 2025-09-29 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 8378c29d-d262-33fc-80f5-ad6319f5bc39 | -9.4007 | -54.6984 | 2025-09-29 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 36207dbe-ddb4-3141-af50-a1ab63404e54 | -18.218 | -53.2962 | 2025-09-29 04:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 49.4 |
| fbe07a7f-e1b2-3803-ac06-1c08e6547fa4 | -15.2893 | -49.5035 | 2025-09-29 04:20:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 4bc4e823-4eee-35ed-96a1-8cd9c1792dfc | -9.4007 | -54.6984 | 2025-09-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| fab54299-e0bb-3bfc-b81e-c922b1356fad | -9.4194 | -54.697 | 2025-09-29 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 2603b7ec-40df-35c4-bf5c-b8bc604678ec | -2.57735 | -48.40354 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f610ce9-34f0-3a20-8322-d827cdf8ed9d | -2.7046 | -48.83725 | 2025-09-29 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da722c8f-d740-3dbe-85a3-f4511456aca9 | -1.53538 | -48.70825 | 2025-09-29 04:55:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5183ae08-472c-3478-a2bc-8e6e81735b77 | 0.32473 | -51.4494 | 2025-09-29 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 451c57d6-5959-3dff-9ea4-470cdd8d5002 | -3.10352 | -47.01838 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20528fae-1b32-3af4-ae64-ff029af38d8c | -3.0848 | -47.76112 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d3d3a23-4198-3ca3-ab9a-0dd11df3a4cd | 0.31804 | -51.45044 | 2025-09-29 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cac083e4-3a64-3cd4-8a3b-9080986add75 | -1.53375 | -48.71115 | 2025-09-29 04:55:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bb92960-8888-34e4-b97f-b727b955d972 | -3.10102 | -47.0044 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 450f1b2c-18af-3d38-bf5a-2664f8481072 | -3.10993 | -47.00578 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6723245e-d794-39d2-bcf9-4bc3ec324f0d | -2.22634 | -48.37228 | 2025-09-29 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51124259-2830-3f20-8f95-385c1be24f55 | -3.09528 | -47.01255 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b48377ee-fc69-3ae4-93bd-8b8b6fe75631 | -3.09972 | -47.01327 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5efc2276-cef5-3384-bb9c-3470b3e05baf | 2.2661 | -50.73566 | 2025-09-29 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a39c6711-3801-30c9-a85f-4b739e2a1621 | -2.58538 | -48.40479 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a4e59830-0d3c-31de-a8fa-0ffc86d151d4 | -3.10928 | -47.01022 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a0b1c8bc-f9ad-3b42-b9ea-390c6e3793ed | -2.22816 | -48.37207 | 2025-09-29 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19a9247f-c607-3b22-b1fa-f2f13cd13d1d | -2.55022 | -45.15724 | 2025-09-29 04:55:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb441da8-efc4-3917-9853-d6671f3b849b | -3.10037 | -47.00883 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 534bc986-e4e1-3580-85fc-6653a8865c24 | -3.09908 | -47.01768 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6867d751-f12a-32f2-8766-92d6461265ed | -0.0972 | -51.2735 | 2025-09-29 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc1c678-2728-3291-86b7-aa0b72f39dc1 | -2.91688 | -48.19411 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ea875ec1-e2a9-39cd-a10f-462260300715 | -0.99595 | -47.06014 | 2025-09-29 04:55:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6f1cfb0-3954-31ce-ae6f-3e91c28c4ee3 | -1.02337 | -48.74171 | 2025-09-29 04:55:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 623bb8ee-842c-3efb-aa65-d9adf12cad47 | -2.22688 | -48.36879 | 2025-09-29 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5d164aa-2440-3e78-ad2f-bb0ed0c24c99 | -2.7054 | -48.83449 | 2025-09-29 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fcce5fc-bde2-31e6-8b8b-311999175008 | 2.26554 | -50.73206 | 2025-09-29 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a58e5bff-7e34-37c3-baef-608c4de145c2 | -3.10417 | -47.01397 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| afaf70ae-bef5-330b-888c-485c16bb0505 | -3.10548 | -47.0051 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd73b7db-02b6-3555-a79c-dcb2b9990037 | -1.42399 | -51.62011 | 2025-09-29 04:55:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f119beb6-4a39-3efa-86ad-4858aa86d3c7 | 2.26329 | -50.73979 | 2025-09-29 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ea2c88a-62c6-3998-a686-af83f5b30c3a | -2.22868 | -48.36856 | 2025-09-29 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 091a12a6-d96e-37ce-90de-aa631249efc0 | -2.58084 | -48.40767 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3dd4f3c5-2212-3e56-9ae9-2d955df03943 | -0.10113 | -51.27042 | 2025-09-29 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 99441f1a-6af0-3951-b66a-c83adfadcec4 | -2.30296 | -52.90641 | 2025-09-29 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec4bfc5f-d66e-3358-8895-0c45a8d9c90b | -3.10482 | -47.00955 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8a73261f-63ed-369f-bcdc-851dcaa4f229 | -3.09593 | -47.00811 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df1f9b48-86fa-3caa-b7d2-fafc15443185 | -2.58189 | -48.40068 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9132497c-8585-3065-9d14-900d243defb9 | -3.08432 | -47.76268 | 2025-09-29 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01fc3005-a8ca-3cae-8e17-d6a23678c859 | -1.94605 | -52.02857 | 2025-09-29 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b469c73e-3304-30ea-a4dc-f4ddffc10bec | -2.80537 | -48.62675 | 2025-09-29 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 353c3dea-bc58-30e6-a3e6-5882149711af | -3.05633 | -49.59674 | 2025-09-29 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aa47211-d8bb-3c70-b0bb-7c0e60ea3311 | -2.58136 | -48.40417 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 4e7cb76e-e610-3424-a99d-3f142524f5a0 | -2.58485 | -48.40829 | 2025-09-29 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b3e23c5d-f412-3c16-ab9d-a1cc64086926 | -2.80236 | -48.56635 | 2025-09-29 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 046d79ff-41b0-379c-81a6-071d72bb9fa4 | -2.96597 | -40.84129 | 2025-09-29 04:55:00 | NOAA-21 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4e793cc1-d62b-39a3-9e6d-6ac53597df37 | 2.26273 | -50.73619 | 2025-09-29 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ab75bb42-6ab0-360f-aa09-48e236e9b3af | -2.8059 | -48.62332 | 2025-09-29 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e615798-2d0e-3ebd-a0be-2bd45c36950e | 0.59689 | -51.5774 | 2025-09-29 04:55:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0856657c-9ccc-3bb7-9ece-79d6a9b81602 | 1.42968 | -50.92446 | 2025-09-29 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5111e313-7a12-3d4b-81fa-fe8f35837c00 | 0.32139 | -51.44991 | 2025-09-29 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45237930-8e6e-3cf2-bdd6-832d566e3d22 | -0.10057 | -51.27402 | 2025-09-29 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6de09cc-56f0-30d3-8b89-321acd5080b2 | -9.05687 | -46.71988 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3a89af36-da13-3a3d-a7e2-2a91d13684a5 | -7.03555 | -45.18305 | 2025-09-29 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d544393-2209-386f-9f6a-0eeda1d15e6c | -10.82035 | -47.93316 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a47bbe2-7e4d-3089-bd6e-94903d053937 | -9.27483 | -45.69955 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a93c5a03-a686-3a16-8542-7ce359347427 | -10.48461 | -49.36637 | 2025-09-29 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8671aeb-6e49-3c00-a85c-3a86388fbded | -3.5003 | -52.4702 | 2025-09-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 219d7a46-c4ad-34ca-b71e-4c748581b6e9 | -8.25916 | -45.49192 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 478ad1e6-483c-32f3-8cbc-54a270101713 | -7.22856 | -44.79331 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e7ea29ee-6c02-3396-8363-c68808780de3 | -11.43966 | -44.96107 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53c2deba-0fb8-3318-b869-ebe01b1a4b95 | -10.17933 | -52.57669 | 2025-09-29 04:57:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3ac4fc-7f3f-3a10-995c-6427df339729 | -9.31575 | -45.70443 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5b5a201-61bf-31fe-957d-6396310c2eac | -8.30072 | -45.49258 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0bd1991-978c-35f1-8f0f-0917616334c5 | -6.83004 | -44.82869 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5946ea68-1186-3268-88c2-1a1760bc7bb0 | -9.77322 | -46.1782 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db04f4b5-ff05-3a84-8ed7-8f6a4cadb6d9 | -6.1994 | -42.84562 | 2025-09-29 04:57:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 17208a7d-c3c7-3ed5-b870-47a1c989abb1 | -6.42916 | -43.50941 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ad11a6a-9de2-3768-88a1-db44b62ccd90 | -4.31735 | -48.08612 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1740bd84-6816-3167-baaa-07b3eb06f03a | -7.14312 | -45.49863 | 2025-09-29 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11673a07-444f-31b3-a2fe-2d2bef528a2d | -11.217 | -47.74779 | 2025-09-29 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7cbca3b-04b0-339e-b6bc-71ff1cea9c32 | -9.63823 | -48.12611 | 2025-09-29 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9547feed-439a-3605-9a64-fcec700d516e | -10.4019 | -48.15377 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bab6c3fb-ad3a-3f59-8265-ac164efb1f28 | -4.67252 | -50.97417 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdf2cd0b-5ee6-38ff-b92d-7c8c9a9477b5 | -6.22241 | -44.20286 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91e7437a-4cbd-3e71-a669-39c8725484e9 | -5.74166 | -42.66976 | 2025-09-29 04:57:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 37e22645-5aea-372f-b8e4-4ee1c3b81411 | -6.49568 | -44.25363 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a9b018c-9ffe-348a-a1c1-561c3b0f7487 | -8.29785 | -45.47306 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cd138b5-2984-331e-9ebf-3fef45775dcb | -5.88517 | -43.29827 | 2025-09-29 04:57:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc1223d6-6212-3dc6-b4c8-7c9aa7085ced | -9.77239 | -46.1937 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d085ad07-2517-3a09-b37d-33c78883ba41 | -8.15309 | -46.40434 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d68ec584-e67f-36fd-8aca-475505de4908 | -9.06077 | -46.72038 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bfe02368-d6c9-380a-b43c-8baa55a24f7d | -9.39641 | -54.69982 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d701ce42-5268-3c02-a8d1-d641fbccad39 | -11.4107 | -44.90284 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd685215-c750-363e-9688-990bc505c717 | -6.89248 | -44.52658 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a05f7762-71a6-30b5-ad9c-d484b5f21c23 | -9.41123 | -54.69148 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8d0fddb2-a512-3c22-a32b-7f78e6753f7a | -6.74221 | -43.37801 | 2025-09-29 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a60ca1e9-c493-38bb-b037-4518c21160f7 | -6.27961 | -42.48856 | 2025-09-29 04:57:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 224f0e0e-8274-3dd2-bd9c-bbb726820fd6 | -8.86778 | -45.02956 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README56.md)
