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
| 2f00c358-cdd6-3cdd-81be-926489726fcb | -6.7367 | -59.6698 | 2024-10-11 01:40:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ddb4fce-b307-3291-a77b-bab08da41c96 | -6.677 | -59.457802 | 2024-10-11 01:40:45 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84454121-1eff-3964-ab0f-e0ace8552940 | -6.3543 | -58.1702 | 2024-10-11 01:40:45 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27c4e8d8-3284-3960-bc9c-0f76ef413262 | -6.6574 | -59.772701 | 2024-10-11 01:40:47 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8e58e26-9fc1-3394-a8ec-dd87e9a3a9bc | -6.6591 | -59.779999 | 2024-10-11 01:40:47 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 732244af-ca1f-3514-b318-d98de29ce7a8 | -6.6065 | -59.997799 | 2024-10-11 01:40:48 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6dd19200-d25c-3a8c-8869-c215568f5432 | -6.6082 | -60.005001 | 2024-10-11 01:40:48 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 986c3c94-b8b2-36b9-92c5-1346af7d3a13 | -6.5413 | -59.761101 | 2024-10-11 01:40:48 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ae12b23-fabf-3d4e-8d43-bc2f20dabb3c | -6.5429 | -59.768398 | 2024-10-11 01:40:48 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b69c5482-6cc0-38d1-9814-608166e111c7 | -6.5609 | -60.023399 | 2024-10-11 01:40:49 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c374874-936c-3b87-a79c-5e889ecf7090 | -6.5478 | -60.0112 | 2024-10-11 01:40:49 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dbe33cff-99ab-3309-a9f9-6acbc8150537 | -6.5495 | -60.018398 | 2024-10-11 01:40:49 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8369bca1-da5d-3635-baf2-a45f27cc054e | -6.5511 | -60.0256 | 2024-10-11 01:40:49 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57323287-dbfb-32b9-b95f-6195d925eb15 | -6.5528 | -60.032799 | 2024-10-11 01:40:49 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57da16ee-9845-3ec4-86e4-fa79beade05b | -6.5267 | -60.053902 | 2024-10-11 01:40:50 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a87b8a6b-0dab-3ad0-81e3-5ca96674bce8 | -6.5169 | -60.056099 | 2024-10-11 01:40:50 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7724da41-6b4c-39a9-9444-afd0e7c2cba9 | -7.3125 | -64.6577 | 2024-10-11 01:40:54 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f18881e-da3f-3ca0-b334-354d7a171287 | -7.3027 | -64.659897 | 2024-10-11 01:40:54 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86ce4428-7528-340b-9c32-1144d59eee03 | -7.3046 | -64.668297 | 2024-10-11 01:40:54 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beac733d-30c1-381b-ab12-83a63cf29eb9 | -7.3064 | -64.676804 | 2024-10-11 01:40:54 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2451f78e-b84a-3f6b-a240-84f54ef5be08 | -7.2929 | -64.662003 | 2024-10-11 01:40:54 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 794d051c-ab85-3f70-8c2f-3087db817465 | -7.2948 | -64.670403 | 2024-10-11 01:40:54 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b455bdd9-77a8-3b40-aa65-e9c5694ce57e | -5.1852 | -55.988602 | 2024-10-11 01:40:56 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02c5fd28-0f70-3c3a-8758-6d7640818d36 | -5.1881 | -56.000401 | 2024-10-11 01:40:56 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c58f59e4-1509-3760-9b77-c7c8cb5fb8ac | -5.5726 | -60.165798 | 2024-10-11 01:41:06 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef8044fc-f7d9-3924-be35-67d792ceb068 | -5.5742 | -60.173 | 2024-10-11 01:41:06 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea8dbed-37c8-3ce7-9646-b70b1bee4aeb | -3.1612 | -50.418301 | 2024-10-11 01:41:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10e0d594-4525-3b00-aa21-e3bd57acd483 | -3.1688 | -50.4492 | 2024-10-11 01:41:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa9b4630-5921-3845-9b92-339983ac80d0 | -3.1516 | -50.420601 | 2024-10-11 01:41:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71c25011-bcd6-3065-b062-d3f3c27c60b4 | -3.1592 | -50.4515 | 2024-10-11 01:41:07 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d63ef2-8151-37f1-bcee-5cf5eb60cac7 | -5.3335 | -60.1138 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0887781d-a2a5-38e3-b730-53674222c517 | -5.3352 | -60.121101 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6728fa6-c1f0-3510-bd2b-a32f268da677 | -5.3369 | -60.1283 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f160fae-6c02-3cf8-a912-7d89a97d982f | -5.3386 | -60.135601 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 478ac982-27f5-3ad8-99db-3e74cc6fa09f | -5.3254 | -60.123402 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 163b8543-d404-3e5b-9fe7-c5dc69fffc60 | -5.3271 | -60.1306 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3df13bd8-c012-3d4f-81ed-cbc66d7a7d83 | -5.3288 | -60.137798 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5851401a-3a29-3a57-b1e9-af40c295765d | -5.3304 | -60.1451 | 2024-10-11 01:41:09 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 905f6d08-e1bc-31b1-9bf5-837dc935be0a | -5.1992 | -60.068001 | 2024-10-11 01:41:11 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc453ecb-b10e-3869-82b0-a15fc829bb31 | -5.2008 | -60.075199 | 2024-10-11 01:41:11 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 916b0f6f-4fde-32fa-84c1-ab2f6fd2e2b7 | -2.8075 | -51.0075 | 2024-10-11 01:41:15 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec3493af-6e1b-320e-ac3f-438edae106c2 | -2.9867 | -52.8764 | 2024-10-11 01:41:19 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5383a9ab-3901-311a-b415-2d869045ad8f | -2.9918 | -52.8974 | 2024-10-11 01:41:19 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da6fecc3-18c0-3417-a5d2-3954bbe7ee39 | -2.9968 | -52.918301 | 2024-10-11 01:41:19 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bef35b3c-c61e-3210-9c2c-f23971982d10 | -2.977 | -52.8787 | 2024-10-11 01:41:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34eb9252-c2ca-3794-971f-c680a7051df0 | -2.9821 | -52.8997 | 2024-10-11 01:41:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc5b5bb-c479-3bc4-a350-6361c28b8751 | -2.9872 | -52.920601 | 2024-10-11 01:41:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d3e0a3f-1c82-3f0c-80c3-d6353aab5414 | -2.9674 | -52.881001 | 2024-10-11 01:41:20 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63cb8aa8-3702-3807-9651-57d3d4c7598b | -2.9725 | -52.902 | 2024-10-11 01:41:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988a42ba-eae3-3a68-9f38-510da6cf26ae | -2.9775 | -52.922901 | 2024-10-11 01:41:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aedbff3-d669-31a1-b1b0-21d0c7ebbbbe | -2.9577 | -52.883301 | 2024-10-11 01:41:20 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da4eec98-6c38-354f-a2c8-49313b5b59ae | -2.9628 | -52.904301 | 2024-10-11 01:41:20 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd5c0c2a-9845-3d59-8b32-be79ca4a3e43 | -3.2569 | -54.166698 | 2024-10-11 01:41:20 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d49091af-30e2-39b6-8646-280d6cd3e5c0 | -3.261 | -54.183701 | 2024-10-11 01:41:20 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a838f7e-636d-3638-9143-35a19f988eb4 | -2.7996 | -52.483299 | 2024-10-11 01:41:21 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 697cdad3-4f54-330c-ac48-6d682a2ae3d1 | -2.7845 | -52.463001 | 2024-10-11 01:41:21 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3e26e17-7f17-3ab4-9f5e-53a18c9898c3 | -2.7899 | -52.4856 | 2024-10-11 01:41:21 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ae76ff1-0bf9-33f4-a6c8-384adc9ee061 | -2.7954 | -52.508099 | 2024-10-11 01:41:21 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8041c5ba-705a-3ac8-abad-db62c26141b8 | -2.7749 | -52.465302 | 2024-10-11 01:41:21 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2cb6374-2e72-3811-be84-4d9926370f10 | -2.7803 | -52.4879 | 2024-10-11 01:41:21 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6824ebc1-9f59-3307-98e0-a17ef466c43c | -4.7124 | -60.817299 | 2024-10-11 01:41:22 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a519335-2acd-363b-bc15-d82aaa62c2b2 | -4.346 | -59.7705 | 2024-10-11 01:41:24 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16a7e5c6-360e-35d0-944a-8de47e445e2b | -4.2887 | -60.012199 | 2024-10-11 01:41:26 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 702fabd4-40d2-31ac-b95d-8efd0cb36462 | -4.231 | -59.852299 | 2024-10-11 01:41:26 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b26d985e-92ca-38ff-9512-0f1c22df36f0 | -4.2327 | -59.859798 | 2024-10-11 01:41:26 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9e5197d-808c-3dc1-a164-adf25709c459 | -4.2622 | -59.9869 | 2024-10-11 01:41:26 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29445bc2-99a0-3b02-a41c-6da145b1e3b6 | -4.2639 | -59.9944 | 2024-10-11 01:41:26 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd0cfaef-6cd7-3735-92cb-e19f8e1c1f8c | -2.6786 | -53.337502 | 2024-10-11 01:41:26 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13911b41-d466-3445-9c57-f7452021995c | -4.2524 | -59.989101 | 2024-10-11 01:41:26 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1dcec6a7-6889-3c6f-bff8-3dbca4e176f3 | -4.2541 | -59.996601 | 2024-10-11 01:41:26 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a120bb91-b160-3045-90e7-75abe9880ad8 | -2.6642 | -53.32 | 2024-10-11 01:41:26 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f392edd7-00d8-31fe-a589-b0f88ee5bcce | -2.6689 | -53.339802 | 2024-10-11 01:41:26 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0534443b-21cd-3f3a-8a35-28cfcbb51619 | -2.6737 | -53.3596 | 2024-10-11 01:41:26 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26eab0bf-812f-3f03-8609-0560af2d9483 | -2.6546 | -53.3223 | 2024-10-11 01:41:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a47077f2-4c6b-3268-9755-8eda826379b1 | -2.6593 | -53.342098 | 2024-10-11 01:41:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b893713-736f-34e9-a11d-e4ab58b8ae90 | -2.6641 | -53.3619 | 2024-10-11 01:41:27 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4447e2d-962f-3e23-bb7d-99abde0ea144 | -4.1913 | -59.9482 | 2024-10-11 01:41:27 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85080e2d-77a2-3583-8de1-13660703d14e | -3.4779 | -59.496899 | 2024-10-11 01:41:37 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 339b18d2-71ce-39ad-af62-734de95e46a7 | -3.4798 | -59.504799 | 2024-10-11 01:41:37 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 10385c34-09ca-3b5c-9cc4-1bf551760a6d | -2.1068 | -54.630299 | 2024-10-11 01:41:41 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d752b102-dd42-30f2-86e3-178482e67842 | -1.5949 | -53.336498 | 2024-10-11 01:41:44 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead2c9ed-bd04-3a21-b77c-d1621ca75be5 | -1.1691 | -53.392101 | 2024-10-11 01:41:51 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0bc894db-9a12-31c9-b600-4f5dc797ddec | -3.0417 | -61.668098 | 2024-10-11 01:41:52 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d835d688-661b-37c4-b2fb-d49aab47c41f | -3.0433 | -61.674999 | 2024-10-11 01:41:52 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6246d18a-1f97-36ff-b13b-68a52ce200a6 | -3.0449 | -61.6819 | 2024-10-11 01:41:52 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f124aeab-7b86-3f7b-8251-ca918510748e | -1.4865 | -61.587502 | 2024-10-11 01:42:17 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e64e7740-2e1c-392d-9178-36400ced1e78 | -1.4881 | -61.594501 | 2024-10-11 01:42:17 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 343069ad-348b-34df-8883-9746158a470b | -1.4897 | -61.601398 | 2024-10-11 01:42:17 | METOP-C | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eaaccdbd-89e7-3c7a-864a-f9e276b42925 | -2.6533 | -53.3506 | 2024-10-11 01:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 354a687f-dea8-394d-99eb-fcf715608052 | -2.6716 | -53.3502 | 2024-10-11 01:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| a443046b-94d9-354e-9253-69608482479b | -2.7847 | -52.4933 | 2024-10-11 01:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| e84b0f21-4deb-3ca5-b583-25d33b8d787c | -2.7848 | -52.4728 | 2024-10-11 01:45:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 12ec10e5-91af-38cc-817c-b2d90a4941c9 | -2.8081 | -51.0084 | 2024-10-11 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| bb4f92b7-ea42-38cd-bcf0-31c26bd7c1cd | -2.9673 | -52.9169 | 2024-10-11 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| e4398d6e-d5d1-38c1-ba5f-b029253c4984 | -2.9673 | -52.8966 | 2024-10-11 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 99a8fdf3-4900-361d-ae29-f7eb8ef89a77 | -2.9857 | -52.9164 | 2024-10-11 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| c1b9b009-072f-3e8e-b76f-1dbd018742f7 | -2.9857 | -52.8961 | 2024-10-11 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 86bde4a4-d9d2-38e6-ba9c-542650827763 | -3.0525 | -61.6727 | 2024-10-11 01:45:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| fbe9c81f-ba3f-3d8c-9bf3-559faa0fcaee | -3.1422 | -50.4562 | 2024-10-11 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 956615e1-8caa-37d2-8b32-8b6c9b8a84fc | -3.1423 | -50.4352 | 2024-10-11 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |


[Clique aqui para ver as próximas entradas](README26.md)
