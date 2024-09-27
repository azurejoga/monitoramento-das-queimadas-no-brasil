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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1191cd4-d80d-391d-8aa2-a8f6c6ac0788 | -7.9175 | -61.2718 | 2024-09-27 02:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 69116cbb-fe80-39c7-9be4-dd071cf184dc | -7.9359 | -61.2901 | 2024-09-27 02:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 4cd8a275-27cc-3401-a4b0-9d346d17a5a1 | -7.936 | -61.271 | 2024-09-27 02:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 17170110-65df-3751-a3a4-0cd111607ea3 | -8.1394 | -61.2817 | 2024-09-27 02:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 79657612-9a9a-34e0-9764-d2473cf15171 | -8.1579 | -61.2809 | 2024-09-27 02:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 216dfc05-6e14-3e6a-8531-f7c6f27c37a0 | -8.556 | -49.6112 | 2024-09-27 02:45:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 73df36c4-29a1-3ac8-80af-1fb59e1afdf1 | -8.6101 | -63.1226 | 2024-09-27 02:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| c1be8ee0-d4e5-3478-807f-cb54333c5149 | -8.6285 | -63.1408 | 2024-09-27 02:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a01284b0-9721-39a1-8ab3-4ee56d282c59 | -8.6286 | -63.1219 | 2024-09-27 02:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7054bbad-3c0c-3f42-96b7-d2869cf908a8 | -8.8116 | -67.6917 | 2024-09-27 02:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 9a8382dc-a976-32ed-a489-5e5b73dc8805 | -8.8117 | -67.6732 | 2024-09-27 02:45:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 7821eb87-be01-348f-a0e0-18fcb65032de | -8.985 | -62.4068 | 2024-09-27 02:45:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 64eada50-a921-32a7-b89c-66165c302fa5 | -8.9977 | -67.3909 | 2024-09-27 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f548aea7-9677-3d2b-a45f-4560ef06699f | -8.9978 | -67.3724 | 2024-09-27 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 272.1 |
| 8492ec39-787b-3341-b53c-c7f85dfb20eb | -8.9978 | -67.3538 | 2024-09-27 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 175.7 |
| 6e0d6e84-54eb-3052-9c9b-4aa5641c323c | -9.0163 | -67.3719 | 2024-09-27 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 44bb977d-74be-3cc9-99c5-94da1d749225 | -9.0163 | -67.3534 | 2024-09-27 02:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3c2be72f-93fc-3dad-b027-e794555db71f | -9.0656 | -61.3934 | 2024-09-27 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 4b1452d6-a925-3390-8679-2524541c2689 | -9.0657 | -61.3743 | 2024-09-27 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 228913fd-fb4c-38ce-9678-166332a79365 | -9.086 | -61.1245 | 2024-09-27 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 3cd2a649-3ac6-38cc-a8f3-b753361eded1 | -9.1029 | -61.3726 | 2024-09-27 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 07e6cfbd-6475-31cb-9cda-70688e329ace | -9.103 | -61.3534 | 2024-09-27 02:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| d01291b0-dbb4-300b-a870-e62256a24682 | -9.1215 | -61.3717 | 2024-09-27 02:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| fcbc6d72-3338-3500-8bac-1679fa3bf7a4 | -9.1216 | -61.3526 | 2024-09-27 02:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c6a4c50a-6f1c-31ff-9bb4-2c1f789d5a7b | -10.1501 | -49.9956 | 2024-09-27 02:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 1d662902-9555-3f7a-bdaa-d8d5f35175ed | -10.3672 | -53.7858 | 2024-09-27 02:46:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| a0cb9f49-81ba-36c8-bc93-4b880331a711 | -10.6449 | -45.8862 | 2024-09-27 02:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 5b952226-a464-3152-bc6e-bea7942b017f | -10.6452 | -45.8635 | 2024-09-27 02:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| dc8c4413-4bca-397d-b7d1-fe37c251f240 | -10.6639 | -45.8838 | 2024-09-27 02:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 32ea680b-ced4-315b-ab10-1b812470a82f | -10.6643 | -45.861 | 2024-09-27 02:46:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6f86802c-d828-3f97-9908-28e554942e81 | -10.6846 | -50.9847 | 2024-09-27 02:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ed3c20a4-0079-3e8a-8b15-724a65ec70ef | -10.7211 | -51.0869 | 2024-09-27 02:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 320252d4-5337-303e-94c9-2629779e5306 | -10.9264 | -54.2692 | 2024-09-27 02:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.6 |
| 76b500ef-107e-3a4b-8e9b-d8b90263a343 | -10.9267 | -54.2488 | 2024-09-27 02:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 186.7 |
| 620048e4-4a01-3434-9a15-6a0219ffb0a1 | -10.9453 | -54.2676 | 2024-09-27 02:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 5ced82e7-b444-3438-8584-f29fb623ea0e | -10.9456 | -54.2471 | 2024-09-27 02:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 77449f1e-69d5-34cf-9abb-4dfbd535fe57 | -11.2343 | -47.1166 | 2024-09-27 02:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9ee26f47-7e67-3dfe-a28d-3377f57d0cf5 | -11.2531 | -47.1366 | 2024-09-27 02:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2cd03c4b-7ae1-3680-a554-b6b038962d8e | -11.2534 | -47.1142 | 2024-09-27 02:46:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 193.8 |
| a35fe5b7-61fb-3c7d-b87e-b12c65f50cf8 | -11.2034 | -54.7752 | 2024-09-27 02:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 616eeee0-97a2-3678-ab7a-0943e55c70aa | -11.2223 | -54.7735 | 2024-09-27 02:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 97412332-c9fc-3384-920e-6230fe6d7aa9 | -11.5872 | -63.9596 | 2024-09-27 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 0c51371c-a683-397b-815d-1918aae403a9 | -11.5871 | -63.9786 | 2024-09-27 02:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6ca1c243-4d23-39cc-84d5-c083696fb7e2 | -12.1668 | -50.8218 | 2024-09-27 02:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 188.9 |
| bc6debb6-d6d1-3823-8ac7-39e38c161630 | -12.1672 | -50.8004 | 2024-09-27 02:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 6f03cbdc-19ca-3b08-bed5-97a66f7ba68b | -12.1859 | -50.8195 | 2024-09-27 02:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5ad409bf-c955-3525-9bea-3052040ee782 | -12.1863 | -50.7981 | 2024-09-27 02:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 82e4a4fb-b722-3f86-9067-0e47900488af | -12.6826 | -54.6763 | 2024-09-27 02:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1f4a6235-97c5-3e78-8f2b-195750c24cd9 | -12.844 | -54.0215 | 2024-09-27 02:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7bdd07a5-a2ac-3bca-b79b-387790ee9a04 | -12.8628 | -54.0402 | 2024-09-27 02:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 7126840c-8040-3866-9b4f-df31299908c9 | -12.8631 | -54.0195 | 2024-09-27 02:46:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 95c97a8f-166e-3d74-9426-14868576e80f | -14.922 | -51.4507 | 2024-09-27 02:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| f2861a60-89be-369b-bc8c-5a7fdc59cc11 | -16.7325 | -55.8445 | 2024-09-27 02:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.0 |
| 272da7df-f83d-3e3d-bef0-2fb2dfa13e8b | -16.893 | -58.0417 | 2024-09-27 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 220283f2-debb-3607-ac29-7c94354e90ef | -19.3977 | -42.5753 | 2024-09-27 02:46:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 609d3fca-0f35-35c4-b494-50f88f173345 | -19.6136 | -42.8159 | 2024-09-27 02:46:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| abc54ec0-7873-333a-8799-27e2d860d0de | -20.1614 | -43.5356 | 2024-09-27 02:46:57 | GOES-16 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.6 |
| 66c65a4a-6634-3c37-a7b9-a9edfe52572f | -20.1622 | -43.5106 | 2024-09-27 02:46:57 | GOES-16 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.7 |
| aa83b460-9cbb-3b58-b247-4aee90787272 | -20.182 | -43.5299 | 2024-09-27 02:46:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| 7ca185f8-ad23-315f-a02b-a09e3a991e9f | -20.1828 | -43.5049 | 2024-09-27 02:46:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 299.0 |
| bebea34a-5817-30d2-afde-6f9fe31579a1 | -21.0865 | -48.8381 | 2024-09-27 02:47:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.6 |
| cbf510c5-d93a-3eb8-98dd-f32f71016cfc | -21.0871 | -48.8149 | 2024-09-27 02:47:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| d617096d-127e-328a-98ac-539764d6961b | -22.7433 | -44.8035 | 2024-09-27 02:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| d5dd735b-ba6d-33af-9010-1ce4161434a4 | -22.7442 | -44.7785 | 2024-09-27 02:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| 581c7e45-938e-308f-86c4-2df08c7c71ae | -22.7645 | -44.7973 | 2024-09-27 02:47:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| 197b8bf2-a412-303c-89e6-a00c4f063086 | -2.358 | -47.5989 | 2024-09-27 02:55:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| f952a0b5-d8ce-33ef-bd0b-55e4a76d960c | -2.3579 | -47.6206 | 2024-09-27 02:55:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e84e56c8-9f56-32bc-89be-9ccf198a9cc9 | -3.0292 | -51.0647 | 2024-09-27 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f2cf5b7a-e633-3d13-9e5e-b172be3f2e95 | -3.0107 | -51.0652 | 2024-09-27 02:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 7b80da66-f723-3bb0-b840-b76cb67e0c6c | -2.9339 | -57.8562 | 2024-09-27 02:55:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 66496742-a03a-39af-90db-ead39797459d | -2.8795 | -51.6695 | 2024-09-27 02:55:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6036f162-1e47-3afd-b6e1-b361523df391 | -3.2136 | -46.7843 | 2024-09-27 02:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| cd705eb2-6ad5-32fa-b5fb-2e83646ed08d | -3.2135 | -46.8063 | 2024-09-27 02:55:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4580f593-cd6c-3c7d-9767-1fb821d11412 | -5.397 | -43.4332 | 2024-09-27 02:55:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| f6ede8b5-6e9c-3d74-8927-10934c3c29da | -6.2714 | -62.4665 | 2024-09-27 02:55:42 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ad9fb165-4261-377b-bb2e-af74059ddaed | -6.253 | -62.4671 | 2024-09-27 02:55:42 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 08f5d5f8-5903-35fb-bebc-f0e6ffa2b10d | -7.327 | -61.1808 | 2024-09-27 02:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5cd00d45-df87-39df-9b3a-cd6970b1beaa | -7.309 | -61.0862 | 2024-09-27 02:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 507ce0d3-d080-3e1a-b938-72147d18454d | -7.2906 | -61.0869 | 2024-09-27 02:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8c4f89cb-a86f-384f-8305-7f4b1ed3a6d5 | -7.2905 | -61.106 | 2024-09-27 02:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f8bc3f01-c544-3b81-a259-d83b64b0dc76 | -7.4791 | -63.9891 | 2024-09-27 02:55:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d7771121-6f3b-35ba-a7f3-fc5181488114 | -7.8156 | -54.7252 | 2024-09-27 02:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b7c6eb3c-b907-3118-92e0-d8ca3b5d7581 | -7.9175 | -61.2718 | 2024-09-27 02:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8f5001d1-27b7-3826-8601-40ecdbefe140 | -7.9174 | -61.2909 | 2024-09-27 02:55:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| bec2ab74-ac30-32cc-a0a4-ae0de55545ad | -8.1579 | -61.2809 | 2024-09-27 02:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 39833dab-b054-3435-a940-b4d3f3f27591 | -8.1394 | -61.2817 | 2024-09-27 02:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 061a9051-946c-322a-942c-c6fc2b3e21a2 | -8.556 | -49.6112 | 2024-09-27 02:55:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f13e14ae-d511-38bd-b861-308df52d2f2f | -8.6658 | -63.1016 | 2024-09-27 02:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| bca3beb5-00ca-3f07-a323-bc09992c8d5b | -8.8117 | -67.6732 | 2024-09-27 02:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 0af837fa-f2f9-3d97-a3ec-d3c3caa49af1 | -8.8116 | -67.6917 | 2024-09-27 02:55:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7b2ab46e-447c-3889-8b95-0ff0f63343e6 | -9.0163 | -67.3534 | 2024-09-27 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 808806b0-5353-3f29-b750-78cfc360725d | -9.0163 | -67.3719 | 2024-09-27 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| d93e7d99-cfc4-3b64-9c86-c60bc4403912 | -8.9978 | -67.3538 | 2024-09-27 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 180.4 |
| 828d696b-2444-3e3b-abf5-a9464c46ea73 | -8.9978 | -67.3724 | 2024-09-27 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 279.1 |
| 368a3954-cd40-330d-b5ff-112c1cc4d3f7 | -8.9977 | -67.3909 | 2024-09-27 02:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 478c3018-1eba-3bad-b3f0-c3c49b3855f2 | -9.1215 | -61.3717 | 2024-09-27 02:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1c2fc66b-918d-3dbb-b602-937f43a70fce | -9.3214 | -65.3522 | 2024-09-27 02:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 76a643ed-e6f8-376e-98c8-561eed1d7b93 | -9.3029 | -65.3341 | 2024-09-27 02:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| f8273099-f1fc-3e83-9624-22f777dd2b9f | -9.3028 | -65.3528 | 2024-09-27 02:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 55922d2a-bf11-3c98-a7b2-fad4ccd9430f | -10.3672 | -53.7858 | 2024-09-27 02:56:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.2 |


[Clique aqui para ver as próximas entradas](README45.md)
