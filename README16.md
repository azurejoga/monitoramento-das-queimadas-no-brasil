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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29fab32e-2438-30d9-ab29-6e0858e7f9c2 | -21.75492 | -45.45428 | 2026-08-22 03:47:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bc415b1d-1c32-3c4b-8bca-aba4ea661f83 | -20.07728 | -44.22817 | 2026-08-22 03:47:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3d81cdc8-b971-3699-a6a3-a32dea1f79d5 | -21.02373 | -44.19644 | 2026-08-22 03:47:00 | NOAA-20 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| edbaec07-64b6-3c49-8c6c-05b0d8b42976 | -6.7691 | -58.6873 | 2026-08-22 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 388e3189-7c6a-3b60-b9d6-69b60cf6c243 | -9.1536 | -59.464 | 2026-08-22 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 4030ee11-26c4-3651-91d6-7ece95855e2d | -9.1909 | -59.4619 | 2026-08-22 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 80440463-9075-353b-9fbd-d213cb533b1c | -9.1724 | -59.4436 | 2026-08-22 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 930c2033-8a37-3989-9db1-0df4ce1f4a5d | -6.7693 | -58.6485 | 2026-08-22 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| bac34848-4836-3b15-894f-fe92fcc6effd | -6.7692 | -58.6679 | 2026-08-22 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| deca3ea5-5f74-314d-b062-b77e13d02e2c | -6.97 | -59.0465 | 2026-08-22 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 917f0d51-3545-388d-ae79-2b4d47528d82 | -8.5218 | -54.8411 | 2026-08-22 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9a6d3519-6f53-311d-950f-5823ea622f68 | -9.1722 | -59.4629 | 2026-08-22 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 6ad6bb98-1250-393a-9a97-82c6e12f07ed | -8.522 | -54.8209 | 2026-08-22 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| f2977397-b5fa-3862-b5e9-924a8f545074 | -6.7507 | -58.6687 | 2026-08-22 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 89464a47-2c8d-305b-95e7-80b7aea58b44 | -8.5406 | -54.8197 | 2026-08-22 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 54514b4f-c9c7-3a63-84d1-997cea802ecb | -6.7509 | -58.6493 | 2026-08-22 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9139566a-f046-3c57-9a3c-66a0232a962b | -6.8188 | -59.6696 | 2026-08-22 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 11415801-36bc-3c3b-83ab-2dc34ae89747 | -8.5404 | -54.8398 | 2026-08-22 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 35804345-69cf-39e7-ae4d-8e1fe0fe48e1 | -6.7691 | -58.6873 | 2026-08-22 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c9540642-1896-31ce-930f-017b3f93be9e | -8.5404 | -54.8398 | 2026-08-22 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 7ed20134-e4c0-38d3-8402-449fb2ff3e8d | -9.1724 | -59.4436 | 2026-08-22 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 7c363599-262b-374e-8843-700827e01c23 | -6.8188 | -59.6696 | 2026-08-22 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b1cc12a1-3775-3da4-b6c6-f324b160b2d7 | -6.7692 | -58.6679 | 2026-08-22 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| cb73e2be-2d70-3229-b342-66d07b1a6840 | -8.5406 | -54.8197 | 2026-08-22 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 5845499e-3cb1-3547-8421-dc390beccd47 | -8.522 | -54.8209 | 2026-08-22 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 99abf09a-560f-3b17-acf9-1761da58f30c | -9.1536 | -59.464 | 2026-08-22 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 604785b2-1b5a-3a9b-a9f7-283f2182d3bf | -9.1909 | -59.4619 | 2026-08-22 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ee2af6e9-32f4-3bad-9004-7b821bcd9a28 | -9.1722 | -59.4629 | 2026-08-22 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 3540fce8-8215-3d30-9f4b-f4a41da67e7f | -6.7507 | -58.6687 | 2026-08-22 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 327b9068-6689-363a-927d-8949e144b90a | -6.7693 | -58.6485 | 2026-08-22 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ff2e28e5-13a4-38b0-b03c-6f3bece3e1c3 | -6.97 | -59.0465 | 2026-08-22 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c69ed7ff-be10-3bad-ad4d-88244372b3f9 | -8.5218 | -54.8411 | 2026-08-22 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| c9e99072-3a64-3d22-8dd7-5784e2da2b41 | -6.7509 | -58.6493 | 2026-08-22 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| fd3394e1-68a7-30fd-8de6-c37f9065cc5d | -6.7507 | -58.6687 | 2026-08-22 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 21a82a7a-61f6-3a20-902a-93baa9757698 | -9.1724 | -59.4436 | 2026-08-22 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 364a0201-20ce-3be0-935d-40b7d5cd0d93 | -9.1722 | -59.4629 | 2026-08-22 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| a13751f0-675e-3f70-8d68-dfcfcdd5f7f7 | -6.7691 | -58.6873 | 2026-08-22 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0a3f0366-cec8-3566-bfc3-b098013c95fe | -6.7693 | -58.6485 | 2026-08-22 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c04c2a29-dd2c-365a-8987-b63f30355cfe | -8.5406 | -54.8197 | 2026-08-22 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| eb3b5698-b014-36c0-9b00-e1003e730fd9 | -6.8188 | -59.6696 | 2026-08-22 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| fc2be928-830b-3eea-99f1-9b7cce64fb7d | -9.1536 | -59.464 | 2026-08-22 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 4592fda2-06a2-3a8b-b528-b759442e1779 | -8.522 | -54.8209 | 2026-08-22 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 4b17d1da-9705-3dae-a262-23b1be9cb376 | -8.5218 | -54.8411 | 2026-08-22 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2c633b18-5c11-387a-a4b0-7cfc76dd9c08 | -9.1909 | -59.4619 | 2026-08-22 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 4858e33b-b630-302a-a7bd-e36de35086bb | -6.7692 | -58.6679 | 2026-08-22 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 0f46897c-2484-32dc-bc16-32306b33407a | -6.97 | -59.0465 | 2026-08-22 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| cbd2ea24-e776-3ae2-828e-35a715bf0ac3 | -8.5404 | -54.8398 | 2026-08-22 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| effbdbe1-cc84-3221-8353-5da871b05a18 | -6.7692 | -58.6679 | 2026-08-22 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 70c4e299-2fa6-3ebd-b80c-d332b23f70fa | -9.1724 | -59.4436 | 2026-08-22 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f39b903f-8e84-342b-b7f4-128fdf55e007 | -9.1909 | -59.4619 | 2026-08-22 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 4cb39793-051c-3101-833b-a20509e1a2d5 | -8.5218 | -54.8411 | 2026-08-22 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7b4283c9-989b-371f-87d5-16db23ffd774 | -15.1878 | -48.7448 | 2026-08-22 04:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a6e2a54e-083a-3a2b-b4d0-9dd490e5bde2 | -6.7693 | -58.6485 | 2026-08-22 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8d8b06e4-4f25-3a4d-a134-201c20f269b1 | -9.1722 | -59.4629 | 2026-08-22 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| bff72dee-54cf-3334-82ff-aac48c000754 | -8.5404 | -54.8398 | 2026-08-22 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4a4840d5-3582-3ee9-97fb-60f964c83fa6 | -10.7982 | -50.973 | 2026-08-22 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| bc5e9a7b-f4be-3ad1-9000-443fa48c52e7 | -6.7691 | -58.6873 | 2026-08-22 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 1dca34aa-02cb-3b7d-92ca-0ac6ed53eb7f | -6.7509 | -58.6493 | 2026-08-22 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a4673074-0c55-3b35-9f60-f3d585b97597 | -8.522 | -54.8209 | 2026-08-22 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| dd017158-11ae-3530-b7c6-e5ca8b27e573 | -15.1683 | -48.748 | 2026-08-22 04:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d31dbce9-592c-343c-93d3-dded096a4d5c | -9.1536 | -59.464 | 2026-08-22 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e5aff8b0-f1e1-3ccb-9990-c85ea23c7184 | -15.1687 | -48.7256 | 2026-08-22 04:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7ab09c77-c730-34aa-a22f-958f35ad136a | -15.1883 | -48.7225 | 2026-08-22 04:20:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 378e096c-f29a-37e3-a663-80763294a748 | -6.7507 | -58.6687 | 2026-08-22 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| d3c2d7ef-10bb-3cab-9f83-486353c674cd | -8.5406 | -54.8197 | 2026-08-22 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 90b143fc-14d9-3da2-97df-d2377877a3c1 | -6.8188 | -59.6696 | 2026-08-22 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2e621f49-4d02-3fde-8214-8edbc014fa1e | -10.7979 | -50.9943 | 2026-08-22 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| d4048cf7-e9ea-353e-91da-aeb03dd035ce | 2.79743 | -50.92782 | 2026-08-22 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad1cf3d1-59ff-3137-a2be-668053f281f4 | 2.79361 | -50.93297 | 2026-08-22 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9fd2f50-65d1-3334-8e09-e3d85d2ddb1e | -5.58911 | -44.00705 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51ae196c-7d60-3e62-aef0-300e1472a742 | -5.60728 | -45.34293 | 2026-08-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c0057c-ca2b-3719-a3b7-92af09437090 | -6.2543 | -43.6851 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd7de11c-0ed5-3112-99af-f9f3aaadab40 | -6.87163 | -43.74336 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55e03aa4-bb85-357f-a672-2f6ba28db8c5 | -4.90779 | -45.24897 | 2026-08-22 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c888c3ca-50d6-33a1-8d96-19523870b26f | -6.79044 | -42.66765 | 2026-08-22 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b16940d8-1344-3bae-9173-36394ad8d0d4 | -5.55441 | -43.43008 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 549f4ec0-4afc-346d-ab82-c98cf0f2645e | -6.24608 | -43.69186 | 2026-08-22 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d9a3f2f-a41b-3f78-b48d-56662df1f54d | -5.58624 | -44.00273 | 2026-08-22 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 858b5ba5-8529-3763-954c-4205742ba6f7 | -7.25155 | -44.55244 | 2026-08-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8dadac4-ad0d-381f-8540-4a2c2055db5f | -5.62301 | -45.70227 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5210d4f3-c503-3293-b624-a7f6f6b4b13d | -7.07136 | -44.9964 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95f87a37-cf19-30de-93c3-f878436b04da | -3.53996 | -48.18217 | 2026-08-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d3409834-3953-38a0-8453-9b086c8eca29 | -5.78302 | -46.11632 | 2026-08-22 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b217eed-9f8d-3293-8c21-c0118ae1393e | -6.33814 | -46.52581 | 2026-08-22 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3540480c-c41a-321c-9644-81787a9b3be9 | -1.9895 | -56.46747 | 2026-08-22 04:25:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2feb557-14ea-3364-a3d3-19a04c072635 | -2.56901 | -47.24659 | 2026-08-22 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99145721-bde6-3c6f-8eee-2ff59556bd8b | -7.07473 | -44.99696 | 2026-08-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ee803b2-3170-3aaf-b70e-aef30b6e80f0 | -4.66942 | -41.49589 | 2026-08-22 04:25:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f7042130-8f04-31cf-8e7e-3053009e0831 | -4.66553 | -41.49532 | 2026-08-22 04:25:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 84a2e71f-5982-31e0-bdfb-bfebc4649e2d | -4.42275 | -55.44158 | 2026-08-22 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39a5e017-9e39-3bd1-bda0-e2231fd6c36f | -4.12312 | -49.44505 | 2026-08-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2914ebea-be38-3ff2-8e52-4e44df98a351 | -7.17965 | -42.75175 | 2026-08-22 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 538f1379-f5f2-30b4-8205-871c9aed6186 | -4.17661 | -48.5753 | 2026-08-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96545be8-1372-3190-9f99-880660fc6ad9 | -6.87576 | -43.7399 | 2026-08-22 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| efdbc520-5e84-3009-90ec-5bc6978f392d | -5.92996 | -41.49166 | 2026-08-22 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7da2ccf6-3997-36bd-88b3-1f06ff8bb5df | -5.6034 | -45.34592 | 2026-08-22 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 887edf92-2a0b-3961-a917-ac6d4aa7af44 | -5.82659 | -43.49687 | 2026-08-22 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a10a3012-73e4-3ad0-82e0-d9d3873fbbcb | -6.41229 | -44.83754 | 2026-08-22 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4919e936-7d8d-3acb-aeff-032e6dc082c7 | -3.01236 | -51.05397 | 2026-08-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89b0e21d-f79b-30b8-8649-71d2c641ebae | -2.89879 | -48.79726 | 2026-08-22 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README17.md)
