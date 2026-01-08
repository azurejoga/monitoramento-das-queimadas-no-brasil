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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aac14d21-5573-3ddd-8c91-6d6082c0fa4b | -1.3309 | -53.1704 | 2026-01-08 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d3bbe352-fcbb-3595-a382-22c9091ab92a | -9.7642 | -35.9107 | 2026-01-08 00:00:00 | GOES-19 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 83.7 |
| 8022fbe6-1ce2-3de7-9aa9-85e874ab111b | -1.3309 | -53.1907 | 2026-01-08 00:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| c9baf9fd-0959-347b-ba58-3e076560fc13 | -20.8921 | -52.3522 | 2026-01-08 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 141.7 |
| d79a73cc-e040-3f84-ae4f-0df08e15d55c | -4.2728 | -43.7601 | 2026-01-08 00:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 530e6931-04c4-36ec-8d21-cc6649e6ec48 | -4.2726 | -43.7832 | 2026-01-08 00:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 7d590cb3-1b33-3378-8fdf-ad4ba874298d | -20.8927 | -52.33 | 2026-01-08 00:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 112.6 |
| c4952c55-4546-316c-983b-33352b02fe41 | -9.8339 | -36.304 | 2026-01-08 00:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 134.2 |
| 1544442d-941e-3181-9ec4-d591da50c9f9 | -9.8339 | -36.304 | 2026-01-08 00:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| 474f2637-114a-3886-a513-834337d2efa3 | -20.8927 | -52.33 | 2026-01-08 00:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 115.3 |
| cd6dbe3c-4f76-35e7-a927-bdfcc57e528a | -9.8532 | -36.3006 | 2026-01-08 00:10:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| abaefe96-e216-315f-96b3-85701ab6271d | -4.2728 | -43.7601 | 2026-01-08 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 2612bd40-37c8-322c-937a-6a202fd1a3b6 | -20.8921 | -52.3522 | 2026-01-08 00:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 85e43bf8-228a-354e-b6c4-9c20ffaf0dae | -1.3309 | -53.1907 | 2026-01-08 00:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 258103d2-acca-3d50-a6be-559547f1e27a | -6.9813 | -35.0267 | 2026-01-08 00:20:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 90.9 |
| 8e66af0f-b737-3386-895b-6c6f0d38a4c9 | -20.8927 | -52.33 | 2026-01-08 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 3cf519ae-9e8e-36d2-a356-821c1c53d526 | -1.3309 | -53.1907 | 2026-01-08 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 38f8294f-8253-36ca-bc7e-ad73e73fc799 | -4.2728 | -43.7601 | 2026-01-08 00:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 6bcdea52-7069-3f86-b88c-6b9f578b9d4b | -20.8921 | -52.3522 | 2026-01-08 00:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 8a643134-48f9-373a-bb64-1805444c9f07 | -1.3126 | -53.1909 | 2026-01-08 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 39820138-5e2c-30e6-b42d-9c260ab7a049 | -1.3309 | -53.1704 | 2026-01-08 00:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 086f0f4c-c01c-33c9-83f9-c762661810e5 | -26.8268 | -48.73706 | 2026-01-08 00:24:00 | TERRA_M-M | NAVEGANTES | SANTA CATARINA | Brasil | 4211306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 952adab5-c8e5-37ec-9f7a-7ddca3bc6a74 | -28.1828 | -49.08418 | 2026-01-08 00:24:00 | TERRA_M-M | BRAÇO DO NORTE | SANTA CATARINA | Brasil | 4202800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 25437633-a133-3cc8-b36d-901d56a27a82 | -28.18139 | -49.09092 | 2026-01-08 00:24:00 | TERRA_M-M | BRAÇO DO NORTE | SANTA CATARINA | Brasil | 4202800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| f3d2cf53-57c3-3ac7-8874-7be9e041a5ba | -20.7132 | -49.82578 | 2026-01-08 00:26:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 99da162c-ee48-38ca-b269-61d6b5c8d35d | -20.71452 | -49.83624 | 2026-01-08 00:26:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 484b0e40-7ca0-30ff-9414-617dc4b44622 | -25.04473 | -49.39987 | 2026-01-08 00:26:00 | TERRA_M-M | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 0179beb1-a50c-3d6f-b842-0d5cc2fbc3e7 | -26.11816 | -51.54956 | 2026-01-08 00:26:00 | TERRA_M-M | BITURUNA | PARANÁ | Brasil | 4102901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 98cb0ebd-4c10-37c8-b2fc-978f08bf963d | -25.04611 | -49.41134 | 2026-01-08 00:26:00 | TERRA_M-M | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4abbcdc1-7e8d-3f91-bd3f-e9b07d7bbda5 | -22.83063 | -49.29369 | 2026-01-08 00:26:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 53934d0f-583a-32fd-a76d-334071846b8c | -20.89057 | -52.35386 | 2026-01-08 00:26:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 66.9 |
| a3b5f02f-926d-3d9e-9ddb-1d32fe5fde48 | -20.88892 | -52.33881 | 2026-01-08 00:26:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 76720d71-e0c3-33a2-afb0-40e21e0ca41b | -15.142 | -45.27474 | 2026-01-08 00:28:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5d5020ed-7de8-32b9-ad5d-535bee3e3aec | -4.2726 | -43.7832 | 2026-01-08 00:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 2224f82a-ea61-311e-9084-ac0b6c0220e0 | -9.8339 | -36.304 | 2026-01-08 00:30:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.4 |
| ca68b3f8-1fb9-3181-b992-c6263f6f4f5d | -1.3309 | -53.1704 | 2026-01-08 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 86316d03-f044-3d01-a7eb-391537a7311d | -20.8927 | -52.33 | 2026-01-08 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8d7f2e8d-b4cc-36d5-a0ef-e039d83adfa3 | -20.8921 | -52.3522 | 2026-01-08 00:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ef7d0d01-3b5f-3c1e-b08d-dd2394dfb08d | -1.3309 | -53.1907 | 2026-01-08 00:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 9dfc9de3-e17e-3227-bf81-f97add31bee1 | -9.9319 | -36.2059 | 2026-01-08 00:30:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 808e5563-7ab8-3fe7-aa25-87156f87c1c4 | -4.2728 | -43.7601 | 2026-01-08 00:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| dc470d40-1faf-3df9-9adb-d15b02a2f1ee | -3.56569 | -47.18205 | 2026-01-08 00:32:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83f2ebcd-e4b8-3aa5-97e6-74ad99f54753 | -1.7241 | -53.18431 | 2026-01-08 00:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 31c838e6-5f61-3ede-bb72-846d72c1876a | -5.32003 | -44.55546 | 2026-01-08 00:32:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d98ec411-edad-3be7-b98f-41bec4323912 | -5.3839 | -45.39864 | 2026-01-08 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 5afcda48-88fc-3443-abaf-87071bb5b3ed | -3.43008 | -50.65138 | 2026-01-08 00:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e2720ae6-f29e-3d4b-816a-d5d4be718929 | -3.26596 | -50.5258 | 2026-01-08 00:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0b2c9728-ab47-3029-a8c2-eb039619e83d | -3.66567 | -44.81247 | 2026-01-08 00:32:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 17.4 |
| cb17a26e-df0d-3066-b53e-5ea40c6c99dc | -0.08766 | -51.28351 | 2026-01-08 00:32:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 605663ec-0cff-39c1-903f-24d803264dc0 | -3.17988 | -51.10173 | 2026-01-08 00:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9440e482-d8b8-33af-95d0-e2b56e134234 | -3.43132 | -50.66029 | 2026-01-08 00:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 69349242-8c29-3fc6-a09c-69841defea5e | -3.51884 | -52.89801 | 2026-01-08 00:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 546c4be7-c554-3ad1-a751-7826b97afa89 | -1.92081 | -53.47876 | 2026-01-08 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 5158af71-2f7e-3580-af3b-ff36ea0e9548 | -1.32721 | -53.17931 | 2026-01-08 00:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 2bb2a6e6-8f40-303f-8533-1ca5734537da | -3.3145 | -49.88673 | 2026-01-08 00:32:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f2a20a3f-bb75-3ed8-9297-783b54e040b6 | -3.65454 | -44.82084 | 2026-01-08 00:32:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 9338c4e8-8227-3df3-ab7d-5c8bd3bce681 | -1.32845 | -53.18846 | 2026-01-08 00:32:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 164.5 |
| 6c58dde6-6a37-30cc-8d9f-c3f4a73f974d | -2.04195 | -52.0785 | 2026-01-08 00:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| efb01ca8-d4a4-3b55-99ec-f69abc26a0ef | -5.3813 | -45.38168 | 2026-01-08 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d54c1d82-e3a3-3c1e-a119-c37912df4e40 | -4.27049 | -43.76462 | 2026-01-08 00:32:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e71dd9e0-0a02-3650-837d-3ea11bee9e30 | -2.78652 | -53.00104 | 2026-01-08 00:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a615d961-5a9f-393a-ba37-c282cfc2ba3c | -3.05821 | -50.95416 | 2026-01-08 00:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7192a8f8-d9f6-3dcc-89a4-ff1216cc3097 | -3.2647 | -50.51679 | 2026-01-08 00:32:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| dcc40d70-9e53-356d-bb01-18f75388f469 | -2.15632 | -53.64911 | 2026-01-08 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8ac1936a-46c2-34b7-9fe4-b3fc95808fe9 | -4.27409 | -43.78861 | 2026-01-08 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| faf632c7-8a18-30f8-823c-ba5e0fc7400e | -5.38816 | -45.38705 | 2026-01-08 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| db0d0ae3-c123-3e37-a820-adaf3edf181b | -0.21197 | -51.4499 | 2026-01-08 00:32:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9f7c45e5-1e9f-3efa-958a-ad71dc330cad | -1.92996 | -53.47748 | 2026-01-08 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 40f58a69-2fa3-32bc-aff6-2cae9a156676 | -4.2728 | -43.7601 | 2026-01-08 00:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| b510c2d3-b99d-3b67-b5af-bd08c8d3dbbf | -20.8921 | -52.3522 | 2026-01-08 00:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 514e25b8-10ea-3683-8af7-880aa9c2e377 | -1.3309 | -53.1907 | 2026-01-08 00:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| a3658382-6786-3e13-bb2c-7c56b59c7e75 | -1.3309 | -53.1704 | 2026-01-08 00:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8c61b4e0-7cef-37ee-abbe-dd79dabe0d22 | -20.8927 | -52.33 | 2026-01-08 00:40:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 36676a30-5919-3d8b-99dc-e223c1d844f5 | -1.3309 | -53.1907 | 2026-01-08 00:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8a666916-c6e0-3a39-9728-1c9c08ac8953 | -20.8921 | -52.3522 | 2026-01-08 00:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6e96086c-ebf6-36cc-ae34-a564b55ea315 | -4.2728 | -43.7601 | 2026-01-08 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| d5974768-e296-32b1-ac8f-806278577d6e | -20.8927 | -52.33 | 2026-01-08 00:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 05d465fd-069a-364b-8e50-fd5f0ce6160a | -1.3126 | -53.1909 | 2026-01-08 00:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| e154b44d-6d1a-3040-b7fa-0b10e4efd1c9 | -20.8941 | -52.346298 | 2026-01-08 00:58:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b9b8d55f-b43b-3bce-bde4-bd29bf17dbda | -20.559401 | -57.952 | 2026-01-08 00:58:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d90838d6-a2dc-3c8d-8292-582fe76f9220 | -21.5466 | -57.522499 | 2026-01-08 00:58:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4a824ea3-312a-3823-8dfd-981054c006ae | -21.5385 | -57.5322 | 2026-01-08 00:58:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 32333bcd-2ed8-3681-b5f9-7408a8440547 | -21.5369 | -57.524899 | 2026-01-08 00:58:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8e82b37a-25e3-3966-8497-875fdd773928 | -20.8815 | -52.337601 | 2026-01-08 00:58:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 816b07c6-f9f4-3026-b793-da89a8ccf96e | -22.817699 | -49.280399 | 2026-01-08 00:58:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6b8072df-9d94-3b88-89ad-76ef139c2bec | -20.8883 | -52.3232 | 2026-01-08 00:58:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 250a70c9-fa7b-3817-a715-64f00f5d57c7 | -20.891199 | -52.334801 | 2026-01-08 00:58:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e1b95631-3b47-35ee-9ae6-c38ea73efa0a | -21.548201 | -57.5298 | 2026-01-08 00:58:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 90a2a6b3-b811-3015-956e-9dc49b467589 | -20.729099 | -55.153198 | 2026-01-08 00:58:00 | METOP-B | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 320b2cc6-0d79-37ae-8d07-0a9f343a6b85 | -22.827299 | -49.277401 | 2026-01-08 00:58:00 | METOP-B | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1182cee2-282a-32bb-9f67-e9ebe9008761 | -4.2728 | -43.7601 | 2026-01-08 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 42dba2d5-6c59-3386-a11e-9c0820dfdb50 | -4.2726 | -43.7832 | 2026-01-08 01:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 25b98b7f-70c9-3576-9a40-ba3d9d0009b6 | -20.8921 | -52.3522 | 2026-01-08 01:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| eab46602-b773-3893-9681-d8ad6239e8f4 | -20.8927 | -52.33 | 2026-01-08 01:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ddb3761a-c05e-38af-a434-7279c77fe046 | -1.3309 | -53.1907 | 2026-01-08 01:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ddcee24d-55b9-3eaa-8a42-42d769e7429b | 3.6666 | -60.279202 | 2026-01-08 01:00:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6dd361-bd99-3b93-81b0-a04533b3c01f | 3.6684 | -60.270802 | 2026-01-08 01:00:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4c32d025-f238-3885-a18d-876d11215d61 | -1.3212 | -53.1866 | 2026-01-08 01:00:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eddd0086-12c0-37a8-94d3-3a8b0beefb85 | -4.2726 | -43.7832 | 2026-01-08 01:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 445a7493-0c6f-3bec-a64c-402a1efed2a6 | -4.2728 | -43.7601 | 2026-01-08 01:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |


[Clique aqui para ver as próximas entradas](README2.md)
