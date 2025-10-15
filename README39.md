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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac5a3a0f-2018-330e-a8b7-e4de5a6de9a1 | -3.73718 | -48.35936 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47b67d56-2005-3f03-ac6d-3c53498bc269 | -4.10925 | -48.02497 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19e70513-fbd9-3a29-8091-c97587d68e31 | -1.11173 | -48.9321 | 2025-10-15 04:55:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10c97ce4-98ee-349e-932e-c1534eda08df | -4.8705 | -45.7746 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1dbbfe3-e031-36fa-967b-368827c0c403 | -4.25737 | -45.58591 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 31d76fab-0da5-3dcb-9c72-06a299be3baa | -0.89719 | -47.54668 | 2025-10-15 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f03f9e62-bb52-3dd9-9e26-32b499605912 | -3.13304 | -50.2129 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3997f64-c958-3b31-a074-ef3bd626b178 | -3.08468 | -47.73059 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f812f92-453c-3caa-bb2d-32e7c9122a13 | -3.04841 | -44.46544 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 223ad1e6-0976-3d22-8667-fbe709cd83a2 | -1.89764 | -51.0076 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8595a8dd-ab1f-3f4e-b358-db81318cf892 | 1.86178 | -55.70304 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 690fa548-2b37-3050-9e78-951c174ea630 | -4.10981 | -48.02131 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4488a6f-5beb-3fdc-a733-4b4f09cef29f | -3.42531 | -50.25529 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6949f4c2-c5cc-3c1f-8eb7-a249b15305e6 | -3.83704 | -44.54759 | 2025-10-15 04:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59698c72-aac1-3341-ab89-f560e634a509 | 1.77427 | -55.76413 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd104195-3d0c-3eea-a26d-9d766d8acf8a | -1.95258 | -48.22475 | 2025-10-15 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 952f47ed-583b-379b-8a45-ba35379d880e | -4.59524 | -47.03387 | 2025-10-15 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 140a3adf-bfac-3ab3-a36e-68e7391ebc7c | -4.89436 | -43.45794 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8b6f96ed-59c4-3561-911f-c5bcf8b6e709 | -2.87293 | -50.73443 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d6eff7a3-8faa-3543-8e96-ec25f21f894e | -3.13665 | -50.21349 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b13d088e-dce7-3531-b741-1434864da287 | -5.06039 | -44.44377 | 2025-10-15 04:55:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53f1ecbd-9d45-3d8e-8305-44bbf067d159 | 2.05174 | -55.79013 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03dbae29-5ba4-34d0-8902-de7e463d3115 | -3.07443 | -49.51328 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d652642-1f32-3423-bf18-29a068b3122f | -4.25882 | -45.5832 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe63351e-5e80-34dc-af4d-88dce64b65c4 | -4.25623 | -48.56785 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5acf9f8-fb14-356f-b7f2-6e021bfeea9b | -3.14466 | -50.45115 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae9fcc53-f6c8-3a50-a68c-5deca29574f6 | -5.40597 | -42.65182 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 62547457-1d61-37a8-b6ab-11689c2a15e3 | -0.90188 | -47.54365 | 2025-10-15 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 239827ae-a126-3292-bbea-c0edd2ca85a9 | -3.42957 | -50.25167 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4dfa736-daee-32f2-9197-fddd58fd5fb3 | -3.73642 | -50.25542 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f957e425-58fb-3f85-8019-df1ec9993085 | 3.44726 | -51.46849 | 2025-10-15 04:55:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6201b08a-4c88-335e-8c63-4026e042a1bb | -4.88858 | -43.45696 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c5f2aa92-963c-335a-9768-92c639fc7d76 | -5.4066 | -42.64895 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ef548b8d-5026-36d8-ab09-07c62d071d20 | 0.24151 | -50.94795 | 2025-10-15 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10d695f9-75b3-3d6d-b736-d0d5f1d8c949 | 1.85784 | -55.72537 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 167fe9e8-2c7b-32a1-bb6f-9dedf4410d95 | 2.29582 | -50.73162 | 2025-10-15 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e852bc6e-6a32-3d4f-b3f8-499174840753 | 1.30748 | -50.72569 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5343da2f-78bc-36e9-b216-4261657bae08 | -4.28297 | -48.58305 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4314d6c5-b986-3a80-8d78-a3f757ed9333 | -3.43383 | -50.24804 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 128e3ee3-c02d-3a01-9cdd-f1c3b633194c | -3.38043 | -50.28259 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f70ac69c-37df-3f9f-82d9-d7f7506d4e38 | -4.42706 | -47.75458 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f86827c2-be5b-3e58-a3d6-1778ecc960be | -4.89921 | -45.51043 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58e65a7b-8b9d-3717-b7d5-8395c712d925 | -3.0758 | -49.50431 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 378c8fb3-2024-3e60-9897-563d3fc839d8 | -4.65584 | -43.12936 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 84f8b97a-fc89-3a60-8347-ac60ca40f5d5 | -5.0381 | -44.73619 | 2025-10-15 04:55:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48739061-d113-33d7-a097-945110230305 | 1.80631 | -55.85138 | 2025-10-15 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e5877e8-e373-350b-be02-e7e9dd993f85 | -2.30089 | -48.57642 | 2025-10-15 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5d73125-e269-3d42-b483-4858730bf6b8 | -2.87935 | -50.73944 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11c847a0-c47d-3140-bd82-cc2ca1d1e361 | -3.43744 | -51.04046 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ca35fef-f241-3944-89bf-ae1aaf2119ab | -3.2585 | -50.02464 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69c050b8-5e18-3d09-ba8b-4896fa6eafb3 | 1.8565 | -55.71687 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9eaf43d-289c-30e5-acaf-c65b922bd121 | -4.4932 | -44.72621 | 2025-10-15 04:55:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8357fd1-6eaf-36c6-bed4-f9b0cf942185 | -4.89491 | -43.45395 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4b5fef66-40f5-3c89-b82a-1274a6d8d2ca | 1.81011 | -55.75438 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4da77def-a08d-3293-84d3-2e66c9f685f7 | 1.75518 | -55.78754 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99e5ed44-d24b-3d82-84b4-201504cca9e8 | -4.14444 | -41.65484 | 2025-10-15 04:55:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 01be7bc3-f2de-39e2-89ca-775497a6620d | -2.30058 | -48.57776 | 2025-10-15 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12ad7996-a014-360a-a155-819b85cec675 | -3.6233 | -48.91573 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5ab44e08-133b-32e6-a2e7-d30eeb8592a7 | -4.11537 | -48.02071 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 852a00f9-2b5b-3e91-8133-1982ac7913b3 | -4.25386 | -45.5824 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b2f2c2b-aa1f-3fa1-9f6b-b67545dc6b9c | -2.81482 | -49.20729 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 320b19e4-da83-3a86-b4f2-c59e54aa5e6d | -2.24804 | -47.87253 | 2025-10-15 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 86280625-d348-37ea-9fa1-32b881b3a327 | -2.14227 | -47.60296 | 2025-10-15 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b194fc-69c5-3b9f-a498-528cdd171c51 | -4.89427 | -43.45645 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d040a65c-6f32-3c6e-988c-511abcc97cd4 | -4.14541 | -42.2142 | 2025-10-15 04:55:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 19814f4a-dbff-334d-b7bd-8e48a4b907f2 | 1.87331 | -55.67598 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7a66aa1-5b7a-36df-a688-001af8196d23 | -4.2835 | -48.57944 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf6bbaa-af3c-30a7-8bdf-cad8bc9feafb | -2.98495 | -50.2905 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd5e11c7-cb7b-3228-a10e-87ae19b68e95 | 1.75056 | -55.80577 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e045899-061d-30d2-826b-610f073337cb | 1.072 | -51.04197 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f60d521b-bcab-3beb-b6ee-ae291094a72a | -3.5704 | -49.43958 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99a4e8a3-de52-32a3-a815-4ffc2071797e | -4.79794 | -45.716 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7ab2b5e-451b-3400-815d-72ba09064741 | -2.81411 | -49.21191 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| de91160b-0f97-3b9d-8534-746f1ca2c6cf | 1.76708 | -55.76825 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bf4828f-3aa6-3ce8-8d8f-288ed3517719 | -4.28404 | -48.57584 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c76c5c15-4c66-382b-ac95-2362f93ceaa4 | -4.54812 | -45.42245 | 2025-10-15 04:55:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79d86e99-3902-30d8-8b43-94b798f02f74 | -2.98854 | -50.29107 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d0d471c-0c80-381d-8333-1ad3c1f26be3 | -4.01712 | -48.96753 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ee4b3bf-e30a-3220-8400-47127c14756d | 1.2975 | -51.24302 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da03460f-616c-3057-bc07-694032901ee4 | -2.94995 | -49.33749 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a80c4e9d-29f4-3391-9993-18162ae51d48 | -4.87194 | -45.77483 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2772b3ca-3912-3560-af33-ad1802aef9d8 | -3.05415 | -44.463 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8b03277-3375-3fec-923d-c73d08ad8661 | -4.11063 | -48.02384 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 126b503f-6c92-3b14-9e14-c85dbaa0cf1f | -4.89904 | -43.46675 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 47e1db24-d489-3332-bfc4-273f770ace9e | -3.09972 | -50.38567 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e21919ac-d1a8-30ac-8abd-5f475c96095e | -3.05272 | -44.47277 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0bbede08-5a12-3ca7-bc28-d140cfdb9cb8 | -4.3947 | -43.46365 | 2025-10-15 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f68c1af9-0af6-3d91-aef0-02cad8abe858 | -3.52949 | -50.30803 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3cda8189-3b52-3c87-adfd-93334c14c26d | -3.16332 | -48.60683 | 2025-10-15 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06d2385c-c6e1-3c5c-b4a8-4a72442ad43f | -5.25411 | -43.47477 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42ec52ef-9345-3b95-a656-e96641efabb3 | -3.73316 | -48.35777 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87102cf1-1358-39ae-aab4-4941f00c391e | -3.38405 | -50.28313 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38adffe1-5b20-344a-9827-92cd30fbb178 | -5.00959 | -44.48861 | 2025-10-15 04:55:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 599d2cf9-aec3-383f-b35e-db2511b0384c | -4.32064 | -44.53813 | 2025-10-15 04:55:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1e257eb-8a38-3728-b347-a52c2df7b165 | 1.78523 | -55.76252 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5a8badb-c388-38f1-a129-2551b0510b81 | -4.79835 | -45.7131 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b42848e1-8737-3fd1-9d15-b63f7b55975a | 1.75585 | -55.79182 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f1e4d2d-552a-3969-bf96-0ce314ac9f9d | -4.77443 | -45.73059 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4e126c1a-2658-3d52-b8ef-5d50c38c5584 | -4.35719 | -48.19604 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c025833a-343e-3586-aace-a16fbe4e97aa | -5.42849 | -40.98395 | 2025-10-15 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |


[Clique aqui para ver as próximas entradas](README40.md)
