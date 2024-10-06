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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d3beefa-2aad-3078-938a-baceb99e2c7c | -17.0007 | -55.0607 | 2024-10-06 00:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| bbce2c9e-d65b-38ba-8832-616c3cad0cfb | -17.001 | -55.0398 | 2024-10-06 00:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ba1255b9-b73c-315e-a5dd-548050527ee4 | -17.0203 | -55.0581 | 2024-10-06 00:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 902340fc-96d5-3e84-a067-8d4fd0f01bd5 | -17.1182 | -57.4039 | 2024-10-06 00:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.9 |
| 4a9d7244-6e43-3af3-8bba-ac76a105abf6 | -17.1375 | -57.4221 | 2024-10-06 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 039cef19-f1ce-3da9-bc7c-0eb4cbe281f1 | -17.1571 | -57.4198 | 2024-10-06 00:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 845bf5d8-9776-3273-996a-f58cec52ebd2 | -18.6586 | -57.2759 | 2024-10-06 00:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 166e3724-c65a-3f17-858b-c2776eeecf99 | -2.7043 | -49.0533 | 2024-10-06 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 32fbb948-bd30-3269-b03d-17b3336d2c1a | -2.6857 | -49.0965 | 2024-10-06 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 3f72617c-7828-33d1-ab2a-6970c4c7a5e9 | -2.6858 | -49.0752 | 2024-10-06 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 182d8372-da80-38fd-ae65-84ce104e205f | -2.6859 | -49.0539 | 2024-10-06 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 57d43881-68eb-36c5-a25c-70eb1c0d3cd8 | -2.7043 | -49.0747 | 2024-10-06 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| a5b6008c-8997-3d35-8a15-ef56a15eb91d | -2.8169 | -48.601 | 2024-10-06 00:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| adb4e739-25a0-36a4-b2ab-7e8d7b373a77 | -2.847 | -50.4648 | 2024-10-06 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 268c208d-4590-308f-bc5c-7a4f3d0f69df | -3.0405 | -53.037 | 2024-10-06 00:15:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3ffcb011-dd60-3685-9780-37195f39ff66 | -3.1053 | -50.4573 | 2024-10-06 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 73b7b67a-650d-3b8e-aa3c-60d196fe93f3 | -3.8008 | -41.5989 | 2024-10-06 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 158.0 |
| ab43bda1-c309-3223-aa97-84fd6661f822 | -3.801 | -41.575 | 2024-10-06 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 55.5 |
| 45d9bb5c-dcb2-363b-ae3d-72047c798c84 | -3.8196 | -41.5979 | 2024-10-06 00:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 5075e354-f441-3869-b7e8-51b73da7bdf1 | -3.7935 | -49.4636 | 2024-10-06 00:15:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 25dc3b65-6989-3a0c-bc12-6ddd00e945ae | -4.4534 | -47.4757 | 2024-10-06 00:15:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 9520a214-073a-39cb-9620-9c1e5fad9611 | -4.4536 | -47.4539 | 2024-10-06 00:15:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 49087f1d-6ae2-3aa0-b091-02f30a850d42 | -5.5716 | -44.8927 | 2024-10-06 00:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| d92e633a-27b1-3845-8293-e5f0dd68ac01 | -5.5718 | -44.87 | 2024-10-06 00:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 182.8 |
| b664a2e6-8595-3aa2-b86f-09a9373e4967 | -5.5903 | -44.8914 | 2024-10-06 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0fbc04f3-1f8e-301a-9b72-5af60cb4fdfd | -5.5905 | -44.8687 | 2024-10-06 00:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 851110ab-4552-3156-a359-f8b6ccb15f2d | -5.8214 | -44.1426 | 2024-10-06 00:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 12919a47-2535-37ee-9e65-1b12d6dac06f | -5.8216 | -44.1196 | 2024-10-06 00:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 738e8f0c-c3bc-33c1-ac11-5ae5b64cfbfa | -6.8916 | -47.693 | 2024-10-06 00:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6dae9224-7191-3b66-b6ff-38ddb555f4cc | -6.9103 | -47.6916 | 2024-10-06 00:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 237.4 |
| 902e6db0-888f-304b-b7db-9167974e9576 | -6.9105 | -47.6697 | 2024-10-06 00:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| a516e3c3-da42-3a7e-a133-843811aebd52 | -6.9514 | -59.0666 | 2024-10-06 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 26a5a455-44fb-3a79-8e3c-b7277513d177 | -6.9699 | -59.0658 | 2024-10-06 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 40be33b5-997d-3dec-ac2d-b6d40b7cd12b | -7.153 | -59.3092 | 2024-10-06 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| ba57ae2e-11fb-3b12-a83f-cf7ca8426e38 | -7.1532 | -59.2898 | 2024-10-06 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 79e37b5b-52e2-3c31-9aa1-c8f1ce301579 | -7.9639 | -54.7764 | 2024-10-06 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6e9732ce-f845-3383-a20e-21226af6d632 | -7.964 | -54.7562 | 2024-10-06 00:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 87dd120e-6c60-3c20-8c00-8a636f3ba348 | -7.9825 | -54.7752 | 2024-10-06 00:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 1f4279f4-baa4-368a-880d-d79d258f1fd7 | -7.9826 | -54.7551 | 2024-10-06 00:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ab98cab5-ecf1-31a1-bf28-afd4c50a08ba | -8.2138 | -61.2213 | 2024-10-06 00:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 3cdb4997-8f49-3f59-9d0b-1471997b5f52 | -8.2139 | -61.2022 | 2024-10-06 00:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 92905fe0-d747-31f6-b57c-9325a02d2d77 | -8.2324 | -61.2014 | 2024-10-06 00:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| cabc6172-ae0d-3a62-a22e-b9a324e33916 | -9.269 | -48.1377 | 2024-10-06 00:15:58 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d1193941-e6d7-3cab-88a0-d300e09d1383 | -9.1573 | -61.5803 | 2024-10-06 00:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 02a9e549-1814-3c96-9a48-84bae25bc52d | -9.1574 | -61.5611 | 2024-10-06 00:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e0706270-6e73-3e9c-a612-f04a1a4c989f | -9.1759 | -61.5794 | 2024-10-06 00:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 443f76fb-3958-3ade-9a5e-1cec0a385a9a | -9.3275 | -46.5609 | 2024-10-06 00:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c60edf07-f9e2-3836-9555-653232516b89 | -9.3278 | -46.5385 | 2024-10-06 00:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3f92d4c7-ba9a-39d9-876d-efcf962a5d67 | -9.3464 | -46.5589 | 2024-10-06 00:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 206.6 |
| 0171fe48-9fcd-3e0e-b0cc-7a8b25244bc8 | -9.3467 | -46.5365 | 2024-10-06 00:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 0aed3830-611c-32b8-9093-00f508c0af66 | -9.688 | -47.8308 | 2024-10-06 00:16:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.0 |
| f455b392-3c5e-3809-821c-ae0217beb186 | -9.8552 | -60.2966 | 2024-10-06 00:16:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8da276e8-2ccf-380d-b46e-267eff4682f9 | -9.8802 | -59.5008 | 2024-10-06 00:16:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| afc04c54-cd51-328c-baba-a4a1599ed7e6 | -10.2173 | -59.403 | 2024-10-06 00:16:04 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b499a8b5-edc6-35e4-a746-4f1a1438482a | -10.4049 | -50.7161 | 2024-10-06 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2cc3884c-06c7-30a6-acbc-c179c04df126 | -10.4235 | -50.7355 | 2024-10-06 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 2e43630b-f90a-372b-876b-96bc2dad40e5 | -10.4238 | -50.7142 | 2024-10-06 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 320.7 |
| f955b35f-c5cf-37c5-8f2d-1939395d3d6b | -10.4424 | -50.7336 | 2024-10-06 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 160.6 |
| bfa92e1f-3c72-3dfe-bb3e-89e3a28fffe0 | -10.4427 | -50.7123 | 2024-10-06 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 292.5 |
| f06f46d9-e97a-3e8b-beab-3dd2400dba4a | -10.443 | -50.691 | 2024-10-06 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5f1d9303-b9ce-3b31-905b-92d59a8b19d8 | -10.6962 | -53.0354 | 2024-10-06 00:16:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| a0e4a1ee-c0d5-3f30-89e0-948f99877b3c | -11.0966 | -54.2336 | 2024-10-06 00:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8dc457a8-8e55-3f13-b83b-ddb4c6faa8de | -12.0211 | -63.7478 | 2024-10-06 00:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 7587beee-49ea-30a5-9284-af3603b91cb9 | -12.5066 | -47.5705 | 2024-10-06 00:16:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 7ae35867-dcfd-30a2-be98-8c23af96b36f | -12.6089 | -53.1338 | 2024-10-06 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| f8bcbeb3-5b09-3aaf-9b3a-a02510b1ddbf | -12.6092 | -53.1129 | 2024-10-06 00:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| bc0d4d9e-92a9-3df6-b3bf-4489813a488b | -12.628 | -53.1317 | 2024-10-06 00:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 184.5 |
| a3d1c18e-5b3b-3bde-bbdf-02a1a631a284 | -12.6283 | -53.1108 | 2024-10-06 00:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 247.0 |
| 035c6bef-e876-3f99-aed7-6d12a6070cc1 | -12.6471 | -53.1296 | 2024-10-06 00:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 2f42a3de-ca5f-3e15-8afe-1563099e5c4b | -12.6474 | -53.1088 | 2024-10-06 00:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 173.3 |
| ab0d605a-4df1-31c9-8810-c4e651f1c1c8 | -12.6532 | -54.0415 | 2024-10-06 00:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 86bfd5e1-7069-3544-bfea-cc3aa5f1a54e | -12.6535 | -54.0208 | 2024-10-06 00:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 92077809-755f-3ac5-8348-62d025a77a8a | -12.6723 | -54.0395 | 2024-10-06 00:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 4b60cbfd-e540-3279-9583-e17b93f6dd98 | -12.7627 | -50.5567 | 2024-10-06 00:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4abb964d-b459-310b-8ce9-59789a376df8 | -12.763 | -50.5352 | 2024-10-06 00:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 7da05fa2-4043-3e3f-b4fa-98a224f05ea6 | -12.9377 | -62.4697 | 2024-10-06 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e174cea1-fbcb-33b7-b858-972f09034017 | -13.3976 | -61.957 | 2024-10-06 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a3c05ff6-66df-35a1-aa06-58f5e2b98af6 | -13.7342 | -60.6471 | 2024-10-06 00:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 11537d66-7af9-36b9-8a29-839d6af6c669 | -16.3959 | -57.3641 | 2024-10-06 00:16:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.3 |
| a77d6b0a-fab2-3b75-bf04-8e693535e488 | -16.4158 | -57.3415 | 2024-10-06 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 146622c3-2bc4-3302-ba24-902a71e37b80 | -16.5745 | -57.16 | 2024-10-06 00:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| a6d0bb2a-7acd-397c-b610-3c94e09e68ee | -16.614 | -55.9214 | 2024-10-06 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.2 |
| abdebb49-aa93-3175-9bf4-97c465269100 | -16.6143 | -55.9007 | 2024-10-06 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 149.1 |
| 386cea90-73d5-3b80-b1c3-5f801ec76ae4 | -16.6136 | -57.1555 | 2024-10-06 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 3934dfbb-4458-3b08-a413-6ae3ff3a1101 | -16.6395 | -55.566 | 2024-10-06 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 113.6 |
| 2c726fdc-70f9-3a04-8086-b6f76db6a581 | -16.6398 | -55.5452 | 2024-10-06 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 193.8 |
| 60a488cb-e0bf-3f26-9e5b-90ed0632d102 | -16.6402 | -55.5243 | 2024-10-06 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 46c56096-5727-3443-b79b-964888dd27c1 | -16.6871 | -57.4536 | 2024-10-06 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 574fa4c5-b779-35a1-9f50-0d8c34161df8 | -16.7067 | -57.4514 | 2024-10-06 00:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| 14caa367-d3fd-3b28-8198-0f8034cf3933 | -16.7647 | -57.4856 | 2024-10-06 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 95c72ba4-f05b-3750-a753-8e4c7f5bf4c2 | -16.8238 | -57.4584 | 2024-10-06 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 1bd918b6-20c0-366e-9bcd-153108ee137e | -16.838 | -57.8036 | 2024-10-06 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 875b3874-b675-3787-81e2-5f41dad572da | -16.9283 | -55.8405 | 2024-10-06 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 126.1 |
| f8d996a3-bfd5-36e8-a2d1-79d9c336ddca | -16.9287 | -55.8197 | 2024-10-06 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| c29d413c-e58d-3881-a282-32403664af7a | -16.9348 | -56.625 | 2024-10-06 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 63262730-2abb-3f4c-a406-1e71cc37c75d | -16.9545 | -56.6226 | 2024-10-06 00:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.8 |
| e715f30d-6539-3367-812c-669df1ffe54b | -17.3837 | -42.6483 | 2024-10-06 00:16:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d92e9988-60df-39cb-8a88-7960446ee981 | -17.0007 | -55.0607 | 2024-10-06 00:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 0c6cbe88-f105-36c4-a229-f4858221f7e4 | -17.0203 | -55.0581 | 2024-10-06 00:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 125.6 |
| b499ea68-3b2a-3f8c-8a87-86702a8a5466 | -17.0207 | -55.0371 | 2024-10-06 00:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |


[Clique aqui para ver as próximas entradas](README3.md)
