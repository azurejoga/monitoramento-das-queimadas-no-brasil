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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8a01190-b110-3cea-8148-9078d3aa5baf | -7.4441 | -63.5777 | 2026-10-05 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b43044cc-6beb-3ab0-9e65-2e405c3d5d88 | -9.1333 | -65.9186 | 2026-10-05 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| e4b006fb-dc53-3bd3-a691-fbe8ad794648 | 1.8583 | -55.8018 | 2026-10-05 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d53d133c-02c8-3a3e-8d80-fc6864c8730e | -2.9082 | -54.0907 | 2026-10-05 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| a02e3444-4cf4-39d3-a35c-baab703f10fc | -6.1974 | -52.8295 | 2026-10-05 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| ae4401ef-12a6-3f20-8765-3d95da8cc5b4 | -6.0074 | -53.5325 | 2026-10-05 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 99b1f43c-5a0f-3916-b1b6-896122560c0b | -2.6859 | -49.0325 | 2026-10-05 02:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2dfb51bb-95d5-3b11-99e7-80a670adb6d3 | -6.914 | -43.6816 | 2026-10-05 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 30170bba-3c8d-3705-a592-5e0f9e7978c5 | -6.0075 | -53.5122 | 2026-10-05 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4e38bb9d-267b-3461-a484-384338dc83fc | -2.9632 | -54.1497 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3a7fcc5f-59cc-3609-bccb-7a5d996b9a22 | -2.9449 | -54.13 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| f5ee5f57-2b47-3c9c-992e-8e35d9210e7a | -6.1974 | -52.8295 | 2026-10-05 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 579f1bc2-7e9a-3aa7-9023-5d3e37f93a88 | -2.9817 | -54.1091 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| ceeceb0f-acd5-3891-b488-49083e4b0505 | -6.0067 | -53.634 | 2026-10-05 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5c7768c2-584c-3a51-a047-88ecfb57b7b4 | -6.0741 | -47.2703 | 2026-10-05 02:10:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 20330f79-47a8-3a6f-af73-5ef22edabcc2 | -6.0739 | -47.2922 | 2026-10-05 02:10:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 67ed47db-e2a8-36f3-83a0-4edb0275d12f | -6.914 | -43.6816 | 2026-10-05 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f002f915-6af0-3c6d-9bcf-0c09f1472405 | -6.8952 | -43.6833 | 2026-10-05 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 040f76dc-6b68-30dd-8fe8-b28e609d4eeb | -2.6859 | -49.0325 | 2026-10-05 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 50708eb3-16cd-360d-85eb-70769e7f1241 | -3.9217 | -49.713 | 2026-10-05 02:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 7be7fc57-b302-307f-b0f1-376061ba75f9 | -7.4442 | -63.5589 | 2026-10-05 02:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 5deb22c4-3a97-3b98-8f6d-65f10ba5c640 | -9.1334 | -65.9 | 2026-10-05 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 2f086146-c0f9-370c-9cab-bbda0b70941c | -6.0552 | -47.2935 | 2026-10-05 02:10:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| e9ab3f25-cddc-3780-b38c-e9745407f669 | -2.9817 | -54.089 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 1296866d-1fa1-32a4-81c4-ddfa7afa0411 | 3.1097 | -60.6133 | 2026-10-05 02:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 835d2193-0fcd-32bf-8126-459f0d38e820 | -3.0001 | -54.1086 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6f272053-c318-3444-b72b-f80e984212a8 | -0.3952 | -52.0357 | 2026-10-05 02:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 504b9798-482d-32b6-9e12-1f617e48b83e | -6.0554 | -47.2715 | 2026-10-05 02:10:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4e0373cd-c19e-348d-97a8-91b51ac5c7d0 | -6.2159 | -52.8285 | 2026-10-05 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| b0ed48e1-73a9-3b15-8ddc-3c74805f1dbb | -3.9859 | -55.8152 | 2026-10-05 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 35d04358-b863-3bc9-a40b-248524ac38ff | -3.9032 | -49.7137 | 2026-10-05 02:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2f9ca793-1b0c-3c17-bf0c-9494f5a91968 | -3.0548 | -54.2277 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 9442981d-f075-3cd1-85a5-c23be6db9833 | -2.9448 | -54.1501 | 2026-10-05 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 09244d51-3e1e-3aa9-a9d2-f87e2cd7bbb9 | -5.9882 | -53.635 | 2026-10-05 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| cc59169b-ba95-3244-8070-f1771d945985 | -6.1781 | -52.9328 | 2026-10-05 02:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 5075455d-c79f-3d38-80b2-561c91867f05 | -3.11 | -53.75 | 2026-10-05 02:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d83ec6c-ec30-3c7f-b960-cc6bfca29d44 | -3.08 | -54.18 | 2026-10-05 02:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d51746f5-4552-3769-ada1-1b8c92a7c051 | -2.9448 | -54.1501 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 5bf30ce5-4c51-3a3b-a671-fad7fd52cfcb | -2.9632 | -54.1497 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 95b731e5-c930-3b18-9c5c-c8c2ca362288 | -3.055 | -54.1675 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 2603e914-861c-3860-af39-406380710b07 | -7.4442 | -63.5589 | 2026-10-05 02:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 89.5 |
| db04f16e-a3c8-36bd-a583-9de2cb2e39ea | -2.9817 | -54.089 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5d5e2d66-4a58-3929-9ee8-22d210d71e0c | -6.0074 | -53.5325 | 2026-10-05 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| e9e1f02b-929a-38d4-97d8-b5c528dbf2ab | -6.0067 | -53.634 | 2026-10-05 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5558608c-31cb-3d91-9876-120132aafbb4 | -0.3952 | -52.0357 | 2026-10-05 02:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ef154f36-2f59-378f-adad-b2759b196302 | -3.9032 | -49.7137 | 2026-10-05 02:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b3fdacba-0807-3d98-9d0c-6d7e1eb7e13b | -0.3952 | -52.0152 | 2026-10-05 02:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 8cf68f25-1d39-3953-b97c-9cb64fb8d09a | -3.0733 | -54.1871 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 315.9 |
| 7adbb4eb-cf00-368c-bfd8-2251cdb85c94 | -6.8952 | -43.6833 | 2026-10-05 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 0ae1af69-223e-3cf5-b223-e11c6dcb02b3 | -2.9082 | -54.0907 | 2026-10-05 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| cc6db928-dada-34fe-a230-c0bc3977e378 | -5.9882 | -53.635 | 2026-10-05 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 20c9c68b-a219-3241-b019-aecdf0be1881 | 1.8583 | -55.8018 | 2026-10-05 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| caecfc61-b28a-39db-90bd-dc45a0d0d2ef | -3.0734 | -54.147 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| fa582963-8e12-3f3f-9cf8-e8022d9aebb9 | -3.0548 | -54.2277 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 14f65ffe-5443-3a80-8949-1bfe2ca52706 | -3.9859 | -55.8152 | 2026-10-05 02:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| f684636e-d431-3598-918b-95aa1de1e0ac | -3.0917 | -54.1666 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| bb94014f-7ca6-32c4-b81b-29d7eeba0354 | -3.9217 | -49.713 | 2026-10-05 02:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 16dd3d2d-9414-3e56-87ad-ab2c573e384c | -2.9449 | -54.13 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ca5a58e7-324c-3ada-806b-04cdb9edc299 | 1.7303 | -55.6456 | 2026-10-05 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2d0d113d-ccf3-3c9a-8a7f-36e327687d5e | -6.914 | -43.6816 | 2026-10-05 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 1cbaa797-d9ea-31c2-a360-8535006b67fb | -3.0734 | -54.167 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 376.2 |
| 24568d59-39d3-320a-9b3b-4111842a164d | -2.9817 | -54.1091 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| 89fb3113-adb5-3b26-b3b6-1952b7f69087 | -6.0075 | -53.5122 | 2026-10-05 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6d056f25-18d5-376b-9e80-8b02e55e607e | -6.2159 | -52.8285 | 2026-10-05 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0f8ba1fa-0f58-3ee8-bd74-365275fc1b52 | -3.0917 | -54.1867 | 2026-10-05 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| c3d79996-4543-3ba9-a095-93d650d51c39 | -6.1974 | -52.8295 | 2026-10-05 02:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3d440656-849c-32a6-8c6b-193a9649bc71 | -2.9448 | -54.1501 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 7fd6c96d-4d02-3f91-8c18-e3374663321c | -6.0067 | -53.634 | 2026-10-05 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d700ce88-8f47-39e2-a01f-261ad1a0f1a0 | -6.0074 | -53.5325 | 2026-10-05 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 84adb5d9-f90a-3ec1-b2db-d62d6ef044b5 | -3.9032 | -49.7137 | 2026-10-05 02:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 7eef75a6-99af-3d7c-ac28-7c0042983a16 | -0.3952 | -52.0357 | 2026-10-05 02:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 76.4 |
| b42c13ef-15d6-3470-a693-e6cdbd4a1653 | -6.0075 | -53.5122 | 2026-10-05 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8e6bcdcd-0cd4-3bad-b508-056f30e819a0 | -6.914 | -43.6816 | 2026-10-05 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 55079e90-ec5f-398c-96e9-dc337b1119b1 | -2.9817 | -54.089 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| eb53f8c7-6073-3be9-a04d-7acae303471f | -2.6859 | -49.0325 | 2026-10-05 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| d4ba4e63-4ad0-3d64-96f4-a41fa004424d | -3.9217 | -49.713 | 2026-10-05 02:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 8b923865-f2d5-3ae7-9dc9-9827b20f679c | -3.9859 | -55.8152 | 2026-10-05 02:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8523f4d1-3e1d-3b72-abfd-344e926615c8 | -6.8952 | -43.6833 | 2026-10-05 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 791b2389-1e9a-3484-b33a-cc9ff43aa55b | -6.2159 | -52.8285 | 2026-10-05 02:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| f670e5f9-e89f-3315-9e17-6db601ffcee7 | -7.4442 | -63.5589 | 2026-10-05 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 2e1923ee-851f-3ff3-846f-2ea1c7bd2c40 | -7.4441 | -63.5777 | 2026-10-05 02:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ddfe492b-8eb5-397b-aedc-16bf9bf7b038 | -2.9449 | -54.13 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| bb66332d-3c9b-34dc-8d64-e4e77e3e148d | -2.9817 | -54.1091 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 488bbc5a-d53a-3104-a3ff-b03bbdd153e4 | -2.9632 | -54.1497 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3079751c-3bcb-34e3-b175-dafe75df5617 | -5.9882 | -53.635 | 2026-10-05 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6f05f5e1-d6d8-3d4c-83a3-5bc765fd93d9 | -3.0001 | -54.1086 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 93750f12-fa30-3661-af66-22d00b65314b | 1.8583 | -55.8018 | 2026-10-05 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 311c279f-ef50-3ecb-9f11-df51e4a75cca | -3.0548 | -54.2277 | 2026-10-05 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 74c1d6dd-abc3-3b5e-8453-7d0d8f3c6419 | -3.5128 | -54.6162 | 2026-10-05 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3a8b6a8a-7db6-3305-a20c-d241121573b6 | -3.0734 | -54.167 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 269.4 |
| eecd98e7-ef9c-3300-9576-fb8c3041d00a | -2.9632 | -54.1497 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b1d0977c-ad2f-35ef-834b-caa8d36fdd37 | -0.3952 | -52.0357 | 2026-10-05 02:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 27e60d6c-3d9b-354e-906d-fd5c6e006289 | 1.7487 | -55.6256 | 2026-10-05 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9c1f4ec7-1a18-3067-9d70-b46eb9ba5179 | 1.7487 | -55.6059 | 2026-10-05 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 01ef07ea-7470-3827-ac6c-b4193cc0cb0c | -2.9449 | -54.13 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f160960a-c8b2-3aed-b8cc-612df75e2f25 | -2.9817 | -54.1091 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| f6db5a93-9adc-36f8-80c4-b6af486b8712 | -8.4457 | -62.732 | 2026-10-05 02:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 34eda450-e7e8-368f-9adc-16d89a55bb8a | -3.8447 | -50.3273 | 2026-10-05 02:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e93cd41a-bb20-344c-99bf-fb7f64963fda | -7.4442 | -63.5589 | 2026-10-05 02:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 97.2 |
| cbf2bcb1-fe4f-3ebb-8068-bc51c682d361 | -3.0001 | -54.1086 | 2026-10-05 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |


[Clique aqui para ver as próximas entradas](README10.md)
