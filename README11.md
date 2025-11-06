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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e125455e-6189-3885-9322-5c1c1edd7d3a | -4.59979 | -43.35987 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d943bbe8-3312-3c90-911d-39bc986569d4 | -4.59439 | -43.35368 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd197911-3ef8-3a6c-a246-72c790538d33 | -4.57818 | -43.33524 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 78b292cd-3326-3cb8-ae62-cf5359e457d5 | -4.27357 | -45.12724 | 2025-11-06 03:32:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 42d462f7-264e-3e6f-9fa0-000f2ef34574 | -3.91482 | -43.15708 | 2025-11-06 03:32:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d1509934-b0a9-3e52-a568-953475f5e1ea | -4.59655 | -43.3631 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da71d989-2039-3151-804e-8bdcb698ba33 | -5.15654 | -41.27339 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ff56705-9d87-3cd1-9382-123b9fc169af | -4.78002 | -45.1377 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b3e46ee-7eb3-36e2-8012-2ab7fd5fdf35 | -4.6016 | -43.34977 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61418beb-17d5-33ba-b5f8-05e43c19e2f9 | -4.58657 | -43.34548 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3f954d0-5be1-3b63-86d8-637157aad66a | -3.43199 | -42.54339 | 2025-11-06 03:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9146448e-1632-37ab-8952-e93d36e8340c | -4.78817 | -45.13271 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9920d64c-e821-3aab-9ee6-06e299ea59c0 | -5.15292 | -41.26159 | 2025-11-06 03:32:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 709d425b-71ce-3df2-914a-411bd97bbb4d | -4.58993 | -43.34227 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b06a8ad-0613-38f0-832c-662970472e41 | -3.4312 | -42.5481 | 2025-11-06 03:32:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77bb8ff5-72fc-3f94-875b-dfa89b24b648 | -4.59349 | -43.35867 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6aabcaf-4e48-39be-8514-5e69f580c870 | -4.60068 | -43.35492 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 249d0e12-367e-30fd-bedf-31bd3a6f8ee4 | -4.78401 | -45.12991 | 2025-11-06 03:32:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f323dffa-567e-3a92-8a3f-e40bb2649e6e | -5.42595 | -40.6679 | 2025-11-06 03:32:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3170ef2e-ab32-3180-89bc-c9f882e39f84 | -3.92201 | -43.15312 | 2025-11-06 03:32:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9047acdd-09ad-3afc-ac6f-f466eb6b4fe0 | -4.5854 | -43.33131 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 91d4f64a-fa9b-3bfa-a4df-73dfdd64cc77 | -3.1406 | -40.05775 | 2025-11-06 03:32:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7776e352-5ddd-3264-a382-4f5b64a616ca | -4.59566 | -43.36826 | 2025-11-06 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f520d3b1-a98b-35ce-809d-9ab900753684 | -6.28616 | -44.73908 | 2025-11-06 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 071d13e7-7032-3171-af28-d24d65b86b90 | -6.76547 | -35.42901 | 2025-11-06 03:34:00 | NPP-375D | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 728d232b-ddb1-3c97-9c47-9f2cea8059e8 | -6.99529 | -39.07322 | 2025-11-06 03:34:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ec9b8769-78ae-3aac-95ac-6ed79affb8f9 | -9.12102 | -37.79083 | 2025-11-06 03:34:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 2fda8af2-e0f0-3a88-9b68-597023366eae | -9.45631 | -35.57339 | 2025-11-06 03:34:00 | NPP-375D | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f37ce9d6-b4b3-3317-8bc3-db5a3ffa45b1 | -5.76105 | -40.81332 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 14607e46-6e95-38c9-b9e3-cdecde0e31dc | -6.0524 | -44.16577 | 2025-11-06 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d09021f-1461-32ea-831e-dcd59cb69877 | -6.90237 | -38.57258 | 2025-11-06 03:34:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 797d9360-a0e9-3a6b-ba26-97e551507d3f | -6.22793 | -40.44571 | 2025-11-06 03:34:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7f068b79-8e9f-3e7c-96d4-f4a9f8be18d3 | -10.07017 | -42.73851 | 2025-11-06 03:34:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2656bbff-4a8e-3222-943e-28831faa1aa9 | -5.62046 | -41.0835 | 2025-11-06 03:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75f1c6ef-f0ba-3ea8-9c13-7dc004ce0ab8 | -6.36105 | -43.75851 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a94f9972-a1ce-3b0d-8f01-b4b6b6664960 | -7.17907 | -38.35105 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b4b2e2b-78e7-3f5b-a392-0ebf3e42e25f | -5.79449 | -40.80143 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41316ad8-63af-38b2-8d19-bd0c978b1121 | -6.26224 | -43.68148 | 2025-11-06 03:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 296a450c-e86a-30ab-bda2-3c239470ccfa | -6.07053 | -43.25288 | 2025-11-06 03:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 026ed0a6-75bb-3922-b1be-6ca108f10ad8 | -8.54688 | -36.50716 | 2025-11-06 03:34:00 | NPP-375D | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 211ab4e6-54a4-3018-92f4-12c4c5f5cd91 | -6.52083 | -38.75089 | 2025-11-06 03:34:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 486ba443-49c0-3977-bb2f-4e1e081b5408 | -7.95042 | -40.33261 | 2025-11-06 03:34:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 32090d16-e511-3522-9d18-6ec10a4b5658 | -5.76464 | -40.82398 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 760a124b-cf17-3b55-bde1-02138ee76fe6 | -6.36743 | -43.75919 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 353df643-c116-3f70-80f6-d4324f8a619d | -7.27931 | -39.38557 | 2025-11-06 03:34:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cca5cb23-d297-3f36-aa34-f8e22169833a | -6.69742 | -40.83419 | 2025-11-06 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c9138f15-cf08-3106-a5d3-cf64a742f5d1 | -5.61984 | -41.08694 | 2025-11-06 03:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c4c143f4-863d-3fec-9694-ba2328fb019f | -6.05343 | -44.16023 | 2025-11-06 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5717638-608d-30fa-8fc4-80cd7366fc0b | -6.06967 | -43.25771 | 2025-11-06 03:34:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dea43dd8-9bef-30cf-a59d-2a37e0105fff | -7.284 | -39.38614 | 2025-11-06 03:34:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 75f7d524-023a-3d0c-9a55-76a44d2e9df8 | -5.76405 | -40.82742 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 224444a9-4333-3d21-a51a-c3fd17991dc6 | -6.26754 | -43.68787 | 2025-11-06 03:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3b2c8ebe-64fc-37f3-9929-98498a7439a3 | -8.26722 | -41.93035 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9da7063-92ad-392e-b331-feec82f9e27a | -6.26936 | -43.67796 | 2025-11-06 03:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 059c553a-d093-3b7f-b283-804c89969c61 | -5.76694 | -40.8106 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e51029c-9e73-3b33-991d-7ff35c6cd95a | -6.30439 | -43.80705 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6b4d1e2-4df6-3d10-93ad-e31d57f88f17 | -6.96978 | -38.12151 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| afa0ce75-5c59-360b-afc1-25168d37a675 | -6.28273 | -44.74078 | 2025-11-06 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28b6170e-b6dc-3a8f-b2b8-0a2a10d730d6 | -5.24392 | -44.39426 | 2025-11-06 03:34:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3f453dce-c2e8-3d61-a8a3-00d6239fd2e8 | -5.61807 | -41.08305 | 2025-11-06 03:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c6e9ea3-619d-3a2e-90cb-1a0344703e02 | -5.76043 | -40.81694 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5fd54755-248e-33b9-ba17-5a673fdcb6c1 | -9.12168 | -37.78708 | 2025-11-06 03:34:00 | NPP-375D | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.8 |
| d7985f96-2943-38aa-b729-ea695f984f51 | -6.26848 | -43.68275 | 2025-11-06 03:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7e6f9e6a-1234-3ccc-b753-297e1dcc81bd | -5.76524 | -40.82046 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28b31188-a23e-33e8-89da-9176403400d2 | -6.05427 | -44.16032 | 2025-11-06 03:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 815ca600-01ac-3353-8a74-3c5cbfd22f1d | -7.27308 | -36.0783 | 2025-11-06 03:34:00 | NPP-375D | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3387ae27-870f-351f-9bf2-54b7bc814cc4 | -6.69688 | -40.83727 | 2025-11-06 03:34:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b0962fb2-8cdf-322e-a217-0ae83e0ac064 | -5.79551 | -40.80183 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 25d1186f-7488-3027-8f8b-e4e31236a548 | -10.04329 | -36.46362 | 2025-11-06 03:34:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b371fd86-af5e-3b6e-8175-e193136233cd | -5.76643 | -40.81357 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9fd56383-ee92-3968-9a88-4e486fe051ee | -5.39472 | -43.93873 | 2025-11-06 03:34:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13972ee2-3e55-3748-9b9c-464b41faa229 | -8.32424 | -38.0878 | 2025-11-06 03:34:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3bd00734-047a-3de3-b335-e212502aaa6e | -8.1535 | -35.41378 | 2025-11-06 03:34:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d49fb8cc-7902-3e9a-987f-e69c5cc62919 | -5.75505 | -40.81668 | 2025-11-06 03:34:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a36ce456-4bfb-3ce0-8ee3-15dfcf664660 | -5.45797 | -44.68856 | 2025-11-06 03:34:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ba38502-bebd-35ff-ac0d-8b65cf290ba0 | -8.89107 | -37.10821 | 2025-11-06 03:34:00 | NPP-375D | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e2c5314e-1256-3639-81d9-0e80275241ee | -9.04828 | -35.44234 | 2025-11-06 03:34:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 14f3846c-bfc5-31c1-b78e-4fb8d1cd222d | -5.61748 | -41.08651 | 2025-11-06 03:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59aefa28-5e2f-3aaa-ba7c-b90c4cc3dc37 | -6.52171 | -38.7457 | 2025-11-06 03:34:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a2388ae5-4698-33de-8ec1-3ade3668a05a | -6.30349 | -43.81205 | 2025-11-06 03:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbdaba74-1302-3f80-9d5e-92b4c5447c6c | -5.77272 | -40.80845 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d33e8b59-babe-35f5-8771-b418e33254ce | -7.14526 | -39.42414 | 2025-11-06 03:34:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 245bfd3b-f96a-3c99-8d3b-957f082144f5 | -11.82393 | -43.15926 | 2025-11-06 03:34:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e66ef72d-f465-31aa-b8fa-be1a5c313642 | -5.62288 | -41.08724 | 2025-11-06 03:34:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ef7ea3c-87f8-3d15-b93d-d12dfd8a4e49 | -7.1786 | -38.34822 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 36062d69-0d1e-3b43-b8f4-10a9fa95067c | -5.85696 | -43.99731 | 2025-11-06 03:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aaaa092-7658-3a13-9791-414bdbf80b04 | -5.79396 | -40.80446 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3227618e-a271-3d98-a258-4751453aae21 | -5.46474 | -44.68964 | 2025-11-06 03:34:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fcb6b45-302c-3aed-a86f-17fca272e1bc | -7.17793 | -38.35223 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6849ebfd-82a9-312c-bdef-304fc8af612a | -5.24058 | -44.39298 | 2025-11-06 03:34:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 842d5d11-933e-3b3c-a91e-d80bfdfa6902 | -7.17836 | -38.35508 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3318a704-c5c2-3b36-99d4-c10cde9cada4 | -5.75561 | -40.81344 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| caa78a9e-267d-37af-9955-4dcf10e32793 | -5.795 | -40.80483 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4f79ab2-1ba6-3fca-b24b-42548cd7b343 | -5.75982 | -40.82046 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 04f3adbb-37d9-32fc-9082-1190fa14bf38 | -6.22845 | -40.44271 | 2025-11-06 03:34:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 73f4919f-394c-39dd-9427-7a017231fad6 | -5.7902 | -40.80121 | 2025-11-06 03:34:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0da5d302-e043-3698-8f4b-787ad2b84eb2 | -10.07397 | -42.7421 | 2025-11-06 03:34:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 90467bfe-4a5d-34b5-8cfb-8afa2b597111 | -5.46365 | -44.69564 | 2025-11-06 03:34:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3a34c7bb-13ed-319b-9df3-1ece62622777 | -7.1827 | -38.35585 | 2025-11-06 03:34:00 | NPP-375D | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f60d8145-49e5-3cd6-a6cd-8d341dd18ba7 | -6.28375 | -44.73513 | 2025-11-06 03:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README12.md)
