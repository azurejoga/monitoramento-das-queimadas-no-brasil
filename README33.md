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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57a3aa74-f1d1-39ba-b553-707380e0e4f3 | -16.774799 | -57.356499 | 2024-10-07 02:06:11 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 091dde54-222c-3cf8-acc9-2436bbedc076 | -16.7838 | -57.3876 | 2024-10-07 02:06:11 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e1bc8d81-393a-38b7-a776-254d80b8c168 | -16.765301 | -57.359402 | 2024-10-07 02:06:11 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c26a4592-b513-39e1-8caf-552a59cab7d3 | -16.7743 | -57.390499 | 2024-10-07 02:06:11 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbaa0c1d-fe08-33b9-8c70-dff0178fcd16 | -16.764799 | -57.3936 | 2024-10-07 02:06:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a1b3c481-f7b6-3d24-b087-311cd3e1b7d0 | -16.783199 | -57.421501 | 2024-10-07 02:06:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3c34e10-a5fc-325b-b23e-f6f6c206eaf8 | -16.755301 | -57.396599 | 2024-10-07 02:06:11 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 994edd9a-e8f5-38a2-9f9a-432bf4372f00 | -16.4646 | -57.719601 | 2024-10-07 02:06:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c30ceac7-74a8-3201-8aaf-0cfd8e8b227c | -16.455999 | -57.689602 | 2024-10-07 02:06:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81ea53c1-59fa-33e8-b4d3-273dd3903e7a | -16.4741 | -57.716702 | 2024-10-07 02:06:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cbfc7b52-a09a-3de0-8885-71756fe18093 | -16.465599 | -57.686699 | 2024-10-07 02:06:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 329259dc-ec72-359c-baba-22ca0f88222e | -16.4751 | -57.683701 | 2024-10-07 02:06:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ee67a36-5e64-3b8b-b234-8036d7a3da2a | -16.483601 | -57.713699 | 2024-10-07 02:06:17 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfed4afd-ff58-3b3b-b068-be0a75e5eb57 | -15.0422 | -51.24 | 2024-10-07 02:06:31 | GOES-16 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 0f97d95a-06ea-3751-a33d-5f1ecb7a0bf1 | -16.5739 | -57.201 | 2024-10-07 02:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 7632032e-52f9-38ea-943b-da09457f04ba | -16.527 | -57.7161 | 2024-10-07 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 293c702c-0b02-3629-8879-3e522b87cf69 | -16.5267 | -57.7365 | 2024-10-07 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.7 |
| 2c4caae3-58bd-366e-a757-6db2bee13e20 | -16.5075 | -57.7183 | 2024-10-07 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 192.2 |
| fc29a653-a12d-3d89-b619-4cbce6e28fbb | -16.5072 | -57.7387 | 2024-10-07 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 238.5 |
| bf5f3706-5aa7-3f72-b5e0-a1bd92c8b782 | -16.488 | -57.7205 | 2024-10-07 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |
| 3ccddb93-88f6-333b-ad34-37bf5c1b264f | -16.4877 | -57.7408 | 2024-10-07 02:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |
| caf35eb0-99d3-3fd5-b4c0-93b040e596a5 | -16.6332 | -57.1533 | 2024-10-07 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.7 |
| d682a04e-f053-3a2e-a68b-26365cd02839 | -16.6329 | -57.1738 | 2024-10-07 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 89dbc628-3f70-3c31-8a95-f50f99e96886 | -16.614 | -57.135 | 2024-10-07 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| 197afb6f-fff8-39bd-ac50-487bbbe423e1 | -16.6136 | -57.1555 | 2024-10-07 02:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| ba0ac968-83f7-31d6-9ad4-066e6ecbc6ad | -17.0985 | -57.4062 | 2024-10-07 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.6 |
| 4c710359-4ac8-33bd-aed8-18aa78d7272c | -17.0982 | -57.4267 | 2024-10-07 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 153.3 |
| 041d7c8a-a8c6-3839-a45b-7cd9c36f2b05 | -17.0881 | -56.8328 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.2 |
| 9c6e73ee-ec67-37a3-a6d8-bb5538e9d534 | -17.0685 | -56.8352 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.1 |
| 26f570a8-a5b6-30e8-ac4c-5a08f2a4918a | -17.012 | -56.698 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 47ce07a3-6879-3420-9750-c405ec7be8b9 | -17.0116 | -56.7186 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| f7b0ed95-4750-3780-881e-fa7c2056178f | -16.992 | -56.721 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 7db8a07b-22c7-337c-9e41-3a4fb58e2d54 | -17.1274 | -56.828 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.9 |
| df1e888b-8b29-35c6-8098-82edc42e8d1c | -17.1078 | -56.8304 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 129.7 |
| d90a5a0e-94ab-32c2-ab40-b51c18461a51 | -17.1074 | -56.851 | 2024-10-07 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 12cd7aa1-b050-3378-b1d6-4d98356a8bd1 | -17.1584 | -57.3377 | 2024-10-07 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| bfcfe435-e4ef-3ec0-911f-a36587097cac | -17.1581 | -57.3582 | 2024-10-07 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 19145fd4-37a7-32a8-befe-e38f3a305124 | -17.1571 | -57.4198 | 2024-10-07 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 4e51ef39-b4fb-3c1c-89a6-3dd3ffca158e | -17.1375 | -57.4221 | 2024-10-07 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| a43c220a-9a93-303f-b7f7-ce7ea7079a91 | -17.6274 | -53.1309 | 2024-10-07 02:06:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 93259bf6-0ec8-3728-af61-aeee6fdda262 | -17.6279 | -53.1094 | 2024-10-07 02:06:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 334.6 |
| c01cc4aa-665c-33ff-8f3d-d8f1c2dd676f | -17.6283 | -53.088 | 2024-10-07 02:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| beee7a11-974b-3cc4-8ab2-5f913748c80b | -17.6477 | -53.1064 | 2024-10-07 02:06:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 51f83d08-94f8-31f2-a575-3dfe719c0ba1 | -17.6481 | -53.0849 | 2024-10-07 02:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1211fbb4-1754-3406-8e22-07a11cc375ff | -17.6679 | -53.0819 | 2024-10-07 02:06:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 95d7065d-9615-34fe-8e4e-7a05c3630eee | -18.4514 | -53.538 | 2024-10-07 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 4e7ab058-e87b-315f-ac87-d7cd04712dff | -18.4518 | -53.5165 | 2024-10-07 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 134.3 |
| e2ca6cfc-6793-39c9-81a0-fb975607b2bc | -18.4523 | -53.495 | 2024-10-07 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 59.8 |
| ef5151df-94d4-3b36-864b-947d35d62f92 | -18.4713 | -53.5349 | 2024-10-07 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3f55fb87-c970-3b67-b28b-496028589ac7 | -18.4718 | -53.5134 | 2024-10-07 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 217.8 |
| 97090ae7-2aef-3c36-9b20-bae5eda5a607 | -18.4722 | -53.4919 | 2024-10-07 02:06:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 72.5 |
| b5b086be-cedb-316d-a604-a10dbb319ec2 | -18.659 | -57.2552 | 2024-10-07 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 384d2863-2a93-39b4-9c23-bc691f1cb5b8 | -18.7176 | -57.3097 | 2024-10-07 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 76a35025-cad1-30a3-aff7-968d3e6eb158 | -18.718 | -57.289 | 2024-10-07 02:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 60238bf4-d9cc-3845-997c-1594ba1f0e96 | -18.8886 | -54.5587 | 2024-10-07 02:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 8bbbf0d5-3bd8-3abd-a55d-000ed1ffb6ec | -19.8318 | -42.3542 | 2024-10-07 02:06:55 | GOES-16 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.0 |
| 8fe4870f-aa1c-3be3-965c-3160e1943e18 | -20.1026 | -49.0562 | 2024-10-07 02:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 1f645ac9-5f4b-3f38-ade1-d077f8aacd93 | -20.1223 | -49.0748 | 2024-10-07 02:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 220.4 |
| 29478b6e-4e1d-38cc-a508-72e8a1f3c711 | -20.1229 | -49.0518 | 2024-10-07 02:06:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 380.8 |
| fbb4cb2b-83c0-3d91-a3d4-dfc9f6d96835 | -20.4449 | -47.6875 | 2024-10-07 02:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 115.9 |
| ae2f284f-3e80-3c55-aef8-7cb8ee93a86e | -20.4456 | -47.664 | 2024-10-07 02:06:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 604827d6-8962-3fc7-a6c9-3a66d47a0b19 | -20.4655 | -47.6827 | 2024-10-07 02:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 224.8 |
| 5df8dbd7-18a1-39af-b14d-27cbc9dd8610 | -20.4661 | -47.6592 | 2024-10-07 02:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 448.2 |
| 7d82b1f8-2f09-3bc5-9254-96a9dddcb327 | -20.4668 | -47.6357 | 2024-10-07 02:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 72.0 |
| fd6f501d-6cb2-3c86-8d36-1087b9451888 | -20.4866 | -47.6544 | 2024-10-07 02:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 155.5 |
| e839d464-55fd-386b-8c66-760248cc4dba | -20.5848 | -48.5137 | 2024-10-07 02:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 5d438ae9-cfdf-3969-8274-fedc2c09c604 | -20.5855 | -48.4904 | 2024-10-07 02:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 424.4 |
| ab7f645d-bed8-3765-a4e7-394ad5ed28be | -20.5861 | -48.4672 | 2024-10-07 02:07:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e32bea92-2465-3b85-af59-fd40698d3cfb | -20.6053 | -48.509 | 2024-10-07 02:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 117.1 |
| eb26d19e-3e23-3f7d-9e16-5578edbbefde | -20.606 | -48.4858 | 2024-10-07 02:07:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 358.1 |
| f9174e1b-9bdf-3020-843b-05bc789ea11e | -20.6066 | -48.4626 | 2024-10-07 02:07:00 | GOES-16 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4099597a-6682-3ab7-8469-94aafed610ad | -21.0712 | -47.2331 | 2024-10-07 02:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6ebbb7d6-55e7-354a-b1da-9973b025a9ce | -21.0919 | -47.228 | 2024-10-07 02:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4f5de368-ad3b-37f9-91ae-fa516012cbad | -21.5691 | -47.7696 | 2024-10-07 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4362ad73-6e33-3b0d-86fa-df487b20e63b | -21.5698 | -47.746 | 2024-10-07 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 341.2 |
| d4e3b427-f2c3-32c7-9e83-0d0d4f80c5a8 | -21.5705 | -47.7223 | 2024-10-07 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 163.6 |
| 3437c7a7-ce2d-3178-b745-3e108fc1414c | -21.5843 | -47.9536 | 2024-10-07 02:07:05 | GOES-16 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5bad0810-53bb-3d64-b152-9db78ae0a7cb | -21.5906 | -47.7409 | 2024-10-07 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 339.8 |
| 2f335b9b-5d40-3293-b370-b6c49c1d7d7b | -21.5913 | -47.7172 | 2024-10-07 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 253.2 |
| f18db0ea-2bb6-39fc-a644-018152692a81 | -21.605 | -47.9485 | 2024-10-07 02:07:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 69.6 |
| cfba8ecc-ea7a-319f-8e17-32393925dfe0 | -21.6121 | -47.7121 | 2024-10-07 02:07:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4a41128b-1d89-3d1d-8f88-65863d0973af | -10.3206 | -64.2472 | 2024-10-07 02:08:24 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 03f70dac-1e58-3bf4-b4b3-aa0c2fd32baf | -10.8111 | -68.3545 | 2024-10-07 02:08:32 | METOP-B | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 011f563f-7e25-31b2-8a1f-396209ef445f | -10.6929 | -69.451599 | 2024-10-07 02:08:38 | METOP-B | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 76159414-6558-3fef-970b-a71045ac8e80 | -10.3794 | -67.875999 | 2024-10-07 02:08:38 | METOP-B | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 782bbb36-861c-3703-975b-34efce659cad | -10.2048 | -68.2771 | 2024-10-07 02:08:42 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a7eddc43-d291-3d26-95cc-d1113e06521e | -10.2029 | -68.268898 | 2024-10-07 02:08:42 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e2099607-398f-31f2-80e1-9b350a15e972 | -7.8771 | -72.455002 | 2024-10-07 02:09:35 | METOP-B | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bdf8dca6-d347-33e4-be8b-9a648d0f83cd | -3.5136 | -65.022598 | 2024-10-07 02:10:18 | METOP-B | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90563308-1a55-3a73-894e-29aa855ca40c | -3.5234 | -65.020302 | 2024-10-07 02:10:18 | METOP-B | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c12d4fb-6639-3464-8739-51859ef13207 | -3.5197 | -65.004402 | 2024-10-07 02:10:18 | METOP-B | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20bd305c-f413-36aa-a531-99e2eb9924fa | -1.0365 | -53.7389 | 2024-10-07 02:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| a3cca403-e430-36fb-b0a5-2627650886c2 | -1.0365 | -53.7187 | 2024-10-07 02:15:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| f0c37f13-8e45-3dfb-bcf3-00760a115b5e | -2.2297 | -53.7026 | 2024-10-07 02:15:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 07d68cd9-257d-34af-b98a-906bf0480b97 | -2.8569 | -52.9197 | 2024-10-07 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1a24ac89-a862-39d6-9cde-d20d9b6a2737 | -2.857 | -52.8993 | 2024-10-07 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| a7769c66-484b-3520-9ead-bd6e0349e460 | -2.8753 | -52.9192 | 2024-10-07 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 7d91f3c2-cc11-3cbc-9bf5-612c4b6b561b | -2.8754 | -52.8989 | 2024-10-07 02:15:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| cbe53ee5-11fb-399f-88ee-051f3a6f1a1d | -2.8937 | -52.8984 | 2024-10-07 02:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b2423021-92bc-39aa-a53d-c2cfdf78cd3e | -3.538 | -65.0414 | 2024-10-07 02:15:26 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |


[Clique aqui para ver as próximas entradas](README34.md)
