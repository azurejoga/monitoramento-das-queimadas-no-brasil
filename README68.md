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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90af9b96-b5fd-3690-acd2-f4b8d95c53df | -17.59459 | -44.53519 | 2025-09-08 04:53:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb67debb-ddbd-385b-a7a7-39a9b31785d1 | -9.47978 | -60.49158 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5e64f36-7e41-35a2-8d26-4ed94d1ecc6d | -13.7397 | -46.90072 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b18e19c9-3bcf-39f3-a142-d9f4867ad826 | -13.74448 | -46.90098 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f24e62d2-8cae-3175-9150-9a7efb6aad90 | -12.94213 | -54.78252 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b950967c-24f9-3bdf-9a2b-430cb752ace2 | -11.08664 | -51.98402 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69a87f77-3555-3b01-a538-1e72679ad02a | -13.91001 | -53.96626 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7d45fbe-35f6-37aa-a9bc-ae7fa93aab7a | -16.28211 | -45.68174 | 2025-09-08 04:53:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 97ff19c9-09e8-3216-876e-de35b47ab360 | -12.82237 | -52.94187 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46c4d2c9-6bc7-3aeb-9ea9-5f0669f980e8 | -15.84577 | -52.30771 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92194f01-e170-3102-8d51-2db491abc42f | -11.41311 | -50.3928 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| f03016fd-d1c7-3f02-8fae-1662d79bc431 | -11.64454 | -52.23936 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f408b64-4073-346d-b041-862684c4e9a5 | -11.20228 | -54.99942 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ef484b5-40c2-3a41-94d1-3f95a66a9206 | -15.75609 | -53.53863 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 528676ea-ec60-36c0-8aff-5d647a437052 | -15.5302 | -48.17892 | 2025-09-08 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8009ea1c-f5a4-34c4-84bc-1f3eb9912405 | -16.30261 | -45.69141 | 2025-09-08 04:53:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db9e9832-c1cd-301b-af32-abf01e1ad09d | -10.0538 | -59.35823 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a8e393dd-17da-3164-bd4e-8dfa012d7dd2 | -11.46377 | -49.25519 | 2025-09-08 04:53:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0265dd62-d5ed-3f08-930f-8532f7d012e4 | -12.93551 | -54.78144 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e58af3a-9687-3cfa-960a-72f08924851e | -12.935 | -54.76322 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13700d10-8fa0-36d2-ab03-3d57369a3b07 | -16.3373 | -52.93156 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 03b9910f-6f56-352f-b5da-4c253ec9a4b1 | -12.94982 | -54.79832 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dbe82ce-120e-361c-a874-95e96eebe2b7 | -12.6252 | -56.96935 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c8a75443-e40a-3abe-b544-87f6429c6cb0 | -16.90392 | -45.7906 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6be4742-72d4-371c-a526-d1e8f3d13ffa | -15.20401 | -52.34621 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8342dfc1-9dc2-343e-96c7-4ea924de5d71 | -11.86783 | -51.06821 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19cfdbe2-edae-3e97-acfd-35570b9964fa | -16.90979 | -45.83584 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 299caab9-d4a3-348e-99f4-cdce059ea9c2 | -13.03641 | -47.12732 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cabcf04e-25c0-32be-aaa0-05bac2d8362f | -14.2562 | -58.35917 | 2025-09-08 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 373a716e-58ed-3441-9c83-c237480d3bc7 | -12.42139 | -63.89553 | 2025-09-08 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c440367d-c96d-371b-b73d-149d2d8c1e85 | -12.81176 | -52.94392 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a95e56d-1891-37a8-8a9a-7567b1e30fd8 | -14.52801 | -48.76536 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d944e95-a916-34d4-85a3-87a33ca65ebb | -13.03912 | -47.14267 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e3a2b6a-f2db-3950-8ccb-0806084b66ad | -15.22834 | -52.35022 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 793c8a6c-cd4a-3f7c-8adc-bf1c9c661bed | -14.8846 | -55.83128 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1b27b74-35e7-371a-ae2b-0648ae756abc | -12.81902 | -52.94134 | 2025-09-08 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 903776d7-19b2-39b9-9ae6-6a32c83f86d7 | -12.64148 | -56.98048 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e367ad5-3e46-3ce7-865d-104b0a5435c6 | -14.37682 | -53.15714 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a8494c5-c7ee-3b77-8bfd-e77c08f2afd4 | -13.03704 | -47.12237 | 2025-09-08 04:53:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd00ddce-2e12-3e7b-83e9-e97f1c61abf7 | -11.03454 | -52.02929 | 2025-09-08 04:53:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03084ac0-4fb9-3fc2-ad2b-6906fbdfe266 | -16.35363 | -43.64088 | 2025-09-08 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3aff85ea-150d-3260-b421-2c1fd58c64da | -11.62016 | -52.21656 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1657542f-44ac-3096-aa3c-0ec4ba46ac82 | -11.86132 | -51.06299 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f02388ef-083f-3a8a-a7ed-591487c15938 | -13.72502 | -46.89274 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf34f573-c200-3fcd-b50f-50a396cf140b | -14.6909 | -48.19624 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2b0825d-5d5a-366c-b6a3-dc8769eae90e | -13.72582 | -46.88644 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d06d5d09-141c-3ac5-8fea-7b62a4cbde60 | -11.21783 | -55.00932 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abd83c50-5fdd-3f50-bece-f6c4fc3873d6 | -14.58928 | -48.0785 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bc3103a-9522-3b53-b2cd-789518ec2c34 | -14.70787 | -60.2546 | 2025-09-08 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70d94c03-b7e1-3ad3-9c3b-a1507afc8d6c | -14.88126 | -55.83074 | 2025-09-08 04:53:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5a6e80d-8e04-3346-b60e-6ac15f22e8a1 | -15.25807 | -53.81944 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e844c9b7-731e-3076-878b-3e5fdeafa70f | -15.75497 | -53.54602 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd1743c1-c255-39fe-a7a6-56aa68414194 | -12.95485 | -54.76648 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 912fa37b-43a7-34b0-8e6b-10ed014182e6 | -13.50943 | -50.80771 | 2025-09-08 04:53:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07f471c3-92bf-3ee4-b9c2-7a8c94296785 | -12.9509 | -54.81303 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa1d2348-c7bc-355a-998b-4340845f26b1 | -11.37824 | -50.40095 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c235ad5-beff-379d-a60b-d9de3c7f58b2 | -9.13276 | -65.9501 | 2025-09-08 04:53:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cd654a8-f470-355e-bf14-3e2ed0de8dbf | -15.25862 | -53.81582 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b929723-aae4-3131-b463-87cff5a432c8 | -11.38672 | -50.42003 | 2025-09-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 556e4a53-6978-3310-934b-82b286572bdb | -9.38719 | -62.33968 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d513017-03a6-3864-b67b-a9506f8ff37c | -13.64653 | -47.91601 | 2025-09-08 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 22784ae6-e3f4-39e9-a127-4b649b7d86dd | -9.47104 | -60.48721 | 2025-09-08 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c972a2a-7620-3208-8e30-a3b619ed17ac | -15.83401 | -52.28951 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb714267-c756-3e0f-9eb4-500b1b98271b | -16.91163 | -45.81892 | 2025-09-08 04:53:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0f447c8-0466-3cb6-b925-142b662bf066 | -12.20137 | -53.91057 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0702f415-c27c-33f6-a1fa-67351844b1ec | -15.83544 | -52.29919 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a613576-2e4a-3aae-9964-7444caba34e1 | -12.51811 | -53.86462 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 414c5acf-101e-363a-9a57-252c1c0c774f | -13.00327 | -45.20913 | 2025-09-08 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2870b32d-8b3d-3c3a-a42d-7a0094cc59ab | -10.2732 | -63.1708 | 2025-09-08 04:53:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef11fe17-492a-399c-809d-4223f19f57d9 | -15.29613 | -43.38734 | 2025-09-08 04:53:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 33178f73-636d-3e8f-abd7-da04176dcc8d | -12.52141 | -53.86515 | 2025-09-08 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a9f16f-4d35-311a-baa5-5aa70c926f31 | -11.91113 | -64.97128 | 2025-09-08 04:53:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bec20e14-0978-3bbd-91e7-cdf08f2ebad7 | -15.74041 | -53.57409 | 2025-09-08 04:53:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af082b17-de87-3fd1-8e6d-b047e4470a96 | -15.26596 | -52.38477 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3871a1fb-d922-319d-b410-7859af821309 | -15.83135 | -52.30264 | 2025-09-08 04:53:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf4dc612-b48d-39f4-b3b2-da6974f70365 | -12.01538 | -50.38546 | 2025-09-08 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8330cac-682f-3ae9-b3e9-bb49d44fdcc3 | -13.27233 | -51.77466 | 2025-09-08 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbfcf581-e632-328c-8aac-a0fe50ff9a56 | -13.55069 | -48.10204 | 2025-09-08 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 538391e9-2fee-3ae0-bf8c-f170d13f6a1b | -10.89544 | -55.71884 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5db99481-1df0-3fc0-b6f8-acb61e3f408b | -12.61895 | -56.98493 | 2025-09-08 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1328bba3-4740-3542-82b5-2303e481aa98 | -16.44639 | -49.28656 | 2025-09-08 04:53:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34855531-777c-3df7-a683-13d51280c061 | -15.25363 | -53.82616 | 2025-09-08 04:53:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 915897a2-651a-3433-8c21-b5e3a3c56f2d | -9.44701 | -61.82199 | 2025-09-08 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ee9bcbdd-17f5-31ea-b05c-91fec602564b | -11.64961 | -52.22875 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceaa98a4-f79a-3348-87d7-4ea85a0aa34b | -10.87434 | -55.71925 | 2025-09-08 04:53:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54c2ec65-cfe9-36af-a602-dbd31f6471b4 | -11.62869 | -52.22929 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aef7e606-b002-3888-b166-595f406ff74d | -15.42228 | -47.6825 | 2025-09-08 04:53:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 167d98da-1a19-348b-9842-efbdf7e154a3 | -12.946 | -54.77953 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 743e5225-1fb1-3c9d-acdb-67412ca6df24 | -12.81929 | -47.9983 | 2025-09-08 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 443a0b32-a901-3883-ad2c-d1d45b1ad473 | -13.66303 | -46.96588 | 2025-09-08 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53b9c042-0c01-3d39-8a6c-13a3dbd9ea35 | -11.2161 | -55.02007 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dbf57c8-ddba-38e4-8ef1-ea37ba03f80a | -14.50973 | -48.80701 | 2025-09-08 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 108955a9-94a6-32f8-97f0-30d4f3e5f874 | -9.62234 | -64.21041 | 2025-09-08 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4076bacf-1cfd-391c-8dc5-f2d390c5f642 | -13.00283 | -45.21438 | 2025-09-08 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94f47f47-cd37-3898-81aa-c2bfb57834ce | -11.91115 | -50.98871 | 2025-09-08 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c62a5ce-ae2c-3a03-a5a5-8835425f06b2 | -16.34648 | -52.94094 | 2025-09-08 04:53:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e0165db1-ed85-3cbd-b48f-c7d8d93df376 | -12.95202 | -54.80594 | 2025-09-08 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3dc67e9-ea73-3368-a491-e3109a142d21 | -14.24534 | -58.33394 | 2025-09-08 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8f69c8e-6856-3ba7-94b0-f778b5efa1df | -14.54276 | -53.26983 | 2025-09-08 04:53:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63d5697d-bfa0-3877-afcf-8ef09d212418 | -11.20389 | -55.01072 | 2025-09-08 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README69.md)
