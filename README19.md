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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5fa5d5e-fd98-32bf-b82e-087e60dc739b | -3.0734 | -54.167 | 2024-10-30 01:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2472b569-225a-3234-98d4-8f9c5b41bb35 | -3.1028 | -51.1041 | 2024-10-30 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 68f0a2de-9a7b-3d67-9227-1f93f4cf4cd3 | -3.1602 | -50.5812 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 620f8081-8748-38e3-afcb-2690d1290402 | -3.1892 | -44.1121 | 2024-10-30 01:15:24 | GOES-16 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5f8ae678-119a-35ed-baf0-ba9014252a73 | -3.1893 | -44.0891 | 2024-10-30 01:15:24 | GOES-16 | PRESIDENTE JUSCELINO | MARANHÃO | Brasil | 2109205 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 9f91feb5-1d05-39a2-9080-24ce5add2160 | -3.1213 | -51.1036 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 404299e2-22d2-3bf0-9ae4-ff6eea1179ac | -3.16 | -50.6231 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 05fd908e-1451-3be5-baaa-b59d23414c2b | -3.1601 | -50.6021 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c7b80472-c791-33ea-9bc7-a83440e1ea1b | -3.1786 | -50.6016 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 9dece42d-f3b2-38fb-8201-519bdc00c589 | -3.1787 | -50.5807 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 3395ce4f-bc3e-3533-9311-f78a79a122c0 | -3.2079 | -44.1113 | 2024-10-30 01:15:24 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 983947ba-fd61-3e2b-93ca-aa6c69601a2f | -3.208 | -44.0884 | 2024-10-30 01:15:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 56a0ece8-cc1a-328d-9941-41504137e388 | -3.234 | -50.5999 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| fb478c2f-e563-362a-bf86-135be1e36ab8 | -3.234 | -50.5789 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 6bea90f5-2e52-3fde-813f-eadff38894e0 | -3.2357 | -50.1805 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 00433030-150a-3af9-ab1b-790bb40ec95c | -3.2535 | -50.3479 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| ef21f282-e6ec-3579-8c4d-fefe8ccc6843 | -3.2719 | -50.3473 | 2024-10-30 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e83b8b66-2777-30bc-80b6-1331502979dc | -3.4316 | -44.0787 | 2024-10-30 01:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 950bd714-57f1-3bc4-bf58-6b269c54dbc1 | -3.4317 | -44.0558 | 2024-10-30 01:15:25 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 47b4b6ab-e1bb-378f-9a86-c6077c283a68 | -3.4502 | -44.0779 | 2024-10-30 01:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9d9b86ba-9b56-3b9f-a36d-84feda5cef59 | -3.5631 | -47.3847 | 2024-10-30 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 259.7 |
| d34b180a-d082-3221-a71b-8a3a917542b4 | -3.5632 | -47.3629 | 2024-10-30 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 32801672-77c7-3ca2-979f-10a86eccd93c | -3.5688 | -50.043 | 2024-10-30 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| f36cb508-62d1-362e-a3e1-b33f803eb7c8 | -3.5689 | -50.0219 | 2024-10-30 01:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 21582625-f734-3382-9253-2157f92935ca | -3.5817 | -47.384 | 2024-10-30 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 262.8 |
| 9da8b9d6-0bc8-39af-815f-3c4ca5bebbcb | -3.5818 | -47.3621 | 2024-10-30 01:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 1fff6063-0dd7-3385-9063-68fde44527dd | -3.8037 | -51.1644 | 2024-10-30 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 48ab061e-228a-36a0-b38b-da717f2edb42 | -3.8038 | -51.1436 | 2024-10-30 01:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 21680091-9018-32be-920e-eacc68e730cf | -3.9326 | -41.4957 | 2024-10-30 01:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 425e27d3-f80d-34aa-9e7f-e97585f5fa66 | -3.9327 | -41.4717 | 2024-10-30 01:15:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 13aec632-8b66-3a8b-9de4-7f1cefafb22a | -3.8221 | -51.1637 | 2024-10-30 01:15:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 05f07a56-cd6d-3e7e-98a7-6474f83bd120 | -3.9486 | -48.1291 | 2024-10-30 01:15:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 97e60899-7d84-3fee-9410-310df312259d | -4.0268 | -54.8008 | 2024-10-30 01:15:29 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f1ed918a-c2ae-3cdf-b4f8-1ecd06656b91 | -4.0705 | -46.2836 | 2024-10-30 01:15:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ae396137-c795-3530-a999-27a781a4b637 | -4.0681 | -50.024 | 2024-10-30 01:15:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| b9171bee-b28d-38f2-bf4e-462ae6a4eda3 | -4.3473 | -43.779 | 2024-10-30 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9d92435d-3c56-365a-929c-aa2efe1a155b | -4.2561 | -43.46 | 2024-10-30 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 395e05d5-c06d-3c24-9400-c61de6528328 | -4.2563 | -43.4368 | 2024-10-30 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| f007aef6-8450-3c4c-970f-60e5bd998572 | -4.2748 | -43.4589 | 2024-10-30 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| b55c17ba-f260-3ece-9859-fc12dff0c4db | -4.2749 | -43.4357 | 2024-10-30 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| adb03d76-f72c-3850-97c4-e0efb4d97465 | -4.4971 | -46.4618 | 2024-10-30 01:15:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 160.4 |
| ce7b53b9-9185-3f44-98fa-1941e6aaf060 | -4.4972 | -46.4396 | 2024-10-30 01:15:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 71f18db5-08b9-3441-94d6-d2cda33caa40 | -4.5157 | -46.4608 | 2024-10-30 01:15:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| c7f8f840-c4b6-352d-baa1-5dc2ac4aab48 | -4.8606 | -42.6275 | 2024-10-30 01:15:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 17f751bf-8398-3ebd-8a7b-bc8c8b72e0d0 | -4.9311 | -43.1857 | 2024-10-30 01:15:34 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 6e4003ea-c0fe-3fb8-9d50-05ebb0bb5c4a | -5.2306 | -47.9566 | 2024-10-30 01:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 02ed16ce-bddb-3d7b-a27a-150c854924f0 | -5.2308 | -47.9349 | 2024-10-30 01:15:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| df5e8dd4-0fbc-37fd-9f2f-cc849799740e | -5.9788 | -45.3621 | 2024-10-30 01:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c91b0928-5ec4-3254-bc0d-1bd727ed1954 | -6.8408 | -59.0519 | 2024-10-30 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 8fe3c9b5-47b0-3cf7-ab74-9890facd3d33 | -6.8409 | -59.0326 | 2024-10-30 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 5943af48-b92d-37f2-8e9f-91e8314259a9 | -6.8592 | -59.0511 | 2024-10-30 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b00a458b-9a69-3db1-aadd-af039a44ea69 | -6.8593 | -59.0318 | 2024-10-30 01:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 6a0db9f3-fc6f-3fc9-b4d7-558cb0002db1 | -7.8736 | -46.9065 | 2024-10-30 01:15:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 14d2de33-1d16-37de-8322-561b9c3a283d | -10.2111 | -36.7201 | 2024-10-30 01:16:02 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.2 |
| 52b0ffdd-9e29-375c-8ce7-f9f9446c356d | -10.2299 | -36.7435 | 2024-10-30 01:16:03 | GOES-16 | PORTO REAL DO COLÉGIO | ALAGOAS | Brasil | 2707503 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 30774c9e-d6fb-3e1e-8c16-c3cc6dc3a98e | -10.2304 | -36.7167 | 2024-10-30 01:16:03 | GOES-16 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 232.2 |
| ab796914-a087-3134-b3b7-7a8dbadc18ce | -10.3434 | -49.6536 | 2024-10-30 01:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 8c30e3d7-3786-3438-92b4-2aed1836476b | -10.7171 | -44.9391 | 2024-10-30 01:16:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f9a3185b-98a3-3b07-a15b-e00095523e07 | -10.7175 | -44.916 | 2024-10-30 01:16:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 323d7bd5-49f4-3941-b931-d888049fb5e9 | -12.899 | -45.0549 | 2024-10-30 01:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| e18f8d95-cf41-32e8-a85b-881304ed1f3c | -19.5862 | -56.7136 | 2024-10-30 01:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| 55402e13-2e00-30aa-bfc5-24533891dc61 | -23.9923 | -54.1106 | 2024-10-30 01:17:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.3 |
| d44cca80-d7b2-3698-862c-d1f9d2777a59 | -3.0913 | -54.287 | 2024-10-30 01:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3ed7c7c7-0c9a-3eb5-9e76-09ff7f4fa78c | -3.0914 | -54.2669 | 2024-10-30 01:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| aa460983-686f-3bb0-a018-b59478317e1f | -3.1028 | -51.1041 | 2024-10-30 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 40d4c31e-6012-39ac-9673-58b37ac3676d | -3.1097 | -54.2865 | 2024-10-30 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 11d8c9a0-3de0-3fad-bf65-a1bfa22678db | -3.1098 | -54.2665 | 2024-10-30 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| cf7819be-b022-3312-8c93-2cb06e9f0db0 | -3.1281 | -54.266 | 2024-10-30 01:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e95177ef-4c96-3db7-969c-c34bd8534dfa | -3.16 | -50.6231 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0835e787-0899-3f11-b0e8-ce44f434019c | -3.1601 | -50.6021 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| b77bd0e0-0ae2-3c4d-813c-f7707aa91e0c | -3.1602 | -50.5812 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| d7a87be7-c941-3051-af7b-350be39c55bd | -3.1786 | -50.6016 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| c64a9bd2-378f-319e-bdb2-8451aa7f7850 | -3.1787 | -50.5807 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.2 |
| fd06cd0a-5782-35e7-ae95-4b36b079b35a | -3.2172 | -50.1811 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 4a9697d4-92e2-3416-b082-b0add61d453b | -3.234 | -50.5789 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4c6976c0-65de-3521-8d63-282f945ee537 | -3.2534 | -50.3689 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4a026d02-234e-34db-8ff4-630396eefe93 | -3.2535 | -50.3479 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 7684cbd4-5bca-371e-b00b-089dc0b95aa6 | -3.2719 | -50.3473 | 2024-10-30 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 53071391-fd2c-3a48-954f-d029fe714b07 | -3.563 | -47.4066 | 2024-10-30 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| b679c0b0-70de-3d35-8179-f48d553dc52a | -3.5631 | -47.3847 | 2024-10-30 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 274.1 |
| 99ad0129-5289-39d1-b706-7a4bfda76592 | -3.5632 | -47.3629 | 2024-10-30 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 148.7 |
| b0dba22d-9727-39d0-8a76-94524fcd1aa8 | -3.5688 | -50.043 | 2024-10-30 01:25:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| c9fa8a15-f3de-3085-a4e5-d7d82e9db374 | -3.5815 | -47.4058 | 2024-10-30 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 59490328-17c7-3f27-a9d8-a56f4118516a | -3.5817 | -47.384 | 2024-10-30 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 285.4 |
| 7ea18c57-0ed5-3773-96a8-c0147b2a7765 | -3.5818 | -47.3621 | 2024-10-30 01:25:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 164.0 |
| c706b3a7-41bb-3d5d-b215-f0ae4d0bb98e | -3.8036 | -51.1852 | 2024-10-30 01:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ab8423f7-cc01-3c3d-8328-051fc9428491 | -3.8037 | -51.1644 | 2024-10-30 01:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| f3d75326-ddc5-37a6-bca0-cbdf840e370b | -3.9326 | -41.4957 | 2024-10-30 01:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| ded6aae5-4901-3b7c-aabb-9ab8f34dcc44 | -3.9486 | -48.1291 | 2024-10-30 01:25:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| dda7b3c2-ad92-3049-a551-f5ff741a20f1 | -4.0268 | -54.8008 | 2024-10-30 01:25:29 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 145646bb-a78e-3a23-a988-f722e3a78a7e | -4.2749 | -43.4357 | 2024-10-30 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 35a3c330-a492-3466-a6f5-ee341afefdeb | -4.2561 | -43.46 | 2024-10-30 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0cbdab11-bb3f-324b-b091-eb4419dc9f25 | -4.2563 | -43.4368 | 2024-10-30 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| b802792c-7138-3217-abeb-206a5c98555b | -4.2748 | -43.4589 | 2024-10-30 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1d98067b-04ec-33d9-af63-9fd75c2b6bfa | -4.3473 | -43.779 | 2024-10-30 01:25:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e06546c7-8ed9-37e7-ac86-d6f8f007f85f | -4.2681 | -50.6669 | 2024-10-30 01:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 5c204350-ebf6-30d2-bc77-4d0d96f36f51 | -4.4971 | -46.4618 | 2024-10-30 01:25:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 250029df-5e4d-30d5-800d-290f8e4a5c53 | -4.4972 | -46.4396 | 2024-10-30 01:25:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 547352d6-f3e8-348f-a2a1-8befaf8118c8 | -4.5157 | -46.4608 | 2024-10-30 01:25:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 28c2e4a1-5c79-3ff1-9e3a-0f149aa8ec28 | -4.7068 | -45.7373 | 2024-10-30 01:25:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |


[Clique aqui para ver as próximas entradas](README20.md)
