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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f1f8829-be77-3353-b893-d7e644656923 | -6.38544 | -54.95057 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb84b2f-d7ba-3f97-af87-d88dea4c90e1 | -8.55174 | -55.3223 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ac3e1c6-d446-366f-9df1-334a32739ec9 | -9.41651 | -60.40651 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d35e58d4-3bb3-3f4e-a5a6-1bd8d9dd0299 | -4.18816 | -49.4069 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa71e2b7-b012-3bc8-a1ed-4f6279fa8df2 | -8.5994 | -54.74093 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47e8b946-50f8-347f-8e54-cf1fd9bec276 | -7.37036 | -45.81099 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 9ccc251a-9dd8-36f1-8e51-3ad020a35a6e | -9.41539 | -60.41257 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 67274d9e-88d7-3d3b-a4bf-f3e3debb8a99 | -8.58591 | -54.75571 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 376b0207-940d-3fda-87ac-708643f7151b | -4.53762 | -55.61977 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50a91948-5668-347f-916d-d6d11124de26 | -9.41167 | -60.54747 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e851f684-ae96-362a-bf69-23a685ea5cba | -9.21886 | -59.76527 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3a55d823-8d8a-3f5e-8061-772de396fcfa | -6.3817 | -54.94995 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 703259da-1926-39a6-9e7b-b9bd6042f464 | -8.10046 | -51.67041 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30fce741-da11-3567-b822-46f2f7611998 | -6.24536 | -55.39773 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d20200c3-59c5-3beb-9914-684012decf23 | -6.87247 | -59.43645 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e32ea8b-70c5-3e34-9da7-908648439c94 | -7.37343 | -45.8192 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b369ae97-a14a-3c00-bc0e-4c10f0a8c226 | -7.46346 | -45.16353 | 2026-08-21 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa6421bb-d7ff-35ae-a362-71cd197132b6 | -6.66012 | -56.35663 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e959a65-5a24-3b06-a55a-253ba14a1bb4 | -8.57581 | -54.74974 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b8b1993-7816-3db2-bc76-ee277e9b5e48 | -8.54788 | -55.3096 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c18ce896-c26a-3e31-b771-ce2c52338259 | -6.22884 | -55.61475 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 68afd5d2-3e22-3132-aedb-fab104a38192 | -10.52906 | -50.8 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1538afd-1cd5-380a-aeae-520eb1aa0d4c | -6.87177 | -43.74544 | 2026-08-21 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62bbf018-fa8e-3a64-b2a7-fbb6cd49bd3f | -10.76401 | -50.31413 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b30b89ed-e203-32e6-9d7a-5a7f38d5c6d9 | -8.59873 | -54.74503 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bb9d4e0a-f655-3bb6-9818-bedae66aee44 | -6.5787 | -58.9609 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6354e2c6-b339-3d48-96ee-8a3c077ddb80 | -11.48899 | -45.10929 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 363375b8-a4b0-36b2-91b4-7f5b8d7d4c07 | -6.12825 | -59.90845 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6ff7b09-af09-3f05-b902-b3727492d105 | -6.99489 | -48.03474 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11d7b757-c890-322b-b4ef-e0f3bf72ab8f | -9.38888 | -60.55605 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99566ad1-66ed-30b5-b486-e79b8d16e0bc | -9.40997 | -60.55676 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0f50ca3-09d3-3ecf-89c6-c1e37d1a4f3a | -9.47951 | -51.63713 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61173083-bba8-3eb0-86d6-839a58ee8d51 | -8.50257 | -54.87195 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 724ea729-b372-3c30-83a2-5167886922b6 | -9.40918 | -60.41772 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 006729db-d5b0-3781-a47e-b596ca83ee13 | -9.39856 | -60.56111 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db04c6cc-0ba5-37ae-b91b-079220ec1e95 | -7.53646 | -55.57924 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb68100-837c-33be-806d-1c7c3fdd9dcd | -6.52091 | -45.90512 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40319377-b718-307e-95c9-b71b053f047b | -10.66368 | -49.02257 | 2026-08-21 04:46:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3db97eae-a57f-30be-b79e-5e952be45d20 | -6.96103 | -52.81449 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c85e5924-f1db-3a4e-b89a-86b140fd155c | -6.38244 | -54.94545 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edb77fee-ea18-32bb-b8d8-24b5790fed70 | -9.20845 | -60.76927 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bbe0189-28ab-3d22-a27c-7ed6e6ff5443 | -8.15741 | -55.37437 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29baf2e1-ab88-347b-ad01-0fc2434c27f2 | -6.64756 | -56.40628 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd2c343e-4ccc-3790-85ea-1cb90eb6959d | -8.59018 | -54.75215 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8cd38d4-fa5b-3ecf-a240-8364f1cbdc57 | -6.24351 | -55.39489 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b7598fa-3499-3d61-9147-c67f1a9ef540 | -6.43114 | -52.74575 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 906a212d-ba31-3e58-906d-e227e1d0d38f | -8.57941 | -54.75033 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a22b7b41-1ff6-37ac-964e-f1b3194bbab4 | -7.0608 | -56.50923 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70b2d15e-949b-3428-97e4-3ce2fb0f6624 | -5.60786 | -44.01199 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 587b1048-3e50-3b3b-93b8-ebb04223c709 | -5.99782 | -57.83549 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8551e566-1929-3e7b-828f-6b2046928a13 | -6.25002 | -55.39347 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c086734-a9aa-3f69-ba4e-6511b7423ea9 | -6.55037 | -56.26457 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa2b9189-73f2-3080-b60b-4d8bde68039e | -3.66475 | -49.18481 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5041047-22fc-3ffa-ba5e-18aacdf5d602 | -6.39063 | -54.94219 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24b0d6b0-084c-3895-8d27-8a548f3b7461 | -6.23274 | -55.41273 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd344e01-4b86-32b6-bdee-df1cc15a12d0 | -4.58494 | -59.94369 | 2026-08-21 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d5ece66-6757-3464-a13e-22cf18b41a39 | -6.20554 | -55.48286 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b35a5d1-9444-3e0f-9025-0e550621a833 | -8.11736 | -50.03938 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36ed48c6-78f8-3160-8931-8c6ee83050f5 | -9.41203 | -60.43076 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b18150b-6cf9-3b5c-8317-7103c1430488 | -6.75912 | -59.46742 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f452d62-e618-3fd3-bd2c-5670debf498e | -4.11641 | -48.93283 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fda2d34-86b3-3acf-a4a0-43d9673760e0 | -9.40693 | -60.42991 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 67a45036-dacd-330d-a8ce-ba66cadbdffe | -8.89702 | -60.54717 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fbe68293-ab7c-38a4-b568-94f7be82e467 | -6.1717 | -55.44751 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1844232-3a0d-3a89-af2e-e76d9323bdab | -9.40586 | -60.41877 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a98f683c-f584-35ff-9d77-997483c7ae1d | -7.36204 | -45.80973 | 2026-08-21 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b10188f5-65b9-3963-8db1-3f541d9f7c17 | -7.34004 | -55.68787 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f7574872-e5d3-32fa-a87c-0511968f0015 | -6.33254 | -46.52167 | 2026-08-21 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 289c6fb1-77f7-391b-b3c5-d6eef29745d8 | -6.86204 | -59.43753 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3aec289d-984a-3e6a-807d-36abbc933fd4 | -9.44925 | -51.611 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c863a237-6556-3798-bf40-8e07a3d437f7 | -8.02697 | -50.03307 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eb5d840-3660-3089-8d97-928391e3d303 | -5.81631 | -55.72266 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 187e971d-4f4f-327d-92fb-d26c8a0bfe07 | -10.24752 | -54.36435 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c773a21-511d-3473-be63-3d0595951de1 | -8.656 | -54.61891 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 259b8019-54a1-3155-85e9-5c04e4e9782f | -6.24439 | -55.42704 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f784add-b765-3116-b686-3eed8860f057 | -9.44379 | -51.62439 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a24d2a85-ab27-34fe-af57-2c4e7750b6db | -6.23506 | -55.39838 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18285447-1945-381e-8f22-c9a358b8f089 | -9.15901 | -59.66262 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d613a49-2a2a-3808-9459-25581a5aebcc | -6.70138 | -58.93423 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be676ae0-ea20-345e-b5fe-010d1edd1e5e | -10.52844 | -50.78146 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 539a2c95-8838-316e-aa46-a97d2e710c23 | -4.93336 | -55.78169 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd54abec-feb0-3fd0-95a6-3cc76c9ad2e5 | -6.82639 | -59.40664 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b0bb3019-b052-3eda-87e4-2c73881a9c34 | -9.43054 | -48.24647 | 2026-08-21 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3efc8c28-38dc-32b9-9d57-672612555a32 | -10.27722 | -50.28723 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 773b79a5-bbf3-3eb3-b485-d023b660c2c1 | -10.81789 | -50.99918 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55d87355-a035-3c2a-9651-aff82bc6cf90 | -10.24404 | -54.36379 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bff499d9-3b78-3061-898b-a2b97250383e | -5.80759 | -55.72645 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05157293-83cf-32dc-b3fe-3c913b60916a | -6.88519 | -56.43486 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39450962-52ba-38da-b918-0b1fe57fa6a5 | -8.09933 | -51.65602 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d381c779-a0a5-35fc-b641-598f8cbc80c3 | -10.10377 | -54.28163 | 2026-08-21 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cde7cfe4-95c8-3b58-8306-03ec9346eda7 | -7.86708 | -63.75849 | 2026-08-21 04:46:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e891e476-ff84-32bf-b03e-59e44562eb88 | -9.4168 | -60.54845 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 725b2d72-5938-330e-b440-d90fea98c575 | -6.87725 | -43.741 | 2026-08-21 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 34c2c34c-6aa4-3545-9f17-d74124f967ab | -7.15719 | -44.04967 | 2026-08-21 04:46:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d395c84-cb5d-3e34-a0d3-048cd15d5ee5 | -10.11921 | -48.81194 | 2026-08-21 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af1114b1-c15b-3ec3-b165-6d7fda50aa85 | -7.25071 | -49.90757 | 2026-08-21 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b932a5d9-29e5-3b25-8c9f-07548f33e615 | -8.06696 | -50.10984 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f67fff16-dc41-3716-8f8e-57cc8559806a | -10.28118 | -50.28405 | 2026-08-21 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aaf991cb-01c9-3148-930e-c1ed9dec744f | -6.61117 | -58.38969 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 109bb18e-ff94-38f3-bb0f-818fba17fe0e | -9.20708 | -59.77457 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README37.md)
