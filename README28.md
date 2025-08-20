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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2688f56c-9a7c-340f-ae4e-9c63b231598a | -7.57782 | -45.41458 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cabf412-87a2-3e8c-8915-31698fa0cd26 | -7.21494 | -48.20545 | 2025-08-20 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61a746b0-344e-3305-b943-c0450db48e98 | -3.27362 | -49.14397 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 470c42c0-9115-3fff-8178-a734f8bdc66d | -6.45827 | -53.38091 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3454f3f9-e538-3658-a967-0bba392bfa20 | -6.63017 | -35.06776 | 2025-08-20 04:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 21bf25bc-3a89-3eec-a1d1-cbe1c8fd5669 | -7.25001 | -50.17795 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57809d93-f5d5-34cf-9642-0d2d9c595055 | -8.17167 | -47.35221 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13c469a1-01b3-3a94-a9cd-2ffac9a7e032 | -7.83293 | -47.67589 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 659df44d-f91b-313b-9835-7a6d2ca8fdbd | -5.40397 | -45.14633 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85333789-9323-3e22-8bd3-972b90cc7594 | -7.22903 | -44.25339 | 2025-08-20 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 779a1ec6-c40f-35ac-a45e-6c30e4e0300d | -6.40627 | -42.49815 | 2025-08-20 04:34:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6070e568-04e8-3e18-a02d-0fda6f5681d4 | -7.6665 | -45.25654 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79c03052-802f-3e3d-8b5f-8e782a90bb24 | -6.51465 | -43.69865 | 2025-08-20 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61238d1d-53d5-3d67-ba21-0db63dc42af0 | -4.95738 | -43.08752 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dbe1f35-3f03-30a8-ab0d-9ff3cabd8bf1 | -6.27093 | -43.70496 | 2025-08-20 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d061ba8-9b55-3b52-9f93-270046f126df | -5.6136 | -43.47054 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69b18ec5-dffa-3356-8e92-a463e9e8b4a6 | -7.73438 | -44.01334 | 2025-08-20 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ead9db2-851e-3407-8358-0a87177075bc | -6.00177 | -44.29185 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a623bee-e729-3b26-a727-2688cb313259 | -5.99689 | -42.85646 | 2025-08-20 04:34:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2115021a-9e92-3d00-9c84-dcb4210fc728 | -3.81979 | -41.57019 | 2025-08-20 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 303a56e9-4c49-3556-a189-4b12e86491c4 | -7.21439 | -48.20893 | 2025-08-20 04:34:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0c17c1a-7539-321b-a044-0883a6c69ffa | -3.23431 | -46.80011 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bed1415c-4c32-3926-99a3-90e8e5a392ac | -4.72593 | -38.39812 | 2025-08-20 04:34:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4984a883-6f2b-3048-9dd1-7b814d8276e7 | -6.0553 | -45.05389 | 2025-08-20 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c694ed2-d444-3354-9484-3306392bad24 | -3.26955 | -49.14721 | 2025-08-20 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6127287-5b24-3987-b458-2873f25c4154 | -4.17417 | -42.02316 | 2025-08-20 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7f93c8e5-ccd9-3281-8cd5-1e0a68adff4b | -2.7783 | -48.59601 | 2025-08-20 04:34:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e025e0f-8f5e-3257-b2a2-fe7b576630b7 | -6.14511 | -57.71631 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2be44c7-fdbe-347c-961c-dddaeb901ede | -3.48195 | -47.67868 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a8052f-7c64-3e9c-b833-6f2f8dff2985 | -3.87627 | -50.97736 | 2025-08-20 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3a1f2752-f58e-3324-91c3-58dbcd0b1d02 | -7.27784 | -50.18256 | 2025-08-20 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f665ac7c-25c0-3809-962f-357218b27411 | -5.64236 | -43.38424 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb545922-6bed-3e2e-a99d-004028b04aea | -6.95083 | -42.87619 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| dd7ca07f-fe00-339e-aa60-4f187f692f71 | -3.65229 | -48.32824 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e52e24d-bacb-336d-bef5-56a530f5937a | -6.91793 | -43.83422 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38897600-fb5c-3cae-8dff-3ace6c3a3789 | -6.67519 | -43.68614 | 2025-08-20 04:34:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b284e140-2cf3-33f9-b012-13045d9db3ec | -9.87297 | -45.97428 | 2025-08-20 04:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f4eeac4-e060-3824-bade-b9157452cfcf | -8.16832 | -47.35168 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4e7e6b2-03e8-33ac-9a73-7ed6b7a19c8f | -7.6408 | -45.28653 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0de6ac41-a748-303f-99a1-2b6d17d1c84b | -5.86837 | -48.1198 | 2025-08-20 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae243f82-a72c-39a2-a12b-7a27386b1f93 | -6.94732 | -42.87201 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| d4b15d65-6f6d-3923-822b-e3e6e97cc9bb | -6.8688 | -43.11523 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df2589e2-c4df-3cd4-80c6-768400da5cc6 | -4.91302 | -43.23856 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7e910fe4-8dd8-34bf-9e49-c4394a7dabb9 | -6.63806 | -48.68425 | 2025-08-20 04:34:00 | NPP-375D | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8677096-a6d1-3f8c-9612-553fedc7121f | -7.05117 | -59.23512 | 2025-08-20 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c863db2-990f-301b-98cc-18795b8b7877 | -6.13773 | -45.1508 | 2025-08-20 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3bc48eb-75e6-330f-ba59-fce6696394da | -3.74083 | -48.93285 | 2025-08-20 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac78ce0f-2af9-3af6-b9c0-26d331aacf99 | -6.05026 | -44.14543 | 2025-08-20 04:34:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a28d65e6-4ad9-3576-a32a-736ef4c041c4 | -4.31049 | -48.1025 | 2025-08-20 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 707b9b56-8591-3f9a-8b86-46377b14ac3f | -9.85596 | -44.69083 | 2025-08-20 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 486f8224-6b97-3a86-b431-54c516c3792d | -7.39589 | -44.27483 | 2025-08-20 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 817f6539-43eb-35ba-a980-6366356c7e33 | -5.63329 | -43.39236 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75c903c1-4ce1-39c6-b085-54735ca96148 | -6.14391 | -57.71387 | 2025-08-20 04:34:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae8bd2a7-1cc5-3756-a737-636d3f9edf91 | -6.96901 | -42.86443 | 2025-08-20 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 44fb1eb6-7169-3fbb-a3e9-9421cf49c55e | -7.63557 | -45.27337 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e278b95-5ae3-3cba-a2b1-39433cac3975 | -5.78456 | -43.89093 | 2025-08-20 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 193d34e9-241e-3a51-9f49-c30af7e20066 | -3.23485 | -46.79665 | 2025-08-20 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 791c1e8e-622a-3884-a337-a677a8fcbbe2 | -5.6107 | -45.18422 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f551c95f-2b29-374b-853a-34fa409cb3e2 | -4.02333 | -48.06084 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68fc1021-4c69-306e-a67e-8f6e0b6f3051 | -6.19366 | -53.52073 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef603947-97cf-3850-8e11-e2c43f2a7c5f | -5.88187 | -46.19397 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb394324-2812-3d1f-9046-ed760aeb45d1 | -5.82634 | -50.1648 | 2025-08-20 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b733076-2496-357d-9246-592a3ea4026d | -7.58423 | -45.41976 | 2025-08-20 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8362398-73b1-3730-b19e-74da72fe3339 | -6.23483 | -44.44956 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2acb52b1-e0f2-3133-a7fb-18a2b6db5fa0 | -5.63711 | -43.39299 | 2025-08-20 04:34:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bdfe82c-09d3-3e76-9579-e311958b029f | -4.39095 | -47.76834 | 2025-08-20 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d26f10cf-8a24-3e5f-8642-b2d4ea91b301 | -4.17363 | -42.02675 | 2025-08-20 04:34:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 73291e16-2bee-34ab-9b5d-d323c64f8e58 | -7.04632 | -59.23193 | 2025-08-20 04:34:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60588782-2549-31b7-b610-32c53c1b4010 | -7.6355 | -56.75359 | 2025-08-20 04:34:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2e7a65a-5fae-3032-b8a4-f9ec689e3dbd | -5.87246 | -50.1481 | 2025-08-20 04:34:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da7a4096-0c8c-3a53-be91-3a72cda35978 | -6.86475 | -43.59903 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 856c7e71-5fe8-3302-9d63-0a70aa2ca40b | -2.90297 | -48.29612 | 2025-08-20 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182d4797-4248-303d-8d36-2881a3689e0f | -5.11263 | -43.21579 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 033708c5-9ac4-3de1-b57d-00410cbff532 | -6.5731 | -43.01493 | 2025-08-20 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb44f5df-f10d-38df-89d9-06b48e11e7c9 | -6.19433 | -53.51675 | 2025-08-20 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84cd2ebe-fd19-3ff8-b51b-726d99602353 | -7.23275 | -44.25396 | 2025-08-20 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b317cb0f-ece8-3c03-86ff-a9e56ba3aed6 | -7.12592 | -44.6392 | 2025-08-20 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d2166cf-250b-3cd0-81fc-7d07d64b9e7e | -7.6594 | -45.25543 | 2025-08-20 04:34:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8f95530d-ba0c-3498-9214-f851f093a1d6 | -8.78929 | -45.47769 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adfb4ff7-b017-32c6-b0e8-00888541d6f3 | -5.9772 | -43.61065 | 2025-08-20 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 382519f7-2237-3258-9f5d-070a679e0c67 | -6.28167 | -43.71091 | 2025-08-20 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb2c579f-47f9-386d-960b-8284fc84bf3a | -8.0284 | -47.66387 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84c42484-2214-3211-a482-df643fe725a9 | -9.27084 | -44.53341 | 2025-08-20 04:34:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a78d3e2-5572-34ba-8174-d1ef38b6bfa7 | -6.53295 | -45.51675 | 2025-08-20 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a44c6bc-899f-3050-a5f1-4235946a826e | -8.79702 | -45.47473 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d4ca2fdb-e0a2-3d91-9659-3cfe0d0fd297 | -6.63265 | -35.06456 | 2025-08-20 04:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5e01e36d-f656-3e4c-971f-87a5b455794a | -8.82649 | -52.03545 | 2025-08-20 04:34:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c34ae150-1f60-39fa-b1e2-408e78a2181b | -6.71823 | -44.3282 | 2025-08-20 04:34:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 878674d9-e22d-33a4-97ed-31f182c70483 | -8.06725 | -43.66837 | 2025-08-20 04:34:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 270c7d96-e8b7-3dd5-8954-d0902ec36998 | -4.9123 | -43.24323 | 2025-08-20 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7c2b3884-a5d9-3f31-97d6-2e6504f27962 | -6.39851 | -44.25961 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9988f603-5377-3131-9d9b-6e648a750070 | -5.80386 | -46.1343 | 2025-08-20 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d609687-f530-3f82-8f59-4575f7470945 | -8.80614 | -45.43885 | 2025-08-20 04:34:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ff1c20cb-17bf-3cf0-beeb-32bf21ae9c16 | -4.00397 | -47.09441 | 2025-08-20 04:34:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54515a24-5158-3d67-bd0f-feea676557fe | -8.16722 | -47.35872 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef4def72-3b78-3584-ba54-7e33f745f22a | -6.57796 | -44.46932 | 2025-08-20 04:34:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f85114d-2f7f-3ed4-b794-3f78ad5964f3 | -8.67421 | -47.98435 | 2025-08-20 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fb4c88c-5405-3268-a681-97667d8bee53 | -8.22163 | -47.31005 | 2025-08-20 04:34:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59ff961a-dc36-3971-a11d-0749a136d51e | -6.8693 | -43.59488 | 2025-08-20 04:34:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dc41b9a-906f-30bc-9f8a-6c400c029438 | -5.40856 | -45.18649 | 2025-08-20 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README29.md)
