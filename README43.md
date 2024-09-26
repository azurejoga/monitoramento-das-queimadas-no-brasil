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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db99f2bb-fd90-3454-ae47-2b2d2ba1b6ee | -11.1845 | -54.7769 | 2024-09-26 02:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| ff6a1ad3-6985-32f6-bd9d-8db5e299c136 | -11.2123 | -51.1415 | 2024-09-26 02:06:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| bb78bab8-88e6-3394-9abb-7c3fb68851d3 | -11.26 | -65.2801 | 2024-09-26 02:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 3e0b40be-881b-316a-bae1-7ae7fd55ebcb | -11.2599 | -65.299 | 2024-09-26 02:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 0a5fab74-23f8-3342-b909-04d7d640f344 | -11.5013 | -56.7677 | 2024-09-26 02:06:12 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b60c4bf2-d6fc-307a-82c5-e678f248cb7d | -11.501 | -56.7877 | 2024-09-26 02:06:12 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 8dd58695-409a-3dd6-ac41-5151763c4209 | -11.4824 | -56.7692 | 2024-09-26 02:06:12 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fafc1ce8-955d-3a7c-ac72-f164240cf640 | -11.955 | -60.363 | 2024-09-26 02:06:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 93eaf62d-db87-3ae0-8cb9-f38f14d33bac | -12.2367 | -45.5045 | 2024-09-26 02:06:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 8df7bef5-142a-3de5-ad25-eeed458b33e4 | -12.5276 | -53.496 | 2024-09-26 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| d18933a8-aea8-38ff-b068-c21096480cb3 | -12.5085 | -53.498 | 2024-09-26 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 56f4ed17-648e-3a40-b0e3-ef7e4a37ee86 | -12.8411 | -62.6874 | 2024-09-26 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| c3d763ce-3770-31ae-8931-c4a5abf89b1f | -12.841 | -62.7067 | 2024-09-26 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 603fe156-fba9-3f6a-864d-d0227e62548d | -12.822 | -62.7078 | 2024-09-26 02:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 7922e4e3-28d1-3d95-ad23-1afc748c9d1c | -13.4993 | -61.2698 | 2024-09-26 02:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 829dd41c-523e-3e9c-aae2-e9835a8b4015 | -14.571 | -45.674 | 2024-09-26 02:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a3eae644-a124-314d-a322-a6222e19effe | -14.5705 | -45.6973 | 2024-09-26 02:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| df285098-f9ae-3bd8-a12d-27c1ab67ac2e | -15.7676 | -49.9555 | 2024-09-26 02:06:35 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 67b05d7f-f602-3592-8e81-c8d7645ab0c2 | -16.118 | -51.9867 | 2024-09-26 02:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| cfab1766-0aba-3a1c-a321-2ca522a1149b | -16.0985 | -51.9896 | 2024-09-26 02:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 12b78a5a-30e2-3937-b4d1-3b9f3ef21927 | -16.098 | -52.0111 | 2024-09-26 02:06:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| bda18cf6-9114-33ad-9a43-ab2d5e40a84e | -16.593 | -56.0067 | 2024-09-26 02:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 1cb2bf0c-df93-378b-975d-2b55695631ba | -17.096 | -56.3576 | 2024-09-26 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.9 |
| b79e8612-d5c7-3f89-9286-fc47c3fe04e1 | -21.9583 | -48.5638 | 2024-09-26 02:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 0037d29a-899d-33ae-adf2-305dd9f55a6b | -21.9381 | -48.5453 | 2024-09-26 02:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 69643ae9-bdf9-35a3-9852-4b6344a4f788 | -21.9374 | -48.5688 | 2024-09-26 02:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 1b7b7338-02f0-349d-9dd1-48016fc91ec5 | -22.2523 | -43.9057 | 2024-09-26 02:07:08 | GOES-16 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| ff9ac79a-b2fb-371c-99a3-63d104422607 | -2.6785 | -57.531 | 2024-09-26 02:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4ccc1316-59f7-36ee-945e-82bc3ce186ef | -2.6601 | -57.5507 | 2024-09-26 02:15:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 66ae8600-bf4a-3a24-92fa-f890e8532bbb | -2.6968 | -57.5307 | 2024-09-26 02:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 126d6fa5-4b89-3bc9-9ce3-ec2058da9fdf | -3.5674 | -50.3584 | 2024-09-26 02:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7b86dfad-7569-3f73-9366-0d70adda88a7 | -3.5673 | -50.3794 | 2024-09-26 02:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 4bdb09e4-4e10-3e9e-aca5-e77476535c5f | -3.5488 | -50.38 | 2024-09-26 02:15:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 0b30c3b8-6935-39e3-9725-24264feddee3 | -3.9208 | -46.4459 | 2024-09-26 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3aea8154-48b5-3410-a4a0-53df35252c25 | -5.8808 | -48.0908 | 2024-09-26 02:15:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 00086946-2ae8-3759-a648-b80a7d045356 | -6.8024 | -59.3044 | 2024-09-26 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| e9ae319e-71b7-38dd-9628-5d749841daaa | -6.784 | -59.3052 | 2024-09-26 02:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e070bc63-0f36-3d12-81fb-57820af67614 | -6.949 | -63.1048 | 2024-09-26 02:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 0ba94112-a6d0-3a6d-9cf6-009868f24ede | -6.9306 | -63.1053 | 2024-09-26 02:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bf552602-2de6-37e2-b55c-749e4d469aca | -6.9305 | -63.1241 | 2024-09-26 02:15:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| f9465200-2b01-3bb2-b6c3-b397dc1e76d3 | -7.3824 | -55.4924 | 2024-09-26 02:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 182.5 |
| 2274e77b-72e0-354e-a257-690494047148 | -7.3823 | -55.5124 | 2024-09-26 02:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 250.3 |
| a7f94ed8-c4cb-3ff0-a68f-dc4f2dcd72f4 | -7.3639 | -55.4935 | 2024-09-26 02:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 0fe1c5f0-2abe-3ae0-8255-7b299f9127a0 | -7.3637 | -55.5134 | 2024-09-26 02:15:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 222.6 |
| c0c7df05-0ad4-32aa-99e8-3a52edae0775 | -7.2905 | -61.106 | 2024-09-26 02:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f78e5b0d-9067-37d3-9c1b-f2954681fcdb | -7.5894 | -42.2971 | 2024-09-26 02:15:49 | GOES-16 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 1f973379-e837-3615-945f-b24e90f8595b | -7.5769 | -62.7828 | 2024-09-26 02:15:50 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| c3dde60f-088d-3d36-8ef2-6d1318b7d897 | -7.8156 | -54.7252 | 2024-09-26 02:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| d6bc5ae1-6f7f-3d00-b9c3-4aeaac1ed3fc | -7.8154 | -54.7453 | 2024-09-26 02:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 828c71c2-474c-3e9b-a311-3fb5e49d6acf | -7.7314 | -72.7695 | 2024-09-26 02:15:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 1558558c-a7c3-3dd7-9f03-31d47f69cafc | -7.797 | -54.7263 | 2024-09-26 02:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| a059f4a2-51e5-3c31-8563-144f83c1dbe8 | -7.713 | -72.7696 | 2024-09-26 02:15:51 | GOES-16 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 9203d0a5-be80-3253-bd01-78803b4a812c | -8.1757 | -61.3946 | 2024-09-26 02:15:53 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f14451b8-5709-34f2-a4d7-2b54fa490d8b | -8.1394 | -61.2817 | 2024-09-26 02:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 15583f9a-e29c-3c99-9782-5ba8beb6d564 | -8.3155 | -54.9956 | 2024-09-26 02:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 54295547-36fa-3ecb-821b-23e5eedea579 | -8.6847 | -67.0097 | 2024-09-26 02:15:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| f5a8dee6-9b1d-3c93-b523-ccd8dba0919c | -8.7087 | -54.7881 | 2024-09-26 02:15:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| c3a313c8-7b5f-3315-97cb-080024c9e9fc | -8.8284 | -58.2161 | 2024-09-26 02:15:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 5d3d6d44-bb97-3844-8a2c-500e7133821d | -8.8098 | -58.2172 | 2024-09-26 02:15:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0ad127ca-8d0a-3f47-87df-01f1716d5faa | -8.8096 | -58.2367 | 2024-09-26 02:15:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| e7c81319-5157-30d6-96ab-422aa725ce52 | -9.1046 | -61.1237 | 2024-09-26 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 43919004-57f5-3bd9-8de5-62c933703490 | -9.1035 | -61.2769 | 2024-09-26 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| d8d101f1-8efa-3cb5-afb1-b207b82b96df | -9.086 | -61.1245 | 2024-09-26 02:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 56d2756e-e162-3f82-82a9-0a05ae0545ed | -9.1535 | -65.5634 | 2024-09-26 02:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 7b1d0b11-8c43-379f-b2a9-d4e366ce9f8c | -9.1349 | -65.564 | 2024-09-26 02:15:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e8594dd1-14b2-34fd-b43a-4fee992aa2e8 | -9.6018 | -50.1352 | 2024-09-26 02:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f5a04a14-506e-3da6-bfdb-3cf7a7f845bb | -9.6015 | -50.1566 | 2024-09-26 02:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 341aadfc-e201-375a-9398-bab940ea79f2 | -10.0515 | -53.4432 | 2024-09-26 02:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| de0f0864-a3dc-3f65-bfe0-9507a460e7e9 | -10.0513 | -53.4638 | 2024-09-26 02:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 44700cf4-a246-3dc2-acfe-4a439f9aebd3 | -10.0327 | -53.4448 | 2024-09-26 02:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 175.2 |
| 3e923901-f1c8-3b98-8f12-9ff9eaf7dd7d | -10.0324 | -53.4654 | 2024-09-26 02:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 358.5 |
| 2620ebd3-9fbf-3181-ab87-1050c7810e32 | -10.0322 | -53.4859 | 2024-09-26 02:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| c15822c2-2c0a-30a4-a582-aa4ddfe1d0d3 | -10.0136 | -53.467 | 2024-09-26 02:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 0029a121-4e71-3c75-8a64-d50115537d43 | -10.3882 | -67.8737 | 2024-09-26 02:16:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 48.9 |
| e5ec5d55-798a-3ea1-a016-02d3a2d518d1 | -10.9105 | -57.4308 | 2024-09-26 02:16:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9912db27-e135-3189-8222-27f41f01702c | -11.2223 | -54.7735 | 2024-09-26 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 9e354098-f72b-37bd-9f4e-0dea28b82d3c | -11.2036 | -54.7548 | 2024-09-26 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| c1e66a45-c771-3003-a3f0-650d6c3eccb7 | -11.2034 | -54.7752 | 2024-09-26 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 444.9 |
| 8ecf2b99-0096-3f3b-93f7-63a952328e30 | -11.2031 | -54.7956 | 2024-09-26 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 189.7 |
| d0d8a330-c0b9-3d70-8635-a84c3a6d54bc | -11.1845 | -54.7769 | 2024-09-26 02:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 105a3a8d-0b49-32a3-8f72-3e9588c54e76 | -11.2788 | -65.2793 | 2024-09-26 02:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 96eff479-8cc4-35ad-93a8-e6be21919c3f | -11.2786 | -65.2982 | 2024-09-26 02:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 1c1afa3d-aa7b-3ff7-9585-9284b83889a9 | -11.26 | -65.2801 | 2024-09-26 02:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b20ba2b7-c4bb-3d8c-b9ca-952c03dc7aad | -11.2599 | -65.299 | 2024-09-26 02:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 7d54ffd9-909d-3adc-a566-2c41a166de5e | -11.4824 | -56.7692 | 2024-09-26 02:16:12 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 82ded3f9-3f90-3458-b593-7e5c7c362588 | -11.4822 | -56.7892 | 2024-09-26 02:16:12 | GOES-16 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 125c84a9-5428-3bd2-9e17-6a757ed2bde5 | -11.955 | -60.363 | 2024-09-26 02:16:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| eae68253-8eaa-3141-844c-92dd8c413bbe | -12.2367 | -45.5045 | 2024-09-26 02:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| b3fe9ec9-e716-3709-9345-c9b1dee1c42c | -12.2175 | -45.5074 | 2024-09-26 02:16:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| da45147f-e04f-3687-a3e2-3212be5b9def | -12.5467 | -53.494 | 2024-09-26 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 2b38ae91-39c7-33d7-8b84-e323259a7376 | -12.5276 | -53.496 | 2024-09-26 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 157.2 |
| e69ead07-0e04-3e6d-986a-456f719304ae | -12.5273 | -53.5168 | 2024-09-26 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 0602e18e-2c11-3548-badf-08c30299b155 | -12.5085 | -53.498 | 2024-09-26 02:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 657e0537-55e4-3123-8660-c68dea178133 | -12.7696 | -51.3256 | 2024-09-26 02:16:18 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3c8e59ae-a510-3e12-b495-c6141dc9297c | -12.8411 | -62.6874 | 2024-09-26 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 121.0 |
| b91a1948-2add-339e-a604-a3f8d4a09bad | -12.841 | -62.7067 | 2024-09-26 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 213.5 |
| ef57e070-53ac-3c51-8ff7-4042758b9043 | -12.8222 | -62.6886 | 2024-09-26 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 6cc5f81a-0192-354b-bbfe-497b614b5ad0 | -12.822 | -62.7078 | 2024-09-26 02:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 086f075c-27f4-3448-9a74-1ea5d187279f | -12.8601 | -62.6863 | 2024-09-26 02:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 68e2fd07-4581-38ec-8f12-e767b36723e8 | -12.8599 | -62.7056 | 2024-09-26 02:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |


[Clique aqui para ver as próximas entradas](README44.md)
