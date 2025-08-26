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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9255fee7-1ffc-3712-825c-0874ad358680 | -9.1954 | -59.5336 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60aef647-cf5e-339e-9e48-4f7ed72ef7f3 | -9.2644 | -59.787601 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed8fc848-62be-3768-8553-d32c1ba1c8a8 | -9.1933 | -59.4356 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb28ffb-cf5b-371c-ad52-eb8cc651772e | -6.5644 | -51.071499 | 2025-08-26 01:32:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e05ea196-8f47-34b6-b658-ba3a23ad1e5f | -7.4239 | -60.622002 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 822218ef-301f-3ce7-b9d4-cbdf6e1016b9 | -9.6514 | -59.630901 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96c96855-569b-3519-a9af-0492aa1eab39 | -7.3789 | -64.345703 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b890509c-6a70-3459-81d7-36003d4a3972 | -9.8087 | -64.282204 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d3c6fc2f-3624-324a-a7cb-89a86ae89613 | -9.1904 | -59.5121 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b5c1297-3621-31d8-af24-32da5438d353 | -9.1673 | -59.456902 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3428b5c3-71e1-3f10-8f27-b839c5edf4e9 | -8.3252 | -50.538601 | 2025-08-26 01:32:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 025facdc-cc61-306e-bb6c-55173d64a3fb | -11.5535 | -52.136799 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a9ba0d0-df05-3d71-9f10-8f463f91526a | -9.1741 | -59.530998 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 877b95a7-58fa-3c00-b9a7-c1ac2b0a01fc | -4.9607 | -55.815498 | 2025-08-26 01:32:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be86bfd7-8c62-3657-9f4d-573b60ed4901 | -10.7471 | -60.721901 | 2025-08-26 01:32:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97dca8f1-d218-3ac9-8d4e-f174fe3c7443 | -9.1944 | -60.7854 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7cf10e2-6867-33f4-a710-6b3cd356874f | -11.3006 | -55.105999 | 2025-08-26 01:32:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87a2f5d2-56fc-36c5-8ec4-37e3eb27e608 | -7.4852 | -61.339298 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61866b91-6dd7-39c3-aa4f-a0681120081d | -8.7444 | -63.735699 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9295ec03-d7c9-3a40-a84c-402bbf1361f7 | -8.351 | -62.937199 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4925f1d1-7f25-3fd9-8391-bab53d8969ee | -6.2597 | -60.0051 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 553766d9-aa1e-3a9d-8f6c-bce54dd7cc65 | -6.7065 | -58.559101 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe72494b-c090-3b56-ab24-c37d565641ea | -6.8145 | -58.975498 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce7fae0-9585-339d-8f4d-3e9eec01e988 | -14.1129 | -53.971901 | 2025-08-26 01:32:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4b6eddd-75ef-3e35-880e-eb3944d57e10 | -7.7448 | -50.279598 | 2025-08-26 01:32:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6e5807-d304-3601-967a-cdf328bc7e71 | -6.313 | -59.878799 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee34b5d1-4a90-3df1-8ef3-30931e9aa7ed | -6.7809 | -59.6717 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38498adf-a3ee-37f9-af1d-d4b00971dded | -7.5329 | -63.374298 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a35140d3-d66b-32b4-a9bf-195390f5e906 | -7.4419 | -60.6106 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c79471c5-3e44-3602-9018-86a74d10aa69 | -8.8453 | -62.4319 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c547b26b-5739-334e-a342-b761cd22687e | -10.5239 | -57.972401 | 2025-08-26 01:32:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb234994-a021-3859-b0d7-cdceec8c1a00 | -4.9577 | -55.8032 | 2025-08-26 01:32:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3e35d6-23d1-3f1c-8d7f-3f9ffd5f54a6 | -9.0329 | -65.718002 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66f9ee8d-9b0c-3a00-ae5f-9b1bc7ea1897 | -9.17 | -60.769199 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1582a9e-f28e-391b-a0cb-0c5452d7246b | -10.4244 | -60.300301 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a29fb450-a0ed-3921-a59a-4e956af10f3b | -9.152 | -60.780499 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65d05d01-4038-3724-bb74-8dcfccd38962 | -9.0057 | -65.402 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0160d3c0-a879-367c-b943-65d9ac56a9a2 | -9.2356 | -60.921001 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ebcbcde-6cd8-3379-8b2c-3dd8bc49e281 | -8.8583 | -62.444 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50991964-59ce-3f8c-8b71-5b529bfc0177 | -9.2128 | -59.431099 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc6d7504-56e2-332b-9179-06f402922691 | -6.8403 | -58.953201 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9522d92-1f4a-3675-963f-26a7d0e5fbf9 | -6.6948 | -58.553299 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91c6e003-9aec-3014-9dbe-eca5c13e6aff | -8.8501 | -62.4534 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 21ae1c1c-3e5b-320b-9c7a-8f38430b5ae1 | -8.5523 | -62.640499 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 490430f9-d4d7-3ee5-9b9a-9685dda6ba62 | -8.3221 | -50.565899 | 2025-08-26 01:32:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b2fd149-c133-307f-9c32-0981f46fc283 | -9.2666 | -56.901699 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 358161da-eb9f-379c-beac-661c2bfd9637 | -6.2483 | -60.000198 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1955e4a-fc1d-31c1-a5c6-17ab67abe773 | -10.8797 | -55.793598 | 2025-08-26 01:32:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| acdb448f-bd0e-3cdb-8739-beb0feb87b69 | -6.8421 | -58.960999 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96f32dae-4184-39b4-b016-d4fa402f4e89 | -9.0015 | -65.382599 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94c58b9e-f8a2-336e-93da-394e9b326598 | -6.8243 | -58.973202 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3bfb86b-1117-320f-a855-2a9a86d672e5 | -10.4262 | -64.387299 | 2025-08-26 01:32:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 13b4ef15-1afb-3425-9c69-27dfe12fdff3 | -9.3332 | -63.191002 | 2025-08-26 01:32:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 22cfffa1-3b79-3c62-b44d-d6796a0fd546 | -6.669 | -58.795101 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4417d74-4fe6-3fd2-8c0e-05699080c109 | -9.0448 | -65.726097 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2901e8-4768-3012-b07c-0b8608afae55 | -7.3967 | -64.333199 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae415c6-da68-3fcb-9ee7-e16eb5ee42a8 | -6.7856 | -59.647499 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14cc644f-4b68-389c-9c79-853be986cc5c | -6.2401 | -60.009602 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c82c9246-9763-313a-8570-e0a128ad3627 | -9.2547 | -56.894901 | 2025-08-26 01:32:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 10f4dcfb-5570-3463-88fd-0a0bb2604b6c | -9.1656 | -59.449699 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd5b2427-0967-33fd-b1d4-30372cec737e | -9.5259 | -60.520901 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31777738-f01a-3368-ac7b-23a3a8349265 | -8.1108 | -62.875401 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88633c0a-cb1d-3d50-beb1-f654511c8588 | -8.9903 | -65.425598 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e310f970-08fa-3dbe-8b47-ada5d940f440 | -8.3477 | -62.922501 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9f45d4e9-26a1-39ac-bd07-c889887f90bc | -13.4508 | -51.1675 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49360720-4519-3041-bc03-9f643fa241b5 | -8.6144 | -62.641899 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8a8f2324-1e78-365b-85ae-511763b91750 | -13.4363 | -51.151699 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59546e19-35f6-3b8b-b939-d75fddb51d15 | -7.4722 | -61.327801 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3dff41fb-0095-334d-96c2-5b246c3b7d17 | -6.8394 | -59.3465 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00638dbb-838b-3b33-93c4-cabeeabcba91 | -6.2385 | -60.002399 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7e433a3-e417-3462-8063-8a7e570c47bc | -6.5812 | -59.878399 | 2025-08-26 01:32:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64925243-efde-3867-bb52-14d3c698cca6 | -7.6217 | -61.034199 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4211e7d9-a089-3844-8d92-4f005a63815c | -7.3869 | -64.335297 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 858d1dcf-59fd-3976-8980-6f96915caa92 | -6.6574 | -58.789501 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0df24fd-8f38-3430-bdd0-1ea5222abf81 | -6.8385 | -58.945499 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ce028b9-70bd-36c6-ab0e-a9e2bd506db3 | -7.4868 | -61.3461 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 209a4083-cc04-36f8-991b-5f43587867a1 | -11.5438 | -52.1394 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58c77c3b-846c-37f3-8993-39b1ed7ee91a | -9.1779 | -60.8036 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2b5f109-d265-345a-8477-95c41592e00e | -9.1985 | -59.502701 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62d1fc9c-31ea-31c7-8f4c-4721137ccf1d | -11.3075 | -55.092602 | 2025-08-26 01:32:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e960782-04d1-30c7-aaeb-8dd654a8f261 | -9.1887 | -59.505001 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a36b7261-5541-34d1-ba9e-b7724ae6d13c | -8.3156 | -50.5411 | 2025-08-26 01:32:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c3daa51-678f-35dd-9dbf-39226232b7ac | -6.2499 | -60.007401 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3015931-10d0-36fb-9f6b-10373eed7b00 | -8.9024 | -62.456902 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ca96dae8-5587-339b-86bf-a98ab18fe1ed | -9.6416 | -59.633202 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a350581-86c5-34c6-845e-0a450754b07b | -10.7456 | -60.715 | 2025-08-26 01:32:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f4453be-b6a2-3e11-bd9d-d018f1da55e1 | -6.7907 | -59.669399 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81069022-2cf1-3ac5-921e-9a16f399f155 | -8.8665 | -62.4347 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f54cd98d-1c3c-32d2-8e66-82a7dddd1685 | -7.8819 | -63.0028 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3f45569d-fa11-3d0c-a707-7e25efc63d94 | -9.2002 | -59.509899 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5457511c-ca93-3a58-9d29-f2226c64c833 | -7.4207 | -60.6082 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5090b900-41a3-3f7b-ba9a-1b6cf1d86ac1 | -9.2547 | -65.6073 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d016bfd-1412-37c7-9cb7-90be9edab25c | -9.2742 | -59.785301 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 028e179f-ab52-3dc7-9a54-3619d84909b6 | -9.1852 | -59.445099 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2a04191-a66d-3406-a93a-706127af9d30 | -9.1861 | -60.794498 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2b5f4dd-43cd-376b-a802-e0154f63e2d8 | -9.166 | -59.540401 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3ca805b1-06f9-3552-a0ba-502714d9ed5a | -9.1633 | -60.785198 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8448f638-7672-336c-aeca-6e7ef86def92 | -9.2325 | -60.907299 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c6d20c2-3746-342c-b916-ee5c3daf7a8f | -7.4435 | -60.6175 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6b381ea6-6cc7-3341-9b97-481a4fcf8e95 | -9.1708 | -59.516701 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
