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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddbb8c4b-0ad4-3c84-8eaa-087f91871f99 | -9.75652 | -43.95942 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2545375-6542-3ebd-b150-d6af8efa35b2 | -6.47963 | -42.15934 | 2025-10-18 04:49:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6aa9d5b5-64c4-3694-b0b2-f46e23f89156 | -5.20626 | -45.75084 | 2025-10-18 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 308db81a-24dc-39ff-86ec-c84700d7730d | -9.75608 | -43.96284 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33e5b2e7-0489-3ca5-87d4-9a5d49fe4187 | -3.59694 | -48.99076 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28c9825d-2ed5-30da-9914-005875acd786 | -2.37159 | -48.51854 | 2025-10-18 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 752d48fb-08d5-30ae-a4aa-1b6239987588 | -8.41344 | -44.72423 | 2025-10-18 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cf7001f-5f73-3119-bb0d-6abacc3d2ab9 | -7.29728 | -47.82963 | 2025-10-18 04:49:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9c7f274-bcd1-3d18-8408-e285e9cdc72e | -9.11929 | -48.89948 | 2025-10-18 04:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 550871d4-2489-38e9-910f-62e6cd5b3a5b | -5.16839 | -48.60236 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11b5b80d-b8f7-3571-90d2-0c53d5890051 | -6.31469 | -44.31654 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c95f34c5-0945-3040-9a4f-f8afc4d3ba3b | -7.95554 | -44.11933 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 323829bf-2a67-314e-a98b-42c0b6ae83fa | -4.53533 | -48.41474 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02324498-e2d9-38a9-ba54-68867d914628 | -7.14569 | -46.41471 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 729c07e5-7ccf-31ce-8390-27e1cea306c9 | -2.86514 | -50.73566 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb2ae9ef-b785-3ad8-bfe4-b92f8c5bf3bb | -7.16639 | -42.37124 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7fffb925-bbbb-374b-84cc-a2c44f5bf532 | -4.99553 | -43.85656 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa836cee-b5b6-36ce-a2cf-9bb48ce2918d | -6.10384 | -45.85035 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4516dd50-3e57-3e7b-bcae-09e76ee85ff8 | -6.29733 | -44.71606 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a35ab0f1-e54b-3d41-b8d3-ee72da7ade11 | -3.48224 | -59.46216 | 2025-10-18 04:49:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97138127-81fe-34f2-b258-15cf1148c9f3 | -8.16683 | -47.03467 | 2025-10-18 04:49:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b0ea03b-2abe-36fa-b46c-fb20757c1672 | -4.44804 | -43.23174 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5032c7f1-3f9e-3796-9f62-c0586177614d | -3.85237 | -41.57647 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b676bed3-6fc8-3956-9e9d-f1e101818d32 | -6.13439 | -44.21797 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ca2fd25-5e06-3f5a-935d-141fe9469153 | -5.10475 | -56.15318 | 2025-10-18 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9e37ef6-c91e-33c3-b067-d077ba35285a | -2.86901 | -50.73268 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a48956a-4d6f-3a31-b5a3-65acd1d36861 | -7.58598 | -44.9913 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b864300-7561-3f50-b741-5d78012a0ff0 | -3.81385 | -51.70238 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cb12789-1f1a-33af-938f-6a30168a986d | -5.20604 | -45.75702 | 2025-10-18 04:49:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e466cd6e-0a35-33d3-8300-e2541303b3e9 | -4.00216 | -45.50719 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8181abd2-86ea-3741-af67-9bfbeed6d1ee | -3.70025 | -49.56214 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66b4f8e0-f344-33c7-ab53-0b68afde0c88 | -8.55065 | -50.08 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 426a2423-c94e-3a92-825a-2953585165a2 | -6.33803 | -44.00492 | 2025-10-18 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87810c14-e4a6-377d-9fab-6b6a48b4207d | -7.2113 | -43.80976 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1638908a-618b-3227-9194-2791a09f45b2 | -6.93202 | -59.53265 | 2025-10-18 04:49:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 228e1039-52fe-33ae-b9cf-c476d2010b1a | -9.68016 | -44.55186 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26079d1c-ff71-33fb-91e7-8ea0b4416483 | -2.51714 | -51.93124 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4ffde6-3118-395e-8c6b-205d98562c51 | -7.7606 | -42.49029 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e2913073-112f-3e33-8a97-97fd733e84d3 | -3.78318 | -51.76804 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deec5040-53e7-3109-ab16-392f6e15fbe2 | -7.16832 | -42.36601 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a7cb1f9-4360-386c-88d6-459691d974d8 | -8.09607 | -44.10486 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6167542b-3b53-3517-925c-382ac6dd76a8 | -2.70679 | -49.41442 | 2025-10-18 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9423941b-9ba4-3372-8f25-7f8d6a2290a6 | -3.14864 | -50.24745 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b63c3ca-da55-3bb8-a668-2e4fea0452e8 | -7.35485 | -43.85448 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f0914df-24d0-3462-9630-44a871b47692 | -6.60336 | -44.44609 | 2025-10-18 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de634a4f-e9a6-344c-bdce-26ee36e9ee53 | -6.20946 | -46.30168 | 2025-10-18 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c48abb5-5e65-30c4-999d-e9b3957eef35 | -2.88178 | -50.73824 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51247871-0b04-3bbd-adf9-6c069a716680 | -3.91109 | -52.33465 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67e447a5-8c60-34ef-8bc7-af33e8f83d33 | -7.35906 | -44.2336 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf4fb53e-8da3-30b2-a90b-7b129c5d82c5 | -4.24639 | -48.56839 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b926b451-c2f5-3380-a882-2371d7870ef7 | -4.28361 | -49.97932 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0234b00-4c15-32d6-bfba-a9358a842957 | -4.82085 | -47.08405 | 2025-10-18 04:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37870aed-189c-36ab-929b-9a0b9fbe8397 | -8.167 | -43.30629 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c0a168ec-eaaa-3ca6-86d8-22473f044579 | -6.739 | -43.8134 | 2025-10-18 04:49:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d49618d1-0e01-378e-8b0c-4b0389a5befb | -3.92373 | -41.73634 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20d869ce-8b95-39d1-bc6b-e85f50b4e5be | -4.25005 | -48.56891 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db14f2a-f809-3678-99e5-095fbf7325f5 | -3.14583 | -50.24335 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7cb4c87b-5e68-328d-abe0-f447a1f97869 | -2.1519 | -51.96214 | 2025-10-18 04:49:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69fb6ce9-094c-367a-8714-c000c02342f6 | -2.91121 | -52.72674 | 2025-10-18 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b3e40da7-50d2-3871-94c8-c71a5693f4aa | -3.29281 | -49.52507 | 2025-10-18 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9515dc91-4c63-3f0a-8cef-ca0dc4253ebe | -6.49057 | -44.5552 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e857fe06-dc50-32c6-bd4a-e58c8a5644f2 | -6.60496 | -44.21618 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feb74a49-9a4d-353b-b0d0-3f209f098fb4 | -4.63044 | -50.95526 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb52c5b0-5400-3218-b064-c436ea061e15 | -6.69532 | -47.45425 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b55412ee-1c1c-3271-9d08-520a0dfc2329 | -1.89382 | -51.01317 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b3bc85da-2c18-3ebd-acba-1bcf9c4e6c98 | -8.36569 | -46.235 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f3bf0ce-1643-3ab8-a26b-765e1b2336e8 | -4.00281 | -45.50287 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a918338d-748e-3725-a3cc-4423d34893cf | -4.72904 | -46.15781 | 2025-10-18 04:49:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99caa3ef-5c15-3713-a6b7-baf88d35db9d | -3.25401 | -51.22271 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 441b0116-198e-33e5-8417-ae221bd9f393 | -8.39179 | -46.22818 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ab310ef8-52f1-35b0-bc4f-862ca56e81b4 | -3.06087 | -43.20837 | 2025-10-18 04:49:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2543d839-8194-39fe-8c05-0e536eba4b94 | -7.24679 | -49.51719 | 2025-10-18 04:49:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac8f5626-b539-3c5a-a7d2-1bf5fda040b4 | -2.22758 | -48.36794 | 2025-10-18 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bb88f18-20d2-35ac-95ae-b5f49712ab57 | -4.45891 | -43.23011 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7524fbd8-70cf-39e9-9b30-ca2e5a94844a | -9.40238 | -49.02441 | 2025-10-18 04:49:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7035233-769c-3e39-8bbd-281ce20e9d06 | -3.62984 | -55.28207 | 2025-10-18 04:49:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c8cc13-9cbe-3afb-95e0-c6c26321f992 | -7.4726 | -42.74585 | 2025-10-18 04:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8844e69-5e66-3cbb-8709-2b138abb3aec | -7.1695 | -46.52792 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e3f051-bf47-30ad-9728-73a74c849d8a | -3.57048 | -49.44569 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1512d64-55f5-37d4-8b9a-2325ddb31fdd | -3.29463 | -50.00714 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25929d9-cc28-35e6-a998-48e535f0e9b0 | -8.3541 | -46.22015 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04cc71fe-6168-30cc-852c-7404837f3159 | -2.86404 | -50.74263 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9027efd4-ae72-3bf3-8e90-2378539ccb33 | -3.44231 | -52.8282 | 2025-10-18 04:49:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 658852f2-ef9a-341c-ab17-7ebef679b028 | -3.49806 | -51.55002 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11b81873-45d9-302c-a720-343e3dae0a82 | -3.12335 | -49.21925 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a843cd3-8499-3b8e-bcec-d38643f002a1 | -5.00882 | -46.02266 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 291db364-1f75-34e4-b1bc-dae65558318a | -8.58958 | -45.43145 | 2025-10-18 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6860c7f9-ceed-355f-9421-b73110600739 | -9.64542 | -47.12297 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65f1b855-b1c6-3f78-880b-8e6983b12a33 | -2.35818 | -57.10391 | 2025-10-18 04:49:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdf6abbb-232e-3150-a6cb-583cd2c5c176 | -7.12271 | -47.233 | 2025-10-18 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0774955e-9dee-3958-a64e-e5dba25cc462 | -8.35995 | -46.24305 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70ee31d9-2731-3c38-8e18-94b306338ecc | -9.5009 | -47.26981 | 2025-10-18 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51134d57-ccc9-338e-b2c4-abdaba6f55f9 | -3.99839 | -45.50222 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f6a2d21f-9895-37ee-b28f-5e0370fb44a2 | -6.13995 | -44.45785 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8adf2040-fa35-3e7d-878c-5eac203530ac | -5.21368 | -45.24313 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42339aa1-3c9b-3be6-bc51-24e11f79e4d3 | -6.33222 | -44.00947 | 2025-10-18 04:49:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1b7055e-f9f3-35d8-9dde-e9b27999fb88 | -2.96499 | -49.30939 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15d17ea0-0511-3108-a1f9-d6e98e4c24fb | -5.92878 | -51.5592 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24c81873-ebb5-396c-80ca-77104cd8f114 | -1.55983 | -60.14273 | 2025-10-18 04:49:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec2fd359-0b3c-30c8-bad8-236317d6e71b | -2.71025 | -49.41495 | 2025-10-18 04:49:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README75.md)
