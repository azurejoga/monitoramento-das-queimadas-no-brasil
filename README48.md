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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be4af446-e6b8-358c-8957-d92185a91630 | -9.3672 | -63.6972 | 2024-09-27 03:36:00 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f8ae1d6f-5f63-37b5-9d14-106ae7c9905c | -9.5829 | -50.137 | 2024-09-27 03:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 08669ce5-76f5-3d9f-9baf-b05ff213e3a5 | -9.6018 | -50.1352 | 2024-09-27 03:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 21775602-bf4b-34f2-8ff9-fc595c6481a2 | -9.602 | -50.1139 | 2024-09-27 03:36:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a84d8187-923d-326e-85cb-9d6143f3f0ce | -10.1309 | -50.019 | 2024-09-27 03:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7d246415-9337-3539-bb22-9619c1a84e8d | -10.1312 | -49.9976 | 2024-09-27 03:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| bba0151d-6483-33bd-8325-f396d07c0301 | -10.3672 | -53.7858 | 2024-09-27 03:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 4c2578d5-4833-30b3-99df-e25d96dfaf9e | -10.7214 | -51.0657 | 2024-09-27 03:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6cc5d285-ac19-399c-95f4-9a1c8249ad0c | -10.9264 | -54.2692 | 2024-09-27 03:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| f6addc07-c132-3e05-a23e-891b9ffeb580 | -10.9267 | -54.2488 | 2024-09-27 03:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 2c769ff1-35e7-3321-a6e2-a9074c9c584a | -11.2534 | -47.1142 | 2024-09-27 03:36:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| df5db542-d0b4-3d93-9f76-1e79391cc15b | -11.2223 | -54.7735 | 2024-09-27 03:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d912ff8b-f65d-3dbd-a632-c209de03819d | -12.6824 | -54.6968 | 2024-09-27 03:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 5d6f100a-eef3-3973-b733-9220d2a038b2 | -16.1189 | -51.9436 | 2024-09-27 03:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| f34326e4-57cf-3ffa-b835-78c682c8aaa3 | -16.7133 | -55.8262 | 2024-09-27 03:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 3b091207-638d-3192-9795-b295d911cd3a | -16.7325 | -55.8445 | 2024-09-27 03:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| c686c74d-4606-3ec6-9171-acff1db387ce | -16.7329 | -55.8237 | 2024-09-27 03:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| e3586c31-2db2-3670-aa81-ccfb96e216a8 | -16.893 | -58.0417 | 2024-09-27 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.0 |
| 3f98366c-b82a-30ca-9f5f-024653fc163e | -16.8933 | -58.0213 | 2024-09-27 03:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| e77a4ad8-47c8-37e1-8c1d-d12113a44562 | -17.0209 | -56.1603 | 2024-09-27 03:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 32f28166-9ee6-3c35-a6bf-b6490f70d9e6 | -17.0405 | -56.1578 | 2024-09-27 03:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 2b77b66c-6bcd-30ee-acf4-8cba7df6200a | -18.9298 | -49.1861 | 2024-09-27 03:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 0286fe35-719b-3fd9-9694-27ddded03053 | -19.3977 | -42.5753 | 2024-09-27 03:36:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.0 |
| 2535d796-ba64-3084-811a-471f71521696 | -19.6136 | -42.8159 | 2024-09-27 03:36:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.2 |
| a4d6c81b-46f5-386d-a655-787fd1b55b44 | -20.5199 | -41.952 | 2024-09-27 03:36:59 | GOES-16 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| fc35de13-4142-313f-a559-0fdab0e31588 | -22.2257 | -48.6155 | 2024-09-27 03:37:08 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.5 |
| ca0f40df-e53a-33df-932b-c260c2f9c9d6 | -22.7433 | -44.8035 | 2024-09-27 03:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.1 |
| aadfa115-a3db-3132-a1db-96c55c78a502 | -22.7442 | -44.7785 | 2024-09-27 03:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.0 |
| ca7708e2-994e-3907-832c-fd63dccfc586 | -2.3579 | -47.6206 | 2024-09-27 03:45:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d2ad737e-b1b3-355b-97b1-55e80ccb00eb | -2.358 | -47.5989 | 2024-09-27 03:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 15fca24e-4692-3f52-801f-c1b63106ac8f | -2.6783 | -57.6087 | 2024-09-27 03:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 0df01242-1f85-32a3-a227-88b2cd6c205d | -2.6783 | -57.5893 | 2024-09-27 03:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 0b89717c-5de5-3dd3-87ed-bf44a2bb5028 | -2.8611 | -51.6699 | 2024-09-27 03:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 41fd1e20-2761-3fc7-9110-33d34b57c491 | -3.0107 | -51.0652 | 2024-09-27 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4908bf99-af93-339d-8e4f-36fa8ac5e767 | -2.8795 | -51.6695 | 2024-09-27 03:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d439ce7e-5861-391e-8c21-9d22e5906f8b | -3.2136 | -46.7843 | 2024-09-27 03:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| e7a7d136-41ff-3dd8-926e-64ad1fb4f20b | -3.2135 | -46.8063 | 2024-09-27 03:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e522e869-3266-3cca-8c6f-e77459c2a068 | -5.397 | -43.4332 | 2024-09-27 03:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f24e7efc-cd33-3b30-b666-8bcee158d026 | -7.5289 | -61.3825 | 2024-09-27 03:45:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| cd74bf78-d6c3-3735-afbf-b5a32ececa0e | -7.5684 | -49.1786 | 2024-09-27 03:45:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 86.5 |
| f79c409d-7026-33fb-984d-8121422e6b19 | -7.5682 | -49.2001 | 2024-09-27 03:45:49 | GOES-16 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 9b6fd276-382c-3b46-a0bf-e7b67bffd851 | -7.7885 | -61.2008 | 2024-09-27 03:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e96e6b3a-41f6-3227-a261-ad415dba0f6f | -7.7886 | -61.1817 | 2024-09-27 03:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| f00308ab-2218-3985-8a67-21ecad3f4262 | -7.77 | -61.2015 | 2024-09-27 03:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.2 |
| 939a8c90-cd92-3c37-be27-53539048d2c1 | -7.7701 | -61.1825 | 2024-09-27 03:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 796d9fe0-84f0-3528-ba5e-56c2d15cd7c1 | -8.1394 | -61.2817 | 2024-09-27 03:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 353fe993-0bb3-3af0-8600-966e48fc1ebc | -8.6101 | -63.1226 | 2024-09-27 03:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9f8af619-c18a-30aa-8a31-4526825d3c93 | -8.8774 | -61.8028 | 2024-09-27 03:45:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| f9a0d31f-f7d2-367e-b8da-d1137bf4c50d | -8.8775 | -61.7837 | 2024-09-27 03:45:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9658dd2b-e002-3693-bf98-41bc066b32f2 | -9.047 | -61.3943 | 2024-09-27 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 5e4a1df0-7f0e-3b37-98a9-139d1e7331a9 | -9.1029 | -61.3726 | 2024-09-27 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 1261775d-4fe7-3aaa-bdef-96e066f74bc3 | -9.103 | -61.3534 | 2024-09-27 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| e5a23a84-3bd1-3562-be4d-78a64eaed47b | -9.1032 | -61.3343 | 2024-09-27 03:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 83f01d3d-d002-3a0a-829b-fece07a63ec2 | -9.1215 | -61.3717 | 2024-09-27 03:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| fc04186f-53fd-3627-98ad-5bf58de599a4 | -9.1216 | -61.3526 | 2024-09-27 03:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 55b614b2-ce84-32cb-b4a9-680bdba31c33 | -9.5829 | -50.137 | 2024-09-27 03:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 93c0216c-1f72-3b90-b440-fe79b47f4b3f | -9.6018 | -50.1352 | 2024-09-27 03:46:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 160.9 |
| 6699bd55-571d-35c1-86a9-be7ee6989b50 | -10.1309 | -50.019 | 2024-09-27 03:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 9fd32197-3314-3c42-81c5-f9a6a8dfd825 | -10.1312 | -49.9976 | 2024-09-27 03:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| d907d7e7-1951-3caa-a4cc-6cc027f0e9bd | -10.1498 | -50.0171 | 2024-09-27 03:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 7f463faa-5b10-386e-b9ef-c9c5456a1599 | -10.1501 | -49.9956 | 2024-09-27 03:46:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 74786d13-f0a9-39fa-bdab-18da29e059cb | -10.3672 | -53.7858 | 2024-09-27 03:46:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f2d48f14-27b3-3f0e-b1e6-484e1636aff2 | -10.7214 | -51.0657 | 2024-09-27 03:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 62c78b28-1be2-36b5-bc0f-ec344fa913b8 | -10.9264 | -54.2692 | 2024-09-27 03:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 25776d39-7ff1-3f19-9ea5-dfed855a0455 | -10.9267 | -54.2488 | 2024-09-27 03:46:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| df113872-c842-358c-8515-f49496b08a50 | -11.2034 | -54.7752 | 2024-09-27 03:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 57c2291e-342f-30d1-8ca5-cb0d518dae6f | -11.2223 | -54.7735 | 2024-09-27 03:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 6bf58cdb-790a-3282-a652-0a2acfd51c6a | -11.2692 | -46.1444 | 2024-09-27 03:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 6f55b39b-a3bf-377d-a326-25e300a78e38 | -11.2695 | -46.1216 | 2024-09-27 03:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| a1228658-921b-3632-b466-92b11ef5030b | -11.2887 | -46.1191 | 2024-09-27 03:46:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| ec27c0b1-c19f-3adc-897d-f0ec32ed0bf8 | -16.0793 | -51.9709 | 2024-09-27 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e29138f8-d427-3cfe-837e-935d1521f3f7 | -16.0797 | -51.9494 | 2024-09-27 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| e37ea801-4fd5-34b2-91e2-db6c8669ac58 | -16.0989 | -51.968 | 2024-09-27 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 67813f17-a1d3-3df6-aa64-d8bc7b150870 | -16.0993 | -51.9465 | 2024-09-27 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 210.1 |
| 7de6c762-d6f3-3ca8-a56b-88423e38f93c | -16.1185 | -51.9651 | 2024-09-27 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 224f6046-6144-3d5c-bec7-7cff0865fa9f | -16.1189 | -51.9436 | 2024-09-27 03:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 5220ee1b-b85e-3884-a849-e1d8d41083e7 | -16.7325 | -55.8445 | 2024-09-27 03:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| aee802f8-c6a6-36b5-a3bb-47058f64474d | -16.7329 | -55.8237 | 2024-09-27 03:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| cdabf400-f92d-38a9-a84b-dd1dbe813f51 | -16.893 | -58.0417 | 2024-09-27 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.3 |
| c6ae6661-cba7-365c-aadc-2179d88aa9a4 | -16.8933 | -58.0213 | 2024-09-27 03:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 15a11f87-0288-317e-b6c3-24aa5b4b3090 | -16.9129 | -58.0191 | 2024-09-27 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 1b735a81-01ac-3475-a282-331013fd0cbe | -18.9091 | -49.2129 | 2024-09-27 03:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| ecaa2ed6-b771-30f8-9a3f-a26cbf183c43 | -18.9096 | -49.1902 | 2024-09-27 03:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.0 |
| 4756c3ae-e2fd-35d4-b886-ab61e4476303 | -18.9292 | -49.2089 | 2024-09-27 03:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 97174eb3-6f66-3fa5-9c0c-119df1554a04 | -18.9298 | -49.1861 | 2024-09-27 03:46:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.0 |
| 15603469-6440-36e5-9135-ed3d70abb16b | -19.3977 | -42.5753 | 2024-09-27 03:46:53 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| df680099-b542-3f3f-b335-8907bed94a9b | -19.6129 | -42.8411 | 2024-09-27 03:46:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| fb307966-a145-328f-be64-200f6a80c205 | -19.6136 | -42.8159 | 2024-09-27 03:46:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 138.9 |
| 43b6fbe8-d11b-37a6-97cb-2ac4c59cdf2f | -20.519 | -41.9777 | 2024-09-27 03:46:59 | GOES-16 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 3ef76234-7504-3397-966f-0368d1260b3d | -20.5199 | -41.952 | 2024-09-27 03:46:59 | GOES-16 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| 8491cbf1-2df8-34ba-96d4-7a04bdd9d92c | -11.26757 | -46.12741 | 2024-09-27 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| aaf23274-ac72-35cf-8560-b10ea09313ad | -12.1969 | -43.63755 | 2024-09-27 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9af87fa0-25d8-3505-977e-44cffb011d83 | -11.87585 | -43.83147 | 2024-09-27 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 024cb2cc-97d9-3282-950f-d70c011da79a | -11.87514 | -43.83554 | 2024-09-27 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f019cdb7-aa29-37f1-a800-e1afb3b2994a | -11.8454 | -43.83001 | 2024-09-27 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 322e2a8e-20a2-3d93-aee7-fd59d144c086 | -11.84115 | -43.82922 | 2024-09-27 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cc0c84e-abac-313f-bbf1-1e2435ab4ba5 | -11.69849 | -44.52201 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e05eb0f7-f066-3d9e-bb5a-09d8aba250c3 | -11.66605 | -44.50816 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29333d52-e3fd-3073-bee0-8eacf77b1a1f | -11.66367 | -44.51078 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00ecc43d-0157-3069-a58e-d938aedda522 | -11.66366 | -44.5217 | 2024-09-27 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
