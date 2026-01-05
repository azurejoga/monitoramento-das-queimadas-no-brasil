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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4e0afeb-5b20-32de-b24a-bb0c44d53f50 | -3.17071 | -52.87355 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 360ac6bd-7793-3368-952f-2064e9d95e60 | -2.25392 | -44.79042 | 2026-01-05 04:50:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 160b6e8f-625a-312f-adda-6c516f65d908 | -3.00075 | -51.05059 | 2026-01-05 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d9f75dc-c5f0-37b1-b379-32e60cfaab56 | -2.43429 | -46.89571 | 2026-01-05 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d028d980-996a-3fce-8059-1c232dcfc96e | -3.87708 | -50.96472 | 2026-01-05 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 90a34be7-5eca-3be7-8513-248c01142156 | -2.90301 | -52.63233 | 2026-01-05 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1956286c-c256-35a4-ae6c-ab22d35a76d5 | -4.69207 | -46.42009 | 2026-01-05 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6c65b22-1583-3ccd-861d-6ebb19e24d12 | -3.53547 | -54.16957 | 2026-01-05 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2deaa687-bfaf-307a-a0d4-5f43fe2e7e6e | -2.80415 | -52.99887 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 870214a3-7f57-3b5f-b360-0d6ac840b736 | -2.79936 | -53.006 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f78f3290-a209-3a5d-b828-dcf33143a750 | -2.8029 | -53.00658 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03def738-443b-3834-b2a7-fc6075eacff2 | -2.83393 | -48.66068 | 2026-01-05 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1441ff-0d66-3b0e-ae30-45e67bebb37f | -3.68038 | -52.53108 | 2026-01-05 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d170c01-0245-3b87-a3f1-504ec74f38f7 | -2.87808 | -52.56587 | 2026-01-05 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a881080-ea5d-3de1-9e04-0b0c17e841ac | -3.92531 | -46.51413 | 2026-01-05 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53dce1eb-c43d-3245-949e-0b215c8a1ce2 | -2.8038 | -53.00373 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d762168-c47d-3cab-b043-464a105649ef | -2.80087 | -52.99931 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6aaa7944-80ed-3fb1-99e2-ce236409d7d8 | -1.52827 | -54.52794 | 2026-01-05 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5274e77a-a1c1-33da-9bd6-8045a11a4a4d | -0.94207 | -46.9246 | 2026-01-05 04:50:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c846249a-f1f6-3579-b677-e21990dae456 | -3.47299 | -52.99148 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3010ea1d-c9eb-3740-8247-c98c23f14982 | -3.45249 | -52.93723 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ffe8ea5f-79d5-3393-9272-999e444bce59 | -1.25591 | -53.48105 | 2026-01-05 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddefff12-f3e2-3501-9460-0ab06cc9f086 | -1.55293 | -53.30209 | 2026-01-05 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ed4f3b0-3022-306b-81ae-6b7b6e7f6b2d | -2.83451 | -48.65701 | 2026-01-05 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1dc0bba-f3ae-3caf-a3d5-31f8341d4fa3 | -4.69089 | -46.42208 | 2026-01-05 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60da8214-8e01-3fdc-9e3b-f36c9bf8a487 | -3.4531 | -52.93335 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c82da82-5bce-332b-b4f8-449dab9795ee | -4.73761 | -45.57466 | 2026-01-05 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5e97134c-301b-3e6a-b297-bfbfa5490c05 | -3.78098 | -47.48584 | 2026-01-05 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 506320bf-36fe-31c9-84c6-3769e15c0be4 | -4.72943 | -45.57325 | 2026-01-05 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8954225a-7755-3b07-a900-b25915004f37 | -2.91369 | -54.12104 | 2026-01-05 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fd0c752-1c1d-38b3-898f-045e72c5a2ec | -2.44468 | -49.02597 | 2026-01-05 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbf1d1d1-8a31-3377-a57f-2b7a5f8441d3 | -3.92149 | -46.51357 | 2026-01-05 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9709e284-9a7c-3eff-910d-44a63cc50408 | -2.85783 | -53.00352 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48a6d65e-eea7-3948-ae81-1db680de9f27 | -4.68775 | -46.41669 | 2026-01-05 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cf68cdb-5649-3ce3-ad30-0916521ac4b5 | -3.53174 | -54.16897 | 2026-01-05 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e4c8a1-f9c6-3f28-9866-75809af41fe3 | -2.98007 | -54.0931 | 2026-01-05 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 025cc775-323e-3476-8a15-e39426a72e7e | -2.80061 | -52.99829 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81c84225-e0cd-305f-b27d-22e27b4b75ec | -3.0627 | -50.95385 | 2026-01-05 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 498551a6-0b6e-30a6-beb4-63445f88b1c8 | -3.31576 | -52.69149 | 2026-01-05 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af2a9c6f-2348-3321-8d43-c4b8f3d28885 | -1.92187 | -46.45154 | 2026-01-05 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 31b39165-b98a-3ba6-99ef-e95d22757735 | -2.8625 | -48.70218 | 2026-01-05 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee13f8e6-00f2-317f-9b8f-2792507fa99b | -2.80441 | -52.99989 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8352eae2-a478-3e03-9ae4-4a5ca7820bc3 | -2.47091 | -47.9713 | 2026-01-05 04:50:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bad65486-1aa4-3fa8-a8a1-e1ea40315a2a | -2.45107 | -48.63266 | 2026-01-05 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e40d416-2226-3975-9b06-0add04c84d9f | -2.24975 | -44.78979 | 2026-01-05 04:50:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 80c384a0-76c8-34aa-8e07-b783a12e4d04 | -1.59203 | -46.01884 | 2026-01-05 04:50:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab1a1dfa-0d73-37c2-93fb-93b2209f79b8 | -1.33454 | -49.40681 | 2026-01-05 04:50:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 84bd57f7-cc91-3f50-9a0a-c98549b9b9d3 | -4.73352 | -45.57396 | 2026-01-05 04:50:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe0a18d8-3d13-380a-a892-7c9f87b79e98 | -2.33205 | -45.81151 | 2026-01-05 04:50:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6abfa7cd-befd-33b0-ac46-2cee986bcd08 | -3.78095 | -47.48326 | 2026-01-05 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e59c7292-dda6-3261-9812-0a2c3a2d0440 | -2.9721 | -54.3327 | 2026-01-05 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4494b5d-9df0-3640-bd1e-2fb4875977e7 | -1.52905 | -54.52307 | 2026-01-05 04:50:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fe26496-4f3b-3a34-8cac-2c22b94482dc | -5.06092 | -49.93352 | 2026-01-05 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7449a03c-79ca-3a96-81b2-cde7a97d1be2 | -3.00408 | -51.05112 | 2026-01-05 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3be4ed0-76e9-37ac-b5c2-a69b59c64687 | -2.79999 | -53.00212 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7daac270-9b11-3641-8e87-ab8408e4b66c | -4.26122 | -48.83847 | 2026-01-05 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f246fb5-58f5-3996-bbb8-42054c311a4b | -4.68388 | -46.41603 | 2026-01-05 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62470f34-0263-3423-8f68-99a66b4456a2 | -5.35102 | -46.78637 | 2026-01-05 04:50:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a85c48c3-2458-3653-b476-91a8a782b9f1 | -4.68313 | -46.42085 | 2026-01-05 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9bf1a810-3805-3cdc-b232-27ae55e7237f | -2.87461 | -52.56532 | 2026-01-05 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17133798-d50b-34ca-b899-fd60068a955b | -2.80318 | -53.00763 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b933f8c4-4d21-3540-8458-68ffe410b00e | -2.45365 | -47.78279 | 2026-01-05 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 85cc9682-485d-3358-9329-fb459ebda0e5 | -2.51194 | -49.06524 | 2026-01-05 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7616323d-04d9-3be8-83a5-2c2bdfbd8cbe | -3.40133 | -51.87287 | 2026-01-05 04:50:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6f6206f-8264-3cb7-803d-b33d1f5b2976 | -4.87828 | -47.92635 | 2026-01-05 04:50:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a937a850-8d5b-3e06-96cd-d5d113b33b31 | -1.29443 | -49.32233 | 2026-01-05 04:50:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddb361f4-7c35-385f-9db1-e7448097114a | -1.86763 | -47.9866 | 2026-01-05 04:50:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 72da5e8e-89f7-33d6-afff-56f6e10ac629 | -2.75496 | -54.21847 | 2026-01-05 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f751e651-3ed6-3fab-be34-43cda5256d63 | -4.82342 | -47.34181 | 2026-01-05 04:50:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1a92ab0-1e63-361a-b696-bd7cdf130e61 | -3.69553 | -47.21841 | 2026-01-05 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0bdb3749-dd84-35e8-9ddc-1d6e715c977b | -0.74208 | -52.42771 | 2026-01-05 04:50:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bc806a14-5bc2-3478-b3f1-7ea104667183 | -13.43016 | -43.85196 | 2026-01-05 04:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a75385-9168-3a1b-b6c2-1485aa10f983 | -17.64852 | -56.44305 | 2026-01-05 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 983cc41c-1233-3fd7-90f6-92311f7c521d | -17.6457 | -56.43829 | 2026-01-05 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c57fd88e-40f1-3a45-a23e-b48739629a97 | -18.55011 | -52.79786 | 2026-01-05 04:53:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7604096b-faad-3f58-860f-3dd1fde6c776 | -18.82496 | -51.61629 | 2026-01-05 04:53:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 397c505b-7c56-33f7-a812-a307dc2795f6 | -20.83684 | -56.16858 | 2026-01-05 04:53:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dca3e21c-f798-35d4-99d6-5e4b6951dee2 | -18.55405 | -52.79467 | 2026-01-05 04:53:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60508cf3-be8a-3840-a12a-ed47a4341e37 | -17.64922 | -56.43895 | 2026-01-05 04:53:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1fb7d1ba-4965-361a-9282-ec57817e7e87 | -13.42978 | -43.85517 | 2026-01-05 04:53:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01a8c07d-dd30-3a5e-8640-33b735f0dc50 | -18.55348 | -52.79841 | 2026-01-05 04:53:00 | NPP-375D | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 847873bf-48ad-38b3-bdbe-9be2b2e76e2d | -22.03885 | -55.51802 | 2026-01-05 04:55:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 308d32aa-1881-31c3-8314-88c7b00d5b61 | -25.47801 | -54.51796 | 2026-01-05 04:55:00 | NPP-375D | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 52817ac6-125f-3774-ab0c-aefc51165b27 | -22.02827 | -56.30413 | 2026-01-05 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a5723ca-d8c2-3d25-8347-ed10824891ba | -22.76558 | -48.01583 | 2026-01-05 04:55:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07cab32a-f092-31e9-9c8e-8e43f516307d | -16.59796 | -58.21256 | 2026-01-05 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 43b0cce2-b709-31a5-9f3c-86ffe48c0c5a | -16.59014 | -58.21104 | 2026-01-05 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9d1cfaad-f21d-3315-843d-ec4ee0bab693 | -22.0215 | -56.30283 | 2026-01-05 04:55:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94d43447-a66b-3583-a8e5-fc556a87866c | -16.59405 | -58.2118 | 2026-01-05 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d4e4cfdb-c3b3-3bcb-9235-976e000ed70d | -16.07596 | -53.26586 | 2026-01-05 04:55:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c418f5-81e5-37ce-a943-d05ac291c0a5 | -16.58922 | -58.21612 | 2026-01-05 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 98cb80d2-47c2-3c2d-8cae-a292b1a9e088 | -22.03551 | -55.5174 | 2026-01-05 04:55:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e8a9157-4dbd-3694-af72-342c13438c48 | -16.07794 | -53.26642 | 2026-01-05 04:55:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e68670fe-23ea-3ffb-8407-9e00e9534c1b | 3.90142 | -60.1867 | 2026-01-05 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65176e0a-2649-3cb5-9d1b-37d4017a5eb4 | 4.14322 | -60.01751 | 2026-01-05 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5104bea0-81a6-39d3-a18e-89b4e9561d86 | 3.9094 | -60.18504 | 2026-01-05 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67721350-afb0-3cb3-963f-f850c7ba71e0 | 3.90542 | -60.18596 | 2026-01-05 05:08:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53e6a53-cc97-3461-b3db-a9caa66a72e9 | 1.66083 | -60.74631 | 2026-01-05 05:10:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0af09de8-7893-32f0-90e6-92221c4748a8 | -1.59422 | -46.01796 | 2026-01-05 05:10:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f29ce59-07ee-37c7-b992-1767aae88cf6 | -1.55274 | -53.30437 | 2026-01-05 05:10:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README6.md)
