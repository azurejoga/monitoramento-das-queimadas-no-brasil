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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b51c8eed-2f37-346c-811e-ecf40d489023 | -9.16976 | -60.83222 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bdabaef-efc7-30c7-8c1b-74cd934b9482 | -8.60949 | -62.64468 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc34ba1c-633f-30fe-a8cd-3a2587aaf0eb | -7.66171 | -63.5238 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f95193a0-1241-365c-bd8e-c6a9903dc799 | -8.9051 | -62.41615 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5baab250-aff1-3c5d-bea7-d16f2f9a0702 | -10.77202 | -47.07829 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b91d3dc5-cd27-3996-9469-048fccd495e9 | -8.75742 | -49.94547 | 2025-08-25 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cb5a32d-5a9f-32e7-9c1d-1a7b8acf987a | -12.49346 | -53.83013 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a116ab61-5b16-311c-9cec-765e249d1dd0 | -8.87548 | -62.46312 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b991b738-2b16-3fa2-ba78-6dcb3a18f77c | -10.7079 | -47.1353 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5254303f-166a-36dd-8bbb-0d9c8e47cf61 | -11.39734 | -50.68318 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b16a8307-1440-3598-b264-2be4b8cee977 | -9.51741 | -60.55804 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0286d09-ccdb-341a-841b-3f875171e18e | -9.16741 | -59.45911 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5a4c3f72-bde7-31a7-8d83-12fd83306a97 | -10.76475 | -47.07713 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73b103c9-d024-3cd2-8158-11318ed65238 | -10.70682 | -48.31372 | 2025-08-25 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7b40fce-bb1a-3d49-ae7d-465fa45f6b85 | -8.54528 | -48.85543 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be42cd58-8a6f-355a-b6d0-4be517526567 | -10.60347 | -50.14045 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7e39b0c5-6831-3ef6-b726-bb3482d11a4b | -8.54083 | -48.862 | 2025-08-25 04:42:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4f4cd59-8210-3f32-a370-4b2e38412381 | -13.43913 | -47.02157 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4680a377-6075-33de-8d50-ba3343d9e915 | -11.58083 | -46.28032 | 2025-08-25 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d976d24f-7d3c-3b9f-9310-0039aa51eb4e | -12.41523 | -46.49323 | 2025-08-25 04:42:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b1edd8a2-810c-3342-b7a8-f8d22622536c | -8.0667 | -49.68849 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17792428-0fea-399f-bafd-aab487fb6169 | -8.61179 | -62.59623 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8853425c-d260-3f95-a3a9-942280cec824 | -12.99094 | -45.22504 | 2025-08-25 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c642aed6-1717-3ec4-a39b-1f489571c26b | -11.26831 | -44.98806 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 005d7335-f1b7-3418-8530-f2f8617624ab | -12.74406 | -48.11694 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 244657be-1e6b-37cb-a4ec-e40321f41e5f | -11.09499 | -44.78032 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257dfaab-83eb-3f5b-9087-3287eb2b227c | -8.87659 | -62.45746 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 947196dc-43f4-3d18-a0ed-819d043cb5ff | -9.47042 | -57.81786 | 2025-08-25 04:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0c78324e-8f17-34c8-8774-7ed52aa6a0a8 | -11.39457 | -50.67912 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cab482b7-506f-3adf-be21-f327bfc8573d | -11.61281 | -46.23439 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdf1349e-91f4-3025-839f-15ef1d0746cb | -10.60092 | -54.88251 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c2f35d5-1841-3127-880e-c8e96e5c6dcd | -11.12545 | -49.98608 | 2025-08-25 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 058b299c-6931-3cdd-a3e4-dc7223f4d763 | -13.28464 | -47.51223 | 2025-08-25 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f3ce932-5a0c-3597-986d-a8558fc6295f | -13.40695 | -51.80854 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 230e2da6-832f-3cb2-b10b-f4c582eebc37 | -13.43128 | -46.91437 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd976d52-9705-32aa-8c2c-e01231333e1f | -10.25481 | -59.10594 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9a5987e2-2ddc-3354-98a8-e5cf00962666 | -8.58397 | -62.6333 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a672e185-2177-363a-b18d-e1858f837c4f | -8.90614 | -62.44582 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 705c30b8-8ac4-3b14-83a0-2896ddb38312 | -6.83306 | -58.95402 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a327c0c2-b318-3efe-9ecc-a24c31f7b703 | -8.498 | -63.86907 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e774846-c4ac-3d83-92e4-59a66fcfa103 | -11.11069 | -44.79045 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65bf0b7f-16d5-355d-b269-12c22dbfa122 | -11.1376 | -46.33852 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9caaf995-b6a9-3054-8290-78f78989ec20 | -12.74059 | -48.14073 | 2025-08-25 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c432b5e5-fb7b-304a-bbc9-c9aabfaeea4f | -11.09185 | -44.77203 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46f40525-978e-3027-a619-3236fce77ace | -6.82819 | -58.95057 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0e97903-82d4-3ee0-ba60-9c771499d959 | -11.86843 | -45.12275 | 2025-08-25 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d90a64c5-f5a1-3553-a09d-c8264f73aa18 | -10.89338 | -55.78332 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 131e0a08-844b-3ecc-bd49-052452cedfbc | -7.5443 | -63.86028 | 2025-08-25 04:42:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b83422d-aa4d-3bf8-8cb9-ff2924940e9d | -9.20376 | -59.48062 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7089aeb5-165f-3658-9a00-48ed129cab6e | -8.10381 | -62.87929 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e3b8c08-b176-3b82-a98b-b3d13f0a4bfe | -13.39575 | -51.81403 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97eee9af-1388-34dc-9e14-b917dbdff436 | -8.11864 | -62.87572 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5621f9c-5f90-3949-bdf6-5f6fe24cd61d | -11.04976 | -49.12632 | 2025-08-25 04:42:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b8e649e-8368-39cc-a6e4-b1e1deb0c5ef | -8.80202 | -47.31318 | 2025-08-25 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7969114-c9e4-39a9-80d0-478e02814933 | -9.14917 | -59.4665 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b75f6cd-cf63-3dbc-bd3d-5d25fc11b1e5 | -9.15611 | -59.48989 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ffc82e7-614d-3bee-af5b-e8c3ef2f8021 | -10.98395 | -47.40318 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddd51bd8-45b7-3772-ab48-7e840d5e2b33 | -9.25501 | -48.18907 | 2025-08-25 04:42:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d39d17db-b863-38b7-a86d-08d1a3270cd4 | -8.98856 | -63.65277 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 122aaf05-ff59-335e-ba68-b86dadd67bfa | -12.18183 | -47.20153 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63e5900f-af85-39fd-8002-bf604590921e | -12.93591 | -46.31208 | 2025-08-25 04:42:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 589deebc-14be-37a2-814c-5db2002d7075 | -8.21577 | -61.38417 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a5c852a8-86fa-3520-bef2-10b279cd281b | -8.0736 | -50.20443 | 2025-08-25 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a18fa4e-cc54-3cb9-8874-94ad55ccaa6c | -8.07112 | -49.68205 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21ae63fe-8391-3b34-b0f3-b88477a5f9f4 | -9.21101 | -59.44224 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a58d307c-5d67-350b-a5a4-00d9bb3a1fc4 | -13.49609 | -46.89066 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cef892d-3920-32b6-95e1-c0cb62ed5c90 | -8.07219 | -49.65366 | 2025-08-25 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b2558e5-3e25-3fb5-98a0-d20c2a3e7e0f | -9.19726 | -60.93007 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 803e9ee9-8926-3cad-862d-504faf28c794 | -6.80991 | -58.95827 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8d11495-46de-3695-b307-ef5f1c1808ec | -9.17892 | -59.45765 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bf05571-9650-38c0-b11a-44674864df9e | -10.60485 | -54.88314 | 2025-08-25 04:42:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2efbaba2-7938-3be1-ab75-c4a3307cc320 | -9.19265 | -59.47482 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10675a1a-2f78-3728-a5a2-8f37ef505342 | -9.69192 | -48.33806 | 2025-08-25 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd7baf93-1e47-3b74-b66b-b83276aa2907 | -13.40084 | -51.80381 | 2025-08-25 04:42:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 568441ad-4844-3f3f-ab45-ce955846bf63 | -11.28749 | -44.97175 | 2025-08-25 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cef1b1de-1305-36cb-8b2e-c100f64b4ea9 | -8.68812 | -62.87207 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2396ad79-e72e-32df-a13f-a970d9484f84 | -13.45019 | -46.91732 | 2025-08-25 04:42:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13a2193f-0869-3fdd-848d-f62be07b97de | -9.20997 | -60.9282 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef9f2dc2-b5cf-3da5-aee5-05f89fdd618a | -12.49706 | -53.83076 | 2025-08-25 04:42:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57ebacb0-adc1-3c08-bb3d-177203eafe3b | -8.62504 | -62.63564 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b7caac-c2e9-3df7-9bc4-85c7e0b7dd4c | -10.89548 | -55.79564 | 2025-08-25 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b213799-c5a7-3aed-b397-f4a3a4b03f2d | -9.16182 | -59.52017 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff92fd6c-b553-3126-929b-3c634677ff32 | -8.23412 | -61.42358 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd072dcd-c029-328c-9144-8de6d1cb448d | -8.98991 | -63.64598 | 2025-08-25 04:42:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d67bba2-f464-3510-8706-e695fd026b8c | -9.23464 | -60.92838 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a1a53e7-467e-3b67-9ede-86f0e28c9cf2 | -9.19891 | -60.92134 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f1dfcaf6-b2df-32d7-a8d5-2e8537794e1b | -11.64315 | -46.21453 | 2025-08-25 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 220ac106-14be-36fc-a76b-433de23da3af | -8.87506 | -62.4406 | 2025-08-25 04:42:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5c144048-7385-3d04-bf81-4be009ecab72 | -8.62789 | -62.63724 | 2025-08-25 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fec9d9a-75d5-320a-8b82-e91de862e85b | -8.21855 | -61.38283 | 2025-08-25 04:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 263cc0aa-7b5a-362b-843a-41cbd2bdffc9 | -11.17684 | -55.02907 | 2025-08-25 04:42:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8bef2b9-24a8-3ef8-82a4-2f874b229766 | -10.72162 | -47.11846 | 2025-08-25 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 346c2ecb-fea3-3c06-a4c7-36bdf9c76753 | -13.61262 | -48.17631 | 2025-08-25 04:42:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85adac92-fc41-3b8f-901b-f9aed0cdd5e4 | -11.03424 | -59.17735 | 2025-08-25 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb99477d-a910-3ce9-bf5f-3fe0464285f4 | -6.82634 | -58.96118 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a953df8-5168-38c5-bdbd-1a3c0dec0d4f | -6.81534 | -58.9582 | 2025-08-25 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bcec169-9465-392c-821c-64136a5a12ea | -9.26369 | -59.77006 | 2025-08-25 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4d64c1d-c86e-3de1-9d9e-2432c5130f06 | -9.5238 | -60.5252 | 2025-08-25 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 532773f9-7f18-301c-b0de-9383ecb5f930 | -8.29722 | -46.36128 | 2025-08-25 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee9a775c-848e-3bb3-9900-edf776b4e45c | -6.33687 | -58.18822 | 2025-08-25 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README51.md)
