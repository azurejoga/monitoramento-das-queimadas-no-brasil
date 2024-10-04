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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b974733-a46a-31a5-b4f4-0dc61fb1aade | -10.44604 | -50.74622 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24875203-7f09-3bca-a359-ba184b1bd7d0 | -10.44534 | -50.75107 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef5ac4ec-b3c1-32a3-b54c-d571a118852f | -10.44507 | -50.78031 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 042265d8-ce87-31ec-bb7b-70bc786172dd | -10.44465 | -50.7559 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 745af003-c345-37d8-a664-cc8d193dacf9 | -10.44428 | -50.7311 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b963068-cb0b-3e56-8fed-27225363e452 | -10.44396 | -50.76069 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2bcce58d-ec24-3794-b6ca-8a2e859b5a50 | -10.44359 | -50.73594 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09a65caf-c9b2-336e-8326-58040039f192 | -10.44328 | -50.76546 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a1a45cc-fe14-3ade-8d94-7d810f6c5797 | -10.44289 | -50.74078 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f62d7db7-3a4e-3947-92e5-547c2382fbe2 | -10.4426 | -50.77022 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32e6a90e-768d-3fe9-add1-d0c86309b2a9 | -10.4422 | -50.74562 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 460894c8-0741-3efa-91e7-54f57f8685a7 | -10.44192 | -50.77497 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3e95206-303b-37f1-83a1-588df1edfdfb | -10.43987 | -50.78923 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de1f50ec-27bc-3fe9-a5fd-82b3d8035c59 | -10.43975 | -50.73535 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 894ed875-1d81-3b3c-916a-e99e48b31dc7 | -10.43906 | -50.74019 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b12fd978-f319-3030-b9f3-99883187893f | -10.43153 | -50.79292 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fe5195c-3f77-3970-ad6a-930c28eb7acb | -10.42878 | -50.81211 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7256282-1247-3222-afb5-79b5315d4c9c | -10.42811 | -50.81684 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3337c853-dcc0-3670-8390-72fd7c2ce289 | -10.427 | -50.79723 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d19ccd9-ddc7-3802-95aa-aa28dcec2403 | -10.4263 | -50.80219 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fafe5bb-cc24-3e3d-9a7b-3e1d950899fb | -10.42562 | -50.80693 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8afe5d1-31d6-33c1-80f0-843bab59a118 | -10.42496 | -50.81154 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5ed4073-69ad-3bbf-9b5f-be3cde2e940a | -10.42318 | -50.79664 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45077314-b126-39f6-8859-6ed19c0914f4 | -10.42248 | -50.80158 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9ef0f807-cc4e-3e75-bd60-f97ea67f99f4 | -10.42179 | -50.80635 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 19613c49-bca4-39df-a443-36875f9ccef8 | -10.42114 | -50.81097 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 33c97e88-12c2-376a-8b8c-d1ed5e614b48 | -10.41798 | -50.80571 | 2024-10-04 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e06e648d-f849-3016-92a0-33f13aa2e8b7 | -11.98784 | -51.9015 | 2024-10-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9222774d-0d5d-357a-aa90-38ed5d7a2b44 | -11.98417 | -51.90099 | 2024-10-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7df66bb-dce1-3149-a869-b29abe89b689 | -11.97987 | -51.90486 | 2024-10-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba94b2a-96d1-3c4d-ab83-5ad20a46f040 | -11.9762 | -51.90433 | 2024-10-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f9c9d8-986a-372e-92d0-df95e2112114 | -11.97254 | -51.9038 | 2024-10-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc032ff9-e123-321c-82ff-7f963c28f036 | -11.95331 | -51.88482 | 2024-10-04 04:57:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94ff94d1-d22d-342f-81cf-b5667b506239 | -12.91061 | -51.27874 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8372aaf6-85bf-3083-91ce-55550ae7c5bf | -12.73491 | -51.97234 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 863361b6-23a4-303e-9199-c45d909a23d4 | -12.73061 | -51.97617 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8336379f-6e99-38b0-8a3a-1bffa5010516 | -12.72567 | -51.9845 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2950b9d5-4c68-33a4-abf7-a2189d23c8f2 | -13.04799 | -51.30835 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75b0b6d4-d1cc-3e41-ae83-6176b159f20a | -13.27519 | -51.2552 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eac8953c-881a-3d43-a0d7-7a13a358a52d | -13.27132 | -51.25463 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94d6c56c-e69c-33f5-abd4-b3b59dff4419 | -13.26746 | -51.25406 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9709bdc8-bd2e-3cca-b221-abf5030e2f53 | -13.26291 | -51.25843 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db0c2722-d641-3e04-8cee-7d2751e3a46f | -13.25972 | -51.25294 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9eee4fc-85a5-3c4e-a33a-861d85d79e30 | -13.25586 | -51.25238 | 2024-10-04 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1128eacf-0a60-36bf-b589-c0d4b514e942 | -13.18244 | -51.23012 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16f17466-b1b1-366a-b67a-066a849e5dc0 | -13.14554 | -51.20259 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5c9dd90-7b29-3a9e-92bb-bd3f00f234a1 | -13.14326 | -51.19924 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b5afa3c-fc79-30bf-93c4-695454d959c3 | -13.13939 | -51.19868 | 2024-10-04 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6406eb1-deb0-37e9-9668-b07d1287ea36 | -10.68934 | -53.04127 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 296928cd-8150-30be-bc42-dcfc2d95df7a | -10.68591 | -53.04074 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1dcc5b5-ac85-376c-a35b-85e15a7040d5 | -10.64025 | -53.66665 | 2024-10-04 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 380d9942-3738-39d3-906c-3f435f2dff89 | -10.49844 | -53.00454 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42a4d378-3f17-3706-9732-2aa1f17e91c8 | -10.47718 | -52.96315 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 884ba268-cbcb-390b-9ac6-4f2311c8c0dd | -10.47431 | -52.95883 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c0de045-d2c1-37d3-bf79-3cf0b37dbd04 | -10.44908 | -52.93942 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 402fd76f-811d-3ebb-901a-952914d392d4 | -10.44851 | -52.94321 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 788edfa7-b69b-3162-987b-864e11f5a36c | -10.44794 | -52.947 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47381171-3e1b-380a-9c3e-55d430134acb | -10.44737 | -52.95078 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93f46150-762e-3d8f-95cb-c7413368b959 | -10.44621 | -52.9351 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f04fdbef-d30f-3348-a770-9a3289c10909 | -10.43164 | -53.67904 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8657f6dc-d055-344f-ad61-f652c2330d44 | -10.43104 | -53.66039 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ff55cf4-d0c5-39a7-b5c2-3b928817b4f5 | -10.42212 | -52.93136 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1ac047f-637d-31fd-9c2c-6f5e8bd3baa4 | -10.41924 | -52.92702 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58aaf802-eab0-3c47-94e5-b2847073280d | -10.4158 | -52.92649 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08d11461-f616-3459-8dff-d3c89beae4c4 | -10.40604 | -52.9211 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36d4456a-84f1-36ac-86cc-fdc3d58cbc04 | -10.40316 | -52.91676 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02888cc9-03b4-3919-8bb6-6d866ce7a993 | -10.40031 | -52.91664 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3eb043a5-5fe2-354e-9196-72262e28be44 | -10.39972 | -52.92045 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbbb0da6-d705-3c59-b182-229c413a3769 | -10.39915 | -52.92004 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e539c7-85eb-3dca-8b5b-ac64bc76db2b | -10.39284 | -52.91939 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 325cff6e-2b3a-3183-950e-6af797e514c6 | -10.38882 | -52.92266 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 614bda3e-e24d-3439-b617-ded83ac99b98 | -10.3848 | -52.92592 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 269c9311-f97d-30d1-acbe-fab33e1b7f62 | -10.38423 | -52.92972 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4172f2ad-1fec-30a4-856a-5bf99334910d | -10.27907 | -53.32307 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 184a9228-fad0-3a97-b5b7-48af152b905e | -10.27568 | -53.32254 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68152da2-19a6-31aa-9dfe-59cdee0c2759 | -10.24419 | -52.74157 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4497feec-778d-3adf-9577-454c535f1b0a | -10.2413 | -52.73721 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3717a9a6-e1fa-3754-ae38-c8250aecfeaa | -10.24073 | -52.74105 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a60be17a-981c-3b84-b53d-55210423f509 | -10.24015 | -52.74488 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51929900-c1ef-341c-9fa9-0023def81fca | -10.23783 | -52.73669 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3fe056d9-f4bb-3446-a522-9b8299eaf562 | -10.23726 | -52.74053 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bba8c87-2e5b-3d7c-bf0f-fd199b7e9705 | -10.23669 | -52.74436 | 2024-10-04 04:57:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 247a879e-7d9e-3c0f-8617-9221946a28ff | -10.01082 | -53.43258 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a59034fe-15dd-3d6a-9b78-a9c068279277 | -10.01027 | -53.43623 | 2024-10-04 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ac0b4f1-fc47-38cd-8ab7-541bf509a723 | -10.9203 | -52.42084 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 456a6b26-6020-362d-8f58-45498e73e648 | -10.91971 | -52.42486 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11790369-6a3d-3173-94fe-2efdc3d1f083 | -10.91912 | -52.45353 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12e17344-81f4-312b-8e0b-15daa46fc573 | -10.91912 | -52.42887 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5219426-a237-3509-b231-1f17baf991d2 | -10.91854 | -52.45755 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84a48c6d-ddd7-3eaf-9985-06ce2bf71cb8 | -10.91795 | -52.46156 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcefcea2-f87f-3421-a344-c7752878fc2d | -10.91736 | -52.44091 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f844bf5c-e7b7-395b-931b-e68feed5e043 | -10.91735 | -52.41627 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa947efc-3d00-3186-82a9-0e3e5a7429d2 | -10.91677 | -52.44495 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 692d06f8-5b11-3f0d-8ce0-d05e6a4f6d02 | -10.91676 | -52.42031 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4d113d2-a966-3b8b-a78d-8c7dff6476a1 | -10.91619 | -52.44898 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e939427-0cf8-3a8a-9d08-aaee40c28b67 | -10.91618 | -52.42434 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dcff9ae-cc25-3af5-8df1-cdfcbd78b2cd | -10.9156 | -52.45301 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 266453c2-336d-3ddd-8e31-bddc77e07a71 | -10.91558 | -52.40364 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6175823b-2e16-3525-98dd-d8148bf80b9d | -10.91442 | -52.43634 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 290fb9d3-3c99-3279-8abe-d1c7ae6bebef | -10.91384 | -52.44037 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README157.md)
