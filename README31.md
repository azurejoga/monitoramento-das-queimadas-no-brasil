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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33809063-63e0-3ebf-9617-352c7e4155e9 | -3.15489 | -54.59927 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f6842e66-add3-35fc-922d-997903d4242b | -4.30186 | -49.13198 | 2026-09-24 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef31b0d4-bc28-3267-8a63-75b7e3687005 | -6.3396 | -43.36302 | 2026-09-24 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9ccd38b1-1f5b-3281-b49f-282bccafec96 | -6.52824 | -51.50404 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5eab8f8-5063-3e0e-932f-95d1a98aabb1 | -3.55592 | -43.46343 | 2026-09-24 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c8261c43-5d0f-30c4-ba33-275a1608b238 | -3.45244 | -50.08379 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 781e6c2c-1882-3f5f-b07d-797b77c46193 | -9.15092 | -49.96259 | 2026-09-24 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f6e09e82-61cd-385d-95c4-ea0f3eac7622 | -8.2687 | -54.77465 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b00fca26-e064-3eb4-90e7-d0ca4d4bdec3 | -8.46254 | -48.69482 | 2026-09-24 04:08:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 450dc19b-b547-3f09-822b-4934ff4e9d68 | -5.19674 | -44.69557 | 2026-09-24 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccb6f498-2e8f-3fb1-9d07-55bc7ecd9c82 | -6.19156 | -43.34669 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b2201f8-3ea1-308a-ab0b-4b85ec8c6b09 | -5.7717 | -45.10363 | 2026-09-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f7c71d9e-f3e4-3499-8257-fbb7e2e84e97 | -8.24636 | -48.21577 | 2026-09-24 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0e708b0-4b74-3027-b6fc-30cec4c391d6 | -7.46122 | -44.54204 | 2026-09-24 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ff857bd-a337-3560-936c-8188203a236b | -2.39257 | -48.52232 | 2026-09-24 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 285b0785-dc7a-310e-b139-6055a5f6e2b0 | -5.85233 | -49.77499 | 2026-09-24 04:08:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7bffe957-4f66-3502-b0c6-97b107650465 | -5.76074 | -43.71296 | 2026-09-24 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da99b102-2a47-3325-9883-d6bfb16f18c4 | -6.72825 | -43.94123 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7fee53f7-7976-387a-a616-058884e22430 | -8.73441 | -47.60751 | 2026-09-24 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d514d461-d428-3df5-b50a-afb0f89f8b0b | -6.97377 | -45.04871 | 2026-09-24 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 00b22dbf-5004-393b-ad90-dc255b8fc53d | -5.99163 | -44.42852 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e91e88dc-1bec-32b9-b075-d3d1b9a226dc | -3.55182 | -43.46675 | 2026-09-24 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 839e1279-6810-3a6e-bb11-ef31ff3fc4e6 | -9.58028 | -46.51245 | 2026-09-24 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8f94716-cc20-3f86-b4da-855ccade3a7d | -6.12758 | -44.59876 | 2026-09-24 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c7a1173-283b-3f19-8b53-8424d3926569 | -3.16998 | -51.35986 | 2026-09-24 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45e023da-0646-326a-ad5a-192709eb76cd | -8.45847 | -51.47996 | 2026-09-24 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb2477d7-3c42-3930-b0cc-ccfdc65f70c4 | -6.20416 | -47.49751 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4bf4f2b8-ad25-3b66-b027-843683d49e99 | -6.21328 | -47.49499 | 2026-09-24 04:08:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 493fe7b5-0946-3cdd-b4df-6c13b55cf518 | -3.16191 | -54.60057 | 2026-09-24 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7afc5efa-fd7e-3619-a470-f7e54b2b7950 | -5.99984 | -44.10647 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91e0f6c6-b8d9-3318-9199-7ce2ec69462b | -5.58175 | -42.7346 | 2026-09-24 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5afdbe93-c930-3e35-ac12-0e19a4fba816 | -2.77306 | -48.65857 | 2026-09-24 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df4ca7ed-fff4-3c3b-9e21-f033fed4905b | -8.72307 | -47.60562 | 2026-09-24 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 221f5a71-1086-37d5-a669-ee49d35708e5 | -6.41309 | -44.49319 | 2026-09-24 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e31e6cd1-c4c3-38ac-b22f-7392649a7b7b | -8.30089 | -50.85238 | 2026-09-24 04:08:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfbfd1d5-7120-3252-ba21-cc1705e42c60 | -7.6801 | -39.01178 | 2026-09-24 04:08:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db29fd56-d11d-358a-9fe0-f0eb7fafdc61 | -4.56347 | -44.08144 | 2026-09-24 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53731c5a-4960-333b-b035-cfe37c741f48 | -6.26974 | -43.26954 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 385458e0-af67-3259-97ed-d73c2b5671ea | -7.1339 | -39.97919 | 2026-09-24 04:08:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 58d796aa-f91d-3898-a535-db180f654d1b | -2.88331 | -49.47432 | 2026-09-24 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 039cc473-f9d6-3cf4-bbcd-632525f4cad7 | -6.78073 | -48.67144 | 2026-09-24 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d106845d-7878-36f2-8b05-68a8ee220882 | -4.9981 | -45.55104 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6533d8f6-17ac-39d7-a092-7d9ff2d36ce4 | -8.15428 | -49.54448 | 2026-09-24 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d84ddfab-f0a6-37ed-a925-adcf5b90d1f7 | -9.47048 | -40.33665 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 46.8 |
| 70857bc9-f4ab-3059-afe8-b290b9e549e8 | -5.71876 | -49.83075 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23202fe7-70fc-384b-a9bc-b5564971398a | -6.52817 | -51.50197 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01533035-5984-3f86-b172-f92b51cd59e1 | -6.09354 | -46.36602 | 2026-09-24 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c655902-959b-39e7-874c-8f10d79fa94f | -8.26976 | -54.76925 | 2026-09-24 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cedaba23-40da-3406-9971-471c43c6c01b | -6.87143 | -42.86308 | 2026-09-24 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a3f1595-f36f-38e5-ab47-eb2e7fbb7d18 | -3.17721 | -48.01844 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c0d9e5b7-eb48-3960-8ea9-c2616db0446b | -4.28983 | -48.61019 | 2026-09-24 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e7f9c55-74f3-3304-9a49-0e4e3cc70aa0 | -8.38542 | -46.28827 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e98bbc7f-f693-356e-8ba1-32a6e7a2cef0 | -6.54649 | -43.08451 | 2026-09-24 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8196d989-f0ca-31da-bac0-597e111534cf | -9.9985 | -45.19275 | 2026-09-24 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4686c1b9-0e47-3f29-9e75-aa4a4c0d6a88 | -2.89988 | -54.10008 | 2026-09-24 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2d640f5b-ca0a-38d5-a6dc-af47cb581744 | -5.60108 | -45.95293 | 2026-09-24 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1022d0d-0f27-399c-a89a-951ef7db991a | -7.07813 | -42.06733 | 2026-09-24 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a3d34d77-1003-3292-a33a-426a8b0003c7 | -5.72374 | -49.83179 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7cbf314-bee0-3d72-b755-99680368f537 | -6.72481 | -43.94069 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1eeed34-108c-3e92-9c18-bed82a805245 | -6.57007 | -51.49056 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 162c0a36-b5d2-3851-860f-97b418843b4c | -3.17565 | -48.02801 | 2026-09-24 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b8cfaea-3569-3809-a103-2738af4e0cfb | -8.14458 | -46.82024 | 2026-09-24 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| af75a985-8433-38ed-aac5-b5ef30ba5bdb | -6.42551 | -43.48516 | 2026-09-24 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d731f221-1829-3186-a606-23f29ddaf624 | -2.24888 | -48.74896 | 2026-09-24 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d092514f-0d3d-3c73-89e2-9f2155811eb8 | -7.54489 | -47.32578 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf1c1445-2fea-313a-9b10-6cb7d64c25c8 | -1.02471 | -53.73362 | 2026-09-24 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f65a9aa-1adb-305c-abd7-8e293199a948 | -3.06151 | -49.57563 | 2026-09-24 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54636a40-6001-3ee0-8f38-ef5432910490 | -3.51698 | -44.24609 | 2026-09-24 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89678eb1-436d-310b-9f44-fecba31fb530 | -9.25232 | -47.3455 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b292181-a25e-370a-91ef-4541ec3625a1 | -8.35169 | -45.624 | 2026-09-24 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24f7d068-e891-3063-986f-f0168ce67166 | -9.47447 | -40.3334 | 2026-09-24 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 419be688-51f5-35ee-bfff-877641d19bcd | -6.6274 | -43.78326 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 92f41856-1451-36a4-9d5d-0ecf4def3440 | -5.5784 | -42.73408 | 2026-09-24 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| cb1be545-24cd-3b9a-9716-d0b8f8d46d43 | -7.67317 | -45.48078 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa40a7ec-93d6-34db-9a27-2111c67c68fc | -4.29789 | -49.12565 | 2026-09-24 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a46080b-47d3-386e-80e6-d4d98397bd1e | -6.91951 | -47.66203 | 2026-09-24 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48eb7bb0-2ace-3965-b146-1a16f808eba9 | -5.98878 | -44.42484 | 2026-09-24 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89667848-f9c9-396f-a4c0-2f56334a3253 | -4.11777 | -51.07947 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 80bad98f-6802-30ad-8564-b5eadfda9b51 | -5.8356 | -43.06435 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 71caa996-ffeb-3e01-b0d5-4277f68c16c3 | -5.82936 | -43.0819 | 2026-09-24 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d54a2fcf-d9bd-329f-8d8b-767c9c60c21f | -3.45354 | -50.07728 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 06616410-dd24-3ef2-8169-b349ab828a7e | -5.79195 | -49.19181 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f14b8cbc-643f-3553-aeae-e6c88f89138e | -8.38846 | -46.29354 | 2026-09-24 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9068cd22-c8e5-3536-a00a-3f7de27b08a4 | -6.33079 | -42.94778 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 996f0fdc-4cdd-3995-85c3-e243996cf434 | -6.20793 | -43.35302 | 2026-09-24 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66f72f8c-3c71-3891-8787-1219d4344307 | -5.57561 | -42.73002 | 2026-09-24 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c26971de-d0db-3fe7-b790-0243eaad89f6 | -5.95114 | -51.79517 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd0e01a7-ce3b-34db-9a9f-d6f7acb50bb8 | -1.60578 | -49.81678 | 2026-09-24 04:08:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd56b149-05e4-3131-835c-5365e5ec3c2a | -5.22463 | -49.22668 | 2026-09-24 04:08:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c02fabc8-dfbe-3d22-bbcb-3a915f768ad5 | -7.38506 | -36.93528 | 2026-09-24 04:08:00 | NOAA-21 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bea080f2-b9bc-328f-86df-661a4d23160e | -8.92907 | -45.94483 | 2026-09-24 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ca3abe6-92e1-3737-a67d-a649273763a4 | -7.19784 | -47.4523 | 2026-09-24 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc62dd46-ac12-30f9-9d19-ad89059e3758 | -4.11708 | -51.0836 | 2026-09-24 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9f3b1513-9d39-3570-996c-43e86f79c366 | -9.24832 | -47.3448 | 2026-09-24 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 319b47c7-f242-3c90-80cf-dac4e49442c9 | -6.53376 | -51.50502 | 2026-09-24 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1844909-de89-3edb-a72c-e4bfc5fbfcb9 | -5.84422 | -49.88022 | 2026-09-24 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a20d11cb-27f5-3ac5-ac42-253b6810301d | -6.87476 | -42.86362 | 2026-09-24 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 356cc231-f828-3c3f-ba8c-21acf1182bce | -7.67613 | -45.48557 | 2026-09-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d1844c4-6bb4-3fcc-ac31-1c8621853e6a | -8.72212 | -47.60542 | 2026-09-24 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a3545df-9902-3c10-80b7-a9f3734c1555 | -6.78295 | -48.68605 | 2026-09-24 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README32.md)
