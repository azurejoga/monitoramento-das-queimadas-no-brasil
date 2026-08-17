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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c44fdf4-0099-3be4-b64c-68b89d1829a9 | -6.6384 | -58.9636 | 2026-08-17 08:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 81569dd3-aec5-3e75-a03e-616e6132000c | -10.5085 | -50.0228 | 2026-08-17 08:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 051d06a7-0601-34a2-bff6-b5dc3bd8d3f4 | -12.7009 | -48.5195 | 2026-08-17 08:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f68965fe-2a64-3790-80d2-d59f562842bb | -6.6568 | -58.9628 | 2026-08-17 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| b52f43a2-3e7c-336b-a2a6-d720e64e77c5 | -6.6568 | -58.9628 | 2026-08-17 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6f6fad0e-a387-3bec-9e9f-9f4f71cf9ed4 | -7.4055 | -46.8368 | 2026-08-17 10:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f20c5933-c18c-3f5e-8852-b1325ca25680 | -11.1487 | -46.5219 | 2026-08-17 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 9e847b66-e270-3819-9495-93d535c22469 | -11.1487 | -46.5219 | 2026-08-17 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 794d508a-899a-35b4-b708-0152bb9a9012 | -7.4055 | -46.8368 | 2026-08-17 10:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| a8649ce0-2451-3022-b814-a9b9236217b6 | -10.5085 | -50.0228 | 2026-08-17 11:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 0b81f5c7-b51e-39ec-aa3f-cc28c2bbf824 | -11.1487 | -46.5219 | 2026-08-17 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2883abdc-a6b3-363e-9dd4-02bf190412cf | -11.149 | -46.4994 | 2026-08-17 11:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 108a8ef9-ebbf-3c8a-8404-962ac668835f | -7.8071 | -47.8372 | 2026-08-17 11:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| a6becb4d-227c-371c-aa21-9884bad5ad59 | -11.149 | -46.4994 | 2026-08-17 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 176.3 |
| 0802ae6d-1952-3c7d-b907-dc3837659a20 | -11.1487 | -46.5219 | 2026-08-17 11:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 232.2 |
| ce7ed93d-0eb5-3e86-88e3-24e69a1d91f3 | -7.13455 | -44.07704 | 2026-08-17 11:15:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 6eaf6bb9-0f17-37ff-a6f5-3988cf40c804 | -8.40148 | -39.74917 | 2026-08-17 11:15:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8bac91e5-56a2-30ce-a451-481b868e5fad | -5.62413 | -42.93452 | 2026-08-17 11:15:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 4377f85d-dcd0-3439-ba9b-1c10656c8fc0 | -5.61355 | -42.93284 | 2026-08-17 11:15:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| b1873a74-6046-3f99-ba2d-0f39a940db78 | -5.60803 | -43.36607 | 2026-08-17 11:15:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| bde578ea-e4e3-35b9-8970-57fd51d9bcf5 | -7.00596 | -43.79146 | 2026-08-17 11:15:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e6cde571-ff7f-3e04-944a-ca40404db5d2 | -6.53532 | -43.11174 | 2026-08-17 11:15:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 32a072e4-b55b-39e6-b466-4a76811b90b5 | -6.89477 | -42.84811 | 2026-08-17 11:15:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.4 |
| d38b7bf7-2ba4-34ae-a024-9c78596de5fa | -6.89207 | -45.27966 | 2026-08-17 11:15:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| aa1f846c-53ed-31f3-861e-b59b9e22aa5b | -3.88582 | -40.36842 | 2026-08-17 11:15:00 | TERRA_M-M | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 53fe420d-ae7c-32ba-bb67-96df420f85d1 | -6.39945 | -41.70751 | 2026-08-17 11:15:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 61316407-02ed-3973-939a-1f4430d10443 | -3.40174 | -40.07423 | 2026-08-17 11:15:00 | TERRA_M-M | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 4b985e1d-d89b-3a24-9ede-edb6218f5e58 | -5.96138 | -38.62913 | 2026-08-17 11:15:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 83fe9ad9-d704-34be-be6d-51c7f3ed7ed0 | -6.52887 | -43.11744 | 2026-08-17 11:15:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3ea9ece7-b371-3d37-b751-c8c27c66d252 | -5.95254 | -38.6279 | 2026-08-17 11:15:00 | TERRA_M-M | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 3fb0d6a5-a4a4-3fd1-94d9-7163026f12b1 | -5.10357 | -38.05019 | 2026-08-17 11:15:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 48b98413-f5c9-34c0-91e0-5c535513688f | -5.59999 | -37.73548 | 2026-08-17 11:15:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 640f4934-cddc-376e-bd8c-dae94d1b8bec | -5.5987 | -37.74462 | 2026-08-17 11:15:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 45fe9dd5-2b55-3a46-b587-e9094a1b7fff | -7.13693 | -44.06176 | 2026-08-17 11:15:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 50ee7d2c-aae8-3e5f-975e-2a8f7536037d | -12.52488 | -47.88977 | 2026-08-17 11:17:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 42ce7cc5-9fe1-3aab-b52a-7110fd526bb8 | -7.39771 | -46.83066 | 2026-08-17 11:17:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| c09643e3-5b4a-3c0c-ac57-8feb8b2e73c9 | -12.69288 | -48.51252 | 2026-08-17 11:17:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| f8ec85ad-fb98-305c-ba70-6355f9fba9b1 | -14.86715 | -46.65974 | 2026-08-17 11:17:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c67a7cb2-6825-3e7f-8011-0c51be8437a1 | -11.12467 | -47.24738 | 2026-08-17 11:17:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 639749bf-6378-3127-aebf-f5fa8cac1b60 | -13.44424 | -43.85094 | 2026-08-17 11:17:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a01d20b-9b5e-32c8-a39b-1935b4038168 | -9.75652 | -45.70905 | 2026-08-17 11:17:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eccf4fa6-6901-3205-8364-7d41ea471636 | -13.44612 | -43.83904 | 2026-08-17 11:17:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| acb8b721-2fbd-3167-b3fe-14afc5522153 | -11.31757 | -46.30606 | 2026-08-17 11:17:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1136af76-ac4b-3019-bf69-9721622375dd | -10.51851 | -50.01333 | 2026-08-17 11:17:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 1f473299-3fc9-3aa1-b961-b6fc590316e9 | -12.33088 | -47.26646 | 2026-08-17 11:17:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| f74b5646-7e61-392b-b0b8-b42e28c16360 | -11.14637 | -46.54476 | 2026-08-17 11:17:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ea77d3f9-f65d-38dd-9c89-359fd2727ce6 | -11.12739 | -46.50031 | 2026-08-17 11:17:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| cf199b6e-c133-32eb-8a94-075a4e9f44d9 | -12.25788 | -45.929 | 2026-08-17 11:17:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 715b606c-ade1-375e-b6b0-d520c873aa03 | -12.3303 | -47.25119 | 2026-08-17 11:17:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 87361c96-39e8-3fdd-8b19-e035da20dfd7 | -14.47547 | -45.68108 | 2026-08-17 11:17:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b98b774f-1e7d-3b84-a303-af9e76a30243 | -12.3344 | -47.24492 | 2026-08-17 11:17:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6cabce6e-4793-346b-b7b1-2b383e75bb24 | -13.51746 | -46.23551 | 2026-08-17 11:17:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| fd72f4cd-79df-3f5f-9300-7661446819eb | -11.49409 | -46.59315 | 2026-08-17 11:17:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| cacd01ac-c529-39bf-9207-4eafe0af796a | -12.26334 | -45.89483 | 2026-08-17 11:17:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d01c51fe-0810-3471-8474-345cdf2852cb | -11.31229 | -45.85054 | 2026-08-17 11:17:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 3182876f-ecff-3ef7-b0f1-380f101deeae | -14.87025 | -46.64125 | 2026-08-17 11:17:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a82dcd12-9ed6-331a-b276-6c9bb4f9dedb | -11.14894 | -46.53164 | 2026-08-17 11:17:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 288d77d1-01c5-360d-b68b-2f9ae5a469a4 | -7.7984 | -47.86219 | 2026-08-17 11:17:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 18171d67-32aa-3016-8de6-13c78bad55f0 | -13.51186 | -46.2287 | 2026-08-17 11:17:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 78f2bc19-385c-30b2-96b4-db650260781d | -11.15239 | -46.51115 | 2026-08-17 11:17:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 303.4 |
| 8417ca61-e03b-32e0-90f3-a6ce7e98fbbb | -11.49491 | -46.58578 | 2026-08-17 11:17:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 279f5fdf-e9d1-32e1-bd70-fea19aa17e4c | -11.46936 | -46.58223 | 2026-08-17 11:17:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 907a9ebd-d0f8-3e97-95e1-dafa29e4ebe8 | -11.14959 | -46.52468 | 2026-08-17 11:17:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 315.3 |
| a1ea73c4-63f7-3944-b18a-de616c7e69c2 | -14.88234 | -46.64256 | 2026-08-17 11:17:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 4acc1327-c6aa-3220-89e0-a0e3e5bb3526 | -7.79604 | -47.86921 | 2026-08-17 11:17:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 8dc32ce7-9465-30b0-bc4f-1fd960340feb | -20.61389 | -45.92755 | 2026-08-17 11:19:00 | TERRA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6f24cc2b-efb1-3ebb-b3da-fadaaf1e3a19 | -19.54041 | -44.03341 | 2026-08-17 11:19:00 | TERRA_M-M | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bbdd9a56-10e9-307b-85b6-72b82303f6a9 | -20.616 | -45.91476 | 2026-08-17 11:19:00 | TERRA_M-M | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f3a5e86e-2735-351a-b2a4-ca6e7d762db5 | -21.63947 | -46.36893 | 2026-08-17 11:19:00 | TERRA_M-M | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| e91877e6-bda7-34fe-b50e-bfda9c1802b6 | -16.39357 | -45.10908 | 2026-08-17 11:19:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 97aa7912-12bd-36ff-86cc-351f3d3b1bdd | -11.149 | -46.4994 | 2026-08-17 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 6cbea15b-e7ac-3a47-825d-9cc0da55e5cc | -7.8071 | -47.8372 | 2026-08-17 11:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2b99d787-5add-35af-b06c-e90543e8949b | -11.1487 | -46.5219 | 2026-08-17 11:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 357.7 |
| 372e720b-74ea-3c55-a3ca-d73f6ab9a064 | -10.5085 | -50.0228 | 2026-08-17 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 7e1ef416-d5f3-34f3-afae-2fa600c1c0a5 | -10.5085 | -50.0228 | 2026-08-17 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f92a2dde-ca9b-3d51-a7e6-621a05f5b439 | -11.149 | -46.4994 | 2026-08-17 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 220.0 |
| d0f4357b-ad60-3872-9397-57611867f19a | -13.5128 | -46.2219 | 2026-08-17 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 13e7537d-3e63-375f-98fc-7e75963a491b | -11.1487 | -46.5219 | 2026-08-17 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 542.1 |
| 92e6edca-8264-3b1d-8ca2-5a541e3b3e27 | -7.8071 | -47.8372 | 2026-08-17 11:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 172.5 |
| ee14ec61-84a5-357e-89e5-a632a687edcf | -11.1296 | -46.5244 | 2026-08-17 11:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| abb61cce-39e4-3f45-942e-0f0b0abc4be1 | -7.8071 | -47.8372 | 2026-08-17 11:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 239.5 |
| 1c2b09fa-2085-38f0-9fbe-f250fe10c79f | -7.6053 | -45.7238 | 2026-08-17 11:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 201.6 |
| 91f42c56-e264-3935-8417-dffc7fc303dd | -10.5085 | -50.0228 | 2026-08-17 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 750c495a-9ac1-3394-9637-65a695f51a54 | -13.5124 | -46.2449 | 2026-08-17 11:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 5523a440-1c75-3d6e-8b8e-cf04dc3fdc7e | -7.6053 | -45.7238 | 2026-08-17 11:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 355c3adf-764c-3541-a1c0-3c3c6f1d6e35 | -13.5128 | -46.2219 | 2026-08-17 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 3c6f28b3-d9f9-3270-b0c2-c1dd5524ad2e | -7.8071 | -47.8372 | 2026-08-17 11:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 3b41144a-ddcf-3f56-b675-dabe6f30134c | -10.5085 | -50.0228 | 2026-08-17 11:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 1ac76e91-35b5-3f52-a212-fc5db9997ddf | -7.6053 | -45.7238 | 2026-08-17 12:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 155.7 |
| ca51ebf9-3496-30d9-aa8d-e9874de8c94e | -11.472 | -46.5692 | 2026-08-17 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a9f195d7-a098-320f-8476-11942992dd79 | -11.1487 | -46.5219 | 2026-08-17 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 677.6 |
| 09961ed8-8b0a-3ae3-8c4a-f186d5490d05 | -10.5085 | -50.0228 | 2026-08-17 12:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 28fde794-0716-3e27-886e-2239d30e94e8 | -11.4911 | -46.5666 | 2026-08-17 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 28c4333e-7e61-3ffe-84c0-256bf29e9e35 | -11.149 | -46.4994 | 2026-08-17 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 382.3 |
| e7056ef3-481f-3935-bdf1-7adb466e965e | -7.8071 | -47.8372 | 2026-08-17 12:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0cd9482f-280c-32d8-89fc-553f1d3a7f37 | -7.6053 | -45.7238 | 2026-08-17 12:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 3e8875b7-3129-3c27-81de-d68c757eb051 | -7.8071 | -47.8372 | 2026-08-17 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 444c17f2-4b46-3b38-9c58-ea115745e435 | -11.149 | -46.4994 | 2026-08-17 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 99569922-b40f-3950-99af-1ebcfa705a7b | -14.4871 | -51.9806 | 2026-08-17 12:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 57fe912d-780d-3e9a-95b4-6b302bf9829c | -10.6071 | -48.3873 | 2026-08-17 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |


[Clique aqui para ver as próximas entradas](README67.md)
