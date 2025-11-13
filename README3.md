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
| dae9f6e5-9ecd-3f6a-94e1-c2d8868db6b3 | -5.3855 | -46.766602 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecfc9522-dee5-3f2a-b617-db3acf017fdd | -5.3836 | -46.7584 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 248e4318-ee46-3fee-aa82-a11485b26f0d | -14.6817 | -51.881802 | 2025-11-13 00:14:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a43258fd-197b-38ef-8b8c-069052e12ab1 | -5.454 | -47.688301 | 2025-11-13 00:14:00 | METOP-B | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20618647-168e-3af5-9799-4136831a8dc6 | -3.2223 | -45.570499 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 77c268f9-b471-31d4-9e2c-cb5eaa064b83 | -5.6866 | -43.534302 | 2025-11-13 00:14:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a89c97cc-7a90-3169-bdf1-8d927b46b17e | -5.4452 | -44.6427 | 2025-11-13 00:14:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecd1fbaa-cf89-37ee-b407-14da4b8c394a | -3.7871 | -46.006901 | 2025-11-13 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25dd6a2d-9d37-3173-a250-616b25e83690 | -3.1545 | -50.258999 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa34acd-306e-3b40-ac9a-4ba88f587ad2 | -2.8188 | -45.428101 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c5b922f-5dbb-382f-8816-b11849c38f1b | -10.6185 | -45.230999 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 421b2c01-3b5f-30b8-b1dc-8e91825c5d28 | -6.2972 | -47.0075 | 2025-11-13 00:14:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0305409-f10f-31bc-8f5b-895805ca8d70 | -4.7216 | -46.437401 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb01ece3-b1c0-3ce0-b259-3c18652653a4 | -4.643 | -48.737301 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b8bbd03-be7b-3e97-922c-ccc6ddfa6eb4 | -3.6753 | -45.924599 | 2025-11-13 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73ce3fc7-25d5-3891-be12-ebf88755c4d7 | -7.8295 | -41.755901 | 2025-11-13 00:14:00 | METOP-B | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35861ab6-81f0-38e0-a13d-603559263149 | -3.3555 | -48.381199 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd8bac0-cc45-3a1d-8f98-d03b7ae611d4 | -3.1026 | -45.764 | 2025-11-13 00:14:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e910912a-ed0a-3333-8fd9-8d8466e4a37c | -7.672 | -45.8685 | 2025-11-13 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4377a229-a2ba-3025-8d15-06e28a54aa6d | -10.7465 | -44.898998 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b18774c6-d503-3f96-b18a-51b626ef3269 | -11.0066 | -49.038502 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0438d2cc-70db-37c1-ad66-0c786350583c | -9.639 | -44.540798 | 2025-11-13 00:14:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79ee3c67-fffe-3a5f-b2d4-8aa4e78adb60 | -3.8499 | -50.0536 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 482823b3-5d07-33e7-9baf-9c9c0d1ccfb6 | -11.7369 | -48.527401 | 2025-11-13 00:14:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53fd2f64-9f8b-361a-8110-1bc8b3c048f2 | -2.7259 | -45.471001 | 2025-11-13 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73a51eb1-ff0a-3754-b415-dab7924f0bcc | -20.4594 | -53.0327 | 2025-11-13 00:14:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 621ae120-fa05-3f17-bc33-5a8f78a7836b | -5.8621 | -47.579498 | 2025-11-13 00:14:00 | METOP-B | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32711f3e-ff12-3cb7-9e0e-d97a36d7702d | -11.7319 | -43.835098 | 2025-11-13 00:14:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85c96824-3153-3b92-a7ff-0114f5e83479 | -4.0053 | -48.969501 | 2025-11-13 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8b6662c-26e2-35c8-8db3-e83c296a043c | -3.4312 | -50.433998 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bfd5b95-2913-3a31-adb2-ead9617dd46d | -3.3538 | -48.373901 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fafd320b-0c1b-354a-ac2d-b9fe96788cf9 | -2.8267 | -52.867001 | 2025-11-13 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfd2eab7-b427-39cd-91a0-4d7c46699b75 | -3.3457 | -48.3834 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e8d47ba-fd2d-3b16-831b-e6ec3d5044c8 | -21.8556 | -45.014801 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3292b632-a6da-30b7-a1d5-5930aad43427 | -2.0058 | -54.430302 | 2025-11-13 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4ac3090-1640-3c64-b525-6d260b68d219 | -4.5748 | -46.027599 | 2025-11-13 00:14:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb98abd4-cf07-3266-a5ea-0a4a0b790061 | -12.5974 | -48.322899 | 2025-11-13 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ff9e130-1a79-3a12-b461-4b19c1f3ad61 | -4.189 | -50.322498 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfe36998-6476-34e5-b6b2-14b62252a540 | -3.8725 | -49.7901 | 2025-11-13 00:14:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76abf9c6-e192-3940-8a76-370f978ae28e | -3.485 | -45.858898 | 2025-11-13 00:14:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af8cc9e6-431e-35ad-96b2-49edc3f65dce | -10.6303 | -45.237202 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 58a6a72c-449a-3224-bee9-eb7a375d8b2b | -20.461901 | -53.0466 | 2025-11-13 00:14:00 | METOP-B | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7528556c-d431-3b0b-ae75-55944886c47f | -3.0353 | -50.2785 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2081db83-63e6-3cea-b633-f6541a388ee2 | -16.4505 | -44.991699 | 2025-11-13 00:14:00 | METOP-B | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c193ad14-a33d-33bc-82a9-1560a7d23b1f | -4.5238 | -46.428699 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 453ba0e0-0850-3628-adbd-f7b1ee912e89 | -10.3548 | -47.699799 | 2025-11-13 00:14:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 963be6ca-ca0f-3d3b-8e67-8e8e063a5b4f | -8.4092 | -44.015202 | 2025-11-13 00:14:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7ab50bcd-554e-310b-8934-1f10eae4f67b | -5.3334 | -44.7799 | 2025-11-13 00:14:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eed8dc59-6673-353a-bc34-b00ba4995a8d | -3.3719 | -48.4081 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6596378c-9ff1-3059-b5b2-e8a309599632 | -5.8604 | -47.571999 | 2025-11-13 00:14:00 | METOP-B | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81fe6c43-a5f4-3d16-a6b3-6ab2f6bbce94 | -10.916 | -44.612598 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 634ea26e-f5ed-33f5-ba14-62487b83108b | -12.4332 | -43.743099 | 2025-11-13 00:14:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31f6f489-449c-3ce9-8353-079d0bfabd2c | -4.7138 | -46.4482 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06d71855-b9c2-37e8-a089-e886e6750a01 | -4.2081 | -50.088402 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d6f242c-4ed7-3e5d-a174-0c7e6d56c675 | -4.3097 | -48.226799 | 2025-11-13 00:14:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4390e5d-b9c8-3c43-b109-778ca01be4bf | -2.1497 | -45.5592 | 2025-11-13 00:14:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b700efe5-5018-3be2-b004-e3472e4f0b4c | -5.3505 | -46.748901 | 2025-11-13 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd18903c-ac88-3c3e-81ed-2c51bcfdc291 | -8.8638 | -50.185398 | 2025-11-13 00:14:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a727321f-4983-304f-a65e-8c7db2d345cf | -4.951 | -47.027 | 2025-11-13 00:14:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae17bb2c-2ba0-39f5-a4f9-24dfe8157cfd | -5.6828 | -46.0056 | 2025-11-13 00:14:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 354a3fca-74d6-3e6c-b0f6-0eb62efc8086 | -5.7263 | -44.829498 | 2025-11-13 00:14:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00f7ebe1-e143-3459-890f-b11551041330 | -10.4452 | -47.327499 | 2025-11-13 00:14:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22dbc915-4d2f-30b4-90f6-6f687ee0e438 | -1.7617 | -54.122002 | 2025-11-13 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6740380-5fee-30bc-b13a-33945011773a | -3.7773 | -46.009102 | 2025-11-13 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 534ead8e-fae0-3935-842b-084ee6cb6d38 | -2.6368 | -52.069599 | 2025-11-13 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9a8be3-df62-30e0-a381-50deecb83e9d | -10.3532 | -47.692699 | 2025-11-13 00:14:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79ff0544-6fc6-38f7-b9d7-db657bc229fb | -3.1124 | -45.761799 | 2025-11-13 00:14:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0cc949-854b-30f5-adc4-1a7e9b809bd2 | -3.4752 | -45.861198 | 2025-11-13 00:14:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cebcf582-14d3-347f-b79a-9a0b19e7b7d5 | -10.7197 | -45.134602 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5642b067-e0bb-3ab6-b962-0fc515ffd380 | -15.39 | -43.054298 | 2025-11-13 00:14:00 | METOP-B | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| ef5fb0e3-7860-324c-b3e2-47044a676a98 | -8.2514 | -44.348 | 2025-11-13 00:14:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 294f47fa-cefc-368d-bdc9-4361bb686e0f | -9.1111 | -50.048199 | 2025-11-13 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126d1bd3-2692-33b9-a83e-c189331d8fab | -10.7826 | -48.131401 | 2025-11-13 00:14:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d256b92-42df-35f7-b458-b60d10a01be6 | -3.0929 | -49.262501 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9cd0e9-7b3a-38cb-a396-204e8f4fa7a5 | -2.6378 | -49.210499 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8243b9b8-c7b4-3610-84c1-8286b8ec1fbb | -6.4922 | -47.003399 | 2025-11-13 00:14:00 | METOP-B | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 157c833d-2d10-3b3d-883b-f2f767539c2c | -4.5356 | -46.435101 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 78a59193-26ed-3748-bec0-0e1164a97d5e | -13.778 | -49.389 | 2025-11-13 00:14:00 | METOP-B | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c4c6ce7-542b-33a9-ac38-de60187d66d3 | -10.8468 | -44.930302 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 476509c2-4f45-3a55-bd16-2c698b2f0aff | -3.0831 | -49.264702 | 2025-11-13 00:14:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 597294b2-3594-3641-b110-402321ac9a50 | -9.3469 | -46.590698 | 2025-11-13 00:14:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12e3dfc1-8cf8-3e0f-85e4-b9923f245cbd | -7.7182 | -47.176201 | 2025-11-13 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 913490e7-65f7-34af-b08b-711e7681bc7a | -3.1649 | -50.6227 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10bfe43f-d973-3bac-aef7-fdc706c062e5 | -11.005 | -49.031502 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a1e1c1a0-86f3-3c12-9707-d30843ba93f4 | -7.2225 | -47.980202 | 2025-11-13 00:14:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 28b707ed-9b4d-3689-b680-fe64297e6336 | -21.853901 | -45.007301 | 2025-11-13 00:14:00 | METOP-B | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea484aea-6535-3506-a584-9006e431cf69 | -3.4003 | -50.161201 | 2025-11-13 00:14:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20538848-6bf6-3965-aaca-2c70f76aaac7 | -5.4355 | -44.645 | 2025-11-13 00:14:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b4aeb57-08d3-330d-9574-c71e013a6e3f | -2.8914 | -48.065201 | 2025-11-13 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9a7b66-1e18-30de-94a5-cc8ca4253eff | -2.7281 | -47.3983 | 2025-11-13 00:14:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95382766-b506-34aa-9b52-dd3eca0b9ecf | -3.6633 | -45.9175 | 2025-11-13 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 732934d8-d5e8-338c-aa79-0dcbcd896eec | -17.3286 | -46.489601 | 2025-11-13 00:14:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 98b74ad6-f8ef-3497-8725-902a7f8e7efc | -8.468 | -47.970901 | 2025-11-13 00:14:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 644ce739-af02-3445-be62-a7386e034e0c | -22.2188 | -46.7365 | 2025-11-13 00:14:00 | METOP-B | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8664999-b5e7-3f73-ba6b-232f57495c7f | -5.6629 | -46.2742 | 2025-11-13 00:14:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fd1bc9a1-62d5-37fc-a152-a8667fc6fc9b | -4.2472 | -49.6702 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac00586-6376-3267-bd53-d1467fadfbbe | -7.2208 | -47.973099 | 2025-11-13 00:14:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c947666-751a-3a1c-9b45-0a4a8a971a6f | -17.0361 | -46.748699 | 2025-11-13 00:14:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9406ba4-a8d0-3ae3-8133-4703c80e3820 | -1.9407 | -52.087799 | 2025-11-13 00:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f90ca800-fcd0-3aa1-bf63-67eeea02546a | -5.3241 | -45.178101 | 2025-11-13 00:14:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
