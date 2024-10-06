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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82a18b85-ad8d-3dd9-b8da-387544c84881 | -17.1571 | -57.4198 | 2024-10-06 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 65a5ce0e-42b4-3262-b264-a2e13bba4ed8 | -17.812 | -53.7859 | 2024-10-06 00:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 233.1 |
| ab14cf2c-1132-3154-97a2-55d1c61fa197 | -17.8125 | -53.7645 | 2024-10-06 00:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 782a24bf-6a9a-31b2-b35c-f67dc244646f | -17.8319 | -53.7829 | 2024-10-06 00:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 944fc452-7247-3288-9fb6-20a024066e94 | -17.8323 | -53.7616 | 2024-10-06 00:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 0a5a1131-a4e9-315d-b642-b5947f155c8e | -18.6586 | -57.2759 | 2024-10-06 00:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 9050f5a3-b50f-3f9b-b2ee-bc720695bf06 | -16.97 | -56.82 | 2024-10-06 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d13efc96-2385-3940-b801-f71531ffdba4 | -17.0 | -56.84 | 2024-10-06 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bec912b7-88df-35fa-bd94-159357b170d5 | -17.0 | -56.76 | 2024-10-06 01:03:48 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74f9ed75-00c1-346a-a861-e27b4795b9dd | -10.42 | -50.75 | 2024-10-06 01:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ad5b9078-0fef-35c1-aa3c-d3de58e92dca | -10.42 | -50.69 | 2024-10-06 01:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c787906d-ea8d-3932-8826-0f84f51f0cd5 | -10.45 | -50.76 | 2024-10-06 01:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eea81001-b2c4-389c-860a-88da4ba87209 | -10.45 | -50.7 | 2024-10-06 01:04:25 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ea88915f-2402-36ad-ae19-27086f53b500 | -2.7 | -49.06 | 2024-10-06 01:05:12 | MSG-03 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f2e4152-17a4-336e-89da-6c4c767c881d | -2.6858 | -49.0752 | 2024-10-06 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 231.5 |
| 300d2d36-de89-3c5f-94f5-ec405b075c33 | -2.6859 | -49.0539 | 2024-10-06 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 159.0 |
| 1939cbcb-8257-3b04-b26f-0138ce6a4386 | -2.7043 | -49.0747 | 2024-10-06 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 377e6368-107a-3c8f-803b-d27f999b96fd | -2.7043 | -49.0533 | 2024-10-06 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| e00ae2f9-d4a0-3b1c-828e-44a513307aed | -2.8166 | -48.6867 | 2024-10-06 01:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8ea849f2-d458-3eb3-a278-97118fec4f2b | -2.8169 | -48.601 | 2024-10-06 01:05:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| bd9657e4-73a9-3bf1-950c-f0651b985cf7 | -3.1299 | -48.955 | 2024-10-06 01:05:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c248c3ce-5a46-3ade-b07a-8bd140fbf354 | -3.2329 | -50.8504 | 2024-10-06 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| dd2ed4ca-e5f7-3fca-b365-4a9e249c7cbe | -3.233 | -50.8296 | 2024-10-06 01:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d0570b46-b502-3ebd-b04a-a618d5650d05 | -3.7068 | -41.6758 | 2024-10-06 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 345b10e8-8c6c-3e7c-a6d2-0fe0db404f77 | -3.7255 | -41.6748 | 2024-10-06 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 93d09e07-9b5a-3a04-b596-cc12a8aeff2a | -3.8008 | -41.5989 | 2024-10-06 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 199.9 |
| 0d263475-a6d5-3829-b8dd-5deaf8241f28 | -3.801 | -41.575 | 2024-10-06 01:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.5 |
| a09d837b-a8a3-3e11-863e-2932ed9d3598 | -3.7935 | -49.4636 | 2024-10-06 01:05:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a54c81b4-76f2-3eba-8169-5b7def50ac2a | -5.5716 | -44.8927 | 2024-10-06 01:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| dc68ac54-1699-3adb-bbda-e73fd65c731e | -5.5718 | -44.87 | 2024-10-06 01:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 370b58ab-5cea-3cfa-9a69-bd4d651a0f6a | -5.5905 | -44.8687 | 2024-10-06 01:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fa55ff6a-1d9d-3f38-9967-1c80e6228c9b | -5.8214 | -44.1426 | 2024-10-06 01:05:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 114.8 |
| ba820f56-d2e6-3ea8-a335-1c4e6b0f9613 | -5.8216 | -44.1196 | 2024-10-06 01:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 36b08e4c-c744-390f-97f8-71412e37c571 | -7.0574 | -35.0443 | 2024-10-06 01:05:45 | GOES-16 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 121.9 |
| 577b9b80-e8d1-357e-9c38-32c0d991c6bf | -6.9103 | -47.6916 | 2024-10-06 01:05:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| bdff5e5e-a380-32ba-a823-9aaff45bfbce | -6.929 | -47.6901 | 2024-10-06 01:05:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 8499d4c5-f4b4-32d1-b85b-edd067a8a543 | -6.9514 | -59.0666 | 2024-10-06 01:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 3371f988-ffa5-34f9-aa0d-cfa792c68373 | -6.9699 | -59.0658 | 2024-10-06 01:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0c1197ad-44e5-3ee4-b08b-178faf67f1b9 | -7.1532 | -59.2898 | 2024-10-06 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| db9a7e9c-721e-3b05-b36a-b57ec6a09fb5 | -7.4741 | -72.6801 | 2024-10-06 01:05:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 77d22f5b-14ee-3aa7-9ec3-4b3252865e0c | -7.87 | -54.8828 | 2024-10-06 01:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f00c9d85-2608-32e9-821e-940447556155 | -7.9639 | -54.7764 | 2024-10-06 01:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| aebac389-640c-3d8c-932a-c7b523a701e5 | -7.964 | -54.7562 | 2024-10-06 01:05:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 061f9482-2485-3b21-97ff-735a41bcbfd0 | -7.9825 | -54.7752 | 2024-10-06 01:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fa080f06-dc55-32c5-b1ce-7366d6d56f3a | -7.9826 | -54.7551 | 2024-10-06 01:05:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 58a7a991-d9b2-3620-a6a4-781d616936d5 | -8.2139 | -61.2022 | 2024-10-06 01:05:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1bde2e93-b3c0-34d9-bceb-994039e8c472 | -9.1263 | -60.6621 | 2024-10-06 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 412cb14d-07e1-381a-b708-318ea2676406 | -9.1449 | -60.6612 | 2024-10-06 01:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f8e27f67-3996-3af8-bcde-d99d17310b7f | -9.1759 | -61.5794 | 2024-10-06 01:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 37476dc5-9d05-3a23-85db-94cd70db7e54 | -9.176 | -61.5603 | 2024-10-06 01:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6cb97e0a-bf83-318b-8d64-551f86131c5d | -9.3275 | -46.5609 | 2024-10-06 01:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 044dd7cf-59ed-3b80-a6e7-34ac5c53c1fd | -9.3278 | -46.5385 | 2024-10-06 01:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 1c3e1107-e699-31d3-af82-70159e85b662 | -9.3281 | -46.5161 | 2024-10-06 01:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 956d06b7-bc52-3bb5-ac18-7bab538454c2 | -9.3464 | -46.5589 | 2024-10-06 01:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 9df1fb72-7feb-3b3e-8a23-f7e31e2ae4f8 | -9.3467 | -46.5365 | 2024-10-06 01:05:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| 9a57253f-1dad-310b-8c0d-e64f1d1a5115 | -9.3637 | -64.3378 | 2024-10-06 01:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e484c178-cf7f-3ca0-a097-aea4478663c3 | -9.3638 | -64.319 | 2024-10-06 01:06:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| eeb40ca6-698a-3e68-9a8b-27638f61c79d | -9.8552 | -60.2966 | 2024-10-06 01:06:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 57a605b6-e413-3396-9544-845e7396ea2e | -9.8802 | -59.5008 | 2024-10-06 01:06:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7c8c2190-2914-3c81-bff6-e01747509021 | -11.0966 | -54.2336 | 2024-10-06 01:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 1186252d-86cd-3bdd-867e-4e5f017578a2 | -11.1155 | -54.2319 | 2024-10-06 01:06:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0ed62de4-06ee-3f37-a932-f0747842c23a | -12.0211 | -63.7478 | 2024-10-06 01:06:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |
| e70629d9-4480-3989-862b-8124639f7883 | -12.5066 | -47.5705 | 2024-10-06 01:06:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dbd526f7-e648-3fd2-b9d6-3c920608ccf6 | -12.7089 | -40.2155 | 2024-10-06 01:06:17 | GOES-16 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 00f9feb8-4b2e-3414-9133-a33c20f4c5f1 | -12.6089 | -53.1338 | 2024-10-06 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5c3d1db2-0506-3b6b-b828-0a1aaa4f4a00 | -12.6092 | -53.1129 | 2024-10-06 01:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 61d31f29-e4a3-303d-9653-679e722a6043 | -12.628 | -53.1317 | 2024-10-06 01:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e5cfdd15-6f23-3c74-b74a-ce1de214652a | -12.6283 | -53.1108 | 2024-10-06 01:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 004cbe62-31b7-33f8-9919-780731b5feb0 | -12.6532 | -54.0415 | 2024-10-06 01:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| bbc34d06-0a98-351b-93a6-2d0ce413dfc3 | -12.7439 | -50.5376 | 2024-10-06 01:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| f3eb3134-29af-344b-befc-870692101b7d | -12.763 | -50.5352 | 2024-10-06 01:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 192.2 |
| ad730342-58e4-3cc1-b52e-6d6c04b4d8e9 | -14.5646 | -48.8217 | 2024-10-06 01:06:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 178.2 |
| 54bf3807-7cef-3c24-97fc-9c8ce6246e69 | -14.565 | -48.7995 | 2024-10-06 01:06:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8f38cb29-837e-3ed2-9b0f-30a4f4d5137f | -16.3764 | -57.3663 | 2024-10-06 01:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 7060d309-4df6-3c66-9aad-e18c1d1b2291 | -16.3959 | -57.3641 | 2024-10-06 01:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| c6db94ca-f13e-304a-9c6d-9a7f3ab98b6d | -16.4155 | -57.3619 | 2024-10-06 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 2846fa86-b993-3754-bb4d-efd5441b3a07 | -16.4158 | -57.3415 | 2024-10-06 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 1f83c76b-47fa-3490-8962-f583350394ab | -16.435 | -57.3597 | 2024-10-06 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 27cca64c-e516-3e6e-824c-9ef9673ff5fa | -16.4353 | -57.3393 | 2024-10-06 01:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| dc98833c-b598-300f-a967-00983bf2a54a | -16.5553 | -55.9287 | 2024-10-06 01:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 33853ac8-6d9f-300d-9981-383aeeab572b | -16.5745 | -57.16 | 2024-10-06 01:06:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 03f73fb2-9b2d-3d37-9418-11b398c3bf84 | -16.7067 | -57.4514 | 2024-10-06 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 36c3a7f9-d228-36a4-8556-c71e426f0d5d | -16.6398 | -55.5452 | 2024-10-06 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 160.1 |
| 57388022-227e-3ce2-9d9c-2f52970c64e0 | -16.6402 | -55.5243 | 2024-10-06 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.8 |
| 54afd7a8-9ee1-3983-9d7b-f63ca4ff74fa | -16.6594 | -55.5427 | 2024-10-06 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 8424e85f-045f-3df1-b97c-2ac8f91f716b | -16.6871 | -57.4536 | 2024-10-06 01:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 90e3b4f4-7d61-3813-8b1e-b23fdd264fce | -16.7647 | -57.4856 | 2024-10-06 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.9 |
| ab9ba862-7d32-313e-b34d-78f577d9dbd0 | -16.8238 | -57.4584 | 2024-10-06 01:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 406a9893-edf6-30ad-907a-4e90282a3b67 | -16.9283 | -55.8405 | 2024-10-06 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 3ddf2ed6-40b7-31b8-887d-2971a42dfbb5 | -16.9287 | -55.8197 | 2024-10-06 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.7 |
| 7b8f8754-c435-327d-9586-bf79f1dd8006 | -16.9348 | -56.625 | 2024-10-06 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 8f5ed914-8287-3ede-830e-7c3110d712cf | -16.9545 | -56.6226 | 2024-10-06 01:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 7cb3bd02-2167-3d77-80fd-8008ddb68807 | -16.9548 | -56.6019 | 2024-10-06 01:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| d758325c-e793-3238-9a7d-136de9167cba | -17.3837 | -42.6483 | 2024-10-06 01:06:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| a94039ed-ecac-339e-b22e-41b2899239ad | -17.0007 | -55.0607 | 2024-10-06 01:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 264332c5-fff9-3d6b-b66e-a5b2ee793bc7 | -17.0203 | -55.0581 | 2024-10-06 01:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 64249b59-424b-3173-a853-06acbf65a3b2 | -17.1182 | -57.4039 | 2024-10-06 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| fc270594-4e62-3a31-9bc0-b275f401b9b3 | -17.1185 | -57.3834 | 2024-10-06 01:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| d8565168-6a06-335a-881d-8087592ac51f | -17.1375 | -57.4221 | 2024-10-06 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.4 |
| f4ef8fa0-4dd8-3a71-a6ee-ad38999367cc | -17.1571 | -57.4198 | 2024-10-06 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |


[Clique aqui para ver as próximas entradas](README23.md)
