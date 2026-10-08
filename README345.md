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

## Dados Diários - Página 345

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ad78ea5-20b7-3df2-861f-71967c11751c | -3.04124 | -54.10046 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 0c1c8539-85fe-3b53-9a1f-2edaec3aa522 | -3.25801 | -54.6777 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| ac0269ff-4612-39bd-983e-dcdc857aaecb | -6.94491 | -59.0969 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 789ae790-4006-3af8-9f72-1a64bb8ab1d0 | -1.47839 | -54.54851 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| eab5f37e-0962-33a3-a3d9-134cb3a13bca | -3.01251 | -54.75368 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18da5414-6b26-338e-95d6-293739323e61 | -2.08572 | -46.5817 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| b8b576f6-da33-32a0-ad07-b539a8b09578 | -6.04623 | -53.47754 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f4f3cd4b-9a7c-3efd-b28e-d2ca76333ae2 | -3.23974 | -42.58726 | 2026-10-08 16:39:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 52c3aa1b-1bd7-3b04-a198-d5b73ea12f54 | -5.95811 | -46.38193 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 17549585-bfbd-3c7a-9a99-64b916b26a6f | -1.32349 | -53.14836 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 260bf2db-636a-34e4-aa0f-78e4044fbaea | -5.27756 | -45.72551 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0eca717a-ac58-36a7-bcd6-5d2041b5bae2 | -7.32094 | -55.00229 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75cd775b-7fcf-3ec3-a36c-1c217c98e141 | -3.72914 | -57.14504 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36daa848-1c8d-3d57-b429-98bd23548206 | -3.29268 | -42.28978 | 2026-10-08 16:39:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2d5729f9-fe29-3195-aab3-0043b623a149 | -4.05513 | -55.3263 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0a23bc3-d580-3956-bc07-5d3c5ce72d25 | -5.70476 | -53.45273 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 22962791-dab3-3555-a74f-ee39079d585c | -3.00448 | -54.08758 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| ac405e16-e0dc-346e-9dbc-dc241b4d6569 | -3.48526 | -60.28468 | 2026-10-08 16:39:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db1e47fe-c3b1-3fb5-b633-3e3e3669b1c8 | -6.16594 | -53.42709 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8a6e32fd-e96c-37b4-a830-b921ad7bc299 | -2.79229 | -57.61529 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29c2a83e-bb32-3882-9aa7-d6b435f801dd | -3.43242 | -59.10427 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2457b475-236e-329b-9051-ed9c141a7cfa | -5.91532 | -51.93509 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3eef112e-664b-3efd-afad-e924c4d821f1 | -4.92922 | -55.86299 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9149cee8-89f5-3356-8dbe-4c2364368a38 | -5.55316 | -45.57479 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6a5ec0a6-f001-30f6-ae39-cce877e6280d | -3.06282 | -54.38481 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f87f48d5-0db6-39d4-b4f4-2bdabae49602 | -6.99415 | -59.10312 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 722e23f0-a10b-3597-810c-aae43d22a360 | -4.45698 | -55.39882 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 691c3760-7b47-3464-8004-35159dce3cff | -3.93966 | -41.54684 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| fbaba979-5d8e-3916-a7db-ff78bfeb03ee | -3.17991 | -50.55274 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0d30d576-d3b0-3a31-b773-ace00a0424d6 | -3.11247 | -53.78443 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f39cfcb9-404c-3f2d-a4d5-af443a4542fc | -3.90257 | -58.95533 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7f1d5565-7ef3-350c-a5e7-0049c7a7c732 | -3.37078 | -53.53364 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0cfcee8-2a83-3a65-a944-c8f13aa8463c | -2.98649 | -54.0645 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| e56d15c7-2728-3617-9e9b-614545c9b536 | -1.39817 | -48.9368 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 01b55736-0827-3e3e-ab1b-91a93559f5db | -6.32377 | -55.32815 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 790315fb-2af3-3234-8122-2b15c6f486ce | -7.19481 | -55.12233 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 480ab153-ca37-3684-ac80-4d73c509ce8a | -3.28894 | -49.12841 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 7a26f926-47fb-34f6-a852-5c6ef48c6bd8 | -2.86838 | -54.15779 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d67bab96-db82-39f9-801d-7cb746251e27 | -7.0027 | -59.11508 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b6c5d82e-4267-35af-9976-56ca1d5769e4 | -4.37577 | -41.8315 | 2026-10-08 16:39:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3b9493b1-1ebd-3375-b22c-1c525f0b64ae | -2.83608 | -54.13609 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3b27aa5e-9f78-3a97-abd6-e52514e449e4 | -5.88394 | -45.96205 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 82297e6b-2dc3-3871-b19c-bb2bc9bd0eba | -1.13745 | -60.40194 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2131178f-841e-3fa8-80ad-fcc14461ce44 | -4.84128 | -43.34022 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 70f5aa87-5397-3d1a-8f81-c8c1149af3fd | -5.5131 | -45.62395 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07f54986-2c40-3458-9ad2-5da2331868ff | -6.61693 | -53.00742 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d5d56bbb-309b-38e3-bda4-f4c436bdee45 | -3.48558 | -59.38391 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 4c5e1064-a777-3241-8232-7f0d4d978a74 | -3.80457 | -40.45177 | 2026-10-08 16:39:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ba29ff90-6e04-38bf-a4ec-396e61ee0887 | -2.02935 | -55.63246 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bcbf42f5-48bc-3d95-afdf-57be8174f4ec | -3.17201 | -50.44833 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| f151d4cc-09e5-3930-97f9-0a7ec21d7a1b | -3.18851 | -58.64788 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| a835a184-5a7a-3137-aa72-7b0770386e05 | -3.6852 | -43.05355 | 2026-10-08 16:39:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8d3130b2-b54f-3de4-b102-79f882ea1939 | -4.91723 | -55.85761 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 063bf677-cc13-3163-bfd0-8f7e181e9276 | -3.108 | -54.19022 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8be5482a-6d02-3ba3-87ef-5c5cc9e89304 | -3.85638 | -44.12643 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 309a6f80-2f92-365c-ab05-663a64807f2e | -5.97659 | -51.52914 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| beffc7aa-6fee-3f6c-b5fe-51d70fb6fa25 | -0.73983 | -57.98034 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c4ece358-b23d-3a11-98f6-facce0f2cb13 | -5.6958 | -45.28823 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cd4f871-c874-392c-9bcb-996f48710fd2 | -7.14291 | -55.10535 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb8ec0f3-f086-3c3a-b0fd-0dfac538ec3a | -4.63878 | -44.56233 | 2026-10-08 16:39:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ef77370c-bd96-342b-a284-214b2b81dae4 | -7.14427 | -55.11565 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 23ca8ee8-433a-3ad3-a10a-d3457e6d5820 | -2.11408 | -46.38971 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 703c6cc6-e383-3710-839c-ac54699e8158 | -4.05486 | -55.32419 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 534304c3-f249-325f-be7e-63a57fe04ea6 | -2.72993 | -44.33393 | 2026-10-08 16:39:00 | NOAA-20 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 739a6df1-00bd-34d6-8a1f-b3bb371a4d2c | -5.70804 | -53.44214 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f03578e1-b982-3174-8cc1-397e5ac14f62 | -2.79219 | -45.19416 | 2026-10-08 16:39:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 48e9176e-2c80-3e34-b4cc-334096e5784d | -2.84905 | -57.4844 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c94b8423-eba3-3fad-be64-a93028b197d9 | -6.45034 | -55.03322 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e75a384b-2dc2-3174-943b-f881d58b9e64 | -1.48385 | -54.55479 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| dad32a1e-adfc-3406-87f7-1d06815a83e3 | -5.7759 | -45.38998 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2ead5ec8-720b-3932-a185-6b6ea1397f74 | -5.36043 | -43.07233 | 2026-10-08 16:39:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2a3d8719-83c9-37ed-a5f7-51833eee37a9 | -3.86234 | -38.51003 | 2026-10-08 16:39:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d47ffce7-252e-30e6-8b57-da46d3f28216 | -2.69576 | -49.04016 | 2026-10-08 16:39:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fd22d38d-d8e6-3fab-8194-e3f48a58ab2f | -3.18623 | -58.63206 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 93153eed-d5bf-372d-b5ff-c57ab461c5f5 | -2.74571 | -54.12099 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| b10ca117-eabc-3983-bdac-ccb169189667 | -1.48797 | -54.54731 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 9e106118-9f07-30b0-9d39-14929701f466 | -4.57724 | -40.64846 | 2026-10-08 16:39:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d4b5633f-0957-3049-8d6f-5ab1e263cdb9 | -4.76801 | -42.66369 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f3c38038-e949-3509-be4d-670cd1cb9da3 | -2.49913 | -56.15889 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 19856570-4c02-3c30-ba6d-5d09f8346ba1 | -7.22559 | -55.09089 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 214a7467-0f3c-3808-83bf-450331403127 | -4.84284 | -44.09492 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0063be63-f4e1-3041-a13a-3d5929f9bcd9 | -3.65324 | -59.16869 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f5610013-952f-332a-bf3d-eacc34b68663 | -3.26874 | -54.68179 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f14de2e-c5ce-34ff-81ee-33fcc214d3d9 | -2.99511 | -53.84932 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| eb8b6ca8-dfeb-3d69-9686-bd691d3b6195 | -1.49961 | -57.74236 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e425b6d2-bba8-3cb8-9254-d1f7327a9160 | 0.5391 | -50.77371 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 233bd5a1-6d8d-3e54-936d-b9a925d3d525 | -1.77497 | -55.03142 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6db3accd-efd2-3958-b6dd-66eb228dd2e6 | -3.58317 | -59.52414 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b8f8efb-e639-387a-92c3-338552d4ff68 | -6.21632 | -52.7801 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e9cd0989-eaef-3e0f-a619-2dde8e287710 | -2.82272 | -51.95797 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 762f2c0d-8e4f-3a0e-990d-37588237bc3a | -5.70026 | -53.48849 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1fb40aac-3954-3470-8474-d8a437679adb | -3.42916 | -60.22289 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| df3da412-c206-324f-a95a-bd2dd9b99073 | -3.48962 | -59.38365 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5e4bc3e5-a084-386d-9d6a-66f071236ea1 | -3.43924 | -45.09678 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dc74aa36-1196-3f1e-b8b2-fb6ff738408b | -1.28938 | -54.5614 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b3d381c4-2113-366e-b88a-445207b25ea2 | -1.8263 | -55.03523 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 529b4357-71e4-30f0-bf07-088ac8425e15 | -5.89214 | -45.9714 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2f08b005-e784-31d7-ba60-642deeef6bd7 | -3.50658 | -59.33827 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 5ec77e25-7404-3d36-8a2e-950655e8c5f4 | -3.93359 | -56.0255 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 1739505d-8a16-3213-82d7-0df1d473e95f | -5.41458 | -45.71128 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README346.md)
