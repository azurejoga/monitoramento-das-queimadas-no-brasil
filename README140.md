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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d289f5-c61a-354d-9620-00b47044ee07 | -11.10208 | -49.85088 | 2025-10-04 12:19:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f94bb610-a0f9-331e-84b0-7288693ee0a8 | -13.01561 | -44.91669 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c30997a0-abd2-3fc8-97f4-edd0f2e97bc8 | -12.0861 | -45.16211 | 2025-10-04 12:19:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 781c3942-8968-3f4c-8a4f-33b27edee243 | -14.04786 | -53.92963 | 2025-10-04 12:19:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| f8c6dbaf-5bd1-3708-be02-70a1d41919a6 | -14.38748 | -45.9727 | 2025-10-04 12:19:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 59602bc4-b6f6-32fd-b66e-15471e9d0f6c | -15.61769 | -46.94252 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| fdae567e-ee48-3c26-9b3a-9102ff15500d | -13.23815 | -48.48612 | 2025-10-04 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| f86d070f-35bf-3f2e-9840-7a8a14db1b25 | -11.11234 | -47.75397 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a36dc739-cf7b-3411-bbaf-9dd746ad79ba | -11.12947 | -47.18554 | 2025-10-04 12:19:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3ee7a169-b4f2-376b-b6a8-27905025a2d9 | -9.29239 | -45.95581 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1a610231-8c85-3917-8836-59b419317141 | -8.89667 | -47.25597 | 2025-10-04 12:19:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1d59b622-7945-3dcc-91c3-3b1dbe6055c1 | -15.24184 | -49.29717 | 2025-10-04 12:19:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0439de97-9cc3-3a50-ac06-0e2755fe2ced | -9.3391 | -47.32255 | 2025-10-04 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 46aa688e-4af6-36a6-ba63-0eb157b81581 | -13.18447 | -50.95956 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 395da2da-1d17-3bd7-aaa4-a0a1f68e3106 | -11.74224 | -46.81839 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5d7396ac-2e7f-39c2-b4c2-8b04bdb21945 | -15.61907 | -46.93217 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c0c8a8c5-410c-36df-ba5f-622971344550 | -10.19282 | -45.49754 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 54f58a1c-73b2-3303-bd24-88bf4c6db766 | -13.19236 | -50.97158 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 425.9 |
| 5db269ca-d430-3102-8431-54f0e5d3e406 | -8.91616 | -46.60836 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e3dbf30b-5a97-384a-85c6-8a3625ddecdc | -12.95166 | -50.99051 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 9196c947-0b6a-3bde-94b3-b5544bbbbd54 | -14.32729 | -52.90374 | 2025-10-04 12:19:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 598ec667-337d-3616-9a02-8fe76234180c | -13.35149 | -47.23296 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d942cb6d-d126-3af8-94dc-1b8e2714987b | -11.93038 | -46.39046 | 2025-10-04 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 853afee0-57ee-3a1b-9a26-1bdccafa9a1a | -13.39071 | -47.54894 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7b783fb6-ad3b-365c-978d-5604b80d4347 | -10.02408 | -48.26731 | 2025-10-04 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 63a5ce7b-d622-3f5c-a1f2-286349e72a56 | -13.32407 | -47.62738 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| db0335ba-4187-363f-9014-1db990b7773b | -12.19778 | -47.77295 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6a9be21f-55b1-39ab-8efe-ca8db6c8799b | -9.96066 | -48.76588 | 2025-10-04 12:19:00 | TERRA_M-T | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a780dd11-dc50-3bb6-a4c0-bd2dc6b1812b | -14.20896 | -46.07974 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5b3f6136-4365-32c3-bb0a-bf21841ea4e3 | -11.79018 | -47.91924 | 2025-10-04 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 565b96c8-a0eb-3fc0-bfc8-f6ffbbd5618a | -13.28324 | -47.59361 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8216fa45-951f-3abd-8c4f-a98f31664d30 | -12.8823 | -47.29704 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 51f5e669-9ed1-3db9-a751-5a6ef5c036d0 | -18.34319 | -44.1799 | 2025-10-04 12:19:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 01c07be9-bae5-37bc-9d3e-767ba777809f | -17.25397 | -48.10567 | 2025-10-04 12:19:00 | TERRA_M-T | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 202e7150-b02a-3fab-a574-ca35443a043a | -13.29982 | -47.60542 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 8dcf4ea6-329a-3366-9164-2321f97ed472 | -17.99431 | -45.01079 | 2025-10-04 12:19:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5d724ef5-6630-3dfd-836d-68e14b3e69b9 | -10.33656 | -50.33013 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 56b558db-9d4e-3ce3-9a53-4332eac5fe65 | -12.94211 | -50.98901 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| e3ec03d3-4c2b-378e-a682-7fa44da7c254 | -12.72102 | -48.56295 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 132.1 |
| e9fe9e4e-b1a7-30f1-b512-49b46ca262a4 | -9.68004 | -48.22039 | 2025-10-04 12:19:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 6a539bda-72a5-3756-83b0-f8bd18632bf3 | -9.36254 | -45.78806 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 7c99b0eb-be37-37af-ba2e-c4932eb2b0d9 | -13.12142 | -47.94977 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c6d0b604-77cd-32bd-b919-05ae53c0b983 | -11.82519 | -45.05049 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5d9ad176-ef35-3409-b348-2c6081db490c | -13.7469 | -51.31091 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5c095424-e062-3b5f-ab9e-ca9e7562d0f7 | -9.92161 | -50.50181 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 607e2687-cf68-307d-9fb9-0d43fc89a887 | -13.10126 | -47.90059 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8f0b961f-b9af-3a2d-b8c4-c570c5e14ba3 | -13.07487 | -42.17657 | 2025-10-04 12:19:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 01f23927-f2ea-3f1b-9af6-ebb48c583f91 | -13.82676 | -43.17756 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 7751b7f3-ac0f-3c8c-a50a-681e24b27358 | -18.31007 | -47.43225 | 2025-10-04 12:19:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| c16f0d20-61d7-35d4-a867-2a47bc2f6877 | -13.28197 | -47.60273 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fcdcf1c7-ba75-3408-abf5-b3f9241f757e | -9.39792 | -45.85838 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 32d760d5-0c9d-381a-bb0d-f3abca4de236 | -15.96354 | -43.34308 | 2025-10-04 12:19:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 9de1af81-020d-3910-ab31-f6546754eb4f | -11.89389 | -44.99538 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b9e7c612-cec6-375c-9ddf-f3dee43f74f4 | -8.95942 | -46.75313 | 2025-10-04 12:19:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 487b8e6e-6c0e-3294-81ef-28fd16e7e7b7 | -14.45961 | -46.33808 | 2025-10-04 12:19:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 87a4c3b7-0903-3bc9-9807-28a4da6c8e0f | -16.35658 | -51.47079 | 2025-10-04 12:19:00 | TERRA_M-T | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3107d3bc-0368-30ea-8074-7c77a28d5d97 | -13.34769 | -47.19359 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4a82d60-c473-3516-b4aa-164b7edd510d | -8.79498 | -47.71267 | 2025-10-04 12:19:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe74e061-c650-3503-b27e-2b57dc2def51 | -11.9746 | -51.48415 | 2025-10-04 12:19:00 | TERRA_M-T | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 035859a6-480a-381e-8a71-53e8acecb30a | -9.91653 | -45.96702 | 2025-10-04 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a5350684-6622-31ca-93d2-7bf7895db97b | -12.71972 | -48.57193 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d601c2f9-a97e-38cb-a249-b16d99b99c0d | -11.44697 | -43.89234 | 2025-10-04 12:19:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 27a05c90-668b-3e3f-8656-f6699890f7ca | -11.66169 | -47.00021 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2d984b45-25f9-3f9d-b04b-f7c1ba27f0e1 | -10.77981 | -46.58712 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 6bf694a0-b879-3a14-ba15-023355d1211d | -11.05417 | -47.7822 | 2025-10-04 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 91afba41-6214-3a5b-878d-846095e1f67c | -12.59169 | -47.00187 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6e7d1277-0af8-334e-8bda-ee9e8b8caa16 | -13.31392 | -47.56965 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0b11616c-cf3f-368f-97ea-e8e791442c9e | -11.01335 | -46.6955 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1fad55f4-243f-30bd-af90-f65bc68df75a | -8.97183 | -50.26719 | 2025-10-04 12:19:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 6c9fb942-4d24-32f2-b7ce-cf62766bd8a4 | -15.98993 | -50.91226 | 2025-10-04 12:19:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 21.9 |
| fad88e36-8f5c-3ae9-8a54-f35a50cb9c8e | -14.21857 | -46.08092 | 2025-10-04 12:19:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 9c0ae062-7914-31a5-bb57-024d27482341 | -14.16797 | -49.20744 | 2025-10-04 12:19:00 | TERRA_M-T | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8c5c2bc7-1eca-35c9-ba9f-627f33dc142f | -10.99142 | -46.52263 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| c6e264c5-a00d-3418-ad14-4d2ff3643c02 | -12.66045 | -46.96975 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b248f9f9-2f42-3ce8-9da7-3b233499b20b | -11.79985 | -45.01251 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8ba4a4c2-3c96-37b2-88e3-ef7d0b450fca | -14.89253 | -48.26579 | 2025-10-04 12:19:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3213fe92-2c3b-3fcd-8ce3-a8fe28dc9dc9 | -8.99336 | -47.49059 | 2025-10-04 12:19:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 6bb5927c-ea37-3b95-b704-ab78f552f308 | -12.5452 | -46.00014 | 2025-10-04 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| afba906e-2f48-3747-8e78-96c39b54722e | -15.53001 | -46.84095 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 27.7 |
| bac9be94-204e-3220-92db-be733de1c06a | -18.38002 | -46.56833 | 2025-10-04 12:19:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 20035830-25d5-3317-aa6e-358b51acb827 | -12.24418 | -47.84108 | 2025-10-04 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5dd9a8cc-cac6-3f3b-8b39-74dd92d41cb4 | -10.33813 | -50.31972 | 2025-10-04 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ff75d273-df95-310a-9aea-752950cd89a6 | -9.14537 | -47.77853 | 2025-10-04 12:19:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 59a876e2-b54d-3c68-9da9-e4365391f34f | -15.54076 | -46.83183 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| afa5a6a4-82ec-3ac8-bdfd-f66eacfa2d16 | -12.72232 | -48.55397 | 2025-10-04 12:19:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 24cde6a8-55f0-3df0-9924-5fddb5af77d4 | -11.16781 | -47.75879 | 2025-10-04 12:19:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 15de3849-db9d-33d1-89e1-7ec485f4e89c | -15.77643 | -47.47382 | 2025-10-04 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.0 |
| c3236fb1-c830-3f60-be87-0523147edb07 | -11.00526 | -46.68796 | 2025-10-04 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| bdb7cf9b-87eb-3777-bcf0-991d3797a0e8 | -13.52013 | -47.2786 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f8e704c7-ac5e-3bb1-b146-6431bb899011 | -15.34468 | -46.30273 | 2025-10-04 12:19:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6f0378a6-2e6f-3601-b938-8f89f3657651 | -18.89314 | -46.78151 | 2025-10-04 12:19:00 | TERRA_M-T | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| e85c3493-fbce-334d-869b-ecc7043e33e9 | -13.31514 | -47.62609 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b1e7966c-169d-3f31-9c00-129493f0ab37 | -14.67932 | -48.27824 | 2025-10-04 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 0da3ef7d-0209-3cc2-803c-708f246c8d06 | -15.53935 | -46.84235 | 2025-10-04 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 03782898-c849-3330-b95f-747e5ff371b6 | -13.32154 | -47.18351 | 2025-10-04 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56c4063a-27e1-31e5-9fc4-119973aef441 | -11.47942 | -45.03817 | 2025-10-04 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8981ec8d-d094-32b1-a6ee-39efc3b8b188 | -13.18285 | -50.97009 | 2025-10-04 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 57d26ad2-f8c6-30e7-a62c-596040b164bb | -13.49388 | -47.26849 | 2025-10-04 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1dad4939-035e-3c39-886a-8a8c89f9fbad | -11.50875 | -46.77626 | 2025-10-04 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| a363fca3-ce49-3f64-8394-ff6290bfd25d | -12.6501 | -46.97787 | 2025-10-04 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |


[Clique aqui para ver as próximas entradas](README141.md)
