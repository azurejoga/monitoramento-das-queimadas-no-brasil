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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fd8754f-d04f-323f-8086-af7e136cca43 | -2.6558 | -47.1761 | 2024-12-20 00:00:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d45d4f2e-db52-3e31-94ff-92c4bf8db27b | -4.9272 | -41.3358 | 2024-12-20 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 61f5e9a4-bb1e-3ee4-8b2b-5cfbc2d1b874 | -9.2216 | -60.3302 | 2024-12-20 00:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 680900b1-5404-3a91-a6d0-2934e151f03d | -9.2215 | -60.3495 | 2024-12-20 00:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 430d1143-40e1-3972-806f-41a9cdfd77a4 | -4.3343 | -45.7352 | 2024-12-20 00:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 00608a49-9364-362f-8533-2cf91c0a84c7 | -2.7661 | -47.3912 | 2024-12-20 00:00:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 44873ee3-cf3f-3e2c-b598-a47cd01b3485 | -4.2726 | -46.6723 | 2024-12-20 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 06153305-43c8-3c6a-8f36-2f0c88a7ae23 | -3.23 | -46.78 | 2024-12-20 00:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 480ff929-0cba-31d2-b62d-e720f34c250f | -3.2 | -46.78 | 2024-12-20 00:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e639ba-35e6-309c-95c9-eccb4dd49b3b | -3.23 | -46.83 | 2024-12-20 00:00:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff6c183-8405-3106-a5c4-58b58e82be65 | -9.31861 | -35.75371 | 2024-12-20 00:02:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 69bb50d4-2acd-36f7-a629-7c9579300eda | -9.31737 | -35.74478 | 2024-12-20 00:02:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| a000e986-5893-3ce8-80ab-358901f273a3 | -9.92798 | -36.3651 | 2024-12-20 00:02:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c5a47104-305e-3a15-b2d8-5a166f33c148 | -10.91748 | -38.82241 | 2024-12-20 00:02:00 | TERRA_M-M | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 88f7593c-1a94-3458-a5ab-965305c1481d | -10.174 | -36.68557 | 2024-12-20 00:02:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 084de21d-8046-379b-8fe0-095d4582c555 | -9.74908 | -36.40268 | 2024-12-20 00:02:00 | TERRA_M-M | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.1 |
| 89f69a52-6152-3134-9793-4ef61e07ab9f | -10.17527 | -36.69491 | 2024-12-20 00:02:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e25185fa-14cc-3ead-987a-d22fad126301 | -9.76546 | -42.00817 | 2024-12-20 00:02:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 7368bff7-0027-321f-aa77-341b6a0f01f2 | -9.66254 | -36.03636 | 2024-12-20 00:02:00 | TERRA_M-M | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 0bf80f0a-57c5-3c00-b21c-836352fb9cd0 | -10.18305 | -36.6843 | 2024-12-20 00:02:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1ff92bda-87ec-3902-9709-bfe5fc899baf | -11.21365 | -37.72784 | 2024-12-20 00:02:00 | TERRA_M-M | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 940b118f-840e-35b8-a7a2-6a0bf6986609 | -9.75804 | -36.40144 | 2024-12-20 00:02:00 | TERRA_M-M | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 1ce6c72e-77be-37e8-8dab-3172e62b3eaa | -11.21507 | -37.73869 | 2024-12-20 00:02:00 | TERRA_M-M | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c6784f8a-8bf8-3f6c-82f3-5f9b0be41630 | -9.75033 | -36.41181 | 2024-12-20 00:02:00 | TERRA_M-M | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 8e70c95f-27dc-3f4d-ad88-76dd75ea77ed | -9.01933 | -40.26383 | 2024-12-20 00:02:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 264636aa-4e30-346a-a743-4c0f6c1a691c | -7.24761 | -44.71424 | 2024-12-20 00:05:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| a3f65757-caef-3128-8033-85648a5bbade | -6.12245 | -43.94863 | 2024-12-20 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5921658b-d5f5-3aec-8698-3b0ad00bdbe8 | -3.22821 | -46.81421 | 2024-12-20 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 651.0 |
| 3f46b2f1-6b1a-3373-81c4-631650b0d1a7 | -2.97731 | -45.00629 | 2024-12-20 00:05:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| c1b154df-c0b9-360b-9271-1344a192d3e3 | -4.93008 | -41.32718 | 2024-12-20 00:05:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 7de37e45-c73d-31a7-9a4a-a727ec614b1a | -4.67756 | -44.41961 | 2024-12-20 00:05:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 39f035cf-ad31-3cfc-9640-28f056f4e960 | -5.63016 | -35.45582 | 2024-12-20 00:05:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 6.8 |
| bf33e890-8872-3b6e-9861-30b07dadb1b5 | -2.7665 | -45.56826 | 2024-12-20 00:05:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d47bf681-f8e4-3986-a7d9-7b603d91cbd7 | -4.42367 | -42.8943 | 2024-12-20 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 86fd6ab8-5980-33fe-a621-0471eaa84ab0 | -5.61294 | -38.99613 | 2024-12-20 00:05:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 0a8d3804-8f3b-35ad-b38a-ed6449b06bd4 | -6.04272 | -44.04044 | 2024-12-20 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| a6b43006-ef1e-347b-823d-0b5e2381be8f | -6.20938 | -39.40102 | 2024-12-20 00:05:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e03043e3-f262-388c-b96a-9b3678a41a75 | -5.52537 | -35.56616 | 2024-12-20 00:05:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 01f64a0e-c292-3e94-bee2-a2ca4846d196 | -3.22303 | -46.77674 | 2024-12-20 00:05:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 375.2 |
| c8154e54-eb11-3e9f-9485-dd7022662d24 | -3.23182 | -46.80704 | 2024-12-20 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 838.8 |
| f4d7eccb-1af5-32a2-b240-a303d3a8ce6e | -8.2323 | -39.03283 | 2024-12-20 00:05:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1d0beb31-40f2-3fb1-8e78-334ddae0d9b7 | -5.60634 | -39.54866 | 2024-12-20 00:05:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 7e429b11-a370-3a40-9068-aeb1f4025862 | -4.93211 | -41.34209 | 2024-12-20 00:05:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 51.9 |
| fef2ac04-50f0-3b91-b43f-83a46f4daa44 | -4.9188 | -41.3286 | 2024-12-20 00:05:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6c430254-29db-31f4-a2ba-31f1a538188b | -4.28177 | -46.68108 | 2024-12-20 00:05:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c781fc34-f984-3053-a171-5955a4193149 | -4.33626 | -45.73186 | 2024-12-20 00:05:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 68d8a10a-99cb-3d93-b343-6d1b4f9fb5e7 | -2.98967 | -40.28391 | 2024-12-20 00:05:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 68357bca-011a-3274-8195-22d9a66465cf | -2.76405 | -47.39329 | 2024-12-20 00:05:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 118.4 |
| ee699d41-7b35-3ff2-9c4e-a8464eb43d66 | -4.84936 | -37.45684 | 2024-12-20 00:05:00 | TERRA_M-M | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f2b562cc-742c-3ed6-bf3b-0e3a4aa43b20 | -3.21404 | -45.50983 | 2024-12-20 00:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 12d808e3-c98a-30a0-ba5a-92bdbd3190c1 | -5.61991 | -35.44801 | 2024-12-20 00:05:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 24585eb1-d85d-3fc5-83ef-4d4d2e62669a | -5.11696 | -43.20906 | 2024-12-20 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2bb1e481-81d4-3cef-a3e0-85f53e4d8cd5 | -5.83686 | -39.0723 | 2024-12-20 00:05:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 63ded9b9-a19f-34fc-97a2-9b26eb674877 | -5.11737 | -43.19416 | 2024-12-20 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0b67b67a-611b-37cf-862c-fe82c736ea59 | -3.69488 | -42.21592 | 2024-12-20 00:05:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 6f7e9958-2b22-3997-981a-565ab5d509a2 | -4.4235 | -42.89986 | 2024-12-20 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1024e2cd-1936-3edb-b105-3ba7dce987c3 | -5.39123 | -40.66858 | 2024-12-20 00:05:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 79dedf70-8610-39a0-8efc-2a5430fdca5c | -7.22576 | -38.68543 | 2024-12-20 00:05:00 | TERRA_M-M | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3850d00f-9e55-3771-a553-3a2254b8953b | -4.07113 | -43.87091 | 2024-12-20 00:05:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 6d6afd4e-49a6-336d-a768-38fad3b2a6e9 | -2.76338 | -45.5639 | 2024-12-20 00:05:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 03bd54a9-5e47-3cd6-b955-d2f0949fe354 | -2.76243 | -45.53886 | 2024-12-20 00:05:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 884fa56f-4450-3830-9757-edc4ab2f6509 | -5.84045 | -39.07639 | 2024-12-20 00:05:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| eec23d16-447d-3863-b65f-201d6a1069de | -3.21051 | -45.50404 | 2024-12-20 00:05:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 4115cfe1-fc1d-394f-b395-9314a10feeb8 | -5.62758 | -35.43766 | 2024-12-20 00:05:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ea67dfd1-8d3a-3542-8cae-5416fb251999 | -4.26756 | -46.67589 | 2024-12-20 00:05:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| dcdb5e64-8f32-33c8-97db-0d374df4fcfa | -2.97784 | -44.99963 | 2024-12-20 00:05:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 75878b75-33eb-3067-8f8e-de5aee6bdff1 | -5.53432 | -35.5649 | 2024-12-20 00:05:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 2364085f-f173-3569-81b0-74a7fe60543e | -4.38773 | -42.14853 | 2024-12-20 00:05:00 | TERRA_M-M | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| c43e6011-871c-33a5-a508-05f5bfeda92a | -3.68652 | -42.20658 | 2024-12-20 00:05:00 | TERRA_M-M | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 057ebfb2-8016-3888-ab7c-eec9466d3e93 | -4.11848 | -43.54319 | 2024-12-20 00:05:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 61b427d3-aae7-3677-91c2-9aac193532c5 | -3.71931 | -41.69772 | 2024-12-20 00:05:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| cf528e23-469c-3c14-966a-3e1ad025feec | -3.24519 | -46.8121 | 2024-12-20 00:05:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| c9dce6fb-12ee-34e4-8025-7621eb62aa63 | -3.22688 | -46.76945 | 2024-12-20 00:05:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 5363e961-4664-3cb9-b9f0-ec52d0449a44 | -3.22589 | -45.50208 | 2024-12-20 00:05:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f9654c5e-eb57-3366-a315-2c3c4ddd789b | -5.11426 | -43.18797 | 2024-12-20 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7d34f7b1-b16d-3613-95bd-586c03a84d79 | -3.22942 | -45.5079 | 2024-12-20 00:05:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 91b09960-f4d1-3c0d-9176-f9eedea41894 | -5.53558 | -35.57391 | 2024-12-20 00:05:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 19.6 |
| dcd72124-8265-31d0-8201-b21f5aebf01a | -5.62887 | -35.44674 | 2024-12-20 00:05:00 | TERRA_M-M | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 200.5 |
| 582cc2c3-384f-3b67-bdd6-77190351761b | -5.94183 | -39.38638 | 2024-12-20 00:05:00 | TERRA_M-M | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e5d29e8e-219a-37d7-8908-8fbfb77eb2e3 | -2.97175 | -40.22718 | 2024-12-20 00:05:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1cd675f2-a0eb-3a5b-ba11-fe2a55fb7a7b | -4.92074 | -41.34298 | 2024-12-20 00:05:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| d20442d9-a60f-3a7e-afa5-61aae140405e | -6.03986 | -44.04609 | 2024-12-20 00:05:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 03b64d9d-8a7b-3dd8-b2ea-c3dcff1796b2 | -5.3318 | -43.73746 | 2024-12-20 00:05:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a757b72e-e6ed-355d-8f06-3f2df14540a4 | -2.76452 | -47.38603 | 2024-12-20 00:05:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 9004a263-b303-3d72-819b-10de87781f97 | -2.7846 | -47.3906 | 2024-12-20 00:10:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| dd5337ea-58cd-3b36-b081-c5bbfab7ab34 | -9.2216 | -60.3302 | 2024-12-20 00:10:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b43358f2-5402-3000-8079-72ea679bbb3f | -4.9272 | -41.3358 | 2024-12-20 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| fe274345-539e-3234-91d8-b38f75fcf446 | -2.7661 | -47.3912 | 2024-12-20 00:10:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 45bec7d7-41ed-3f1b-aa57-4812531f49ed | -4.2726 | -46.6723 | 2024-12-20 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4d8904ee-7dbe-3ea1-9d5d-6beb15afd7a1 | -9.2215 | -60.3495 | 2024-12-20 00:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c6b183df-b110-359b-92ed-af484bd6290f | -2.7661 | -47.3912 | 2024-12-20 00:20:00 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 69423883-c339-3d3c-9ed4-4a11060db413 | -3.232 | -46.8056 | 2024-12-20 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 373ac531-9978-3806-aa20-def906dbd776 | -3.2136 | -46.7843 | 2024-12-20 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 710d5df2-588c-39e8-b77e-1bc7161c829b | -9.2216 | -60.3302 | 2024-12-20 00:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 37287c5b-af3b-354e-952b-db2d7cdbe330 | -3.2507 | -46.7829 | 2024-12-20 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| e5d9a321-69cf-38cd-9417-336b674eabd4 | -3.2321 | -46.7836 | 2024-12-20 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 218ec9dc-a28d-38a1-839d-b08447ddd01d | -3.2322 | -46.7616 | 2024-12-20 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1c026c15-d344-3202-a4df-a78f528fa8fb | -2.6558 | -47.1761 | 2024-12-20 00:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4818c075-764d-3217-8458-0be983c50b48 | -4.9272 | -41.3358 | 2024-12-20 00:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 1b40ee4e-5107-3a6f-ac8d-b6d88c425d45 | -3.2135 | -46.8063 | 2024-12-20 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |


[Clique aqui para ver as próximas entradas](README2.md)
