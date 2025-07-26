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
| 69bce8c4-68e8-3b59-aa2e-a6f8106777e3 | -19.37901 | -44.79778 | 2025-07-26 12:14:00 | TERRA_M-T | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d65fb13f-30d0-31e0-8fe5-876339def4ad | -15.35655 | -43.16325 | 2025-07-26 12:14:00 | TERRA_M-T | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 4e6ec992-194d-328a-b0ee-2eb14f648645 | -17.13541 | -47.74063 | 2025-07-26 12:14:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0390eb8c-2679-3d24-97d0-fb7eca10b39e | -13.52253 | -45.51146 | 2025-07-26 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 17fdf6e9-a8c3-3728-bc6c-7be22fa6c602 | -14.21992 | -43.9503 | 2025-07-26 12:14:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cf891809-8672-323d-abba-dbeb4832f875 | -13.24695 | -51.12995 | 2025-07-26 12:14:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5597ae22-7814-374e-8ee5-ca27c859a037 | -16.12401 | -47.40374 | 2025-07-26 12:14:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 2f8ef533-d491-33e5-b867-29bf61a8c9ed | -17.81323 | -44.46012 | 2025-07-26 12:14:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7345e88-8f39-36e0-92a4-9e4386bec304 | -14.65911 | -42.25113 | 2025-07-26 12:14:00 | TERRA_M-T | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 042940fd-9ad1-3b0e-9fa7-ef7cbf33e5b1 | -14.94625 | -46.94008 | 2025-07-26 12:14:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 29fb960c-a4e8-3dda-81dd-d56f9f65f99c | -17.57775 | -47.50098 | 2025-07-26 12:14:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cf872c3b-0e05-3d82-8766-3c094511e6d2 | -18.38985 | -44.19424 | 2025-07-26 12:14:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7721db1-8b36-3eb3-b8c1-2624d507862b | -14.94349 | -46.95882 | 2025-07-26 12:14:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 59d65ae0-a755-34d8-9b17-48aee3eef994 | -14.95396 | -46.95656 | 2025-07-26 12:14:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| fb77d8db-d5d3-3ebe-a181-ac30f546577b | -18.44052 | -47.34819 | 2025-07-26 12:14:00 | TERRA_M-T | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c44bec1-9d3a-3ba7-89df-59516c52ce38 | -22.26722 | -55.98774 | 2025-07-26 12:14:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 31.5 |
| c2919106-30d1-3e23-9e40-18d95f7c74f1 | -15.35825 | -43.90982 | 2025-07-26 12:14:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6566c533-5095-354a-bb2a-a8f7d3a145f7 | -14.94488 | -46.94937 | 2025-07-26 12:14:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 31e43928-2afa-3dcd-b792-5c889b28cbce | -14.68573 | -52.67844 | 2025-07-26 12:14:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 379e5e15-d9cd-3bff-8d74-7943bfc68d29 | -13.5075 | -45.49088 | 2025-07-26 12:14:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| a5270f7b-64aa-39fd-b4ac-6c867413cb23 | -16.10976 | -48.04517 | 2025-07-26 12:14:00 | TERRA_M-T | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aa0f8592-aa3c-3f06-8735-7dcb6b4432da | -29.83047 | -51.1133 | 2025-07-26 12:17:00 | TERRA_M-T | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 9.5 |
| c175c088-9516-3feb-8adc-15797034526e | -29.82878 | -51.12421 | 2025-07-26 12:17:00 | TERRA_M-T | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| c237b61c-5503-3538-8827-9f3e15dc3c93 | -13.5081 | -45.4873 | 2025-07-26 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 92b597e2-3958-3008-b488-47ad5ab51f81 | -13.5081 | -45.4873 | 2025-07-26 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| f8c58bc3-2242-3754-883e-4ecad84efbea | -6.6758 | -58.8654 | 2025-07-26 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 213.7 |
| e2ff4c91-564c-3cf0-b7cc-c70197398f58 | -13.5081 | -45.4873 | 2025-07-26 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 3c52a237-c849-3e49-9a9b-127b1ca206f9 | -6.6758 | -58.8654 | 2025-07-26 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 225.0 |
| 50a56cf2-0fef-35b2-bda0-82f246650c71 | -13.5081 | -45.4873 | 2025-07-26 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 3a8569f9-2686-3683-94e2-0ea6cbc3b3d6 | -10.6714 | -46.6279 | 2025-07-26 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ef7a56df-8fb6-30b3-b786-dc285cd66531 | -6.6758 | -58.8654 | 2025-07-26 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 213.8 |
| 7afc87a5-a58e-34c0-beba-26b01e1a6f53 | -6.6576 | -58.8274 | 2025-07-26 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 287.1 |
| f764f805-bb2f-3063-8d1f-54729b96a4c4 | -10.6714 | -46.6279 | 2025-07-26 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 2e5f0909-6d63-3ed9-a3fd-de027bd29a8e | -6.6206 | -58.8483 | 2025-07-26 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 569.6 |
| 51675f86-d9b4-3932-b12c-29b95129c3fc | -6.6207 | -58.8289 | 2025-07-26 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 322.9 |
| c04ad77b-40e4-3a28-a588-40e5d469c530 | -6.676 | -58.8267 | 2025-07-26 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 0fb036a6-fcad-368c-b9c2-5849050beb2f | -13.5081 | -45.4873 | 2025-07-26 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9bf9b5d9-4887-3b86-b779-5bf932d99cd1 | -6.8764 | -43.685 | 2025-07-26 13:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 57ea1e12-4be5-345f-9905-ace64cf9a99c | -6.6205 | -58.8676 | 2025-07-26 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 204.4 |
| c16f7c10-1a1f-39b0-9e06-dfedfe578a1a | -6.6391 | -58.8282 | 2025-07-26 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 511.8 |
| 9ffe5114-b2ea-3031-93b4-c4e62b9959e4 | -6.6207 | -58.8289 | 2025-07-26 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 338.1 |
| c1da64db-2177-3bbf-b05b-9f2ac598adbe | -6.6206 | -58.8483 | 2025-07-26 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 564.3 |
| 8bfb04aa-578d-3893-9b89-4aa06c87e1d2 | -10.6714 | -46.6279 | 2025-07-26 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 4cad75c6-4df5-387a-81ea-d70e37bd168a | -13.5081 | -45.4873 | 2025-07-26 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 725dc208-ad62-3d1d-9f2b-cc698cf5a241 | -3.4367 | -43.1298 | 2025-07-26 13:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| cc79e7b8-9a20-388a-ad16-0c41a088fa7d | -6.676 | -58.8267 | 2025-07-26 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| a81729fc-a217-3efb-9c39-cb1d38b37a0d | -6.6205 | -58.8676 | 2025-07-26 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 205.5 |
| 7ac702de-40ff-369b-a6cd-5930c3293f20 | -6.6576 | -58.8274 | 2025-07-26 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 298.5 |
| 62952324-9935-3c5e-8b08-0517b00912e9 | -3.4366 | -43.1532 | 2025-07-26 13:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5f13a281-dbb1-3cd1-b8f7-3e7eddc87261 | -6.6391 | -58.8282 | 2025-07-26 13:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 474.7 |
| 94ae1f4e-55a8-310a-a58d-05819b241a31 | -18.4011 | -44.1853 | 2025-07-26 13:10:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 70a4de0d-a592-327e-b641-887a796e11ae | -10.6523 | -46.6303 | 2025-07-26 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 57a24a49-f82c-3823-9d25-c7fef4beda1d | -6.6391 | -58.8282 | 2025-07-26 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 401.6 |
| d86e1fde-cb2c-36a9-af14-bb79fe39b26b | -6.6576 | -58.8274 | 2025-07-26 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 235.8 |
| 543add36-619a-3e7d-a51c-8a83ff872bd4 | -3.4367 | -43.1298 | 2025-07-26 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 60dfd037-4a0d-3512-95fc-eba1c314669a | -6.8764 | -43.685 | 2025-07-26 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a495b051-2808-388d-9f64-4f4a4247ca74 | -6.676 | -58.8267 | 2025-07-26 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 6090447b-f992-337c-bdce-41616ebc2b29 | -6.6206 | -58.8483 | 2025-07-26 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 599.8 |
| 7556d735-3aa3-30f8-9d66-51859d77610e | -6.6205 | -58.8676 | 2025-07-26 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 3db8c900-7459-3326-866f-651cf483204a | -2.8626 | -42.2384 | 2025-07-26 13:20:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d198372f-d81b-37a6-86f1-88e048d0e90e | -10.6714 | -46.6279 | 2025-07-26 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| ec424d82-d805-3918-affe-debb643ddf82 | -18.4011 | -44.1853 | 2025-07-26 13:20:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| e6dbd317-d1a6-3dd1-bed8-5af6cf2c4c78 | -3.4366 | -43.1532 | 2025-07-26 13:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| f58ebc02-dc01-3cc3-ae44-4d377ee756c9 | -6.6207 | -58.8289 | 2025-07-26 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 350.3 |
| 620dfa99-ddb8-31d2-8c3c-8506c65ddb0a | -6.6206 | -58.8483 | 2025-07-26 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 520.6 |
| abe33a2a-3a5c-32fa-97d2-236970891a75 | -7.2956 | -60.1882 | 2025-07-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c2fa430a-4ced-3a3e-b7d6-c5589876a7e2 | -13.5081 | -45.4873 | 2025-07-26 13:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 0f0b7381-30b7-318e-917f-c67205a102ec | -6.676 | -58.8267 | 2025-07-26 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 139.1 |
| 0a18951c-d19d-3dde-9011-832d93e7305a | -3.4366 | -43.1532 | 2025-07-26 13:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a26038aa-6888-3bac-b7a7-209afb6881e5 | -6.6391 | -58.8282 | 2025-07-26 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 479.0 |
| 00733e93-91b4-3c4c-b46c-a492679c89a6 | -18.4011 | -44.1853 | 2025-07-26 13:30:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 120.7 |
| fa7160c5-baf7-30f1-a84d-8205f1649498 | -6.6207 | -58.8289 | 2025-07-26 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 361.0 |
| bc21a867-efe4-37d1-b61e-be076cece767 | -7.2957 | -60.169 | 2025-07-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fa9df39e-a594-3032-9032-78706f765a8d | -10.6714 | -46.6279 | 2025-07-26 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e84b7c9e-2468-39c5-baf8-801d1afd25e6 | -10.6523 | -46.6303 | 2025-07-26 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| dc9e66fd-4aac-347f-b717-927b9e9520cd | -3.4367 | -43.1298 | 2025-07-26 13:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| dd2793b7-6d5b-388d-a99b-6f34685096be | -6.6576 | -58.8274 | 2025-07-26 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 289.0 |
| cc55fc9f-2665-3cbc-8b39-53b9193cecfb | -6.6207 | -58.8289 | 2025-07-26 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 394.1 |
| 58da3843-84db-3878-9d50-2579f907a11f | -7.2957 | -60.169 | 2025-07-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| ead9de49-d5f1-3e6a-8eb1-cb219d583504 | -3.4367 | -43.1298 | 2025-07-26 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ee1c1239-233f-39b4-a45f-00b6de7c3acb | -7.2956 | -60.1882 | 2025-07-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 6c2bf4cb-faa3-31b7-8253-458da15d38e5 | -18.4011 | -44.1853 | 2025-07-26 13:40:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 112.7 |
| b7e3a108-228f-36f6-86ab-308c21853687 | -6.6391 | -58.8282 | 2025-07-26 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 416.5 |
| 1671e90a-ecc2-3986-a057-5c3ab13c8f4c | -6.6206 | -58.8483 | 2025-07-26 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 584.5 |
| 153de15a-c4e7-32b7-b925-97f08a0b81f6 | -6.6576 | -58.8274 | 2025-07-26 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 266.7 |
| 1dff7ec0-914a-3a13-8924-b1b62a9c0d26 | -6.5377 | -45.6126 | 2025-07-26 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6cf23045-bbfe-3f48-9736-1b822cc87581 | -3.4366 | -43.1532 | 2025-07-26 13:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9ab0492e-b28e-368b-9321-3caa3d8a4e3e | -6.676 | -58.8267 | 2025-07-26 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 137.4 |
| b1354deb-9180-3194-b523-2c6ee97a25b6 | -7.2957 | -60.169 | 2025-07-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 855727e2-b84d-3967-b9bb-f91ff126edb1 | -10.6714 | -46.6279 | 2025-07-26 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b06e47bb-3d49-34d3-a1b3-d0efc799dc70 | -6.6207 | -58.8289 | 2025-07-26 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 392.2 |
| 3ce759e4-5356-308f-b5d0-3a5b2c0be620 | -7.2826 | -39.6224 | 2025-07-26 13:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 236.6 |
| 115dcf26-0514-3aff-aa87-1086d4303452 | -7.2956 | -60.1882 | 2025-07-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f5f4a23d-13a9-3ebc-b2c6-855f97db7f56 | -7.2823 | -39.6474 | 2025-07-26 13:50:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 144.0 |
| 5a4ff5b4-2425-3be2-b79d-de25eba25af9 | -6.6391 | -58.8282 | 2025-07-26 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 527.8 |
| 20f3b64c-3c75-3a07-adbe-06d15a5e8074 | -6.676 | -58.8267 | 2025-07-26 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 155.4 |
| 672b1b17-e91f-36e2-ac56-5ba173846e96 | -6.6576 | -58.8274 | 2025-07-26 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 346.1 |
| c0b95b1d-f1e7-321e-ab03-60a1efb8b6c6 | -6.8764 | -43.685 | 2025-07-26 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 9a9c5170-a294-387e-abf6-4d07756d0bb0 | -11.5775 | -44.8645 | 2025-07-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| acd0c7ee-b127-3c82-8fbc-8b26401e7f38 | -6.5613 | -41.5135 | 2025-07-26 13:50:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 205.7 |


[Clique aqui para ver as próximas entradas](README34.md)
