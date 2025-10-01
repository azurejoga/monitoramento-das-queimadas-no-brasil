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
| cfe06930-5908-34d1-898a-01d0e88d935a | -23.36084 | -47.16612 | 2025-10-01 03:34:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 025f14f3-fb54-34ea-9a1c-c74834b79ee1 | -23.22481 | -49.40339 | 2025-10-01 03:34:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bc1be231-5ac0-38e4-91a0-9c7ea41ad3df | -23.05741 | -47.03384 | 2025-10-01 03:34:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5d483394-0ac4-3bdc-a436-7dfdb3d29abd | -22.57549 | -46.77983 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f800f6b6-fdce-3485-8d67-3736ac03512a | -22.26997 | -46.71755 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2bcd3f6f-60a6-3d41-bafc-87bb370ca96a | -23.15437 | -50.09078 | 2025-10-01 03:34:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 5062f09e-10db-3bd5-b000-81fd6380eff9 | -22.27322 | -46.7293 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a5cfaabb-d2c8-34db-abd2-d2fe17a24e13 | -22.65534 | -46.75132 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b51863c-0a90-3ee7-803e-acf0fcf5ef5c | -23.20637 | -45.11726 | 2025-10-01 03:34:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a86868b7-de8d-3295-a2c2-efa939a35930 | -23.33184 | -46.86601 | 2025-10-01 03:34:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 305022a2-e03f-37c7-8a95-cfeefa3d2109 | -23.21163 | -45.11748 | 2025-10-01 03:34:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aa1cd04f-7151-3b28-ad5c-43ab1905790d | -22.43831 | -48.31443 | 2025-10-01 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a89d64f-aac2-3e1d-bd2a-41da12bd0c70 | -22.64952 | -46.7508 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49981293-8954-310b-abb4-3c62f0188f21 | -23.40046 | -47.05367 | 2025-10-01 03:34:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 562dfbd9-f953-3041-b088-42f886a9d6c4 | -22.44249 | -48.31511 | 2025-10-01 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3625bb0-39fa-3c67-b09d-348bc92e0600 | -22.57774 | -46.77833 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b0f93ab0-cd78-3889-8a53-48dbd24840f7 | -22.26408 | -46.71722 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| edeede25-701e-3207-9574-90aa148fa223 | -22.41377 | -45.11834 | 2025-10-01 03:34:00 | NOAA-20 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d16279c-bf92-3fc8-966d-2b40d0440c88 | -23.22334 | -49.40932 | 2025-10-01 03:34:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0d219387-851e-3088-8516-9ef312aa8673 | -23.15264 | -50.09759 | 2025-10-01 03:34:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 93d9e349-aa9a-352c-8b75-91289ebe7e97 | -22.26741 | -46.7207 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20fa460c-73df-391a-8e9d-7a5a23d3aea4 | -22.26159 | -46.72004 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7ad37efe-3c67-3995-8cb9-7f9f2d8854ef | -23.32898 | -46.86697 | 2025-10-01 03:34:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| deb69320-3642-3f3a-874c-cf0e11e9b2a3 | -22.92276 | -45.51001 | 2025-10-01 03:34:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4ef87215-cd50-3fea-be52-c0548734fb2d | -22.77702 | -47.61436 | 2025-10-01 03:34:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7929460a-20e4-3ed6-b2d9-d4d8ff97e774 | -23.36176 | -47.1621 | 2025-10-01 03:34:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90cdeffc-d8ae-30e0-8141-552633f5dd84 | -22.57672 | -46.7827 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6eb742f9-b9c0-3fea-9f3f-3a74b8abb903 | -23.58623 | -46.21989 | 2025-10-01 03:34:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de037a58-9bbf-33d8-9a7d-3c5f9e829ba2 | -22.58572 | -46.78723 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f73d0ee0-e6a3-3228-9e81-fa4abba54862 | -23.21256 | -45.1132 | 2025-10-01 03:34:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9b2a42ce-1463-3b3b-b6fc-3a9e8a6c452c | -23.20724 | -45.11329 | 2025-10-01 03:34:00 | NOAA-20 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76ac2dfb-3f6a-3f9c-94aa-b830d592996e | -11.3826 | -45.0774 | 2025-10-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 223.4 |
| 094839c5-73d5-3559-a600-c7adafd304fc | -3.1012 | -47.0301 | 2025-10-01 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| e6948000-12af-317c-a8f2-020d4d660218 | -16.2562 | -50.9275 | 2025-10-01 03:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 96aba6c6-c7d2-3739-aaed-126ae00b23da | -3.0827 | -47.0088 | 2025-10-01 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 3aa6cbca-cab6-30e7-9f15-3f9c2d38c94d | -11.383 | -45.0543 | 2025-10-01 03:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 1ae4d866-5459-3a00-8717-bdcbcb35950f | -9.4394 | -54.5739 | 2025-10-01 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bb0fe2ab-d54c-37e0-8ce6-9e22bdc96b06 | -3.1013 | -47.0082 | 2025-10-01 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 89ad9755-7d51-35a1-ab3a-693a4f05c911 | -18.6332 | -50.6978 | 2025-10-01 03:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| cb1fd292-037b-3f24-bde6-fb4adc1c1a51 | -6.1674 | -47.2638 | 2025-10-01 03:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3150cadf-d44d-31c5-887b-8a156e643180 | -22.5735 | -46.7755 | 2025-10-01 03:40:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.7 |
| 57a8e3b3-efa5-3f12-961b-cbdb06c01c94 | -3.0826 | -47.0308 | 2025-10-01 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 76bccc26-bbe4-3e4a-9abb-cb159f55aff9 | -14.1926 | -46.1091 | 2025-10-01 03:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 9280666b-c155-3275-b47b-d59c5e2fcbff | -14.3514 | -45.9437 | 2025-10-01 03:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 51813fee-e31a-37ae-8841-2575681284b4 | -14.3519 | -45.9206 | 2025-10-01 03:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b57778ef-b38e-3bb1-bbdb-a74d417fcc6c | -11.4588 | -45.0895 | 2025-10-01 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8b759e47-e574-3fa7-b37c-da4efb57c894 | -20.6302 | -46.2287 | 2025-10-01 03:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 56.9 |
| e8cf86bd-6a93-3aef-8367-fc379ea3e8ca | -11.8434 | -44.9872 | 2025-10-01 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3fff37ad-b73c-36d1-b742-3f964c923364 | -20.6515 | -46.1995 | 2025-10-01 03:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7ab58a0f-2279-3fe7-8328-6bc7bd8f3637 | -20.6309 | -46.2046 | 2025-10-01 03:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b357ed1a-e570-36a0-8105-a85d00338580 | -18.6327 | -50.72 | 2025-10-01 03:40:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| a43ddd9f-c893-31e7-8e5e-9516feb283f3 | -16.2562 | -50.9275 | 2025-10-01 03:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 47acc42e-11c0-3a7a-9457-4397a3643dfc | -3.1012 | -47.0301 | 2025-10-01 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 2aa2c513-f3f6-3c31-a77b-29b0c38623a6 | -3.1013 | -47.0082 | 2025-10-01 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 403152c9-dace-314e-942b-af01c54ab757 | -10.9007 | -46.554 | 2025-10-01 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c7d2043c-1f26-3426-9cdb-3e72a3792f52 | -11.3826 | -45.0774 | 2025-10-01 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| e5a78529-ef07-3ec8-b4fb-4bbbbd55c104 | -10.9197 | -46.5516 | 2025-10-01 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c98e5923-69f1-3f46-b543-b351344a7d7b | -11.8434 | -44.9872 | 2025-10-01 03:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 7b1b85b1-4bd8-38d2-a8b7-e5406d583043 | -3.0827 | -47.0088 | 2025-10-01 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4845a05a-756f-3b0a-aa99-72296a5f6b0c | -14.3519 | -45.9206 | 2025-10-01 03:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5522c460-1d55-3ac6-b55d-450e65b76b22 | -11.8622 | -45.0075 | 2025-10-01 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 11bfa9d5-df5d-3c64-847b-8f67057707c4 | -5.6363 | -43.9027 | 2025-10-01 04:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| a6dea060-5006-37bf-ae0d-ec1543a60787 | -11.8434 | -44.9872 | 2025-10-01 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| f77313f6-015c-381c-b884-fcdbf68e78d6 | -16.2562 | -50.9275 | 2025-10-01 04:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8b8e2501-9c66-3cd1-abca-fa383001667d | -11.843 | -45.0104 | 2025-10-01 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| bc4bc377-d444-3afb-93ad-57a606f5e8da | -15.1615 | -49.082 | 2025-10-01 04:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 7687a8b5-e6a2-3796-adb7-cc615ae1e257 | -3.0827 | -47.0088 | 2025-10-01 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| dbff0126-48d1-307a-8d2d-b609402641aa | -15.181 | -49.0788 | 2025-10-01 04:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b8028876-29fb-3103-8bef-a1e3da511292 | -12.8949 | -45.264 | 2025-10-01 04:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 849e426a-1b9e-3ca7-a390-d5c09291a516 | -5.6361 | -43.9258 | 2025-10-01 04:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| d2b5955d-c8ae-33e1-9f6c-c4fee9e871b3 | -3.1012 | -47.0301 | 2025-10-01 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| cdf7246b-17af-37e6-b568-b9fc8c1dea4e | -3.1013 | -47.0082 | 2025-10-01 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| a0990fd8-ec67-3ddb-b490-ff78a6830a97 | -11.8438 | -44.964 | 2025-10-01 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ddabd50e-a82b-350e-ad43-941200686b6e | -14.3519 | -45.9206 | 2025-10-01 04:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 65dadf12-4eef-35b0-90f6-094f222a74b5 | -14.3519 | -45.9206 | 2025-10-01 04:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 65d5871a-1bf2-33b9-9a59-8c890d01e5c4 | -11.8434 | -44.9872 | 2025-10-01 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 9bc4769b-f466-35d2-adf0-49206e26beaf | -9.3089 | -54.5229 | 2025-10-01 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a2563f4b-3c4c-3d50-815f-21cf1958fc97 | -16.2562 | -50.9275 | 2025-10-01 04:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 7909f389-0a40-375b-9a8b-4dd2df2a12e2 | -11.8246 | -44.9669 | 2025-10-01 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 02e319e9-b4df-3872-be04-6caf72056d94 | -12.8756 | -45.2671 | 2025-10-01 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 2d926d45-0a58-3dcb-82b1-a6dd0e88bcc8 | -12.8949 | -45.264 | 2025-10-01 04:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b811074a-b4f2-3605-9c3a-6bd477138599 | -11.8438 | -44.964 | 2025-10-01 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f363be8c-d5a7-3246-8e7d-3679d186268f | -11.843 | -45.0104 | 2025-10-01 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 385e4758-993e-304a-ab1c-7e2bfa0bec60 | -15.181 | -49.0788 | 2025-10-01 04:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 25eec7c4-974f-3e0f-8d9f-90af50c0e3dc | -14.8021 | -45.7946 | 2025-10-01 04:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| c4256233-bff2-3f0d-bf91-96c5ea80ada4 | -11.8622 | -45.0075 | 2025-10-01 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ee429637-1b1d-39ce-b7c6-26f58e8e62b7 | -0.09987 | -51.27907 | 2025-10-01 04:17:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76299f74-98f8-3c53-96a4-b165f03f2938 | -1.11725 | -48.03305 | 2025-10-01 04:17:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 684e4b43-d373-3e5b-84da-04d0e6264f9d | -0.90693 | -47.54507 | 2025-10-01 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d56f3011-b57c-3e6e-b971-8a8256c30893 | -1.33307 | -47.57251 | 2025-10-01 04:17:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea017933-086b-31fd-b130-013aeb320b0b | 1.28796 | -51.24488 | 2025-10-01 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 884461cd-f5ba-32d9-9cb5-95cf0f04dc33 | -0.90314 | -47.54453 | 2025-10-01 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7934fbc1-33c6-3e21-92d9-ae083ca0c816 | 1.2887 | -51.24825 | 2025-10-01 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b86057b-0139-3457-874c-43f7ebc7d867 | -1.14332 | -47.24809 | 2025-10-01 04:17:00 | NOAA-21 | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 025bd63a-489d-36ab-8f66-6a7696546000 | -1.33613 | -47.57764 | 2025-10-01 04:17:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33965002-de27-3d80-aebc-d512f290ddd1 | -1.33335 | -47.57523 | 2025-10-01 04:17:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d8bb1336-7d1e-3535-84b4-74717b2f19c8 | -2.98451 | -39.92928 | 2025-10-01 04:17:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 349d9abf-0e15-30f9-9651-461d75f1a01a | -1.69521 | -47.29089 | 2025-10-01 04:17:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04d2516d-df81-336f-87d8-327aa8dc7238 | -0.09803 | -51.27706 | 2025-10-01 04:17:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 682bb144-e7e5-377b-a5ac-d7b1c0b68ac8 | 2.26119 | -50.72844 | 2025-10-01 04:17:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README29.md)
