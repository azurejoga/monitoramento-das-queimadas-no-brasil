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
| 4ba35e7e-af6d-3327-b29c-86e8c3e9087a | -11.63266 | -56.85981 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61fa6179-5878-3bb2-9658-cb62fbd2ae18 | -8.87738 | -48.49819 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38a48519-90b3-3763-800c-5d9ad009528f | -11.47631 | -52.92022 | 2026-05-29 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c53ae3c-ee26-30ff-aa27-a9625aa04b26 | -11.59583 | -47.44622 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 76c9f9ee-3ce1-3316-b8ce-d29292d99e4e | -13.71199 | -50.69025 | 2026-05-29 04:55:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d050c5df-3ae1-3c55-9f9c-2be11e049f05 | -13.6432 | -55.75612 | 2026-05-29 04:55:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c39c348-3398-34fe-be37-0019372dc91d | -11.7782 | -52.51321 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ed2c03-caf3-3e7f-a5a3-03a7782d1b97 | -11.4687 | -57.1069 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb95cf9a-627d-3702-88e4-1204b38e83fc | -11.30029 | -54.03031 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 027e2c15-3718-31ca-bbd6-5fbbd21f7586 | -8.68341 | -48.301 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5d6a0a4-b740-364a-a462-44a2186a2807 | -8.22483 | -49.67005 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02bbaefc-dc41-3a6f-98a5-315fc54ee169 | -11.58777 | -47.44507 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f55c80ce-1b09-3344-8e03-d780be2d3457 | -13.18081 | -52.70517 | 2026-05-29 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c75bea4-0cd8-3836-8e0c-617ed97c553e | -11.56392 | -54.57885 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1d28bcc-007c-306a-99fa-9627df2b622b | -8.6895 | -48.31079 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d158307-2c45-3243-95a6-a003f75ce3eb | -8.68213 | -48.30967 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b261b7f8-d1e5-3376-a9e2-20f185914d05 | -2.96576 | -39.9272 | 2026-05-29 04:55:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15e38808-bf4c-36f3-ae19-7a8dc1d992af | -13.11756 | -51.72316 | 2026-05-29 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecb9d4b3-6ce8-325f-a192-d156464cb5d6 | -13.18025 | -52.70872 | 2026-05-29 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3ac514d-e595-3d4a-b66a-9537b39bee7f | -11.4696 | -57.10178 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37e538fa-4c0d-3c9b-ab87-68a1dfef0ee3 | -10.65765 | -49.72698 | 2026-05-29 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76fcc070-679a-364d-8a04-01e913801364 | -11.827 | -48.21311 | 2026-05-29 04:55:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26df84d9-677e-34e2-b016-bb13644bbee2 | -11.79315 | -40.0849 | 2026-05-29 04:55:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 763de9cd-b364-38a5-a60e-042732c6d1ce | -10.13169 | -52.40091 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af9cd0f6-3403-384e-b8c6-7580ae66e00d | -8.68645 | -48.3059 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23051a10-c441-3cc1-abce-516dd667f2af | -8.71844 | -54.99343 | 2026-05-29 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e94c412e-cf63-3e87-bd01-6953f3ec4e63 | -9.21688 | -47.91938 | 2026-05-29 04:55:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a394bf81-788e-35b8-9a88-d61865eab20e | -9.76129 | -50.01086 | 2026-05-29 04:55:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 415358c4-d48b-3138-8bdb-e6910dce32ad | -10.65825 | -49.72304 | 2026-05-29 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49734160-511a-3cb4-b95b-7f1f147b72c8 | -11.0499 | -49.60342 | 2026-05-29 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fffa3fe1-ccae-3e78-bb47-760c07bdfd81 | -2.96638 | -39.923 | 2026-05-29 04:55:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d6058f55-9ad7-33f3-8a21-e0c4f9b6aafa | -10.66177 | -49.72358 | 2026-05-29 04:55:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d6d557d-e879-353c-8841-a32b41d2bd72 | -11.04635 | -49.60288 | 2026-05-29 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b8654a-cef9-3087-966d-f9b6db5260ce | -11.58727 | -47.44864 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf63f72a-0c03-3f69-a985-d77c3d68dff8 | -12.00239 | -45.35662 | 2026-05-29 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19aef9b7-0b64-397e-9f45-6771fedac091 | -8.72149 | -47.83134 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83039eb3-4ab0-3274-ba67-9bf2692b4ed6 | -11.74614 | -54.78782 | 2026-05-29 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd26b622-87e6-34aa-8296-812ca92cd6ad | -11.16561 | -46.79922 | 2026-05-29 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16042809-6099-3278-9a6c-4b8bfa337181 | -10.9787 | -48.15341 | 2026-05-29 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ace8a920-981e-3110-8688-ebf986cee9e8 | -12.01171 | -45.35792 | 2026-05-29 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd2b20ad-711b-303b-8042-bdef23cddba6 | -11.97005 | -47.37082 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c3e57d9-856d-319c-8212-389af120a384 | -8.52733 | -51.57634 | 2026-05-29 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70c58ff0-ca7a-3ead-99f5-d0f9d089f428 | -10.49076 | -55.60569 | 2026-05-29 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ad91000-2f47-3500-a01f-213ab88f7538 | -12.9948 | -57.77898 | 2026-05-29 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee7b6c63-e71b-3e32-ac1b-bac1d0fdb8cc | -11.69176 | -45.38665 | 2026-05-29 04:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86fcaaae-92e1-3e17-adcd-06db8d903249 | -10.51726 | -48.10538 | 2026-05-29 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9457ab8c-f672-39dc-a798-ea6f7a9be5b5 | -11.89606 | -47.60622 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6b00af4-ec4c-37f2-b2f4-1a3660496f81 | -8.71162 | -47.79955 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b12bf299-3a60-38ee-892c-e784cd62a02a | -9.21309 | -47.91879 | 2026-05-29 04:55:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfea4edb-ee1c-3c44-8528-1dac08a315af | -11.94312 | -43.39911 | 2026-05-29 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1cd143bd-292f-3564-a93e-5e86451257d7 | -13.63846 | -55.75405 | 2026-05-29 04:55:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb38b32-29b8-381c-baa7-bba40b90431e | -9.95434 | -52.45546 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0096ee6d-1125-3166-a17d-e78245b04f9a | -8.88881 | -51.87704 | 2026-05-29 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 160fa994-a3c6-35b7-a13b-6e7b83187ab2 | -8.24142 | -46.36403 | 2026-05-29 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07e26689-4bd8-3a4e-a718-1bbc1deaa282 | -11.9427 | -43.40245 | 2026-05-29 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 129ec506-1d57-3878-8670-ee41134a74c9 | -13.63964 | -55.75548 | 2026-05-29 04:55:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59a015f1-1b4b-391d-b7e9-7b9a0a8846da | -10.12836 | -52.40037 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3498989-abe7-3dbe-ae21-50d8f2d4775e | -11.83136 | -49.79371 | 2026-05-29 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea256c85-b82b-3457-b24b-1639a8b8edb6 | -11.29688 | -54.02973 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7329551-c2b3-3483-911d-e1eec5047430 | -12.99015 | -57.78178 | 2026-05-29 04:55:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5943fa43-3379-3c00-bff6-a63f3402ff2c | -3.27376 | -49.13917 | 2026-05-29 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cf7ab8e-409e-3eba-9e1d-b52abf9db181 | -10.13113 | -52.40443 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0edb46dc-6945-308e-8364-118ea924cc02 | -12.36439 | -54.16774 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d591abbe-6000-3d8c-93c0-905d7c97f0ec | -11.59229 | -47.44206 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 203cd45c-3122-3a47-a278-f0285edc75ff | -8.72261 | -47.82946 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f151a8ad-f118-36f9-a513-c0e718d96992 | -13.11419 | -51.72263 | 2026-05-29 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e2140d2-18d5-3a69-ada0-05529b7aaec7 | -11.56045 | -54.57825 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe8fa27a-51d4-36c7-9407-7de0ac7e7294 | -10.97487 | -48.15284 | 2026-05-29 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98d04448-f87e-3cd2-b878-0fcbc2f95e16 | -7.5066 | -55.00581 | 2026-05-29 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4134cc97-55ee-3f4c-abb7-bb757cb673c5 | -11.58876 | -47.43787 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f89fd2de-8bbf-3807-b3cb-17b34751ae68 | -12.36039 | -54.17086 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1d2769c-5c3c-38d0-a6d4-e70ec6dcda56 | -11.56044 | -54.58517 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c71728b7-b3bb-35e6-900e-a7ccb646b071 | -10.98262 | -45.09508 | 2026-05-29 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0d235521-17b2-3e05-aacd-fb5bd3a389a2 | -11.33304 | -51.40147 | 2026-05-29 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30a9ed95-505f-376d-af00-6904c0b71cf4 | -9.95101 | -52.45492 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8e6c30d-e830-3d41-922a-701671cefc8b | -11.63179 | -56.86472 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eab6703e-9cea-3743-9c05-2388a151c7d5 | -11.60085 | -47.43963 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 10faaf73-bbad-3b16-bee8-5058afcc5be3 | -9.14924 | -50.04527 | 2026-05-29 04:55:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e89bcae9-51bf-3cd4-a582-6a761525245c | -8.70783 | -47.79895 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebf2b111-9b87-35ea-9939-c3e6db5f9e05 | -11.69241 | -45.38178 | 2026-05-29 04:55:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 396d1bd4-8f0f-3378-a722-55be46fc7021 | -10.82602 | -46.8933 | 2026-05-29 04:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a641dec1-9eff-3f98-ba88-adadc4778133 | -10.04615 | -51.66037 | 2026-05-29 04:55:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9c104e0d-e20f-3f5e-a903-bd044098374e | -8.89213 | -51.85607 | 2026-05-29 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc6e8c2b-d16a-33de-bc05-158b8cca8d06 | -11.80062 | -52.5167 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6567c80c-3cdf-3229-a794-94c0aefe062a | -11.55982 | -54.5821 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74fc348e-669e-38d2-91d1-e37dfe9b9a6f | -11.56109 | -54.58131 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 873d9515-7f31-3981-b981-779712556fd5 | -11.79396 | -52.51561 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 708c87b2-e251-3a34-af88-fb277927c90b | -10.7165 | -49.03462 | 2026-05-29 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcecd949-fe29-3833-ba6e-1ce3672ecfb8 | -10.47889 | -48.90859 | 2026-05-29 04:55:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a30927b-a71c-3c87-9300-29cfa9cb4217 | -10.87319 | -53.7363 | 2026-05-29 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c7a9869-92c0-314c-87e4-295cd4dcbd2e | -11.33249 | -51.40506 | 2026-05-29 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cbfa498-5e38-351c-a58c-561dd463360a | -11.16091 | -46.80237 | 2026-05-29 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53a2086c-7e89-3514-996a-9550ac755b95 | -11.7399 | -44.51511 | 2026-05-29 04:55:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e425aad-bf1b-3e23-a236-e351e63d4917 | -8.84848 | -46.71105 | 2026-05-29 04:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf9a08e-9cb4-3bcc-bc45-4b4cf7628545 | -9.16139 | -46.86165 | 2026-05-29 04:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d0b4ada1-25a2-3d07-ade0-50a73dcc36c0 | -8.68581 | -48.31025 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6088fda-4349-3c56-b736-cc8f6bb69225 | -13.17692 | -52.70817 | 2026-05-29 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e300792c-a24a-3dc4-bffc-fb705b9bbc35 | -13.18748 | -52.70627 | 2026-05-29 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a8ebb56-4e85-3cb9-99c3-4151d6303c68 | -10.62763 | -46.89702 | 2026-05-29 04:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3644d39d-e432-3d6c-8d24-4046aa4055a8 | -10.52108 | -48.1059 | 2026-05-29 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
