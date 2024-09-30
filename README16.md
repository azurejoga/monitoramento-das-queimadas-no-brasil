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
| b5bc483a-9357-341f-bf8c-218751357ab7 | -16.665199 | -57.445 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| efdf49d1-e506-380b-906a-cb503367944b | -16.760599 | -57.799099 | 2024-09-30 02:05:46 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8f80d515-e887-3e93-998e-f78e9c53e356 | -16.456699 | -57.326599 | 2024-09-30 02:05:49 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2280f0c2-ff33-31af-b42d-4f03c7ed6fcc | -16.4617 | -57.345299 | 2024-09-30 02:05:49 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9474256-1e81-3874-9c45-4f07adae16f0 | -15.9077 | -57.176998 | 2024-09-30 02:05:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| db6a1852-5107-35b5-aa66-8df9fd8a237d | -15.8981 | -57.179798 | 2024-09-30 02:05:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 908e0b4b-eff1-32c1-a54f-d68adeafc02a | -15.9034 | -57.199299 | 2024-09-30 02:05:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9d199a2-d433-356a-ac20-a2a3e847d9fe | -15.8149 | -57.370201 | 2024-09-30 02:05:59 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b11ff8e5-05d8-3ee7-97f5-677dde75e73d | -15.7701 | -57.781101 | 2024-09-30 02:06:02 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 669b98b8-e771-3347-8e38-7dcf071e7780 | -15.7749 | -57.799 | 2024-09-30 02:06:02 | METOP-C | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7067393f-a8a6-3e59-a1f3-b79587a7688f | -14.8887 | -57.973301 | 2024-09-30 02:06:17 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cddcdb52-3006-3e83-bf13-20b626d958f9 | -14.879 | -57.976002 | 2024-09-30 02:06:17 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a5e017a-8005-3c13-87f7-0a4fa15dec03 | -9.7054 | -62.170502 | 2024-09-30 02:07:58 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c31a4518-fa15-32e7-bd5f-6aac68896858 | -9.0532 | -62.331699 | 2024-09-30 02:08:09 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1396ee43-5cd8-3f0c-b631-cd9bee4888b7 | -10.0401 | -68.137703 | 2024-09-30 02:08:15 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9e9dfb7b-2cb9-30d5-a14d-2736dea6419c | -10.0416 | -68.1446 | 2024-09-30 02:08:15 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b70033cc-3859-3149-9fec-f66d0266d724 | -9.5358 | -68.595596 | 2024-09-30 02:08:25 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 72e95c52-d2ef-3821-ba72-37ae6ce8efa0 | -9.5374 | -68.6026 | 2024-09-30 02:08:25 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad3c180-bae2-37ad-8d36-bf4c51efbc63 | -11.15 | -45.74 | 2024-09-30 03:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17b7fea3-330a-3d53-85ca-052eb753cb56 | -11.18 | -45.75 | 2024-09-30 03:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45e265fa-e818-3fcf-8b95-60925cd4ca9a | -7.03423 | -45.36345 | 2024-09-30 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9db8bddb-d4a7-3743-b426-c1893e1f9800 | -7.03354 | -45.3672 | 2024-09-30 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39b2200d-f5ae-351c-a1df-25c57d4ed029 | -6.97376 | -44.21713 | 2024-09-30 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81e73ee4-5883-3d7d-9658-eae24cce2d26 | -6.96857 | -44.21601 | 2024-09-30 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 734b303b-b6e2-3d21-b6d0-7b52644b12fc | -6.39527 | -44.7818 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce7d0c08-3063-3a40-92d7-9d645b4f9125 | -6.39495 | -44.78728 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e0efcea-7656-3eec-b4fa-908dcb343aaa | -6.39467 | -44.78528 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b24cb0e8-075d-355e-b16a-cc54e337ec7c | -6.39406 | -44.7888 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac92afe7-c0be-3b64-9c6d-6494d5ef39b1 | -6.39136 | -44.77591 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e0f4f92b-ae52-3a8b-aeda-5d16f1bb732a | -6.39073 | -44.7794 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c3b4157b-073b-35ed-a07c-0685cc91e57b | -6.3904 | -44.77737 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b80421b5-a995-3a0b-932e-df8d486ca5e9 | -6.39009 | -44.7829 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eeeede11-0525-3940-97d0-3b7114387677 | -6.38979 | -44.78086 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47e0bf1c-e359-3987-8e18-a5dedfbb3791 | -6.38918 | -44.78438 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5f2378f-e508-3b85-b7b4-5e819555de51 | -6.38587 | -44.77507 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ad3aed64-c162-34fd-832b-08037589c905 | -6.38551 | -44.77306 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f0e57a1-3259-3982-889c-6f867a26a062 | -6.38524 | -44.77851 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc5e3bd9-9d64-3f95-901f-0d330ba1e0f2 | -6.38491 | -44.7765 | 2024-09-30 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b901a715-3128-32e3-affa-91f3d93592b5 | -5.64538 | -48.42009 | 2024-09-30 03:42:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9c3e3910-193c-381b-953f-b1e81e203477 | -5.64482 | -48.42024 | 2024-09-30 03:42:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc0345e6-c0b5-3d51-a230-1aca2ad3fb01 | -5.6442 | -48.42661 | 2024-09-30 03:42:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e9fac5fd-9f0c-3c72-a118-edb88fde0a9b | -5.6436 | -48.42677 | 2024-09-30 03:42:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2c8b53ff-bf2c-3ea5-8b48-73d3aaee1590 | -5.33497 | -47.89784 | 2024-09-30 03:42:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 674c1b13-20fb-377c-b290-e73db3cdaf01 | -5.3282 | -47.89668 | 2024-09-30 03:42:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d209473-ca1a-3d76-a69e-0a4f934c559c | -5.32144 | -47.89552 | 2024-09-30 03:42:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8daca44-7d2a-3218-8db2-0ad8de26a175 | -5.32032 | -47.9016 | 2024-09-30 03:42:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcc7e6a9-7560-3375-9c70-a71d93c5e8e4 | -5.31824 | -47.90032 | 2024-09-30 03:42:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e58a12d2-2933-370d-a086-706b2ee52f3f | -5.09185 | -46.16933 | 2024-09-30 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d95acdcc-83ce-3884-906b-8a7a43dca8c5 | -5.09101 | -46.17404 | 2024-09-30 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 235fcd50-65f8-3537-831d-4c49d495f644 | -4.87099 | -45.80834 | 2024-09-30 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1267767c-35b2-3c76-bcd2-fcfca80dd59b | -4.70774 | -45.87758 | 2024-09-30 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed199ca6-f820-3bc9-b240-0df37949f052 | -4.70687 | -45.88249 | 2024-09-30 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c69bb60c-b4e0-3b7b-9444-d592a1973ed3 | -4.70597 | -45.87881 | 2024-09-30 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed87ceb9-1e0b-3f4c-aca5-c751d35c3cad | -4.63697 | -48.53449 | 2024-09-30 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8ce3f31-6511-3ec9-8a17-aa63dc262e9b | -4.63396 | -48.53421 | 2024-09-30 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 682cfff8-3b4e-373d-b033-62a5f6e9db1c | -4.62987 | -48.53335 | 2024-09-30 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28a4b550-fb20-3cdd-a9b0-57d65b463040 | -4.60941 | -46.64798 | 2024-09-30 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afe18852-183b-3e6b-bec1-a45fe151ddc4 | -4.60853 | -46.65296 | 2024-09-30 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7342b69-a959-3b11-9f5e-47836e2ddede | -4.49131 | -48.11433 | 2024-09-30 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bc35be3-0a40-3082-a301-e0bef32e3e3b | -4.49115 | -48.11174 | 2024-09-30 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3ffa082-5149-3df2-94bb-b21ac3054f5d | -4.48995 | -48.11828 | 2024-09-30 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66d20d80-74c3-34e1-9a07-d1bdf4192651 | -4.43925 | -46.14764 | 2024-09-30 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 783d370a-9306-3555-8a2c-ee9574c4bc03 | -4.18813 | -47.93895 | 2024-09-30 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 95861838-a3d9-3aa4-a3b9-b4339adc5f38 | -4.17725 | -46.85849 | 2024-09-30 03:42:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb297340-1f90-3587-bda4-68d8f37e9513 | -3.62721 | -44.54259 | 2024-09-30 03:42:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69cee64a-780c-3939-ac71-6e0a1319df46 | -3.62654 | -44.54646 | 2024-09-30 03:42:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e111f6a9-d680-3dcb-9ca3-383239c52c7c | -3.59527 | -44.54136 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c7c25f8-0d53-3620-88ea-9264ffacbbd8 | -3.59461 | -44.54528 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e6e9d95-e534-391d-95a6-f3f7ff11d355 | -3.59328 | -44.55315 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d11a359-d2de-3ae0-a53f-49cf4dd7ef77 | -3.59263 | -44.55701 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de815945-99e3-3d93-a4be-d8b546d72a0f | -3.59198 | -44.56088 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53804532-5519-3fc3-ad3a-73459d088f9f | -3.59133 | -44.56474 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50602c6a-29df-31b8-a49a-ae91109c69fd | -3.5909 | -44.53284 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cfcd6d19-5c7b-3850-9e76-b40ad0dda61a | -3.59068 | -44.56858 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b0a3687-64fc-3102-98a3-34b10ae46426 | -3.59026 | -44.53662 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5531de7b-9284-3a51-8f28-1c225de50a9a | -3.59003 | -44.57242 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 901bff2b-a1c5-31cb-a31f-10832e36b95e | -3.58895 | -44.54438 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| cd47c26b-8429-331f-b10d-3c67942230b9 | -3.5883 | -44.54827 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe1712ed-a2a8-3218-a085-86b66b163d06 | -3.58764 | -44.55216 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 545308b1-03de-3c02-9af2-450ff7820058 | -3.58699 | -44.55601 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17ada406-730d-3554-9c76-d3e499d12c3b | -3.58524 | -44.53202 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 52a2232c-9df8-3e3f-9fef-0665c0435fba | -3.58461 | -44.53577 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c2364ee0-fb42-31a8-b7f2-846adc8c9edd | -3.58396 | -44.5396 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 4bafe08c-7e98-354a-b4ae-ccbcc689ec65 | -3.58331 | -44.54344 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 234f4011-915f-34ae-9bdb-ca38687911a6 | -3.58266 | -44.54728 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba7f2dae-e2e1-33c8-af4b-f4b6b07a0d63 | -3.58201 | -44.55113 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 867dd06a-3274-3d5a-a458-9e2120e3517d | -3.5783 | -44.53875 | 2024-09-30 03:42:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 029320f3-441f-39d8-86ee-d02a24446caa | -1.65117 | -46.15212 | 2024-09-30 03:42:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93c1a079-44e6-3b78-a317-d7e306ce4942 | -1.65029 | -46.15754 | 2024-09-30 03:42:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6ea0014-4a8b-3325-ba79-16f7d23c1366 | -8.12851 | -39.52874 | 2024-09-30 03:42:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 26827c45-0441-3aee-926c-fd47d5d53953 | -7.89033 | -39.32843 | 2024-09-30 03:42:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7afb4557-60d8-33c5-9fec-8f8fd16f5046 | -7.88957 | -39.33294 | 2024-09-30 03:42:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 053311ea-f3f3-3d7c-a742-e60a9cf46f52 | -7.8866 | -39.32778 | 2024-09-30 03:42:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 184d1d04-9615-3a73-a57f-28d08a78eb24 | -7.47759 | -34.9425 | 2024-09-30 03:42:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b5b7a894-4439-3836-8762-fc57d70cc979 | -7.47622 | -34.84272 | 2024-09-30 03:42:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 11433de6-5fe5-352d-a606-26e832b315ea | -7.4243 | -34.98032 | 2024-09-30 03:42:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b5ada608-e866-3477-b328-10ac0a7eddad | -7.42375 | -34.98378 | 2024-09-30 03:42:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 93be53b6-e242-3ce9-8a70-632217b3af4f | -7.41729 | -43.37659 | 2024-09-30 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 23aa4ecf-f694-3055-a46f-26308bba8d15 | -7.37742 | -34.88713 | 2024-09-30 03:42:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 584a1a11-898b-348f-9bbc-75f2646f698b | -6.78866 | -40.14227 | 2024-09-30 03:42:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README17.md)
