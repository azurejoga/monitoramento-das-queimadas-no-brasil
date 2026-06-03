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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abfa5f5b-2935-3890-b76c-60d8d7ae877d | -11.80075 | -47.32935 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a31f66-0991-32ce-83b5-60f50367675a | -8.87559 | -48.50229 | 2026-06-03 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e6683be-b2ce-3ef9-bdd0-83c8c8bfd0a3 | -7.27478 | -46.80894 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2d3e167-a408-3d4e-a578-a0fc73362c01 | -7.59803 | -46.46383 | 2026-06-03 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bbfaabf-73a7-3d02-9cef-944db8877501 | -7.27093 | -46.81189 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a89e2fa-abba-35c0-bb7a-899f8cf81acc | -11.8035 | -47.33338 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a62b30a-61fd-38d2-8786-b9eea4ba5475 | -9.18284 | -58.05742 | 2026-06-03 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6cc3a9aa-41df-3458-8891-22343850ee5c | -11.13874 | -45.14526 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 35b6a7c6-134a-30a2-93fd-60aa0876afe1 | -7.95333 | -46.84687 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79f345ba-2688-39c0-a8a5-26cd9d38b686 | -9.182 | -58.06192 | 2026-06-03 04:27:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f8f50308-3fce-3512-8536-23a0091aaa84 | -10.55222 | -46.6272 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90d068e8-96dd-323b-bb40-c4d535925672 | -10.21095 | -48.25914 | 2026-06-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f99bfa38-fd34-3598-9467-5cb1af9f55f2 | -11.99763 | -43.78491 | 2026-06-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b63ecbdb-554b-3109-945f-96c3ede10e3b | -8.87957 | -48.49915 | 2026-06-03 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 518ca2aa-5483-3197-afa3-232eee9ffcb1 | -11.57038 | -54.58042 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b67a1240-9423-383e-8c85-0c9bd62e47fe | -11.57589 | -54.57642 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b6a6efd-08db-361e-aa24-6743492c369a | -9.93051 | -48.69454 | 2026-06-03 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c6e8152-9c9d-3783-9bd8-8518eff86954 | -12.73176 | -54.21123 | 2026-06-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2b5041c-b5dd-38ee-bb67-2c84dc2263fc | -7.27039 | -46.81536 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83b9c2bb-5fea-3187-a8e7-cd7761e3cfce | -11.95251 | -49.29962 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4851d31f-faaf-300e-a7c8-6203ff1be84f | -12.08791 | -48.41995 | 2026-06-03 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d83e93f5-7d77-3414-854c-01bd13887f4a | -9.0879 | -48.64972 | 2026-06-03 04:27:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb30390d-4fcc-3d07-b059-ce83b0539ed1 | -12.00434 | -45.35477 | 2026-06-03 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d22e480-692d-3928-8712-7d561f775a46 | -11.62768 | -55.179 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3f6a189-e735-368d-b75a-8a89f8597991 | -8.9812 | -47.98311 | 2026-06-03 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f897ac2-875a-387e-8463-902d1777f3ef | -11.12788 | -45.12401 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fc288d9-1b4e-38b5-867f-543e9934e979 | -9.0873 | -48.65339 | 2026-06-03 04:27:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9acfc2df-a332-394f-a7f4-20744dcbd94e | -8.05141 | -46.19197 | 2026-06-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e81da59-d3a6-34c1-975d-428292c40c1c | -11.99301 | -45.14985 | 2026-06-03 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dc0e2f9-80d6-3abc-ab38-74e767b13c41 | -11.04913 | -54.19587 | 2026-06-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76c77e15-a28d-3263-bd62-3d3a5e52ea89 | -9.09071 | -48.65394 | 2026-06-03 04:27:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 405507ce-cc97-3fe3-868e-94e199391504 | -12.45425 | -46.50752 | 2026-06-03 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe1575c6-a914-3a39-8a83-ab42dffda7e8 | -7.50781 | -55.00312 | 2026-06-03 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 494f4645-a6a8-3de2-93f3-438e34591fdd | -12.30206 | -47.90659 | 2026-06-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f813bee4-e658-32fd-92a4-cdaf3210a3ea | -7.27423 | -46.81241 | 2026-06-03 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b90027e-4b10-3738-baf7-bfad757b37e9 | -14.04751 | -46.34584 | 2026-06-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 414daf27-2332-3dfb-a20c-abe49b5fe1f1 | -12.73781 | -54.20309 | 2026-06-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a650b5c0-950c-3dca-ac57-e2c135762d45 | -12.89339 | -49.50164 | 2026-06-03 04:27:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65d1f9f8-b2b5-32bb-89ef-04c8670065b8 | -12.81054 | -54.86282 | 2026-06-03 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52cd1e32-95f3-3310-a93f-f19f32e47ed9 | -8.2066 | -49.84047 | 2026-06-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9aca243-3461-3278-9320-df0c6e6397fa | -13.96472 | -46.03093 | 2026-06-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d38f4678-1451-347a-a878-1ad8d1e8f294 | -11.99534 | -43.78155 | 2026-06-03 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca0c7a7a-ac3f-3639-938e-970832de6795 | -10.87168 | -53.73893 | 2026-06-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c2e4900-479f-3f35-a8a3-5143bacaf9da | -12.73863 | -54.19865 | 2026-06-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d77b4ad5-066f-3c6c-8586-8398fb466954 | -12.0049 | -45.35097 | 2026-06-03 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 550c7010-1f7d-3b14-81b8-93d225563581 | -10.81806 | -56.59573 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3b5aee5-847c-372a-adc5-fbfbe0b0f25d | -11.75903 | -47.07105 | 2026-06-03 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c22cea8-4201-3d95-a192-6fda2efea70b | -10.98085 | -45.09833 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcda988f-1629-3fb6-a4e3-f78668f9f5e2 | -11.56856 | -54.5903 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 119eb932-cdad-335e-be7e-acc8712335af | -10.57293 | -57.32436 | 2026-06-03 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f76c842d-88de-377b-a3f4-56e9ffcdf976 | -11.75519 | -47.07403 | 2026-06-03 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dd187978-561a-3710-b324-5cd811467ec6 | -10.54177 | -46.62914 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a3b171d-ef4c-3f2b-a1cc-bbb85f1f4850 | -9.0913 | -48.65027 | 2026-06-03 04:27:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be5aadac-5b8a-3acd-a57e-7428769edfc9 | -11.2706 | -53.96616 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 364ed596-7fea-3534-aaad-3896afa7fbb8 | -10.55998 | -46.64275 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cf73906-e633-3b49-8ad9-69f54e26be07 | -12.73734 | -46.96796 | 2026-06-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54e2fde9-8955-3b36-af9e-81a998543483 | -10.59721 | -53.47355 | 2026-06-03 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36bde57c-254b-3786-b405-63fa8ae5f7e1 | -11.8002 | -47.33285 | 2026-06-03 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| abb6194d-0503-3a6b-9ba8-2a37933c29be | -10.54231 | -46.62565 | 2026-06-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4ff1a863-03b3-3187-8366-7a5e88bf8d85 | -11.56669 | -54.5746 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc01dccd-b6df-380f-89d0-3064aeb2af52 | -11.13588 | -45.14089 | 2026-06-03 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17e15977-c347-3b7e-b235-8163ac5580bb | -9.80225 | -48.9258 | 2026-06-03 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c3ec56a-dbc2-305d-822f-6e2c9239580c | -11.57088 | -56.34093 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06aae655-437f-341f-a876-987571460757 | -11.5727 | -56.33141 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1c8bcbf-5754-3a0b-be85-083bc2f4a3d9 | -8.05033 | -46.19888 | 2026-06-03 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9a685973-1a2d-36cb-a9c0-e6bcef73e4a7 | -11.79544 | -54.02251 | 2026-06-03 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7c828fd-a837-345d-82e2-4d9d67f03421 | -11.5715 | -56.33772 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b9ab692-47f2-3383-ba3b-5d4fdf323239 | -11.95069 | -43.39846 | 2026-06-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95caead7-b9e7-3990-87b8-ee70aee57dcc | -10.63285 | -48.32429 | 2026-06-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b053750c-be3c-352d-90a8-4f58260219d9 | -13.95843 | -46.19138 | 2026-06-03 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae78f808-285f-3cf2-b25b-0a7f5ee7e16b | -14.05089 | -46.34636 | 2026-06-03 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc78a8b5-4b72-3950-b6a8-08d9072a1397 | -11.57788 | -56.33244 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f160c323-47fc-3f2c-8492-9e86a86d91dc | -13.5115 | -54.31525 | 2026-06-03 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9411061-3417-3623-988e-737b1583dffc | -12.01566 | -45.86129 | 2026-06-03 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75ca5ba9-d894-33cf-8d97-95c8039be310 | -11.32878 | -51.39511 | 2026-06-03 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8303defb-2035-34a4-b242-42e5fd6077f9 | -12.32684 | -47.89981 | 2026-06-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 532476db-913e-3bf9-8e59-157987ac39ba | -11.62572 | -55.1897 | 2026-06-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2c410add-3531-392a-a537-5e0609ee9962 | -9.89095 | -52.44099 | 2026-06-03 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7960cd30-29ba-3411-8f33-8588264d4994 | -11.56947 | -54.58536 | 2026-06-03 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 091e90b4-13f0-3cba-a1df-e620d06a922c | -8.75763 | -39.82769 | 2026-06-03 04:27:00 | NOAA-21 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fce945cb-e2d8-381f-987f-e261313a9165 | -11.75464 | -47.07753 | 2026-06-03 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c577ee18-70c2-31d0-b04b-b656b9adf8ad | -11.9538 | -43.40374 | 2026-06-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ea920f8-a9c5-3526-91c6-e1e4bbe91d77 | -11.57667 | -56.33878 | 2026-06-03 04:27:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81c7eaf5-60f5-3405-a842-0273767044bd | -12.92771 | -43.62504 | 2026-06-03 04:27:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9182294a-d8b3-3a4b-9ff6-9fcd2ab505ac | -11.84885 | -46.6419 | 2026-06-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 802e77cf-91e1-3f17-9562-e3476584b1b9 | -11.85494 | -46.64648 | 2026-06-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11e2cde4-f302-3329-8f12-c7d1759490b5 | -12.01622 | -45.85762 | 2026-06-03 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 632fb644-bc43-3b26-9d9c-b522cfbe342d | -10.14792 | -47.77607 | 2026-06-03 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed9a3d8-cead-331f-9185-33dea8a24dee | -19.16558 | -55.18337 | 2026-06-03 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2aece8de-c4ff-32bf-86f5-faed1f9440f2 | -18.46469 | -54.70528 | 2026-06-03 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 999d0b1c-c514-3520-ae7d-941ab0f95e14 | -18.77958 | -48.03763 | 2026-06-03 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c6bfdaa4-2aff-3686-a5bd-396d6bd623b5 | -17.44426 | -42.631 | 2026-06-03 04:29:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 752d295d-2d68-35dd-a7ab-9a42aac490b6 | -15.2331 | -48.56896 | 2026-06-03 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f19eb55c-0236-3bef-b326-be6709239df0 | -18.46397 | -54.70913 | 2026-06-03 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a764d340-23aa-3e76-8615-7510fddadf92 | -18.61894 | -49.19376 | 2026-06-03 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6859e6bf-b2e7-3e1c-9bdf-cd2fa142553f | -19.72115 | -40.15975 | 2026-06-03 04:29:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 16767be0-7462-3030-b8fd-0fbd4e8302f5 | -16.58316 | -45.87847 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 299bcfaa-d58c-30f8-9ab4-8c7ea3d07fa3 | -16.57832 | -45.87926 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddb277ca-f402-3e62-b3b7-045d1f335c6b | -16.57891 | -45.87521 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72fe369a-8676-311a-9c8f-b2baeb48c599 | -16.58023 | -45.87386 | 2026-06-03 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README6.md)
