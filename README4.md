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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2327074c-82f0-331b-8750-0799e6a1addd | -9.2179 | -45.3321 | 2026-06-24 00:43:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1942f5bd-b14b-32b0-a5b6-dc6c0394334f | -12.8723 | -44.366402 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9fbe42a1-c63b-3196-8021-be1a0f9ce5db | -6.588 | -43.912498 | 2026-06-24 00:43:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a16a9b2-b7a9-3766-b2bb-f4c14ebf2f8d | -5.7281 | -49.094398 | 2026-06-24 00:43:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f74d68f1-4998-3425-9b0a-a6ad90fddc6e | -7.5988 | -46.477901 | 2026-06-24 00:43:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 034ef4f8-5bef-3779-8492-612d7d3aa252 | -8.6818 | -47.855499 | 2026-06-24 00:43:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bf352e0-79f9-3ee8-ba48-5a6c4f1be1a8 | -9.1925 | -46.496601 | 2026-06-24 00:43:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9fa33e2-f98e-337f-a3c2-8a5d49a05230 | -12.6619 | -47.6758 | 2026-06-24 00:43:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d94a483d-c94d-3264-a322-032c8f52f7d1 | -3.8734 | -42.979198 | 2026-06-24 00:43:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9513c460-fa25-35c0-b2d3-de4d5f45a8ad | -8.6132 | -46.007 | 2026-06-24 00:43:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f68173a5-361f-3668-967b-92756f4dd501 | -3.8667 | -42.951099 | 2026-06-24 00:43:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0db31575-17ed-3e6d-b9fd-fe9aef505fb4 | -9.7488 | -47.8764 | 2026-06-24 00:43:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 52546120-6fc6-38f0-87cc-fe02bb6c4f25 | -8.8821 | -48.5051 | 2026-06-24 00:43:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fc5e3dc-2772-3bff-8c8c-ed1737bbddf3 | -9.5872 | -49.115898 | 2026-06-24 00:43:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53631826-38a5-3746-81b2-f1b14b0586df | -12.7794 | -44.4534 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09077043-c210-3c48-a7f4-d4f81e69c737 | -6.9894 | -42.8867 | 2026-06-24 00:43:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4f31b4b2-ee28-36f7-8e74-39069dc36e66 | -17.6134 | -46.692101 | 2026-06-24 00:43:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e669bf3-1332-3d4a-bef7-a2f3963e46de | -6.9992 | -42.884399 | 2026-06-24 00:43:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 03a9ca2c-5208-39f4-a92e-80394c4beaa6 | -11.6205 | -48.494598 | 2026-06-24 00:43:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2360ee94-1734-3afc-9827-deae203cbcad | -11.4869 | -46.732399 | 2026-06-24 00:43:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e83b8e2c-1b8a-3df0-9bd2-a5ed78d82817 | -9.4536 | -40.3606 | 2026-06-24 00:43:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b2fc2862-4fb1-3b9a-bb5c-455dc56c2520 | -9.4484 | -40.380299 | 2026-06-24 00:43:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 31ccd9db-e7f5-3e58-aa3e-c5f16effd92f | -6.5925 | -43.887901 | 2026-06-24 00:43:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7a53736-ae74-3e14-880d-1149fc4f2ddb | -17.2612 | -46.315701 | 2026-06-24 00:43:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57ad2e29-c9a7-39fc-82c3-6359913fd162 | -8.2708 | -49.3536 | 2026-06-24 00:43:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29fe2037-5764-3091-a66d-30c1c132ee4d | -7.9246 | -48.285599 | 2026-06-24 00:43:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dd2c189-11a7-3dd3-897c-8d70ab17db80 | -11.9699 | -49.230202 | 2026-06-24 00:43:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3764c98b-84d6-3cbd-912d-2065e9cb3c21 | -10.8018 | -48.563801 | 2026-06-24 00:43:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 810eda0b-b850-355a-96c1-239e45a55453 | -6.5978 | -43.910099 | 2026-06-24 00:43:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 579aac13-5331-3bfc-9143-a473e961a9a9 | -12.7306 | -49.0891 | 2026-06-24 00:43:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4d6353a-6453-3ef0-816a-362e8d460d3b | -5.8214 | -45.063999 | 2026-06-24 00:43:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 72940432-34f8-35a9-a894-6a625c6af37b | -11.5476 | -48.262199 | 2026-06-24 00:43:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91fe1427-47cd-3d33-92d0-f21d795e5728 | -9.925 | -53.283501 | 2026-06-24 00:43:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53f0c3e0-75ec-3679-83d2-eb4951a7722b | -8.3133 | -45.392502 | 2026-06-24 00:43:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| be68cb50-28b7-3705-841b-5e4378534a1e | -10.117 | -47.547901 | 2026-06-24 00:43:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff8f268-c12f-3d8d-8129-dc77f927fa88 | -5.7379 | -49.092201 | 2026-06-24 00:43:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e175abac-fdf6-3f27-bf3a-521c2248d0ed | -7.9164 | -48.2948 | 2026-06-24 00:43:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4585a293-5de6-30b7-a978-7987a00caeba | -9.9272 | -53.293598 | 2026-06-24 00:43:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b99b8308-a91d-3f36-94ac-d81dd7f9b77d | -12.8464 | -44.345001 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b0ad5d86-8dd3-3161-953f-87ea1fe88cc2 | -17.2875 | -47.033298 | 2026-06-24 00:43:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 94bebbaa-8993-3985-a1dd-9e16c740e36b | -12.5187 | -48.275002 | 2026-06-24 00:43:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3517741-e575-33c0-ac9e-9a63df18891b | -12.8269 | -44.3498 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f98d01c0-205f-3787-a37b-9d5989576dbc | -12.5171 | -48.267899 | 2026-06-24 00:43:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98068ad9-8eba-363a-af13-90c085e97906 | -6.3569 | -43.594299 | 2026-06-24 00:43:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee67b9f2-dc5f-3329-a4fe-acde2925eae6 | -8.1317 | -47.885101 | 2026-06-24 00:43:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a93d2d6d-8801-3417-813f-f0d0eed43ac0 | -4.3358 | -48.957901 | 2026-06-24 00:43:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6dded74b-b3e1-3c32-b219-a56e04fd61b3 | -6.8383 | -47.867298 | 2026-06-24 00:43:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d5b4803-312b-372a-9f9e-61f07b899835 | -5.8191 | -45.054298 | 2026-06-24 00:43:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fab7f10-27d9-363f-a286-1bad5cc05092 | -12.829 | -44.358501 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14debe0e-a88b-3e7c-8bfa-1b4db84fd3b5 | -10.1088 | -47.557201 | 2026-06-24 00:43:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50f4a49c-8ce0-3e59-8b50-6fc677d96723 | -7.3668 | -47.031601 | 2026-06-24 00:43:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e71ceff5-2954-3836-8de1-2e847280a742 | -9.1907 | -46.488998 | 2026-06-24 00:43:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0a9228f-3756-3c2b-b6bb-c89ed0debf64 | -17.289101 | -47.040401 | 2026-06-24 00:43:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db2a4709-89ad-3a74-b07d-573c134375ca | -12.8367 | -44.347401 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fb72672-d7b5-3046-a687-fa55cfea8be2 | -8.69 | -47.846199 | 2026-06-24 00:43:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7fe5778-ee3c-3b10-8c76-77856ddc954f | -5.8093 | -45.056599 | 2026-06-24 00:43:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2086976f-f9ab-3ebe-aaa5-4553e5dd4588 | -9.2199 | -45.340599 | 2026-06-24 00:43:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f27d315-482b-312d-bbf2-0c5f7852c027 | -7.2871 | -46.248901 | 2026-06-24 00:43:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbb7d4aa-c675-384a-97da-58b96f525582 | -6.8481 | -47.865101 | 2026-06-24 00:43:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8aeae934-fe6e-3a0f-8594-ac61eb92598b | -7.9262 | -48.292599 | 2026-06-24 00:43:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ee7d9cbb-84e8-3c61-9ff2-c7b4b092a707 | -6.3667 | -43.5919 | 2026-06-24 00:43:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9dba909-6b95-37fa-bd91-de3ce4549f33 | -3.9682 | -43.118 | 2026-06-24 00:43:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9d527e3-dcc7-3fc7-8835-dd794a096e27 | -9.4395 | -48.872501 | 2026-06-24 00:43:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f14c4f0-47b7-3301-a1c1-80a86e81a75a | -13.0705 | -53.341599 | 2026-06-24 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab7c56af-a314-371f-aa55-647882c805a3 | -7.9148 | -48.287899 | 2026-06-24 00:43:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 434282e1-86b4-3a6b-ba7b-7e6147f0c8c8 | -13.0827 | -53.3524 | 2026-06-24 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 2e97f953-e14e-36f3-af15-cd1b674c4c67 | -13.0635 | -53.3546 | 2026-06-24 00:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 9d0bdf8d-5623-3d12-adea-7d8a0a5cb292 | -12.776 | -44.4458 | 2026-06-24 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| de830452-0856-3dfe-9036-e0d0907d31e4 | -6.3703 | -43.5898 | 2026-06-24 00:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bb3a014b-1848-3236-bf01-5f758adab6c2 | -12.7764 | -44.4223 | 2026-06-24 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 151232f8-5ed4-311f-9618-e72378bd9531 | -12.7953 | -44.4426 | 2026-06-24 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a4e5e066-3ae8-3485-9cba-fba0690e1a2c | -6.5924 | -43.8957 | 2026-06-24 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 55277818-3958-39d4-a029-fecbf6d3a8a4 | -12.776 | -44.4458 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 671f6b8f-1f14-338b-9887-880dc4bb9f4c | -12.8354 | -44.3657 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 887.8 |
| 450cdbf1-00a3-3785-b02e-bc14dfd83876 | -13.0635 | -53.3546 | 2026-06-24 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 136.4 |
| c7b37d80-84d5-3f63-b4d7-cc99fefd886a | -12.8543 | -44.386 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 995279cb-007e-3b46-bfbc-ea7b1f1f0826 | -12.8359 | -44.3422 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 472.8 |
| 0f07f0a3-c20d-3d30-8b63-4467ea464d7c | -6.3703 | -43.5898 | 2026-06-24 01:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 2bbca740-90cb-3aef-9b22-af3ce8e41dc2 | -12.8349 | -44.3892 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 330d9cc3-8aa0-3692-9bf3-173bdd4e9664 | -12.8548 | -44.3625 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 493.5 |
| cf29fd63-a471-3756-a626-003187d2e4e6 | -13.0827 | -53.3524 | 2026-06-24 01:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 608bb5d1-578e-3903-bed3-d14995084062 | -12.7953 | -44.4426 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 9af73e6a-00cd-3dd5-8b4b-7899b1dd14a3 | -12.8552 | -44.3389 | 2026-06-24 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 249.7 |
| 136789cb-22ef-3a44-a145-5887134bac0d | -6.5924 | -43.8957 | 2026-06-24 01:00:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 1dafc539-da10-3ed1-8eaf-ba607769ee73 | -6.3703 | -43.5898 | 2026-06-24 01:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 35f45173-5e75-380b-9ca6-8e8cc6ce4de9 | -12.8552 | -44.3389 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 241.0 |
| 772d1dd7-a7fa-3e5a-9f85-9552b8fe3523 | -13.0635 | -53.3546 | 2026-06-24 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 5c8f2580-f823-3e0e-b2c7-11a97ec195b5 | -6.5924 | -43.8957 | 2026-06-24 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| fd7b5257-e121-39b0-9375-d57cdc554bce | -13.0827 | -53.3524 | 2026-06-24 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 559e35dd-1603-349a-a000-91beeef075c1 | -12.8543 | -44.386 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7501e0a9-fac1-3327-b47a-01fd9618e16c | -12.7953 | -44.4426 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 55d160c8-9b5e-35f9-85f1-ca6d3f94b221 | -12.8359 | -44.3422 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 357.6 |
| 5ce8ae6e-f226-3ed1-80d3-df27470db730 | -12.8354 | -44.3657 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 791.7 |
| 2b3dcca4-c014-3dd3-85e5-c6a835a95c45 | -12.8548 | -44.3625 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 541.9 |
| e5e14c95-049f-3d80-a74e-bdd2ac6c33b7 | -12.8349 | -44.3892 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| b8ed43c8-d736-3c3a-9bb1-184ab1af483f | -12.776 | -44.4458 | 2026-06-24 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9aa1bc0b-94dd-337f-b3d1-c92fbaaf565b | -6.3703 | -43.5898 | 2026-06-24 01:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ccc3401c-7265-3b7a-9cae-48bdca03dc79 | -12.776 | -44.4458 | 2026-06-24 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| d7b35ba0-b4a7-3e03-8aac-8f9dbdd6b19d | -13.0635 | -53.3546 | 2026-06-24 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 2e4f9fd9-e07a-3990-8997-a0d867432a45 | -13.0827 | -53.3524 | 2026-06-24 01:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |


[Clique aqui para ver as próximas entradas](README5.md)
