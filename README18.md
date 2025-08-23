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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8bd85ca-e56c-3bb7-86f4-1cffb2271461 | -13.41963 | -46.26765 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 40e351d2-a868-3271-b540-fd65dbf40b17 | -14.9125 | -48.00237 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39910076-877d-3580-9726-c8bf893bf110 | -11.32429 | -47.84867 | 2025-08-23 03:40:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| adb38502-e3b6-395e-b279-252a705ee35b | -17.70245 | -48.51869 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca496314-bf5b-3df2-9bca-7a7a453f178e | -17.58481 | -46.5675 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 639e5e6d-b2fb-333b-bdd4-1124a1fa8a27 | -17.58859 | -46.56844 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8de43850-dd5f-3039-bf2c-917f5256e00a | -11.97262 | -46.77905 | 2025-08-23 03:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f7e4eb7-c9f0-3772-9fdc-5e295f2b8363 | -14.81036 | -47.94548 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cff65503-a63a-3cf5-b15b-366a8160d63b | -11.13332 | -44.77355 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 945a74a1-d550-340a-9e45-53cce3687e75 | -14.80153 | -45.43469 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbf6de62-2113-38bd-bc02-1d11fcc5bcaa | -12.94549 | -46.29762 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 295d1c2e-613b-31d0-a8a7-762b073d6c62 | -14.80287 | -47.94889 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 877346d9-9b38-3d34-9f64-379ef916d2ec | -11.12277 | -44.76726 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aef02df4-acb8-3cde-b058-a6d6aa1f40d2 | -13.49358 | -47.03749 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a49b0511-6103-33f4-b4bf-3d3baf2b0ec9 | -18.25952 | -45.57822 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b101bba-c7e6-3ca3-9cef-ded81586a517 | -14.80535 | -45.45309 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c79b3032-9276-398c-b992-4332ba9e39a7 | -14.94917 | -48.01719 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 831b84ef-1592-353c-8159-84b96b2c5dcc | -17.59128 | -46.56487 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7af3a0a4-52d9-366b-8fed-eaa5fcf0829c | -17.69496 | -48.49361 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75c5b6c5-a0b6-3ec8-956d-409320f6f900 | -18.29974 | -45.54261 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 016cd7be-4134-3684-8337-3d28d6de311f | -14.81579 | -47.95077 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 35ee299f-7b0c-360d-b4d7-f773ff8c53f0 | -13.42054 | -46.26317 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 971918bb-0bee-339b-92d8-92d4bc5340c6 | -17.59419 | -46.56982 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67b97cf6-f711-30eb-9cd1-3f55488e7d6b | -17.5911 | -46.55649 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f309651d-a424-3c0c-b223-f93ed8967996 | -17.60062 | -46.56723 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad9d035e-9bd9-36fa-a5ce-665d8cbc940a | -14.90662 | -47.99602 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e151733b-4638-3cd8-b3ee-b9b76f27ddc2 | -18.25193 | -45.56242 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a07f890-1dac-3b45-9562-e0e3b4f55974 | -14.80214 | -45.44029 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8053e46-0132-35aa-8dcd-dd1ef69d2ea0 | -12.18634 | -47.21341 | 2025-08-23 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba8265a3-b2fe-3648-b645-58e4f0591127 | -14.47359 | -46.06169 | 2025-08-23 03:40:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 998d36ef-57b7-3ea9-839f-8e86a509ae57 | -13.4215 | -46.25844 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9ce0f646-39f4-38f4-8a66-7be53fc45d43 | -14.78287 | -45.47884 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 228d5964-983b-352b-bd39-7c3b8196ee58 | -15.20076 | -48.25019 | 2025-08-23 03:40:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86e1408f-7863-3b35-ae6a-f354290cf96b | -14.47447 | -46.05732 | 2025-08-23 03:40:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9c13cce-52a7-3b7b-8ae6-2a8c13433397 | -11.12427 | -44.75948 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2309c12f-9904-37ae-90bc-12a1c4164d11 | -13.04039 | -46.33015 | 2025-08-23 03:40:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3905e865-8f5b-3559-afaf-0ba362d7725d | -14.90632 | -47.99978 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2289f97-d59a-31d8-8983-07f9f10ed522 | -16.61739 | -49.41059 | 2025-08-23 03:40:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9e1adf6-b812-309d-b6c5-e5ad578aad60 | -13.38031 | -46.21694 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 909910e3-e07c-3c53-b501-30d8d6245517 | -17.26409 | -46.76969 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5c631ce5-2ae1-3c51-ae92-1ffc0707418d | -18.30355 | -45.55044 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f42cc1ac-b3d8-3327-9d1e-9cd16d23492a | -18.26923 | -45.58402 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dcfe852-9407-38a2-852c-2242a47b15fe | -11.05298 | -44.60284 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb003a8e-d438-39b3-93b5-918b0a500439 | -12.99961 | -45.22792 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 72107ab4-17cd-3552-a9a7-eb4addf16156 | -17.6979 | -48.49915 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c822dbc-8ddf-34c1-b038-7d8f99d5ec7f | -17.04865 | -47.1361 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f2d0b0b-0797-37bc-8095-0b13c973873c | -11.13556 | -44.76187 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7dcc1a7-0004-3c3f-881c-926c03f669b4 | -13.37695 | -47.48557 | 2025-08-23 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ec2658c-9368-3bdb-bc79-32621c2abbf0 | -15.70749 | -41.92715 | 2025-08-23 03:40:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4bc723e5-c27a-37c6-93e8-d10a70c82e20 | -12.99475 | -45.22281 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5e60835-b63a-382d-aaa0-ca26b33185c8 | -17.58634 | -46.55114 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7306ba0b-c464-3cd5-97b0-bd455deca4c2 | -13.41548 | -46.25751 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22c9ba25-7af8-33aa-8983-ef573bd1cc13 | -13.37595 | -47.49033 | 2025-08-23 03:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96d96745-4256-34bb-8795-19bdbedfde0e | -12.78677 | -48.72362 | 2025-08-23 03:40:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fd073bac-5a81-3f4f-8171-296b09e1800b | -18.25879 | -45.58167 | 2025-08-23 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f588266b-fbec-32cc-a5c7-6fda3ac0e56b | -12.94451 | -46.30242 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0f3193b-aa73-3e7a-9ae3-e6f0908a3cb8 | -13.47996 | -46.89737 | 2025-08-23 03:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a63ef904-8f3a-3dbd-87b6-a1329f831ab5 | -11.43825 | -47.33279 | 2025-08-23 03:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72fff872-8f03-3a62-9c79-c4968f02eab7 | -14.821 | -47.95792 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b28cc527-38dc-3898-9ddc-14ab4e7ed411 | -12.17991 | -47.21196 | 2025-08-23 03:40:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 930bf524-2f73-38dd-aecd-a113b36bdc6a | -17.58827 | -46.55163 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6cba1b7e-e901-379c-9df1-b742401c0d69 | -11.1201 | -44.75066 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5948869-0804-30c4-8517-e41ef9f349d4 | -15.19977 | -48.26001 | 2025-08-23 03:40:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e195442-20a6-3ad7-938f-680531ebcc57 | -17.58466 | -46.55912 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a7d84ad-60bd-3a61-a561-919c2e2868cb | -17.58298 | -46.56708 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8489fa5c-6282-3721-8f16-3b90d53637a9 | -17.6938 | -48.49865 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2633de49-e767-3506-9627-b073214d62b6 | -14.82837 | -47.9549 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47e88ca1-3c83-3021-9e45-addc80602df1 | -12.67518 | -47.81428 | 2025-08-23 03:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 377bd42a-2cd8-3da0-9a24-4d3536fa4c7d | -17.69905 | -48.494 | 2025-08-23 03:40:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39ec6312-83da-3ad3-b506-af883aa00daa | -12.98913 | -45.22162 | 2025-08-23 03:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90378ec2-6ebe-31dc-a35b-8a3ceece3d50 | -13.3714 | -46.22166 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 56ed62c7-7cdf-30d5-ae68-2e51168c01b3 | -14.90134 | -47.99154 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55baeea0-e5d4-3981-a774-f445d8f186e3 | -16.23893 | -48.7626 | 2025-08-23 03:40:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73993e48-6aad-3cd6-95d5-a50c3026103e | -14.92263 | -47.32319 | 2025-08-23 03:40:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2173323b-11ae-3765-be9b-2c118682e244 | -15.56193 | -42.68251 | 2025-08-23 03:40:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a72d1fd3-1dc3-3d10-b8e1-4754b510f558 | -14.94301 | -48.0145 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f128108b-8747-3ec1-8223-76fb308f1340 | -15.1996 | -48.25546 | 2025-08-23 03:40:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb0720d-9d0a-3ecf-bdcc-af0ccb580da1 | -13.40639 | -46.24116 | 2025-08-23 03:40:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e73fa589-7249-3716-9383-5998732f1717 | -14.81089 | -45.4542 | 2025-08-23 03:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780282c7-cf12-366f-986b-f0c23a2dcaca | -17.32529 | -46.56784 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| acc8bcdd-ee9a-3e95-b3b9-fa5b74d69ae7 | -11.13929 | -44.74248 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67c5d073-149c-315e-99b6-83336c7cbda8 | -14.90759 | -47.99382 | 2025-08-23 03:40:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f299784-8f00-38a7-8644-0ffbb4a71e9a | -17.31965 | -46.56655 | 2025-08-23 03:40:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6443247-c59d-3b1b-95d7-fcc5afe3c6d4 | -17.5874 | -46.55561 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6523521-ec20-3ca6-aa97-894d63a8071d | -11.12687 | -44.7765 | 2025-08-23 03:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 513028a2-0168-3563-919f-7d053dd332b6 | -17.59214 | -46.56091 | 2025-08-23 03:40:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb085f2a-daad-3c0e-a165-2d5bafa69cce | -19.43904 | -42.54576 | 2025-08-23 03:42:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8c7968e-98e5-32dd-a6c9-ab986944372d | -21.85238 | -41.40264 | 2025-08-23 03:42:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba8e060c-629c-3fd1-9974-1719d5fd0f29 | -22.6298 | -47.43273 | 2025-08-23 03:42:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eadbc90c-71b3-3670-833e-67292f9a9dbc | -20.27925 | -46.64896 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3488b897-8f29-35c4-8277-9784952d9559 | -20.27557 | -42.83057 | 2025-08-23 03:42:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| aaf16794-c085-38f8-b2a4-5a1952437a82 | -20.35544 | -46.54028 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 954af3de-7937-3633-8bf6-d45e179b307c | -22.74183 | -46.54654 | 2025-08-23 03:42:00 | NPP-375D | PINHALZINHO | SÃO PAULO | Brasil | 3538204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3379c060-c5d5-3049-ab0d-8cddfac2c942 | -22.17863 | -43.28498 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b56fe23a-a495-3678-9645-d406bb7916eb | -22.09702 | -45.02447 | 2025-08-23 03:42:00 | NPP-375D | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 62a9c512-6fe7-3012-8523-ff633e218b2f | -20.27768 | -46.6826 | 2025-08-23 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae3ce488-941c-34ff-852e-8a87a519b18a | -20.44464 | -42.11879 | 2025-08-23 03:42:00 | NPP-375D | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3d2d5859-283c-3f9e-b33c-569986d58804 | -22.17313 | -43.27254 | 2025-08-23 03:42:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 56a5e439-b153-355d-b81a-45f6fbff3391 | -20.09134 | -47.76146 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 735c9dce-0d6c-3f5d-a21b-87abbf93a88f | -20.0903 | -47.76606 | 2025-08-23 03:42:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
