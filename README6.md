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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15d1bea5-591c-38bc-ae8c-fac3cc554a48 | -4.06096 | -50.00267 | 2024-11-22 01:06:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6f926c25-6f04-3140-88eb-37b3a76ed9ab | -5.96008 | -48.06242 | 2024-11-22 01:06:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 719b9b54-6f5e-3d4d-b612-d1a199d5cab1 | -2.30854 | -53.60573 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 82fc531b-dc56-378d-b704-bd0a677a0b3e | -1.62868 | -52.42052 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85902b92-fe02-3c59-be0b-1badc42818d7 | -3.62123 | -45.76527 | 2024-11-22 01:06:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0adfb898-736f-36fe-bb9f-a30e98dab9a2 | -3.06664 | -53.29495 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5bc4eaf2-3d81-3640-b62a-cbb788ceb314 | -3.82038 | -48.97198 | 2024-11-22 01:06:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 2ba7963d-f793-381a-902b-d2c4e2aade60 | -2.41075 | -48.32992 | 2024-11-22 01:06:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 317672cc-133a-38ee-828b-5309b52c120d | -2.68538 | -54.98882 | 2024-11-22 01:06:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 17efccce-7756-390c-b557-271f3ed3ed59 | -1.59093 | -50.43746 | 2024-11-22 01:06:00 | TERRA_M-M | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d80d4fd5-b446-3d5e-99c1-1316be194148 | -3.27012 | -53.83072 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 29d572a1-9b2a-3ecf-9d45-2ee81217999d | -2.85563 | -53.97151 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 970d867e-bd6a-3ed4-bfe8-e0a588b2d416 | -1.2043 | -51.95572 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 49708273-c758-386f-b17b-3a98430f08b2 | -1.09676 | -53.16759 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab73f440-4a42-3c0b-937e-2d886e4f137c | -2.62004 | -51.80859 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4efa2874-95c4-3f8a-ba96-2fee65624889 | -4.2454 | -49.08753 | 2024-11-22 01:06:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b58fdae6-6804-3a76-adfa-9e9426690b88 | -4.21381 | -48.65265 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1c22b643-1376-3457-8ca2-4b41190bed2d | -3.46073 | -45.91898 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| f91046db-1cd0-33cf-b7ba-c3377e66b1c9 | -1.70926 | -52.48092 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6cbbe855-94b9-3187-904e-26f13fa2129a | -2.80832 | -54.02359 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| b72b11fa-f3d4-3c9f-8e6a-5c1c585bf1ff | -1.19541 | -51.95698 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 5326fa1a-f584-3223-b3aa-727c5e7aed40 | -1.13908 | -53.40716 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c2094ab6-d6d2-34a0-ac9d-9d90e84956e8 | -0.26592 | -51.57133 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 626f9f0b-386a-3040-b249-5f0525e56501 | -1.6363 | -52.41048 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6b92dfc9-a954-371c-9a2c-ec0a2fa17830 | -3.27799 | -53.81993 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 15069d2f-aa17-324e-8d7f-28eb4c4e0388 | -3.63991 | -51.45498 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c79eb7e8-8c98-3d88-ba69-572d7e93fe96 | -0.27366 | -51.56092 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 027b7cdc-b1e6-34d9-8780-e346e1e4a6c2 | -1.6131 | -52.58107 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59c972d0-27ca-3236-ad0a-3fee9d448cc7 | -2.61353 | -54.54212 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b1760ab2-b43c-3a54-94bd-5fd28216deb5 | -3.65218 | -51.14601 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 2e2a958c-0a50-3563-9f3e-66b3023850d4 | -1.96464 | -52.9909 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 72fcbd55-4747-3a85-ab25-c88f6e985428 | -4.70612 | -45.81839 | 2024-11-22 01:06:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3b9aeec9-5ae7-32ff-b37f-4891ee7558fd | -3.40573 | -54.02621 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e5915b63-0a45-3ed2-8f61-c4d8df3e0d68 | -1.72345 | -52.71234 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f4339523-a326-3158-a86a-e1529b8bf53f | -2.74152 | -54.1375 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bad1c6c5-c83e-34fb-91be-1cf9a59b2894 | -3.43084 | -50.10603 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7edc22d3-acfa-3cfc-a6ec-092da5066a70 | -1.11105 | -53.40196 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb2c6d90-a723-3464-ae83-1e000af59c61 | -3.51395 | -54.68284 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0d5ecff8-5870-3765-9cf8-cf530d3dd92f | -4.23051 | -48.62659 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5bccdd16-43d0-3278-91c8-9ee6cb7c1337 | -5.96775 | -48.05542 | 2024-11-22 01:06:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 5bfb0272-f2d5-3612-9845-a0b02341ea5c | -3.29915 | -53.84993 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2e552775-57c4-3600-ac01-1a9147bc0d3e | -4.67279 | -46.40364 | 2024-11-22 01:06:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ad3d930a-0ea1-3d75-a90c-e7330e756ad2 | -1.78759 | -53.63442 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 9541c1ff-ed61-3a3c-873a-2602c3a7cc68 | -1.96544 | -48.39251 | 2024-11-22 01:06:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f4efb3e5-66e2-3855-96c9-38baec7b974d | -0.95961 | -51.72601 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57393715-0b99-3cd0-8745-5a873c14b719 | -1.42623 | -46.80946 | 2024-11-22 01:06:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 427da195-0d11-3b7a-980c-e002170812d7 | -2.50615 | -49.01122 | 2024-11-22 01:06:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 94668939-f533-303e-8ce9-40d4454d8852 | -5.81303 | -44.73711 | 2024-11-22 01:06:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 0ec79f61-0e96-3c98-bd3d-2c315f15cb7b | -4.19953 | -53.49894 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a2ea9057-43b5-3884-ac96-b7945ec52e1b | -3.10854 | -53.99271 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| d1d28ac6-ffa8-3568-9661-826e0f0d1819 | -1.63298 | -52.65904 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3ee7a24e-5eda-3201-bc55-68605a3acd87 | -0.34772 | -51.56279 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f0169c08-a811-3e46-a4df-57a8bc2b33b1 | -3.6873 | -50.21557 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9dfb0550-f7d5-3d26-8317-d90e059c56fe | -4.1188 | -51.05814 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| fc5f470c-0e68-31b9-bf1a-ebcc53600bdf | -3.08742 | -45.43 | 2024-11-22 01:06:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 16e92ed9-00a2-38ee-ad28-18ad8cdda1b5 | -0.27492 | -51.57006 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7cbf112b-3401-3463-bdc9-40691d8d2cf0 | -2.58846 | -54.03713 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9c5b7fdd-d96f-3bf8-b69d-855e96de69e5 | -2.22542 | -53.7368 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 77ccdc26-117d-34a9-969f-78f6ef410035 | -3.2443 | -54.23776 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| b0a941af-6aed-34d2-9708-a0006fb6bfc0 | -3.6488 | -51.4537 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 706bb057-52f3-357a-9a03-f87c389e4946 | -3.85625 | -52.34643 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 27f308fb-8b1e-39ab-9495-baf79f4e2d29 | -2.80698 | -54.01396 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 723d602b-6560-369c-8e8e-dd82c5abc1ab | -3.3158 | -47.01444 | 2024-11-22 01:06:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 03171399-9cae-32ca-bc55-dd9737b067be | -3.22418 | -54.23046 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 8e840939-67b3-376e-be9e-793b1251326f | -3.30216 | -50.36399 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1ede9f5e-20f3-3cf2-a3db-9db4a232f938 | -3.23493 | -54.23909 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 2af4d7c0-be69-3565-81c5-5c49da64b8df | -3.06682 | -53.22999 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2ae57fc5-c216-396d-8342-bea2fb1e70ed | -1.62685 | -52.61502 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 776f3cf1-62c5-3e41-b1bb-fe0274ed6af6 | -0.95836 | -51.71702 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f180af61-0fad-3b02-abe0-6e01001e8ceb | -4.67035 | -46.38721 | 2024-11-22 01:06:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 6167d6f4-2e17-3e20-8ade-6f1a9c4b88c7 | -3.40639 | -46.25126 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 13d4968d-30bb-3a16-bb68-168c547a6d6b | -5.41358 | -49.22648 | 2024-11-22 01:06:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 1b4d321b-2963-3abe-a8ac-7dd548364827 | -4.25229 | -48.70588 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 0f712155-9b51-36b1-8645-bb037c351c03 | -3.4733 | -45.91702 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| cf41e7f7-90a3-3949-92f5-b51aa480a2c6 | -2.61878 | -54.05251 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ab71e8aa-1363-360d-a946-a680bc10ea84 | -0.39855 | -51.59614 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 42b848a1-521f-39c5-8503-3629e50ec0eb | -4.24226 | -48.63683 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 943022b1-59fe-33f2-8572-10bcc4f40627 | -3.55022 | -51.53749 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5bbab41f-3527-3481-9098-57d7364a557e | -6.26544 | -44.54253 | 2024-11-22 01:06:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 05acf493-840b-3ff2-97d2-49b60e2c55ef | -1.87207 | -54.36983 | 2024-11-22 01:06:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38a778fd-9ddb-33fe-bef4-32e3123d1ae4 | -1.59975 | -53.21195 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| daf21c15-db18-3f1a-8b74-4dc72958090b | -3.25217 | -50.397 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b8871e9-edc2-3d3d-9d09-341d2a4a989e | -3.23355 | -54.22915 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8feef4cf-3f42-3921-a6b8-9e8efdb346a9 | -3.80717 | -51.99347 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 5e2f49da-bd5d-3bad-9249-06fc11abab6d | -3.22834 | -54.26043 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| a12b7c49-4e54-3373-a454-5f4f07070620 | -3.57399 | -54.51967 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dd5125e3-eead-3487-b2e3-52bf85949233 | -3.42944 | -50.09622 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 8e196609-d3d5-3c1f-9dd3-9dd7c8403c4c | -3.00844 | -51.55122 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 827dafa5-96df-31f4-96c0-d2f95fd7cb5d | -2.78276 | -51.7191 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6d27306a-8227-31ab-b413-df2c4247d69b | -3.20682 | -54.24302 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| b691b3e3-1d95-3e2d-938b-254e5d051bc7 | -6.18427 | -45.45459 | 2024-11-22 01:06:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0175dc4e-8046-3313-94b8-f1159a1ab989 | -1.61677 | -52.60747 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 40c53c40-f5db-32cd-9fdf-0a26d26bb431 | -3.30046 | -53.85952 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 778b6a09-2eb7-3ef1-99a9-480f8948bd58 | -4.58004 | -48.01625 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| afacdad2-cc68-3594-80bb-3b4782664220 | -1.28462 | -52.4665 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1fde18dc-c376-3d4f-8fad-c8c62adf87dd | -3.83511 | -52.2593 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| b98be98d-8723-31a2-bf3a-3dcb5b55a182 | -1.45789 | -52.66004 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 43ab6b39-2c94-31be-9df1-d49f9ed2e06d | -1.39608 | -52.34579 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d547ee6b-99b0-37d1-82c5-646ab4b2d734 | -1.63789 | -52.69427 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a5363e84-6a5e-361b-9e9b-303138788d6c | -1.78381 | -53.60693 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README7.md)
