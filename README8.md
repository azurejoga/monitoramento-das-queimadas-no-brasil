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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 590238ae-e7ba-3e5e-aae1-6d66644f1aa9 | -2.7962 | -51.352299 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4f71551-9ca8-383f-bf8c-5be68575355b | -2.8621 | -51.649101 | 2024-10-12 00:25:38 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb37dbbc-bea5-353f-9227-8f6c7d37ebf7 | -2.8644 | -51.6595 | 2024-10-12 00:25:38 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d702e18-b6f3-3b81-9d93-39c16cf8694d | -2.7843 | -51.344398 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 460553cd-72cd-3d59-a225-14a83b2aead1 | -2.7865 | -51.354401 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c63c28-833f-376c-b1e1-0609db8da2eb | -2.7887 | -51.364399 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17aa7beb-cf18-3171-8ed1-c8aef9c15b80 | -2.7745 | -51.3465 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a082b5-cc35-327a-9ff0-f4160ba58f0a | -2.7767 | -51.356499 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80bc99e5-9e97-3c48-bf9e-648751fa5657 | -2.779 | -51.3666 | 2024-10-12 00:25:38 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df026385-ebda-3043-84e8-b1905ad5397a | -3.5998 | -55.422298 | 2024-10-12 00:25:39 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df9d26c-6a3b-3db3-87ea-0b267b8f425e | -2.9921 | -52.8843 | 2024-10-12 00:25:40 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67336c81-e8e9-310f-9443-52960dd70f49 | -2.9823 | -52.886398 | 2024-10-12 00:25:40 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340ffa5f-83fd-3b98-bbad-249668685ede | -2.9726 | -52.8885 | 2024-10-12 00:25:40 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce19bdb6-b0dc-3e39-9803-acecedb87411 | -3.518 | -55.419498 | 2024-10-12 00:25:40 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5e71f6-d016-3e39-8f76-e615f45e10b6 | -6.0791 | -44.6276 | 2024-10-12 00:25:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| d283a44c-ed8f-3ebc-b56a-d53f054ee071 | -3.5082 | -55.4216 | 2024-10-12 00:25:41 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1594705a-fd4e-30a4-afa6-4f410bdb3424 | -1.6269 | -48.011002 | 2024-10-12 00:25:44 | METOP-B | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56691b6-64e1-38e2-b5d4-68034d5f5017 | -1.6285 | -48.018002 | 2024-10-12 00:25:44 | METOP-B | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ba8940-7836-3082-b307-b25548bad541 | -1.63 | -48.025002 | 2024-10-12 00:25:44 | METOP-B | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb8716b-2b04-372e-a2fb-90d562815a35 | -6.7284 | -59.346 | 2024-10-12 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b7ca36c3-f557-3fdb-80a2-38189d4201cf | -6.7285 | -59.3267 | 2024-10-12 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 907fea72-46c1-3cd0-8cfc-a6c8d61a961e | -6.7469 | -59.3452 | 2024-10-12 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 482f6947-7d3a-3e30-a172-8d15ddf3205d | -6.747 | -59.3259 | 2024-10-12 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 164.9 |
| 2bccbd39-9d9a-3544-9aab-356e2a0facbc | -6.7471 | -59.3067 | 2024-10-12 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 1b47e3e8-2865-324b-8bb2-a96be85e7c68 | -6.7654 | -59.3252 | 2024-10-12 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 848c6b21-3a08-32ab-8afb-9d00e267175c | -2.9637 | -54.0994 | 2024-10-12 00:25:45 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c408159-5375-3ea4-8db4-7c73eb928d42 | -6.8591 | -59.0705 | 2024-10-12 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a1e9ab4c-fe04-356d-b36b-e3984f5b0748 | -6.8776 | -59.0697 | 2024-10-12 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 480fe585-6fce-3482-b7f1-c2d1f5684361 | -2.6696 | -53.322498 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3667fc0-b5cc-3503-a25f-d54e4b946328 | -2.6726 | -53.335899 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f117d6-1a00-300c-bcc4-593e55d77ac0 | -2.6599 | -53.324699 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01c8ee32-a667-3cbc-a99d-8cb2dd9d4948 | -2.6628 | -53.3381 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1de742e8-786e-3ed8-9cdb-35b4d4b83d37 | -2.794 | -53.977402 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e528a6d-3ec4-30a8-b763-19de340fb519 | -2.8006 | -54.007301 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d16fe79-0dc8-3c90-8661-f21628ae9601 | -2.7875 | -53.9944 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9587ded-85a3-3bde-a384-b4514a9a47bf | -2.7908 | -54.009399 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c1691a-50c2-319e-a4fc-69469a27e143 | -2.7973 | -53.992298 | 2024-10-12 00:25:47 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48b76c8f-49a0-342b-a8e6-f2f22c335176 | -8.214 | -61.1831 | 2024-10-12 00:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.6 |
| babb29fc-458e-3e7d-b2b9-bf2f915f4b27 | -1.0657 | -47.989201 | 2024-10-12 00:25:53 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e42f42f9-b70a-3362-8cdf-ae737098737a | -1.0673 | -47.996201 | 2024-10-12 00:25:53 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d1d6a8f-9dba-39c1-bb80-3098273604b5 | -8.2325 | -61.1823 | 2024-10-12 00:25:54 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6007d588-c87e-3050-957b-4315128fe7a4 | -1.07 | -48.236698 | 2024-10-12 00:25:54 | METOP-B | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b29e5a6e-afce-39fd-987b-beccf63d6267 | -1.092 | -48.837299 | 2024-10-12 00:25:56 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23382c27-cd45-3c6f-b3dc-8bb85868d1bd | -1.0937 | -48.844601 | 2024-10-12 00:25:56 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f222e24a-6e1d-3861-bc32-f753de8f4eca | -8.9042 | -63.5454 | 2024-10-12 00:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e03d615a-c2d8-3b12-b3c2-9f8960ad5638 | -8.9667 | -62.3506 | 2024-10-12 00:25:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.1 |
| d1a4a90c-3770-3202-b4ab-2b217f1270b0 | -9.6594 | -56.9635 | 2024-10-12 00:26:01 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d64426e6-52f8-34e1-9a48-5dbaf5fb74be | -1.8961 | -54.395 | 2024-10-12 00:26:03 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e471a5ab-310c-3142-9d3d-d0f7c1f6e378 | -1.8995 | -54.4105 | 2024-10-12 00:26:03 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c809277-0347-35c1-953e-0103ad3d1641 | -1.8863 | -54.397099 | 2024-10-12 00:26:03 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25206f3c-6078-3319-b325-c5c36796d4e4 | -1.8897 | -54.412601 | 2024-10-12 00:26:03 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad370279-dfac-348c-8e8a-f693dc0789de | -1.6049 | -53.319698 | 2024-10-12 00:26:04 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ee083f5-be0d-3fa0-b729-fe0ec485e87a | -1.5951 | -53.321899 | 2024-10-12 00:26:04 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac620e52-dd2b-3cec-a707-785f49c1bf2d | -1.5979 | -53.334801 | 2024-10-12 00:26:04 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 205a09b2-52c9-3f68-b72e-83a68d586742 | -10.3708 | -61.232 | 2024-10-12 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 6c3add46-3f4e-3eeb-a775-ab978603f36d | -10.3895 | -61.231 | 2024-10-12 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 093769ce-4efd-3900-80b1-33a241699d8f | -10.3897 | -61.2118 | 2024-10-12 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1c9c59cd-0839-3d4e-a85d-c73e1ac9d03a | -10.3898 | -61.1925 | 2024-10-12 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| cdc45cba-f766-3c25-ae02-ca01c7e60047 | -10.4079 | -61.2685 | 2024-10-12 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| de54dcde-e0be-3b33-b91d-da6b88d11a8e | -10.8398 | -44.4365 | 2024-10-12 00:26:07 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 21501875-13f3-3f32-946f-e04f2509363c | -10.9506 | -44.653 | 2024-10-12 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ad7b90d5-3b6f-377d-83de-76d9866dc044 | -11.2912 | -50.9208 | 2024-10-12 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8d1e5ce8-42f2-320b-88ea-151a9670dfe6 | -11.3102 | -50.9187 | 2024-10-12 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| c13214c5-de76-3a39-9726-8e72cac0dbca | -11.3105 | -50.8974 | 2024-10-12 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 8d4622f5-0ed0-31c2-9f70-a197bca4ef6c | -11.3292 | -50.9167 | 2024-10-12 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 067f8d7b-dac0-3329-a637-18ec10bccd54 | -11.3295 | -50.8954 | 2024-10-12 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 99cba495-89fe-3bbc-8f16-eac27b43a833 | -0.2287 | -48.936798 | 2024-10-12 00:26:10 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0925c39-36ca-3ace-9ff4-e1b4f1bcb096 | -0.2303 | -48.944 | 2024-10-12 00:26:10 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd88b93b-aecc-3321-9285-c58b455c0b2f | -11.2761 | -60.5038 | 2024-10-12 00:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1c91c683-3398-335d-b811-1123ad9ca035 | -11.2763 | -60.4844 | 2024-10-12 00:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 128c3fd1-4f43-32be-85ef-c75472227cb4 | -1.1696 | -53.388 | 2024-10-12 00:26:11 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd59a207-d13a-3973-8f48-d1917fd9a875 | -11.8188 | -58.8459 | 2024-10-12 00:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 4750a6c4-4110-3998-9714-02c912d03207 | -11.8375 | -58.8642 | 2024-10-12 00:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 213e393a-9bda-3ce8-a02c-ba8c61329ddb | -11.8377 | -58.8445 | 2024-10-12 00:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| 75228011-7a71-3b6e-b81f-9533f307771a | -1.2715 | -54.6623 | 2024-10-12 00:26:14 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f0e479-27a0-3f44-9ab7-1db150cdca2e | -12.6034 | -48.6209 | 2024-10-12 00:26:17 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 33d9fbeb-b341-399f-8410-7371d54ad62c | -12.7793 | -43.3114 | 2024-10-12 00:26:18 | GOES-16 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 01ef0667-7741-33b6-8fe3-609627833dec | -12.7678 | -44.8671 | 2024-10-12 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 4ee9f4e2-e14c-31cf-a984-170e21f7285f | -12.7871 | -44.8639 | 2024-10-12 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 276.8 |
| 8dad4a78-59ff-388d-8024-0cb6129e766b | -12.7875 | -44.8406 | 2024-10-12 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 193.7 |
| 7c4e77f5-77ed-37d0-84f6-a947ea2ce9b9 | -12.8064 | -44.8608 | 2024-10-12 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.7 |
| b66de053-a948-35e2-b2c1-ab42d4b4e8e7 | -12.8069 | -44.8375 | 2024-10-12 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 00b9ef12-680c-3f3d-8c7a-d7c64d7e4932 | -0.4132 | -52.033501 | 2024-10-12 00:26:19 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8fb4996c-a762-30c5-abda-66f213d36865 | -0.4155 | -52.043701 | 2024-10-12 00:26:19 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f78d9f29-3908-3e2c-8e71-fe75572d401d | -13.213 | -51.1216 | 2024-10-12 00:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 2e444fb9-33b3-3cbb-8fdf-c588ff4f6fc5 | -13.2133 | -51.1002 | 2024-10-12 00:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bdc33548-d9c5-3199-b837-62c9b82468c7 | -13.2322 | -51.1192 | 2024-10-12 00:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 170.0 |
| e00aabb1-0c87-33df-a823-83ac728ebd31 | -13.2325 | -51.0978 | 2024-10-12 00:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7b3bd643-7280-394b-a71a-777d0ff9c89b | -13.2514 | -51.1168 | 2024-10-12 00:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d12fbe3e-7150-34e7-991a-e87ce9e97c8d | -0.1072 | -51.634201 | 2024-10-12 00:26:22 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 8852786b-483a-3b5f-a35b-240ef9517226 | -0.1093 | -51.643799 | 2024-10-12 00:26:22 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 52ea3464-b5c4-350a-ab9a-07995cdbbb84 | 0.3922 | -50.9715 | 2024-10-12 00:26:28 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 230ed41e-dc1f-3631-8635-88293e754a9d | 0.3903 | -50.980202 | 2024-10-12 00:26:28 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 059845a6-e478-35b0-a137-31147835290d | -15.6225 | -59.9784 | 2024-10-12 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9c8c8d48-74a0-30a3-8ca0-c1c761b0db85 | -16.9802 | -57.4609 | 2024-10-12 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 0b1e07cf-d9e5-3b71-9b65-5504c49b203e | -16.9805 | -57.4404 | 2024-10-12 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 55d99ed7-f960-3069-890f-72373db4616f | -16.9998 | -57.4586 | 2024-10-12 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 28473ca7-c636-347a-90e9-84ce2a958c6b | -17.0001 | -57.4381 | 2024-10-12 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 1ca54e1a-656c-3296-b316-7ff40a3b0324 | -17.1758 | -57.479 | 2024-10-12 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| 6555af3f-7fe1-3751-813f-1afbc3c38987 | -17.1761 | -57.4585 | 2024-10-12 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.4 |


[Clique aqui para ver as próximas entradas](README9.md)
