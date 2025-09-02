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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3eedbef-1bba-3e67-8696-337eecd4f0a8 | -11.674 | -52.18597 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 50dfaba3-a332-342f-be3a-6ade9ec8ad05 | -3.72394 | -58.84031 | 2025-09-02 05:31:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 060d65b3-d30e-3bf7-8206-e404d3a3f040 | -11.85409 | -51.47493 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f36b11ab-a280-3322-9c73-66d2dacfd8df | -9.37464 | -63.50192 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25ad75ae-eeec-320f-96ee-48fe27580f71 | -8.64331 | -63.27161 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20fc9fcf-9d47-3955-bc83-26000b060a54 | -11.65982 | -52.20238 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bdbca592-6be0-3b23-824b-fd37fd55f69e | -6.15293 | -62.52904 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18b464ce-98f6-35fe-bf7a-61a69bb237d9 | -9.19831 | -60.25055 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5422b92c-0a78-3744-910e-040f45d3a823 | -6.8547 | -52.81137 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5e00602-d56c-3062-8483-4fc12e81be03 | -7.54454 | -61.3354 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6320b39a-5631-3326-88fe-2143609f86a3 | -8.55513 | -63.01608 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc02f44f-5a54-3093-9f4d-27fa59e40ae0 | -6.82926 | -52.83541 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38577871-ad68-3a96-8dc9-96528450fd44 | -8.66725 | -62.8475 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7b1ffaf-6837-3ece-be76-94efdee39d26 | -9.64592 | -63.11574 | 2025-09-02 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1a8ed181-a90e-3d6c-a330-8c65bcda713e | -7.54229 | -61.32778 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 28fe2ea6-8f32-3581-ac21-5d7747d25065 | -8.69349 | -62.40079 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19da7b9c-60a2-3c0a-bbf5-43bed4ce58eb | -7.59973 | -61.61146 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c427cf6-19d6-3752-9d9c-82260ce411b5 | -8.55902 | -63.01311 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec618f57-1384-347a-b661-5dd0ab9c0b1e | -8.75329 | -62.42812 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0b342f1-f101-3443-a9de-2034e9cc3bf3 | -7.28283 | -60.65849 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3679dbc-5290-3d01-9465-1e69a981b75c | -6.82382 | -52.83474 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23b6fc47-18aa-34f1-9cf1-74312aca9fcb | -7.69639 | -50.27629 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c6a9d7c-08a9-3e03-8536-e0e431aead41 | -8.85568 | -50.57967 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4275821a-4961-38b4-b713-25b3473c2efa | -7.45265 | -63.16005 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bac59f23-7232-3a45-ae30-7222c9bfdd8e | -6.33599 | -53.43996 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e527c721-28a1-38ec-8241-83c9e3bce1e8 | -6.42843 | -55.61802 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f6e1d99-4c84-39d3-a867-c6456b585419 | -10.44222 | -54.77494 | 2025-09-02 05:31:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1425ff9b-97fd-326a-82f0-49b76588abc2 | -11.66345 | -52.17095 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e53ec6f9-5f30-3968-aaaa-88e0ce819f83 | -6.83205 | -52.81487 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b80eaee4-74a5-3ad2-bf8f-9e87aab60a30 | -7.70596 | -61.10462 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3576655-972c-349b-926a-2022793dc3b9 | -5.32165 | -56.00211 | 2025-09-02 05:31:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f27c9e5e-0237-3969-a569-c47f4f19e5ba | -10.67489 | -60.77124 | 2025-09-02 05:31:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d492d5a-b087-3f76-9c12-4262b6bb5c2b | -7.69572 | -50.28149 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 69f81e8b-bac2-39fc-81f8-353217b2b093 | -8.76376 | -61.43621 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a099ab9e-c44b-31c5-9720-545757ff9240 | -8.76993 | -61.44084 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed62c357-b1e0-34e7-a531-543b861fc723 | -8.50671 | -63.90464 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b43d80c7-7b1d-3a47-ab3a-1ec286e599e3 | -6.79652 | -52.82496 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dfdd853-c05b-3b5e-a3be-3ca76cdb6735 | -9.26904 | -59.74859 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a7e2b09-6c45-3aa0-a602-dcdaa05d3782 | -9.7267 | -48.96075 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cb672dc-ad7d-36ec-ae96-b58386898766 | -6.82221 | -52.83894 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06fd1a95-af1e-3151-87b4-a4d6cb45a45f | -4.12188 | -56.3429 | 2025-09-02 05:31:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7d870f5-cf53-3356-b62c-0d7837a16e47 | -11.67085 | -52.21304 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3db4dc42-e378-3e28-bc6d-a6a7db28c2fe | -7.60362 | -61.60848 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 08687b45-2f8e-3ec9-a3ac-280a21a2f791 | -9.83614 | -63.87193 | 2025-09-02 05:31:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f5f517-4e12-3a38-8a32-ceb789b4da55 | -11.66926 | -52.16113 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e2474e5-ed5f-3189-9d0e-973d51421143 | -11.67467 | -52.21682 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 32b46aa1-9284-3dd6-8497-dd93e34f8986 | -11.8535 | -51.48013 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb333ae8-cbb4-306e-829c-73df30713754 | -6.83561 | -52.82942 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db1b9450-592d-3c3b-b617-4550834351e7 | -7.67838 | -61.08191 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36c2b985-7cff-314d-93b0-50abf6eacb8e | -6.81677 | -52.8383 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef5d46e-c2cf-3480-8703-df61d19784fe | -11.66919 | -52.21156 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 72f9d20b-c2d6-33ec-a258-9cde7fe6740d | -6.84833 | -52.81739 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3449b3c8-ac71-32b1-b470-12d936e8d67d | -6.81478 | -52.81973 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b718a5be-4168-350d-bb46-0925000bbf95 | -8.75274 | -62.43161 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 097854d9-3ed0-33fe-8591-fffecc8a2cfb | -11.66426 | -52.20186 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ca3534a2-f78f-3ba3-a2e5-cbc9acc3d228 | -9.73639 | -48.96755 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bae90cbf-4762-363a-af27-19469237c811 | -5.14989 | -60.37193 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b5854a0-ab7c-377f-b8b4-4e0d90ca274f | -6.4038 | -58.20827 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fc6054de-d6ed-31c2-b9b4-4fb61591a54d | -10.38983 | -59.41631 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0e974e-fba6-3ea1-9028-8e332782633f | -7.08167 | -63.07217 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1aec91f-f61f-3a7c-a861-c369c52fe4e0 | -8.97424 | -65.96947 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e768911-a0ce-3ed8-bdd5-d247e93250c8 | -7.50411 | -63.49314 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3a36615-a52f-366e-a168-8892f70d619f | -8.67686 | -62.39814 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5e8d4da-172d-3021-ab13-743b84d486b0 | -9.18656 | -60.81993 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d05c76-254e-3599-b91c-d5e71e9848b6 | -7.60028 | -61.60795 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56b56182-ce8c-331b-952c-d6ec082d03ef | -6.82466 | -52.82182 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87dec33a-bcea-34a5-8b6d-48add19ac91d | -7.69585 | -61.10305 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b5c0163-50c9-3051-b41b-004689cf3344 | -7.70174 | -50.28211 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 195f29c4-af45-321f-853c-0a17138f7abd | -11.66757 | -52.17488 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee329e52-7104-31c1-9ec8-4abe73c62d57 | -10.75468 | -49.57323 | 2025-09-02 05:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bef157f3-baca-386d-b570-8263ddc79c20 | -7.69529 | -61.10664 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c735332-f013-32b7-8706-3180f0778c48 | -8.73065 | -62.42459 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca3043b2-e6f1-35b6-8a5d-ce36e1a421e6 | -8.42354 | -62.29336 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3098e16-4fe0-3ad1-8351-0fa8ef3ed2af | -9.26065 | -59.75574 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab883e37-df3f-377c-af6c-3fe8492f6ba0 | -11.65823 | -52.20093 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 44112fbc-7bcc-32e3-a466-92721ab637d7 | -9.33971 | -55.21739 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08bb00cf-6820-32dc-80b3-b0a8cee23e20 | -10.34864 | -59.20564 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21c2e1dc-744a-3f47-bba1-f79dd9b42d0d | -6.13571 | -62.52988 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcea1de8-1a63-377d-ad43-8c0f951ad67e | -6.83206 | -52.80883 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b063fc9-ac70-3c57-838b-7df6fa138ab4 | -6.92533 | -63.13762 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7a2ba75-6835-3637-9862-f0fe71bd6cf3 | -6.00542 | -57.8564 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a6dd9cf-81bc-382d-8ea6-001b6c60f3b5 | -6.82417 | -52.82524 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3d88709-fae0-3894-9aeb-9a249f84d0af | -11.66646 | -52.18391 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c87aff26-6947-3eae-99ac-505af237e663 | -9.83591 | -48.61723 | 2025-09-02 05:31:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5761b0bc-46ea-3b49-ba01-0a6b97316464 | -8.65432 | -67.24815 | 2025-09-02 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8057fc40-3a9f-3078-bff1-4e6f5943ce64 | -7.59256 | -61.63552 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89c3654c-fbd1-3c6b-912e-45b91f8743b3 | -8.93402 | -65.94071 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f2994ca-f6d2-3333-93b0-47b7727495bc | -9.46582 | -60.3139 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4949b5fb-6322-3690-992a-b19c48b2845f | -10.90178 | -50.83873 | 2025-09-02 05:31:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c9cecf6-faae-36d2-b391-fd9f6f92af74 | -11.66189 | -52.18451 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34f3a06f-e3c2-33ff-b681-45ffcc7290a2 | -7.28509 | -60.66634 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50ab7e06-400f-3640-931d-bea9d5e6bf32 | -6.98975 | -63.01393 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00764f78-938d-31d7-98d4-90871b54e3a3 | -8.56014 | -63.0061 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac108491-fdba-38c7-9878-afcebdd039a1 | -6.9864 | -63.0134 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80b931b-e844-3424-85f2-4eea1f7e88ad | -11.67308 | -52.18007 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2b86d716-bd2e-33c1-b9b9-51323d2a7d41 | -9.28553 | -61.01736 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a957a6dd-ccf4-3e76-9667-362a6d070eae | -11.66534 | -52.20771 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0369da74-9a17-3520-b4b7-901aec3ba53b | -11.66399 | -52.16632 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3813ff8d-c171-3f75-a60b-76fab76c36ea | -11.67293 | -52.1951 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 48257781-219b-35af-a6a3-51ae5558b195 | -11.84602 | -51.52539 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README76.md)
