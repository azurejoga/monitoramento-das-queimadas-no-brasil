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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c9d6e38-5205-3518-8aaf-1f31c7b55ab4 | -9.362 | -61.5324 | 2025-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 3d0e9d4f-0a25-3602-9dbc-f38b4108bb28 | -8.9401 | -60.7288 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 42244ef5-b55f-3e21-8106-63d9c55977cf | -6.548 | -42.7547 | 2025-08-10 03:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| b57fecbd-ad01-3047-b626-1c7328ee2b7c | -6.5477 | -42.7783 | 2025-08-10 03:50:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 58.4 |
| f7b1edd9-bb52-30d9-bbe0-44344b5638a0 | -8.9399 | -60.7481 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 0a3dae7c-5273-3282-93e8-c45cf9a0222a | -9.3808 | -61.5124 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0f472269-aefd-3e54-a242-011307affaca | -9.3806 | -61.5315 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 8fd6fd4a-1013-3c32-ade1-562d37a41510 | -8.9213 | -60.7489 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 5fa51550-efd1-3b51-a100-19047e9de269 | -9.3622 | -61.5133 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 648192a0-2643-3f45-980e-a8ee0c09a6fb | -7.0615 | -59.1779 | 2025-08-10 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 76095e53-c69f-3f47-a90a-fa87566767a7 | -7.08 | -59.1771 | 2025-08-10 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1b7440c5-03c7-37f2-bfd9-ca6bdf2e2ae5 | -9.362 | -61.5324 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 140.7 |
| e0d51a41-e23a-3a4b-8972-e1a5f2a69561 | -8.9215 | -60.7297 | 2025-08-10 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| a47ad630-8ee8-3272-97d3-3d51e8553bd1 | -7.0614 | -59.1972 | 2025-08-10 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9a1ab851-f85b-3d41-8798-8cdd125e534a | -7.0799 | -59.1964 | 2025-08-10 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 341b8560-af31-3fbf-8ede-5ba4ae83db96 | -5.392 | -41.32769 | 2025-08-10 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77e2c655-1deb-33ec-8e08-18afbce03214 | -4.91519 | -37.41355 | 2025-08-10 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 07bc9673-1531-333d-bc88-685e34d40aa9 | -2.81513 | -41.88296 | 2025-08-10 03:53:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 862ea6f8-26ae-3f56-8882-95499e53ebfe | -5.34895 | -36.13695 | 2025-08-10 03:53:00 | NOAA-21 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 28251b3a-6c6c-39b9-97b7-ae20a960f974 | -3.27806 | -48.81519 | 2025-08-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ec299882-160c-3972-a2f7-e9e00d44704f | -3.23197 | -46.79226 | 2025-08-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88c63dd8-69de-3f09-89f5-7b57b76341ec | -3.9688 | -47.88109 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b2349b5a-2233-3f7f-b4ff-83726f29d252 | -5.69191 | -39.23114 | 2025-08-10 03:53:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df387122-ba1b-3782-ab91-de4851cdfd8f | -3.58606 | -47.52464 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3da7f133-f90e-3065-be70-d8b8fcfd2af5 | -5.43348 | -41.23025 | 2025-08-10 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8117c5b6-51be-3cbd-9916-2bdc911bd119 | -4.29719 | -48.0744 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d14716b1-82e8-3acd-8ead-41ef3ed7cd01 | -4.34838 | -47.53738 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e8cd4cad-16d3-3b26-992f-40ab01719944 | -5.3848 | -41.32675 | 2025-08-10 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 356cf66f-629c-3dd3-aa6b-e4824f71cbcb | -3.23671 | -46.79635 | 2025-08-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb6b83c-0e54-35cb-a9f6-03beca5164bf | -4.14655 | -46.452 | 2025-08-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccb46654-2cae-3755-9815-b77138dba1d5 | -4.10931 | -38.17492 | 2025-08-10 03:53:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e3935549-0a8b-3398-9281-54ee88f53682 | -3.11529 | -48.96389 | 2025-08-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 511e82c4-58dd-36ae-a523-57398d019d91 | -3.42868 | -49.0489 | 2025-08-10 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc9b4831-a364-3ba5-8f64-a38a54040e06 | -3.58608 | -47.52477 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ef2f1c9-1bc8-3d6a-ac5f-fe91ca40007f | -2.44123 | -47.32644 | 2025-08-10 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d3f9e13-5e5f-3215-95cc-7add52a94595 | -3.58671 | -47.52114 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 919d26ae-6304-3a1e-8cc5-4c1734064c27 | -3.22743 | -49.34535 | 2025-08-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6e593d9-0028-3361-a188-6f0f4315380c | -2.44064 | -47.3301 | 2025-08-10 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aa2001d-e04d-3b7a-aa41-4386b38d2f17 | -3.2788 | -48.8107 | 2025-08-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b173d888-a450-3bd3-9d43-786a44292fcf | -3.23143 | -46.79551 | 2025-08-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39b4b0c0-bb9c-3506-a158-0c3708cd81d7 | -3.23724 | -46.79313 | 2025-08-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cca44c8f-6ac4-38e4-b00b-7cbec6cf6971 | -3.58666 | -47.52101 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7878962-b323-3ccf-a9ec-4d75339c68dd | -4.11262 | -38.17543 | 2025-08-10 03:53:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b78df896-48ff-34de-8de3-b5f705b8ef83 | -3.19255 | -41.85472 | 2025-08-10 03:53:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e8f61b2-67c0-3f51-948b-07cf7473cc08 | -4.29784 | -48.07062 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7b72164c-ab9d-3024-a8e6-5d0b0b3c8fde | -3.62585 | -47.52382 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f057ea-084e-3b68-873b-d2675007d9a4 | -5.43084 | -41.24658 | 2025-08-10 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2bde56a-ef07-3c05-b178-91f871f233f6 | -3.11561 | -48.96658 | 2025-08-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ec08c5d-0bbc-3ccf-b4b4-d5b160896dfd | -5.19602 | -39.33296 | 2025-08-10 03:53:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 87a3992e-faed-3599-88ee-ac9e48f19927 | -3.31032 | -42.53117 | 2025-08-10 03:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd05fb56-d26e-3903-9538-224e283d2e43 | -4.14608 | -46.45478 | 2025-08-10 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f3d438-6af5-3769-bbf5-48705e41d6f3 | -3.9625 | -47.88432 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0952c54-7534-3cc2-9f24-af34113ef161 | -3.42946 | -49.04425 | 2025-08-10 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a1928bf4-3f62-332a-a9dc-6da749b1da37 | -5.34952 | -36.13318 | 2025-08-10 03:53:00 | NOAA-21 | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e9b2a36c-e960-3cc3-af3a-c1fe860143f4 | -4.11315 | -38.17199 | 2025-08-10 03:53:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f7a78aec-c3c1-355f-9b2d-40fe67cea64c | -3.65116 | -48.3233 | 2025-08-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6daa9b38-0ab4-3ff0-bd71-0244be5f50ac | -3.22824 | -49.34056 | 2025-08-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b50cb768-bc51-3a63-a798-1531ba46195a | -4.31764 | -38.12636 | 2025-08-10 03:53:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c6c9f862-a028-328a-b6d3-f82f8205b370 | -3.62521 | -47.52761 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4464e97f-933a-3635-8911-2f8071b1e12e | -4.34981 | -47.53767 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4b788fb5-69d1-36d8-8930-ab6a7a6a9529 | -4.30284 | -48.07532 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef5fa887-65f8-369a-898e-461e33539b72 | -2.44028 | -47.3299 | 2025-08-10 03:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8554c99c-025c-342d-b95f-b97ca29ea9ca | -4.34918 | -47.54131 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c55f773c-95fe-3a1b-b8c8-3a135b9c9bc5 | -3.28096 | -48.81129 | 2025-08-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa946215-9353-3cb0-890f-31191c7e0b1f | -3.18876 | -41.85414 | 2025-08-10 03:53:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ed07ad5-e0b6-3e6a-b49e-5444e3d53122 | -3.28019 | -48.81576 | 2025-08-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1ad8aee-83b3-3a76-97c1-5db941837c62 | -3.62035 | -47.52289 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa3d3b37-c91b-3da9-96f6-30c0a81b124f | -3.59155 | -47.52562 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91e44c0a-7827-327c-9e60-34d8fb9e81ac | -4.05986 | -46.93541 | 2025-08-10 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cc8f7669-d3ae-38f6-8c80-1d45371ce6be | -3.75778 | -41.03183 | 2025-08-10 03:53:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9877e617-54a5-3ccc-8571-e29c803602bb | -3.59158 | -47.52573 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff831443-e12d-360f-98f8-a1c2bb0b2aa8 | -3.96624 | -47.8847 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f6a85034-4518-379c-964e-72900661308e | -4.17276 | -42.44493 | 2025-08-10 03:53:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cffb3dde-08a7-3124-910e-2256244003e6 | -4.29234 | -48.27414 | 2025-08-10 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d18d495a-bd5c-3eef-aeee-ff2c9b13f424 | -3.27495 | -48.81028 | 2025-08-10 03:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9a488e7-640f-3117-9d0d-011e780a6051 | -4.34778 | -47.54103 | 2025-08-10 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c6ef494-a79b-3d67-bb3a-8a830651b0a0 | -3.42988 | -49.04684 | 2025-08-10 03:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f0caff9-7fcf-3d39-b70a-1696903643e0 | -4.30218 | -48.07914 | 2025-08-10 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e60407a-60ed-338d-a631-f03e3503ec42 | -3.96691 | -47.88087 | 2025-08-10 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 351804ff-2b7c-3ec6-8018-c265e6368780 | -3.65106 | -48.32444 | 2025-08-10 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abca43c2-2a83-3a10-a390-339c007d91f6 | -3.11452 | -48.96853 | 2025-08-10 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a7938e0-77ff-356b-9398-dbd19ff6a76a | -8.88265 | -44.78879 | 2025-08-10 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4a6de861-895c-3dad-a26b-9fbf62dc0002 | -7.87298 | -45.55445 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 03a51e4b-1a30-3fd2-8b5e-bf055dbe211e | -7.87374 | -45.55006 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02aac48e-b403-3695-ac6d-1bc68f5427c5 | -6.19665 | -46.10415 | 2025-08-10 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eaa45727-fef6-3fb9-bf10-320a380c664d | -11.77951 | -44.94813 | 2025-08-10 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3127d9a-da9a-350e-b3ca-83786d686485 | -6.94966 | -44.55368 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7e8da121-23af-3637-8f3e-61aa55747574 | -6.94833 | -44.56155 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e4a35bcf-52ac-38da-bc4d-d356d55caf51 | -9.5198 | -45.42735 | 2025-08-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 25fb07e2-40f2-3883-93ca-c7e7014e2546 | -6.95393 | -44.55433 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f7ed4fec-e979-3b93-a68f-9968aea37fbb | -12.5302 | -45.6772 | 2025-08-10 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ca45137-11e4-3309-857f-9bde2f95204e | -12.23284 | -40.56834 | 2025-08-10 03:55:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aed700bf-b27d-31e0-b7be-18ed517137a8 | -7.42979 | -43.98875 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3507aa54-8866-33e4-8c5f-6b1e18150600 | -7.16118 | -44.07107 | 2025-08-10 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2dd6fac-ac13-3689-b957-6f60f082bfde | -11.93321 | -44.8093 | 2025-08-10 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 098d74d3-5a6c-38a3-8093-2f189407ea66 | -5.40928 | -44.42773 | 2025-08-10 03:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d6bcf9f-da80-3129-8666-e2f1feac6668 | -7.22064 | -35.7715 | 2025-08-10 03:55:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2bfe1460-715a-34c4-be2c-56ff512d059f | -6.54973 | -42.77362 | 2025-08-10 03:55:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| d1d31a86-3d95-3aaa-9577-1a6ccab87183 | -7.41256 | -43.99251 | 2025-08-10 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2809a2b3-dc5e-3937-b958-7815ee14da77 | -6.52846 | -47.43146 | 2025-08-10 03:55:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README8.md)
