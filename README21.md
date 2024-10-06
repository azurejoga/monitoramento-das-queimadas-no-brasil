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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dfc4caf-d0cd-3518-b63c-f3e1e80d9b5a | -3.90502 | -48.34528 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| 3d0f9621-676f-3cb2-ba20-8dfc588562c0 | -3.8974 | -48.3554 | 2024-10-06 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13c37798-cecf-38ff-acc1-97045b34b1c9 | -3.84464 | -46.467 | 2024-10-06 00:54:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 79c51cf3-2332-3cbb-bfcd-eeef43b2c0b3 | -3.82838 | -49.45628 | 2024-10-06 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4beb443d-651f-30e3-af5e-f57af3c81878 | -3.82707 | -49.44688 | 2024-10-06 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06f1cb86-8854-37ed-9910-c00062de2c24 | -3.82259 | -47.49466 | 2024-10-06 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f790a736-e78a-365f-b982-4b00d9a7d537 | -3.79321 | -49.47075 | 2024-10-06 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c34d2764-b346-3364-8f88-a493db84ba26 | -3.79192 | -49.46135 | 2024-10-06 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d378d5d6-767c-385d-b5a9-2e9f0efd0d1d | -3.78409 | -49.47198 | 2024-10-06 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 70d5113c-f916-36c3-b073-8cf2e2d181db | -3.7828 | -49.46259 | 2024-10-06 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3a3fabbc-f769-30d6-b07d-d03a4ff2b8a2 | -3.77675 | -47.61813 | 2024-10-06 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 528ca97c-ed6f-3217-b944-95b5be66f404 | -3.69361 | -47.61788 | 2024-10-06 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2010e593-5add-3f12-b41f-3f9b755768c3 | -3.61449 | -47.5184 | 2024-10-06 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 071376f8-458a-3a80-a280-15205e8b9de1 | -3.61325 | -47.50956 | 2024-10-06 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a94095fd-587b-3580-9eaa-3c72c85adcdf | -3.60564 | -47.51966 | 2024-10-06 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8e908cf5-49ab-3732-aca9-5beee6198c00 | -3.58094 | -50.39546 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4fb73e41-899e-303d-b9b9-64c894637997 | -3.51115 | -50.84361 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3d2ba883-d412-39f6-a01d-4aadfd761c6a | -3.50585 | -50.27052 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| b2926007-bd63-3356-9770-dec062de6585 | -3.50482 | -48.91389 | 2024-10-06 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c1544d46-29c7-39c7-adc2-3c95a939630f | -3.4964 | -50.27183 | 2024-10-06 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9e41467c-3213-3e90-b99a-b9c813ab8af4 | -3.49588 | -48.91512 | 2024-10-06 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4db836cb-81c7-37fc-8864-b76ddb6e1017 | -2.6858 | -49.0752 | 2024-10-06 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 351.6 |
| edff25b0-4d22-358e-b2cf-195ccb8d6ab7 | -2.6859 | -49.0539 | 2024-10-06 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 204.5 |
| cb8fec58-80c7-3a5c-b7f3-098ee83c061e | -2.7043 | -49.0747 | 2024-10-06 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 195.1 |
| 14143335-9f68-3e62-b66c-ec4afff54f70 | -2.7043 | -49.0533 | 2024-10-06 00:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| e235e4ff-cf45-3fd2-bab6-4a7920db8a5c | -2.8169 | -48.601 | 2024-10-06 00:55:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 9505e828-71b6-354e-b889-2227ebda1379 | -3.1129 | -48.6131 | 2024-10-06 00:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| b4adc6bd-5c4a-3fed-a52a-017ba8fe4d14 | -3.1314 | -48.6125 | 2024-10-06 00:55:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 50db948d-628e-33e9-851f-3563d1829514 | -3.7068 | -41.6758 | 2024-10-06 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| c0b0df96-e5ea-30fd-965d-d1191ea3de56 | -3.8008 | -41.5989 | 2024-10-06 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 216.1 |
| c272f46a-9efd-3ee9-b1b9-9038b7443fc8 | -3.801 | -41.575 | 2024-10-06 00:55:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 399f6d2d-7458-39d8-9c8c-54b67dbbf5d0 | -3.7935 | -49.4636 | 2024-10-06 00:55:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| b99e054a-3906-34e5-b5c7-b7902540f614 | -4.1854 | -48.8718 | 2024-10-06 00:55:30 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 4f64b366-ee36-3170-ab20-e4346eef7c75 | -5.5716 | -44.8927 | 2024-10-06 00:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| a84f1072-8df3-35dc-a425-b4d2a9485ffa | -5.5718 | -44.87 | 2024-10-06 00:55:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 179.2 |
| e8a92f78-a25f-3c0b-8432-9bea017194f6 | -5.5905 | -44.8687 | 2024-10-06 00:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| db4337ee-b88c-3e25-8180-2327a2366555 | -5.8214 | -44.1426 | 2024-10-06 00:55:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 8651fd65-d70a-3838-8942-5edbbc88d252 | -5.8216 | -44.1196 | 2024-10-06 00:55:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 1d3cf5a5-d462-3aef-8fb1-47f4415f9cb9 | -6.9103 | -47.6916 | 2024-10-06 00:55:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 18cea163-a783-36e6-ad40-54454246df90 | -6.9514 | -59.0666 | 2024-10-06 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a8cd2753-ccd4-3d8d-83fc-340767352aa7 | -6.9699 | -59.0658 | 2024-10-06 00:55:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 54ce9b10-3d6d-3724-abbb-4cc9edf78399 | -7.1532 | -59.2898 | 2024-10-06 00:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a1dc2211-5a76-3f1b-8528-8de7c429b3ed | -7.4741 | -72.6801 | 2024-10-06 00:55:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 8da9c2ad-2804-317a-821a-fdac42bfc177 | -7.87 | -54.8828 | 2024-10-06 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a8eb57c3-834c-3c80-bb4e-59d5a105fe34 | -7.9639 | -54.7764 | 2024-10-06 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 89f20bd8-2525-370d-838c-f34343ea7543 | -7.964 | -54.7562 | 2024-10-06 00:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| a2cd8289-4121-3220-af13-f052be72c8c4 | -7.9825 | -54.7752 | 2024-10-06 00:55:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b9c6d1a0-18a0-3ac7-b491-d8354bbd4b15 | -7.9826 | -54.7551 | 2024-10-06 00:55:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 85f201d5-f939-3763-938e-024d82b19e0d | -8.2139 | -61.2022 | 2024-10-06 00:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 96c02c15-2b3b-3f76-88e1-380c5a410e03 | -9.1263 | -60.6621 | 2024-10-06 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 5875b8bb-f3a8-364a-ac04-1e94bcd52b0b | -9.1449 | -60.6612 | 2024-10-06 00:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 314c791f-ad71-38b4-b486-fd4b1e13d7b0 | -9.1573 | -61.5803 | 2024-10-06 00:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0f4e373b-7b0c-3362-b2ce-b3c888993931 | -9.1574 | -61.5611 | 2024-10-06 00:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1bb48be5-8eaa-3ddf-8bea-263243fd9d43 | -9.1759 | -61.5794 | 2024-10-06 00:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 860bee04-fb1a-3a8e-891d-95e9cf93873b | -9.176 | -61.5603 | 2024-10-06 00:55:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| e53adb13-17c9-36b5-bec9-b23004a46488 | -9.3275 | -46.5609 | 2024-10-06 00:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 02c6554d-129d-3bdf-8134-1cfe75acf2a7 | -9.3278 | -46.5385 | 2024-10-06 00:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 239.2 |
| c587cf17-f370-3548-8301-f62f1c0f6db7 | -9.3281 | -46.5161 | 2024-10-06 00:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 71e93040-14b3-3ea9-99c3-023fafca5ac4 | -9.3464 | -46.5589 | 2024-10-06 00:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 244.8 |
| d3727147-03a3-3289-a5e4-75d431b47b08 | -9.3467 | -46.5365 | 2024-10-06 00:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 361.2 |
| b2d85daf-d752-3dee-b6b7-63437ea4ce25 | -9.347 | -46.514 | 2024-10-06 00:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| a4b58e74-b32d-3425-b72b-1d9dfdad9c63 | -9.3637 | -64.3378 | 2024-10-06 00:56:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e34eb669-c4c2-34ae-b660-ec1f49e11c6c | -9.3638 | -64.319 | 2024-10-06 00:56:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 77a679c7-9c32-3919-9ac9-fa162b581746 | -9.8552 | -60.2966 | 2024-10-06 00:56:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 9438d423-3e19-3186-b33a-3601cbf836e6 | -9.8802 | -59.5008 | 2024-10-06 00:56:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0ba2f9a0-f72f-35fb-8a71-57b27969e2c7 | -11.0966 | -54.2336 | 2024-10-06 00:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ad1771c6-060f-3125-b591-3d446dd064c0 | -11.1155 | -54.2319 | 2024-10-06 00:56:09 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e0df7ecc-0dbb-3c17-8c48-02f688228e92 | -12.0211 | -63.7478 | 2024-10-06 00:56:15 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| a03e4e58-ba3f-37b5-8edb-b775cff12d29 | -12.5093 | -45.3017 | 2024-10-06 00:56:16 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| f642d517-f466-3f31-ab9e-f872f8e172e8 | -12.5066 | -47.5705 | 2024-10-06 00:56:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 5a6494ea-3132-31ca-9ae2-3ec6ecba2b72 | -12.6089 | -53.1338 | 2024-10-06 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 296dd8d8-f12a-3e3f-ade2-497a470e967a | -12.6092 | -53.1129 | 2024-10-06 00:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 29d992ed-8ea2-311a-9628-d0434018d811 | -12.628 | -53.1317 | 2024-10-06 00:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2b0decde-01bb-3824-97a2-b514384b5b93 | -12.6283 | -53.1108 | 2024-10-06 00:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 2f3d652c-c692-3cda-ab91-1c08b671368b | -12.6532 | -54.0415 | 2024-10-06 00:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 40ef8793-9da3-306f-ba6a-2ddf16cbdd9d | -12.6535 | -54.0208 | 2024-10-06 00:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 0dfe77ad-d4b7-317a-8641-0518ba9f98b9 | -12.7627 | -50.5567 | 2024-10-06 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 1ce455e7-5a81-3046-9486-ca8717a261ab | -12.763 | -50.5352 | 2024-10-06 00:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 202.5 |
| a42252a4-e7d2-350c-a730-5b8bcceedddf | -14.5646 | -48.8217 | 2024-10-06 00:56:28 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| be3c4b0e-b34e-37aa-af66-9a9054645337 | -16.3278 | -51.264 | 2024-10-06 00:56:38 | GOES-16 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ef7e6f1f-1c96-3c26-9ade-17d1125c3803 | -16.5944 | -55.9238 | 2024-10-06 00:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| ed83ae00-b1bf-3977-9a95-9fc64aaed584 | -16.614 | -55.9214 | 2024-10-06 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 145.1 |
| 64b8049d-92da-3e23-8310-181b42b115be | -16.6143 | -55.9007 | 2024-10-06 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| fe920b21-a3c8-3bb9-964c-6676d6f4b6ac | -16.6336 | -55.919 | 2024-10-06 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 4840df93-7a57-3b52-b8e2-cd463ca46e88 | -16.6398 | -55.5452 | 2024-10-06 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 204.8 |
| da9c005b-203a-3576-a35b-22e1218173f0 | -16.6402 | -55.5243 | 2024-10-06 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 157.5 |
| 00e3e5a3-ab7e-3b2a-af22-bdb5cbbc4f15 | -16.6594 | -55.5427 | 2024-10-06 00:56:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 116.7 |
| b045e8ae-4453-3769-a428-772d10a9c237 | -16.6871 | -57.4536 | 2024-10-06 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 880b454c-19cb-33df-ab78-f77389e17835 | -16.7067 | -57.4514 | 2024-10-06 00:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 6a00b8cb-ef94-3828-995b-4a74bd2235a5 | -16.7647 | -57.4856 | 2024-10-06 00:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| a694d3ca-fa6c-3e86-8547-bf9e9a4a7ad0 | -16.9283 | -55.8405 | 2024-10-06 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| f5c8a9cf-68e9-3d8d-8e10-ba1cf7f4f462 | -16.9287 | -55.8197 | 2024-10-06 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.5 |
| b65b1f35-14e0-324c-8feb-9575046a3c7a | -16.9348 | -56.625 | 2024-10-06 00:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 130.6 |
| 5c3295b6-2cbc-3d1f-ace4-af581183d628 | -16.9545 | -56.6226 | 2024-10-06 00:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 160.2 |
| ce52a707-ca1c-38b1-ae82-bab5ebbad76b | -17.3837 | -42.6483 | 2024-10-06 00:56:42 | GOES-16 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 45ab53dc-a9e2-3ce3-95e3-6c6c57952b92 | -17.0007 | -55.0607 | 2024-10-06 00:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 3f5d5ed7-e207-3d1c-98ac-0f56f287c699 | -17.001 | -55.0398 | 2024-10-06 00:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 51c70854-0be3-3a63-b192-00e834d22e87 | -17.1182 | -57.4039 | 2024-10-06 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 91f3cbee-0d40-3844-bbc4-72f0cb5862e8 | -17.1185 | -57.3834 | 2024-10-06 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.4 |
| 73baa646-9b21-3acc-a5b5-a65ec9a17525 | -17.1375 | -57.4221 | 2024-10-06 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |


[Clique aqui para ver as próximas entradas](README22.md)
