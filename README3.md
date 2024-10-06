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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 978e46de-b365-330c-b6be-a40d5cd69d50 | -17.1182 | -57.4039 | 2024-10-06 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| b05f4c33-ed8b-33ad-8b5e-2f429c687f5f | -17.1284 | -56.7661 | 2024-10-06 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.6 |
| a9c295dc-06c8-3587-a33f-2cc4c4593a6e | -17.1375 | -57.4221 | 2024-10-06 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.1 |
| 140681d1-e3c2-38b8-899e-de002779e9aa | -17.1571 | -57.4198 | 2024-10-06 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 207438e1-01c2-3f96-91cb-97afef6b948d | -17.812 | -53.7859 | 2024-10-06 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 048357b7-b61e-3996-97a5-b9b7b8966fc9 | -17.8125 | -53.7645 | 2024-10-06 00:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 169.3 |
| bd3a40bf-72cc-3191-9c89-a0ecf4d82845 | -18.6586 | -57.2759 | 2024-10-06 00:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 44687e95-43d6-3ead-93d3-327a21a07ab0 | -1.7668 | -47.1984 | 2024-10-06 00:25:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 803afde2-b4bf-32b1-9b2f-45d030f63301 | -2.6857 | -49.0965 | 2024-10-06 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| c492f058-8473-3b8e-ac7e-830b791c7035 | -2.6858 | -49.0752 | 2024-10-06 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 657baf4b-812c-30f6-9843-6fcab7e18d7e | -2.6859 | -49.0539 | 2024-10-06 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 5a365557-f91d-3692-bd33-4a4ce4954779 | -2.7043 | -49.0747 | 2024-10-06 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 29057dd6-ce9e-36b8-9ecf-91919d777312 | -2.7043 | -49.0533 | 2024-10-06 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| ed0634e3-a987-30c5-857b-16f6f4732578 | -2.8166 | -48.6867 | 2024-10-06 00:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 954fd854-01ed-3d0d-8227-41d8655a53ad | -2.8169 | -48.601 | 2024-10-06 00:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| e4f424de-b115-3929-a07e-9938337b7ddf | -2.8354 | -48.6004 | 2024-10-06 00:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bfce0c02-b2bd-397e-8dc1-09d31e556705 | -2.847 | -50.4648 | 2024-10-06 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3e4a4930-9752-3b70-b108-5d696fde7be4 | -3.0405 | -53.037 | 2024-10-06 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 750775f3-393c-32b8-a745-818ee6e4752f | -3.1053 | -50.4573 | 2024-10-06 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 85d78fa2-6192-3c7f-8a7b-522218240ea7 | -3.1299 | -48.955 | 2024-10-06 00:25:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 383eca74-e1cf-3562-abc8-8af564997a15 | -3.8008 | -41.5989 | 2024-10-06 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 184.8 |
| bf6cbd28-9683-3c37-bc41-7f96bec122a6 | -3.801 | -41.575 | 2024-10-06 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 86a91a73-928e-3a35-867e-77ef7766748b | -3.8196 | -41.5979 | 2024-10-06 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| ed43909d-c9e9-394c-b670-9ffa19ad2b7b | -3.775 | -49.4643 | 2024-10-06 00:25:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 38d8af8b-00b4-35e8-a937-23a81cff88f8 | -3.7934 | -49.4849 | 2024-10-06 00:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| dd83534e-6d56-3c2d-85d9-0a00bd0e036a | -3.7935 | -49.4636 | 2024-10-06 00:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| de554d9a-1f80-3553-8358-e39458929644 | -4.4534 | -47.4757 | 2024-10-06 00:25:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 5d1e99cc-9204-38bb-8752-d8860d195b94 | -4.4536 | -47.4539 | 2024-10-06 00:25:31 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| df37d8c8-5706-340c-889e-54567cc42a95 | -5.5716 | -44.8927 | 2024-10-06 00:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 9d977e88-8d60-3b44-a6c9-83f083ec5867 | -5.5718 | -44.87 | 2024-10-06 00:25:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 0c4984fa-a664-30a9-b73f-661b2d920e6a | -5.5903 | -44.8914 | 2024-10-06 00:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5e4f7509-f7ae-38b8-a33e-c1eb25fdcedd | -5.5905 | -44.8687 | 2024-10-06 00:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| f86961d6-857c-32a3-a2d6-3f55f6c5256e | -5.8214 | -44.1426 | 2024-10-06 00:25:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 0cf51908-07a9-33f9-894d-05bad86fbc8d | -5.8216 | -44.1196 | 2024-10-06 00:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 99189a5a-eced-360f-8296-28836453bd77 | -6.9103 | -47.6916 | 2024-10-06 00:25:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fe3a7278-22f5-3a78-ac20-a220bb96612c | -6.9514 | -59.0666 | 2024-10-06 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 0289323c-db66-34e7-9edb-aedf50c2f120 | -6.9699 | -59.0658 | 2024-10-06 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 49976ec8-4795-3c1f-8ab8-47dbf289fde9 | -7.153 | -59.3092 | 2024-10-06 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4350341f-2912-3383-8fd3-80cb6d6b2781 | -7.1532 | -59.2898 | 2024-10-06 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 01205dcd-8aab-3635-8eb8-22524f66698e | -7.4741 | -72.6801 | 2024-10-06 00:25:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 2f2bc028-18a6-3279-a26f-9b02c93d73ec | -7.87 | -54.8828 | 2024-10-06 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c68248ba-849f-3808-bdee-bedb0da0a41d | -7.8886 | -54.8817 | 2024-10-06 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e5cbc948-5d1e-381a-9120-5b6409fe9aa0 | -7.9639 | -54.7764 | 2024-10-06 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| db3ee321-893a-3746-b9d1-3435dae1cfed | -7.964 | -54.7562 | 2024-10-06 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| aaabf0b0-d835-325c-b86d-544104dfba37 | -7.9825 | -54.7752 | 2024-10-06 00:25:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 49dc7deb-3bb0-3b52-b466-58431e81b6d0 | -7.9826 | -54.7551 | 2024-10-06 00:25:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 0157def1-a665-3705-9d03-ed6e6229a909 | -8.2139 | -61.2022 | 2024-10-06 00:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2c3fd1c1-ed32-30d8-b3e7-d532d89befc0 | -8.2324 | -61.2014 | 2024-10-06 00:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7c961344-bf3e-363b-ae14-94c0e792eb07 | -9.1573 | -61.5803 | 2024-10-06 00:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 35b38ffe-91d0-3cc0-989c-2cf1ab4a53c5 | -9.1574 | -61.5611 | 2024-10-06 00:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d266a01b-8f0a-3d87-93c5-8430196c17e1 | -9.1759 | -61.5794 | 2024-10-06 00:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 75b925cc-a670-3271-b965-8e201bb89b07 | -9.176 | -61.5603 | 2024-10-06 00:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 680cef1e-979a-3b23-adf8-af29d34b1f2b | -9.3275 | -46.5609 | 2024-10-06 00:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 1849d7ef-798b-3471-bf7f-96452b826b95 | -9.3278 | -46.5385 | 2024-10-06 00:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 97edfee8-df09-3f1c-a35a-345784e631da | -9.3464 | -46.5589 | 2024-10-06 00:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| 3183ea20-e21e-3956-8b29-a012cbae27a4 | -9.3467 | -46.5365 | 2024-10-06 00:25:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 197.9 |
| 5d11ceb4-805f-3915-8bbe-09834d9703f0 | -9.688 | -47.8308 | 2024-10-06 00:26:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 1b07ccaf-547f-3d18-8746-1da045cc6eb2 | -9.8802 | -59.5008 | 2024-10-06 00:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ce886c04-d9c5-38f6-b6e5-cee6b272c711 | -10.6962 | -53.0354 | 2024-10-06 00:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6a533720-d1f0-3f3d-9143-6c3c24c7b3f1 | -11.0966 | -54.2336 | 2024-10-06 00:26:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 52807f5c-9948-31d0-acfe-901997afbcbd | -12.0211 | -63.7478 | 2024-10-06 00:26:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 124.8 |
| fad8de38-8cf7-3412-97c6-47b1560f237d | -12.5066 | -47.5705 | 2024-10-06 00:26:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 756067e8-9b0b-3245-8fd3-2e539786e532 | -12.6089 | -53.1338 | 2024-10-06 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| bab2b5ee-8a5e-3600-9691-3c3e916837a9 | -12.6092 | -53.1129 | 2024-10-06 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 44d1b8ff-9344-36a2-a5b5-139ed2f35769 | -12.628 | -53.1317 | 2024-10-06 00:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 158.3 |
| fc9c4f02-8a26-33f2-b4a0-bc48df9c2d89 | -12.6283 | -53.1108 | 2024-10-06 00:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 6c2b926c-f286-3c56-926e-aa02be47b17b | -12.6471 | -53.1296 | 2024-10-06 00:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| f12bd9c6-2a9a-3ee3-86ef-4320a14281fd | -12.6474 | -53.1088 | 2024-10-06 00:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 149.1 |
| dc13e139-03ac-3bef-8e72-cbcd1d8b1cc5 | -12.6532 | -54.0415 | 2024-10-06 00:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 78256141-1f32-30ca-9b5f-6dbc8dfe359c | -12.6535 | -54.0208 | 2024-10-06 00:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 71873dcd-9a46-3a77-ab27-7bfe79146166 | -12.6723 | -54.0395 | 2024-10-06 00:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 842c31a0-c145-3672-96bf-c4bb70c1c8dc | -12.763 | -50.5352 | 2024-10-06 00:26:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 203.2 |
| bb49d935-ac59-39c8-8d48-5e4a3b010297 | -16.3959 | -57.3641 | 2024-10-06 00:26:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| c8f3bbf6-4c7b-3719-b397-f5f641ee8014 | -16.4362 | -57.278 | 2024-10-06 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 71dca9b9-706d-3663-a185-7096e61a5e3f | -16.5745 | -57.16 | 2024-10-06 00:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 30da7170-5038-3267-9679-8ce5f61bb997 | -16.614 | -55.9214 | 2024-10-06 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 170.8 |
| b8def0c0-dd4b-3776-93d3-7475e3d63c7c | -16.6143 | -55.9007 | 2024-10-06 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 147.0 |
| 6841a2d0-4b72-3fab-9c53-f1078eb33b8b | -16.6395 | -55.566 | 2024-10-06 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 5e08887d-d6cb-3e59-9245-c61896f8bb60 | -16.6398 | -55.5452 | 2024-10-06 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 189.5 |
| afed3a77-287c-3f0e-b6dc-825b5b3863ca | -16.6402 | -55.5243 | 2024-10-06 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 130.5 |
| b5720010-3119-33df-a104-594cdac224fa | -16.6329 | -57.1738 | 2024-10-06 00:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| f4f9cec7-ca7e-3b9d-8990-2d2bb62c8f39 | -16.6871 | -57.4536 | 2024-10-06 00:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| db3e9b32-3526-3ffc-b3e3-d6e95fa6df70 | -16.7647 | -57.4856 | 2024-10-06 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 1cb35140-ae88-3bfc-8b75-351bd832c13b | -16.8238 | -57.4584 | 2024-10-06 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 8fee075f-d40e-3dfa-bc59-ebaa19641245 | -16.8672 | -54.8485 | 2024-10-06 00:26:41 | GOES-16 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 58432d5d-f072-310e-9a8e-b2a98841a073 | -16.838 | -57.8036 | 2024-10-06 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 8de15f65-5e48-3a9e-8899-63dfd802613e | -16.9283 | -55.8405 | 2024-10-06 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.7 |
| 239ad482-4414-3320-b148-86a57273b7bd | -16.9287 | -55.8197 | 2024-10-06 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.0 |
| 83a52346-4de0-39a2-99b3-1a0ebb42dc5a | -16.9348 | -56.625 | 2024-10-06 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.6 |
| f50a9f4b-9eff-306e-bc6b-35f2e4405b1b | -16.9545 | -56.6226 | 2024-10-06 00:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 107.7 |
| f136871b-aa8f-3aac-9bf0-c94554329032 | -17.3837 | -42.6483 | 2024-10-06 00:26:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d7520c2d-9c46-3b24-b542-b1c2506dd8de | -17.0007 | -55.0607 | 2024-10-06 00:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 39fdc890-f9c0-3ede-83d0-a2bcc2e1cfef | -17.0203 | -55.0581 | 2024-10-06 00:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 113.2 |
| b16049c4-fb78-3756-a5b0-a47d9b14438b | -17.0207 | -55.0371 | 2024-10-06 00:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 2336722e-0d31-3037-9900-8f9fd655bc97 | -17.1182 | -57.4039 | 2024-10-06 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 52003d37-1efc-35fe-ae90-f98e10ce7d60 | -17.1284 | -56.7661 | 2024-10-06 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 423300da-da4d-3e4c-9ede-93b8df826f83 | -17.1375 | -57.4221 | 2024-10-06 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| 16ab685e-9689-3d83-b2f8-82ff7479d835 | -17.1571 | -57.4198 | 2024-10-06 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.8 |
| 974950ec-fecc-3f02-ba02-e34d11c8f014 | -17.812 | -53.7859 | 2024-10-06 00:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 005293f7-5dea-3c2e-b11a-10d9e4966a6e | -17.8125 | -53.7645 | 2024-10-06 00:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |


[Clique aqui para ver as próximas entradas](README4.md)
