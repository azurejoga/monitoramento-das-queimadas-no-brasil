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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a6596c4-9274-36ba-bed6-8967c884c673 | -7.53771 | -35.29041 | 2025-12-21 04:01:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a81d8f76-29ed-3f86-b368-7efb12312530 | -5.06549 | -40.84138 | 2025-12-21 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 86d881d4-1ee1-33aa-b76b-ce3b621d9a21 | -10.41362 | -38.03229 | 2025-12-21 04:01:00 | NOAA-21 | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d7ed7236-53a6-3995-b4e9-1d059fc461eb | -8.74669 | -37.18261 | 2025-12-21 04:01:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 457bc62e-54a5-3571-bcf0-89e1814ffb9d | -8.13769 | -41.12242 | 2025-12-21 04:01:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| be4e8226-7846-39a3-87ab-d6331f28142d | -5.91248 | -38.35972 | 2025-12-21 04:01:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d8e4b45-0101-3499-a4d6-ed383771e309 | -9.57173 | -44.60469 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 225e1df7-27af-37ed-a9d3-70e5e13562e1 | -7.42942 | -39.47853 | 2025-12-21 04:01:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ce2c976f-6339-3391-b2e3-4105bce3cd37 | -10.41718 | -38.03284 | 2025-12-21 04:01:00 | NOAA-21 | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| fe7b4735-5aef-3808-aa37-b091253c93f6 | -6.4069 | -39.23207 | 2025-12-21 04:01:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e60c461a-93b0-3efe-8fb5-1ed9d0c8d259 | -4.60651 | -38.32204 | 2025-12-21 04:01:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba341aa3-b853-3ed5-9b85-0d6ec6180131 | -5.16202 | -41.15557 | 2025-12-21 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f074b880-8030-3a0b-9bd1-6516d6a84dd6 | -6.17855 | -39.23579 | 2025-12-21 04:01:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 627cdc53-0e81-3926-a275-3288051eb60b | -9.70804 | -42.917 | 2025-12-21 04:01:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 621aa43a-34a6-3ffc-9010-f48d9434bf16 | -9.9014 | -36.17434 | 2025-12-21 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 524bad28-de9a-3c59-aa70-38838f5157b2 | -4.52132 | -38.6985 | 2025-12-21 04:01:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6a7ae4ac-01ce-3294-90e1-43ca011fe769 | -6.44102 | -40.62196 | 2025-12-21 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd8db536-f1ba-3e8c-9a9c-e195f51d40fe | -9.51756 | -43.24292 | 2025-12-21 04:01:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ea1626a6-0a7f-3b1f-806b-f1d831c668b4 | -7.91844 | -35.33818 | 2025-12-21 04:01:00 | NOAA-21 | FEIRA NOVA | PERNAMBUCO | Brasil | 2605400 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92dbff82-a9c5-32ea-84bc-b606228e18e2 | -8.1738 | -35.89696 | 2025-12-21 04:01:00 | NOAA-21 | RIACHO DAS ALMAS | PERNAMBUCO | Brasil | 2611705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 58b11ba4-f9b5-3815-b82d-c90abf1f884a | -6.4569 | -39.95808 | 2025-12-21 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9de2fa47-cf83-3d05-be66-1fed8ae67439 | -9.56812 | -44.59581 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1eaa47b6-2499-3a6b-8491-300350ef567b | -6.46319 | -40.69675 | 2025-12-21 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f9c6167a-b745-372e-b39d-d948e2fbf54b | -9.56661 | -44.60501 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8c0d3bad-f2a5-38f3-b2e7-07e4b0403138 | -5.06492 | -40.84492 | 2025-12-21 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9939610b-d745-3391-a554-0621d64a24fe | -11.84248 | -38.20146 | 2025-12-21 04:01:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4f23e341-8e9b-329e-9f4b-f34350ffb66a | -9.56425 | -44.60349 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9df71c74-6eda-31b4-8f51-ce4f2716b521 | -9.48768 | -35.61833 | 2025-12-21 04:01:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4ee9a11d-2312-3743-b628-a71a82b8d750 | -9.90194 | -36.17149 | 2025-12-21 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3459b042-f01f-373e-a839-1b6e19f7a78c | -7.53926 | -35.29019 | 2025-12-21 04:01:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| af79ad5e-e17f-3f02-8be5-e83f23d5258d | -9.57035 | -44.60562 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7ddabd25-dc60-3273-b7e1-56a4c5796638 | -4.81403 | -42.2147 | 2025-12-21 04:01:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 11d2a66b-b4ea-3e55-9ac0-41d3824930c3 | -5.81097 | -39.54478 | 2025-12-21 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3b9f6b77-619c-3312-939b-22b90f1a2f84 | -10.55599 | -37.87535 | 2025-12-21 04:01:00 | NOAA-21 | PARIPIRANGA | BAHIA | Brasil | 2923803 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| df3e1c55-59da-3917-9e4d-21287d6885d1 | -5.06883 | -40.8419 | 2025-12-21 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9428a5bd-a161-380a-bc70-5be2d4b0060d | -10.49316 | -44.92728 | 2025-12-21 04:01:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9261c581-d984-379c-b6dd-1a2d1af4dd5a | -9.90586 | -36.17206 | 2025-12-21 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| beda122f-f08f-356a-a305-719cfd17ab44 | -9.62938 | -35.88625 | 2025-12-21 04:01:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 86626e44-7413-3ade-b789-21a410152d6e | -4.81465 | -42.21079 | 2025-12-21 04:01:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 23efea9a-e86f-32bd-b30e-a9338cf8c816 | -9.04623 | -40.43016 | 2025-12-21 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d88b6420-25a2-3611-a27f-5ed556fcb316 | -5.0885 | -37.62547 | 2025-12-21 04:01:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 467344f6-2b14-3385-83e7-5ef787f4ba98 | -9.48818 | -35.61475 | 2025-12-21 04:01:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a8498f6e-2c93-3c3d-93d1-a2b93db5aa9a | -6.25738 | -39.799 | 2025-12-21 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 15de99fc-54b1-3b89-bf5a-6ece74d85fb1 | -9.90532 | -36.17491 | 2025-12-21 04:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ac94bd18-2111-382c-82f2-375a26f5b901 | -4.71538 | -41.77388 | 2025-12-21 04:01:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b84c63d-b388-313b-9ef0-bce6e5616889 | -6.46651 | -40.69727 | 2025-12-21 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09d6c6c1-a87a-30ff-ba2e-1b67a12c7a34 | -9.26585 | -44.31039 | 2025-12-21 04:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a75b5649-a907-38a9-bbdb-7417ec3226b8 | -9.56503 | -44.59889 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 853d1aa5-09f0-3956-bd05-91ffc88944b6 | -6.26122 | -39.79606 | 2025-12-21 04:01:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d9b75593-f400-3744-9447-0e396a3cde88 | -9.56736 | -44.60041 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ff72a838-1fb3-3fba-954c-28daf346636f | -11.16384 | -43.31804 | 2025-12-21 04:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b59861ac-dbb1-32e9-aaa8-0a4dad86c330 | -5.16482 | -41.15965 | 2025-12-21 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1359b045-5eb3-3c18-9fd3-b59e204193e0 | -7.43275 | -39.47904 | 2025-12-21 04:01:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 05be4841-d34d-301e-a64f-d87fc1db7a07 | -4.71599 | -41.77011 | 2025-12-21 04:01:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43187829-b368-333d-a3c4-f90249febf2a | -9.56799 | -44.60409 | 2025-12-21 04:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b807b165-083d-39db-a832-ec0915ddce59 | -5.54271 | -39.54122 | 2025-12-21 04:01:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 72fc21c7-d4eb-3c26-a792-b97965ea1e64 | -7.53874 | -35.29387 | 2025-12-21 04:01:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| beab5ffb-5982-3dbb-852b-10498ec49448 | -4.52187 | -38.69501 | 2025-12-21 04:01:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc49ab81-a887-3a5c-a43d-0d2fe93d7184 | -14.43822 | -43.9857 | 2025-12-21 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 234dc6b4-d2db-3470-8bde-0ee24c6cf3d6 | -11.7556 | -43.32861 | 2025-12-21 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 752fdc1c-c031-36e2-832a-e057c5fb7f52 | -15.65924 | -43.11335 | 2025-12-21 04:04:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 560a3423-e104-3e7e-a226-92fb5897321d | -11.75622 | -43.3248 | 2025-12-21 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a27b34f9-4b43-38aa-ad8a-6ffd30d1aec0 | -12.27131 | -43.54737 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b5b1927-a33c-3c0b-89de-f3d938586a4e | -12.26763 | -44.61403 | 2025-12-21 04:04:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b23bf26-f890-3146-ab59-d6e1c7348aa2 | -12.08618 | -43.52066 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccb0aa2d-1b50-3844-a383-d09b3da43d82 | -12.27603 | -43.54028 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a936abdd-f717-3532-b0df-2d0d5222fa2d | -12.28228 | -43.54529 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e25d130c-9d32-3175-828b-724b50f453bc | -12.27947 | -43.54087 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ba6690a5-9c27-32bb-b8e7-38e694e9bb24 | -12.27475 | -43.54796 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d432e7b5-1f7a-3e14-bd75-e7e2c0488528 | -17.94777 | -42.29766 | 2025-12-21 04:04:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2047e1c7-f009-326b-904c-851ea821504f | -11.76309 | -43.32595 | 2025-12-21 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a1dd6a5-6a28-33c0-8856-001ede7da0a3 | -16.00741 | -41.6811 | 2025-12-21 04:04:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7627b7e5-504d-3b39-b0b6-4cc5feacc62c | -13.54316 | -44.4982 | 2025-12-21 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9820a85-8257-30b4-8915-6cffdafe8bf5 | -14.38817 | -43.64792 | 2025-12-21 04:04:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90eca0f9-67f1-3b90-9b32-ad3895b5139b | -12.28292 | -43.54145 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0cea6301-9fab-3fd0-8243-cb0739c4105b | -12.27884 | -43.54471 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 825b8e93-660b-32aa-895e-fc14ffd27891 | -12.22001 | -42.44647 | 2025-12-21 04:04:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a4b4a76-561a-311a-a033-1cabdbf9d149 | -14.43886 | -43.98184 | 2025-12-21 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c5f025c-d9eb-31fa-bad8-4d8538351ec0 | -16.58898 | -45.87588 | 2025-12-21 04:04:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95189e1a-c873-37ac-8d4d-a50c998d121a | -11.75966 | -43.32537 | 2025-12-21 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| feafbbf0-b479-31c9-91be-905a19fe17c8 | -12.29142 | -44.44924 | 2025-12-21 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a75f6f05-1943-348b-9e70-5e08ce9507b6 | -17.34136 | -42.45943 | 2025-12-21 04:04:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd96349b-5d22-3284-89a0-393dc76b68da | -12.27539 | -43.54412 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 07f7eab1-2bf4-3221-8cf7-92a523540b9d | -13.72303 | -44.37864 | 2025-12-21 04:04:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72ff45a0-2dd4-3cbf-938a-6f72279f62db | -12.27194 | -43.54353 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a6e0ff4-3590-31d4-b6b4-53fd8c2e430f | -12.72698 | -41.80761 | 2025-12-21 04:04:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8303e389-6ff2-3127-8c3b-a27bf4445e9e | -16.5519 | -42.65797 | 2025-12-21 04:04:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43900476-62db-3b65-b33d-ded2b0a854cf | -12.2782 | -43.54855 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92d6fa83-c9f6-396a-aed8-d5fc1efbf7d3 | -11.76029 | -43.32157 | 2025-12-21 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c48ac727-9994-3eb2-a65f-0a0ad37b4229 | -11.75903 | -43.32918 | 2025-12-21 04:04:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14039334-c990-342c-89a9-e37378674e3d | -14.43542 | -43.98125 | 2025-12-21 04:04:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a904671a-0d30-3d4f-bcfa-c98bf9d0b014 | -15.60856 | -41.79911 | 2025-12-21 04:04:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 61895a25-6363-31e1-9941-a3babc4f014c | -12.27258 | -43.5397 | 2025-12-21 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c546b435-a726-3fb8-a1e9-191db745f98f | -21.53801 | -57.53519 | 2025-12-21 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e9bc071-5326-31aa-862e-6b155dc60df8 | -21.54475 | -57.53652 | 2025-12-21 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b0b6974-1609-3e0b-b5ee-9c11f2af9063 | -20.68866 | -40.59273 | 2025-12-21 04:06:00 | NOAA-21 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4741c061-7aa6-3d24-9dcf-93257d62f47b | -21.13876 | -40.96406 | 2025-12-21 04:06:00 | NOAA-21 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| e6b03a33-f7a2-3f80-a5f0-9a30effbd6d5 | -20.63914 | -51.67891 | 2025-12-21 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9bb9fdbd-7146-37f1-8034-765dae9521af | -21.54214 | -57.5349 | 2025-12-21 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34cdc810-3854-381c-aaa7-e23da9fbcfd4 | -23.1674 | -49.54835 | 2025-12-21 04:06:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README4.md)
