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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82f91f1a-d36b-3031-82ba-0b4dd79e42c4 | -22.3922 | -49.2961 | 2024-10-01 03:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 7281cf3f-0799-3bbc-9a47-e8b0fee689bf | -23.0793 | -45.3951 | 2024-10-01 03:37:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.0 |
| 4b90a827-878b-3f74-966b-2e1a772951b5 | -2.4048 | -50.3085 | 2024-10-01 03:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 926f74af-22c1-3bea-8620-21673cc82b42 | -2.4047 | -50.3295 | 2024-10-01 03:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 332.9 |
| e04b22c4-ceab-399f-9cab-8de6f98bf79b | -2.4046 | -50.3505 | 2024-10-01 03:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 1abe4e43-6482-3ebb-80b7-c3fa88969bca | -2.3863 | -50.3299 | 2024-10-01 03:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 4907ae12-76c3-3079-853a-d7784ce6988b | -2.3862 | -50.3509 | 2024-10-01 03:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 79452061-c07c-3347-a708-199c25fa12ef | -3.0282 | -51.3345 | 2024-10-01 03:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 1593a3cb-6a7d-3821-92da-42c60cf4b04c | -5.9788 | -45.3621 | 2024-10-01 03:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| c39d3a04-0167-3a63-907b-b5c77cac5163 | -5.9786 | -45.3847 | 2024-10-01 03:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| d3fd10af-6d2a-356e-975e-45d0e3b83374 | -6.545 | -43.0373 | 2024-10-01 03:45:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 43129336-79c6-3d16-898a-bc833ea8aebd | -12.1406 | -50.0524 | 2024-10-01 03:46:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 47254af7-f567-3ee3-aef6-4fbe2fc389b9 | -12.1402 | -50.074 | 2024-10-01 03:46:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 29c27adf-32da-33e2-9d45-cb2f691c56a9 | -12.2738 | -53.9773 | 2024-10-01 03:46:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 3810c34c-3cde-36b6-adb1-84711a4ae980 | -12.2735 | -53.9979 | 2024-10-01 03:46:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 54404008-f749-3763-8440-e47828360b23 | -12.2547 | -53.9792 | 2024-10-01 03:46:15 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 42932c52-afdc-3e95-9d50-b35ee731e730 | -12.2545 | -53.9999 | 2024-10-01 03:46:15 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 1b6c2987-a512-3873-b928-55701c120e0a | -12.9783 | -51.428 | 2024-10-01 03:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 3dac160a-7d31-320a-8bd4-81d4911fe5ae | -12.8397 | -62.8607 | 2024-10-01 03:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 39981c70-1163-33a9-9626-075e5e9577c0 | -12.9591 | -51.4303 | 2024-10-01 03:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 94410e13-aa8c-3969-9550-a5d6233a6e0e | -12.9588 | -51.4517 | 2024-10-01 03:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 0e75eaf7-5863-31f5-bde6-5b69bdc33856 | -12.8206 | -62.881 | 2024-10-01 03:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 55351e0f-a1be-387e-835b-35b80fcfb89f | -12.94 | -51.4327 | 2024-10-01 03:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 2c220d92-f0c9-38c2-abab-e217d9aeb14d | -12.9396 | -51.454 | 2024-10-01 03:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| c6676edb-44f1-3648-a7b0-ba74053d932f | -12.7826 | -62.9025 | 2024-10-01 03:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| c567d30d-75d4-3309-be4d-36935f88afa4 | -12.7636 | -62.9036 | 2024-10-01 03:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 606d25cd-d581-31cb-8671-ded09e433582 | -13.2304 | -51.2262 | 2024-10-01 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 5ad58b49-00ad-3efa-9f58-dd77a9268ae5 | -13.2116 | -51.2073 | 2024-10-01 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 945f817b-1c34-3b99-bd2a-e2b08b6b2b13 | -13.2112 | -51.2287 | 2024-10-01 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| dc14775f-ca8a-3348-a904-0fa10f8480a4 | -13.2308 | -51.2048 | 2024-10-01 03:46:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 77e1f910-a08b-3f97-ba9a-b1f43ad23536 | -13.5768 | -51.1607 | 2024-10-01 03:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d14ca3fc-719b-3942-bc2d-bbfda1e68881 | -13.5957 | -51.1796 | 2024-10-01 03:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 553bbdf8-c31b-3ec8-a8fb-40423ea5708c | -13.5961 | -51.1582 | 2024-10-01 03:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| dd74800f-9ce1-3016-9927-d2a88a2c5b31 | -13.6342 | -51.1746 | 2024-10-01 03:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5b392669-dbc9-3ea0-ad39-dded1a20398e | -13.6346 | -51.1532 | 2024-10-01 03:46:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 95132686-1c6e-35bb-92d9-ed0aa56815f0 | -14.7406 | -48.7498 | 2024-10-01 03:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 82c4deb4-8dd7-3ec2-a941-808ec9d56f41 | -14.7402 | -48.7721 | 2024-10-01 03:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 934c19c5-8e00-3af6-bf96-983789267bb7 | -15.9127 | -57.1733 | 2024-10-01 03:46:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6523fc44-dcf5-3462-a2fc-fbdeb0f41a14 | -16.1116 | -50.3391 | 2024-10-01 03:46:36 | GOES-16 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a05bd5a5-63b6-3f52-ac16-3442cf81c92e | -16.474 | -57.3553 | 2024-10-01 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| cf5dce2a-aede-3246-b439-e4436dddf640 | -16.4743 | -57.3349 | 2024-10-01 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| fad18083-a41e-387e-a9e2-d41dd394b0b7 | -16.4935 | -57.3531 | 2024-10-01 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| f56741b4-11a7-33fb-8efe-3ecc9139b92a | -16.4939 | -57.3327 | 2024-10-01 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 269f0f6d-4ee2-3b7d-8c6d-4eb7055e1736 | -16.5131 | -57.3509 | 2024-10-01 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.1 |
| ef8eea2a-e0c9-370c-bdf6-fcc90793f65b | -16.5134 | -57.3305 | 2024-10-01 03:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 444ec0d8-7f88-3682-914e-d48b2ad6b0ee | -16.613 | -55.9836 | 2024-10-01 03:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 9e39c9b9-40a0-3496-8bae-b1ca8ebece8d | -16.6133 | -55.9628 | 2024-10-01 03:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.5 |
| b64ca7b7-77d7-33d8-afd5-d86c74a4ef91 | -16.6136 | -55.9421 | 2024-10-01 03:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| ff7d3cf4-ff41-3e31-93f4-90665cb6ddb6 | -16.6329 | -55.9604 | 2024-10-01 03:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.0 |
| 0976e8b6-7d42-3947-a038-b22f4c399302 | -16.6455 | -55.2117 | 2024-10-01 03:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| e9d5e1c0-17e5-3d43-9033-01285a86a3a8 | -16.6459 | -55.1908 | 2024-10-01 03:46:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 56.0 |
| f4d31b79-e16e-3cff-bd37-26e41642adf8 | -16.6316 | -57.2557 | 2024-10-01 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 39716c78-d2fc-3463-ae5e-333702e0f0d2 | -16.6525 | -55.958 | 2024-10-01 03:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 551a1c36-da4c-36ac-9bbc-b1e4452a2967 | -16.6505 | -57.2944 | 2024-10-01 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 229.9 |
| 6406d966-0687-31dd-8d18-c99f9c3f149d | -16.6508 | -57.2739 | 2024-10-01 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.3 |
| 374c105c-25a4-3027-8905-83805a1b7091 | -16.6512 | -57.2535 | 2024-10-01 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 35e65d5c-9412-3a8e-b048-7c0e5afea3ce | -16.6701 | -57.2922 | 2024-10-01 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 175.6 |
| 879d2e53-539b-30d3-89d0-b97ff08c8580 | -16.6704 | -57.2717 | 2024-10-01 03:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| d1f2bc64-400b-3217-a5ba-add01c5fdf69 | -16.8784 | -57.7175 | 2024-10-01 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 30dd7ba8-2ecf-3c98-86db-0a1543cfdb07 | -16.8787 | -57.6971 | 2024-10-01 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 2609785e-85b7-376a-af1d-48c91856e7fa | -16.898 | -57.7153 | 2024-10-01 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 8ef82c1a-096c-31f2-b766-b83bcc3709fd | -16.8983 | -57.6949 | 2024-10-01 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.3 |
| 3614a8bc-8775-3333-b637-847fe55fa320 | -17.0506 | -56.7344 | 2024-10-01 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| ef109e80-4087-3f8f-b33f-c82e52d73d2b | -17.0509 | -56.7138 | 2024-10-01 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 168f0f28-0826-3edc-bb24-80099c2841c9 | -17.0702 | -56.7321 | 2024-10-01 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| ea9e240a-cee8-3896-ad9b-4a2c21cead19 | -17.0705 | -56.7114 | 2024-10-01 03:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 845b46e5-6ec4-3e51-90ae-702aacb33a64 | -19.1329 | -57.4628 | 2024-10-01 03:46:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 78e6139d-547c-3bfd-83b2-6a6184345b5c | -1.1711 | -47.731 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7a0a53a9-4269-37bf-9654-cedf207f69be | -1.17022 | -47.73645 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7ca98ce9-57c5-37e6-bb17-7399d227ea94 | -1.16994 | -47.73192 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b356498c-6edb-3728-b824-8abb91a98df8 | -1.16934 | -47.7419 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dcea7be1-7dbc-3380-bca7-b14890763a13 | -1.16903 | -47.73736 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1b64eaae-6ce9-36bd-b1b6-10d591d1841f | -1.16812 | -47.74277 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b68cd844-a778-31f0-b542-853330b95b79 | -1.16368 | -47.73539 | 2024-10-01 03:47:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15cb977e-e61b-3517-8ac8-535a8c284863 | -7.9202 | -38.48095 | 2024-10-01 03:47:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3ad56962-22cf-3859-bcf9-20df89dbf3cf | -5.26243 | -36.19195 | 2024-10-01 03:47:00 | NPP-375D | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a23e7e1e-e69a-3509-94c0-a2a9554982fd | -5.15983 | -37.96367 | 2024-10-01 03:47:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2079bd50-e062-319f-b825-1e90adfdec5d | -5.15924 | -37.96729 | 2024-10-01 03:47:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71636faf-25ec-3235-937a-69d074b73e9f | -5.10254 | -37.66684 | 2024-10-01 03:47:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ce1d82ca-5c2f-39f6-810f-f3183ed3d183 | -4.64482 | -37.9058 | 2024-10-01 03:47:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 91afc808-338a-3a5e-b059-594c3e9eb394 | -9.97586 | -42.33369 | 2024-10-01 03:47:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a325b34f-e13d-3814-8eb1-212cc0655e4e | -9.76146 | -41.88158 | 2024-10-01 03:47:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2cf6a940-da96-3e75-a0d0-25ac8769ed5d | -9.571 | -40.34769 | 2024-10-01 03:47:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b875f53-b11a-3307-bfc7-59a3164b831d | -9.56742 | -40.34708 | 2024-10-01 03:47:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a8f9e07-8770-3ad6-99c0-40ac6d1507b6 | -9.4693 | -40.39548 | 2024-10-01 03:47:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aeead98a-a547-359f-af5e-4ac1d0c01b32 | -9.27295 | -43.46164 | 2024-10-01 03:47:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b76a5a9-fc67-345e-bcb0-f5728d40ee74 | -9.26864 | -43.46078 | 2024-10-01 03:47:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fea2e097-e8dd-3106-9abf-51c83cb8b235 | -9.25694 | -40.81775 | 2024-10-01 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 176c8722-9dc9-3a46-8c45-a6c46222fc42 | -9.25253 | -40.82149 | 2024-10-01 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 42b51df1-6ff3-3cf9-904d-4081d3a23a90 | -9.25179 | -40.82586 | 2024-10-01 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 202c550d-013b-35ae-a11b-25308b4b31ef | -9.24885 | -40.82085 | 2024-10-01 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 45d1cda3-583d-3f45-9585-39c0533c3b86 | -9.24811 | -40.82522 | 2024-10-01 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8d644b1e-34bd-3ddf-a07f-74838fef5208 | -9.01827 | -40.57064 | 2024-10-01 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9733182c-6efd-37d8-9088-5aeded75e798 | -8.94259 | -40.59733 | 2024-10-01 03:47:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a72ebe70-c9dd-339d-b8d4-d6e67c358f16 | -8.92615 | -41.19479 | 2024-10-01 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b4f93c22-40bd-3c23-8d6a-36e58d4eacfe | -8.48554 | -40.56745 | 2024-10-01 03:47:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a4009580-d4cd-3b06-8557-3ad33cc4b31f | -10.71101 | -39.7911 | 2024-10-01 03:47:00 | NPP-375D | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3fe34667-f6d9-3f0f-b8cc-7d56fb831909 | -10.55916 | -40.13712 | 2024-10-01 03:47:00 | NPP-375D | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0cae6a0-7b70-3ee4-8b5d-3accb2756dda | -8.04315 | -41.06731 | 2024-10-01 03:47:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b82f530-1480-3738-b26b-b177fdc7acda | -7.85583 | -43.09103 | 2024-10-01 03:47:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README43.md)
