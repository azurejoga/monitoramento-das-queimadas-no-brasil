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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e68b9e04-5e09-37f5-8d77-1d3f83760ae7 | -14.5634 | -52.0344 | 2026-09-04 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f8a5fa4c-41da-3508-a1a7-ddf8274e1c86 | -3.7462 | -61.7552 | 2026-09-04 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 73f8f536-79ba-329d-ad38-81db27c0f2d6 | -6.6697 | -59.9635 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 12390c45-89a6-3d08-b90e-d189a67d9d2c | -11.8248 | -46.0448 | 2026-09-04 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dd6ea4fa-236c-301d-9aef-df93a966d0e8 | -7.244 | -59.5367 | 2026-09-04 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 8ccf4825-04d4-3646-8797-d800dbb00413 | -4.6669 | -55.635 | 2026-09-04 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 384f12df-df56-3b8b-8f94-fb1142d25326 | -5.5978 | -44.0209 | 2026-09-04 14:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 20db7acb-ae83-381c-afe6-909e65f00fa1 | -11.8439 | -46.0421 | 2026-09-04 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 50faf3fb-5f11-3493-be6e-4ff3591e36d4 | -15.2275 | -56.3716 | 2026-09-04 14:40:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7d9a0bfe-ba61-3557-bab6-65e815e74a75 | -14.098 | -58.8611 | 2026-09-04 14:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5d8c1a98-0c88-302d-837b-f4839129e900 | -17.1074 | -56.851 | 2026-09-04 14:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 3650df79-167b-3ca5-91d4-82f99ce02522 | -5.3833 | -42.8496 | 2026-09-04 14:40:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 81.2 |
| 2c58ed12-db06-32ba-b15c-2e15b850a038 | -6.6883 | -59.9436 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 931b81c5-591f-3b52-bea8-b46db26f63fe | -14.1174 | -58.8395 | 2026-09-04 14:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 08c363c7-ddb7-3487-b419-21f88ab34c09 | -3.7645 | -61.7548 | 2026-09-04 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 220129fc-9bd3-34fa-839d-7f558e50efc9 | -3.7828 | -61.7545 | 2026-09-04 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 957b98ab-881e-3c27-9943-be395ba4d76e | -3.5723 | -58.6545 | 2026-09-04 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 95e3ea99-19cb-3b84-bcfa-fd42b15f5c9c | -11.2106 | -51.2688 | 2026-09-04 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 76b13ed0-b87d-3200-ac0b-d692d7977307 | -10.4914 | -51.3212 | 2026-09-04 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| ce3cb533-2215-3457-a1b2-ea0d8486a367 | -6.6882 | -59.9628 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 202.6 |
| 5e854132-8253-3b6e-80f3-8dd7b4cf2b53 | -6.6696 | -59.9827 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 122.7 |
| 3ec27917-e31b-32f1-bb9a-118507eaf276 | -6.688 | -60.0012 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.8 |
| c0be7881-7de0-3b02-9810-a3e15e8af97b | -17.0878 | -56.8534 | 2026-09-04 14:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| e4b22cf9-2ea1-3957-b738-ab4b55b69bf3 | -6.6698 | -59.9443 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| f903efb3-abe5-399f-a159-5036399c7860 | -17.123 | -55.9194 | 2026-09-04 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 0816ba43-1b9a-3ff5-bcc8-14153868d554 | -17.1427 | -55.9169 | 2026-09-04 14:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3c862977-3a04-3044-8ef8-b6fa5d895fc2 | -13.4005 | -51.3756 | 2026-09-04 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 73153821-df9c-3e47-b7de-fdf3b9a164bd | -6.1543 | -59.944 | 2026-09-04 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 1c65c0d4-76b8-3209-9c10-af570f63c0b4 | -3.6215 | -60.566 | 2026-09-04 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 86688b0c-65c0-3939-9fd7-2d0308f92cc9 | -3.7645 | -61.7737 | 2026-09-04 14:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 7983131b-3dea-3178-97eb-4375d9411104 | -6.6698 | -59.9443 | 2026-09-04 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 952e2f6d-8e22-3e33-858c-aefcf461c9cb | -6.688 | -60.0012 | 2026-09-04 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| c946c365-0f06-35cf-9054-d690638fd8f2 | -17.0878 | -56.8534 | 2026-09-04 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 7ad49457-ffd5-30ba-83e8-31c8a25a3ba4 | -14.1172 | -58.8594 | 2026-09-04 14:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5237ca01-2c9e-3a6d-8a9e-130b1581f7df | -3.5723 | -58.6545 | 2026-09-04 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 354dcf74-adf9-34df-8eea-99c4625a4076 | -15.8336 | -46.0196 | 2026-09-04 14:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 512517a3-f3ac-322e-873d-d45e3c703fbb | -6.6882 | -59.9628 | 2026-09-04 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 253.6 |
| d4916402-87b9-34ce-8769-a01c924399dd | -4.6669 | -55.635 | 2026-09-04 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 58751f0d-af65-34bf-8d6c-08ce2c1a6eac | -17.0881 | -56.8328 | 2026-09-04 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 3316695c-8c59-3637-955a-40d2cb05a67c | -15.2275 | -56.3716 | 2026-09-04 14:50:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| efaf3b51-2fd1-3c49-a594-7133d1395480 | -6.6697 | -59.9635 | 2026-09-04 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.6 |
| ac0fd4b9-69a3-30c3-b40c-b6b37930cb3c | -11.8439 | -46.0421 | 2026-09-04 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 26d2e34e-3476-3672-9229-4fbf94966470 | -3.7828 | -61.7545 | 2026-09-04 14:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e2f8e99a-7ea1-3c6b-89d3-318d0cea536e | -14.1363 | -58.8577 | 2026-09-04 14:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d2c8a638-5231-392e-80e8-10054e691337 | -15.2866 | -53.8617 | 2026-09-04 14:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| ee3817dd-978f-3e24-8996-056fedc91f85 | -13.4702 | -57.0977 | 2026-09-04 14:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| dfa6450d-c465-3519-8713-853dc8c51cff | -17.123 | -55.9194 | 2026-09-04 14:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 6b363072-bd82-3c37-bdf9-abdeb7436145 | -3.0164 | -61.4848 | 2026-09-04 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8acd660a-364b-3e03-8735-e86adfa562f3 | -11.8248 | -46.0448 | 2026-09-04 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c7d48d81-ea82-343e-9ab3-9683cf518f4d | -10.4914 | -51.3212 | 2026-09-04 14:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 4ffe4fe8-d39a-3b29-8797-a510036e12bc | -6.1543 | -59.944 | 2026-09-04 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.3 |
| ced44bbd-a6eb-32a9-9f83-bc74bb13554c | -13.9853 | -58.6919 | 2026-09-04 14:50:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1a165c30-a507-3672-8387-a30278957f80 | -17.1427 | -55.9169 | 2026-09-04 14:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 2e58377d-8400-38a7-8cc5-592d7f9fbd8e | -9.8433 | -64.9965 | 2026-09-04 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 3bf73a2b-7e1f-35cd-92b7-eb22f5e82d89 | -6.6696 | -59.9827 | 2026-09-04 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| d5a2ef91-22a3-3d32-a67b-867310c72ccb | -3.6215 | -60.566 | 2026-09-04 14:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 41fc2a9c-e18f-33ac-b096-6f13a6e7f8e4 | -12.3488 | -45.6712 | 2026-09-04 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b5068ec9-bf65-38c5-9489-d073a7c941e8 | -17.1074 | -56.851 | 2026-09-04 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 001676d5-b20c-3675-a3b8-a3523da66d21 | -4.6297 | -55.7353 | 2026-09-04 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 295dff84-f5e1-3a18-bfb8-ae0d358be62d | -13.4005 | -51.3756 | 2026-09-04 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ddb229c9-89f4-38c5-995f-cf7bac7296e3 | -6.6698 | -59.9443 | 2026-09-04 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.8 |
| ad7af891-ac95-39df-8d43-0ae35f4ab03b | -13.4511 | -57.0995 | 2026-09-04 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 69442660-2c4b-3881-bd99-b2da128bcacb | -15.2866 | -53.8617 | 2026-09-04 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cd599495-dcc0-3247-9b34-3ee57d233fba | -14.1172 | -58.8594 | 2026-09-04 15:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c8c7ff46-0173-31b5-b70d-73d97506add2 | -17.0881 | -56.8328 | 2026-09-04 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.1 |
| b478530a-e8e1-31fa-9771-c13b39f0ed42 | -6.688 | -60.0012 | 2026-09-04 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 9f0b342d-80f6-3622-8f9e-306e0356f755 | -6.641 | -58.4987 | 2026-09-04 15:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 31e647e5-c1f8-3e09-a780-90c73cf3fea9 | -11.0741 | -51.5576 | 2026-09-04 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 177a5fa0-2237-3e41-8f5a-aae9a26f6acb | -1.4761 | -54.2565 | 2026-09-04 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ea35842e-ce45-3a90-8f16-a201d4a4ae81 | -13.9477 | -54.3971 | 2026-09-04 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 47f6c7f5-2daa-324c-aadd-349f3df936d9 | -17.1074 | -56.851 | 2026-09-04 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| b34a6ff5-a79f-390d-afeb-9c775f2a2711 | -6.6696 | -59.9827 | 2026-09-04 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 70e74728-0664-38ae-a133-bf0887ab7750 | -11.8439 | -46.0421 | 2026-09-04 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 7bf7d3b5-53c7-39c6-8fce-58363fde922f | -3.6215 | -60.566 | 2026-09-04 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 2f034824-e4a6-3b30-b849-8237177c9aac | -11.8248 | -46.0448 | 2026-09-04 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 65e847aa-44db-34a9-870a-7a33ca8365bf | -17.123 | -55.9194 | 2026-09-04 15:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 9e50c483-4904-31dc-9250-f29a980796a9 | -13.382 | -51.3352 | 2026-09-04 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8eb576ed-6422-3c02-97c1-ed4be074c974 | -15.2863 | -53.8827 | 2026-09-04 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d6c69dd1-533f-34c3-9c48-bf2264930e6b | 0.1931 | -51.5011 | 2026-09-04 15:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 7d27573a-cd62-3082-a4d0-6f98b8be1ccc | -15.2275 | -56.3716 | 2026-09-04 15:00:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 8a5d2853-177d-3250-ac9e-818b4f05ba24 | -17.1427 | -55.9169 | 2026-09-04 15:00:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 4acee511-865a-3541-a35b-166ffdfdb0e3 | -6.6697 | -59.9635 | 2026-09-04 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 26c827ff-4869-3cbc-8581-aaba526696b5 | -3.6033 | -60.5664 | 2026-09-04 15:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f31ac946-9607-3856-b33a-7b0db1f7e157 | -4.6669 | -55.635 | 2026-09-04 15:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 557f90bf-2a63-30c5-8520-5227eff0d17a | -11.0744 | -51.5365 | 2026-09-04 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 77ba071b-668d-3cf1-9718-fd5d5591ec4d | -11.8252 | -46.022 | 2026-09-04 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| bf0fb35a-2aa3-324b-a8d3-a981ba4dc78d | -13.7014 | -52.9464 | 2026-09-04 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 944579bb-7e94-39b7-9688-bc32260b2524 | -17.0878 | -56.8534 | 2026-09-04 15:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.6 |
| ebbb54f4-da5c-3a24-ac79-aceb3af2cb5d | -13.9853 | -58.6919 | 2026-09-04 15:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 21257d53-9145-3e95-a02a-dfcab36f592d | -15.287 | -53.8407 | 2026-09-04 15:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f846b667-8556-3d4a-9f3d-6c97a0fe515d | -11.0557 | -51.5173 | 2026-09-04 15:00:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| d4303760-3e8b-3b66-b671-623f66a0256b | -11.2128 | -53.9976 | 2026-09-04 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9e443750-9692-3f8d-b065-ea034028ed60 | -3.0164 | -61.4848 | 2026-09-04 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 6d0b80fb-6e21-3e3f-a029-3b5043aec101 | -17.123 | -55.9194 | 2026-09-04 15:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 50705ef3-cec4-37e9-9a17-14046bcd1d7f | -17.1423 | -55.9377 | 2026-09-04 15:10:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 52ddb640-7250-336c-bbf6-55bda6a55ef9 | -3.3503 | -59.4657 | 2026-09-04 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ea350c50-7ded-35ab-9607-fbada8fc324d | -13.382 | -51.3352 | 2026-09-04 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d08bc9c9-4dc3-37e4-b068-234f376b2749 | -6.0807 | -59.9465 | 2026-09-04 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 5063797b-f6d3-3c74-b713-8d3c9bc101c2 | -14.1361 | -58.8776 | 2026-09-04 15:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 0ef9996d-0ac8-37ba-9772-1d8ade0f4573 | -13.4575 | -51.411 | 2026-09-04 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |


[Clique aqui para ver as próximas entradas](README45.md)
