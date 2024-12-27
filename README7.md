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
| 2c5880a5-39b5-3a6a-9394-ae49c6efc7b2 | -2.6399 | -45.94711 | 2024-12-27 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b41c840d-e609-3dd2-8be0-8b60e32244ce | -4.10262 | -45.30938 | 2024-12-27 04:31:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2f26a3d-5b8c-3ca8-a2cc-6c48a36cd4c8 | -4.05499 | -47.10839 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05804cff-639b-331b-a731-92d5066641bc | -3.60211 | -44.82832 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9e682fd-0d4c-3692-aa8e-8fdf8c2ad60f | -1.71768 | -46.2136 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4779cea2-eef9-3354-86cd-c2d1e9d9c7c6 | -3.37259 | -44.20068 | 2024-12-27 04:31:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 358a7049-eece-3057-be09-a40c871b0db3 | -1.92862 | -53.34357 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f0412a8-7740-309f-b843-c7bb67082b61 | -3.18803 | -45.98777 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e777d474-c0d6-3452-9c9e-09b2d956a2a4 | -3.88569 | -47.01513 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c725a73-be78-3b69-b16b-1421e79a3801 | -2.83119 | -46.6877 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d851f89-670b-3c18-9d84-db2b824edbee | -3.87907 | -47.0141 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c78911-8419-33a1-bdd6-7c13d43216d6 | -2.35024 | -45.41844 | 2024-12-27 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0aaa12f-503a-36a1-a141-1705b16bedf1 | -4.04427 | -47.04321 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2cecca9-bd13-37cb-b891-6d0b17c5576e | -1.49059 | -52.39289 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c581df8f-037a-3710-8468-bfb358f0bb92 | -3.93091 | -47.02915 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49db248d-24ae-36d0-ace0-49e7c9399d60 | -2.63751 | -46.09481 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 637aafab-dc68-3079-9017-ee2782ffc709 | -3.1839 | -46.12492 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 096790d5-f291-3bab-9e5d-a1cac8d59302 | -1.64912 | -45.8666 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80f971c2-f103-3956-8b96-3bebf59ea4a9 | -3.23329 | -45.96191 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 85d0c3c3-36c9-356c-b5fb-a0eb232e70f1 | -3.28198 | -46.58813 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0e99d9b3-2fcb-3602-a647-778f5633f9ac | -3.68719 | -47.17413 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8b9e8869-30a8-3cfd-aaf2-f875cbaa5114 | -1.19153 | -47.38465 | 2024-12-27 04:31:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99626e05-c8fe-3d1f-99f7-2f3838fa5313 | -4.00919 | -46.7011 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa5d8b5f-474a-39a5-8775-6f292b46e1b6 | -3.20686 | -52.44454 | 2024-12-27 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7954283c-27c9-320f-b14a-0327d88ef540 | -3.9032 | -46.98963 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3ec9480-5569-32e1-bcfd-0c22afad04a4 | -3.91278 | -46.90623 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62752013-11bb-36ef-92ec-0e235ca8fb25 | -3.19529 | -45.98523 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d8cc8bbb-8729-31e3-896d-1dc2c0c20c88 | -2.86992 | -46.72192 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5865658-0d4d-3167-81b5-c80a88db1e90 | -4.01036 | -46.71553 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6158c588-46b2-3a03-ab07-a4fc9f4031e6 | -1.08478 | -47.93406 | 2024-12-27 04:31:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 393040d1-2ca0-3325-865d-b94c7175137d | -1.44618 | -53.68459 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e31772a-e7f0-3c7e-8bda-11274afa79c7 | -2.15366 | -53.73865 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86c950d1-bab5-3df5-8793-886f7ac041b7 | -3.00248 | -48.05083 | 2024-12-27 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 51af1022-d8d3-3876-a7a3-1112fdabfbaf | -3.5016 | -45.75643 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2ca5dc1-de73-3257-9653-f4be9deb24e6 | -3.68442 | -47.17019 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 960e4308-228f-3316-b165-0003ffe1351c | -4.02567 | -47.07561 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8d8fe43-c96c-3a49-acf3-20e493042da3 | -4.04096 | -47.04269 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 963dfa3b-5b30-3730-8cfe-ce0f46fa8cd5 | -2.78562 | -46.71601 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa51421e-a385-3c5d-897e-bf518a9e2ce7 | -2.81933 | -45.9277 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 395ed1f9-ae2d-367b-9ac5-6868f509ef0f | -3.00193 | -48.05431 | 2024-12-27 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 38b02047-de54-3621-9746-408d14a2d3f8 | -3.18522 | -45.98369 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7bb6c91-ab8c-3e4c-8acf-0db0c0c00d7e | -1.64578 | -45.86609 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf6353cd-940d-3542-a3bf-9cc0c4c45ac3 | -4.03327 | -47.04856 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 907e7504-bde7-3ea5-96f2-d44c9322e02e | -3.77601 | -46.60411 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23de13eb-6bd2-3a23-a1f7-0b5d162df828 | -2.64473 | -46.09233 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ab5815-b56e-3c92-9445-1e9ea08dd18f | -2.71499 | -46.14312 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb3c93be-14da-3e81-ac04-4ebb46ec27d9 | -2.80567 | -47.59206 | 2024-12-27 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2f7c1eb-bed9-356e-9958-63c17fd608e6 | -3.87879 | -46.95048 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab9ce01d-c48b-33c5-b8b2-c52feeb89408 | -3.16645 | -46.25919 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 705e243b-d95d-3f5e-9cff-996a4ba0a739 | -3.07095 | -47.76781 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c73814a9-ee7a-3c97-ac50-a04560188731 | -1.83002 | -45.71073 | 2024-12-27 04:31:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a285352-9511-34af-914b-e0abf1681310 | -2.66975 | -46.08535 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf864a6c-9f82-3ca3-8dd4-22bd007d2a17 | -2.69561 | -46.61731 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c77db8c-9f0f-3902-84ce-6e7868bbbb9d | -3.1867 | -46.12897 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eef77e2c-5862-3110-9efc-4a89bee11b3d | -2.76597 | -46.07898 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae45097-6a8a-3f21-9297-dce9e2d9eb63 | -4.05169 | -47.10789 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b16b737-b36a-3182-9758-084a72e49375 | -4.04865 | -47.03681 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5c147d1-1ae4-38d9-8df0-62cd9885f700 | -3.19809 | -45.98931 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 47dfa1b7-3bd8-3c17-aa12-7528771f562e | -3.06723 | -47.76664 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf10c315-2219-38f5-8f96-e070e7fcbd78 | -3.07356 | -41.90082 | 2024-12-27 04:31:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 050c02db-ce6e-3689-8b90-0388803e8d86 | -3.19249 | -45.98116 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be03ea8-1e1b-3674-9c40-fbf10f0761af | -4.52578 | -42.0682 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87310a1a-630f-3a7b-a5bb-9a21a39956b4 | -3.10102 | -46.57043 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53051e31-5ccf-384d-a74d-dca21ea49586 | -4.05222 | -47.10444 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b15706-1881-3f2f-be86-9ec643196a59 | -3.89784 | -47.02406 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4ac5e37-d5c3-3264-a8f9-c762107f208b | -2.28638 | -45.57565 | 2024-12-27 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22d25a1e-f76a-310b-a489-b7f50044b171 | -3.9876 | -46.68709 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 404f3ff0-d394-3ce9-b724-debf205c1429 | -3.91063 | -46.92006 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1705f875-59b4-3cd2-869d-c3fdcf51a2a5 | -3.97673 | -46.58194 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d89c16b-7388-340b-91e0-45010fcfc020 | -2.63588 | -46.10534 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a1b1ce5-1aba-322f-a034-0df1384cb008 | -3.94066 | -46.98831 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf351343-afac-37eb-9c98-311d14480a43 | -3.19754 | -45.99287 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 54e2d287-86a4-37da-8b31-306fecb0a828 | -3.93512 | -46.98039 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ac620c-9391-34e0-888c-10c37b92dd78 | -3.92797 | -46.98282 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2daa8a88-1e9b-387b-8b59-93a49d6a7db0 | -3.89936 | -46.99257 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c700811-73e4-334b-875a-99dcb15fff2d | -3.73574 | -47.34356 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fd81b3f-971e-34c5-8859-586687ad3b95 | -3.23609 | -45.966 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c1ac4b4-f55a-3201-85ff-ca1033e0624a | -2.76213 | -46.10359 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 074cf78c-68c7-37ac-b411-35231dc5adda | -3.88515 | -47.01857 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 294d7572-8e9f-3562-9eba-8302adabd805 | -3.92743 | -46.98626 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e8319d7-fb74-3fff-a22a-e2b0f0ced94d | -2.77705 | -47.144 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1de61c13-6372-3d72-bbe8-c0c7bc5c663d | -1.72216 | -46.22849 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd7385f-43d2-3c41-9223-b208ff21e1b0 | -4.04919 | -47.03337 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cac3036e-3483-30bb-831f-1acc8f80cf96 | -3.90374 | -46.98618 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c19ccf-efe3-3f94-9dab-2173e658ccab | -4.05303 | -47.03042 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef6e4e82-acd2-3815-9a6e-19023df24de5 | -3.93736 | -46.98779 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a846fce-6b33-397d-bd9d-142ea7520cae | -3.35246 | -44.87504 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed85a251-44a7-3c30-bc8e-25f0f66d3fd1 | -1.6419 | -45.86909 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 172ae361-673a-376e-bc3a-3f874cd0b37b | -3.87192 | -47.01652 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4a26e05-9445-3dd3-9194-5a7f5c18a5bb | -3.18858 | -45.98421 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e27d9d5-3d58-3104-8b43-44b20c66c67c | -2.82214 | -45.93177 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6ca384e-acac-3ffa-bece-0e62c8365abc | -2.3842 | -44.4074 | 2024-12-27 04:31:00 | NOAA-21 | ALCÂNTARA | MARANHÃO | Brasil | 2100204 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d015bbb-7027-362a-a327-63c405969aa9 | -4.3008 | -42.3245 | 2024-12-27 04:31:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 33898cef-afa1-3adf-995d-e7c218ec80b7 | -3.98814 | -46.68359 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 613edcb2-56cb-3960-a259-27ae0c94fcec | -3.00139 | -48.05779 | 2024-12-27 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 94788c99-ac2f-3b9c-a06e-57719d45777d | -1.55648 | -53.49796 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13a89cc5-f7c8-3dbb-b86b-d784dc83f9f7 | -4.03988 | -47.04958 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5f68220-a4c3-3075-a70f-afe8a29af0a8 | -4.16615 | -42.03327 | 2024-12-27 04:31:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bd6c5b16-0bd6-3ffc-81f2-4a1c712b2aa1 | -3.03467 | -40.11457 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0ee4aa04-4ad1-3c5e-8260-f10989efeaec | -2.71553 | -46.13962 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
