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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6ab3ea4-8429-321d-8959-2b063958483a | -11.0399 | -47.81536 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4e23f78-ebef-3405-a323-aa9d1b9dcfdc | -11.09238 | -47.82099 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a1903f6-476e-3500-84ee-c8e09422bba1 | -10.23173 | -50.28662 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf78b08e-97ee-3510-b544-6a2bb11f034f | -9.04367 | -46.65334 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d186d892-567b-3d8b-8cb7-a6b70db485c1 | -11.28322 | -47.82617 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ac2f8484-99ad-3bed-927a-3cac2947a12d | -11.00558 | -46.59316 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b23c97bb-fd6d-37da-b786-cf2779a2f250 | -7.72654 | -46.22318 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b7e4c96-61c2-34c1-9a89-f7270c04e381 | -6.483 | -44.29197 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12399479-2c6b-3214-840e-9a899f048bdf | -7.56632 | -42.39874 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 886ae723-90db-361f-bc10-13182ad6813a | -13.32528 | -43.1044 | 2025-10-02 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1bc0e23e-2814-3984-8975-6bf2178a74a6 | -11.79324 | -47.56422 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| effee12d-7a4f-3498-87a1-c4f177c758b3 | -7.84424 | -42.85172 | 2025-10-02 04:02:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| d44b3d2f-cebc-39be-8b07-1976a27a3895 | -6.69085 | -48.70729 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 354e535d-58c0-32ec-bd12-67fc8375da3c | -9.40816 | -47.58497 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73f3b709-9e4b-3f1d-8f41-7ecb2f46f2b2 | -11.0028 | -46.58488 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fb262df-a63e-373e-8b37-613140454fa3 | -11.99406 | -46.57457 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6a98194-4928-30f5-aea9-0d682a2ee33c | -7.70433 | -42.15669 | 2025-10-02 04:02:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0130b500-f0d5-33f5-933b-de101eb07b22 | -9.9372 | -43.73153 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4ab3b83-2d48-3b8c-ad57-cc1b464febc6 | -9.04797 | -46.65401 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6338391f-c284-348f-8753-a2233b035ee6 | -11.87205 | -45.02018 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d92d08c6-69a2-3fda-8fcb-8ba288e52fd5 | -12.15623 | -46.67655 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9095e31b-e4a9-3ab1-a2a3-ac494387131a | -7.48077 | -46.46624 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f69418e2-b575-3a91-bb04-eada228ebc93 | -7.77306 | -42.53275 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 0a2857b9-ae52-3901-9367-2c8032b89201 | -6.10685 | -42.68288 | 2025-10-02 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fc4ae451-f2ec-3326-aac0-564519114e0f | -13.01125 | -45.21563 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06541877-677d-361a-8038-6a1be4d2cc9c | -12.63351 | -44.85238 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0105b554-7e59-3a9b-9bbc-707b7daf0907 | -7.45763 | -46.4709 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6a94e0e-b6d6-3f98-bf2e-f6148a2f1101 | -8.77796 | -40.35514 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 87e8f52d-1615-336e-9abb-eda61d2e5205 | -10.25673 | -50.33052 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6bfef5e-74d2-3086-8f54-e94e84bcced1 | -6.95932 | -45.32124 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6eb8ecaf-6dcd-3478-943f-1b830ba987e3 | -10.60279 | -49.63799 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05870861-39e6-336b-a476-2bcc85f2c045 | -12.22094 | -43.75669 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6622923d-096c-3f6c-a6b5-eba5d82cc779 | -10.99604 | -46.62281 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 518ba41b-3f2a-3701-b2f1-b31831c23bc8 | -7.16942 | -41.70004 | 2025-10-02 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 42aa4bf6-ad64-34f1-9771-60e1862d3641 | -11.27592 | -47.81551 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5dea393-72eb-316f-accc-994ea20cae81 | -9.94008 | -43.73623 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 508544ca-c2ef-30ac-9b58-b66bb47a4835 | -10.2299 | -50.32549 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b1526624-dc62-3608-a022-fdf1d007cf6f | -12.68766 | -47.5621 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25e9f259-7adc-36d0-9e76-f6c5585982ed | -7.77836 | -42.52192 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 929d6260-121a-3752-914e-916ee14cc0a5 | -11.17392 | -47.26551 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aa97c094-1216-39d2-b131-7e560c17c90b | -11.67321 | -44.28 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b3fca67-868d-3a63-ad2d-13100958a3ec | -6.69493 | -48.71424 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01b3e0da-d054-3a5b-a3a2-9aaa7fae9062 | -6.79668 | -45.96363 | 2025-10-02 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a46f0f9-eba5-36d0-820e-6d7de2f83a87 | -11.36257 | -44.96887 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f725dac0-b02a-35ae-8911-d1b94f2ee44f | -11.67728 | -47.49598 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 662a292d-3dc0-3688-b701-dc24e4951b46 | -11.17598 | -47.27909 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 63bbb691-eb6b-3ec3-b6c1-1c16cbe42677 | -12.66597 | -46.87565 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff2d6d5e-dbd2-3f1c-9e04-f58f761bdf1c | -11.59443 | -45.05562 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 899b235a-8f14-3cdd-8bb0-61525c826af3 | -12.86398 | -47.01278 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e21ce74-dbb4-319c-939f-c07ddecdd99c | -11.73898 | -44.42848 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd9da866-1809-3a42-be12-6d7d287a5b15 | -10.18143 | -45.4465 | 2025-10-02 04:02:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64bc4f4c-cb36-3eac-94c1-8d07757c9c21 | -7.3095 | -42.87772 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b8a34f7b-5c96-3c60-82f9-3eafd026e7e4 | -11.77219 | -46.83499 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1bce50a5-d424-3174-a570-3a9e4a0fed19 | -6.04992 | -42.67454 | 2025-10-02 04:02:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2ed792c8-556e-306d-a53d-5f49cfd6aa18 | -8.46816 | -46.83323 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d15c6f7-ef42-3ed6-b784-54bd5a430318 | -12.64801 | -44.23071 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c4b5a7f-e790-3b1d-834a-1269fb370ec1 | -10.93357 | -46.6748 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52da8c75-6a99-3daa-a067-017c9dc53678 | -12.02553 | -46.63361 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 06bc2938-b730-3bf1-b1eb-78a32603f437 | -6.32224 | -43.89239 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f86fb30b-74e0-358b-8838-7cf3364ff806 | -7.55887 | -42.64015 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 272bdc53-2aae-3c8c-a7b2-2d08bcfddf5c | -8.50968 | -47.82516 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b25d283-0396-326f-a755-0db43d877596 | -13.47784 | -43.50853 | 2025-10-02 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bc620bf-9f74-36ac-b9da-aabeb643cfeb | -11.17422 | -47.18835 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f30e7fae-4519-3ca0-bcbb-00919cee5086 | -9.94184 | -43.7702 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 37020a5f-a4db-3876-b5f4-b3500ea53287 | -11.03373 | -47.82395 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 609a05b3-154f-3d5b-9341-b83b9daf055b | -8.71316 | -47.14573 | 2025-10-02 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80d08de6-6201-3c6c-bf0d-951e0f2fb51a | -11.61027 | -45.03039 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c1ff5eb-ab74-3cc3-b014-83e521925aef | -8.81633 | -46.68348 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28d284f0-cd11-3a4c-bb0e-3244c5ece4fa | -9.93855 | -43.59019 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3c95e48-6902-3f05-8b89-233047537cdf | -6.70217 | -48.70279 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ee43732-03ac-3441-aab4-ad25a4ed126c | -11.80228 | -44.96818 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 34b6135f-6a52-342a-b919-a962e33686ae | -11.19274 | -47.74962 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2963bc1-5e2f-39c1-8142-5a43a285a3c7 | -10.23853 | -50.30927 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4b3ef28-0533-37c9-828e-39e5b21894ac | -9.94055 | -43.71107 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de0271ec-0e27-303d-b7e3-1e892e595a2c | -9.91438 | -43.71503 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7062106f-a8c0-3fa5-99e8-9bebb2393abf | -11.09044 | -47.8167 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29f643d8-e797-3347-a5f0-1ad83fb8662b | -11.16887 | -47.26899 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7ba8e17b-38a0-3c29-8179-ddd482de508d | -9.92148 | -43.71622 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1ebe1cfe-a989-3f0b-ba1b-aae944fd8ac5 | -9.71039 | -48.95242 | 2025-10-02 04:02:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2afead16-22ad-31e6-9213-09e6dbb3ea16 | -10.68605 | -48.56797 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ac026de-08e2-327d-a9b7-b6a7157581da | -11.86324 | -45.00474 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e21499f-bf82-37fc-bbe8-fe5ac0d58d62 | -11.09123 | -47.81224 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdc77d35-23c1-39db-ac45-7414fac390ce | -9.93042 | -50.48859 | 2025-10-02 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5f47d361-741f-38a6-b05c-6f58459fe6e9 | -11.45694 | -44.96496 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f946ac0-2f06-3455-aebd-1e8b45e63079 | -7.78118 | -42.52629 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cf5eceda-3d35-3fd1-91bf-6eedb6ef7be0 | -6.32424 | -43.04419 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d328a3d4-0232-3ad6-a2fe-ecd4907372a8 | -11.21835 | -48.21487 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8841f6c-50b8-3eb1-8fb5-f32e918bdc90 | -12.81184 | -47.01929 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9252a5b-c32a-328d-82eb-bc1f5f671ef6 | -9.94609 | -43.69943 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03c79326-d798-3de2-bb17-53acdb47945d | -9.93452 | -43.74792 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6019eb12-6dc5-3965-bb5b-c85c02de1e73 | -11.80597 | -44.96883 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1e50c9c-7b07-3b18-9759-fc3b7aa8708c | -10.84745 | -46.59285 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9536818-d234-3b34-9782-30039ff92dee | -11.17091 | -47.28263 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 14855c6c-3fcc-321f-b923-cb557d9d5cbf | -11.60189 | -45.05684 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6f24731-11bd-37a2-91ab-da3c22a07e59 | -7.78525 | -42.52302 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 95a6ad77-351f-3cbc-9212-5c0724754d63 | -11.01112 | -49.58022 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0230e0f-dee3-3a54-9bbc-fa0b06a31dca | -9.85698 | -44.60173 | 2025-10-02 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 51994c69-64d1-34b8-bd24-7d471f9ef3d4 | -11.46807 | -44.96691 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbcb72b2-7a01-3e75-82e0-1d1495a26c59 | -11.59914 | -47.22207 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f7779d4-79ad-3d6d-b5a9-fedf09e999e9 | -7.7036 | -42.15635 | 2025-10-02 04:02:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README26.md)
