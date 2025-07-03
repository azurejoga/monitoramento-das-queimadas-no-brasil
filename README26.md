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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 691a7170-ca6b-3b47-a6d3-56d20695961d | -14.2453 | -43.6658 | 2025-07-03 13:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 68be48c5-d41d-3e46-87ad-a11e7db048c3 | -6.2757 | -43.6675 | 2025-07-03 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 265.2 |
| f78a8bc3-adf3-3318-b805-6838f6a6a3b4 | -11.4793 | -47.2858 | 2025-07-03 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| dc9711a9-bf72-3497-b20d-0c46f73bd6b4 | -6.2943 | -43.6891 | 2025-07-03 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| f59238f0-9376-36ca-89de-cd04e1e299b5 | -6.2755 | -43.6907 | 2025-07-03 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 247.7 |
| 6f1b621b-4ad3-381a-b5cb-d4156ea2cb0c | -6.694 | -43.1648 | 2025-07-03 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 130.6 |
| a4a8baff-f65e-3883-a728-fe8c136f972c | -7.1925 | -44.0038 | 2025-07-03 14:00:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 147.3 |
| cf20712e-c432-30a9-a9ed-ccb8457a117c | -10.6483 | -44.4861 | 2025-07-03 14:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 83bbd78a-292e-3585-8a90-fd91259786d0 | -6.2757 | -43.6675 | 2025-07-03 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 281.3 |
| a4299978-2008-3a07-ab9a-943c507b47da | -12.6636 | -45.2776 | 2025-07-03 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| e8610dcd-838c-3214-91dd-861ac4881315 | -6.6938 | -43.1882 | 2025-07-03 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 522825fb-1d13-3625-ad4d-ff1fd82d941f | -11.5464 | -47.8551 | 2025-07-03 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 106.6 |
| a510b7c6-166f-3dfc-8f60-e2e64266bd64 | -11.4793 | -47.2858 | 2025-07-03 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f540fbf3-1279-3499-8b61-2a7cdcb64777 | -6.2943 | -43.6891 | 2025-07-03 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 66f646c7-4bb4-3be3-b2fa-fea336cb2e45 | -6.2945 | -43.6659 | 2025-07-03 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 8a017883-c753-3166-a9b6-c3cd674881c1 | -11.546 | -47.8772 | 2025-07-03 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 240.5 |
| d6099335-a5e3-36b2-bd43-9b7aed06f5a1 | -6.675 | -43.1899 | 2025-07-03 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 246.6 |
| 0f49fc94-3da0-3689-960b-c70271b03b18 | -4.0148 | -43.2408 | 2025-07-03 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c004e0ec-e9af-304a-b845-53b6ac7006ec | -14.2453 | -43.6658 | 2025-07-03 14:00:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 9350bc24-8e9d-3422-b832-81fd825eb7f3 | -6.2755 | -43.6907 | 2025-07-03 14:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 212.4 |
| f1c98954-9a50-32ba-b759-03b8ffc7dada | -6.694 | -43.1648 | 2025-07-03 14:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 78dfe4d9-650f-30a4-836c-0879c6b23b15 | -11.4602 | -47.2883 | 2025-07-03 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4bb73424-b8d5-38ee-b4b1-0c989e2a5536 | -12.6632 | -45.3008 | 2025-07-03 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| eb33c82d-b7e1-3889-ae22-daf628630ce3 | -7.1927 | -43.9806 | 2025-07-03 14:00:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| a9abdad5-47b4-3543-b21f-c68511f3b7e5 | -6.675 | -43.1899 | 2025-07-03 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 224.5 |
| 678c0077-eb7d-38b7-84c2-6726dfea05ce | -12.6636 | -45.2776 | 2025-07-03 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 45dc3c7c-8072-3c22-af5d-04b323f54441 | -4.0148 | -43.2408 | 2025-07-03 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| bce18736-f582-3802-bd09-62e7488cb304 | -6.694 | -43.1648 | 2025-07-03 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 152.2 |
| 1d807d10-b9c4-336f-bd63-842a23eeacbb | -11.4602 | -47.2883 | 2025-07-03 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f99b54db-6082-3506-9c0d-8e2a2eeec170 | -12.6632 | -45.3008 | 2025-07-03 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2fc9f9eb-1ef7-371e-99b9-e1d3b953414a | -11.546 | -47.8772 | 2025-07-03 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 83ab2ab4-61a6-30c9-b3af-a0f432a7d0ed | -10.6483 | -44.4861 | 2025-07-03 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| bc1c0d41-fe5c-3adb-a43e-778b717a98f3 | -6.2757 | -43.6675 | 2025-07-03 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 95a81441-5e94-3fab-8a62-486da6d6897b | -11.5464 | -47.8551 | 2025-07-03 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 99b6f75e-3498-3c03-81aa-c46ff49d050f | -11.4793 | -47.2858 | 2025-07-03 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ce5bf707-5c09-3981-9786-7bb75b286652 | -7.1925 | -44.0038 | 2025-07-03 14:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 9b779574-b36e-3ca8-a79f-5ee6eabd186e | -6.2755 | -43.6907 | 2025-07-03 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 264.9 |
| 7f6aa14e-2041-3a1e-94e2-725c5f8bde05 | -7.1927 | -43.9806 | 2025-07-03 14:10:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 931455a5-5a7b-30ff-b845-3b0aa33d58a6 | -6.2943 | -43.6891 | 2025-07-03 14:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 266.5 |
| 7c69a3c6-3438-3d46-b140-0018988ef27e | -6.6938 | -43.1882 | 2025-07-03 14:10:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 120.8 |
| e3807b21-0433-3d7a-a7f2-942e967c3d9b | -14.2453 | -43.6658 | 2025-07-03 14:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 51981a17-e80a-3165-82fc-e2a850f0db76 | -11.4793 | -47.2858 | 2025-07-03 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c81e43de-4ec4-32a6-a0c0-26392cce7ca5 | -6.675 | -43.1899 | 2025-07-03 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 278.7 |
| 7c738948-ea80-3d43-ab5f-3fc6ed8d1424 | -6.6938 | -43.1882 | 2025-07-03 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 161.5 |
| 5cbf8ce4-1f7a-3d18-a34e-2863f95a9c21 | -7.1925 | -44.0038 | 2025-07-03 14:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 017e3ff5-fd59-33f3-a018-44c918a2b641 | -11.2868 | -46.2326 | 2025-07-03 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e4d43fd9-d174-320b-ac50-45e3bf322315 | -6.2757 | -43.6675 | 2025-07-03 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 305.4 |
| eef9e72e-8138-3c4e-9d8f-847600bdcf7c | -12.6632 | -45.3008 | 2025-07-03 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 8590f7c8-e7e6-3139-b0d0-aee70e3bea79 | -6.2755 | -43.6907 | 2025-07-03 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 315.5 |
| a3231313-5c28-3932-b8d4-6fb80fd989c8 | -7.1927 | -43.9806 | 2025-07-03 14:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 137.0 |
| df1ef73c-f64a-310e-8ae4-2af973f7d2c3 | -12.6636 | -45.2776 | 2025-07-03 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 92cbb657-9616-3117-b9ac-6609b38bb600 | -11.5464 | -47.8551 | 2025-07-03 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 19e7adb8-1361-30aa-b44e-9ac208cd2255 | -6.7314 | -43.1848 | 2025-07-03 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 82.1 |
| 25f5675b-3e51-361d-8c70-b0fdd1da5c43 | -6.2943 | -43.6891 | 2025-07-03 14:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 266.3 |
| e4a06c58-958d-3cfe-a9a8-507a390eaaa9 | -11.4602 | -47.2883 | 2025-07-03 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 99a53109-9eee-3373-a0e4-f01018e7f25c | -10.6483 | -44.4861 | 2025-07-03 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2fdbfd8c-f4d6-3397-bfdc-2a13fd9e199d | -6.8193 | -45.5446 | 2025-07-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 859f9523-3c08-3c27-9fbe-7543b5c10778 | -6.8196 | -45.522 | 2025-07-03 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 6a0b27cc-a7b9-3e6e-8b7d-66aa524004d0 | -11.546 | -47.8772 | 2025-07-03 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 279.6 |
| fc5812d8-ecc5-3aef-8f1c-2477e49b7631 | -6.694 | -43.1648 | 2025-07-03 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 189.0 |
| 8209d517-ef42-3de7-b24e-89ae7537a8e1 | -14.2453 | -43.6658 | 2025-07-03 14:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 7856187a-e9eb-32b0-a430-13321ea51aae | -4.0148 | -43.2408 | 2025-07-03 14:20:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 05c6f57f-03a0-31ce-8adb-73334f0e7b7e | -6.2943 | -43.6891 | 2025-07-03 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 322.9 |
| 6934bf96-2e3b-34bb-a523-53806334044d | -11.2868 | -46.2326 | 2025-07-03 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| aba860bc-89f5-303b-be58-64735b53c0ae | -6.2757 | -43.6675 | 2025-07-03 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 296.4 |
| 8e8d3be0-7c2b-3269-a5ec-aa55a84b7edc | -14.2453 | -43.6658 | 2025-07-03 14:30:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 17c8abea-5873-3de2-8e49-2376941bcc7b | -12.6636 | -45.2776 | 2025-07-03 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 5f0f2368-f177-3c94-9178-d5559f5e871d | -4.0148 | -43.2408 | 2025-07-03 14:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 0ba68ec8-3666-3a08-a11d-a5fe6292ea41 | -11.5464 | -47.8551 | 2025-07-03 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| db8bcb39-0d24-3a17-a614-1653795f8a36 | -7.1925 | -44.0038 | 2025-07-03 14:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 86c9f67e-dc21-3943-9b32-e65c4d1fef68 | -12.6632 | -45.3008 | 2025-07-03 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ab5014d2-ca86-312b-b78f-60813e49c572 | -6.675 | -43.1899 | 2025-07-03 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 229.6 |
| c3987de6-f634-37c9-87da-032d9dc9766f | -6.6938 | -43.1882 | 2025-07-03 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 70c2ad58-12fa-3130-841d-e9af724f6502 | -11.4793 | -47.2858 | 2025-07-03 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| fcd426c7-e80c-32d4-a9c5-0b3515ad9c4c | -7.1815 | -43.3067 | 2025-07-03 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| a2017f58-28c0-32cb-a714-e6836c26b92e | -11.4602 | -47.2883 | 2025-07-03 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 8d9ea776-c4f2-390b-8d94-9ad68ad42bc4 | -5.9216 | -43.4403 | 2025-07-03 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 435d9dc8-8cb6-3037-a4bf-36744877f03e | -7.1927 | -43.9806 | 2025-07-03 14:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 24270135-7c87-3ccb-b9b5-c0082ae168cf | -6.694 | -43.1648 | 2025-07-03 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 22441f3e-3e0d-3986-b129-6f1385b67115 | -5.9213 | -43.4636 | 2025-07-03 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 3448d0ec-81da-3958-ae6d-060f63586e7f | -6.2755 | -43.6907 | 2025-07-03 14:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 280.7 |
| 0e800068-fcd5-3729-adff-345e18cd71f2 | -11.546 | -47.8772 | 2025-07-03 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 9824ed57-ede9-34a9-9347-37b52d6a0401 | -11.3063 | -46.2073 | 2025-07-03 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| aec61974-a7a0-37c7-8332-1c4c5f693ec2 | -10.6483 | -44.4861 | 2025-07-03 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0760eac9-2d2a-352f-b412-26951e567264 | -11.5464 | -47.8551 | 2025-07-03 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 6a7eeb7a-a0d5-3639-86ae-1e27bb07a1b5 | -10.6483 | -44.4861 | 2025-07-03 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 559c24a6-ef67-3dc7-899e-a69ba73b4e50 | -12.6632 | -45.3008 | 2025-07-03 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f2fff420-3bfe-3a79-bcd5-34606f42da68 | -6.675 | -43.1899 | 2025-07-03 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 198.0 |
| 2012f477-a7d5-3a6a-97ee-9f899b150ca1 | -11.2868 | -46.2326 | 2025-07-03 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.4 |
| fc9bccc5-3f6d-309d-9479-9fac2373e13b | -6.6938 | -43.1882 | 2025-07-03 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 6a542141-6ab2-3608-982c-f78b66b89966 | -6.2943 | -43.6891 | 2025-07-03 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 350.1 |
| 1e85a8c2-1c02-37b6-8326-132fbbfe72d2 | -11.4602 | -47.2883 | 2025-07-03 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| a1bc5304-e4cb-38c2-8ccc-b3c94f383345 | -5.9216 | -43.4403 | 2025-07-03 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 5f289503-266a-3ebb-9b86-d8cda0b3cec6 | -6.2757 | -43.6675 | 2025-07-03 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 328.5 |
| 769c6d3a-71f5-3337-9c1c-54b9bc90d219 | -6.2755 | -43.6907 | 2025-07-03 14:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 291.1 |
| 25bbd7d4-2fac-3e54-bcf3-cfba1f89588c | -12.6636 | -45.2776 | 2025-07-03 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 9e764435-4f07-32ff-95dc-900096c2caf4 | -11.546 | -47.8772 | 2025-07-03 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 257.7 |
| f10564c2-2513-3683-a228-f60dd98a4d18 | -7.1815 | -43.3067 | 2025-07-03 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 32de45c5-615f-3b46-9579-da51782b242f | -6.694 | -43.1648 | 2025-07-03 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 143.4 |
| a3ee17c2-bedb-3b7e-8801-e232370f0e1c | -11.4793 | -47.2858 | 2025-07-03 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |


[Clique aqui para ver as próximas entradas](README27.md)
