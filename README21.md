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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc1ce80e-07e6-326c-9c41-fc4372f5149b | -10.5169 | -42.42106 | 2024-12-01 03:27:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4e0fe5d3-4db1-3531-947c-207cea8c542f | -9.21003 | -36.57486 | 2024-12-01 03:27:00 | NOAA-20 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfc89bc0-7147-3f66-9ab9-3d7818222a61 | -6.91947 | -43.55548 | 2024-12-01 03:27:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a88cf00-7e2b-33e1-b8fb-b321895ca75d | -9.39442 | -39.9436 | 2024-12-01 03:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 732c0cb8-90cf-3420-886e-8a320b7338cb | -6.18531 | -44.42895 | 2024-12-01 03:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 179be2d9-3982-3d8e-b077-f00deb9cfbba | -5.18235 | -43.95442 | 2024-12-01 03:27:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84ee1c62-7b1c-3188-9883-b1582905d12a | -8.75186 | -38.78704 | 2024-12-01 03:27:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 262f7be7-5723-33f4-9bf2-d51f5fc735ad | -10.14021 | -36.41791 | 2024-12-01 03:27:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 4.7 |
| d84ce84b-d344-36ba-8ae3-cac5c957d5a6 | -10.13651 | -36.41729 | 2024-12-01 03:27:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc9f124c-700c-3870-85ce-589546f822e9 | -8.66549 | -35.7038 | 2024-12-01 03:27:00 | NOAA-20 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f1c5783-99b2-3bed-9010-26d5cf84b70b | -8.55127 | -35.75837 | 2024-12-01 03:27:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8cc80604-4f69-39f0-97a4-acc32f48862d | -7.2191 | -39.04937 | 2024-12-01 03:27:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1bb36823-e738-3935-b948-a7ec93be8883 | -4.44611 | -45.36733 | 2024-12-01 03:27:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bbeedb6-6973-3bcf-af5d-f420dc6d6aee | -5.91042 | -43.85163 | 2024-12-01 03:27:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c5ee45c-bba9-3c82-8cca-0c354eca679e | -5.14109 | -44.22072 | 2024-12-01 03:27:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ca6bb25-55da-302d-84f0-68ca59a31182 | -9.51626 | -36.04284 | 2024-12-01 03:27:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9a674deb-47d1-35c5-8c89-9546aa5894fe | -6.40079 | -39.88309 | 2024-12-01 03:27:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d2d7c60-9ed3-3f84-ace7-81aa0836282c | -8.07174 | -34.97729 | 2024-12-01 03:27:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4e1ccab6-580d-38fc-97fd-2e2dd345c2c9 | -10.69507 | -37.0483 | 2024-12-01 03:27:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 26cd2940-22bb-3cd6-9775-49f225bfdfa0 | -6.86491 | -39.91694 | 2024-12-01 03:27:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ac00ba2-b500-3dd2-89c2-0b83e4c03198 | -7.11937 | -38.66838 | 2024-12-01 03:27:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e283a94-629b-35af-a27f-ef600dee442a | -6.19186 | -44.43037 | 2024-12-01 03:27:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13819231-7195-31fc-ab3b-140147b39787 | -8.6662 | -35.69955 | 2024-12-01 03:27:00 | NOAA-20 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1dc256ca-742c-3d18-abeb-b3641d3109e5 | -5.91041 | -43.84314 | 2024-12-01 03:27:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2428bfe0-22ea-3949-817a-1b92fdb55951 | -6.9274 | -43.54687 | 2024-12-01 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| fcedbb8d-2d33-3c55-882c-3094cc1cca15 | -8.74615 | -35.91607 | 2024-12-01 03:27:00 | NOAA-20 | LAGOA DOS GATOS | PERNAMBUCO | Brasil | 2608701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9d5e63c6-c78a-390a-98ce-fdbcedd09fbc | -8.93342 | -44.25492 | 2024-12-01 03:27:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b379cc5a-93c9-355e-bda3-25747962390b | -6.9344 | -43.5401 | 2024-12-01 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f10a7c56-3554-31a3-b5ea-02792a23d922 | -3.259 | -53.6388 | 2024-12-01 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 387089db-ee82-34ba-ba7a-050ed23c0e14 | -2.8013 | -53.043 | 2024-12-01 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a3f1c195-d151-3a5f-8b2b-c18d6b9fd806 | 1.1438 | -56.0067 | 2024-12-01 03:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 66897dfa-4205-38c7-adc6-69b8b063406b | 1.1622 | -55.9672 | 2024-12-01 03:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| fbf18b6c-18f2-3f5c-8239-ae8db1b8a3c2 | -3.4974 | -53.8339 | 2024-12-01 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7b06cfbc-71f7-3daa-be92-b797f6c3525f | -3.1273 | -54.5264 | 2024-12-01 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2859eb97-62db-38f1-897f-9e2d329b57f3 | 1.1439 | -55.9871 | 2024-12-01 03:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 611721e8-91e1-303a-ae27-e0be7bceb31f | -4.5578 | -45.7232 | 2024-12-01 03:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 120.0 |
| a0ed8e5b-0acb-376f-852f-a1cb40d4a000 | -10.6674 | -44.4835 | 2024-12-01 03:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4c6b8898-4678-3c1a-9723-04bcede04f0d | -2.7503 | -51.7553 | 2024-12-01 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| be0a9a32-7b3c-3917-82c0-ce03b5dd63da | -3.2591 | -53.6186 | 2024-12-01 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0b748fff-f91e-3f53-b258-2e837da28b0c | 1.1622 | -55.9869 | 2024-12-01 03:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3d4efdf4-dba9-3fed-a41a-2cb293969e44 | -6.9156 | -43.5418 | 2024-12-01 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a8e1b205-d587-32bf-b3ce-63241384e067 | -2.6578 | -51.8811 | 2024-12-01 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 146387d4-2fc4-33c2-8835-1d44c132a94a | -4.5562 | -43.3028 | 2024-12-01 03:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| f7d117c5-aeff-3320-af44-037554fbe983 | -3.8171 | -52.2583 | 2024-12-01 03:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 7e96a46d-8fc4-34fb-a347-f8d94549286a | -4.5375 | -43.304 | 2024-12-01 03:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 620c8e8a-adda-3a77-b097-d0a5e4581e94 | -22.6741 | -42.85943 | 2024-12-01 03:32:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d26c8c68-3981-30d4-91dc-a71a51fa910e | 1.1439 | -55.9871 | 2024-12-01 03:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 341649fb-3dec-3b73-be1e-4ca31b317e14 | 1.1621 | -56.0066 | 2024-12-01 03:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4f3503b4-1f33-3c59-986d-10ae526e8f97 | 1.1438 | -56.0067 | 2024-12-01 03:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7554e802-3ab5-3249-a7b1-e4c08d64d5e6 | 1.1622 | -55.9672 | 2024-12-01 03:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 0ea8dd84-4269-3d38-985d-d827bdaab252 | -3.2591 | -53.6186 | 2024-12-01 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a264ca70-061d-398f-a1f0-6f09184da977 | -2.6578 | -51.8811 | 2024-12-01 03:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 73c7df3a-948e-36ca-a91f-7d71d4bdebd8 | 1.1622 | -55.9869 | 2024-12-01 03:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| a8210427-a6f1-3646-8c3a-bf8d38a26d93 | -3.259 | -53.6388 | 2024-12-01 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| b863be07-d787-36c1-bbd4-6a1b2504e637 | -4.556 | -43.3261 | 2024-12-01 03:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 80216365-f90c-3d7e-8ca1-53239821e173 | -6.9344 | -43.5401 | 2024-12-01 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ad7eb18d-972d-3653-9b9a-543bd60b1f3f | -3.4974 | -53.8339 | 2024-12-01 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7b93429e-5722-36cb-a4bd-2a8406f5f508 | -4.5562 | -43.3028 | 2024-12-01 03:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 7dd534f2-6401-30fd-84e3-5475e81229c9 | -4.5578 | -45.7232 | 2024-12-01 03:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 104.2 |
| f1c61542-18ab-3099-a8bf-bbcacc628f22 | -3.1273 | -54.5264 | 2024-12-01 03:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d7e5491a-5c9f-3cc1-ba08-75a13b86a82c | -3.2774 | -53.6383 | 2024-12-01 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 050eaa17-90ff-31b5-9fa5-f85e60d16fc3 | -4.5563 | -43.2795 | 2024-12-01 03:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 8689b388-badb-3765-839a-cb457bb18c4f | -3.259 | -53.6388 | 2024-12-01 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ac395c0d-a5d6-39a6-8747-9040c0e86fc9 | 1.1439 | -55.9871 | 2024-12-01 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| b003281b-388f-3ec7-af91-05f49724efe6 | -10.6674 | -44.4835 | 2024-12-01 03:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| c3754154-119d-3c15-957d-5b3f3709dbd1 | -3.1273 | -54.5264 | 2024-12-01 03:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| c8d436e2-6e50-3f04-afad-dc677e8432ea | -3.2591 | -53.6186 | 2024-12-01 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d026dd8b-f35e-3b3c-8bd0-5769fe1f9095 | -3.4974 | -53.8339 | 2024-12-01 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 3440ed75-d1d9-336b-8d6a-57ce9dc1d1a9 | 3.2755 | -60.0781 | 2024-12-01 03:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 22c5320e-19a5-3d3e-b0de-f87ee2c63e0b | -6.9344 | -43.5401 | 2024-12-01 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 03fa66f1-b168-3fb1-b951-e4c980e5a8c2 | -3.2774 | -53.6383 | 2024-12-01 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 5bb5f2a6-3a6d-33a5-ab01-f2c82a61318c | -4.5563 | -43.2795 | 2024-12-01 03:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c2803d98-00c0-3cb8-b270-7ab3782e6ce9 | -4.5578 | -45.7232 | 2024-12-01 03:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0032f5ba-1d7d-39db-a192-a6d3b0d40ee5 | -4.5562 | -43.3028 | 2024-12-01 03:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 15c7a6c8-ce65-32de-92ba-d2e64ecddfea | -2.9963 | -45.5706 | 2024-12-01 03:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| d822e74d-8d21-3d56-a4c3-ba4bd4bb4a3b | -4.0052 | -44.7596 | 2024-12-01 03:50:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4a6fe983-c652-31ac-aca6-d68f5a4d45e4 | 1.1621 | -56.0066 | 2024-12-01 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 80202e52-f103-340e-9f5a-8e836e15af7b | 1.1622 | -55.9869 | 2024-12-01 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| c2230594-7bad-3f9d-9818-fbdb059129b2 | -2.6578 | -51.8811 | 2024-12-01 03:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 532646e2-1a05-384e-a6a0-c4474d717b1f | -2.7503 | -51.7553 | 2024-12-01 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 09495206-9968-39e0-a009-041ee58ee769 | -2.6578 | -51.8811 | 2024-12-01 04:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ba3cfa48-3c7f-326c-9236-f2d36ff199d5 | -3.259 | -53.6388 | 2024-12-01 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| edbdc4a5-9292-3cc8-8b25-a098a70294be | -2.9963 | -45.5706 | 2024-12-01 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| edee9429-74e5-3cf3-b993-40454155a09d | -2.9778 | -45.5713 | 2024-12-01 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 19109779-061d-3e06-a3b9-968cf96ccac8 | -2.8197 | -53.0425 | 2024-12-01 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d2e07841-d4b9-3409-9dad-4e4f510d5741 | -3.4974 | -53.8339 | 2024-12-01 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1c120974-04cd-37cc-b946-685f4330c8c1 | -3.2591 | -53.6186 | 2024-12-01 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c1404104-7f5a-33a6-9605-ae5ffd1a2304 | -2.8013 | -53.043 | 2024-12-01 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 35d6e8a2-9045-3ac9-828c-ccf57899507e | -2.9777 | -45.5937 | 2024-12-01 04:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7868992d-5e61-3738-84bc-d51abd3c261f | -4.0052 | -44.7596 | 2024-12-01 04:00:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0e5e18cb-0d00-3647-a627-1ead1049d810 | 1.1622 | -55.9869 | 2024-12-01 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3ce0a85c-2971-30fd-b253-78ca0ff5f61f | -3.1273 | -54.5264 | 2024-12-01 04:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 8751b22f-d455-33a4-aed5-bc3bd23529cc | -4.5562 | -43.3028 | 2024-12-01 04:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 161.1 |
| a6fd1c2b-8ec2-30e2-b65c-69ec5d4c8e9b | -4.5578 | -45.7232 | 2024-12-01 04:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e613f015-f505-3362-87dd-85f5d480925c | 1.1439 | -55.9871 | 2024-12-01 04:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 12b4b684-9a44-34d4-b635-fa2c5fafbf0e | -6.9344 | -43.5401 | 2024-12-01 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 3d4c8229-d770-3061-8cf2-35f811dbc5a2 | -2.7503 | -51.7553 | 2024-12-01 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d7f27275-f37c-3df9-8bef-950204b0d597 | -2.9778 | -45.5713 | 2024-12-01 04:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e4dd86fe-5c50-3fa2-ab10-5dc341967f74 | -3.259 | -53.6388 | 2024-12-01 04:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| b1eef0c5-fb53-3c67-b122-94cf97ebd76a | -2.6578 | -51.8811 | 2024-12-01 04:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |


[Clique aqui para ver as próximas entradas](README22.md)
