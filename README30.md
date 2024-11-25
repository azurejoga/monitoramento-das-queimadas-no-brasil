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
| c71ce00e-82b4-3701-a0ff-ebaac54100bf | -3.504 | -53.81525 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d982babc-359f-3632-b02f-48bd241f6bb6 | -4.37045 | -48.56428 | 2024-11-25 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b9e2c6b-d30e-3489-9145-7017215e5632 | -2.78217 | -54.054 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4fd51cc-856f-315d-bee5-1df825bf48cd | -0.57936 | -51.71221 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d916f296-d242-38b0-b28b-d8880d7d0aa3 | -2.57813 | -54.23415 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea5e82dd-95ab-3fee-81f2-5e6b9a997952 | -1.04909 | -51.74135 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f08bc3f6-5fe2-35f6-a2f0-19bdd91aa5c2 | -2.79544 | -53.00794 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca372e78-47c8-3992-8a58-1e6b8138d145 | -3.00332 | -51.54929 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 967113e8-6fbd-31a0-aa96-314ff8719f94 | -3.0624 | -53.22295 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e089dee-2464-3f4e-8d47-a31171e8b6ad | -2.54553 | -53.9923 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a15d623-b3b9-3bbf-9b04-c0d44f485c09 | -3.06186 | -53.2264 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e91ebf8d-e3d7-3783-85ef-d37790402845 | -3.88205 | -52.35803 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac34b0e8-37e2-376e-96c4-b6096a24d4ce | -2.84825 | -54.00362 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75a2320c-4948-3843-9f2d-d525083c932e | -1.64122 | -52.10638 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b49acee-87d5-3979-b8bf-0fd605bafadf | 0.2997 | -51.08113 | 2024-11-25 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0779c5e4-9cf3-36c9-a897-bde540336035 | -3.1084 | -54.00174 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c54b26bd-5883-376f-9d49-43a728b0e205 | -2.73537 | -46.10516 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a5a6ae3-7a4c-393e-b3cf-5ad185761f45 | -1.45096 | -53.40131 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1078a8cc-fc44-3c55-81e6-a1a4adecfb9d | -4.13737 | -48.76532 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65744413-b820-3f01-9897-f0cb6e01804a | -0.94769 | -51.71854 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d665e9e6-5a7b-3d1d-952b-1c485c81b537 | -0.43049 | -51.56598 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65952fec-fe93-3ef8-a698-7ed6c00ebc8c | -3.04789 | -54.02453 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 045872b1-4fb7-3cfc-8142-9e05bdb64a44 | -2.85045 | -53.9897 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0491051-c7c6-3522-a1bd-6582fa169a1c | -2.76581 | -54.03363 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3a2e2e7-b28b-30c8-a251-ff0b0439aa5a | -1.39849 | -55.20551 | 2024-11-25 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 35f49c35-9241-31f9-80dd-d521cdd406c0 | -3.65899 | -54.42112 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e802eec-5bd7-3ffb-b31a-93d7dc8327a3 | -3.28412 | -53.66365 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20125ff1-7603-33f2-af06-0ccea3fbf085 | -4.70846 | -45.72677 | 2024-11-25 04:55:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ad150ce8-084b-351f-bf6a-76e70344ca51 | -2.82827 | -54.02192 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b886c888-1331-3b41-98aa-d37dcda672b7 | -2.78106 | -54.06098 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcc540fa-1584-3a29-9173-0f8908fd4933 | -4.5185 | -49.05722 | 2024-11-25 04:55:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38215e40-dbb3-318a-9def-fcb9b802b7e4 | -3.55072 | -51.50632 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e92d1bb7-8919-3ff7-8713-15c099de7ff0 | -1.13319 | -53.6537 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 285a84c7-1558-34b7-ae66-b1b14d41dc0e | -1.24017 | -51.61772 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee121204-c37b-35f9-b7d5-7197cc56515c | -1.10615 | -53.39661 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66bfb1d9-d43c-300e-84ce-b808b6f355c8 | -2.85213 | -54.00066 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28a481a4-87cf-327a-ab5b-3dbbb0fcc438 | -0.19871 | -51.37777 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cb797bc-80a6-3a21-beb4-36350b48d2a6 | -2.981 | -54.0855 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5074b7e-e038-3ba7-8319-1fd08325a105 | -3.24683 | -53.27629 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65327bba-9da5-39ad-bb81-90c41484288c | -1.72635 | -52.4872 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bd231b7-31ab-3903-a1c5-ad4ee13737a9 | -2.83659 | -54.01251 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41b334ee-16c0-3c81-87ea-0fd8d512c126 | -3.80939 | -51.99906 | 2024-11-25 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d265d0e4-eed0-3e00-a01b-b8291651c34f | -4.85164 | -50.80686 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f676a238-fc20-30c8-93c9-fe34e344eb20 | -1.18774 | -53.88377 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 96af6764-06f3-34d7-8372-868f6ae4acd1 | -3.63265 | -51.51829 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 318aa38b-4ee3-393f-b3bf-74369f2ef64b | -3.25455 | -54.21748 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7db467b9-958a-3792-ae74-84bc9dc824f9 | -3.11406 | -54.13832 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 910411e8-02b1-3ab9-a9da-c0fb0c6a2cc9 | -2.61522 | -53.97814 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 247ac605-425e-3af5-991b-60e8a57dbf42 | -3.26988 | -52.96166 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d5a710-d347-3a7f-b35c-f19a4f5e601d | -0.23892 | -53.76564 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abedde5f-1094-323b-9664-027c59bea2f5 | -1.25535 | -51.63103 | 2024-11-25 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29c1c770-a8bc-3d8e-b9e5-2d3a28f5775f | -2.88997 | -51.58096 | 2024-11-25 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84da17f6-39ef-395c-9b5f-9e356096717d | -3.05449 | -53.1652 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9fc81ad-4294-32e7-b59c-36ae169cc344 | -4.2503 | -49.1898 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f75f1da5-9ffa-3fac-863e-27e170f29a77 | -2.78051 | -54.06447 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 523ebcd6-cf7b-3c85-b00e-5d309232038b | -1.06286 | -52.42606 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fad0a466-0080-3d71-9a3f-07c759d061ef | -3.82984 | -52.29531 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce353ea4-0655-3a62-8594-db1b928a88d7 | -2.07893 | -47.88163 | 2024-11-25 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2773d47e-7e9c-376d-ac8f-f4ea58d08c36 | -3.34401 | -50.51016 | 2024-11-25 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3bc13f4-294a-387e-89a3-22acfbb13f7b | -0.6224 | -51.72251 | 2024-11-25 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ac0011a-1f64-376c-96e5-dc1a135de38f | -4.1364 | -48.76378 | 2024-11-25 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74c967ed-6a31-3a64-a28d-5979f5ced878 | -4.20507 | -50.23654 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6407ee96-978e-328f-bd7c-d8c4c9a7994a | -0.95833 | -51.71657 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69146980-8368-3166-9fb6-f59bf0c209a5 | -3.87813 | -52.36107 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abced297-d628-3bf2-a9cc-01b4d7f34d9d | -1.96008 | -53.32523 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1335c09-2e2b-3bb1-836c-1e6b6e6a0c1b | -2.82938 | -54.01495 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cedbfcb7-deff-3ef3-9c91-36f2b3f2bcfe | -2.54153 | -47.12267 | 2024-11-25 04:55:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e905b4d1-fe12-3fc2-8d1b-d6be8ddff6d7 | -1.03715 | -53.1703 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63f580e7-c17e-3bb3-b0d3-48765d31c021 | -2.58298 | -53.96596 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ae1ff3f8-5641-3665-9b0e-17ca059302b9 | -4.4143 | -49.70622 | 2024-11-25 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a73094cc-d873-34ac-adc4-8c768a299c9c | -1.08952 | -54.03836 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3145e38b-dfb1-38c9-a015-dce716e276d2 | -0.9265 | -52.64886 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d3c64e0-4f01-3b26-a7f9-d7ddb353f071 | -3.03789 | -54.02296 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b2a561-6c33-3dcc-b8ac-5e482622e932 | -2.71478 | -54.14024 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 544ddd69-2065-352b-b501-f4c07b738a9a | -2.57576 | -53.9684 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 937b9fbf-a17e-331d-87ad-c3405c794db1 | -1.54444 | -53.06255 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e32e1f6f-f8cc-345c-9f28-c54415588dc2 | -4.31688 | -45.89526 | 2024-11-25 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d4fc9855-2926-3da3-a3a9-4b94334b9ab4 | -1.07034 | -53.17547 | 2024-11-25 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4eea827-3bd6-3ae2-8fa4-b86f81d5eb63 | -2.62468 | -53.9832 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f96432a7-8d43-3983-95b0-73cac17a7438 | -2.57869 | -54.23063 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e6af852-08d2-3acc-af69-ac0319b0fb33 | -4.12643 | -54.24728 | 2024-11-25 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eadd1dc6-0c1f-3b5b-baa4-921c708165b9 | -3.71699 | -43.87412 | 2024-11-25 04:55:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 30709236-ee91-3b7f-b53b-69a60d36e4f9 | -3.08352 | -53.26157 | 2024-11-25 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d34293b2-a14b-305b-8c9e-6fa076faabda | -3.10001 | -53.73772 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11c6788d-e1e6-39e7-94be-7a1b6d99f413 | -1.14265 | -53.65866 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfce52ae-e68c-3b3f-a95f-bda08d16f6c2 | -3.54562 | -50.40242 | 2024-11-25 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79fdd1ac-9ae9-3a81-b0be-b85a1c9009f6 | -2.68777 | -46.27266 | 2024-11-25 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61823256-1d5a-3c4c-8741-4f155d3da645 | -1.98235 | -56.57116 | 2024-11-25 04:55:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b687b3ef-0eee-3313-9a1d-6992c377d301 | -2.78161 | -54.0575 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ab8968f-dcf4-3e8f-b80a-3eaf48b9d11e | -2.76754 | -54.06607 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d75a8d12-3264-333a-89eb-4e01c041ddcf | -2.13931 | -52.7677 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| db758e3c-de5e-39bf-b220-57e8a5da958c | -3.02182 | -54.0597 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56615a64-894d-39ea-8f72-53748837208b | -4.22823 | -53.49377 | 2024-11-25 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cb6efd9-f755-396a-9634-044e6f3d6f97 | -2.43664 | -53.88924 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce73a701-c534-39b5-8105-7cd6f351ead8 | -3.10226 | -54.00454 | 2024-11-25 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f06f67f8-8857-304e-8649-5cc7ea425b01 | -1.60647 | -52.58144 | 2024-11-25 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86a043b9-dc8d-3560-ad50-aaa1c6c8f9bc | -1.06032 | -51.80095 | 2024-11-25 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1f3e740-24ec-3cfe-b7e7-5a8276f06ce2 | -1.13109 | -54.17535 | 2024-11-25 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c66d2c9c-237a-34cd-8030-893473d28c49 | -2.83007 | -54.11875 | 2024-11-25 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87aa6e4f-1e27-3de3-8009-1e53b04cb923 | -2.81947 | -54.09919 | 2024-11-25 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README31.md)
