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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15c83ef5-c381-3cc9-a785-1c476b455b07 | -3.83036 | -48.88855 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| af302b4f-ae42-3bad-bd0c-4d0c440a66ff | -3.81841 | -48.86953 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5cc97b5f-4517-33db-a192-5953f0df9d10 | -3.81748 | -48.87503 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 031b9c37-ea00-399b-b1b6-b87605822381 | -3.8135 | -48.86872 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6525c473-da6b-3224-9397-c9817382f4b7 | -3.81257 | -48.87423 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cd22131e-693a-3089-823f-09dad9cd8469 | -3.80834 | -47.80219 | 2024-10-20 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d4941eb-68bd-325d-b6a0-412ae4b23c7d | -3.7623 | -48.89108 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 843a34ed-61b6-33b9-8672-967da2bc06b6 | -3.75872 | -48.89382 | 2024-10-20 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bcbd1d1c-3b38-39a9-8755-af9f9da82684 | -4.34674 | -48.56498 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63f5f51d-eebd-345e-a23e-d13d8aed3a74 | -4.3459 | -48.71629 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89a62de5-1400-3913-a2ad-99e9cbae9238 | -4.34589 | -48.57015 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 84bcb18a-e332-3d3b-b777-a930e422df6c | -4.34198 | -48.5642 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4d7928a-40e8-32c6-b703-a8588371d4e9 | -4.34189 | -48.71397 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b867c976-bc93-3c44-87f2-e15f4b800c88 | -4.3411 | -48.5695 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 557ea37c-f7fc-3109-a2a0-398a76487c67 | -4.34023 | -48.57476 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e76a0bb3-6a08-3319-973d-0f9f79ae70cb | -4.33632 | -48.56878 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1f2b912-4d45-301d-8071-b79231478ca3 | -4.33262 | -48.62064 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 48da4db9-ec03-3fce-adbe-91e8e3a6cfe2 | -4.32784 | -48.61984 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8ecb91d3-63ae-390a-b469-75699a676364 | -4.3004 | -48.33691 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52324830-cf87-3f4a-b0c4-cc4cb803e325 | -4.29605 | -48.60426 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3577ca0b-2c68-39e2-bbd7-eaea55584ee6 | -4.28775 | -48.62428 | 2024-10-20 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1a0e87d-9798-3d28-8ad9-d10423615f97 | -4.27824 | -48.06644 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fe93891-7b0f-3345-b6c5-0b68c224d043 | -4.10419 | -48.2418 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f50ab54-8301-3408-8578-8a4af7d5137c | -4.1034 | -48.24667 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93741dad-cfaf-3489-be53-4a49f071aaf4 | -4.10238 | -48.23911 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5353614-c1b9-352d-b732-623ab05ce878 | -4.10156 | -48.24397 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30e980a3-9164-3077-b04b-8712d60aefb4 | -4.09948 | -48.24121 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 791e399f-5a4e-3bb7-ac5c-0dec6190cc1f | -4.09768 | -48.23854 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 592d90f4-49c9-302b-b6e8-5fed7be466a3 | -4.07975 | -48.27368 | 2024-10-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a37b808b-da3d-36a1-8008-75a05bc9ab60 | -5.92037 | -48.13926 | 2024-10-20 04:08:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ba1eb51-69f5-32fd-96d1-4a91e2cd042b | -8.88735 | -48.82867 | 2024-10-20 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d76aa8b-0dc2-3fb5-a342-fbdf6aee5b99 | -8.88535 | -48.82624 | 2024-10-20 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef2ac703-47e1-3df2-a5ba-10bf0c105fab | -8.88455 | -48.8307 | 2024-10-20 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a46da790-b03d-35c9-be12-01666ff10f92 | -8.88286 | -48.82787 | 2024-10-20 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aec9d3e-df6a-30c3-a3c2-8caaf9ea50f7 | -2.12516 | -49.53812 | 2024-10-20 04:08:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be6f0c2e-8a66-32b6-92ac-118b50bdf111 | -2.11988 | -49.53727 | 2024-10-20 04:08:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24bee5fb-3d18-3f37-be47-4286de0e715f | -3.22098 | -50.35962 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7a51de9-59e9-3251-b7ae-2cc47de52b38 | -3.15483 | -50.38008 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19378812-336a-3b46-8d95-0c99ae5803ff | -2.973 | -49.09518 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 115a37da-247f-3580-a76e-2f439e73165b | -2.97253 | -49.09806 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a69edf8f-cfcc-3dcc-ba17-d0baa9419208 | -2.96168 | -50.52139 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 950e3f7d-4ca4-3b1b-bf0f-950d7ec689fa | -2.80711 | -49.61882 | 2024-10-20 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeeba970-f2a1-3e9c-94e5-cd013d227604 | -2.80602 | -49.62531 | 2024-10-20 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c095f01f-daa7-3169-9669-beef1d37e558 | -2.80186 | -49.61799 | 2024-10-20 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2a5909f-4e31-3f87-9282-fcec952cf26d | -2.78939 | -49.30186 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e8f3a08-c20d-397c-b745-865749ee44de | -2.78888 | -49.30495 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 7735db08-67f0-32c1-b055-92a78e45f023 | -2.78837 | -49.30806 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| cf78cb45-c5cc-3bca-a971-34b3c1c67702 | -2.78785 | -49.31118 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 29c9d3d7-8a4c-3e0d-906c-93569c6f9592 | -2.78475 | -49.29799 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fad49ce0-3d42-3450-a108-27b981d8d016 | -2.78425 | -49.30106 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2e2964ff-6d41-3765-9174-dbd96fc20b16 | -2.78374 | -49.30413 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f7aa1466-0f53-35eb-9ce7-53d8a8cd90ef | -2.78323 | -49.30721 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c7ca37a7-0529-3a22-a2ce-d0cb8a01854a | -2.78272 | -49.31029 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a9b38741-d23a-31cf-922a-11ade0963ae2 | -2.7791 | -49.30025 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9f90c9a5-cd24-3355-a1df-20a3ec078c4e | -2.77859 | -49.30333 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 08565d03-01fc-333a-ad5b-1ad7cb94d8fa | -2.77808 | -49.30639 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ad227b96-7893-3828-ac53-08b229348618 | -2.77097 | -49.41344 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b5ccc83-1bd1-3edf-afd3-6cb8e2eebf38 | -2.77045 | -49.41658 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83d77d66-5ae6-33ea-ace8-454d13714694 | -2.7663 | -49.40947 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7707b933-15c9-32ae-81ad-a395699747a1 | -2.76578 | -49.41261 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 518cca36-a5c2-3f95-9d84-e48848246199 | -2.76526 | -49.41578 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2e5097df-fa0d-3457-a27f-147abff82109 | -2.68417 | -49.31717 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d97ca2d4-b21d-3a83-b27e-b05c59139460 | -2.66171 | -49.13575 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 341cf222-83b3-313c-9027-7bb73102fd73 | -2.66119 | -49.1388 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c78ac238-1c6c-3d10-9557-47db4d18a07b | -2.66068 | -49.14185 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e18b3ef6-d356-3812-aba2-cabe043e0eb8 | -3.55282 | -50.31026 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 74a5685e-4161-30db-a4ec-d8e98104b439 | -3.55224 | -50.3137 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7cb1ffed-2bed-38d6-8388-a69586a641af | -3.54563 | -50.31052 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 728fc537-bd08-33a4-8d2a-b2dc9d6c116c | -3.54506 | -50.31398 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9e87c88-e37f-32aa-a11c-88f45b3fe358 | -3.45322 | -50.32799 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cddf699e-75fa-3546-b02b-477c85ecb6fb | -3.45261 | -50.3316 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3f85799-e429-3b31-a3d3-dc7e34377668 | -3.43376 | -50.2136 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd207e04-19e9-3c87-bb2b-19ec8f00837a | -3.43315 | -50.21714 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef1ac6b3-d418-3a57-83b0-f5db5979cfd3 | -3.43245 | -49.97608 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcebee25-a58d-3b3a-8634-1dfe68067f31 | -3.43161 | -50.2132 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e92e5ca8-e891-3c55-8f2b-9df74ffb3316 | -3.42712 | -49.97525 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98f51b10-e55c-378f-9569-eef9ccb990c5 | -2.55744 | -49.17666 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41b802a0-d217-3b57-ae82-ab42e13c4c10 | -2.55693 | -49.17969 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5d74807-5884-3ffc-a3aa-81a406279e7f | -2.47772 | -49.10098 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5c6fa76e-9acf-33fe-936a-bd2126f89dfe | -2.47262 | -49.10019 | 2024-10-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1465bb8-99ac-3119-b1ee-c1b931e25fd2 | -3.54739 | -50.30936 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 239f85f1-b798-3f77-8462-d33ed0e0c8fd | -3.5468 | -50.31279 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e8d1f09e-1922-33db-8ed8-c8d0669b6f43 | -3.47661 | -50.48992 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d15812f1-50a9-320c-9721-29526bc7a497 | -3.47602 | -50.49347 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 525c5e53-b699-3cb0-97fc-6272e5ae5eb5 | -3.47085 | -50.35632 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2490b3eb-261d-3db0-9b14-67b30ffed4a6 | -3.47024 | -50.35991 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7442e4a6-d0b5-346a-91c0-bbe732b13e90 | -3.43734 | -50.19286 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf95899c-3854-3a93-b868-792080e27092 | -3.43674 | -50.19633 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e23059c-efea-309d-bd27-edc7e9f1597e | -3.43101 | -50.21679 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77c3c2cf-21f1-3a68-acaa-a2e542a55a83 | -3.42677 | -50.20886 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 748ef856-fd3f-3642-8bf5-3223f7c6e54d | -3.42619 | -50.21231 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d493841e-2e03-39bb-b757-ae11854e89d6 | -3.38771 | -50.34311 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8e31f5d-687d-326f-9458-b0b636ecb1da | -3.38712 | -50.34661 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8c54f70-7f87-3e07-abdb-433f1665ee71 | -3.38165 | -50.34579 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1547f9f7-bd98-3325-aad6-961082c07c4b | -3.36089 | -50.30252 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb8b1a2e-8dcf-3c25-a67c-666a48065bad | -3.07265 | -50.50103 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b6468b2-a6bf-3e69-9e6c-0ee8b5840f7d | -3.06718 | -50.362 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac013ff8-c816-3fc9-8bfd-ed421c8590eb | -3.0671 | -50.50011 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b485de61-8b3a-3d7e-97b4-e0fc1d895e7e | -4.97798 | -49.86908 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cd0cf12-c782-3f7a-95a2-42317a853710 | -4.84023 | -49.91847 | 2024-10-20 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
