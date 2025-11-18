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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16f64560-2225-3d45-b30f-68d401c234a2 | -7.1806 | -45.50795 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce88e14c-f8ca-33e5-ab09-be04573ec3e5 | -6.72682 | -35.22079 | 2025-11-18 04:21:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b4db0360-5c86-384c-9fb3-759deb6c85ad | -6.04123 | -39.49403 | 2025-11-18 04:21:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| faacdbf7-8ad7-3e1e-a820-b4b4ba439317 | -3.40535 | -50.18932 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ddc986c0-0539-37f3-88c4-b260cba85432 | -7.62595 | -42.57759 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c39daca4-7516-3169-850b-fc1be5652461 | -4.6079 | -45.95113 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa1bcb14-9c10-3a2b-acd4-1d36692ea636 | -3.46643 | -50.11693 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 623a9564-5725-3d6e-a9a6-2180824ae777 | -8.55426 | -47.77977 | 2025-11-18 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46fea8ed-a74c-3de1-9d98-d64ff2171b28 | -11.42845 | -43.3178 | 2025-11-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea46bd4-d9ad-3edd-86ad-8da463f4bf2c | -9.8839 | -44.18255 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 305c3043-49e2-3c2a-bf32-bbdc59147990 | -5.55954 | -47.11056 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fde385ef-2504-3018-91dd-36a9ce601255 | -5.46267 | -40.97271 | 2025-11-18 04:21:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f89e44cf-893a-33db-a6b1-9ae42ff432fe | -10.14164 | -47.51356 | 2025-11-18 04:21:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5e81b46-631c-3826-8eef-f741a7f8054d | -11.05219 | -45.15761 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9b96d3f-fd19-39c6-836d-f9eeeedbd367 | -4.10918 | -45.8393 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02e04297-a146-3ae0-b272-7193dcf48954 | -4.61911 | -41.73346 | 2025-11-18 04:21:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ae470b6-fb7e-3eaa-a89b-0d8b6aa710e5 | -4.18453 | -44.24417 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc5439cb-2dd1-3fb3-a2b2-b1a753d8c74a | -10.84696 | -44.87971 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96f07489-7574-30ef-867d-60398f0ab534 | -4.1724 | -44.23525 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 309baf9c-3403-342b-b221-bb1a23b7af17 | -7.40639 | -40.06393 | 2025-11-18 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ff9a00c5-f0d3-3ecc-8ac7-13892c4eaa1a | -8.20131 | -49.79204 | 2025-11-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba489dcd-dd4e-3577-b06d-0af2e330c32b | -4.67405 | -45.9952 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43d31791-e736-3518-987b-514a23ae8ecc | -6.16142 | -44.69883 | 2025-11-18 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95bb713c-2789-38c3-9464-47ee607f109b | -6.6779 | -40.90804 | 2025-11-18 04:21:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1c2695b6-00d1-33f0-ac98-bcd1298b4bc4 | -3.18824 | -50.64872 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d70a239e-4172-3490-b194-24746cd13d9c | -11.21635 | -47.92751 | 2025-11-18 04:21:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bee2836-7d7e-38f8-9276-e6a51e576fb0 | -7.22046 | -47.98193 | 2025-11-18 04:21:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b13eac16-380b-3467-b078-5f0243105379 | -3.81197 | -47.49863 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f119a7d7-46f6-3ddc-83e8-710cbd6a8845 | -9.93697 | -47.86722 | 2025-11-18 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c38c7a3-52ff-3bef-a56d-06d7a6d1972f | -7.0707 | -46.0513 | 2025-11-18 04:21:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e482dc53-2ca1-3f2e-9d9f-d7172735b531 | -4.64616 | -45.52737 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc4a3eda-afb3-3061-ab67-f3b5ae7fc371 | -5.47593 | -41.40644 | 2025-11-18 04:21:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7e519fee-f5e0-3413-94fe-8ea65f6f142e | -8.21785 | -48.30411 | 2025-11-18 04:21:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7430d90d-378e-36be-bfa3-8efa03e19df7 | -4.70404 | -46.31483 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b916800-1fe9-3b9b-a9d6-ffba18ee5e34 | -6.09299 | -41.65908 | 2025-11-18 04:21:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| df69f7e8-08d0-3886-a00d-79e28c053e52 | -7.54834 | -47.06333 | 2025-11-18 04:21:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e37c6b4-a861-3833-bc43-7c2bb4619be2 | -7.18392 | -45.50847 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e809e9a6-2c43-3b6d-8eb4-c3ae82520169 | -3.24466 | -50.50459 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5899400-3f7d-3324-b7a4-595bfe826c4d | -4.27355 | -44.24109 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4df20f2a-e079-3ded-8379-822424584300 | -10.58286 | -49.01041 | 2025-11-18 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d841d069-55ed-35fe-9f95-7ddad164ebfc | -7.86754 | -46.87053 | 2025-11-18 04:21:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d08024b-c0a8-3549-979b-ff58fe541c12 | -10.51723 | -43.96908 | 2025-11-18 04:21:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5214d03-5f3e-35da-a6a8-c5766bc7b3df | -6.43672 | -45.73499 | 2025-11-18 04:21:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbd1099c-a0b4-3bfd-9f11-183e2091a612 | -6.15936 | -46.10913 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a8a6003-772f-39ff-a4de-f192bd604332 | -5.96891 | -44.12398 | 2025-11-18 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1549b417-0c5b-3feb-b389-69f89da09c4b | -8.06051 | -46.85122 | 2025-11-18 04:21:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc865493-f748-3589-9171-af6a66f17c8d | -4.04776 | -47.50288 | 2025-11-18 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 608080ee-8ec1-3e03-a9b7-7933a6478fd0 | -8.43415 | -48.02193 | 2025-11-18 04:21:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9b23e3f-a007-366d-9a6f-8fb39234dc4e | -4.60376 | -45.94999 | 2025-11-18 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 092e327e-a87e-3ee6-9267-1308db8f5e6a | -4.19329 | -44.23145 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 62748e74-4bb0-3a2c-987b-ed9ae89d6153 | -4.19659 | -44.23196 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 82db3563-08bf-379e-b46c-48060fc037ff | -3.15098 | -51.48508 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b0827b9-6b70-300e-ae2d-7f7f2f5ffc11 | -7.43008 | -45.19796 | 2025-11-18 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5c10a2f-79bd-3322-8ec8-ba2a5f8e1ff9 | -4.18123 | -44.24366 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc1e686d-c942-3764-96fc-7891b31ecd19 | -6.31109 | -43.78319 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ebd732a5-fa34-3108-b405-d06367e9d5f3 | -6.67696 | -42.0356 | 2025-11-18 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 75fc472a-3acb-34b3-b8ac-35dba144d40d | -7.24929 | -39.39183 | 2025-11-18 04:21:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0b1d1d5-8526-3297-84a5-d3dab4292541 | -7.05899 | -45.54551 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29144b13-44c6-3e57-8167-063d74c43df0 | -9.88335 | -44.18614 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 631ed628-68f7-3607-92a1-81512bf18750 | -10.16203 | -48.15736 | 2025-11-18 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 632ea797-2b78-3c43-8bd6-74c370676016 | -3.51946 | -50.34663 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 245977a7-1d11-3794-bdbc-4e4dfae46912 | -9.02952 | -47.46327 | 2025-11-18 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 215c0db8-5e88-34c5-9da2-01e830063416 | -5.18897 | -46.07135 | 2025-11-18 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b114991-8413-3476-8366-ff63aade704d | -6.7278 | -46.3147 | 2025-11-18 04:21:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa459eee-607f-3092-bde6-eed94102eb88 | -3.3959 | -50.19211 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c7326d9b-499c-3276-948c-6f8b245bd962 | -3.18371 | -50.64799 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66401ff3-d6b8-396f-aac7-b579b6188c25 | -8.03601 | -48.93612 | 2025-11-18 04:21:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ba9742d-bc1b-3d2f-8c34-8ab2cb6aec4a | -7.41621 | -42.75535 | 2025-11-18 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 72ca2083-988a-3c3e-bfae-05c8d6b072ae | -10.38036 | -47.4944 | 2025-11-18 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d88e2e40-f9ff-3fc5-ab8a-86c27462dc55 | -7.33423 | -46.16716 | 2025-11-18 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0386ec64-2b31-3bf0-aec9-6947d95b27f1 | -8.31644 | -43.94004 | 2025-11-18 04:21:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1ebfae4-dc49-3955-a3b3-8973c30da3f0 | -3.18617 | -50.65369 | 2025-11-18 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd2ba05f-35fc-3733-8c6f-4cd5ab48a862 | -4.19008 | -53.43422 | 2025-11-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae43ceee-d5e2-3998-8b22-28b848b7e43b | -6.64649 | -43.81366 | 2025-11-18 04:21:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9bcee6b-6680-345e-a7ba-80aea4c3f011 | -7.30761 | -45.75811 | 2025-11-18 04:21:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c52139f7-8b89-3196-8fe3-c9996939206c | -4.52697 | -46.41515 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a247e3c3-392a-358e-b747-24c63e692613 | -3.64556 | -50.84233 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9b6310c-b012-3c5e-ab18-11d7d5145124 | -10.58724 | -49.00668 | 2025-11-18 04:21:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 565f9813-a26d-32a0-85c2-197fb09dd675 | -9.88055 | -44.18203 | 2025-11-18 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5c83d02c-9a61-334b-a74b-682da3d63fe9 | -10.36109 | -48.92188 | 2025-11-18 04:21:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1bcad909-dd95-3218-a44e-d4a766487572 | -4.19605 | -44.2354 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 911ca080-22b1-32ae-90a1-37a199b00479 | -9.22936 | -45.5688 | 2025-11-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0b86182-ebed-338f-8d2a-c1a54fd0a962 | -4.18284 | -44.23335 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fdb1a38e-a8b8-3ede-bfd0-47f8044de69c | -5.74086 | -46.28667 | 2025-11-18 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a643c28-9be9-3d85-b1fd-0c066d358125 | -10.74897 | -48.03347 | 2025-11-18 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35949de6-12b2-30f3-8c72-d22481a0c94e | -10.66126 | -49.37273 | 2025-11-18 04:21:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 105f5e43-6fac-360d-9d94-cfaeabb2313f | -3.16397 | -51.49461 | 2025-11-18 04:21:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 12f2b039-a305-3ae6-ac3a-c982fd9164fb | -5.4055 | -49.81138 | 2025-11-18 04:21:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a95ad926-ee10-3b6f-9e9a-86055a76223a | -4.27523 | -44.25191 | 2025-11-18 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65a55885-5b19-3bd6-910e-e0408e356387 | -4.72888 | -46.38042 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ebdf7f7-0f6d-3bd0-9226-0a621441c3b0 | -3.40589 | -50.26799 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1582c0d6-a36e-342e-af0b-6ffbe4c9c1f2 | -4.64951 | -45.52789 | 2025-11-18 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aee0622-586b-30f3-bfaa-36cdbbe1541d | -3.64176 | -50.83695 | 2025-11-18 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e15bfb3f-fd07-37eb-9f9c-a47f178745c3 | -5.01257 | -42.3975 | 2025-11-18 04:21:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fbc4c98d-cb0a-34a5-8bf4-9bee34eb5187 | -11.20737 | -43.17715 | 2025-11-18 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 49d407ce-574f-3f57-a2ce-ecc4d67b09ff | -2.34113 | -55.80138 | 2025-11-18 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2cdf843e-480b-3ecc-a543-ced5faeb3181 | -10.87386 | -49.54171 | 2025-11-18 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d70baca-17a2-30a1-b704-f8c46382e11c | -5.84282 | -49.87132 | 2025-11-18 04:21:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28ad6d82-57a4-31cc-bf29-06df3b40e8e6 | -4.74991 | -46.39896 | 2025-11-18 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3178ea01-7e91-3fff-a4ce-669aeaedad17 | -10.64778 | -49.72981 | 2025-11-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README28.md)
