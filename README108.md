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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da7ae2e3-78c4-363b-8033-03060994e505 | -3.67955 | -55.94485 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46590936-41ee-3e68-989d-6d9b117ed180 | -5.95227 | -46.37907 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08adcd77-a848-38b9-b946-d443b2c2b326 | -5.74564 | -53.4571 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5115d39f-bc66-3b6c-8747-53aca5ff7d0d | -7.21003 | -55.18177 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89f08067-c74e-3553-b71a-927189befe65 | -3.07195 | -54.24831 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1726111-5e25-3f11-a93d-d4f7590a3900 | -4.7772 | -55.72635 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4214715-fcc2-39b1-89e0-a9e37f8837e9 | -2.94238 | -54.14996 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6969b6c8-250c-3cfa-8824-19949f0241f7 | -3.10391 | -53.771 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 71ccea1d-644a-3d2d-b2f0-336730265637 | -3.8431 | -55.99007 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 025246a6-89e8-3d51-adb9-70adeb33f6be | -3.28506 | -54.01902 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a64bf61d-41d6-39a1-810c-1b24bccdb43c | -3.32654 | -50.18541 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cec7fd8-0d9e-3e74-b119-8d04f7d78de1 | -3.16513 | -54.729 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c08e275-5571-33a1-918c-0daf70787e7f | -8.991 | -45.92042 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8adc2393-f252-3377-924b-565e40bbc0b0 | -7.00233 | -59.12619 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 13ee7606-0241-3356-bfaf-0a690af05e0d | -7.39587 | -55.21335 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1d5774b-9fdd-3041-be3e-b7f0e29e95f8 | -9.77924 | -55.11125 | 2026-10-08 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04686659-3f73-3556-9ee4-bfff5d1c54f8 | -3.05092 | -53.91152 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3faf4d38-9494-3939-9634-d997f5cb7c78 | -3.04841 | -54.15851 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53d55ff2-80f4-3875-815b-97bcfc13f12d | -7.46424 | -42.85684 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86ac5612-fc68-37b9-8d03-585c70eebed7 | -2.75958 | -54.09072 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f5f63f0-9424-3d56-b715-006ce3e80317 | -6.87892 | -55.59026 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68d849a3-c510-324f-8254-f04eeacdfa8e | -3.30286 | -54.04829 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f811c19a-8aba-3b8c-8713-95929cfba23d | -3.0272 | -53.94295 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a0a9539-feac-3cae-b7cf-63afeea4c2c6 | -11.74063 | -43.64228 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5b73c65-1fe6-34c2-8d1f-54e0d97ed899 | -3.03464 | -54.08605 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 724577f4-4420-366d-b1c5-1fadf39cb720 | -7.38035 | -46.23922 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b4d4468-2f9b-3969-a801-24a6b7dc9596 | -7.38097 | -55.21128 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc6c908f-a448-3729-ae74-4ad970d64d22 | -3.00973 | -54.10009 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0562bce8-ef9c-3d21-bfb9-b806c9fceedf | -3.59899 | -54.66683 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 00da6e9d-3a15-30b0-b1fd-f5edb6d83b94 | -6.14909 | -52.64662 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb08e664-ca8e-31c4-a6f3-263a1eb786e8 | -7.1863 | -52.61343 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba6ce5b0-1fdd-35bf-8dd7-0bf600253be3 | -10.7779 | -46.58248 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97e8246b-0dea-34c7-b6c4-efd2963e0988 | -5.70194 | -53.48545 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 17681f2f-6b05-34e2-9bdf-fbfec5516f06 | -3.08259 | -54.3976 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b3aedc3-3998-34fc-b9b5-eb7265dd34c4 | -4.37803 | -54.75104 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e9d0df0-d2a1-360b-9a20-3d288145f872 | -3.01895 | -54.13748 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80b9e80b-a3bf-358d-8ecf-d9f40a928b93 | -6.15303 | -52.64355 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a9aa053-5007-34c1-8090-e60991d7ea8c | -3.01298 | -54.05584 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f66eb34b-6c02-3ea7-9502-d3beb77bb515 | -6.92375 | -43.669 | 2026-10-08 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d879f0b2-f177-3286-a473-557edcf6fce3 | -2.46226 | -56.06287 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34a48704-e646-3032-8475-bc9a56c177e7 | -3.04542 | -54.15352 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12b89beb-adcb-32e9-9d12-379b4e50765e | -8.21107 | -46.33544 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 249cf656-bad6-3487-9d79-d79958b20e41 | -3.26654 | -54.0662 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5504677f-c840-337a-b98b-64df957d6405 | -3.02925 | -53.93008 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8530398b-be79-3b25-a826-c2535b195745 | -3.28327 | -54.05548 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0303d537-9f0d-32ad-9205-97b855ab4a9f | -7.4691 | -42.84007 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 88d02c03-cb38-3c58-88be-7e7f6a95d35a | -3.0771 | -54.23993 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d7d5020-db32-33b5-8b7c-262beb77f9d0 | -3.0971 | -53.73671 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 728747e2-3127-311e-8413-96c8cd9c1a49 | -3.28242 | -54.05832 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8466e0aa-3fce-3f49-bb33-3dbac065911a | -4.34281 | -56.25303 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e772bf7-213b-3bff-a262-a59f232b5fd4 | -3.83416 | -55.97257 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 601665c5-fe82-3856-9596-22eca569b972 | -6.9888 | -59.11846 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4751940e-b5d1-3216-b352-d9220d950d16 | -2.5035 | -56.15742 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c1d2728-0fec-3486-8097-7322093b41a0 | -2.99895 | -54.04919 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc7f5cbc-6735-3224-9785-d8be541fb824 | -5.70075 | -53.49288 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9762f9ff-6f38-3ec8-bc67-1c4242bbb5c4 | -3.56879 | -54.49353 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3fe4ffb8-89f4-377e-b411-8f13227f88a9 | -2.94457 | -55.7904 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b41e4fa-e89f-38ee-a6f1-a3e541925a60 | -3.01279 | -54.73851 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31d600c6-290b-32c1-aa7a-60fd2e2b6876 | -3.02934 | -54.07177 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89e9719d-0d5a-317d-8e2e-d3453b2143b7 | -4.54234 | -54.98364 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e064653e-5fea-3ec2-9e5d-3249b25a7f1e | -3.65161 | -54.2864 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7b169271-ac88-3d4c-be87-75630936f43e | -3.00345 | -54.13956 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05f93e2e-9a36-351d-8d2e-c06038f5fc89 | -4.14853 | -54.03672 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63e1ce46-fa3e-3a4b-b6ef-54fbdac89fbb | -6.14349 | -47.93004 | 2026-10-08 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bf4dc890-9a9d-31f9-a466-6df8938b045c | -3.09979 | -54.28912 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ee6e734-252b-38f8-8d67-ee84028e95c3 | -3.03495 | -53.9178 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b399968-03d9-3bd6-a2a0-233d9084a870 | -3.04718 | -54.15088 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec6ac9d2-66a7-3cba-8703-f757c7b59719 | -3.10467 | -53.75937 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f315a6e2-b5fb-36fd-9359-e50f6a7a8166 | -2.72089 | -57.46489 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ef3d519e-e271-3cdb-b845-429f3ac1bb91 | -3.02788 | -53.93866 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ace42f41-5063-3179-9d5f-62ea027b6b0f | -2.49596 | -56.0681 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c406471e-e7cf-3776-b63e-7c903ddb3cb0 | -5.04872 | -49.76246 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae4ee086-427b-35ae-9f4a-6f54db604f53 | -3.00519 | -54.76142 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98a2cdf8-ff6a-38c5-947b-d5a8c47dc851 | -5.95162 | -55.34555 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 48538c64-35c5-3486-b548-1cc65b967638 | -4.80838 | -42.74541 | 2026-10-08 04:46:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85e73526-2204-3693-a7bb-6edc7a7786cd | -2.7772 | -54.07542 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f11d5c0-1d3f-37b1-ba6c-e7db3fe34839 | -3.00185 | -54.12579 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1851d913-07be-3ac6-af9d-f097f4e96120 | -3.87479 | -55.82406 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f21b332-8aa5-3672-a56d-e5490fc64932 | -4.93224 | -55.86901 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f69e2e66-11bc-3855-a564-2dfeaa4074b3 | -3.50966 | -54.66681 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47b3d79f-59b7-3cf8-9ce7-93b4544b94c6 | -2.7765 | -54.07981 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d0047fc9-f77b-34b4-9a2d-376294dec7ba | -3.6633 | -60.61496 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 772336b2-4c9d-39c2-b4ce-be7c395da12a | -2.94201 | -54.05546 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d34bce81-24d3-329b-b1fe-8abc9ce7b18d | -6.4662 | -55.47732 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905cdd63-b505-34f5-b22c-e84af37efa7e | -3.17663 | -54.61313 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a29db002-a13b-399c-b5d0-f80c7b4ba727 | -3.0902 | -54.30138 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9728f089-b563-3cac-90f4-859bd9feb07a | -3.9467 | -56.02138 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbd6fc76-017a-39c2-b2a2-2385141c377b | -3.57164 | -59.49205 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ba6bd1ab-ea9c-3d4a-ab2a-88974db6b8b0 | -6.94856 | -45.27365 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80c71159-3363-3b1f-9fa0-f3571ee5fe5e | -8.07766 | -55.29398 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cced0c2-7c10-3686-a2f7-67e90023f568 | -7.601 | -46.76195 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e351d12-0a84-3021-b9f9-bac84d8595db | -3.21493 | -53.96565 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9b174e3-75ff-3d84-9904-23795506dc5b | -5.09245 | -49.70041 | 2026-10-08 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3afeea51-9e26-334f-b251-4be903866dc3 | -5.87435 | -50.09932 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8ffa3bc-fc27-3513-8dbe-8ce88c034f5b | -4.07449 | -59.83625 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0cd6725d-1050-3828-9c26-5e937d8b8f7a | -3.07368 | -54.28513 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6e806e52-27f6-3606-894d-5cb31a878183 | -4.37351 | -54.75502 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c893de2-2d8a-308d-8827-ce2b2532bee0 | -3.71573 | -59.33631 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac5aaa16-c14e-3ef8-b45b-6fcfd4f5e199 | -6.49076 | -62.85297 | 2026-10-08 04:46:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6511f69-8ea9-3e72-b7b0-354a71af5f58 | -3.51141 | -59.33185 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README109.md)
