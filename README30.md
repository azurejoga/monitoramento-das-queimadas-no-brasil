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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae94471a-802f-3690-a86c-2c892952e5e5 | -10.60617 | -44.94247 | 2024-10-30 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bd2f4b9-d7c0-31b0-a71b-7abbfe3a1088 | -10.60395 | -44.63442 | 2024-10-30 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67461e9e-2fa8-3e6f-89c9-3758b6f8ae96 | -10.603 | -44.63936 | 2024-10-30 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8bd058d-2f08-353c-8db1-d15d1f7bfcaa | -10.60292 | -44.63338 | 2024-10-30 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a468956-9393-3b0d-9e5b-441274d8305e | -10.60193 | -44.63836 | 2024-10-30 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ed27c44-13f7-3472-8f44-a98571479737 | -10.49351 | -45.11212 | 2024-10-30 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4098d63b-0a4f-3fb7-8bb4-9598177ee192 | -12.1388 | -46.98861 | 2024-10-30 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 097b5f8a-d636-3894-bdbd-3271824d714b | -12.13827 | -46.98997 | 2024-10-30 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31812ac0-0892-3b2a-8c88-a0520d1f5466 | -12.13782 | -46.99324 | 2024-10-30 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f971b50-b745-3a31-a688-82a30dd27491 | -12.13725 | -46.9947 | 2024-10-30 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 66e1eb19-1eb3-3558-ae1d-ed5a9d349c2f | -12.13646 | -46.99977 | 2024-10-30 03:30:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbab9122-3598-38c5-ace4-15ec9cb99cbb | -12.00067 | -47.65855 | 2024-10-30 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1779ae3d-eb15-3a3d-988c-e100a172b047 | -22.55083 | -47.70346 | 2024-10-30 03:32:00 | NOAA-20 | CHARQUEADA | SÃO PAULO | Brasil | 3511706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eab13fb4-8cb1-36d3-88eb-ae383c7b58e2 | -24.15621 | -50.20546 | 2024-10-30 03:34:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fe24b8e7-4e5d-3476-b33c-aeab998027cf | -24.15465 | -50.21158 | 2024-10-30 03:34:00 | NOAA-20 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ccaed41-fe37-394a-b540-bc598d60342c | 3.5448 | -51.2772 | 2024-10-30 03:34:45 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b96bc4be-e887-3fc2-bd4b-a2839053f9ea | -2.833 | -49.2413 | 2024-10-30 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 4a1bb570-696d-3df4-b506-95a90f9577cc | -2.8331 | -49.22 | 2024-10-30 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 22cb9f4c-c0ee-3a62-a2cb-724d901362cb | -3.0734 | -54.167 | 2024-10-30 03:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 1b6acf81-edbe-3770-980a-4909ca16f6a1 | -3.0913 | -54.287 | 2024-10-30 03:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| cf83888c-aa94-3eec-8e39-ac5929b104b3 | -3.0914 | -54.2669 | 2024-10-30 03:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 10e41df1-ce6f-30e4-bdf2-7d02b47d95b7 | -3.1097 | -54.2865 | 2024-10-30 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| df1dc6c7-3a38-381d-aec6-163e4207d873 | -3.1098 | -54.2665 | 2024-10-30 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ac01a077-a588-3251-93c4-7c4d58e83617 | -3.1281 | -54.266 | 2024-10-30 03:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 37a12174-ba3e-3744-a165-81d70397dd86 | -3.1601 | -50.6021 | 2024-10-30 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c41a870a-c42d-321e-bd3e-5b879c3a1026 | -3.1602 | -50.5812 | 2024-10-30 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8498645a-62c7-3a26-9219-b399349cf79b | -3.1786 | -50.6016 | 2024-10-30 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b6d09dbd-3221-3b85-a38a-75ca83a354ee | -3.1787 | -50.5807 | 2024-10-30 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b4b0eddd-4325-3838-94fa-f8ba50350019 | -3.2378 | -45.5839 | 2024-10-30 03:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.9 |
| af051a08-9751-3c3e-99d2-283d43995a98 | -3.2379 | -45.5615 | 2024-10-30 03:35:24 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 15971207-6820-3fdf-b492-ba5657d38bff | -3.2564 | -45.5831 | 2024-10-30 03:35:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| a3b094cb-2ac7-33aa-aadd-a519b578d2ec | -3.2565 | -45.5607 | 2024-10-30 03:35:24 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 7744cfb6-90d9-324c-885e-b62ea85953fe | -3.2535 | -50.3479 | 2024-10-30 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 2f8ef3a8-4941-394e-abd4-ca4e0409c7a4 | -3.2719 | -50.3473 | 2024-10-30 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 7535b02a-c200-3c48-96bc-ed1de372039a | -3.5631 | -47.3847 | 2024-10-30 03:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| b69edc07-55c0-3273-b79f-60dbf2afc027 | -3.5632 | -47.3629 | 2024-10-30 03:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 664a5225-1cdd-3719-97d5-9b5f693cb7ae | -3.5817 | -47.384 | 2024-10-30 03:35:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| adc61d63-4c20-3f1d-bcb7-f716fc303589 | -3.9485 | -48.1508 | 2024-10-30 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| dc7e920c-4543-341a-beeb-1cd1d98f3767 | -3.9486 | -48.1291 | 2024-10-30 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 083a3780-b715-3522-b98e-0f9f25a40758 | -3.9487 | -48.1075 | 2024-10-30 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| eaac797d-3f4b-31c5-b51c-63445af50525 | -3.9671 | -48.1283 | 2024-10-30 03:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1cfb010d-aab4-37bd-a49b-cf9befc906dc | -4.0681 | -50.024 | 2024-10-30 03:35:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| beafe8fe-dc81-3b18-a3ec-7d99bf06cdd6 | -4.0682 | -50.0029 | 2024-10-30 03:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 02c3c6a0-c0f1-3e48-ba27-b4c0bf54fb5c | -4.0866 | -50.0232 | 2024-10-30 03:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 24eeb83f-c337-3c1f-a79a-83ebd370024a | -4.0867 | -50.0021 | 2024-10-30 03:35:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| e05ebdd2-9c29-3afc-9f9d-12c2b71c0da1 | -4.2561 | -43.46 | 2024-10-30 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| ceac2da1-7772-326f-ab22-64c2af9ef398 | -4.2563 | -43.4368 | 2024-10-30 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 546081bb-a842-3a9a-aa41-ca78b73242da | -4.2748 | -43.4589 | 2024-10-30 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1ade6b3f-2d64-3f9d-9159-b27291cd65eb | -4.2749 | -43.4357 | 2024-10-30 03:35:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 76a25c6f-baec-3c5b-9321-042636685c16 | -4.2679 | -50.6879 | 2024-10-30 03:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| dab2f035-8b1a-306e-8a7d-aa2e88c4a352 | -4.2681 | -50.6669 | 2024-10-30 03:35:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 5c381281-14ae-3877-a99e-f8536905faca | -5.2306 | -47.9566 | 2024-10-30 03:35:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 9501a53f-8338-36c9-afc2-f190608c23ae | -5.9788 | -45.3621 | 2024-10-30 03:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2957ddcd-e4f2-3308-9c62-2e748de9b083 | -6.4044 | -42.1035 | 2024-10-30 03:35:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 148.1 |
| 4dea36fe-95a6-3443-8a3a-a1dcd9433381 | -6.4046 | -42.0796 | 2024-10-30 03:35:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 773541e7-fef9-35b8-8178-d6126ee63325 | -6.4232 | -42.1017 | 2024-10-30 03:35:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 338.9 |
| 30eb3ec2-2788-3575-8631-cf12b096ee3d | -6.4235 | -42.0779 | 2024-10-30 03:35:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 8ed5720d-7610-38ed-970d-9dbd23928ca9 | -6.442 | -42.1 | 2024-10-30 03:35:42 | GOES-16 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| adfc6568-52f9-399b-bdf0-eab71d2b8990 | -6.8592 | -59.0511 | 2024-10-30 03:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c13bbc93-c66d-3b52-ae68-eecaff78b3c9 | -10.3434 | -49.6536 | 2024-10-30 03:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| cd7c8b78-672a-3a2b-b158-71259edaae65 | -10.3437 | -49.6321 | 2024-10-30 03:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0b773e15-2049-36fc-bb11-b9edfa2dc79a | -10.7175 | -44.916 | 2024-10-30 03:36:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 896ea296-b581-3ad0-8a41-06168cb57433 | -19.5662 | -56.7164 | 2024-10-30 03:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| 92e0331e-88a4-3a9f-adf8-e091b16ba382 | -19.5862 | -56.7136 | 2024-10-30 03:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 0b444b5f-fc96-361e-a86f-e5dd1aabed42 | -19.6063 | -56.7108 | 2024-10-30 03:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 154.2 |
| 84177752-41fb-378a-b1b3-d3c5c3f9f7aa | -19.6264 | -56.7079 | 2024-10-30 03:36:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 92.1 |
| cc1cb291-e0e3-3b3e-a0dd-337637cfc3a6 | -1.458 | -54.0763 | 2024-10-30 03:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 23f723cc-28f5-3ef4-aa5a-861f3c10c6cc | -2.833 | -49.2413 | 2024-10-30 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b5e11681-0153-32a0-acf6-907d96caa077 | -3.0734 | -54.167 | 2024-10-30 03:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1d17bd17-a459-3fa7-a3dd-3560b6c2e20f | -3.0913 | -54.287 | 2024-10-30 03:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 553a8d23-2e28-3ad4-a40e-dd3a71108f69 | -3.0914 | -54.2669 | 2024-10-30 03:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 9cc856e7-a29c-3504-8367-49a67c9e28a3 | -3.1097 | -54.2865 | 2024-10-30 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8264be85-24a0-3254-a0bb-bb8eddc0a5ec | -3.1098 | -54.2665 | 2024-10-30 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 1c6cfd3e-8e7c-3dc9-9021-7972e467c918 | -3.1281 | -54.266 | 2024-10-30 03:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| ce67709c-17bb-3645-a2ac-a6feaf50adf4 | -3.1601 | -50.6021 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 13ecce87-a8de-37d2-acc9-e9d02de27136 | -3.1602 | -50.5812 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| cf65f2ad-7579-37dc-af07-2bd3f0d9c832 | -3.1786 | -50.6016 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 3a1a54bc-a7de-3c3b-af76-fbb1f67eb299 | -3.1787 | -50.5807 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 99dea471-3fc1-365a-b09d-32ec42608da5 | -3.2534 | -50.3689 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 0a1a5a3d-1d91-3ec9-9711-e8ef6928bbda | -3.2535 | -50.3479 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 1e7857f5-caa5-346a-8825-9edbac3f19b1 | -3.2719 | -50.3473 | 2024-10-30 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| cce688e5-6cc0-364b-be9f-ebaad6501bbb | -3.5631 | -47.3847 | 2024-10-30 03:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1b5b8744-202a-38e3-aa46-771b90993532 | -3.5632 | -47.3629 | 2024-10-30 03:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4c7cedce-5248-37ad-91ec-7ae8e94fc59e | -3.5817 | -47.384 | 2024-10-30 03:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 2c19ebe8-e9a1-3edc-8de3-87a8d07aeb1a | -3.5818 | -47.3621 | 2024-10-30 03:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| c91d81a0-0f73-318c-acb0-7fff406def07 | -3.9485 | -48.1508 | 2024-10-30 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 7bf1e4cd-5eb6-301b-9750-c093f7a7e754 | -3.9486 | -48.1291 | 2024-10-30 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 84522096-b089-3b43-8af0-4dd0dac46d87 | -3.9671 | -48.1283 | 2024-10-30 03:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6324bd2d-35ca-3a35-9dba-19ec6133fd53 | -4.0681 | -50.024 | 2024-10-30 03:45:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e5b2f6ba-948d-3b54-b9b2-53396fe6a8d6 | -4.0682 | -50.0029 | 2024-10-30 03:45:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ad71fc30-fc20-313e-a6fb-fe5cebde4cb2 | -4.2496 | -50.6677 | 2024-10-30 03:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| eadafb81-9dcf-3f2c-8729-9cd0bff31fff | -4.2681 | -50.6669 | 2024-10-30 03:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 8ba84c4e-845f-3d63-95b1-3ca8048c360e | -4.2561 | -43.46 | 2024-10-30 03:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 92748bfc-3012-30bb-b991-a14130e6e6ac | -4.2563 | -43.4368 | 2024-10-30 03:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 70abf6d1-9612-39a9-9115-2d2aad297ba6 | -4.2749 | -43.4357 | 2024-10-30 03:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 7b74854b-8705-3a14-8610-5363fbdbded7 | -5.9788 | -45.3621 | 2024-10-30 03:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4e245e8a-07d2-3b3b-8bc4-4140b85d5247 | -6.4232 | -42.1017 | 2024-10-30 03:45:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 254.5 |
| ef3cf1fe-6941-30b9-81ce-ed3c58879d6a | -6.4235 | -42.0779 | 2024-10-30 03:45:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 145.4 |
| 17ba4b46-044c-392e-aa11-9c57cbf2f472 | -6.8592 | -59.0511 | 2024-10-30 03:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| d2661101-856d-3718-a96f-7fe414b61705 | -10.3434 | -49.6536 | 2024-10-30 03:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |


[Clique aqui para ver as próximas entradas](README31.md)
