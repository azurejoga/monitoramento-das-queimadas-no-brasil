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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a424d5a-9937-371c-ba2c-7bca4200dd37 | -13.18713 | -51.36078 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4797c1b-a79a-3198-9a4b-492caae89ee6 | -20.51763 | -44.73018 | 2026-08-26 04:10:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 04eb3eae-2d0b-3842-9539-e4696489e9a2 | -14.369 | -51.75872 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 532f43ca-55b5-3201-ba7b-bad17036bf98 | -13.24801 | -51.51654 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 435283ba-1a3f-3b7a-ae68-3726af11b73f | -16.50017 | -39.91647 | 2026-08-26 04:10:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f8b5232b-77f7-31d4-bf3c-5ee4a40b951f | -15.27098 | -52.7692 | 2026-08-26 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3889de1d-c6ec-3ea1-9a64-45a6d1410761 | -13.85849 | -54.05363 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e80901bd-b42f-3e4a-a745-64b887eb6fd8 | -13.23401 | -51.3869 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fb70e817-2a76-34b7-9bd9-0c6ae164ec50 | -15.5946 | -53.12544 | 2026-08-26 04:10:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba09c81b-9a3b-3a3e-aaf6-ff070648c0ab | -13.29345 | -51.46326 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 53d67f02-deea-373a-a613-0c643cafccb5 | -13.85524 | -53.99204 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19507a79-588e-3589-b8f6-67f078753710 | -13.85627 | -53.98707 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87848eed-05ef-3367-9a04-808c28839fe8 | -13.2528 | -51.40569 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9dcfd616-d3c5-3bab-881a-3d06fe37f657 | -14.28459 | -51.14686 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6b8bd2fb-94a0-34eb-b6b2-d736b4783ec4 | -18.22082 | -42.83919 | 2026-08-26 04:10:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8641cbc3-04a6-377e-8d94-5ab934bdbc0b | -14.42045 | -53.35323 | 2026-08-26 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4e0865c-a40d-3bb7-a228-c5e0c11473a1 | -13.26565 | -51.46107 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a41cbe38-7c06-3f1a-9a8a-f9736b3eab39 | -13.25889 | -51.51884 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 604f5a45-e108-39af-9c37-4eca3551de37 | -14.3232 | -51.73387 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6aa0073d-6def-3fe0-a34a-831d9ef31b11 | -19.64864 | -42.91451 | 2026-08-26 04:10:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3296157d-1591-313c-bf06-b79a6fc12cac | -20.24661 | -46.32815 | 2026-08-26 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 875352b6-916b-3003-8ef2-dc8c11a33967 | -13.87054 | -54.08989 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ab8b8641-a5e2-3f6e-9079-ce1709b68ddc | -13.1885 | -51.35371 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1176f11c-9285-3402-b9d5-c2b8ae625f13 | -13.24589 | -51.5274 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1405dc0c-d264-3747-a950-f7accdfc8ae2 | -13.2701 | -51.46133 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a66d7ac7-4021-3347-8e21-930aa9739e93 | -13.85728 | -54.05933 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40ca7fd8-3a41-3a0e-9307-f79c88ae00ee | -14.84038 | -45.52719 | 2026-08-26 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 690d9a4a-96b0-3d93-b85a-100196900640 | -13.26638 | -51.45749 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ac1213fa-4ee5-3ee8-9517-b85534c10ec8 | -13.60266 | -49.01233 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68c71edd-66b4-30e1-a501-03f598869275 | -13.60362 | -49.00719 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e19e852c-66e5-3df3-ac53-e10ebb52cc7e | -13.18899 | -51.35896 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 34297883-3350-3f5c-8861-eedde497f1a6 | -16.52346 | -49.4234 | 2026-08-26 04:10:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 42d6607a-b986-34e9-b8fa-2a0d72bd78f7 | -13.85382 | -54.07559 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b928ff44-6b14-3f2b-88ec-a666c0500d24 | -13.2718 | -51.45863 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a6e0e6d-dbcf-3b14-b203-dbf24c86d47c | -18.64767 | -47.28756 | 2026-08-26 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 230284e1-92fd-3426-b10c-ab76772b27cb | -13.28023 | -51.46725 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b8dc386-3df8-35d3-aa49-fd1784b3a00b | -13.61183 | -48.98869 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5298aae6-1dfb-3e75-bfd2-f5711398234a | -13.23002 | -51.37866 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7e34a3e9-75d5-311e-bb5c-61f5708c778f | -17.69544 | -40.18262 | 2026-08-26 04:10:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 250729c2-dd63-3e29-9adf-a1db8767337e | -13.2819 | -51.46453 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2adb39e0-0ebc-33ba-9456-e9d0e3fb9073 | -13.29274 | -51.46683 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c594dd32-5805-3a91-a94e-5e8626c08d06 | -13.18644 | -51.34373 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 57c5cf73-9fc7-3e0b-972d-b65cd896e450 | -13.19112 | -51.34838 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b94e1ae0-fdae-36b2-9b45-31cf12bf0706 | -18.66786 | -42.21542 | 2026-08-26 04:10:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0078fad4-35b6-3285-9440-7d9f4b18f690 | -13.22721 | -51.39284 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05f2bbd9-dd12-32b5-9cf3-01c2373a6294 | -13.2533 | -51.52201 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a7f9e19-08b5-398b-b7a5-36b8357557e7 | -20.34962 | -47.50232 | 2026-08-26 04:10:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf8eeed8-a76f-3399-9cec-b2e19160b61a | -13.2488 | -51.39744 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 89448e49-ae4a-3a29-b340-b6d173adee9a | -14.35889 | -51.75282 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 72664060-8a50-3497-a7d1-828600e80308 | -14.39064 | -51.76345 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6120117a-8a39-3d15-9c65-7e621ef2bcce | -18.54055 | -42.57718 | 2026-08-26 04:10:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d825d8f0-728f-3efd-98f5-550b05c56814 | -16.17496 | -50.76468 | 2026-08-26 04:10:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c8ab341-4570-385e-a726-bf749931d139 | -13.23665 | -51.48787 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 374bb01c-9d12-3122-9dae-87d7eb2bdad9 | -18.21304 | -41.57181 | 2026-08-26 04:10:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 377f9321-7413-35f9-92f8-c4c1cab0b314 | -13.85877 | -53.99068 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8abe12b-f17a-32a7-ba17-53394d31103c | -14.28524 | -51.14354 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8dd2b575-c43d-310d-a2bf-de70ed828737 | -13.19041 | -51.35191 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| b3d06cc0-44f4-321f-b697-05ee95686ee8 | -13.18573 | -51.34725 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b06f5ab6-0abd-39f6-a8fc-81fcf3d067af | -13.25204 | -51.52493 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f7168aa-ec5b-35e8-ad15-ccb1f318f35d | -13.2394 | -51.38805 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f669f1f0-8f11-3e42-a074-ac9b0ecd8753 | -18.64674 | -47.29257 | 2026-08-26 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6986aeb5-d466-3ba6-bbb4-1a5812436bf2 | -13.66158 | -51.84447 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8dd3e13b-5eed-3ddc-b9ed-b5a8a518f667 | -14.31736 | -51.72825 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce131f81-c5b1-3322-923d-4809d9b3fd7c | -13.29815 | -51.46798 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3a08a55c-53fb-3916-9d4b-2ace7d73db51 | -15.76643 | -43.37499 | 2026-08-26 04:10:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96cbbcb9-39fb-36c9-a70f-e0ffdc7ea724 | -15.04981 | -41.23719 | 2026-08-26 04:10:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0670dd1c-29fd-32eb-bbdb-7e51a75d90c1 | -13.22931 | -51.38221 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9e189dbe-ab79-3d98-962b-825b493792ad | -13.16225 | -51.34444 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd813aca-e613-3d32-9a7f-dbfc7a464817 | -13.6493 | -51.84828 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81c3f203-e201-3a75-860f-e39adf129062 | -17.77591 | -47.0952 | 2026-08-26 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69751405-c2f4-3f31-97f7-098c33b930f1 | -14.28589 | -51.14022 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 168a21f6-758f-3a4e-a48c-4e54a6e0d0b3 | -16.61633 | -43.41567 | 2026-08-26 04:10:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 908c7b27-abab-367e-ae6d-202e6f64c898 | -20.35081 | -47.49947 | 2026-08-26 04:10:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e8f41c9-d561-3f10-a9ed-c9d0c4500111 | -13.24518 | -51.53101 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 74e6a4b6-3420-3eb2-9f96-cc9dad41ca80 | -13.86351 | -54.06093 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49bc317a-1193-3f71-9912-6b14c4531072 | -13.60721 | -48.98796 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 92d793b8-980b-3c47-824c-457d433dcef3 | -18.69814 | -46.59791 | 2026-08-26 04:10:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40437de6-8409-3828-9079-b5bdd4e46fe0 | -13.18919 | -51.35017 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 23f17b57-c21d-35c4-b579-df9d54176a03 | -13.42867 | -51.84537 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9b19f57-3893-3257-a4e7-a75246ed5e96 | -13.18987 | -51.34663 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f6ffb6f4-646d-3061-bf6d-2eb306a3795e | -13.25019 | -51.39033 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 1bac5b04-62f7-3433-b1fd-4bd08793826f | -14.39534 | -51.76822 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c7f01feb-43cb-36a8-a255-60e01b04e385 | -14.30141 | -51.11641 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8f9e6f7-18c2-325d-bb55-68815d8f0ab7 | -14.32135 | -47.23489 | 2026-08-26 04:10:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d12988e-b12b-37dc-aa6b-894427d31e44 | -13.2535 | -51.40213 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ad1009ba-a703-3b2b-8c24-02362feb81fd | -20.52162 | -44.727 | 2026-08-26 04:10:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| adaca4cb-3ca8-3330-9482-5268b8010675 | -14.32406 | -47.24299 | 2026-08-26 04:10:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe32103c-e7de-3b80-a88c-305c02da5497 | -14.79525 | -48.80658 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f0a3c76-99b4-3d8e-8f20-e5f843ad3fb8 | -13.23974 | -51.52985 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3097791-7989-3020-9e7f-dde9376d3fd9 | -13.23331 | -51.39044 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8597d55a-4679-3f57-9ca2-18ccd3325931 | -13.16833 | -51.34205 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72b23a9b-3254-39f5-8ad0-29b11e39caad | -14.29237 | -51.13491 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52e7f067-fa30-399b-a1df-d5888c1cb6e5 | -14.79176 | -48.80072 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99944b00-eb1c-3eb0-bf56-30560b2ca7b7 | -18.65053 | -47.29336 | 2026-08-26 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 213c4c2f-ee43-3114-a98a-68913b3ca8ba | -13.85983 | -53.98571 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a04a0a44-ea5f-36b3-afca-87a42a9476fc | -18.94274 | -41.01412 | 2026-08-26 04:10:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 970336f1-29de-3dee-a6ba-c1659ac44d8a | -13.26493 | -51.46464 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72ab8361-71c0-3582-af1c-8457e61a77df | -13.242 | -51.4034 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ea5277d-e9a0-317f-908f-ce5f3218fcde | -18.64708 | -47.29523 | 2026-08-26 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 67c73232-f40f-3ac4-ac39-903f6db5ea96 | -14.53502 | -52.28719 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README25.md)
