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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bac3773-b6ed-3edf-851a-7ec9a871b5c6 | -6.19417 | -52.37126 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aabbec4e-9d4e-38dd-8441-0cd8a416edbf | -10.87797 | -50.22839 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f286bbc-4064-3a8d-852f-52a5c5c37f86 | -9.18433 | -59.46205 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df20be4e-8f14-3857-b8e1-9925000e3f36 | -7.01861 | -59.55603 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 761aacbb-33c9-34b3-8710-8623c4bad44a | -11.16066 | -54.01065 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 155c506e-147a-3d45-9923-9c30a17d0341 | -10.89542 | -50.27726 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4086ffea-23aa-31a5-8e5a-0ae6a8456d13 | -10.30464 | -48.22549 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a53e9db7-294d-3127-915f-9684f621946e | -6.86056 | -59.02657 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 59e16c7b-e8af-3e31-a660-c17b1271afc4 | -11.3966 | -47.20618 | 2026-08-22 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca9662f2-60d1-3276-8a4a-e4de1fe41128 | -6.86477 | -59.03222 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c9e80ba6-7f45-34c6-a6f5-e19e7a59ab17 | -10.52065 | -50.77353 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9d1d41a-9146-3a8d-be07-8a8675bd29e8 | -13.39075 | -54.36581 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6ab4507-0ac3-372d-ae97-832129862325 | -6.53942 | -58.51933 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3e20dc12-f8b2-3ea1-82b8-54c8b79f34c9 | -8.09713 | -50.03753 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 327649a2-4e20-3119-83ae-a430601b94e4 | -12.76075 | -47.10862 | 2026-08-22 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e479378-d804-384f-be2b-01a4d4e23e00 | -6.64819 | -56.34034 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6de73829-a641-3121-86eb-f034c3c9ff71 | -6.81894 | -59.40278 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c84137d7-f600-3007-a747-bcbd4bc0448b | -6.96221 | -59.05547 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ba27fc1b-8509-3de0-b147-e1116f14f9f2 | -8.51668 | -55.32017 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2507cba6-1a67-3538-978d-6b954c74d197 | -6.13655 | -59.90115 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe305faa-4d5c-3fdd-8732-abdc2864b374 | -13.25567 | -51.61359 | 2026-08-22 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5422f56b-b7de-37a0-82a4-d8f4c842fc6a | -12.85233 | -48.44195 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5974f44-eb2f-3a3c-843b-937e0abdf646 | -6.79268 | -58.63148 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2f90739-fae3-3a30-bd9e-3ff192a47c24 | -8.0935 | -50.03699 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8e7acb4-a698-3e7d-9075-15ee73339967 | -11.3491 | -46.0307 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f00f5a53-a01c-321a-8993-e6620ed0a761 | -12.80484 | -48.39796 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fe6f367-5a99-3ce3-8849-818d81e1c4c8 | -6.76829 | -58.6556 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| fc4276f1-4c27-35f3-a15c-e1ec4a883709 | -8.5256 | -54.81203 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| db3b81c0-4d7a-3421-a044-b9b76e977061 | -11.1204 | -46.19606 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b26872c-49d0-3323-b201-03f34f80ac25 | -6.65003 | -51.48745 | 2026-08-22 04:27:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 244cf2bd-da26-3bd8-af64-f3b1bc41c181 | -11.10325 | -49.89266 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b8a35d7-f523-32ff-b906-4f48926b701d | -6.75762 | -58.67345 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e90e9bfb-7c22-3566-bb4b-204e776563c3 | -8.09424 | -51.65743 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 748d2c18-9ec8-31b1-bf92-61e0438de835 | -6.1532 | -57.74499 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3352d3ba-1187-354a-9e44-e1b77d15fa68 | -9.19408 | -59.44765 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c72e984-d253-3914-9882-044d309fa546 | -6.77528 | -58.68958 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2dc25753-c9c2-3530-aafd-06e72f8ace43 | -7.34668 | -55.67029 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f0410bb2-646f-32fd-8bf6-9946daa7e3e0 | -11.05431 | -49.1089 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ab488539-b72e-31b1-9da0-7d0d7706a879 | -7.68598 | -46.16729 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc7f75d8-6f06-3e8d-a04c-ab6df1a94acd | -6.90707 | -58.99444 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b5a3fca2-123f-3853-a7c9-1886986edd12 | -6.80676 | -58.98782 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9082765c-7996-3b43-a42c-20eadb910754 | -9.00196 | -50.72377 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f67ad145-589a-3e4e-8dc8-20fdbad1c02f | -8.61588 | -54.72743 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9358ee7-080f-35e7-93ae-8ec13c0276f2 | -9.43716 | -51.63092 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c240a55c-afca-33a5-b255-e94cd8197c97 | -9.21678 | -59.77336 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 90a5679b-66b0-3d0f-ad12-d2a0fdd7d4c6 | -11.39991 | -47.20671 | 2026-08-22 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6204265-b932-3eae-88ed-a8f74d368611 | -9.16376 | -59.46397 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 263fcbcc-eeeb-3ed6-bc52-6000a5af8c81 | -11.4375 | -44.56133 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ea999b5-a2bd-31f0-8a92-459f0f0601e5 | -11.89775 | -55.47329 | 2026-08-22 04:27:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a0ae0f4-d9ff-358a-b4a1-613a9e42b01c | -9.4548 | -51.59771 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fb33034-9d8c-3a57-8a98-d63e89385f1f | -8.15726 | -46.72218 | 2026-08-22 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3321a62d-671f-3f62-bda3-380a3509fc7b | -10.52005 | -50.77638 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 437a4536-30a2-32a8-9782-69756ed0ac0b | -13.38212 | -41.34464 | 2026-08-22 04:27:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1390f27f-2ff9-3885-ace5-e6b3c5d58c8a | -14.12863 | -48.06723 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80e0085c-867e-3584-93b9-47f11da0081b | -7.55016 | -55.55957 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c22726b5-ebea-313b-a81d-828071f22de0 | -5.99832 | -57.79866 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 490dbe24-6a41-3e0a-bdd7-680fde4df68d | -10.5237 | -50.77704 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9768e6e5-63ed-30b3-acdd-ac12112cf847 | -8.09823 | -51.65802 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d69661e-c240-33e5-8b4b-8161b21344ef | -10.51556 | -50.82486 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6ac3dd6-5d41-38ae-8782-419d80e7fec7 | -8.52784 | -55.31598 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc70c61d-462a-3e9f-b9f5-dd527c6d876f | -15.44488 | -41.38845 | 2026-08-22 04:27:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 607adcd9-e1d7-3177-9c4e-4d893a71d263 | -9.03417 | -45.88425 | 2026-08-22 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b59ed6c-ad31-319b-8d19-227531c4cad1 | -13.45892 | -51.76593 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89b8fd37-c911-3b48-8dce-4497e6e098d9 | -7.25369 | -49.91774 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ade148eb-1e33-38ae-bc45-f34953a93256 | -6.94999 | -59.30813 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d56c346-eb22-394d-a416-4bb99aa00b42 | -11.38802 | -46.35514 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2dec31a-90b9-310f-bcb3-2245c67ae820 | -6.43523 | -54.96152 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b89cb84-6e7f-33a0-ae31-9263c32d92ee | -6.69614 | -58.94007 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 15c96fbf-eb0f-3699-81e8-c191e320cc10 | -6.69463 | -58.94162 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8a84f369-b221-3ba3-8df0-20af5a83027f | -10.29639 | -48.21299 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2a3c967-e921-39ba-9bee-6375f44f0476 | -6.82625 | -59.67577 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5076c33a-164b-369f-97ff-b6c00a038768 | -8.53083 | -55.32858 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d40c1ef1-839a-3836-8c89-06cdad523bd6 | -12.81864 | -48.4183 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f9ca186-45f2-374a-87ff-2097bff4ba9b | -6.37634 | -54.95025 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c8e65071-77f6-302a-816a-6bb63a6803d6 | -9.05082 | -50.87794 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3fd9d69d-66fb-32ac-b84a-f48da206a741 | -6.20868 | -55.63945 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8ce2f56-8985-33ae-93d6-8b695b5f37c0 | -12.28235 | -43.15785 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6473cc8e-368f-3d84-b113-7606c63d9151 | -8.5351 | -55.32752 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628a88db-65b5-3ee3-a94a-a6abd3c3b866 | -6.88743 | -56.43398 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1273f530-f748-3c7a-846a-21d50dc24db7 | -10.89475 | -50.28134 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e42e9616-5366-3968-9833-3dcca3e9023f | -11.55574 | -46.92484 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d56fbf49-e42c-3ed3-aa75-be9a9ec4c72f | -8.53433 | -54.84741 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fae8508a-8ffb-3cff-a41c-caa069e286c6 | -8.5268 | -55.32185 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b780e2d-8cef-383b-b8e4-abd54cbf4d25 | -11.79335 | -50.15817 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fe6ae2d-7185-3fa0-8453-9886f3764b33 | -7.74833 | -46.15925 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bda62a8-3ece-3d52-aabb-bfa3dc82e6fa | -9.26907 | -45.6421 | 2026-08-22 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c17d05c5-0e4b-3ad3-b2a3-06cffdc66a21 | -12.66706 | -47.80339 | 2026-08-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bd1c2f1-1be8-3c52-86de-0b1e9156fc61 | -10.27206 | -50.37605 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5cb01b9f-cf76-3308-bb32-3a0cae8c8b98 | -6.38038 | -54.95725 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| baaed703-e4e7-3555-b133-64921ee86b52 | -9.15747 | -59.4635 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e475c0d8-c026-3c2b-b35f-e5b03ca9cd35 | -9.43757 | -51.605 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f7d5b66-8a27-35be-aec6-a579ab898134 | -6.6649 | -56.34336 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee53c94-8730-36c6-b42f-d6cefb7a9535 | -9.18656 | -59.45192 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e8b78ec-a010-3246-b801-6e998294137e | -6.86712 | -59.02778 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 698eb71a-8b85-368c-821a-77bdd7dba1de | -6.93561 | -59.31144 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f40f08a-a862-3006-b86a-5c508d4b58db | -9.00099 | -50.74041 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ef380d2-fd14-378d-a310-8acb624bebe3 | -10.29582 | -50.3886 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af899c06-8f5d-3e7d-9352-7b5932d3d18a | -8.54315 | -54.8264 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 717d0125-e19a-3c47-8f56-c071be1653b4 | -6.75859 | -58.66806 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 7bf9fe19-c0fc-3fb9-bb35-899ee49dc6da | -13.25935 | -51.61422 | 2026-08-22 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README27.md)
