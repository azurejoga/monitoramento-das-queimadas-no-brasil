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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da487c4f-1773-3f89-8fcf-5e7a1639c37b | -10.88088 | -57.45664 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5ba22e7-ccc0-335a-b859-600102f59e30 | -10.88047 | -57.48055 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fca6622-de9a-3446-9ecc-e95244273710 | -10.87767 | -57.476 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 142da60e-65a5-3cb6-a5e3-aec72b73f508 | -10.87703 | -57.47989 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d783ec5-2479-36fc-b2d6-cbabee3237ec | -10.87679 | -57.4599 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7112b91-506b-3f01-9873-5ead53724896 | -10.87398 | -57.45547 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c14a4e1f-d62b-3cd7-b8bb-65ce5cebdfbf | -10.87358 | -57.47927 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b265f49-7c4b-34e2-aafc-13f7b6100e21 | -10.87334 | -57.45931 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b742ae8-146f-3024-ac6b-929b4ff75723 | -10.87206 | -57.46701 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| feb3b272-1585-3ddc-8188-01dacab5fe19 | -10.87142 | -57.47089 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2c7f04c9-87c0-39e9-abda-53f9599d197e | -10.87013 | -57.47866 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4936bb0a-77e8-324b-929e-ec174b84c358 | -10.86989 | -57.45872 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a0c419d-e752-3673-9067-c691ddb9b3f7 | -10.86926 | -57.46255 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d6a512f-a9c6-30a9-a9f8-60050d9cf377 | -10.86861 | -57.46641 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d54c665-edb7-38fc-afb2-e7e5505b8268 | -11.62472 | -57.10218 | 2024-09-26 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 264d913b-a1b4-3372-bec7-a711f8f7a607 | -11.05017 | -57.30484 | 2024-09-26 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db9e42e1-c8dc-38ac-a27c-5b4d4dbf436a | -14.9379 | -57.95466 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e91b88d3-2e83-32d6-92a0-e8a66a800353 | -14.93727 | -57.95845 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0ae6aa54-a158-3074-bd53-87732f3cf118 | -14.93199 | -57.9692 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 808d8d55-a41b-3ac8-8c47-63d283b243ec | -14.92483 | -57.99121 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a47e81f-704a-375a-bbfe-6ff0836c98dc | -14.92143 | -57.99062 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca3133fa-ea93-35c2-95bc-f14b7d7bb23e | -14.9208 | -57.99439 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27400ed4-1c78-3f44-9db5-bbd86285d9d9 | -14.92018 | -57.99815 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee2384d9-a6d6-3c1d-af80-a898b0a35e2f | -14.9174 | -57.9938 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85acd156-fbf8-3597-92e4-4e13086a4d27 | -14.91677 | -57.99757 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f705f6a-7138-376b-8d76-5e0a693234b0 | -14.91213 | -58.00443 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b2cf3b2-34bf-3937-a81c-d0c2274964b5 | -14.91153 | -58.00808 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a442cc95-63c9-3acb-b6c7-639846f56af2 | -14.90997 | -57.99638 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fea96faf-da59-3229-a3a1-e1cb63f65a92 | -14.90657 | -57.99576 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c01ad862-4ef7-34a6-a426-69339560d98a | -14.90413 | -58.0105 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31f799d8-21d4-3887-a458-b008e4ffe7f4 | -14.90359 | -58.01038 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 279299b0-cb2e-363a-a3e0-a22d6d29ef2e | -14.90351 | -58.0142 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73eb01ac-f844-370f-856f-63694871e3e1 | -14.90298 | -58.01408 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39863f6c-f38e-3941-bb38-8d258a720e2d | -14.90289 | -58.01794 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 548f8d73-1a93-38ac-adf0-8d44338e9b7f | -14.90237 | -58.01783 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 552368ad-bd12-327e-bd31-dff0000a9160 | -14.90019 | -58.00978 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdc7413c-8ccf-3d91-9108-a4f048404b54 | -14.89958 | -58.01349 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b51778cc-e8e0-3998-9c30-77c939ac706c | -14.89897 | -58.01723 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 12b05aea-c0d7-32a7-baf0-47f25c32a0e8 | -14.89679 | -58.00918 | 2024-09-26 04:59:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fe8b789c-004c-3d82-bf9a-0309dfe4c88a | -15.35397 | -58.18131 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0794d607-01b5-316c-9b59-6858266ee91a | -15.35057 | -58.18064 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ab648ff2-b8da-3c25-8cca-1f330a93ca0f | -15.3499 | -58.18461 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e6367f73-d1ff-385e-a597-bf3c5fcf21f2 | -15.34503 | -58.17175 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0aad0f3-60eb-392d-9d59-e2deef6a9a04 | -15.3444 | -58.17554 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b1a70ce-ad2f-3716-844e-1361314b1d8c | -15.34312 | -58.18323 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98ecf26b-0558-350d-ab75-94a5fe9966a8 | -15.34286 | -58.1637 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad2e311e-67a0-3bdf-8fc2-488b0a6031e8 | -15.34224 | -58.16744 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d5551a71-d56e-3ba4-9ca6-87b742b8bf70 | -15.34099 | -58.17497 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 800720ff-9b57-38c0-91a7-fe695418e643 | -15.34049 | -58.19897 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3e284721-7f24-327b-bdc9-4faa03f32d03 | -15.33944 | -58.16316 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 25a12f82-128c-307c-8cb1-2a7f34c270fc | -15.33909 | -58.18635 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 05525986-082a-357c-86f0-0133c034db09 | -15.33882 | -58.1669 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3c032d68-ed15-3483-9edf-c547ea232bad | -15.3354 | -58.16636 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2bb71b23-30b6-3466-a9d4-7d01838341d1 | -15.32174 | -58.16408 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b4ebac46-ffa9-3215-8108-04eef8d37212 | -15.31949 | -58.1986 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bb76dbd-c5a8-3392-a335-397ee1fa64b3 | -15.3177 | -58.16728 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28ef56a3-d38d-375b-82ab-ffd4789d92b8 | -15.31608 | -58.19797 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8fa01fb3-2c9b-3741-8334-4cb83530e216 | -15.31365 | -58.17049 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 994ac3fb-a3be-3d5f-be77-ca98efc3daf0 | -15.312 | -58.17857 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc7a2854-d761-35d0-8e90-4000d1aa8313 | -15.30858 | -58.17804 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a2279c1-f44c-35f0-a958-9a99b2bab231 | -15.30578 | -58.17371 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2045027-5a77-3205-af51-71b6caa839f8 | -15.30454 | -58.18128 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a495a49-efc4-37d1-b10a-db8267c8e417 | -15.29833 | -58.17638 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0999513-1e75-36fc-8c7e-05c9a190f9cc | -15.29771 | -58.18013 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| abad3ba6-4a07-36d1-9c0b-371d6633a3ca | -15.29367 | -58.18333 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ef3f7e0-b841-338e-b4c7-38253fcc523b | -15.29305 | -58.18709 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 344b25e1-63cb-346a-bfb3-6af692082fdc | -15.28807 | -58.1747 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b4aac2f-3a3a-3fdf-b78e-3ab197a167f1 | -15.28776 | -58.1979 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 091bdadf-f533-334f-b4e0-d5d79a95887f | -15.28466 | -58.17415 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e37e6b0-d2b4-3c4d-a5b7-6bb2e92a8b3e | -15.28124 | -58.1736 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bdf6777-c599-3e21-9540-c084d7e43ec8 | -15.27557 | -58.20788 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7bb90ca-5aaf-3b2a-a44f-c21908a17de8 | -15.35735 | -58.18203 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 42549743-e641-3d4a-a3b4-ad976980666d | -15.35122 | -58.17673 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ad3158e0-8b20-3e83-80aa-6504a96b220c | -15.34717 | -58.17997 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7af5fdd1-2c30-3a7b-aa17-cb0f7bcd85f7 | -15.34566 | -58.16798 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ce130e6-ac35-30be-951b-68854ef8c4fe | -15.34388 | -58.19964 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 017f91be-8b02-311c-ad0f-f488571054be | -15.34162 | -58.1712 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26f2155e-c722-39f7-9509-5c8ad5ba7f0e | -15.33603 | -58.16261 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4fd92f52-1e84-343b-ba75-c381594f7f59 | -15.32733 | -58.1727 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d69ed56c-51ec-3565-b995-cf0a606c39a6 | -15.3267 | -58.17645 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 737455fd-3b9f-3255-9b7b-f9d33244a24f | -15.32454 | -58.16839 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1faea39-fed4-3e93-8b87-746640932792 | -15.32391 | -58.17213 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc38ef7e-21f7-3bd3-b27a-0357400207d5 | -15.32112 | -58.16782 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9c35c07-c85a-3f5b-b3fa-c7caf807ce9f | -15.32014 | -58.19471 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a93ca94-53e1-39d3-9847-a84cf7ae0abe | -15.31707 | -58.17104 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dab2389d-da19-3153-9093-cf8df5308694 | -15.31672 | -58.19414 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d97b9e4d-bf85-3942-bdc2-f0f0251e6f78 | -15.31645 | -58.17476 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 95899d6d-0648-36cd-82d8-559252acb750 | -15.31583 | -58.1785 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7155be98-84cd-32b0-b03a-0d6086fbd008 | -15.3152 | -58.18227 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffd5ab8e-3a18-3d9c-b3d0-9582cdb6be1e | -15.31323 | -58.1711 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35b74c13-118b-36c8-a104-1962b82a7b29 | -15.31303 | -58.17423 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e20fe5e6-efef-3ac5-887d-85514078f83e | -15.31261 | -58.17483 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99a9b1b3-840b-3bf1-bfe6-e09f547cc4b1 | -15.31241 | -58.17796 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 46fa0006-dcc2-3bf0-9b10-eb34eb23a4f6 | -15.31178 | -58.18172 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c91001d-ad63-3631-9c54-bce1f386de56 | -15.30981 | -58.17053 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e8adbcf-f0e7-3040-b354-01908ea8c778 | -15.3092 | -58.17428 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b743bf2-d692-3445-b9f4-b00901a35195 | -15.30516 | -58.17749 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b292a5f8-e3fc-3f09-af8d-f1d1cbb857f9 | -15.30392 | -58.18506 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8c80a2f2-d425-3b17-bfd0-bb1f612fc052 | -15.3033 | -58.18885 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6454ad9-515e-3c52-9190-57bfcde1e5fb | -15.29243 | -58.19086 | 2024-09-26 04:59:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README134.md)
