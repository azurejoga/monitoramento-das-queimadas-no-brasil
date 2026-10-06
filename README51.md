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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36bbfaa4-6e6d-3b1a-ba30-4cb695863e83 | -14.80198 | -42.0116 | 2026-10-06 04:42:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10762fde-841a-3c56-9c28-11ed0e4f4bc4 | -14.77973 | -44.65655 | 2026-10-06 04:42:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f4a84981-ceb3-30f2-8239-716e823b171b | -14.80264 | -42.00603 | 2026-10-06 04:42:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b978e4f6-042c-3508-99de-b197dc29236f | -16.01421 | -43.60173 | 2026-10-06 04:42:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81faedc7-94c1-3ee7-b0f9-fad3f63b11b4 | -14.05456 | -44.29141 | 2026-10-06 04:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1bc3b6a-7c03-37f6-b811-d1ccae0a1e36 | -11.99152 | -60.47425 | 2026-10-06 04:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67bd2bcc-063e-344c-b949-e62a63cb57d9 | -13.61035 | -44.35691 | 2026-10-06 04:42:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f267fdb-aee6-3477-a9ab-b9156c1e759c | -13.5007 | -61.13694 | 2026-10-06 04:42:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d4aa48b-d26b-3fab-bd10-beada18ebce8 | -14.19696 | -44.36458 | 2026-10-06 04:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce41b60b-cd4b-3cac-bd05-fc19f3c68d93 | -14.76292 | -45.1461 | 2026-10-06 04:42:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 304e30e0-744c-3385-86ce-319d57bb91ae | -18.54087 | -41.30014 | 2026-10-06 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74d38df4-f8a0-396f-895f-e3e6e91f73fb | -14.7838 | -44.65716 | 2026-10-06 04:42:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| efaf2290-68f1-3a74-8722-175e40b162ba | -12.1306 | -63.15708 | 2026-10-06 04:42:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a29f94d-2010-35dd-8af2-ef8919d405e7 | -18.53549 | -41.29958 | 2026-10-06 04:42:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 18289cdd-092d-352d-b31e-4a156bd7c545 | -14.75897 | -45.1455 | 2026-10-06 04:42:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 238e3d6c-de78-3c81-a45a-1b6262d9c474 | -14.06911 | -44.48584 | 2026-10-06 04:42:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d41fbf4-0708-3aca-a9b9-97ce7fbcc880 | -3.6732 | -55.9425 | 2026-10-06 04:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| e95d33e5-a26f-38b1-8b0e-3d95eb8b5677 | -11.26 | -45.48 | 2026-10-06 05:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6e690a03-f86a-319f-b92d-068ab7f65843 | -11.26 | -45.53 | 2026-10-06 05:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d27c333-ce67-3fcb-9c7d-d6c5d2abb9af | 3.32049 | -51.3424 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ad822cb-72e7-3e6a-892b-5e8af33c2d65 | 3.31971 | -51.33749 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49acc7b7-4d8f-3012-971e-94da359a1e2d | 3.31842 | -51.34048 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2633b48e-8c8d-383e-8f58-22c6761f3432 | 3.51736 | -51.28035 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91a74b9b-04b3-35d0-9d3d-9e692ed0191e | 3.31296 | -51.33644 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696a51ae-6062-3b7b-bed5-983aeaaa937f | 3.51269 | -51.28115 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6a0f022-55cf-3600-90c9-f363d67d5f18 | 3.31506 | -51.33834 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f50c2ff-6017-39a3-ba63-5d2ff026285d | 3.51538 | -51.27938 | 2026-10-06 05:21:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 990f8087-d269-3a85-8a48-3f455e5565e6 | -3.04931 | -54.22818 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c377361-7298-32b8-bec9-3ea7c824a658 | -2.78668 | -57.68244 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 24278291-ff70-3fa6-aa65-a5e8e162e16d | -3.50451 | -54.62534 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c80ec75d-c253-3189-b740-a5e38c6b1802 | -3.6563 | -55.5038 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 12ca9559-4d3a-33dc-9266-df43b326dcef | -2.95349 | -54.14648 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc785cc-5604-3d7b-bc91-a3626d59c729 | -3.72215 | -55.46482 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e659b066-d1f4-3857-9403-a1538f596f9d | -2.55591 | -57.38655 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57377bfd-fd00-346e-8fbb-2f55b6db3e72 | -4.29296 | -54.80545 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5cec7977-0767-3e82-abff-e6f75ae2e2a2 | -2.9474 | -54.15779 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 999cf429-9366-35be-a3ee-5f34f991359c | -3.84673 | -50.31072 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e4dbff5-99c7-3f8b-b28c-37cdecc7076e | -7.90694 | -70.91485 | 2026-10-06 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e42ec5e2-da07-3d7b-97a9-02838287e0a7 | -3.05173 | -54.21245 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0d70a1a4-9151-3e85-adb1-be64d21faa03 | -3.09758 | -53.73976 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 93003fa8-9358-3afa-9614-3573d8b3bbdc | -3.00456 | -54.18079 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc0c204e-9582-3a1c-a84a-42849c70c039 | -2.78381 | -51.6696 | 2026-10-06 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b8f5908c-07b8-3b6c-8ae3-4eb865a2207c | -8.59064 | -66.81286 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96e6ab6e-51cf-350f-89e3-a189fae74961 | 1.98289 | -60.61796 | 2026-10-06 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26cadf73-4da0-347d-ae8c-de9837150887 | -4.14903 | -54.02874 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdbe1469-b358-3867-bd20-0b2a0f0715a3 | -2.94499 | -54.14527 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50b98f0d-08d4-3051-bd6c-ad2f4a96f6a8 | 1.78328 | -55.56873 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ad7e232-6b0e-3d92-9679-6a62f8a35121 | -2.96727 | -54.1102 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a424ab59-039d-3994-a640-adaa8fdf9d9e | -3.80749 | -49.11177 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c96efedf-96ab-35c4-b963-3c93974cf4fc | -2.89171 | -54.15323 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61793265-4eb1-3198-93c8-b24eedec3d69 | -2.98972 | -54.10561 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70e5f058-50d1-3883-9530-c2b937034bf2 | -2.99874 | -57.78698 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acdbbe29-7620-3ccb-9c76-6a452f479fdc | -3.08796 | -54.17207 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 978d9383-f39b-3b37-9ebe-92aa963bcda8 | -3.09513 | -53.72639 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a5cc18ce-4646-3dcc-b777-cad60b18ea2b | -3.2859 | -54.17894 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27ed8598-21fd-3910-b862-9771f2dd1af4 | 1.85906 | -55.77039 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 09b4f65b-9fcd-3dac-947a-40ba4d458866 | -3.6535 | -59.16222 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 813b832f-fd78-3ecc-9d70-7e5f1b2c4adb | -3.80404 | -51.03602 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8d585c8-2011-3d19-a366-c890dc2b3869 | -4.14404 | -54.03228 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d322526c-abf5-37db-a1cd-b3f3549fc1a5 | -6.91237 | -59.26489 | 2026-10-06 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195170f9-54ba-3830-b341-4069f11ba9df | -3.33633 | -59.47559 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0de731a1-22b4-3efc-8788-c75eabbffcd8 | -3.16594 | -50.60616 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ead0aa0-1c5f-3788-98b7-7df5a45eb932 | -3.58187 | -54.31473 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd93ac79-443b-3d3b-b4db-906b6fc4e2a1 | -3.12529 | -53.70494 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f4d8953-f962-3234-9368-29a10b323a3c | -3.21725 | -53.87958 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85eae157-f2b9-388d-8966-017c398eb37b | -2.95063 | -54.16445 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d8b28b5-043f-3b3b-a591-0dc25818a87f | -3.58674 | -54.31074 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12e7a15e-5a4e-3ced-96f3-326e4642cafa | -1.50836 | -54.81012 | 2026-10-06 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8030c57a-e0f8-3bd0-bd2c-4bed2703140f | 3.12514 | -60.56131 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63cc400a-1cc7-374a-8094-3dfd0f356618 | -3.09704 | -54.16943 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b141551c-e0c2-345b-8b24-324aa96b0f53 | -3.18129 | -54.09563 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02f234ca-8083-3a25-aa24-84796d8bcfd2 | -3.06482 | -54.15223 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f671b69-6470-3e15-874a-1aea33c424e8 | -3.07347 | -54.18208 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d44089d9-27b5-35f1-a6ee-de83cd2cdeba | -3.10209 | -53.71003 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75446ec7-b56a-330c-a3c8-72b9fac12da3 | -3.32433 | -53.85552 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66cc02cd-e2e5-32b2-ada6-41d71e6d99db | -3.27229 | -54.01464 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b63339-3a15-3f49-8cb2-2a001e7b196e | -3.08817 | -59.18868 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42ba95e8-1d3f-3e8f-909e-d9bd0dbb8904 | -3.31847 | -53.85675 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 05d2d413-93ae-3652-bbef-7404bcadebc4 | -2.13385 | -56.69911 | 2026-10-06 05:23:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2fb93d17-5507-3289-81a0-1279ea1faba0 | -3.11356 | -53.75742 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a98c41fb-2275-3e92-90b5-3917bec433ba | -3.00317 | -54.13215 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d2de2fdb-84f9-3a2b-9500-f2855d9dd933 | 0.49736 | -60.59802 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5512d7-2ded-315f-afb0-5fe143fa9d18 | -3.49022 | -57.78181 | 2026-10-06 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99182ae0-9df7-358e-957c-b351843a0b30 | -3.90386 | -52.16642 | 2026-10-06 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f8454364-91a6-3269-a33d-1206373fae86 | -2.02332 | -56.89405 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e323b74-1595-39a5-af2e-4f726874ec00 | -3.07206 | -54.2502 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| db74fc8a-4fd8-3338-9ba3-29d0a9eee5fd | -3.09951 | -53.72705 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 35e70e0a-4225-32d0-afbf-b942ae6eed02 | -3.63326 | -58.94355 | 2026-10-06 05:23:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 342a2e31-6a60-3c86-a4b7-e05d1b391952 | -3.23583 | -53.87395 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a3d3c97-9482-352e-baf8-a8601dc75482 | -3.05919 | -54.22023 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 778845df-d2d5-384e-a041-9c8f2146950f | -3.51991 | -54.63554 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e3337ea-86cd-3036-9a14-a554c1233e78 | -8.9774 | -65.44176 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0366511-1cdd-325a-9989-b2f47e46a3a6 | -2.78219 | -54.10445 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b03fde91-dced-3bde-af0d-fd123fb203c5 | -8.6826 | -66.59751 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f936e38-12c3-3c6d-870a-a2c12458bc4d | -3.07392 | -54.14951 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84b45221-1ffc-383c-8c60-a621de9534e6 | -6.96285 | -71.49565 | 2026-10-06 05:23:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59ec5c77-c4e6-3a2c-ae99-843e418067aa | -2.9922 | -54.11821 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e24453c-6090-3a37-b318-38a161a001db | -3.54509 | -59.48705 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44e5e578-201b-3a72-8f19-b18c2054eb07 | -8.76566 | -63.6905 | 2026-10-06 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 755528ab-e031-3144-906d-6cc4c82c395e | -2.90241 | -54.08186 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README52.md)
