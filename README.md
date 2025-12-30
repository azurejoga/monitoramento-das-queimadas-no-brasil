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
| 65aedccb-d93c-32b6-ab5d-136e2323594e | -3.3863 | -42.1208 | 2025-12-30 00:00:00 | GOES-19 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 40.4 |
| 7ed75000-5a59-3b63-9b13-22c2b41de971 | -3.5461 | -43.5894 | 2025-12-30 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 00438ad5-3c9e-356d-90dd-dc67a3e4c96f | -4.345 | -44.1247 | 2025-12-30 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| fd315892-21f4-3827-828e-b8ed98da1ef7 | -4.1226 | -46.9 | 2025-12-30 00:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bda948d3-3aee-3b99-a25c-58f656c926bf | -18.832 | -51.6099 | 2025-12-30 00:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 87ca1f5d-0617-34b9-8246-429cd9d312d2 | -3.546 | -43.6126 | 2025-12-30 00:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| a99d0a13-bbb2-32fb-8484-2a8239dc85d2 | -4.3451 | -44.1017 | 2025-12-30 00:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 29029fcd-5d1e-3e7b-b8ed-6a69cd487ae1 | -4.345 | -44.1247 | 2025-12-30 00:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 34f61e90-f6ff-3cc1-ab06-294f62b7ec9c | -19.0985 | -56.0698 | 2025-12-30 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| f75081cc-cb8e-3617-85ab-02a7287d6f2e | -18.832 | -51.6099 | 2025-12-30 00:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 2eef2b6c-0899-3235-b27d-2c5aa0eab12c | -9.498 | -35.7396 | 2025-12-30 00:10:00 | GOES-19 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| 9e3ef6ac-7d27-3dfa-85be-582e45bb5823 | -14.4967 | -52.5526 | 2025-12-30 00:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ae9957e3-f02d-3db6-9e6b-7f126d1a5033 | -15.1281 | -52.9353 | 2025-12-30 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3c6b3bb3-4416-3331-ab31-97df185d868d | -15.1277 | -52.9565 | 2025-12-30 00:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 56e1f19f-7164-353c-aeda-e88b963a5a71 | -9.362 | -35.8172 | 2025-12-30 00:10:00 | GOES-19 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 60.2 |
| 4f5bc4b8-5515-3078-9066-cee22fc2e678 | -3.546 | -43.6126 | 2025-12-30 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 609f6d6b-c883-338c-8238-2e8fe55676bd | -3.5461 | -43.5894 | 2025-12-30 00:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 7f2084e8-4d8b-3b8f-910f-31a8e9cc1643 | -4.1226 | -46.9 | 2025-12-30 00:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 58628741-3450-3f51-a5de-1f1e315fc840 | -9.9477 | -36.3916 | 2025-12-30 00:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 9ced2d00-bfe9-30df-bbbf-bb9355996fb0 | -4.345 | -44.1247 | 2025-12-30 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| f6f6815e-a6a0-3205-80ce-7f13c01153d1 | -4.1226 | -46.9 | 2025-12-30 00:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 98ec1755-0146-30a0-95d1-085c042f2697 | -18.832 | -51.6099 | 2025-12-30 00:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8b528174-3deb-3d48-8401-e2506ae73921 | -4.6079 | -46.5887 | 2025-12-30 00:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0c7fd41a-4baf-3bb4-90eb-b2ea231ae959 | -3.5461 | -43.5894 | 2025-12-30 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| fadc9eb9-fe13-3bef-bbe8-05161df8507e | -3.546 | -43.6126 | 2025-12-30 00:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 876061a9-fa93-3862-8f28-6659b0a7e09d | -4.345 | -44.1247 | 2025-12-30 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 9c3b1945-2a9e-321b-95aa-fbf71ea4388c | -3.5461 | -43.5894 | 2025-12-30 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d38492db-14a2-303f-9c40-0c707bd08bdc | -3.546 | -43.6126 | 2025-12-30 00:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| a4a0d818-3aa9-3574-9180-71fdc62ce5d9 | -18.832 | -51.6099 | 2025-12-30 00:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 12a37606-0ab0-389c-ba2d-0de20e2af99c | -13.4802 | -44.0198 | 2025-12-30 00:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 5c005260-3e3c-37d5-a0f7-ce4c5ad3a53d | -4.1226 | -46.9 | 2025-12-30 00:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| efcc79dc-8fcf-395d-aa59-c656b0fe768a | -4.345 | -44.1247 | 2025-12-30 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f3350a20-3db7-331b-a831-642ca3f476f3 | -4.1226 | -46.9 | 2025-12-30 00:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 182b782b-a1e2-3a43-9668-984ea97bc977 | -18.832 | -51.6099 | 2025-12-30 00:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 0c7563ed-4172-3850-932e-b4ff48f86497 | -3.546 | -43.6126 | 2025-12-30 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 9a6c59df-72cd-3e77-b26e-6ca7b395f043 | -3.5461 | -43.5894 | 2025-12-30 00:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 073710b4-1c30-3ca9-988c-a50c42704de6 | -1.4782 | -54.197498 | 2025-12-30 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2183998d-d08c-3db1-985c-b7240ab33bae | -1.4759 | -54.187698 | 2025-12-30 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d07316b9-b1fd-3b3d-a4e5-2707945f1bd1 | -3.5461 | -43.5894 | 2025-12-30 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 8cfd4269-000b-346a-a768-9f7af7c7f2ce | -4.345 | -44.1247 | 2025-12-30 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 0cf7f748-48dc-306b-a61b-14c28e79fcc0 | -18.832 | -51.6099 | 2025-12-30 00:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 9164ced3-7bf6-3526-8f13-318bb9560fed | -3.546 | -43.6126 | 2025-12-30 00:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 3e0d131b-747c-3c3c-933f-88591d000a33 | -4.345 | -44.1247 | 2025-12-30 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 0a816d7a-047a-340d-a248-7083db51055b | -3.5461 | -43.5894 | 2025-12-30 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 04719eef-fd81-3212-ab22-9d51ea513c11 | -18.832 | -51.6099 | 2025-12-30 01:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| cf682b32-2940-3c2c-8aa0-4bea5a2c48aa | -3.546 | -43.6126 | 2025-12-30 01:00:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| f83d19e8-7277-3218-a1ab-118d8847984f | -18.82088 | -51.59807 | 2025-12-30 01:06:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 73b7c888-574a-3fae-ae75-164feb50af98 | -18.82429 | -51.61747 | 2025-12-30 01:06:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 30b7f162-25bc-3e3c-be6c-1d005bab5db6 | -12.30181 | -57.3581 | 2025-12-30 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 34e2a323-3977-38b5-aacd-ef625d77ed50 | -12.294 | -57.36948 | 2025-12-30 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 26af253c-e21e-3abf-a4e2-10f7dee44fd8 | -12.30325 | -57.36806 | 2025-12-30 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b7c94f31-3534-32d1-a2d4-f7e736146bf1 | -3.5461 | -43.5894 | 2025-12-30 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| b2e8d730-5ed8-31e6-8cd1-dbbaaf1b3a4c | -4.345 | -44.1247 | 2025-12-30 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 8e48c6f0-7959-3304-a2e3-24c293474317 | -18.832 | -51.6099 | 2025-12-30 01:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 4cd1b0ec-eeec-317c-b72b-a70bdb0662bb | -3.546 | -43.6126 | 2025-12-30 01:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 38e73a30-f20b-35f9-88a9-bab526d6d3cb | -18.832 | -51.6099 | 2025-12-30 01:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 7638831d-3017-37c0-98b4-d2ed7c96620c | -4.345 | -44.1247 | 2025-12-30 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 60236631-5773-38d4-b58b-e54eeb703183 | -3.546 | -43.6126 | 2025-12-30 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 98fe9f28-44d6-3067-aadc-d3219f2d9be1 | -15.1281 | -52.932301 | 2025-12-30 01:23:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54219a64-6346-338f-b6fd-89c9ce577e9b | -15.1307 | -52.942699 | 2025-12-30 01:23:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea71ed69-56bf-341a-80a3-f6f028ff5dc4 | -15.121 | -52.945202 | 2025-12-30 01:23:00 | METOP-C | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 495df2c4-c4f9-3e07-9a7b-ccebb987e79e | -18.8218 | -51.610298 | 2025-12-30 01:25:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6305d076-fad1-32cf-b219-6b9e05494bfe | -12.3059 | -57.3615 | 2025-12-30 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41d07b07-35a8-31ec-8829-44de5b7877d1 | -12.2962 | -57.3638 | 2025-12-30 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7132fb8d-73e4-3c90-acfc-b8208c668c2a | -18.8246 | -51.6213 | 2025-12-30 01:25:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 00ce1e09-b697-3c6a-9e28-a6bc861a4897 | -18.819 | -51.599201 | 2025-12-30 01:25:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d2e65c02-1403-38ff-b456-8d1ad2327402 | -4.345 | -44.1247 | 2025-12-30 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0bfcf51a-83a7-39ea-8244-526efec334d4 | -10.2376 | -36.3398 | 2025-12-30 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 6e74b58a-02cd-3405-8e55-9138b58c7721 | -18.832 | -51.6099 | 2025-12-30 01:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 25899b60-5ade-3be2-acf1-e2e0ec1f5486 | -10.2381 | -36.3127 | 2025-12-30 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 163.1 |
| c64eaaea-a132-3bf5-a89b-afd5263966ad | -4.345 | -44.1247 | 2025-12-30 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 20c174a3-9d3c-3f9d-b461-4a01ea4e9805 | -9.9111 | -36.2904 | 2025-12-30 01:40:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| 96b10a96-c8d0-3d3c-8e59-7f7e3db285e5 | -18.8119 | -51.6134 | 2025-12-30 01:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 819c44ad-8cb9-34a6-9bc7-89611621507d | -9.8923 | -36.2668 | 2025-12-30 01:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| 231b7b0f-2331-3a98-b165-c86537976f51 | -18.832 | -51.6099 | 2025-12-30 01:40:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4c5a29b7-e1f7-3d53-879f-4e50f45b4370 | -9.9116 | -36.2634 | 2025-12-30 01:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 115.1 |
| 6e7c2033-a2b5-3dd8-9efe-2d679efc1f72 | -18.832 | -51.6099 | 2025-12-30 01:50:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| f977800f-3752-32a1-acf7-681c2198c849 | -4.6079 | -46.5887 | 2025-12-30 01:50:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3e8a046e-0bad-3e62-98ab-7ea91c5c2c84 | -9.9324 | -36.1788 | 2025-12-30 01:50:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 9e7aa6eb-0c6f-37ab-b7b3-d20181149f91 | -4.345 | -44.1247 | 2025-12-30 01:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 4e6fc64e-c1ba-3656-a46d-b33b1c09a306 | -4.6079 | -46.5887 | 2025-12-30 02:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 25517c93-7664-339c-812c-7c8c3af09986 | -4.345 | -44.1247 | 2025-12-30 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8594cf8f-e7ff-3265-b4b9-989099c6dca2 | -18.832 | -51.6099 | 2025-12-30 02:00:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 52dc8f5a-83ea-37f7-90de-69f543c07969 | -10.1806 | -36.2962 | 2025-12-30 02:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 143.6 |
| c4cb40b3-f029-385c-9b25-629ca8ae9f5c | -9.8695 | -36.4591 | 2025-12-30 02:10:00 | GOES-19 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.7 |
| ff701953-deb7-37b1-8db4-c11403a87df8 | -18.832 | -51.6099 | 2025-12-30 02:10:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3c46dccc-89fa-3c45-b6bd-0ef1e5153698 | -3.017 | -49.4482 | 2025-12-30 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| eb0ed853-610c-39b1-b5ec-896ea673288a | -9.9116 | -36.2634 | 2025-12-30 02:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 156.6 |
| 5ee9ce79-4293-318a-a68e-cebdd909c356 | -4.345 | -44.1247 | 2025-12-30 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3b5b6635-586c-3c87-88d3-7e7d9f1e5afe | -9.8918 | -36.2938 | 2025-12-30 02:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| f8b19c9a-e1f0-3c9d-a14d-b6334851a59f | -9.9111 | -36.2904 | 2025-12-30 02:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| cd52e6b5-48bc-349e-910e-7564d6f88340 | -9.8923 | -36.2668 | 2025-12-30 02:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| 97ee2c92-6b73-33df-b38d-da6fff6f5511 | -18.832 | -51.6099 | 2025-12-30 02:20:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1895fd6a-ec5d-3f51-8bf7-4e3658fa08d4 | -23.8748 | -49.3732 | 2025-12-30 02:20:00 | GOES-19 | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 4310c98b-1060-3c36-a865-eeb80c09da9d | -10.1806 | -36.2962 | 2025-12-30 02:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 160.8 |
| e67ad5b4-a1f9-30f9-aae8-c6bb27de0007 | -3.017 | -49.4482 | 2025-12-30 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8f31f1db-adf3-3215-b864-3e6b72d752e9 | -4.345 | -44.1247 | 2025-12-30 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b237c918-b55d-33ec-944c-a0d1ca4508d5 | -4.6079 | -46.5887 | 2025-12-30 02:20:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b9652d8b-2a74-3ba2-b895-e6e060a7b900 | -10.1999 | -36.2927 | 2025-12-30 02:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 103.1 |
| 7a1257f1-b649-3617-b409-e9cac6a3e96f | -18.832 | -51.6099 | 2025-12-30 02:30:00 | GOES-19 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |


[Clique aqui para ver as próximas entradas](README2.md)
