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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f78ede63-391f-352c-9aee-a77507f29f0e | -3.7068 | -41.6758 | 2024-10-06 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 93a9fa05-889b-3afc-942c-5caa92df505e | -3.7255 | -41.6748 | 2024-10-06 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 66a0163d-b3ef-37ee-bedf-005e4cbd80f2 | -3.8008 | -41.5989 | 2024-10-06 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 2172d406-b374-3b36-8e4f-0852cc3e7176 | -3.801 | -41.575 | 2024-10-06 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 10b22a8f-9da0-387f-a49e-8998fc39fe42 | -3.8196 | -41.5979 | 2024-10-06 01:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 08dba9ab-07ad-3296-bd80-5ccb2ae791f1 | -3.775 | -49.4643 | 2024-10-06 01:25:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 5b1e8e57-50bc-3a67-8de3-8d3aeb8ec66e | -3.7934 | -49.4849 | 2024-10-06 01:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8f2fc900-ee79-32bb-b9b2-7d7286aa50c2 | -3.7935 | -49.4636 | 2024-10-06 01:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 6361b537-51d3-3be5-8930-50679a243d83 | -5.5716 | -44.8927 | 2024-10-06 01:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 203fc812-a69c-3f30-8291-d8b27c024717 | -5.5718 | -44.87 | 2024-10-06 01:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 189c15b9-926c-3f5d-9f20-945bc5d4f507 | -5.5905 | -44.8687 | 2024-10-06 01:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| d32425da-4533-309a-b09e-e784558e51c4 | -5.8214 | -44.1426 | 2024-10-06 01:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| ce673bfe-380e-300d-9f6b-02057bb25b8a | -5.8216 | -44.1196 | 2024-10-06 01:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 480685fd-3a4f-3d1e-9607-16001738bede | -6.9103 | -47.6916 | 2024-10-06 01:25:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 42.2 |
| cc56e617-4a1c-3b1e-a688-8190ccf98127 | -6.9514 | -59.0666 | 2024-10-06 01:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 56475051-cfa9-3da1-9789-db80c5a3cff3 | -6.9515 | -59.0473 | 2024-10-06 01:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 5259df14-2525-3e5a-a6c1-9e2defba557f | -6.9699 | -59.0658 | 2024-10-06 01:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| ff3b793b-cad7-3b02-863f-15866571919f | -8.2139 | -61.2022 | 2024-10-06 01:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 09442ec6-980e-3e27-b7e8-79ffbfd342f8 | -9.1263 | -60.6621 | 2024-10-06 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| daa119ae-1a79-3455-9dec-e0adf4681c15 | -9.1449 | -60.6612 | 2024-10-06 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 139087bd-cec2-3cbf-b0cf-e9c5c12ba6e0 | -9.145 | -60.642 | 2024-10-06 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 3ab9f03b-54ef-395f-bb11-f92c727e2152 | -9.1759 | -61.5794 | 2024-10-06 01:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 54ed3744-e021-3316-8f67-88cbd6f7e73d | -9.176 | -61.5603 | 2024-10-06 01:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 90cf423b-224c-3fd4-8e57-8eb996a23936 | -9.3275 | -46.5609 | 2024-10-06 01:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f0087366-46d2-3f2c-b071-ac1261bb5ecb | -9.3278 | -46.5385 | 2024-10-06 01:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 192.4 |
| fc2b4548-64d4-342e-9eb2-7743fdef5558 | -9.3464 | -46.5589 | 2024-10-06 01:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| e8b83739-ef98-3515-974b-a44d0fb3a1dc | -9.3467 | -46.5365 | 2024-10-06 01:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 104553c8-1a9e-3409-bd3c-35f163f6df40 | -9.347 | -46.514 | 2024-10-06 01:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 141cfa9c-1e47-3568-8802-767ce946f985 | -9.3647 | -51.0898 | 2024-10-06 01:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| d95ab6f8-b842-3553-8b7c-f917acef9eab | -9.365 | -51.0687 | 2024-10-06 01:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2550aef7-b42b-3c4c-8654-c58d9dceca8b | -9.3835 | -51.0881 | 2024-10-06 01:25:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 23cf31be-9ab1-321b-b577-aa1fe88725c3 | -9.3638 | -64.319 | 2024-10-06 01:26:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bcf8dc43-c002-3953-b345-e75a35556d39 | -9.8552 | -60.2966 | 2024-10-06 01:26:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 70bb8766-cb4c-3d75-a617-dfd4c0f16c66 | -9.8802 | -59.5008 | 2024-10-06 01:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7fbaa3bb-0d3d-3956-9f00-3a17b4297f07 | -10.2173 | -59.403 | 2024-10-06 01:26:04 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| dbf8dc3b-718d-3d72-8468-9547eaea14b4 | -10.7962 | -44.7669 | 2024-10-06 01:26:07 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 10c269c6-de3f-3a4d-8c2d-baac675ef731 | -10.8149 | -44.7874 | 2024-10-06 01:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 6220562f-9a7a-391c-a978-2e5115bbb6ef | -10.8153 | -44.7643 | 2024-10-06 01:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 250.2 |
| ed5b93b8-596c-3281-b231-62273acb8685 | -11.0966 | -54.2336 | 2024-10-06 01:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ac5629e8-4ba0-321f-96fc-988a5876e472 | -11.1155 | -54.2319 | 2024-10-06 01:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 88cd7076-ae8d-375a-bd63-0735b165fd98 | -12.0211 | -63.7478 | 2024-10-06 01:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| ce16e8a0-242d-3016-9c7b-58ca59716599 | -12.6089 | -53.1338 | 2024-10-06 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e3939998-f356-3c9f-902d-59d3225e5c59 | -12.6092 | -53.1129 | 2024-10-06 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0b20a712-d10c-3b83-8409-39589c8f3193 | -12.628 | -53.1317 | 2024-10-06 01:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 2036402c-1da2-3778-a148-3bd0484c6748 | -12.6283 | -53.1108 | 2024-10-06 01:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2590c20c-2269-3ff5-a3c4-4995de1c8a6d | -12.6532 | -54.0415 | 2024-10-06 01:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 47512c26-1a4d-3598-b1c7-368852566674 | -12.763 | -50.5352 | 2024-10-06 01:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 179.4 |
| fd83cef3-87fd-3cb1-95ce-58b5abb32dc0 | -12.7822 | -50.5328 | 2024-10-06 01:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 2f93cb86-db9e-3e47-8521-dfbfc405f852 | -16.5745 | -57.16 | 2024-10-06 01:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 5303eeed-7a08-3101-aa41-f5ded7c83300 | -16.614 | -55.9214 | 2024-10-06 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.6 |
| 98d1953c-670c-3a83-88f1-3ac26e69c678 | -16.6336 | -55.919 | 2024-10-06 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| c165113b-68a2-33ad-815b-7fdb7f74c139 | -16.6395 | -55.566 | 2024-10-06 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| d265bbfb-8ff6-3a1d-885e-2fb822123687 | -16.6398 | -55.5452 | 2024-10-06 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 167.2 |
| 41b1c6ba-3716-3acf-acf1-5482ac6ab64a | -16.6402 | -55.5243 | 2024-10-06 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 134.9 |
| e2c4b4d4-75af-3880-8618-c79a26ceb88a | -16.6594 | -55.5427 | 2024-10-06 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| a47eb853-e091-35e2-b93f-dfc6b341e696 | -16.6598 | -55.5219 | 2024-10-06 01:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 796e14a1-2f68-3543-b497-e7d1f9fc02ea | -16.6871 | -57.4536 | 2024-10-06 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 75810bbd-9433-3304-bfc7-9ce24697e323 | -16.7067 | -57.4514 | 2024-10-06 01:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 5732d951-f0ad-31cd-8136-ffc853a150eb | -16.7647 | -57.4856 | 2024-10-06 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 968c2d41-2f80-3b23-87bf-f4c08aefab09 | -16.8238 | -57.4584 | 2024-10-06 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| ac9c30e0-92f0-3f17-965e-f09f5e44e9ce | -16.8433 | -57.4562 | 2024-10-06 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 379e81f3-2c54-38ff-892f-e31b79c4de2f | -16.9348 | -56.625 | 2024-10-06 01:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 012135f6-1a70-3132-819d-97baf7beeb43 | -16.9545 | -56.6226 | 2024-10-06 01:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 3fee4df3-acf5-3eaa-8ac3-09e0206480a0 | -17.3837 | -42.6483 | 2024-10-06 01:26:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 105.1 |
| b602b997-403b-325b-8af1-aae011844e67 | -17.0007 | -55.0607 | 2024-10-06 01:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 73519e0b-ebdb-35ae-bb6f-bca739310fcf | -17.001 | -55.0398 | 2024-10-06 01:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 72490f06-a856-312e-b888-91c8d9a05d6f | -17.1182 | -57.4039 | 2024-10-06 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.5 |
| ca3ff366-2fb8-3d70-ad47-c95df89bcc24 | -17.1185 | -57.3834 | 2024-10-06 01:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| ab1dd9a3-ae8d-30e4-814b-b9ffbeba1915 | -17.1375 | -57.4221 | 2024-10-06 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 6b455156-c86f-3f16-a380-d7189ad2bdfa | -17.1571 | -57.4198 | 2024-10-06 01:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 7e94ae81-7834-3485-b178-1b718b0f46aa | -20.5813 | -49.3865 | 2024-10-06 01:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 9c77c8d8-c8e8-30aa-8ebe-5b5012e7670f | -20.582 | -49.3635 | 2024-10-06 01:27:00 | GOES-16 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 23347ad2-4970-35b1-9c53-48c8d58be88f | -1.7668 | -47.1984 | 2024-10-06 01:35:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 26ebd085-873e-369b-b670-69ff1a0af2d5 | -2.6859 | -49.0539 | 2024-10-06 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9c5c0dbe-16cc-32d7-9227-d3499d40cb51 | -2.7043 | -49.0747 | 2024-10-06 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 90cfb95a-caa5-38a4-82be-b04494ab76b5 | -2.7043 | -49.0533 | 2024-10-06 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 24040c5c-91ff-3749-b6a6-9adf2f73c7dd | -2.6858 | -49.0752 | 2024-10-06 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 141ac969-a33e-38b6-ac75-38d81a69c58a | -2.7981 | -48.6873 | 2024-10-06 01:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 50a868ae-1fd0-3f69-b8f1-0c6bc1626ae5 | -2.8166 | -48.6867 | 2024-10-06 01:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 792ec655-14be-307d-9e0f-fb401cfc0a5f | -2.8169 | -48.601 | 2024-10-06 01:35:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| d838454d-c54a-3710-b274-60ea18c0fa31 | -2.847 | -50.4648 | 2024-10-06 01:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a4ee6e1c-42a4-30c5-b04e-5cca2aae5ccd | -3.1053 | -50.4573 | 2024-10-06 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6398d095-6aea-31b6-8d08-1632da85526c | -3.1129 | -48.6131 | 2024-10-06 01:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2c59b668-975f-337e-a85c-4eab4d73a388 | -3.1314 | -48.6125 | 2024-10-06 01:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| ed2c0744-adf2-377c-a0ea-b953179d09c9 | -3.1315 | -48.591 | 2024-10-06 01:35:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 22692a1a-b7a8-3c88-b8ba-ae282c2f5cb8 | -3.2329 | -50.8504 | 2024-10-06 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 72a8568e-ab57-3821-9722-132a0fcd8a55 | -3.7068 | -41.6758 | 2024-10-06 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| f987f8bf-8c88-36ac-b44f-56d53fbdb2c0 | -3.7255 | -41.6748 | 2024-10-06 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| aa1fa94d-abef-3cbb-8b88-03d87f046a69 | -3.8008 | -41.5989 | 2024-10-06 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 862fc91f-1338-3bff-bbfb-e975e78a7ac4 | -3.7748 | -49.4856 | 2024-10-06 01:35:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 08fe0b6d-c92c-33ee-9cd2-019c9b028a6f | -3.775 | -49.4643 | 2024-10-06 01:35:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 4a652b75-673e-3fdd-a642-4ac889a7cdb9 | -3.801 | -41.575 | 2024-10-06 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| f0e3cd52-33cd-3db1-842b-d758dc999645 | -3.8196 | -41.5979 | 2024-10-06 01:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 9baa948c-6c5f-3755-8d17-42290ad877a4 | -3.7936 | -49.4424 | 2024-10-06 01:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 75a59865-6ef9-3e4c-a39f-23514df08c75 | -3.7934 | -49.4849 | 2024-10-06 01:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 233d4adc-c1c2-39d0-87ea-0deac1dd99b3 | -3.7935 | -49.4636 | 2024-10-06 01:35:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a02183ff-9217-3762-bd0c-9bd0abc0259d | -5.5716 | -44.8927 | 2024-10-06 01:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7b719d9b-0eee-360f-86e2-28e93a8791e3 | -5.5718 | -44.87 | 2024-10-06 01:35:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| f13997d2-d827-3cfd-bd23-70895894ac4d | -5.5905 | -44.8687 | 2024-10-06 01:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b7a5e6ce-5979-31cd-b977-237bd4926594 | -5.8214 | -44.1426 | 2024-10-06 01:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |


[Clique aqui para ver as próximas entradas](README25.md)
