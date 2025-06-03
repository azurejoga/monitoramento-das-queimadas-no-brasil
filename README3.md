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
| e2e01270-f449-3bac-b869-c1c3a427e5cb | -11.90813 | -47.45034 | 2025-06-03 00:56:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 515fee63-ccbd-3b1f-b541-ed1e964f47d2 | -9.07039 | -47.14779 | 2025-06-03 00:56:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2f66a3bb-d8b8-396d-9c1f-cb64a8570385 | -10.23308 | -52.22553 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 97484f3f-2d80-38d7-8eb9-a13e4b44812a | -11.24677 | -49.5059 | 2025-06-03 00:56:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8673e730-5f31-37e3-899f-b936e77367b1 | -11.24521 | -49.49529 | 2025-06-03 00:56:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 8c2f6249-bfc8-3c49-b3c5-d1290b00f7f7 | -11.57167 | -47.44315 | 2025-06-03 00:56:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 09566ed8-9d60-34d8-8bc5-8631567fa2d4 | -11.25631 | -49.50439 | 2025-06-03 00:56:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 24269054-754e-39d4-b726-54c65276a24a | -12.28453 | -50.11707 | 2025-06-03 00:56:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7e0214f5-6c14-3983-a061-5f2f9e4323b8 | -11.25476 | -49.49377 | 2025-06-03 00:56:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d4814c64-0b24-3690-a37b-e19b1f79b192 | -13.63755 | -52.19153 | 2025-06-03 00:56:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| f9ecb1de-a2de-38f5-a525-b15f1d50da0a | -11.5826 | -47.44125 | 2025-06-03 00:56:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 62a4910b-b09c-3824-adcf-6555eef88968 | -10.24189 | -52.22425 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 8c179ca8-5b46-3f72-9a74-a70fc08d4452 | -9.60762 | -49.01909 | 2025-06-03 00:56:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b49aea29-f9ce-36fc-8c6a-ec1c8d330704 | -11.43578 | -55.00967 | 2025-06-03 00:56:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b613de1d-78ca-3c0b-9ac3-1d6c786a1016 | -10.23432 | -52.23444 | 2025-06-03 00:56:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fc846b9b-caa1-3a01-a356-e76cc1f98178 | -11.41028 | -52.94415 | 2025-06-03 00:56:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d396844e-6daa-390d-b3c9-5b5097d614c9 | -10.50153 | -53.64861 | 2025-06-03 00:56:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 93b20a15-53fb-3ebb-89ee-8e054247314a | -10.45947 | -47.93307 | 2025-06-03 00:56:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c2499f6b-5845-3db5-afa1-653ce84a6c34 | -13.6363 | -52.18242 | 2025-06-03 00:56:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| e806836c-b717-3190-be3d-94adc7bd3f13 | -8.19878 | -49.81212 | 2025-06-03 00:58:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a68a1815-eed4-3c05-9654-5be8e5367823 | -7.01271 | -44.56868 | 2025-06-03 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 81718047-cf62-3b07-b281-bcc5114270b4 | -3.03494 | -49.42113 | 2025-06-03 00:58:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 7ca3a6ae-9f9b-39c5-bf4a-3935ef0f4260 | -6.98127 | -42.92612 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| f971c505-fff8-303e-ad83-bc2e02ced55b | -7.22394 | -43.11156 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 8b1f3da2-de30-3837-9a79-a00722c05f3b | -6.97791 | -42.93361 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.3 |
| bfae5002-b145-34f7-88b6-18ea1b5b97b8 | -7.90103 | -50.3612 | 2025-06-03 00:58:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ba38579f-f5ff-336a-9991-b2dc1c910b9e | -3.03691 | -49.43499 | 2025-06-03 00:58:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5b5f2403-aa76-3d1b-a273-8a86a6ffc70c | -7.90255 | -50.37155 | 2025-06-03 00:58:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 34ebe5dc-d479-3891-9a65-4bd2cb176d19 | -8.60228 | -51.57733 | 2025-06-03 00:58:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e2279556-08e6-3974-b0ba-f63aa4275fb9 | -7.2348 | -43.14058 | 2025-06-03 00:58:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| 7a0fe1be-cb95-3178-ab93-6d96399571d6 | -7.01419 | -44.57419 | 2025-06-03 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 95dbc4bb-edbe-3c1a-bc8a-a5a5b0a22932 | -7.22861 | -43.10365 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 9e886264-5b0c-3508-9a0d-b54b9e5722bc | -6.97167 | -42.8954 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 1e707ae2-d20c-3cfb-900e-285c78a94c27 | -8.90996 | -50.0563 | 2025-06-03 00:58:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bd7ad893-5d92-393a-a2cf-e83933e4b041 | -7.22986 | -43.14836 | 2025-06-03 00:58:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| f81a299e-d658-38e5-ba97-6aece5c0efef | -8.19715 | -49.80108 | 2025-06-03 00:58:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 969a460c-dafc-312f-9137-64d0ab994901 | -8.90843 | -50.04583 | 2025-06-03 00:58:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| daa78120-5173-33e3-9b4b-d2a16a0d8f43 | -7.21194 | -43.10632 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.3 |
| f5ec865d-ae6e-372e-b949-4e3fcea40dc9 | -8.9131 | -48.89814 | 2025-06-03 00:58:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c5b51e1b-087c-31cb-84a2-cbc8111eb0dd | -7.21816 | -43.14316 | 2025-06-03 00:58:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 37215e7a-fdc0-3ee1-ad41-77cdcb7aab11 | -8.91493 | -48.91035 | 2025-06-03 00:58:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| ecc8c16f-2ec3-3238-941c-2e22559b24d8 | -7.0175 | -44.59805 | 2025-06-03 00:58:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 6eda838b-48b2-32aa-aa90-3e3b38336234 | -7.2214 | -43.1153 | 2025-06-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 70908c9e-da87-337b-89b3-4ea1a2ffdbcc | -6.9791 | -42.9034 | 2025-06-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 153756d9-50bf-305e-a6f9-3cf04cf67055 | -11.2546 | -49.5098 | 2025-06-03 01:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7a19fed6-da1b-38c5-8f68-06560010ff6d | -11.2549 | -49.4881 | 2025-06-03 01:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| a7467953-c4a5-3249-b365-625b690bf76c | -7.2211 | -43.1388 | 2025-06-03 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| fb94d8d5-d0c9-346d-a49e-00b7fd3239ea | -13.1028 | -52.0281 | 2025-06-03 01:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 14b031b1-f960-3a63-9c50-0de98284eb94 | -11.2546 | -49.5098 | 2025-06-03 01:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 31fe3628-4c7f-38ed-b56d-556b1fefdd8c | -18.8675 | -53.6434 | 2025-06-03 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 14a4ec1b-7d01-38df-a04a-bfc308a5266a | -18.8679 | -53.6218 | 2025-06-03 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4f5ac96c-1e51-345e-b85f-c9f80b97a074 | -7.2214 | -43.1153 | 2025-06-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| abc705e3-5521-31dc-b220-43549e36e7d1 | -11.2549 | -49.4881 | 2025-06-03 01:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 1ae7866d-4e14-324a-8e96-a40893833ae0 | -7.2211 | -43.1388 | 2025-06-03 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.0 |
| 3e2a6ecf-b458-3e3a-9e1a-a32d99a1bedf | -18.888 | -53.6186 | 2025-06-03 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 9bc0d710-8f1b-3270-9394-45b9346ed353 | -10.462 | -47.9428 | 2025-06-03 01:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 97b6a49b-7d82-32cf-bb49-36bf12ea0f27 | -18.8875 | -53.6402 | 2025-06-03 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 130.0 |
| a5efeb26-0cf8-3247-8f48-3c4f16517725 | -10.6928 | -57.638802 | 2025-06-03 01:17:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 709dcd9a-4a18-3a7e-9549-fbedcd007930 | -18.881701 | -53.655201 | 2025-06-03 01:17:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 936571e6-a36e-3bc0-8e4f-94c66067f799 | -20.7243 | -56.627399 | 2025-06-03 01:17:00 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 56ff862c-050f-3592-82ac-25463fca77ae | -18.872 | -53.658001 | 2025-06-03 01:17:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5ab4c4-6084-3041-8850-83cda83e44b4 | -18.867901 | -53.6423 | 2025-06-03 01:17:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 43d9fcb8-172e-3267-882d-218865a79a4f | -14.0141 | -55.116299 | 2025-06-03 01:17:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb7cfe1-e448-3830-961b-9ddf63279a87 | -18.8638 | -53.626598 | 2025-06-03 01:17:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 12def231-8d55-39ff-8f7e-a761ab899650 | -18.873501 | -53.623798 | 2025-06-03 01:17:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6f800da9-1e43-3433-9e45-8cdb71126456 | -14.0179 | -55.131302 | 2025-06-03 01:17:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 876afff1-9bac-3aea-b1b2-08ead74cf153 | -14.0276 | -55.128799 | 2025-06-03 01:17:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8c9831a0-2037-30e0-b062-7353938910fc | -10.6956 | -57.650398 | 2025-06-03 01:17:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 410987d2-0449-34f2-9e7f-57f4b85e8360 | -20.722 | -56.617599 | 2025-06-03 01:17:00 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25a0bb88-71cd-37c8-bef4-eae291e088fe | -11.5527 | -56.428501 | 2025-06-03 01:17:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 720e7ab2-db92-31b9-85f1-2660df72358d | -18.8776 | -53.6395 | 2025-06-03 01:17:00 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 285cb0cb-b155-3da5-b7ec-8033fb0dbebd | -9.2435 | -63.289501 | 2025-06-03 01:17:00 | METOP-B | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86e6a384-0fc9-3184-bd02-db0f2d331ea3 | -11.5624 | -56.425999 | 2025-06-03 01:17:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a6178bf-3a5b-3a99-a1b5-3691349b6fb9 | -6.9791 | -42.9034 | 2025-06-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.2 |
| 676a9cc8-bcc4-3f9d-b995-63325dde9d7e | -18.8679 | -53.6218 | 2025-06-03 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 23b241c9-b8d8-36b4-b195-e3440c33283b | -18.8875 | -53.6402 | 2025-06-03 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 2b85e382-adc8-3490-8eae-794f835958e9 | -11.2549 | -49.4881 | 2025-06-03 01:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6d73931a-4573-3214-8faf-24479f0a96ae | -7.2211 | -43.1388 | 2025-06-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| 335bebc5-ad97-3c8a-a3bb-7bbdac4cfc0b | -18.8675 | -53.6434 | 2025-06-03 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 200.3 |
| d32722f8-a2d2-34ba-8bf7-742350b2c6d0 | -7.2214 | -43.1153 | 2025-06-03 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| b129c2bd-0026-342d-b6cd-c84536cf8fa4 | -18.888 | -53.6186 | 2025-06-03 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6316f85b-998e-3be6-873d-7c56da48918d | -7.2214 | -43.1153 | 2025-06-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 3c485903-987a-3324-b98d-1cc1a7af7ff6 | -18.8679 | -53.6218 | 2025-06-03 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 70d9da3b-7d8c-3216-b880-7cb12bb37d58 | -18.888 | -53.6186 | 2025-06-03 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8b8adecd-0165-3d7a-82ec-ac930a7c9448 | -18.8875 | -53.6402 | 2025-06-03 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 058e80ec-27f9-3a8d-b1ce-4b7c26680d71 | -13.1028 | -52.0281 | 2025-06-03 01:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| b89dfc35-0539-3715-918f-29b591658687 | -7.2211 | -43.1388 | 2025-06-03 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| e2b5a22c-2095-3e60-9df8-6fb7c60dd512 | -18.8675 | -53.6434 | 2025-06-03 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 193.6 |
| dc325d66-b28e-3e15-8724-19ebff20b79c | -7.2214 | -43.1153 | 2025-06-03 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| 3ce9cc62-1c22-37d8-9142-47bea198d2a5 | -7.2211 | -43.1388 | 2025-06-03 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| f7c1c884-ee32-3940-89d2-d60b22fda72a | -7.2214 | -43.1153 | 2025-06-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.7 |
| 7b051d8d-37bd-3d94-bb8e-8f354d68e004 | -7.2211 | -43.1388 | 2025-06-03 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 8f9becd5-7b66-31a9-b671-773d1fb23fb8 | -18.8679 | -53.6218 | 2025-06-03 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8e958de4-55a1-3220-97b0-94146a4acc86 | -18.888 | -53.6186 | 2025-06-03 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.9 |
| bcca6ab5-38e0-398a-bf35-5a93f2752916 | -18.8675 | -53.6434 | 2025-06-03 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 175.0 |
| 23b66b2b-bc4d-319f-ab0a-f805913dd287 | -18.8875 | -53.6402 | 2025-06-03 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 111.1 |
| bc930674-5dfa-3611-8501-8802ef88cedb | -7.2211 | -43.1388 | 2025-06-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| cf6d0208-f44b-335d-8568-30cb9378c7de | -7.2214 | -43.1153 | 2025-06-03 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 8b3e294b-35af-3c42-ace0-2425cd67af9b | -18.8875 | -53.6402 | 2025-06-03 02:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 96.1 |
| e699876f-5bdb-34c4-ab72-7a7b853c61a2 | -18.8675 | -53.6434 | 2025-06-03 02:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 67.6 |


[Clique aqui para ver as próximas entradas](README4.md)
