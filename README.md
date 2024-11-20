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
| f2b803bb-9d32-3af7-8ea3-3b4f7c27db0d | -2.9969 | -45.436 | 2024-11-20 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 214.3 |
| 8e81896f-c373-328d-870f-31a03ed8698f | -3.4936 | -50.319 | 2024-11-20 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7926752c-4b7f-37e0-bc99-20bdb0a9e827 | -4.1683 | -45.4971 | 2024-11-20 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 4cb135cc-f081-3c3e-9d48-ddb6c343dab8 | -3.3131 | -45.4013 | 2024-11-20 00:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 89.1 |
| efd6011f-c394-3d26-878f-420e3e4ae4c0 | -3.802 | -47.8104 | 2024-11-20 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d93d0bf0-bcf4-3823-a8c4-b02e0f16fe71 | -4.3959 | -47.7618 | 2024-11-20 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 602ea206-1aa2-34ba-b358-8fd5a4a853d1 | -3.011 | -51.0028 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| aa4db100-3851-3d22-9fe6-ad7c9c2fa60f | -3.0109 | -51.0236 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 28f0d9de-cc12-39b6-a3c2-95ee0a91b016 | -2.6212 | -51.7997 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 7e40b6f3-4a8b-32a3-ba0f-b1369b3ac3d8 | -17.1362 | -57.5041 | 2024-11-20 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.1 |
| e1a1cbde-5a05-362e-a341-33666939536c | -4.5429 | -48.0151 | 2024-11-20 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 1d5c801a-3abc-34f7-9f0b-19e31607e359 | -4.0671 | -46.8586 | 2024-11-20 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3f2350db-e1f6-3323-bd05-f6149281f298 | -1.4709 | -47.1163 | 2024-11-20 00:00:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a9a4f4c2-5d3a-3730-b1bd-c17797c05967 | -2.9117 | -53.0403 | 2024-11-20 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c1c43839-bf1f-3d71-bb72-66b2a1c38900 | -14.3409 | -51.5092 | 2024-11-20 00:00:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 0bc8c6d9-899d-3d54-addd-66621148525e | -2.0092 | -46.6004 | 2024-11-20 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3351987b-6e09-368c-9de3-a22ab8cb426a | -4.1682 | -45.5195 | 2024-11-20 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 657b5b9e-fa1c-37aa-9b1d-a8f10cba1409 | -4.1861 | -45.6308 | 2024-11-20 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3219b45b-05bf-3e85-bbe7-5b1734d35310 | -4.459 | -46.5966 | 2024-11-20 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| c63df052-f99b-31be-962a-6e30c029ffc4 | -3.4752 | -50.3196 | 2024-11-20 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 8bc81a5b-cb1d-3865-97a6-68d6466087bb | -3.0155 | -45.4353 | 2024-11-20 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 146.6 |
| be721e54-b755-3d17-a55b-068541fc46a1 | -3.3088 | -50.3671 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| a59ce4eb-e5cb-30aa-94f6-384db0292915 | -1.9907 | -46.6008 | 2024-11-20 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| e1648ab3-5b7f-3624-9bb2-95c640627b89 | -11.1109 | -54.6204 | 2024-11-20 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 38306e8e-2eff-302d-9603-66d908445284 | -10.9613 | -51.5059 | 2024-11-20 00:00:00 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f746939f-8640-32d8-959c-6a9c57cb93f3 | -0.947 | -51.724 | 2024-11-20 00:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ec29904c-6b1f-3ad4-9a9b-3b3cfb04729e | -2.6028 | -51.8001 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b774e916-6a62-3559-8519-20b8dc802fdd | -3.3739 | -44.4247 | 2024-11-20 00:00:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 1c63aaa7-c0bd-3ead-9114-b81d679cbcd6 | -2.6212 | -51.8203 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4e24081b-0226-39f1-8eec-5f0fb763ba52 | -3.0901 | -54.6672 | 2024-11-20 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a26d96a9-de25-32fb-830a-368c239b8371 | -2.93 | -53.0601 | 2024-11-20 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 510fe4e7-d98f-3c2e-b449-84e6b704c4db | -16.9012 | -57.5108 | 2024-11-20 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 60d16de4-1c51-3cd5-a5cc-c1fa759893ca | -3.7858 | -44.0622 | 2024-11-20 00:00:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 56ceb249-1433-32a4-b790-f81913ea015e | -3.2708 | -50.6196 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| be347bf6-c400-37a2-974f-8580000152ae | -4.4592 | -46.5745 | 2024-11-20 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 123.2 |
| b6dcaf7e-cc78-39f7-bdfb-44b71bcb671d | -14.3219 | -51.4904 | 2024-11-20 00:00:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d7c79d30-8be2-369c-99b5-c80a0bcc1dbd | -15.3025 | -56.5268 | 2024-11-20 00:00:00 | GOES-16 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e0763986-95ba-3178-904b-1a7a3e4bd275 | -2.9116 | -53.0606 | 2024-11-20 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 56506c86-46f8-3f99-911b-0d3cbb3e57e9 | -4.0672 | -46.8366 | 2024-11-20 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 3585f0c5-986c-371f-b834-eb23c9420b11 | -1.4524 | -47.1166 | 2024-11-20 00:00:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| fe28a66a-1335-33f6-b648-53cd94b622db | -3.1477 | -49.1251 | 2024-11-20 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 6433814a-5225-3724-a9d0-d984a1009f6f | -4.5614 | -48.0141 | 2024-11-20 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| b4803d9f-6f06-3028-8352-ffd269131cd9 | -3.0154 | -45.4577 | 2024-11-20 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 883454f4-d057-3b26-931e-60ca10e15212 | -4.4405 | -46.5754 | 2024-11-20 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| e8f5cb6f-7973-3d92-9463-76eba2ae3c27 | -2.6397 | -51.7992 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| bf5640f2-9b00-327c-8e28-3793030506d8 | -11.1106 | -54.6408 | 2024-11-20 00:00:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| df0a6ce1-a2fe-30ce-b565-3933c76a92d1 | -4.4404 | -46.5975 | 2024-11-20 00:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| a6f306c6-1f68-3cc1-bc7f-6f2e914b0f49 | -14.3413 | -51.4878 | 2024-11-20 00:00:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| e284c393-dc96-3478-a6f1-77da5e6fa15e | -3.2014 | -54.3243 | 2024-11-20 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 60229f7a-22b3-3958-868d-8edf169b619d | -2.9968 | -45.4584 | 2024-11-20 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 5d26bb66-e309-3c2c-b4b1-ffdd92c350a8 | -14.3216 | -51.5118 | 2024-11-20 00:00:00 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 07436d3a-e6cd-3e89-8f5a-23869dfd255e | -3.1292 | -49.1257 | 2024-11-20 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| e59f375b-1644-3663-b39e-b5c9fd38d9d5 | -2.6213 | -51.7791 | 2024-11-20 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 1e2f708e-ce5d-3699-9317-b19110df572a | -2.2134 | -46.485 | 2024-11-20 00:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e5f20b1e-a8bf-36c6-8b12-23d25819f5f0 | -6.5332 | -44.1779 | 2024-11-20 00:00:00 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 5b9d8ba7-e928-369e-a008-4652378fa8fe | -2.99 | -45.43 | 2024-11-20 00:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 862e2700-2681-324a-b813-eb1b79542b27 | -1.4082 | -46.7934 | 2024-11-20 00:09:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71fdf0c4-a412-3e1c-b66c-49749c6d2d61 | -6.8915 | -39.551399 | 2024-11-20 00:09:00 | METOP-B | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6beed2e4-fc3c-3f5b-b510-bdff396833af | -1.256 | -53.385799 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9f12ac-492d-33ef-b32d-14ceeea5953a | -4.1474 | -45.5075 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 307845ea-975b-3ef4-aa28-4c634a0803e0 | -2.7013 | -46.085499 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bfa8931a-2ac1-3626-bda6-86dc67696834 | -2.3083 | -46.858501 | 2024-11-20 00:09:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c455ff4-96b1-31b8-b57c-c7510a6cedda | -10.4136 | -44.484901 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 46c88232-aadc-3f7c-bb44-8f7a907813d8 | -3.4522 | -48.2528 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2db7e661-a25c-3e5a-8335-4654ac0e535d | -2.5699 | -45.591999 | 2024-11-20 00:09:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e2bae99f-e01e-3702-8483-aef838201db0 | -9.9223 | -44.494701 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ff44ae80-40b1-3b96-b0af-b8453c192287 | -9.4207 | -39.030899 | 2024-11-20 00:09:00 | METOP-B | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 92a1a88d-20c8-3077-a237-496c062d5e77 | -2.8329 | -46.673 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34327a19-756c-3264-9793-4836f0ac56eb | -14.3056 | -51.458801 | 2024-11-20 00:09:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92db221c-42de-317f-95c9-539d8891b33c | -1.4098 | -46.800701 | 2024-11-20 00:09:00 | METOP-B | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23e433e3-5dc9-3b90-9d2f-b458aaaf6133 | -3.0777 | -45.972801 | 2024-11-20 00:09:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8e51ee9a-597f-3730-9e05-3fa5a4fcf7e1 | -3.218 | -48.8638 | 2024-11-20 00:09:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebf3bdc-4d23-3b2e-bb14-b9ac891ef632 | -3.6894 | -43.4734 | 2024-11-20 00:09:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5382f07a-4959-3ed7-abfc-c7bb5949b095 | -2.6272 | -46.2141 | 2024-11-20 00:09:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c56a96e5-d150-3842-93ce-2159b336e4d2 | -4.5477 | -48.005699 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 067bd573-6a17-30bf-8e47-6cc9a8ebcbbf | -10.412 | -44.4776 | 2024-11-20 00:09:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc3e8b30-145d-39b3-9c07-2c31ca831109 | -6.5282 | -44.180599 | 2024-11-20 00:09:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 337fde1b-1e2d-3429-93cd-303f20040418 | -1.2462 | -53.387901 | 2024-11-20 00:09:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dffacc5b-ff03-3cd4-9899-3e12ab6f0014 | -1.69 | -46.1231 | 2024-11-20 00:09:00 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a6cd9951-0a79-3d86-bc7c-12f00278ff58 | -3.0338 | -45.1353 | 2024-11-20 00:09:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74efd7f6-2ae2-37b7-91b4-24acfb4cd25f | -4.5458 | -47.996799 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6e583b-ef23-3e82-98b6-92d1ac6de834 | -3.2881 | -49.0415 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c80f4c-cf6a-3b20-a49a-b10203bc162c | -3.4503 | -48.2439 | 2024-11-20 00:09:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdca9430-89a8-37fb-8588-280da6c9243e | -5.2338 | -42.647301 | 2024-11-20 00:09:00 | METOP-B | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a67a3a91-4d4e-34bb-98e2-b5643b61de06 | -2.8154 | -45.126099 | 2024-11-20 00:09:00 | METOP-B | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e94b8d84-cfc8-35b8-9103-15e69c5853b5 | -2.6713 | -46.226898 | 2024-11-20 00:09:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 681e6cc6-6c5e-350f-91cb-1cfae9bf54f5 | -4.5379 | -48.007801 | 2024-11-20 00:09:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4141ddf6-e453-3270-b122-fe15da572b03 | -4.2305 | -53.634399 | 2024-11-20 00:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3ffcc83-708a-3eb6-ada8-30b914a34d25 | -1.4925 | -47.443802 | 2024-11-20 00:09:00 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e799461-4729-3ce9-816f-1da8687150e5 | -4.7666 | -46.485199 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0783439d-fbbb-3e78-9839-2a0030cbd351 | -3.8481 | -44.2668 | 2024-11-20 00:09:00 | METOP-B | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed0ff9bf-af84-3f13-aa24-b9b58a2a9cd6 | -3.7292 | -44.013699 | 2024-11-20 00:09:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 546d3f42-3a3f-37e6-8580-f94692d2e234 | -3.7909 | -47.787899 | 2024-11-20 00:09:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6652b6f-d6f8-3ebc-b0ca-5e5571e99f26 | -6.6562 | -40.310902 | 2024-11-20 00:09:00 | METOP-B | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fa2690a9-488e-356c-a26a-f4ab2d88a818 | -3.0152 | -45.3269 | 2024-11-20 00:09:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d626052-b92a-3f06-b16e-5bb3e8cdee08 | -4.4284 | -46.583099 | 2024-11-20 00:09:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d80e9ef-1353-386a-a06f-57cfae922946 | -2.9195 | -49.4156 | 2024-11-20 00:09:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84f03003-d078-3390-9349-134393f97806 | -2.9907 | -50.988499 | 2024-11-20 00:09:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08c5a2df-08e6-3db4-bdc1-00198187293e | -5.3761 | -40.66 | 2024-11-20 00:09:00 | METOP-B | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0581c59e-cd3c-3b07-b0fa-f6a84d0e3890 | -9.0049 | -44.345798 | 2024-11-20 00:09:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
