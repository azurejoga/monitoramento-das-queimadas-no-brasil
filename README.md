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
| 5088a638-d431-3fbb-8ba8-bcd7268d3d9e | -17.0 | -56.84 | 2024-10-06 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 258027fd-4e91-3804-9b7d-b57947f50d0b | -17.0 | -56.76 | 2024-10-06 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81a414a1-5004-373d-a95f-f8a981ded39d | -17.03 | -56.86 | 2024-10-06 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8bea1cf5-470b-37cd-9937-43242fc0a7ba | -17.03 | -56.78 | 2024-10-06 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0afdb4fd-0b39-3810-b9d8-febae1fa17aa | -9.34 | -46.57 | 2024-10-06 00:04:31 | MSG-03 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6785164e-b326-3c65-81d5-097c358950ab | -5.58 | -44.89 | 2024-10-06 00:04:55 | MSG-03 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26a7e5d5-b9ae-31dc-af5d-a411572d4059 | -3.79 | -41.61 | 2024-10-06 00:05:05 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 486a2fd7-c6cc-3b5e-9dc9-ee5d524de096 | -1.5486 | -54.775 | 2024-10-06 00:05:15 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| fc2cce80-83da-378e-a16e-a6d1eaaa6269 | -2.6858 | -49.0752 | 2024-10-06 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 26a741f7-0647-3489-bbf3-5b342ad4ebb3 | -2.6859 | -49.0539 | 2024-10-06 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2a901501-2b99-356f-85db-62344a445d49 | -2.7043 | -49.0747 | 2024-10-06 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4dd1113d-bcda-3518-b21e-cf27cbf62625 | -2.7043 | -49.0533 | 2024-10-06 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| d706bf39-f8b3-3730-8708-758efe1a88b2 | -2.8166 | -48.6867 | 2024-10-06 00:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 69f6da6f-9fbb-306b-8682-6f84f0af3872 | -2.847 | -50.4648 | 2024-10-06 00:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b0da6b3c-813d-36cb-96bc-a60364101936 | -3.1053 | -50.4573 | 2024-10-06 00:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 86af24c3-ae9e-30e3-89bd-d7f99a14a83e | -3.3084 | -50.451 | 2024-10-06 00:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| f98973ba-2a7a-3160-95dc-ffecd56c5bde | -3.8008 | -41.5989 | 2024-10-06 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| 93e95050-8c2f-3980-9dc5-e83dd13864c0 | -3.801 | -41.575 | 2024-10-06 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.3 |
| 0169fc36-9e37-326c-a659-ddd487b628de | -3.8196 | -41.5979 | 2024-10-06 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.6 |
| 07726b94-55ef-3f1c-9ec2-11231e297254 | -3.7935 | -49.4636 | 2024-10-06 00:05:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 66edbd8f-66ab-3abf-a5d5-a2dbbb1f8bfc | -4.4534 | -47.4757 | 2024-10-06 00:05:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 084baee8-a689-31f6-97d6-ea5892c84b9d | -4.4536 | -47.4539 | 2024-10-06 00:05:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 62a23a16-df95-3cc8-9cbd-9c6a8c086dc2 | -5.5716 | -44.8927 | 2024-10-06 00:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| f30a1589-5b1f-3fd2-a9f8-335f4817ce82 | -5.5718 | -44.87 | 2024-10-06 00:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| a7572c9f-ad63-39e7-8a2c-159194031efc | -5.5903 | -44.8914 | 2024-10-06 00:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c711471e-9b58-372a-a90c-2946df6d5d96 | -5.5905 | -44.8687 | 2024-10-06 00:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 5e8227c3-4f3a-3a9b-88f7-240df1df1b4a | -5.8214 | -44.1426 | 2024-10-06 00:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 7a46391e-afeb-388c-a7a3-c2fe4a9de404 | -5.8216 | -44.1196 | 2024-10-06 00:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 2075a4ef-e953-381d-8481-877d2cdb091d | -6.9513 | -59.0859 | 2024-10-06 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| bd1f73fe-d6e6-39d0-b9bc-9a00a09b954a | -6.9514 | -59.0666 | 2024-10-06 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 9131331b-d1d7-38dd-95ec-5ba561221bff | -6.9698 | -59.0852 | 2024-10-06 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| abf047de-c329-327a-8b04-a57e7b9f686f | -6.9699 | -59.0658 | 2024-10-06 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 69b69547-8248-3a44-bef9-12c7b55933f1 | -7.153 | -59.3092 | 2024-10-06 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 9d3ae9e2-92a1-3cb7-86be-19dbb6b3f280 | -7.1532 | -59.2898 | 2024-10-06 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c388a99e-cc9c-355b-aaaa-2f5061a4e67d | -7.3841 | -64.665 | 2024-10-06 00:05:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 58c03336-4306-3a98-a230-49bcac6435d6 | -7.4741 | -72.6801 | 2024-10-06 00:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 7e959a24-3050-3d59-89d4-a6cfe2b9f8d1 | -7.7301 | -49.8288 | 2024-10-06 00:05:50 | GOES-16 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bf31f2d1-5853-3e28-90eb-71be79059be0 | -7.9639 | -54.7764 | 2024-10-06 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 321ec154-05ab-3121-8a6a-98e358c92e3c | -7.964 | -54.7562 | 2024-10-06 00:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3df26026-1bf2-3a09-a514-52ee7598db26 | -7.9825 | -54.7752 | 2024-10-06 00:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 34da622c-2502-3759-a126-8e5f8abc93e1 | -7.9826 | -54.7551 | 2024-10-06 00:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 6db5c5e1-3615-3ea6-91f3-8c6cf0af1257 | -8.2138 | -61.2213 | 2024-10-06 00:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f4151028-0de0-35cd-8b9d-37fd46deee0d | -8.2139 | -61.2022 | 2024-10-06 00:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9fafbc28-d8b3-3c43-89fe-ec2fe395d11f | -8.2324 | -61.2014 | 2024-10-06 00:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| e35fac92-4afd-3cf4-a843-24c13e2a4496 | -9.269 | -48.1377 | 2024-10-06 00:05:58 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 85af8e7f-732d-3cb9-8f3a-041c4c7b00f9 | -9.1573 | -61.5803 | 2024-10-06 00:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| be6d75eb-891b-3a6c-aea8-c62931f5e95c | -9.1759 | -61.5794 | 2024-10-06 00:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 460ed0ab-73a0-32c5-ae7b-e84f5e2a86c7 | -9.176 | -61.5603 | 2024-10-06 00:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| fa48c00a-7d76-3fa3-bbbf-7f3357b1a9cd | -9.3464 | -46.5589 | 2024-10-06 00:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 250.7 |
| f9f1e69c-30b1-3d1f-b60b-2480e5921fad | -9.3467 | -46.5365 | 2024-10-06 00:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 253fb6b3-8272-3833-9f82-39e63a1ddcd8 | -9.688 | -47.8308 | 2024-10-06 00:06:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f5f02229-2b6f-3372-a398-c143f5de2d28 | -9.8552 | -60.2966 | 2024-10-06 00:06:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 80dfe1ff-5d7b-36a7-99e9-d279e139d030 | -10.2173 | -59.403 | 2024-10-06 00:06:04 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 3c2f4704-6b7b-3d0d-a3f6-6fe66d79b9a3 | -10.4235 | -50.7355 | 2024-10-06 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 170.4 |
| d33e5775-cca5-3ed3-bd2e-fd26185ada9c | -10.4238 | -50.7142 | 2024-10-06 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 6a366f26-1d60-318e-a995-97c77e2d7f86 | -10.4241 | -50.6929 | 2024-10-06 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c4e8669e-5aa7-3178-bf24-e7617fa26022 | -10.4424 | -50.7336 | 2024-10-06 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 69d2099f-f182-3d85-8847-9b7b79e89d09 | -10.4427 | -50.7123 | 2024-10-06 00:06:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 894cf95e-83f2-398e-8345-c197bd91b99f | -10.8153 | -44.7643 | 2024-10-06 00:06:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d18eba10-cb95-3b26-9ebb-ec091285f7de | -11.0901 | -54.7852 | 2024-10-06 00:06:09 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3b792096-1a37-3471-879b-da03b2917790 | -11.0966 | -54.2336 | 2024-10-06 00:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2bdbb304-0c7d-371c-b756-fc937507fa66 | -12.0211 | -63.7478 | 2024-10-06 00:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 163.9 |
| d948e01c-0b21-318c-aed5-a4606be24716 | -12.6089 | -53.1338 | 2024-10-06 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 129.3 |
| f6dbe23e-c93c-3943-80f1-e249d648f5d7 | -12.6092 | -53.1129 | 2024-10-06 00:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 530b505a-2c74-399f-b61f-4a09b34a4c72 | -12.628 | -53.1317 | 2024-10-06 00:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 227.4 |
| a82648c9-baee-3975-8327-a82e3a60ef81 | -12.6283 | -53.1108 | 2024-10-06 00:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 270.9 |
| cbf491dc-48d0-3c9a-a40b-81822ce3b834 | -12.6474 | -53.1088 | 2024-10-06 00:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 003ddeb6-9b5e-3718-8015-f466f2e1d6d9 | -12.6532 | -54.0415 | 2024-10-06 00:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 1322cb65-b819-3f5b-8860-ba9291e00b01 | -12.6535 | -54.0208 | 2024-10-06 00:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 3a855271-3a86-3f2b-85ab-a708b9d6a9f0 | -12.6723 | -54.0395 | 2024-10-06 00:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 738f7b7c-ac95-3d10-9999-6c3fa85199e5 | -12.6726 | -54.0189 | 2024-10-06 00:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| b313327d-e985-36eb-a2e8-30d25184115b | -12.7439 | -50.5376 | 2024-10-06 00:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a89b0be6-eb7b-30fa-a566-63faaa49c40a | -12.7627 | -50.5567 | 2024-10-06 00:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1d0177f1-c3da-341f-8931-de1870bee891 | -12.763 | -50.5352 | 2024-10-06 00:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 53f3001f-ba2a-3d20-b15b-ed95e424236e | -12.9375 | -62.489 | 2024-10-06 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 38106510-c706-37e7-b588-5f98cf359ce6 | -12.9377 | -62.4697 | 2024-10-06 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.0 |
| e8a83341-5576-316b-9020-4678b5eb166f | -13.3976 | -61.957 | 2024-10-06 00:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 8aae09db-91b5-346e-a0c0-d965ced82199 | -14.0767 | -45.1579 | 2024-10-06 00:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 4da6e0f0-9431-3cb6-9704-ad159eca97eb | -16.3959 | -57.3641 | 2024-10-06 00:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 29823da0-fb9c-3517-8001-0915be6d9b11 | -16.5745 | -57.16 | 2024-10-06 00:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 7dd9f951-be39-3c41-a563-40f1f25827cf | -16.614 | -55.9214 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 154.0 |
| d27190c3-aedd-3268-aa20-799c4027603d | -16.6143 | -55.9007 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 5ea242ad-a4c4-32ee-bd68-65c93bd99d7f | -16.6203 | -55.5476 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| 3f67657b-76f2-30a2-8c12-8f4aa322fff1 | -16.6136 | -57.1555 | 2024-10-06 00:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.7 |
| af6f8f8a-28e1-3d26-8447-b8aab044d24c | -16.6336 | -55.919 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 4cf94f04-57ed-30a6-8833-dc4e0bb6c653 | -16.6395 | -55.566 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 117.5 |
| 85b004ae-04fc-37a8-a99c-4002c2f112ab | -16.6398 | -55.5452 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 207.8 |
| c7b311bf-1852-352d-92c9-5f70388a8d8d | -16.6402 | -55.5243 | 2024-10-06 00:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 152.1 |
| 38c18d9a-2feb-3dd4-94ba-586cf54654f0 | -16.6868 | -57.4741 | 2024-10-06 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 203c7e78-b777-3a15-8d90-9a3889202cbb | -16.6871 | -57.4536 | 2024-10-06 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 86408ea1-a260-3a67-9ea3-b4f836748754 | -16.7067 | -57.4514 | 2024-10-06 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 7b4f78c8-07d6-3741-abc3-4d60f99e3ada | -16.7647 | -57.4856 | 2024-10-06 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.2 |
| 194ccd5a-b8ae-34b0-94c7-a77c8af1277b | -16.765 | -57.4652 | 2024-10-06 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 268436d6-9f1e-3a86-a2d4-93378bed6c05 | -16.7843 | -57.4834 | 2024-10-06 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| c246ce06-0e24-3951-b532-d98479bb9013 | -16.8238 | -57.4584 | 2024-10-06 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 13451e4f-f9ca-3b5d-acce-41c9efe3b5b4 | -16.9283 | -55.8405 | 2024-10-06 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 120.9 |
| 3901ae20-648e-39e9-8f10-1bf4995142ef | -16.9287 | -55.8197 | 2024-10-06 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| bf6a9230-0c54-339c-9a3f-4da174740854 | -16.9348 | -56.625 | 2024-10-06 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| 475abded-4e94-35ec-8ea8-f9bad6ea634f | -16.9545 | -56.6226 | 2024-10-06 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.2 |
| e9a37163-3f43-3194-861c-a8da9cad156d | -17.3837 | -42.6483 | 2024-10-06 00:06:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 79.1 |


[Clique aqui para ver as próximas entradas](README2.md)
