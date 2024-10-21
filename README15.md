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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ddef4a4-ef06-3cbc-a838-148e209cec58 | -5.6896 | -46.4128 | 2024-10-21 01:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 0388e11a-77f1-3c32-bb1f-265b6d7210af | -5.7081 | -46.4338 | 2024-10-21 01:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 311d3390-d371-3a78-b3e7-5447f0672be6 | -5.7083 | -46.4115 | 2024-10-21 01:25:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| b85722ee-6a2d-354d-8551-7c5ec41be544 | -9.3718 | -66.4891 | 2024-10-21 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0fc0dbdb-e2a6-3822-9c19-1c3b3249af78 | -12.4778 | -63.1885 | 2024-10-21 01:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 360e15fd-9dd1-3ffa-a2db-f284982cb9b5 | -12.5147 | -63.3014 | 2024-10-21 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f3d287e7-b337-3577-98d7-99de3a365ccb | -12.5357 | -63.0319 | 2024-10-21 01:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c74b636c-bc9a-387a-92cc-7708a260b260 | -17.7065 | -57.4569 | 2024-10-21 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| cb059f1c-a5bc-381b-a5a9-b18fc3650f78 | -17.7259 | -57.4751 | 2024-10-21 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| f5dbeaf6-1b73-3c38-9a8c-43a2d2d7bed2 | -17.7262 | -57.4545 | 2024-10-21 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 4edd1c8b-8b0d-3029-a279-6ee7b20a1f29 | -17.7848 | -57.4885 | 2024-10-21 01:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.1 |
| d120f693-dcdc-3d50-980d-53915c9a2015 | -18.263 | -56.1021 | 2024-10-21 01:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.2 |
| c49eab58-0c35-3037-bf4c-79d722bde775 | -18.2828 | -56.0994 | 2024-10-21 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.2 |
| 051ec953-4397-3a63-a651-9d1c0401d168 | -18.2832 | -56.0785 | 2024-10-21 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| 73e15baf-6cd1-31a4-8d42-ad8926f8e698 | -19.523199 | -56.615898 | 2024-10-21 01:30:28 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3566fb65-1a9f-3722-a69d-6b02cabcab27 | -19.524799 | -56.6231 | 2024-10-21 01:30:28 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e910d0af-9098-304a-a63f-0a4ae71c5e4b | -19.513399 | -56.618301 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6ab0c2ed-8e04-3bfc-8116-f1655c8e2655 | -19.514999 | -56.6255 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7882370f-1d43-3441-824f-53a1ea72ea60 | -19.516701 | -56.632702 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 645e8c8e-dfef-37ca-8c01-044128391fca | -19.518299 | -56.639999 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 95fbe8e4-1380-3f83-a303-ca22c631cd5b | -19.519899 | -56.647202 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ecbc2d8e-d4a2-3266-8837-6ba58b2c9bd8 | -19.506901 | -56.635101 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b5d6eb9-b940-3db8-bb07-551455b71ba4 | -19.508499 | -56.642399 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4f58e420-41bc-371e-9fac-19be9350bce7 | -19.510099 | -56.649601 | 2024-10-21 01:30:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0f17330d-051f-380e-8e89-8b124099efff | -18.2484 | -56.0853 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d68531c9-25c1-39f4-b408-b677dcbcdb80 | -18.250099 | -56.092602 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a6d8df6-f1f8-3db6-b19b-389b326d9f0c | -18.251699 | -56.099998 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bce7d9b3-045f-3df2-9d6d-1f0c5d87f99a | -18.263399 | -56.1511 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c5748fe-33d3-366b-bfa4-73b3f41313a5 | -18.2651 | -56.158501 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 13bf83fc-218e-302f-89ee-185f085318a6 | -18.266701 | -56.165798 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 82317d87-8007-3eb0-8216-7a5c4ac7fb42 | -18.2684 | -56.1731 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c4558043-0c85-3939-af62-65cc618b68aa | -18.2701 | -56.180401 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f870bb05-6530-3499-94d9-cba5beafd65f | -18.2369 | -56.080399 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d5b7be5a-2289-3697-8a6f-877612867033 | -18.2386 | -56.0877 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d8560309-00a4-3b61-9f6f-17cf0a5b738e | -18.240299 | -56.095001 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca1cc869-629e-3310-9789-d51605d9f5c4 | -18.242001 | -56.102402 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a40b0daf-747d-3ae9-ab43-2d0ec670d6b2 | -18.243601 | -56.109699 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d71a15dd-c553-3b2f-b251-67b7c6643b1e | -18.255301 | -56.1609 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8d330b06-aac7-3c2c-900d-5976214d7d3c | -18.253599 | -56.1535 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d0319d96-8f63-3502-9b95-a171f371ee66 | -18.2603 | -56.1828 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5ea32580-37c1-3a5d-ad81-90a3bdd3c859 | -18.2586 | -56.175499 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2b7035aa-527e-3c1e-b723-6c5714e09357 | -18.256901 | -56.168201 | 2024-10-21 01:30:47 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a82d0ca-0c4a-3eb7-a1ef-4ecde724e416 | -18.0144 | -57.337101 | 2024-10-21 01:30:55 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a3bc227f-430d-3ab7-8021-02e5e8f0f26a | -17.9869 | -57.305801 | 2024-10-21 01:30:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fad1bcc9-e51b-38dd-9c79-ada9257d23ef | -17.9853 | -57.298698 | 2024-10-21 01:30:56 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 879e23e2-3da2-3654-8dfa-12c99899f240 | -17.9634 | -57.4324 | 2024-10-21 01:30:57 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ed458fcb-d4e7-3e4a-a337-d0fcde3fdf95 | -17.899799 | -57.4702 | 2024-10-21 01:30:58 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cb5f959-4c2a-3f21-86ef-d702f759fdf8 | -17.898199 | -57.463001 | 2024-10-21 01:30:58 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8e4f09e2-2f92-3384-925c-9167e981f1bf | -17.9095 | -57.467899 | 2024-10-21 01:30:58 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| aa67e7a0-6bb5-3cc1-be86-b42dc615f89d | -17.7384 | -57.485901 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 772a87ba-eb45-3db9-85eb-8c92e1a5119a | -17.736799 | -57.478699 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 382f0f08-4dc9-312c-9dc5-7984eead0f63 | -17.7498 | -57.490799 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01637fcf-a650-3060-accd-7e81f9d69129 | -17.748199 | -57.483601 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2e10233-304c-322a-b5b0-b2fa29696b25 | -17.7596 | -57.4884 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 91ae5a4f-5b33-3177-b6da-8e92a3c60258 | -17.757999 | -57.4813 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c764113-4083-3ac6-8f7c-4f4a454e1622 | -17.756399 | -57.474098 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aec00489-32c6-3591-b365-0d2fb5e60d93 | -17.7694 | -57.486099 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bc71721-2a17-3ecf-9894-d204c74b2bfe | -17.767799 | -57.479 | 2024-10-21 01:31:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a11a8798-77a1-3609-a9c9-3fb99172f5bf | -17.6654 | -57.435398 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7be9a5b8-0777-30e2-b4b8-2b9457268ec8 | -17.663799 | -57.4282 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0225451f-bc0c-3996-8aec-4ef805b864c5 | -17.6847 | -57.476101 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00f0b9dd-d7f4-3b2f-999e-aa95454eef1b | -17.6831 | -57.468899 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f629108-5946-3d54-9d67-979a1853c993 | -17.681601 | -57.4617 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e59fa4c-f128-3237-be04-80ac0ec484ae | -17.68 | -57.454601 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 247f0f54-c4a7-3129-963b-3d5ebd170980 | -17.6784 | -57.447399 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d65cfc9-cb25-3ac2-b07e-0e50dd2c5375 | -17.672001 | -57.418701 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 791b5b7c-9c76-365f-b874-7f0234e11d3b | -17.670401 | -57.411598 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de08e10c-2cd2-3d40-9a25-e16cf7b0a394 | -17.6961 | -57.4809 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 530e6dce-48ca-3972-befb-16eb25e4dbe7 | -17.6945 | -57.473701 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e361c0b-dff8-387d-b2e3-7ca686099f58 | -17.6929 | -57.466499 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 763bd3d2-d5a2-3ac1-996b-1021c9e52352 | -17.691401 | -57.4594 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d29a187-52c9-3285-856a-601240f6360f | -17.6898 | -57.452202 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74165fe2-f343-335c-9515-75549f22afd6 | -17.7043 | -57.471401 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6c553911-21f3-34d9-8787-eedd6e949250 | -17.736401 | -57.5695 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be21c3ee-eb49-3e05-8799-c4732b3009ee | -17.7348 | -57.562302 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7693bf19-f5f0-3fb3-9409-9573da85cc7e | -17.7332 | -57.555199 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c2be804-95ed-33ad-926f-cbb06e3f8427 | -17.7446 | -57.560001 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aa4d6ca9-d13a-357c-921e-e99e955416cc | -17.7271 | -57.481098 | 2024-10-21 01:31:01 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3bab2b92-72f2-3508-8679-efd38869264c | -17.655701 | -57.437698 | 2024-10-21 01:31:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6600738-d4fe-3c83-b74b-8db2f109900b | -17.6541 | -57.4305 | 2024-10-21 01:31:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa1a7c63-fc0a-30ff-a477-b735e3519d01 | -17.6525 | -57.423401 | 2024-10-21 01:31:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e69f8b8-29a7-35b7-8748-8e86a52936bb | -17.6509 | -57.416199 | 2024-10-21 01:31:02 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a0f5e61-9696-37e9-9f1b-343697b2fca4 | -17.2166 | -57.316399 | 2024-10-21 01:31:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3fb49a22-35b0-3147-901d-b8e62dabbc27 | -17.215 | -57.309299 | 2024-10-21 01:31:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c717a8a4-4a5b-3714-82f7-1165d3bcc5ec | -17.2134 | -57.302101 | 2024-10-21 01:31:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c416534-1637-3727-9dfe-01ce06606c3e | -17.2248 | -57.3069 | 2024-10-21 01:31:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 496aec53-37a0-30d7-a7ca-bb02d9568727 | -17.2232 | -57.299801 | 2024-10-21 01:31:08 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc693048-91a7-3ed0-a7d9-67f80517a02b | -16.9744 | -57.5243 | 2024-10-21 01:31:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02751778-3295-39d1-a775-f68e0d90b734 | -16.972799 | -57.517101 | 2024-10-21 01:31:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f592d97-b3bc-34b7-99f7-4709650d8492 | -16.2633 | -59.1581 | 2024-10-21 01:31:30 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c19ca582-1426-3496-bd13-f46ac289714f | -16.2617 | -59.1507 | 2024-10-21 01:31:30 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d425ed88-e5aa-3400-89d7-9fbc73eb785e | -16.2731 | -59.155899 | 2024-10-21 01:31:30 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 972050cf-24c3-358e-821a-49908f4aea00 | -16.2715 | -59.148499 | 2024-10-21 01:31:30 | METOP-C | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8b585667-ab85-3cee-980c-0a03d7977a08 | -11.8318 | -56.870998 | 2024-10-21 01:32:17 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e7d942c-137b-31f2-b630-884684ac1e8d | -11.8336 | -56.878399 | 2024-10-21 01:32:17 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81664c35-07ca-3f4d-9c24-ccd33c1f848c | -11.8353 | -56.885799 | 2024-10-21 01:32:17 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01757191-fbff-3eb5-90f1-41cc2f827119 | -12.4915 | -63.306499 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7591f11f-2ff0-3fc5-bd1d-5d347346e45b | -12.4893 | -63.2962 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d554faf-a66f-3f5c-9ad9-92feacf646e2 | -12.4658 | -63.183601 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cafe4c85-797d-3f94-8b11-c9fcc7701eba | -12.5068 | -63.2817 | 2024-10-21 01:32:29 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
