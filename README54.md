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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dfc88b3-c928-36c0-9d15-8ecf6170ec79 | -9.0588 | -50.46674 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f835e7e9-1a85-32c2-98ec-fc7aace2b6db | -10.44638 | -53.60636 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c099a3a-fc80-31f4-a453-234fbaa2aeca | -4.9925 | -56.25405 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8aa8f46-3d7f-3332-ac3f-2b397e08ec83 | -9.19377 | -46.03403 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb183de0-7be1-3814-bef2-4f93faf81035 | -7.87621 | -46.25492 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ddb8555-5865-3a66-8ee3-f16a2806cc2a | -8.82564 | -45.89622 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 30e17c72-68be-3d9b-9503-0bd78930242c | -6.96768 | -62.93177 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e441fe7b-2fe6-3fc5-9388-e215b5a679a5 | -9.99658 | -51.68283 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a346bfea-e8a5-3300-9e2c-52c47e24230a | -6.27169 | -43.69053 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0125724-b550-3d84-a431-948608096162 | -9.89945 | -53.79653 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f32a67a0-5d99-3b9a-8fbf-2cf30e43e295 | -3.83564 | -52.17375 | 2025-09-08 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b37506f6-059d-3c0c-86cf-f5888ab3b0cd | -5.87469 | -43.95542 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7cd77e9-caf6-3baf-a3d9-18e0775ade06 | -9.05464 | -50.47033 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 550f7197-7cb0-35d6-8b61-37c4174a5263 | -6.62698 | -53.35748 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be61b859-7c5c-3eb7-8f67-161412b28aaf | -7.02036 | -44.9435 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0836451-be39-36da-893e-eeae000a4342 | -7.70937 | -44.7235 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ced0879c-e182-371c-bb54-0fe850a7d842 | -6.46716 | -43.94456 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b391cbd-84f6-390f-9fd4-07c5d45a75f5 | -6.24716 | -43.71204 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48b98058-492f-31b6-8f6b-4fd14839d883 | -6.8459 | -52.85414 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9cbeb58-0afa-3fd2-929f-e4b4866d17b2 | -9.97952 | -51.68018 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b12128e4-f518-312f-9ae7-f28bd703d12e | -7.73951 | -50.31093 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aec56381-f2c4-3b97-b1cf-d68944624d19 | -5.22549 | -43.69363 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28c79faf-760d-3b55-a33d-3ead9da71fe7 | -8.04328 | -44.05642 | 2025-09-08 04:51:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10d10ad6-40cc-37d2-b8ad-052e6b47376f | -11.57635 | -44.65804 | 2025-09-08 04:51:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9c5e044-6cf5-3522-9702-9af66c593fe4 | -9.99255 | -51.66307 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95564a79-8956-3009-a4f3-4eb9dcf9442d | -9.08115 | -46.98756 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 61d6f136-b0bf-38cd-b392-f4e33de40ee4 | -6.81557 | -52.80639 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf3071c0-3436-3b9a-bd15-d2fe27314eeb | -7.85258 | -44.79561 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e33334be-7911-398b-8f3e-024a53c4f18d | -5.8871 | -43.95584 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ca23961-5c6a-3cc4-857f-a0e46e9cd3d2 | -9.83573 | -47.79585 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85cec2b0-7cf6-3b99-b118-8c3aac4b584c | -6.2826 | -53.42726 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa92aa5a-8613-3be5-b9dd-42d6851d3cb2 | -6.63858 | -53.36996 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 269a46f0-76bf-3ee6-92c4-8d8f8824b4f8 | -9.08672 | -50.4499 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd613a63-7855-3e28-83ce-881a5f32f508 | -8.607 | -54.67355 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fc437e1-0605-3306-b4a0-daa62a71907b | -5.10281 | -56.14799 | 2025-09-08 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9928a1cb-11d3-3160-96df-8cd3478f8454 | -6.21865 | -43.29691 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82500e7a-5ae4-3af1-9ee2-2a39d0e03ffa | -7.39804 | -61.62785 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3e8019f6-f803-3830-bec6-be67925b0e19 | -6.66813 | -43.84733 | 2025-09-08 04:51:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 639f4b65-f31d-3376-82a1-979f2d7b34cb | -4.30605 | -48.09632 | 2025-09-08 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f16091f-bace-37ec-8855-0810dc25d87d | -5.5617 | -52.16676 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faaa0343-b72d-39c5-94e6-9f8213e7f224 | -11.03162 | -45.94828 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 16651ef1-acd5-3af6-be19-3750db66d18c | -7.3518 | -43.94338 | 2025-09-08 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3806814-e5c4-3ca1-aca1-30c0fc5690a8 | -6.67351 | -44.55786 | 2025-09-08 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea39cb33-c9ac-3f00-bf45-5683fd835d56 | -8.1975 | -44.77901 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9193172-06da-3b09-90c3-1d56e9168fd6 | -6.95508 | -62.93741 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3733d708-e9f6-36ae-a9a0-b6c55ec11dd7 | -6.00654 | -46.19139 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ff0a3dc-7121-31ff-b0bf-3b775f6aff9e | -9.08172 | -46.9835 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c1d33a1f-0638-31c9-91ee-6d11275cadb5 | -6.25764 | -43.71434 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ec1532-a384-3b12-b794-a8a036642233 | -5.98874 | -44.14834 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99fea472-3aef-3a54-8a5b-a24bc2967ed7 | -5.95205 | -53.795 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e87f528b-5c8f-39e9-8013-6e5beb8bcf58 | -9.14674 | -46.06329 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ae80b2f9-f12b-3aba-8354-d599a0b2aa9f | -3.3007 | -54.91366 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a1569ef-3077-3cac-8a69-4ac28c1aba9e | -5.21938 | -43.69911 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 003ce716-88cc-3e5a-b811-0ef72ec621d2 | -9.17006 | -59.38482 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a8a07e20-b486-38df-b74e-92c643a18afb | -10.14753 | -46.21016 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| d752ea19-af44-3a32-bd5a-5ff883fe5cf1 | -9.53919 | -59.0667 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78478961-6774-319e-99cb-a2ad4fa41887 | -10.28526 | -48.80281 | 2025-09-08 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b9334056-0cf0-34bf-afa7-a1c68493d3f8 | -7.11782 | -63.07037 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca05f10d-8bd6-3c0b-8d5a-1519296e8287 | -6.5391 | -44.79099 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c86a1b84-efdd-345b-aa31-44c04eaf23d2 | -7.9912 | -46.33626 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79e05cff-4125-361b-a207-6444803a5a94 | -10.95891 | -46.82251 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 866c5023-26f1-378c-832c-f6d95e12fce0 | -6.62974 | -53.36147 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e44543c-e98c-38b2-aaf0-ad4f40c82fdd | -8.14061 | -48.4753 | 2025-09-08 04:51:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47130be9-6ddb-37ee-8b84-d8ce0d1e0def | -7.47586 | -61.59233 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a86e67d3-c43d-3f21-b872-391c7da2c8f9 | -3.30425 | -54.9142 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a11e2bad-42cc-366b-9e54-07750e0a976f | -11.3238 | -46.54284 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12a7439d-73cc-3dbc-b631-07da116c5fef | -4.52764 | -54.84021 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49122f0e-90ee-3e99-8586-2b580ba2507b | -9.82264 | -53.31006 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3896cf4d-b66e-3423-883f-9ec93b98c4b1 | -6.40634 | -43.88034 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c86ad6ee-8f07-3624-9ef7-bc056966283e | -9.1978 | -46.03968 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b47f43eb-614c-3f13-9c1f-43406f477183 | -6.05374 | -52.216 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2adf6179-7c4d-317a-81f1-9b4d488a152e | -9.06296 | -50.46312 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f3468c8-9e1f-3d31-8591-7fbebc2730f2 | -6.25243 | -43.71297 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cf7548b-fe9e-35bb-a881-5a5fa17dbfe4 | -5.88495 | -43.95753 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59d4149f-2d4a-3bb8-b8e4-65c811c9316f | -5.88197 | -43.95477 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4a0ddd7-9116-382a-bf04-efcfc1ba6f03 | -9.99371 | -51.67868 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be226c38-c448-3503-bb92-def5aefbe3f0 | -6.40679 | -43.87716 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f31a624c-652e-3c54-b55f-bd8afdae5283 | -6.46155 | -43.94658 | 2025-09-08 04:51:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ab7738-abe2-30f9-b85c-3fd8fbe82ed0 | -7.47076 | -61.59146 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0559ca60-6e79-3e6d-ac5c-c38cd6b469f8 | -8.70111 | -45.31549 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94837b4a-6edc-3591-818c-8112f0b4074b | -9.03998 | -49.79935 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0472c025-8d54-3f9b-bc20-1e0ec7fcde08 | -5.73883 | -45.36951 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d1c4145-c8b1-3719-a327-d969011b955f | -9.9954 | -51.66744 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d7d6078-5bd1-336b-9b3f-6960df4a6c0d | -6.17196 | -51.5219 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 562764cc-85f4-34ff-8633-0d6d7109a30f | -7.78781 | -50.75739 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d701b757-6b56-3d23-9566-fadf672e984e | -7.97504 | -44.8358 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abd5e60b-e5d8-3f6d-983a-f893215ce3c5 | -7.80176 | -46.08467 | 2025-09-08 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc64a4cc-4ff5-3a0a-ac21-176b421f37a0 | -9.17218 | -59.37272 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7d672a2e-21b2-3171-8210-839411c5d914 | -7.4713 | -61.58846 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5b39e27-b7b1-33ac-87cf-bea1e8f74a1d | -7.78142 | -52.12881 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9015927-7218-3b2a-98b9-78aa3500f5e5 | -6.04733 | -44.42643 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f454dc1b-e7e9-34ad-b534-e720a683c845 | -5.87432 | -43.97216 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eb4050ed-faaa-365a-baa0-f3925a67c42a | -7.35226 | -43.94003 | 2025-09-08 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba445c8b-12a0-3bd4-9473-8f813ba0a21a | -6.26071 | -43.69184 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2573dba1-12ec-3d4b-828e-f3dd4ef3a063 | -6.61531 | -44.00149 | 2025-09-08 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5eeae48f-9d6e-3cde-8e37-095583340904 | -5.83801 | -52.20327 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 01c06ca6-ed03-3be7-989e-871cc0ed9c6a | -10.46623 | -53.63097 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b01599e3-ab64-3bbd-9381-1ba9cccc9ce2 | -6.15503 | -45.47281 | 2025-09-08 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 202997f2-9bbb-36fc-9541-403a62ef4839 | -9.98865 | -51.68915 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea3ab8e1-edb0-3040-94ac-deba13c0581d | -6.08127 | -43.35676 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README55.md)
