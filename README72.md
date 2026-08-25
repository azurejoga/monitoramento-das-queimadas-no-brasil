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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c189dc71-0e45-3ffd-adec-86353586ada2 | -7.3849 | -55.1723 | 2026-08-25 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 5390724e-9b52-35e1-9650-b5277a84b28b | -6.9873 | -59.2389 | 2026-08-25 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| ed0cc68a-53f7-3b65-89eb-b983f951dd7e | -7.2903 | -45.3456 | 2026-08-25 12:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 4acb94a6-12fd-3ae6-8460-b959eda5b7f2 | -11.4298 | -44.5615 | 2026-08-25 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 526.5 |
| b7855f45-b0aa-3c54-a343-36887384c300 | -6.641 | -58.4987 | 2026-08-25 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2ebf6ea7-016c-39db-8cd4-1825576fa35d | -3.5407 | -48.1673 | 2026-08-25 12:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| e52a3a11-73a1-3e06-a3a7-8bdb19df4541 | -7.0057 | -59.2575 | 2026-08-25 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 3d4cda9e-afe8-3d68-b6fb-68be2e06bc4d | -11.44 | -44.54 | 2026-08-25 12:15:00 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9f717f-1184-3cd7-8d3d-50fbcb72d801 | -11.45 | -44.59 | 2026-08-25 12:15:00 | MSG-03 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1c62dde-235f-350d-ab05-e81d3156fee9 | -11.41 | -44.53 | 2026-08-25 12:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 006f2807-511c-372d-8d97-b5a17756f9c9 | -7.0057 | -59.2575 | 2026-08-25 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 11ce385b-8f1e-3ff0-871f-04d6f94daa6e | -8.5775 | -54.8575 | 2026-08-25 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9b4e242b-028d-3725-8516-980b746e29bc | -3.5407 | -48.1673 | 2026-08-25 12:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 78b2e6ac-02ce-334c-894f-cc71f9e7ffac | -13.3595 | -48.2051 | 2026-08-25 12:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 669aa5de-68c8-38af-a42f-6a907b6d1e6d | -11.4298 | -44.5615 | 2026-08-25 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 539.4 |
| debd55a5-6673-3b2f-9cee-a9397d041667 | -6.6226 | -58.4995 | 2026-08-25 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| a7860cbe-65fc-32a5-aed7-087dca2cbacc | -6.641 | -58.4987 | 2026-08-25 12:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| d075bc46-0d92-3659-9eea-925bdb717858 | -7.2713 | -45.37 | 2026-08-25 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9500e2a3-448d-3432-9477-06108e32211d | -7.2901 | -45.3683 | 2026-08-25 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 9f9557c0-cb20-3fbc-baaf-623c390c9ecb | -6.9873 | -59.2389 | 2026-08-25 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 68b1fc81-0d06-3a5a-9f50-b86c974c21fe | -6.9872 | -59.2582 | 2026-08-25 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 248.4 |
| 9f063d78-2922-3a0f-891d-ffbd593bcd59 | -11.4494 | -44.5353 | 2026-08-25 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| e0600488-d483-30c8-9019-7c3c622296df | -7.2715 | -45.3473 | 2026-08-25 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| bbec5f13-c082-3ed4-a7dc-3c2a07007e54 | -11.4302 | -44.5382 | 2026-08-25 12:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 493.2 |
| c03e685c-0882-3ab5-a805-1872474a77c6 | -7.2903 | -45.3456 | 2026-08-25 12:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 1c851b5e-d538-340f-a7d3-5fc629936f26 | -3.5407 | -48.1673 | 2026-08-25 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| e4fa86e1-1a31-3bd1-afe4-29e0e9cc195b | -6.6226 | -58.4995 | 2026-08-25 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| caedf1fc-2609-3236-8384-91436a917f43 | -12.757 | -46.4538 | 2026-08-25 12:30:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ee408479-ac4c-313b-8e82-b163df541227 | -7.2713 | -45.37 | 2026-08-25 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| cc97975c-12b5-3e12-bba2-7269e3daa6d2 | -6.9873 | -59.2389 | 2026-08-25 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 66f24e77-bb2f-379d-91a3-c739975c634f | -7.2715 | -45.3473 | 2026-08-25 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 202cc558-e15a-3ce1-a8db-723efba8957e | -6.9872 | -59.2582 | 2026-08-25 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 225ffbbd-3ceb-3379-9f4b-eb8e562f13a5 | -11.4298 | -44.5615 | 2026-08-25 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 431.4 |
| ba580654-529e-3c5c-8ce3-34d3ba2d22eb | -6.641 | -58.4987 | 2026-08-25 12:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| c8421285-8e98-3b21-ab44-36bfcf18357a | -7.0058 | -59.2382 | 2026-08-25 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 95559bda-9e1f-3145-ac54-a09d51d2305c | -13.3402 | -48.2079 | 2026-08-25 12:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| af271d6c-7a18-36c3-84a5-c51b3db69e43 | -7.2901 | -45.3683 | 2026-08-25 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 8df10ddb-6db4-3934-bd97-c08b38b4df0c | -7.0057 | -59.2575 | 2026-08-25 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| a3a1d686-43ec-37f9-b91c-723b85f63007 | -11.4494 | -44.5353 | 2026-08-25 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| cb1fe544-3160-3df9-aa25-4b633efe05d7 | -13.3595 | -48.2051 | 2026-08-25 12:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 26cb56cb-56b0-3d59-b986-add7d6914554 | -7.2903 | -45.3456 | 2026-08-25 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 9ff29c48-9861-3e26-a281-27142d471528 | -11.4302 | -44.5382 | 2026-08-25 12:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 420.1 |
| fb236b8f-6224-33ee-99eb-95802f6253d0 | -9.5753 | -49.2367 | 2026-08-25 12:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 957275ef-1c49-36a1-9e8f-89e28c726fe5 | -7.0057 | -59.2575 | 2026-08-25 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 176.3 |
| 5551d2ef-6e6d-383a-8c76-2a86d45c2db4 | -6.9873 | -59.2389 | 2026-08-25 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 805fa386-00b3-384e-8a36-4a3dad49d6de | -11.4306 | -44.5148 | 2026-08-25 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bde46b28-e7b3-3b4f-b561-86f1e7e5b947 | -6.6226 | -58.4995 | 2026-08-25 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 3eb48645-a536-3387-9a52-6662288fcc1b | -11.4298 | -44.5615 | 2026-08-25 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 413.7 |
| 959b81e3-f8ce-3885-bbd6-c07340dc8802 | -7.4286 | -43.1182 | 2026-08-25 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 285.3 |
| 39350090-ad67-37fc-97c1-885ca8b4b45f | -6.641 | -58.4987 | 2026-08-25 12:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 529eb52b-7391-334b-be40-d45ef4022cac | -7.4477 | -43.0928 | 2026-08-25 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 185.7 |
| 76e9fb8d-c019-3d1b-afbd-a44de6855c9b | -7.0058 | -59.2382 | 2026-08-25 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 973315f0-2ce9-3e06-87c6-d8888c26eb86 | -11.4494 | -44.5353 | 2026-08-25 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 9ca14161-bd30-3720-a4d4-e88cbaaec0ab | -7.0055 | -59.2768 | 2026-08-25 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2c039ebd-ea99-3a38-a3e7-59121f24c84c | -3.5407 | -48.1673 | 2026-08-25 12:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| e5effe03-fc7d-388e-80f0-756516668839 | -13.3595 | -48.2051 | 2026-08-25 12:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 7318a367-83ae-39a5-9cc8-5ee2b3678210 | -12.151 | -50.6098 | 2026-08-25 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 48f51dd0-0cec-31d6-a4fe-a2f884d9d868 | -7.2715 | -45.3473 | 2026-08-25 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 9f0cdf2e-ff99-37e3-a9ac-eaaa6941e808 | -7.2903 | -45.3456 | 2026-08-25 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 516710dc-2163-32ab-91f4-3a5751206452 | -7.2713 | -45.37 | 2026-08-25 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fc950b03-db9c-3038-8c97-4fbf4ada1dcc | -13.3402 | -48.2079 | 2026-08-25 12:40:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d1b75c24-21df-338d-b2cd-6bd46f8decb1 | -7.2901 | -45.3683 | 2026-08-25 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 166.1 |
| c34b3531-9def-34ca-abf6-8e9493dbbdf5 | -8.1765 | -46.7007 | 2026-08-25 12:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| e9aa6c4d-0bdc-3aad-b6eb-4fe206e49035 | -6.9872 | -59.2582 | 2026-08-25 12:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 208.1 |
| ebcddca3-068c-3f7e-b98a-03c0afc5dfc5 | -7.4289 | -43.0947 | 2026-08-25 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| bd7ecf23-85eb-3384-b898-e085c1ba6cf5 | -6.6357 | -45.1752 | 2026-08-25 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 49bd34d0-26fa-3959-83c3-f6b72725a39d | -11.4302 | -44.5382 | 2026-08-25 12:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 548.0 |
| b5f115e2-887c-3023-8890-27a28cdff736 | -14.2533 | -52.1177 | 2026-08-25 12:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 3063a06d-cd60-3916-9208-8954b469c4bf | -7.4474 | -43.1163 | 2026-08-25 12:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 344.5 |
| 1d94fac1-b5ee-30aa-8ab2-9f68cc3a6cd2 | -12.757 | -46.4538 | 2026-08-25 12:50:00 | GOES-19 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| ac7af2cf-cded-3ba2-899e-51d7adb27f9e | -6.641 | -58.4987 | 2026-08-25 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 157.3 |
| c21c30b6-64e3-34f4-a979-2dd9ffc3fa4b | -11.4302 | -44.5382 | 2026-08-25 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 780.2 |
| f37899ad-5908-314d-8e0f-d4f373147ab6 | -8.1765 | -46.7007 | 2026-08-25 12:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 70b09526-130f-396b-a112-69c00f9f23c3 | -12.151 | -50.6098 | 2026-08-25 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 57069408-66fd-354a-b31f-455a7f2b94b9 | -7.0058 | -59.2382 | 2026-08-25 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 42298236-19ed-38d2-967d-569ace3d3edf | -11.4298 | -44.5615 | 2026-08-25 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 372.1 |
| 34c7bffb-798b-399e-98ff-ebb69c7b27ae | -7.2901 | -45.3683 | 2026-08-25 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 9d907ac5-b8ec-3758-a616-740820290705 | -7.2903 | -45.3456 | 2026-08-25 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| f3c01659-9a8a-34db-a008-5c18c895bd30 | -6.9873 | -59.2389 | 2026-08-25 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 4afe6232-6b5f-3e8c-a30c-dfa58b5bd7b6 | -14.7592 | -48.7913 | 2026-08-25 12:50:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 5086ede0-48e8-3393-bd7f-25470440ea6f | -7.0057 | -59.2575 | 2026-08-25 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 372176fa-e560-303c-998f-da2007121388 | -6.6226 | -58.4995 | 2026-08-25 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 953ad3de-fdbc-3747-99c5-39fc0f6cb05e | -13.3398 | -48.2301 | 2026-08-25 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 94c58c57-2bdb-3447-b747-ac990412a48e | -14.2533 | -52.1177 | 2026-08-25 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| a2ac25fb-5ba8-3cec-afda-bbd08215b377 | -6.9872 | -59.2582 | 2026-08-25 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 254.2 |
| 7ceb8819-3025-3406-a0fd-fc35f5e748f2 | -13.3595 | -48.2051 | 2026-08-25 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 173.3 |
| 8fb863e8-f11f-3ba2-b623-e97d482d00b7 | -13.3402 | -48.2079 | 2026-08-25 12:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| dbf5651f-736e-3a70-92dd-c0e57b50ac4b | -7.4474 | -43.1163 | 2026-08-25 12:50:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 602707a5-a1c6-389f-8a30-3f02119e9747 | -7.0055 | -59.2768 | 2026-08-25 12:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| e5a203a6-ac64-3a90-80ad-ebaef268e70d | -8.1111 | -47.4812 | 2026-08-25 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 59498951-277e-3d39-b53b-6d5cfd69910f | -7.2713 | -45.37 | 2026-08-25 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 6700591d-462e-3d70-9fd3-9d2a241d54fe | -14.253 | -52.139 | 2026-08-25 12:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f24efffa-8225-3744-949b-4cedff3241d2 | -11.4494 | -44.5353 | 2026-08-25 12:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 174.8 |
| b55286c1-fda5-323d-9734-38b7ecd2c189 | -3.5407 | -48.1673 | 2026-08-25 12:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 245c8486-53a2-3ba8-aba8-0a8df8638749 | -7.2901 | -45.3683 | 2026-08-25 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 1f2d77b4-bd32-3f6b-afe5-66c4febb5b61 | -3.4167 | -43.3867 | 2026-08-25 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 07428741-5e2a-3191-9ce3-a175d32260d6 | -8.5775 | -54.8575 | 2026-08-25 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 45cb128e-c99a-3ba3-9f27-e5936d3edf4c | -6.6409 | -58.5181 | 2026-08-25 13:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a198f770-69e9-318a-939e-dda0fc4e991a | -13.3595 | -48.2051 | 2026-08-25 13:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 907ff47f-0e26-3247-8640-583fada5f4fc | -11.4306 | -44.5148 | 2026-08-25 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |


[Clique aqui para ver as próximas entradas](README73.md)
