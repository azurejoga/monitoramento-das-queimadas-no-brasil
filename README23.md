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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b4e2ba9-7287-36fe-9e47-11dcffa88177 | -17.1574 | -57.3993 | 2024-10-06 01:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.5 |
| aec020ef-c5b9-3f28-bc56-b9324b9dcfc0 | -17.8323 | -53.7616 | 2024-10-06 01:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 133.3 |
| c4c98af7-816d-3492-bf6d-6828679f0742 | -17.812 | -53.7859 | 2024-10-06 01:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 7dfd7fdb-0c84-31c7-aad0-e1cdcb478733 | -17.8125 | -53.7645 | 2024-10-06 01:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 7939b25b-9006-38e7-a2d6-6be980af9b8c | -17.8319 | -53.7829 | 2024-10-06 01:06:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| d2217d00-1426-3cc1-83d8-4568aecf009c | -21.3794 | -48.6317 | 2024-10-06 01:07:04 | GOES-16 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1d72f2aa-ab5b-3b6d-bde3-8c75855ff25a | -1.7668 | -47.1984 | 2024-10-06 01:15:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2629849f-74ab-3297-ab2a-2ab4ea085648 | -2.6858 | -49.0752 | 2024-10-06 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| cdd31cf8-4a72-3134-bc1a-afc7836621b7 | -2.6859 | -49.0539 | 2024-10-06 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 83de4e7a-3e09-3a6e-895a-3ecebdb228bd | -2.7043 | -49.0747 | 2024-10-06 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| d611a2cf-a36d-37ea-9202-267726741d99 | -2.7043 | -49.0533 | 2024-10-06 01:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| af4d49bf-de7e-335f-9862-6d98bb185f0f | -2.8166 | -48.6867 | 2024-10-06 01:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 67b40bc7-3681-3538-9908-1782a590b4be | -2.8169 | -48.601 | 2024-10-06 01:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a70acae6-edd0-36ba-8041-0f3ccf51a084 | -3.113 | -48.5916 | 2024-10-06 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| e28197ed-efc3-3820-ab62-283463a626f0 | -3.1129 | -48.6131 | 2024-10-06 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| c133da31-236d-3b06-92bc-e25256b04495 | -3.1314 | -48.6125 | 2024-10-06 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| ca6b98fe-385f-352c-8f21-c690d6213090 | -3.1315 | -48.591 | 2024-10-06 01:15:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 16c18261-9142-38fa-8c32-368ea7c2ccbd | -3.7068 | -41.6758 | 2024-10-06 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| f827cd2f-8037-3ef6-8bf0-dfa4816695d0 | -3.8008 | -41.5989 | 2024-10-06 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 168.2 |
| f2e3644f-ab6e-36a5-9ad7-787bb5334344 | -3.801 | -41.575 | 2024-10-06 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 107.5 |
| 0b02c911-bc4b-313c-bce8-90073f07f755 | -3.8196 | -41.5979 | 2024-10-06 01:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| aa84737b-cc88-38ef-99db-430ca6cfcdf6 | -3.775 | -49.4643 | 2024-10-06 01:15:27 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| afd711e4-04bf-3921-8616-fee46fa19151 | -3.7935 | -49.4636 | 2024-10-06 01:15:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 00e87716-3f1f-32b1-8e1d-5b48e73d89d4 | -5.5716 | -44.8927 | 2024-10-06 01:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4e013808-b199-38de-b381-472efd45be01 | -5.5718 | -44.87 | 2024-10-06 01:15:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 0e2cbfb1-ccbc-3eaa-94b7-2f42fadbfaef | -5.5905 | -44.8687 | 2024-10-06 01:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ed9891f9-3062-3c0f-906f-49da0ce2eb38 | -5.8214 | -44.1426 | 2024-10-06 01:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| d70f4e90-18c0-3025-838f-feb4a06410a5 | -5.8216 | -44.1196 | 2024-10-06 01:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 416fc719-aff4-3ef9-85bf-ea8a9f680a54 | -6.9103 | -47.6916 | 2024-10-06 01:15:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 06a474a5-2e98-3db1-b216-71fae0132d1d | -6.9514 | -59.0666 | 2024-10-06 01:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 9eb34d4a-abe7-3287-917d-bbbc003717d2 | -6.9699 | -59.0658 | 2024-10-06 01:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| ee1f0da2-5027-3e84-971f-d3a7123d14ab | -7.1532 | -59.2898 | 2024-10-06 01:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| e8a86367-11d1-3cb4-aa9d-116522e71934 | -7.4741 | -72.6801 | 2024-10-06 01:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| e8a871b7-29f5-3beb-a6a6-32d1a1a63fde | -7.964 | -54.7562 | 2024-10-06 01:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6cff81cb-ebac-39f7-a1a0-8c61168ed881 | -7.9826 | -54.7551 | 2024-10-06 01:15:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 8faaff49-2475-3669-9f4e-afa98a956c77 | -8.2139 | -61.2022 | 2024-10-06 01:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 94b49316-fd51-336a-87e8-e879c3599835 | -8.2324 | -61.2014 | 2024-10-06 01:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 83cde8a7-f28c-345d-8ffc-d0071b854cf5 | -9.1263 | -60.6621 | 2024-10-06 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ba37be39-372d-306a-af53-ed3636cdbf28 | -9.1449 | -60.6612 | 2024-10-06 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f99fa268-fdf8-3897-b30c-25363de4f784 | -9.176 | -61.5603 | 2024-10-06 01:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 01bd384a-b69d-333a-b15f-f55e1215a553 | -9.3275 | -46.5609 | 2024-10-06 01:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 66e5ae28-1e9b-3f25-8110-281ba7d0a374 | -9.3278 | -46.5385 | 2024-10-06 01:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| ce242834-d74c-3cf1-b002-bcdf9db139aa | -9.3464 | -46.5589 | 2024-10-06 01:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 9f8ace04-b77a-375e-b2e1-30cc5d73a799 | -9.3467 | -46.5365 | 2024-10-06 01:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 328.5 |
| 9a876c2a-7aae-38cc-a6d4-ad8a4138b5ec | -9.347 | -46.514 | 2024-10-06 01:15:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| d329a1d7-8475-3706-959d-1cabf9d0a17f | -9.3647 | -51.0898 | 2024-10-06 01:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6fadd775-4350-3691-b719-2118e82255d6 | -9.365 | -51.0687 | 2024-10-06 01:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| aafb266e-07af-37f5-a736-3010562b48fc | -9.3835 | -51.0881 | 2024-10-06 01:15:59 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 8c827aed-41df-3022-82a1-eae3bcc1bf6d | -9.1573 | -61.5803 | 2024-10-06 01:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| dc823f7e-a409-3165-89b8-87d33d4673f4 | -9.1574 | -61.5611 | 2024-10-06 01:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 80018594-74fc-3de9-985e-7bacc9a1477f | -9.1759 | -61.5794 | 2024-10-06 01:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 95f7b7f1-9afc-3961-945e-04c73df5a225 | -9.3638 | -64.319 | 2024-10-06 01:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 17098970-9f11-3eed-ad8b-8c6e5aa1cf24 | -9.8552 | -60.2966 | 2024-10-06 01:16:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 70152afa-de17-32dd-b7cc-2c6c2869beb4 | -10.8153 | -44.7643 | 2024-10-06 01:16:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 225645b0-4f5b-30ce-ae72-ac02a4e131ce | -10.8932 | -52.3726 | 2024-10-06 01:16:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| e0f50678-1d73-33eb-8abb-25b43cb5cb00 | -11.0966 | -54.2336 | 2024-10-06 01:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d909ad49-f311-3b65-9d1a-2e6ce193911b | -11.1155 | -54.2319 | 2024-10-06 01:16:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a518ddf6-ae95-3d04-ade8-e9bf32b2b423 | -12.0211 | -63.7478 | 2024-10-06 01:16:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 93.7 |
| b0ba1847-5235-3de9-9e78-26de2dc92364 | -12.6089 | -53.1338 | 2024-10-06 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7bd24d31-69c7-3c5d-abe5-88af9faa9886 | -12.6092 | -53.1129 | 2024-10-06 01:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b1d7899f-f9d1-3d5a-9040-60583113fec2 | -12.763 | -50.5352 | 2024-10-06 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 4a484f96-de66-3ef4-becf-6f2d72d7273a | -12.7634 | -50.5136 | 2024-10-06 01:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 48d1415d-a59a-33b9-bb29-8a7f8cf1d16a | -12.628 | -53.1317 | 2024-10-06 01:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 19509ec8-a1bf-3c25-8913-ef756b325938 | -12.6283 | -53.1108 | 2024-10-06 01:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3cafbdd4-5e27-37a1-a422-4233aaa09198 | -12.6532 | -54.0415 | 2024-10-06 01:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 0512273d-24eb-342c-b827-8740d897e5ca | -12.6535 | -54.0208 | 2024-10-06 01:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| ba152ab9-356c-3bf6-bf4d-164021930949 | -14.5452 | -48.8247 | 2024-10-06 01:16:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c09fe149-6e50-36e1-a70f-82d819aa3c6d | -14.5646 | -48.8217 | 2024-10-06 01:16:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 5a08b543-3d60-3296-99d0-53438c5836e3 | -16.6871 | -57.4536 | 2024-10-06 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 269f31e7-fd04-3cac-9018-da5abf69156b | -16.7067 | -57.4514 | 2024-10-06 01:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.9 |
| ada33d1b-7a1d-3737-a59d-4f07fec0e3ae | -16.614 | -55.9214 | 2024-10-06 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| dfb5eaf4-d856-3f57-bb3b-0a6ef40e4497 | -16.6395 | -55.566 | 2024-10-06 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| e58fdf36-e841-3016-a1e7-f737559c4418 | -16.6398 | -55.5452 | 2024-10-06 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 172.2 |
| b08308df-dd22-3b67-8996-95e2d4e9ce66 | -16.6402 | -55.5243 | 2024-10-06 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 126.3 |
| 16d51db9-13b9-33ed-8743-4b963cce5eca | -16.7647 | -57.4856 | 2024-10-06 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 7149fffc-8256-323b-bd5b-88c134401f6c | -16.8238 | -57.4584 | 2024-10-06 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 33fb48e2-18fb-3654-9d52-2fecab874ec0 | -16.9283 | -55.8405 | 2024-10-06 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 91cb19cf-947c-3ce3-bd9a-0fff394e08d3 | -16.9348 | -56.625 | 2024-10-06 01:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 106.1 |
| baa31cc0-af0a-3b18-9e5e-22da563f81cb | -16.9545 | -56.6226 | 2024-10-06 01:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.7 |
| a12335a5-9b85-3758-b967-8b236f018938 | -17.3837 | -42.6483 | 2024-10-06 01:16:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 1b194b72-bdde-3f9e-a3f5-3b124414d236 | -17.1178 | -57.4244 | 2024-10-06 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.8 |
| b708786b-3480-36ba-a497-583a6ed69818 | -17.1182 | -57.4039 | 2024-10-06 01:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 7ef682a7-adf3-3ceb-8b2b-562b00bf1cc3 | -17.0203 | -55.0581 | 2024-10-06 01:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 03126cbf-374d-3cce-8cd8-9a1c72a72dfc | -17.1375 | -57.4221 | 2024-10-06 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.4 |
| aa130005-d4a9-3e14-81d2-a27a0b4b1c04 | -17.1574 | -57.3993 | 2024-10-06 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 640fd2c9-d401-3b2e-8275-0a6e82c67301 | -17.1571 | -57.4198 | 2024-10-06 01:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.4 |
| 8881cf49-2de9-3a9f-a509-a31a47791858 | -17.812 | -53.7859 | 2024-10-06 01:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 8e5e4ece-1226-38c0-8f6c-74fc43ce6645 | -18.6586 | -57.2759 | 2024-10-06 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| dd882318-5da1-33c1-8f6a-4f09abba3ba7 | -1.7668 | -47.1984 | 2024-10-06 01:25:16 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4ea7e8d4-aede-3f65-88ed-a9328af99a93 | -2.6858 | -49.0752 | 2024-10-06 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 70b08364-2795-342c-a74f-7c2c7b451982 | -2.6859 | -49.0539 | 2024-10-06 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 17bc9077-b0de-34f1-9264-3fef1dcad20a | -2.7043 | -49.0747 | 2024-10-06 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 54800747-58f3-3ced-bc19-82cd2461afcb | -2.7043 | -49.0533 | 2024-10-06 01:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 82cdf997-5f78-3e64-82f4-bef0fafb795f | -2.7981 | -48.6873 | 2024-10-06 01:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| b899a299-ae6c-3dac-a892-012caed2ec05 | -2.8166 | -48.6867 | 2024-10-06 01:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 91d6199d-1b99-3091-a29c-953c0f971616 | -2.8169 | -48.601 | 2024-10-06 01:25:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 54218619-f581-3c3b-b7f1-35ab89d83509 | -3.1053 | -50.4573 | 2024-10-06 01:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 2e444742-9d16-3b38-8495-8c46207af696 | -3.1129 | -48.6131 | 2024-10-06 01:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b3890f59-0439-38c1-896f-3c133073e55d | -3.1314 | -48.6125 | 2024-10-06 01:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| e7d896d2-b40d-35b7-bf38-17800687a59d | -3.1315 | -48.591 | 2024-10-06 01:25:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |


[Clique aqui para ver as próximas entradas](README24.md)
