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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daaabee2-d6d5-30bf-a705-554463870af0 | -7.88505 | -46.09199 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0a1ca601-781c-339a-9fc4-68bdf9964546 | -1.3604 | -54.63435 | 2026-08-28 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06a9012b-db1f-31cc-8c8d-e879df0fc390 | -8.16467 | -46.179 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0fa78778-7d60-3920-b710-274a0f729591 | -6.26949 | -53.11933 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73d8117f-31db-3e61-8539-89772e62f456 | -6.64334 | -53.18986 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47a70566-e603-3df3-be36-ac47d86a2aba | -6.2397 | -53.47942 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b55ea856-cfc6-3343-beeb-3f6887bc00aa | -3.23166 | -40.02153 | 2026-08-28 04:49:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c64e347a-4cf9-3d14-a9d7-d2fd2eeb2c00 | -6.27614 | -53.3541 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4bde840f-e03c-35b8-b23a-56e2ad92d662 | -6.49798 | -53.25356 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ba85aa5-6483-3309-b716-0adc98594553 | -3.94227 | -54.84349 | 2026-08-28 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fc57471-5d11-3a77-bcf8-82025f94184c | -7.20697 | -42.75022 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1818ee87-13ab-3d49-9094-f76be765f16b | -6.16475 | -57.79141 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e0c73cf-2618-355c-9776-212da3af57d9 | -5.81409 | -46.22099 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7dd2722-47da-3b1c-814b-b63b09c3dae6 | -6.22233 | -53.46948 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12bc1e51-48b1-3aa1-875f-dad7252b71e6 | -3.46367 | -39.58157 | 2026-08-28 04:49:00 | NPP-375D | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4e757934-cf1a-3f54-89f5-7dda82cf274e | -6.16979 | -57.79231 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d04d77c-76b9-3dbf-b70e-02afd377bc13 | -6.63223 | -53.18797 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bde3a80-6d84-3649-8e4d-319f26c7699f | -8.16974 | -46.17061 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b362081-49b5-3493-8d2c-4de22a79dc11 | -6.30929 | -53.5462 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f471a490-cc1d-3478-b6e6-8439f4e61643 | -6.16526 | -57.78854 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c94246f1-f341-3958-8b80-1f821e6c53ca | -6.17674 | -55.46243 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 514d062f-68b3-3703-bd6f-50b5abf831a2 | -1.36544 | -54.63093 | 2026-08-28 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32dc3713-4e5e-39d9-b5ab-7701b2fd6145 | -6.27395 | -53.13812 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6abc3595-dedf-3622-aacb-0dec5c48d436 | -2.72911 | -47.03636 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3f24bef-38d5-3029-b1b2-e54667ca7c65 | -6.64631 | -53.1949 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f65eac6-b889-3158-b2b9-d3046e5f330a | -1.96303 | -48.37659 | 2026-08-28 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4275a30-68e5-3be4-adff-b23e6c4d809b | -6.31858 | -54.74061 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45a18835-58ac-3f6a-bea4-450360a5d69e | -7.25679 | -45.86249 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4afa1216-e0d9-36b7-bf39-6f1640b666f0 | -7.08749 | -42.80383 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6eef0929-31af-3e23-beb6-b858d3597d85 | -5.87062 | -49.7728 | 2026-08-28 04:49:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02dcaeb3-567b-3955-b10e-58c1d615ece4 | -2.72854 | -47.04 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d7196c1-ca37-3e8a-9fdd-4348f62cf862 | -6.32267 | -54.74134 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81b63ba4-520b-35a7-a6dc-401e48876f4d | -6.27566 | -53.14033 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fa4e3115-6132-34e9-8676-5c452a62bab7 | -8.07954 | -45.8157 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93d4ee17-ab0f-3e32-946c-9e6d40e89112 | -5.47051 | -45.1185 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab857a69-03ff-3f4b-ad63-796e97a34bb9 | -4.96206 | -56.27296 | 2026-08-28 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 692495bf-ca20-33df-8169-00b855d71562 | -8.17412 | -46.16687 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad2f6865-b68c-3622-af74-3877c23c9a13 | -6.75751 | -46.13691 | 2026-08-28 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b56cd8b3-cc22-35b3-b9c9-b197bbae183b | -7.28176 | -49.94802 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e99ae2db-e626-38be-9e1a-00987e15ad8d | -7.4473 | -50.92126 | 2026-08-28 04:49:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4995d5d5-021d-3473-8a5a-92b9815139ad | -5.89291 | -52.11429 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb32e6a0-5f73-39eb-ad1d-36f27855d7bf | -2.73138 | -47.04415 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17b9d753-67fe-371a-b81f-1bd186fb42bb | -5.29217 | -50.93689 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4dfcefe-83e7-3dde-bd80-28dceb5e5dbb | -7.25988 | -45.8676 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ee9903cf-9f99-3328-a25c-7f53ab3f2441 | -6.16272 | -57.80294 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fac65404-8dcd-3543-83bf-0d9eaa1bcb2c | -6.52806 | -55.24667 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f9ccab3-3dbd-3975-bcea-1ac897a09f0f | -5.87006 | -49.77627 | 2026-08-28 04:49:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e029fae-6604-32d9-a44f-7df5a6bc3d74 | -6.64704 | -53.19049 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9cc44fb-f78a-306b-9bdb-2c09c59acf1b | -6.90273 | -44.67298 | 2026-08-28 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bdd6e41-88f0-31e8-8bb6-344aea73c16c | -7.16646 | -43.16956 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2341b3e3-4d84-389e-a53f-851d6eb761f4 | -6.64261 | -53.19425 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13970a37-c068-3eee-8103-9793b15f7664 | -5.98805 | -52.19423 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbc1fc0d-1f5b-3bfc-b610-31b30dbe4f6c | -7.16002 | -43.16637 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09a399df-d0d3-395e-b95e-954204996fae | -6.24237 | -55.47609 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ed4a3f7-b766-3880-9b93-548dc59c7e2e | -8.06066 | -45.8653 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3427b4f8-1bdf-3b69-b465-521b283efcef | -6.93176 | -42.68067 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4baeedee-b3ad-3797-9bda-39c191019e9c | -6.41497 | -51.68137 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f72f5312-c625-3b57-8667-fe5084d5c4ce | -5.89356 | -52.11024 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 089333f3-ebae-3fc6-a1d5-58e727c2bc9f | -7.08816 | -42.79918 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 75a6e3fc-d67e-3cab-94d1-d909446526d9 | -6.26198 | -55.41285 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 28de5ecb-d051-34cf-b522-bbf8e1f9ca18 | -7.1015 | -42.83127 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ae9d409-538f-3d67-a679-bb51c98a1d66 | -6.28138 | -53.36902 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 210b5288-24af-3ab9-aaf3-568731862d51 | -6.25997 | -53.11966 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ccf48f3-6096-3b78-bb0d-785fefee7fa3 | -7.29317 | -49.25502 | 2026-08-28 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19b3cf25-c99d-31ac-b5bb-ff84fe7ae1f7 | -6.62853 | -53.18733 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8739555d-0a32-3a6e-8a76-ad6ec9576d1e | -7.2685 | -45.35189 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fb84e94d-f4a9-37e8-9699-940e98dfa8a2 | -5.47819 | -45.11972 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef97a8af-7c8a-3b1c-bb57-1d3142a41aca | -7.27361 | -45.34964 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dff059bf-4a6a-3384-ae02-bcb7c98d7a59 | -7.36285 | -46.66577 | 2026-08-28 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be2e2bd4-7327-36a8-a308-f2e1d6f8a234 | -6.50541 | -53.25491 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a7b374fc-721c-3782-923e-c2b2787ba0c6 | -6.63297 | -53.18355 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 838829cc-9766-3649-acf4-9aaf6a7d93c0 | -6.03425 | -46.75711 | 2026-08-28 04:49:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52b82785-b5bf-315e-8664-470ee6d36b93 | -7.25748 | -45.85793 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| dcaf11ea-6939-3275-ae71-32123c1986d6 | -6.23591 | -53.4788 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f042d01-d8a3-3caa-aebe-3a81914a457a | -5.47363 | -45.12378 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a076892a-836d-3ea7-be4a-f8ada1aee5a5 | -5.87789 | -52.18491 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58c76c9f-a70d-3c9e-80c2-36bd8370163a | -7.31592 | -42.96482 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7ebea89d-e264-30d8-9eea-a210cc627863 | -6.42577 | -54.93584 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6918de27-b114-3db6-9c52-7a375ee3483a | -6.24127 | -55.40526 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 043821dd-faae-38da-9fda-ed099e26e99e | -6.16878 | -57.79807 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71858e1-187a-36e4-a5a7-9489b7a55f6f | -7.3539 | -46.65167 | 2026-08-28 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3656f3fd-5c67-31d8-b8f3-ebd4dd23edc2 | -5.47544 | -45.12109 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee1465ae-f2eb-34b0-ba9d-61a68d39ef12 | -6.84188 | -45.0281 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43fe2588-38fb-3e77-a4da-410649428d2a | -6.26738 | -53.1209 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c535336d-dc88-3dc9-8b99-77b959962ef4 | -5.29158 | -50.94054 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c60f2a29-ea4c-3e6f-a6eb-97ad90f46ec2 | -6.06627 | -53.77142 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed58ef97-6a75-3bfa-833f-0eba0b7327a2 | -8.08931 | -45.85564 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea588355-6f09-325f-9ee2-240cbe152706 | -7.27291 | -45.35448 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52aa0690-8cf2-3222-b06d-430464a1a40f | -7.31561 | -42.96652 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c5226946-1ef6-3e48-b475-3c35f6dc8027 | -7.25611 | -45.86705 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 300bd4d6-0972-3eaf-9f0e-f77d29ffa1bb | -7.1626 | -43.16442 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4c288e23-1d16-37bd-94b7-8e358b6d9889 | -7.26401 | -49.84549 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54b4733a-ea79-3062-9d4d-6aa5abde5bbe | -8.1132 | -45.82574 | 2026-08-28 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f404cf66-7f66-3b85-bd4b-309bf5c18ef0 | -8.08851 | -45.80773 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 995cf0d3-313d-3d04-92c7-b18dce9d53fa | -6.1592 | -57.79342 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f57db21e-ef01-3f84-b53b-0a0295004f93 | -6.16374 | -57.79713 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e5eeb55-7fae-3daa-b729-5af9afe811ae | -6.23877 | -55.47125 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a55283c-10d1-3137-b90a-e0e5a8380b6c | -7.26776 | -45.35674 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5827122c-321b-357c-95b3-e194aac6f48a | -6.2316 | -55.93871 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f60f43dc-7744-3a8b-9ff7-e57888b0a2d7 | -2.71848 | -48.80244 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README32.md)
