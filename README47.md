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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d33db73-8f8b-31b8-a0de-31e13de982fa | -2.81353 | -54.05378 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3f12582-b150-35fc-b654-1dbf2c81923b | -3.04436 | -51.26991 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b2fb7cf-c828-3754-a6cf-790aebbd0620 | -3.09626 | -54.05343 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 231bc98a-5659-3c52-a4f0-476ab885bbe1 | -1.66599 | -52.75549 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0aec644e-d9d1-3507-999a-d59e7f4b46a1 | -2.80841 | -55.3113 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e08ee1db-20d7-3dd8-bb3f-81952c266ef9 | -3.2837 | -53.24974 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73934473-7d07-3c96-b69a-58694fb8be14 | -3.34642 | -49.76833 | 2024-12-04 05:03:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a5604ac-322a-37a3-8c88-16ead94cacee | -2.9867 | -53.88049 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1c88e6e3-9658-32f4-bd6a-5a0ee86cc8b9 | -3.08655 | -53.75962 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66af3ee0-6946-363f-9d92-089bcd4863f5 | -3.10576 | -54.05854 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fb55d53f-12eb-3ad5-8efd-a52b02a3a056 | -2.46137 | -53.71635 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31e4b62c-7acf-3bd5-b2e5-28398faf3ffe | -2.003 | -54.10804 | 2024-12-04 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e9ef94e-373c-3c46-b072-2294ab95b16a | -1.65541 | -52.38448 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 10a4618b-55c1-35d3-88eb-74394088e1ee | -2.97283 | -46.95093 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80fc8309-8390-3d65-bb54-235bd116eca9 | -2.77546 | -55.32731 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a91ebca9-c5fd-3b41-98de-0b10b87e2e7e | -1.40588 | -54.99314 | 2024-12-04 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60aba213-2790-34af-a3bc-5412f960cba7 | -3.39136 | -50.31476 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd4e6615-b6e3-3671-a423-7ed12f2ed606 | -3.55607 | -52.91219 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba2d582-1f31-3c55-ab14-f789753ee4be | -3.03263 | -53.87292 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7fbbda9-b000-3b28-b2e8-f79534734858 | -3.2018 | -54.27199 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8644fa40-91b9-3f55-a812-2b56d9fd1516 | -1.91526 | -52.86545 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ed5dcac-d1a1-312a-a0e2-4746c78d4588 | -4.3822 | -43.37081 | 2024-12-04 05:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5aebf4f8-2b38-34a0-b50d-13c5c2351035 | -2.82365 | -53.05079 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f8c52819-90cb-3542-91a1-ae8af1e2bddb | -4.748 | -45.69777 | 2024-12-04 05:03:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d70474c-49d2-393b-a4a4-7cdcfe57afc1 | -3.81264 | -46.94899 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9853e331-1104-33cd-8df4-b85b96beaae7 | -2.75106 | -54.17393 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 536c75a0-f623-344b-a9bb-547c312e2401 | -2.97709 | -54.44804 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a9e7a3f-74c2-3370-97b2-63bd6fd293b1 | -3.22107 | -53.63621 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ebb3168-eae5-366c-893d-d1d741598973 | -3.08693 | -54.11351 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4f760e2-f980-32fd-a997-dff442445141 | -3.19391 | -51.17716 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b8efa16-8a88-3048-83c7-1fbbd45dd2fd | -1.75895 | -52.6288 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e8df7d74-ab99-3d97-a79b-58991c59993b | -3.12184 | -53.99929 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4de59381-d16f-3cdc-a5a5-d1b849bf912b | -2.36091 | -53.79544 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ccd3005-873e-3996-86ad-49af30f612bf | -2.79555 | -53.00394 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d894445-2379-32c2-95a5-66bf923cd81b | -1.65225 | -53.8242 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2a762b8-940e-3891-be81-1f170fa880e5 | 1.13121 | -60.51812 | 2024-12-04 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 86b84a1d-5dbf-343b-89c6-8571a460a0e5 | -3.27012 | -53.42996 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d1a9d08-0a1e-3f07-8009-004273aa7012 | -3.58883 | -53.04724 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 95535ae9-cde6-3ac3-9924-636324782e8c | -3.53667 | -50.17564 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48c80323-694b-3dfb-a511-dc3f957fabbb | -3.89329 | -50.0742 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2548f59-0e6c-3f5d-a33e-7a5117594618 | -4.27425 | -46.5768 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33ea5e03-1aaf-3c65-bb4f-61f1d4341ffb | -3.54954 | -51.3354 | 2024-12-04 05:03:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 50d3fc4d-bcb1-30cf-bc79-dd4144df488b | -2.36665 | -53.86898 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6077cf10-e021-34e9-b75e-e65695389569 | -3.2468 | -53.87283 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab197675-0a38-324f-a289-f64ae6f46b93 | -2.83356 | -46.75703 | 2024-12-04 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 45e9714b-17a4-31cc-b9be-a02d848a062a | -3.34368 | -51.20888 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea01e9ff-09ee-3d37-9776-12efa4a89da8 | -3.92793 | -52.4005 | 2024-12-04 05:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a77b8995-50fe-360f-9779-6a820f3ca6b2 | -2.99283 | -54.10655 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5c559d5c-8b9f-3872-b511-616d6cc6110e | -1.81161 | -46.31013 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c61256e-d4ef-340a-9fb8-8bf89a82ea59 | -4.12016 | -46.90645 | 2024-12-04 05:03:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27b9a745-058c-38ee-977b-f2c1ca3dcc26 | -3.0758 | -54.11905 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4665121a-32a1-349e-8fb7-98db03a8bd06 | -2.82593 | -53.05885 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 8a883cb0-206e-35ae-99bc-538ff407e0d1 | -3.02521 | -53.4269 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370c09a8-04f1-3643-a3ec-8b1894849537 | -2.69245 | -54.24379 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e304c0c-8b7c-35f3-84e9-f2a84559d98a | -1.74559 | -52.64631 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 797a61e1-2636-3c76-acba-6ecf74537966 | -2.86547 | -54.09426 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 385a973e-c370-385e-b29f-1f5b2673a1c2 | -2.20433 | -53.77142 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4b09e1b4-6d7a-3c4d-92ac-d507eb7c7987 | -2.828 | -54.04877 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e86536a4-5ead-387c-a181-b947d2059f4e | -2.458 | -53.71582 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c77ac5f-38fb-3adf-a0ff-150c20953946 | -3.10512 | -54.0185 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f34aeebb-e359-3b8a-8ca2-2c2434a1614c | -3.12073 | -54.00638 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c292ad09-4225-3d49-a6d5-e8b0ddaa3c5d | -3.15475 | -50.33973 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d0e4f11-caef-3181-b1a9-5a5dfe5e380c | -3.27625 | -53.25243 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5097b752-1dbd-3163-8504-4375338b6a94 | -2.60469 | -54.39386 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f061283b-5ddd-33a4-bcb7-89d12787415c | -1.44657 | -60.07822 | 2024-12-04 05:03:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddaf9667-509d-35ce-aa93-0d6f3d0600cb | -2.4426 | -54.0147 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bea6473e-a053-3b15-9d6d-c542304360e0 | -1.7206 | -52.76303 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60025ca7-7220-341f-8f4d-6f37191600db | -1.88176 | -53.31053 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a882ff07-7992-3cfb-9c5d-6f3b53fca940 | -3.19427 | -50.64521 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1e3e320-c316-3d45-80bc-cad54848cb82 | -1.60067 | -52.49951 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee84175a-2e6c-3db8-9e2b-f0da51df3381 | -1.76184 | -52.63316 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| cf0a5ef8-d929-385f-b2fd-e3a90e83a9f1 | -3.26061 | -53.62747 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0a360d1-90d2-39d2-800a-7080577f370b | -3.32555 | -46.60561 | 2024-12-04 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 037e0e7e-3c13-37ad-bc92-7f5a8326eb5c | -2.64421 | -54.29313 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36868b4b-d4c5-3b55-862b-aa6a25df7018 | -2.80869 | -53.0562 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad0c44b-9fac-364d-9a4d-d10d77701207 | -3.1118 | -50.20407 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26d6a237-6064-3118-a800-62591c7886c4 | -3.12349 | -53.98865 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 78eb58b9-a11a-3187-b64a-b0e1f0a43ecb | -1.62531 | -52.3642 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f308502-2d08-3627-abf8-693b91960df8 | -2.84418 | -54.05487 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8f8464b0-8e76-35c4-9d0b-5fb4ceb0545a | -2.61712 | -51.81949 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ac52993-3f0b-34c9-af45-81aac9afc3c7 | -2.85698 | -54.82635 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cd77de64-9ea9-3350-a67f-6333494050a9 | -3.27135 | -53.62537 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c19b7f79-1659-30a5-bd6c-d434d4bc2129 | -3.10093 | -53.23007 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 430a48db-1f7f-34c2-af27-791506d345ba | -2.61836 | -54.34977 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a07f418-e72b-3ffb-8b5b-ae1ed43dc76b | -2.81073 | -54.04974 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 213715f7-62c0-35f3-946e-88755b2abde1 | -2.43823 | -54.04282 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84e9161f-04fb-368c-a68b-50a6fc4f83c4 | -2.88897 | -51.35128 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cea044d6-04e2-3219-bed6-b4116f5d46b5 | -2.78471 | -52.86602 | 2024-12-04 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 620a51f1-c919-330e-9ea2-e9250f5056b3 | -2.87363 | -54.01962 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bb40b15-1fa5-31ae-888a-1c5d58c2b52c | -2.81447 | -53.04166 | 2024-12-04 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 28502b53-aa1e-37a8-9014-990963f9c7d6 | -3.25631 | -53.83383 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c42609d-5603-36ed-a716-de3dc247ebf7 | -2.02598 | -46.33924 | 2024-12-04 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5e1958-a4b4-383e-acea-980549672a6a | -3.10737 | -54.0261 | 2024-12-04 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f630134-3625-3c42-b499-b9ff1fe93d69 | -1.68427 | -52.7969 | 2024-12-04 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e256e85c-f1a4-35ac-a3e2-f29e03c4f940 | -3.32169 | -50.22132 | 2024-12-04 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f352404b-ce23-3a3b-9ca2-0b1aa897e4d6 | -3.05698 | -54.50309 | 2024-12-04 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb27ff40-f6c6-37a2-a8a8-ee6b6b1825dc | -1.61678 | -53.83688 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b3dd9c5-4bc8-3796-ae8f-2dae8a6ed5d4 | -3.06892 | -54.05285 | 2024-12-04 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b23f148d-f9f4-330c-9b3f-3acfd2cf1602 | -3.36614 | -50.39041 | 2024-12-04 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb7c2e41-06bc-34bb-9094-277d94148b13 | -2.41746 | -54.1545 | 2024-12-04 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README48.md)
