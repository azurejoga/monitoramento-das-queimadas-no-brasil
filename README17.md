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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd79ae61-fbfc-32a4-89e7-c50441b8bb17 | -2.9051 | -45.1918 | 2024-10-21 01:35:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| cf9ae902-e9f0-3501-831a-119c05cc0a90 | -2.9852 | -53.0587 | 2024-10-21 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e49ddb52-146d-3706-902f-418d2dd9cf5f | -2.9853 | -53.0384 | 2024-10-21 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 84852fa0-f598-3248-8b0b-eff8cacb7439 | -3.0036 | -53.0583 | 2024-10-21 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a91ff854-4512-32c7-921f-bf133d60ee8a | -3.0037 | -53.038 | 2024-10-21 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 7a55101b-1bb9-3574-9acf-7b640e175a50 | -3.0581 | -53.2395 | 2024-10-21 01:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| a4424c0a-2710-3dc1-b716-a42d0494c0a1 | -3.0765 | -53.239 | 2024-10-21 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| ee8fdaef-7832-303a-80a3-29590a411b4e | -3.1138 | -53.1163 | 2024-10-21 01:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 75d00c53-f708-3ac6-a1ff-9ab2a581af08 | -3.1962 | -50.8099 | 2024-10-21 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 7a18f6f5-abee-3064-98a9-7bdf9459d88f | -3.1963 | -50.789 | 2024-10-21 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| af996bbc-6a19-307e-8569-e500a722b54e | -3.2146 | -50.8093 | 2024-10-21 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| aa648ff0-5666-3a13-acc8-1a6dd11b07a8 | -3.2147 | -50.7884 | 2024-10-21 01:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a1d93fe9-c937-35e8-b9b4-33c61d0caea7 | 1.0433 | -51.1465 | 2024-10-21 01:35:24 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 851b7467-6963-34ca-a303-e17882ec8b21 | 1.0377 | -51.171001 | 2024-10-21 01:35:24 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 16716a0d-2afb-3168-987d-cd2fc4229dff | -3.7752 | -53.4012 | 2024-10-21 01:35:28 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bab16e95-94cf-3a4a-b82e-7757c95193c8 | -5.6707 | -46.4363 | 2024-10-21 01:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0a77d3ea-c418-3e25-8fb5-b6812ce4604f | -5.6892 | -46.4572 | 2024-10-21 01:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| a28b5941-4c7f-35a4-aa9a-0459142b8f6e | -5.6894 | -46.435 | 2024-10-21 01:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 213.5 |
| 72a0a691-bc2a-3cce-8cf1-278ee1c9a6e2 | -5.6896 | -46.4128 | 2024-10-21 01:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| f020c652-a632-380e-8268-14e75b02e0dc | -5.7081 | -46.4338 | 2024-10-21 01:35:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9366850f-4520-3bac-8cac-ae3bdc275b90 | -9.3718 | -66.4891 | 2024-10-21 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 11995c5f-47c2-39a2-80ba-8c9b5ebffb6e | -12.4778 | -63.1885 | 2024-10-21 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 30.4 |
| c8848338-86d8-3c02-bee6-811b4cc1f1b5 | -12.4967 | -63.1874 | 2024-10-21 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 31.8 |
| c08aa9c9-a8bd-3c2b-b28b-04a3203bf13c | -12.5147 | -63.3014 | 2024-10-21 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5f6474af-9f2e-3353-bd00-dd83878475bf | -12.5168 | -63.0329 | 2024-10-21 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 7f21f36b-0b0c-3f86-9c9d-a8e8531c7fc0 | -12.5357 | -63.0319 | 2024-10-21 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 50a08a11-d62b-32eb-b845-ae9fc45b01e9 | 2.7327 | -60.093399 | 2024-10-21 01:36:24 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 33f87b25-97fd-37e4-b275-d26863466e56 | -17.7065 | -57.4569 | 2024-10-21 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| f39e5ccc-ac23-3ad9-bf57-cdf3728025fe | -17.7259 | -57.4751 | 2024-10-21 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| fdd6d180-6ffb-3dee-9f46-5d7f42916b72 | -17.7262 | -57.4545 | 2024-10-21 01:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| de6c2ca5-155e-31f7-8ddd-fa9dd7ce1145 | -18.263 | -56.1021 | 2024-10-21 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 0b204f04-86bb-3f26-b7bd-30e3e3911e5f | -18.2828 | -56.0994 | 2024-10-21 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.4 |
| d5608b42-394c-3c12-94a6-195ecd733760 | -18.2832 | -56.0785 | 2024-10-21 01:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| e14dd257-0791-385c-9943-05369676371b | -1.2018 | -53.6366 | 2024-10-21 01:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 1cff6793-c868-3234-8e06-1dc8549aaecc | -1.1835 | -53.6166 | 2024-10-21 01:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 429bdf1b-dc43-3463-988b-1380b1850e24 | -1.1834 | -53.6368 | 2024-10-21 01:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 1fb3a68a-97e9-3454-b0e7-9667375fc53b | -2.2671 | -47.0775 | 2024-10-21 01:45:19 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 87b5a744-2f9f-3dd7-9718-25c0622c054e | -2.2199 | -50.4594 | 2024-10-21 01:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| b1f43c96-518a-3677-b4fb-cac4e80478ca | -2.4824 | -49.102 | 2024-10-21 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 5017fe23-6cc1-3997-93ab-b0b772830bc0 | -2.4824 | -49.1233 | 2024-10-21 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 42c3f2fd-be8a-3a5e-bb6a-734b2f63230e | -2.464 | -49.1024 | 2024-10-21 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 7e1fef8a-716a-31e4-8018-2ac401f9d83d | -2.8069 | -51.3613 | 2024-10-21 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 854dc551-fef1-3bea-ab33-94332ad8a905 | -2.7885 | -51.3618 | 2024-10-21 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6492298b-34d0-35c9-a0f1-058b6a0e3fe5 | -2.7774 | -49.2854 | 2024-10-21 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| be5533e6-9af7-3942-b1a7-55a613464b4d | -2.7773 | -49.3067 | 2024-10-21 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 35446520-112e-3eef-8677-cc309d6770c1 | -2.9051 | -45.1918 | 2024-10-21 01:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 24b263fe-1f1d-39d3-b014-8657536bfbc4 | -2.905 | -45.2143 | 2024-10-21 01:45:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |
| e455151e-8bf9-3213-9111-b7ff900b417b | -2.8556 | -53.3256 | 2024-10-21 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 18e29a30-ceb1-3a7e-946e-2a04c4be6fc8 | -2.8555 | -53.3459 | 2024-10-21 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c72797c8-5fdb-3139-b856-8b4d37fc0f18 | -2.8668 | -45.4631 | 2024-10-21 01:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8645068e-6097-3787-8690-7c46b6de722c | -2.8372 | -53.3261 | 2024-10-21 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 4f5d8bcb-2a31-3fb1-896d-307e479e77b3 | -2.8371 | -53.3463 | 2024-10-21 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 37042d8e-75cd-3387-8319-35277a7c6c12 | -2.8482 | -45.4637 | 2024-10-21 01:45:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.5 |
| cfc038f1-bc8b-3570-a77b-4becb6258f62 | -3.0581 | -53.2395 | 2024-10-21 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 8679154e-c041-34d0-92b6-d8fe5f4e00e0 | -3.0176 | -54.3489 | 2024-10-21 01:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| f73b4d4c-4718-389a-a320-d36b809c6daf | -3.0037 | -53.038 | 2024-10-21 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 047c6ec5-1e9b-3ebd-a456-2730059875a3 | -3.0036 | -53.0583 | 2024-10-21 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2a25b9bf-b0e0-3a0c-bc02-a0e0937cb624 | -2.9853 | -53.0384 | 2024-10-21 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9a5891fb-3afe-336f-85b7-ee2a5bc5657a | -2.9852 | -53.0587 | 2024-10-21 01:45:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 1da3b7b3-0934-3576-bf0e-6ceefea234c3 | -3.2146 | -50.8093 | 2024-10-21 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b113888c-03f1-321f-b395-ab71d6a36073 | -3.1138 | -53.1163 | 2024-10-21 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 21ada8e0-ea44-3165-989d-23c5becde799 | -3.0765 | -53.239 | 2024-10-21 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 57fb12c6-4514-3e12-90a3-fddbe328c201 | -3.2585 | -53.78 | 2024-10-21 01:45:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| acb014ba-bb98-3402-a682-72947b3ab7b1 | -5.7083 | -46.4115 | 2024-10-21 01:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| cabf993d-eae3-30fd-9321-b4b372ef5d83 | -5.7081 | -46.4338 | 2024-10-21 01:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| eae899bb-191e-37f8-930e-2370e2040d41 | -5.6896 | -46.4128 | 2024-10-21 01:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 73607f10-4241-3bbf-a207-873ff87541b7 | -5.6894 | -46.435 | 2024-10-21 01:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 191.4 |
| b5f7bd21-ea7f-3720-b6d8-05310b940ac4 | -5.6892 | -46.4572 | 2024-10-21 01:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 2de0873d-9992-3a14-9ae0-ca68644c384d | -5.6707 | -46.4363 | 2024-10-21 01:45:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| af10cbfc-abef-3674-a6cc-2ad91f1fc3b4 | -9.3718 | -66.4891 | 2024-10-21 01:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 709cecda-ef19-3e47-a22b-6385ad0ac483 | -12.4778 | -63.1885 | 2024-10-21 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d80a62e5-0460-364f-89ce-58d6af28c582 | -12.5357 | -63.0319 | 2024-10-21 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7a358bed-1e17-33cc-942e-eb00bc13d705 | -12.5336 | -63.3003 | 2024-10-21 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| afa6ba95-6e00-3ba4-9bce-a226a99ce7a2 | -12.5168 | -63.0329 | 2024-10-21 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| c6c0c198-42fa-3426-93df-c2e0d66e3339 | -12.5147 | -63.3014 | 2024-10-21 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f17b1176-85b5-3d31-b310-589e70628c69 | -17.8045 | -57.4861 | 2024-10-21 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| f23a26d6-97ec-3c07-a84e-cc00307f83b8 | -17.7262 | -57.4545 | 2024-10-21 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 48c7353f-53ab-35d2-9d97-591ddd02cd06 | -17.7259 | -57.4751 | 2024-10-21 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 9e813c7d-d665-3115-aa49-cceeaaaf653f | -17.7065 | -57.4569 | 2024-10-21 01:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 643fa52f-69a3-3903-aa2a-10df68c54f81 | -18.2832 | -56.0785 | 2024-10-21 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 4ffe085e-40f9-3ad4-8cb1-50bdafb8b093 | -18.2828 | -56.0994 | 2024-10-21 01:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.5 |
| 902049ae-a5f5-33ca-9f14-b1c18e6f0a3d | -1.1834 | -53.6368 | 2024-10-21 01:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 24cd7608-cfe7-32cc-ac92-3e04730f8f6d | -1.2018 | -53.6366 | 2024-10-21 01:55:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ef5883ab-353d-3b1c-88fa-e5b6a546875b | -2.2199 | -50.4594 | 2024-10-21 01:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f38293c6-59e5-3cd2-a69e-82acb82f2aa0 | -2.4824 | -49.1233 | 2024-10-21 01:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 45f2f165-fff8-3467-b4c9-5b8ee49119a2 | -2.4824 | -49.102 | 2024-10-21 01:55:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| ad88dd22-1778-30e7-b293-240aa6921235 | -2.9051 | -45.1918 | 2024-10-21 01:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 5627048f-a93e-38c8-aefb-3a75eed27f40 | -2.7773 | -49.3067 | 2024-10-21 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d1c3d530-8a96-38e1-9804-b1f83d148100 | -2.8069 | -51.3613 | 2024-10-21 01:55:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8fc28e21-8cc1-3a45-9362-7671d4f942bf | -2.8371 | -53.3463 | 2024-10-21 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 7f8d68f0-fafd-3e2b-aefb-31f6f32167ca | -2.8372 | -53.3261 | 2024-10-21 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| c4b01fda-87a1-3b4f-af02-ac5e3055991e | -2.8668 | -45.4631 | 2024-10-21 01:55:22 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5ec20e5d-438d-37a4-8ad2-0e670e151c4c | -2.8556 | -53.3256 | 2024-10-21 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d1b8ed8d-7c9f-3131-84c0-a8f63605f3b4 | -2.905 | -45.2143 | 2024-10-21 01:55:22 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 794c5b1b-ca67-31ab-8851-c5f83fd38e37 | -3.0036 | -53.0583 | 2024-10-21 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 63730f02-74fe-3803-981e-53a676dd3e70 | -3.0037 | -53.038 | 2024-10-21 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2513a2d1-b842-3c17-935b-7de92a20f6d6 | -3.1138 | -53.1163 | 2024-10-21 01:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 95e2ed2c-3805-3733-a960-b20fa74d0575 | -3.2585 | -53.78 | 2024-10-21 01:55:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 30b125ee-7f02-3b62-8268-25b7aa78aaee | -4.8758 | -48.2145 | 2024-10-21 01:55:34 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 20e8f315-35dc-36a7-9ae5-d4885e7a5b41 | -5.6707 | -46.4363 | 2024-10-21 01:55:38 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |


[Clique aqui para ver as próximas entradas](README18.md)
