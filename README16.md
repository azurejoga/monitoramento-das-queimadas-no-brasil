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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ed97732-f29a-36dd-99fd-57d4b2cb176f | -17.3643 | -42.6284 | 2025-09-07 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 9424dc2d-cf18-3ae2-9fc7-343a2d9fada0 | -12.948 | -54.7724 | 2025-09-07 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 408.0 |
| a1c57bb3-9a42-30f8-925a-2a28bb1d786d | -14.1753 | -53.3506 | 2025-09-07 02:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 8d8eecc0-1dc5-3d3f-a1b5-0c7ce7972cbf | -7.7404 | -48.8204 | 2025-09-07 02:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 2d34082f-d657-3f19-b6ee-0807f32629e7 | -12.967 | -54.7705 | 2025-09-07 02:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4d8622a3-33e2-32c0-a55b-996a695ab8e8 | -3.5995 | -47.5142 | 2025-09-07 02:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| df792333-6ac9-36a4-a1ce-b68e863f4a61 | -20.5628 | -46.4358 | 2025-09-07 02:30:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 7f4ec6a1-8817-3ca9-9902-266067364f6c | -12.9289 | -54.7744 | 2025-09-07 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 4156aced-b0d9-35e8-ab1a-2abffcf1332c | -6.7297 | -45.1447 | 2025-09-07 02:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2cae7d5e-3b2e-3465-8eac-991a0e000974 | -20.5635 | -46.4118 | 2025-09-07 02:30:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0bcf2a02-e9b1-3653-8448-f4427fef4a7b | -17.3636 | -42.6532 | 2025-09-07 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 49.0 |
| bf01f33f-d9ee-3c22-a20d-d7e62b793a69 | -6.3006 | -51.4205 | 2025-09-07 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 40db4c4d-922c-3935-b44e-eba7582fdcf3 | -20.5422 | -46.4408 | 2025-09-07 02:30:00 | GOES-19 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f204add6-fdfc-358e-981a-093cef958ccb | -6.3008 | -51.3996 | 2025-09-07 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ba577c48-40ef-3e60-a464-14bd00d95c32 | -12.9286 | -54.7949 | 2025-09-07 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 8da758d8-aeff-3e3f-a174-ec77c6831332 | -7.7404 | -48.8204 | 2025-09-07 02:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 3527ddac-b1af-3613-843c-0a6b1c744947 | -12.9477 | -54.793 | 2025-09-07 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 183.4 |
| 662a4a4e-87d6-3253-9eaf-1dc28cfb3cb1 | -17.3643 | -42.6284 | 2025-09-07 02:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a691dad8-8990-36c1-8b4f-cdacffce916b | -12.9482 | -54.7519 | 2025-09-07 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 105.9 |
| f0cc3231-9d37-3ac9-a59e-2b31efd606c2 | -12.948 | -54.7724 | 2025-09-07 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 487.7 |
| 390ccfe9-f687-3c39-8e9f-ccf7dd37d293 | -12.967 | -54.7705 | 2025-09-07 02:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 456ddd3b-2502-3302-b43a-523af8b14c5f | -7.7591 | -48.8189 | 2025-09-07 02:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 95.0 |
| bd0d43d8-b8d7-3411-896a-479cafb2ae56 | -6.3008 | -51.3996 | 2025-09-07 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| dc37bd7a-60d2-3e5b-a008-c4fcb32684b5 | -7.7404 | -48.8204 | 2025-09-07 02:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b078f44a-6886-3ef6-96ef-19e0f1c22175 | -7.7591 | -48.8189 | 2025-09-07 02:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c57b627c-7134-33ca-b097-6fbb3104bae5 | -12.9477 | -54.793 | 2025-09-07 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 5b5f615f-5b27-33fa-8ba4-821c65341b02 | -19.4898 | -47.7646 | 2025-09-07 02:40:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f566085d-d18f-33d1-9515-693ec190e7fe | -12.9289 | -54.7744 | 2025-09-07 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 205.0 |
| 667bb056-4808-3d12-8907-740904755d87 | -12.9482 | -54.7519 | 2025-09-07 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 98276492-b47d-3217-a5fe-5830ccbeaa86 | -12.948 | -54.7724 | 2025-09-07 02:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 544.8 |
| 2e58e454-e401-3738-b6c4-37c7f55fb78a | -6.3006 | -51.4205 | 2025-09-07 02:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 507ff43b-a1e1-3c90-a96e-ecb052c9d497 | -3.5995 | -47.5142 | 2025-09-07 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| dd759858-3e36-34c5-a84c-78100605d74a | -9.2971 | -66.6215 | 2025-09-07 02:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 3ec2c352-1e8b-3795-8443-80910e7dfda4 | -17.3643 | -42.6284 | 2025-09-07 02:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 5296f7e4-c47b-33dc-b65e-a636b0cb3d2a | -3.581 | -47.5149 | 2025-09-07 02:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 760a2449-7dc3-3b95-aec0-bd8980b69f82 | -6.7297 | -45.1447 | 2025-09-07 02:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 61b9ade1-144e-31cb-bf15-e49c7484984e | -17.3643 | -42.6284 | 2025-09-07 02:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5464399c-1d02-327b-98c5-1a5fc41241f2 | -7.7404 | -48.8204 | 2025-09-07 02:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d89587f9-6aa6-37a9-842b-770ec918927b | -7.7591 | -48.8189 | 2025-09-07 02:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 9f0b894b-b63c-349b-8c9c-42099689e65b | -12.9482 | -54.7519 | 2025-09-07 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6226349d-6ea9-3603-af2f-0b360c579e39 | -11.3194 | -46.567 | 2025-09-07 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d89e1c68-6f79-34eb-a8ad-bd2188757a13 | -9.4309 | -62.3683 | 2025-09-07 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| f3a352c1-2049-3f26-a5ea-8dab96594eb2 | -12.9289 | -54.7744 | 2025-09-07 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 219.9 |
| 7cfda1d7-b96c-3104-be86-52198a51331d | -3.5995 | -47.5142 | 2025-09-07 02:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 96ddbc74-e643-336c-abab-a8107a1c7cf9 | -6.3006 | -51.4205 | 2025-09-07 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| fa9712ea-0910-3de4-bb2d-2f8678377543 | -6.3008 | -51.3996 | 2025-09-07 02:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| a7c1cae5-c33c-339d-b84d-20cdfaa87b21 | -12.9477 | -54.793 | 2025-09-07 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| d6dff811-292a-3fa6-859b-9481b6c35fe6 | -9.4495 | -62.3675 | 2025-09-07 02:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 2ed3ded7-1faa-3626-8cf9-1273b76e688f | -19.4695 | -47.7691 | 2025-09-07 02:50:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 31571f0f-8f04-3529-9857-1a56eab5f32b | -12.967 | -54.7705 | 2025-09-07 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 27c55880-1c1d-3bf6-bd26-3edd14bc4982 | -12.948 | -54.7724 | 2025-09-07 02:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 350.1 |
| 76b98ba2-9c5a-3935-a4cc-f32789f253a8 | -11.3198 | -46.5444 | 2025-09-07 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 26a9ccac-7d74-39ab-aa1f-aba89edcd45e | -6.3008 | -51.3996 | 2025-09-07 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| fa4a09f5-7a14-3193-9f9e-4e0fc942525a | -3.5995 | -47.5142 | 2025-09-07 03:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 13fa9b5d-c90f-3d8b-8cf5-5e51698e693e | -7.7591 | -48.8189 | 2025-09-07 03:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 5bd71f3c-d07f-3f50-a111-6ecc013b0413 | -7.7404 | -48.8204 | 2025-09-07 03:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ed339715-e72e-356d-8f2e-4cff091def4f | -6.3006 | -51.4205 | 2025-09-07 03:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| a4631e54-b781-3961-b60e-b52d070f8889 | -9.4309 | -62.3683 | 2025-09-07 03:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 08a7467a-9b79-3347-9eeb-8075357a853b | -11.3198 | -46.5444 | 2025-09-07 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 989d306a-b516-3708-9cbf-cc7392479a91 | -6.3008 | -51.3996 | 2025-09-07 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| b33ae517-1511-3f3b-b881-e4c0c8ae2726 | -19.8853 | -57.9031 | 2025-09-07 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 994ea61f-1149-38fb-b5ef-c2442ab247df | -12.948 | -54.7724 | 2025-09-07 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 398.0 |
| b4a024d2-38f6-3abd-ac26-12bcb3205481 | -6.3006 | -51.4205 | 2025-09-07 03:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| fc1b3ef5-072e-32ad-b791-3884448cab79 | -12.9289 | -54.7744 | 2025-09-07 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 292.0 |
| 3c6f9dab-a42d-3d9b-8606-aea0844376a6 | -12.9477 | -54.793 | 2025-09-07 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c6827b7b-f608-382e-9b63-e4031a4a51a1 | -12.967 | -54.7705 | 2025-09-07 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| eaa9e2ed-84e2-33f8-aefc-bdd66fc54a06 | -11.3198 | -46.5444 | 2025-09-07 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 08708bc6-31d1-3402-8bb9-b254ef6db27b | -12.9482 | -54.7519 | 2025-09-07 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 7a2616f5-1a12-3e56-a164-ba1c38aec4a0 | -12.9292 | -54.7538 | 2025-09-07 03:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8fcbf442-60bc-3646-8330-a5e1c23c1c77 | -11.5958 | -47.1588 | 2025-09-07 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 549ef546-f796-3d02-90b6-809b9061dc29 | -3.5995 | -47.5142 | 2025-09-07 03:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 79fd074f-fa72-30d7-9922-8b752598ea7a | -11.3194 | -46.567 | 2025-09-07 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| fc9665ed-ec7a-3c6e-9d47-133b38d86b4f | -19.4695 | -47.7691 | 2025-09-07 03:20:00 | GOES-19 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f1b6ff06-a0c4-3503-949d-b47564238050 | -19.8853 | -57.9031 | 2025-09-07 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| e5913050-92b9-3b67-8209-e590f48e25e6 | -6.3006 | -51.4205 | 2025-09-07 03:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a215f6d8-ec71-3486-8417-47c2aa98c324 | -11.6149 | -47.1563 | 2025-09-07 03:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| d0564cf0-ecc5-3f2a-bb1d-a1c8369df3bc | -11.3198 | -46.5444 | 2025-09-07 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 7f625a08-6d69-399f-b068-dcb0f14a83b6 | -2.87869 | -40.30314 | 2025-09-07 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b38c7284-8286-3b05-b0e8-c0c13425a261 | -3.35435 | -39.27535 | 2025-09-07 03:28:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e431881f-26ab-362d-bd73-4bbff4a60955 | -3.35346 | -39.28078 | 2025-09-07 03:28:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 99689f84-bc42-3949-82e9-758653eaf5f2 | -2.87922 | -40.2999 | 2025-09-07 03:28:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b667a2a4-4f58-36c3-a541-73907a269821 | -12.9477 | -54.793 | 2025-09-07 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c1278ebd-d79a-35a0-87b3-645a389c7612 | -12.9289 | -54.7744 | 2025-09-07 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 6ae0ad94-ed91-3205-b771-94d6e3c76cee | -11.6149 | -47.1563 | 2025-09-07 03:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 85c886ae-591b-329b-a984-60de7f4b4ad1 | -11.5958 | -47.1588 | 2025-09-07 03:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 178.4 |
| f3ec97d5-5a4e-31b3-8daf-200a0460a56f | -12.9482 | -54.7519 | 2025-09-07 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3bed6f00-c686-3f6b-aac7-198fb46fc819 | -13.8403 | -46.2828 | 2025-09-07 03:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 7a99e82a-d34c-3653-9bde-3e4469c9bd4c | -11.5954 | -47.1812 | 2025-09-07 03:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 292094bf-d346-389b-a65b-1878ef9b2400 | -12.948 | -54.7724 | 2025-09-07 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 319.7 |
| d1206443-73a2-3679-9607-f88b5c1213bf | -13.8407 | -46.2598 | 2025-09-07 03:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 7c2d91db-6190-3920-ad07-041b139a3175 | -8.18354 | -44.78238 | 2025-09-07 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 54a62223-ded0-327a-acde-1bc3e3786996 | -6.15237 | -43.17924 | 2025-09-07 03:30:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a2fc9c7c-7167-34cd-b728-8956f3469a84 | -6.18527 | -45.42131 | 2025-09-07 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 3aa213b4-49dc-3ed7-afac-b6f380d0c359 | -7.80888 | -45.42605 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b61f37a2-2e02-3865-8de2-ab5d832f4eb6 | -5.83051 | -44.12798 | 2025-09-07 03:30:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 91f65523-40be-3983-b79f-f2a4104b27cc | -7.81706 | -45.43489 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffe5b196-01cf-35fa-8889-378a79b0ff08 | -6.2318 | -42.59318 | 2025-09-07 03:30:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59c30d2b-943a-3d3a-a7f4-dca3b2a1e0c9 | -6.88603 | -45.59929 | 2025-09-07 03:30:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 18b490ff-6099-36fb-9c61-60d2f234925d | -7.81569 | -45.42673 | 2025-09-07 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94b38a73-6296-39b1-adb4-b8e12efc5c11 | -6.55723 | -42.94479 | 2025-09-07 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README17.md)
