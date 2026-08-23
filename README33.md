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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f787d180-ed67-3913-9430-3e39a2231afa | -12.58466 | -47.88087 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcde4d78-a410-3497-a5ff-310c836d6308 | -9.09893 | -60.92426 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d3ae8db-9c34-3408-9323-7dc11211b8dc | -10.79412 | -50.96765 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89055253-626d-3845-a339-ed693f796736 | -11.61714 | -50.55411 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1038378b-351f-3b83-a98a-d1a4b8351f04 | -14.54315 | -52.79735 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9626cdde-95a9-3339-8dbe-408847e57269 | -9.16468 | -59.46965 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aebe0f6d-3a16-3513-94c7-dc4e4c71e6f6 | -15.04101 | -48.69404 | 2026-08-23 04:46:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9dcb2409-28c3-3343-a0ab-a6f245a04de2 | -10.3279 | -45.40443 | 2026-08-23 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 839132c1-fdaf-30d3-9174-4df8a280169d | -14.51992 | -52.00912 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16696b3e-4533-35e9-92c9-164188689f02 | -7.5557 | -61.17807 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f185be7-f1f5-3342-9b8a-de4bd5231f5a | -10.81118 | -50.58672 | 2026-08-23 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af9a3046-97a8-300c-a659-975a777aa6a7 | -9.102 | -61.59445 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83fec799-436d-3012-9059-9a4ec9f19a2b | -7.59423 | -60.9398 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00d7ec33-a676-3e3d-b0a4-87400cfca794 | -10.83786 | -50.97506 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20772b53-62ca-3a02-9113-e3d96f570352 | -13.44069 | -57.0794 | 2026-08-23 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b704ac9-7ef9-3379-9ebe-074bc2f861a5 | -14.37681 | -51.77942 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ba91fdc-c7ec-31d7-aae7-e1461e6cef0f | -9.16041 | -59.45987 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 720c144e-0b97-30be-a639-8aa6246bc953 | -15.34048 | -52.77891 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 957e47a2-25cd-3d58-9f21-577fde9c3e79 | -8.99302 | -50.76204 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c29ddddb-4b60-32b6-8afb-b9a4b9d5981c | -12.22246 | -43.17145 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 14d907e7-cd41-3ae9-9204-776565b67c31 | -8.54008 | -54.84427 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 725c42ac-ec9c-36c7-940b-12087628e266 | -12.72836 | -48.39711 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c4a1197-d1bc-3059-a981-5c3fae9c398b | -10.33158 | -45.40499 | 2026-08-23 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5476759-278e-3082-b44d-a44ac9969933 | -14.40908 | -51.79219 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 637570f9-2078-3fa1-91dd-b2b3d18c8159 | -8.20079 | -54.98606 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7554c24c-d117-379b-bb55-2b14aa0f5026 | -12.84697 | -48.46396 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 199b173a-a9f7-336a-8898-3aa265b7b514 | -8.5262 | -54.81956 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 396e7a95-4eed-3696-bddf-71a7ec88872d | -14.31376 | -51.83933 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0056ec69-b666-3486-8128-d7713c3ce28a | -9.86161 | -60.11151 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40f14c5f-81ad-3809-9c76-06df675a7e9c | -13.15991 | -51.41779 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2df5a8fe-4567-3c29-a453-5c3b9424b756 | -12.77178 | -47.12562 | 2026-08-23 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b89d35d-24bd-3250-9c49-6c6883f78b2a | -9.43562 | -51.59852 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98a5b311-acad-37df-b27f-c40f2188734d | -7.78541 | -61.42389 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c96ceea-1a10-3906-b87f-6b8a1e429645 | -10.84629 | -50.98816 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c140f199-18d1-30ae-ab01-4d5418927b12 | -9.10395 | -61.59558 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 29dcd0e0-70ea-31bb-9e8e-7e3752e0176f | -8.96344 | -50.76867 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f73fd280-3881-32d5-bb32-6dd19eb42f22 | -10.30844 | -48.21132 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d7c4e0f-a295-3658-8e9e-2ffbb8fb88b1 | -15.76245 | -49.97241 | 2026-08-23 04:46:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d80407c6-eb7f-3391-bab8-b7f4a3b4b5f3 | -9.52379 | -51.64316 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42c027ed-2c54-373b-87bd-8e5c8b10d7fa | -16.06201 | -50.42736 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdb63d15-444e-3134-be0e-7311a5a4d817 | -12.73643 | -46.44816 | 2026-08-23 04:46:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 486fe97c-99e4-3589-8cfb-a99881590bd5 | -10.84348 | -50.98379 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 65a0f52b-7f3b-3c32-a575-eab8e3af7bcf | -13.2253 | -51.4486 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| deff39e3-b816-3e76-a34f-1aca2deda2e1 | -13.89278 | -54.00019 | 2026-08-23 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77ea3079-a69f-3a68-8efd-7cca47f96f7d | -16.0509 | -50.43283 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3e853780-c4d9-3f96-b8d8-1e68e3e158f7 | -14.50016 | -59.82578 | 2026-08-23 04:46:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8373e7c-d16d-302c-8cc7-8acfba848bf3 | -12.23057 | -43.17693 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 26e8ceba-e2ec-36f4-8262-d046df2b73d5 | -11.21266 | -55.07834 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aab816ad-ca3e-3134-99d2-3f87a1ca80b4 | -12.75075 | -48.38576 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc70b67f-92d3-3644-936b-ad394917172b | -8.53134 | -54.81606 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8a4ecea-0abf-3b82-a918-a721fb46463b | -13.18696 | -51.44585 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6a20cfb-a829-39c0-a9d3-ba6a1d9a8967 | -8.53939 | -54.82196 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab076cc6-dd6e-371e-9433-be9c97b42fef | -9.42641 | -51.6311 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ca2ecc3-0dc9-331e-9561-d0fc38ad9850 | -10.49767 | -42.548 | 2026-08-23 04:46:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 408923d5-8483-3303-a7f3-e6c5830e5ee5 | -7.61455 | -61.61218 | 2026-08-23 04:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9179ca17-0e51-3151-8d93-f11628e330fe | -9.17305 | -59.45786 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca92cf51-59ef-3aa8-bd2a-4bf9ef5b366b | -15.24852 | -52.83051 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f9f12af-fd57-308b-8a76-b81bea4a6d66 | -11.43508 | -44.52787 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00cf6d36-52a4-3139-814d-e7d869e57667 | -10.93895 | -49.59955 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0696fe65-d6c3-3842-bee0-8d2df926cb36 | -13.44956 | -43.84501 | 2026-08-23 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bb643ff-3170-3f2f-8add-24b32b6bdffb | -10.51542 | -50.77166 | 2026-08-23 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ece5e98f-a615-327a-9a0d-3d2c0d373d97 | -10.8385 | -50.97128 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e97862d1-8485-3c20-96e2-371290fd216f | -9.03977 | -50.83187 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 337f3912-c040-32fa-9874-9223830f5e8d | -10.80037 | -50.9726 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03cba349-d519-339b-81cb-9a753012e1cc | -13.43541 | -43.85447 | 2026-08-23 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6fe7a8c7-64c5-3688-af0e-4e6edd0c691f | -12.11973 | -57.21035 | 2026-08-23 04:46:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d88b6bdb-dcb2-36a4-8444-7b0a97979924 | -12.26417 | -45.08332 | 2026-08-23 04:46:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3384be7-64f3-3d14-b75c-66f50d9d7f23 | -10.55869 | -61.45766 | 2026-08-23 04:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1492ff09-06f7-3b4e-99d2-2fd7e12f01cf | -8.52409 | -55.34354 | 2026-08-23 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f54ecdd1-4c61-39cc-b202-217dfc595431 | -8.54082 | -54.83997 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa007f6b-699c-33ad-8e37-1e3843168bfd | -12.75146 | -47.11841 | 2026-08-23 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cfd4675-22e1-31fd-9013-dd148127a0ba | -10.79287 | -50.97522 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75967419-f067-376b-afc5-b759de86902a | -14.44214 | -51.80589 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8e90b21-c2e4-34e4-84dd-04998dbea22f | -14.14735 | -48.06044 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bd2fd15-196c-31ad-bb76-2827d2c6c5b8 | -10.06942 | -60.50544 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe9dd1c5-d7a9-358b-92d8-2ff3222fdef2 | -8.5249 | -55.33897 | 2026-08-23 04:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee67253b-c9cd-36c5-ac86-b737aeb1d0bb | -16.05365 | -50.437 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5a21a812-b250-3bf4-8224-97bbd8b6ccb4 | -7.44067 | -59.78209 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a1c578c0-19ea-3439-be94-c460c2464dbe | -11.85188 | -51.67213 | 2026-08-23 04:46:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 205b7485-ba84-3cb4-8ae0-e559fe84042f | -9.15316 | -59.56262 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43b6e6a6-8023-3505-845b-dc8e739e1429 | -10.3051 | -48.21081 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f512bf4-2e18-392b-98ba-1b69dce79481 | -16.05812 | -50.43038 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6005933a-ed26-323f-9c19-26c1c2ffec60 | -14.25121 | -53.04359 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd5e7921-a29f-3eb3-99bb-034b7f3f6634 | -11.36457 | -46.94743 | 2026-08-23 04:46:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12c4a9c3-f94f-3146-a2cd-e6ac069c4b6a | -14.99723 | -52.69091 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08cd0d22-8200-352c-8a17-fd4836ed4f3b | -15.51691 | -49.83265 | 2026-08-23 04:46:00 | NPP-375D | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e7857f75-69e4-31f0-8c4c-fbae36f56e89 | -12.81462 | -48.40667 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1e4ce62-8a2b-354c-860c-6457016577a0 | -9.52737 | -51.6438 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85bcdfe8-d81f-395e-90ba-010760f431ce | -10.34514 | -48.23886 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2a08bba-271b-399f-936d-cdc77608d15c | -8.96186 | -50.75666 | 2026-08-23 04:46:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fe7a433-d213-3e3d-acab-c6c255bb8c8d | -14.38367 | -51.78063 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d21259bb-57cb-3736-8aa3-6167cd281649 | -13.15864 | -51.42536 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 27f53b9e-9784-372b-b41b-d27a2ba8650a | -7.55453 | -61.18421 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4893953-93fa-3453-bfb7-35af78ececee | -10.46524 | -49.96686 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7347988c-555a-3b83-a316-7feb0cac9f39 | -7.59559 | -61.2326 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60129e35-7590-347b-b69c-c65375ecf96b | -9.15484 | -59.55381 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 744b25e4-71e0-377e-9257-d06508b13aab | -14.33946 | -52.92159 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcb83f0d-fb00-3d66-a598-1ea131cb24e0 | -14.13086 | -48.05405 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 600d3d5a-b1d8-3086-b5f2-7f7101046d57 | -11.20838 | -55.07754 | 2026-08-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df42b3ec-fd8a-3683-9ed7-b352276491eb | -11.16265 | -54.00993 | 2026-08-23 04:46:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README34.md)
