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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7094b98-fc45-39d5-8552-09e37baca149 | -6.95009 | -59.07573 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d188b0bd-2273-3f0f-b537-a71296ef11a7 | -7.54873 | -55.56167 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 940fbb14-a131-3622-8252-651eede1c598 | -5.16921 | -45.06234 | 2026-08-23 04:44:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 701d3a87-2def-3f8e-b98d-4d7d6bd4e264 | -6.5419 | -58.5154 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d84dffc3-0d7d-30a8-b3a0-696c297a0003 | -8.92563 | -48.53317 | 2026-08-23 04:44:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ed2d998-5800-35d0-9098-3d239ad8ab76 | -4.96256 | -56.27285 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55a7826c-d0c4-3634-848b-15bf435a27bb | -5.61127 | -51.78916 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d967880-04ea-3bc4-8b15-7119f42ba8bb | -6.81485 | -44.81076 | 2026-08-23 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a44bca0-2f2c-3313-8d5b-62ea1b047656 | -6.37755 | -54.97416 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 881829de-6c3a-386b-a6d3-39d001547ed6 | -6.18903 | -53.5216 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9db62e31-2a5a-3238-8ae6-597c025dcd4e | -5.959 | -53.6265 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03977569-1d87-373e-a40c-ffc863824765 | -4.3107 | -46.42019 | 2026-08-23 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbdb8cd7-41d0-3a8e-9b16-64cc6243d2eb | -6.76041 | -58.69244 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08fac767-8c24-306d-8aa0-cdbd67086cdb | -6.54697 | -58.52061 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84964a19-317e-3a79-bcbc-3b2b09b88dad | -6.86303 | -59.40749 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 667985c2-b2b2-3552-a379-d36b18276f58 | -6.80888 | -58.65828 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 271596ab-2280-3767-87f1-65fea97d05c3 | -6.79753 | -59.59808 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4509901e-cd46-37f0-9758-0e22ae62234a | -5.01544 | -47.06546 | 2026-08-23 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54b5ef04-d9e9-3636-bb9d-0b950f9ac2a8 | -6.93857 | -59.06308 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52c79b69-05be-3656-9e9e-10b568f77cc1 | -2.56611 | -47.24984 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de9e5d96-2006-3f9c-acf5-011969e99959 | -6.77606 | -59.7505 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 703ff48f-b0e0-3ea8-b1fb-82850b551745 | -6.94925 | -59.08025 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 93ff8409-9db2-312d-ad37-a946f7594229 | -6.61168 | -58.39142 | 2026-08-23 04:44:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddc14a95-372c-3e77-bc6b-1819b70aa218 | -6.96206 | -59.07804 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7bc25457-1620-34c7-b0ce-64f3106ca8ec | -7.72816 | -46.1394 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 369290f0-ab92-324e-9be7-65cce64f3a41 | -6.79774 | -59.42345 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a86ab093-a7b4-3666-91f1-a1d94efdfa1b | -6.55358 | -55.09261 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca74382d-c49d-37ca-8e7c-4cbf3ad4b5dc | -6.76344 | -58.67557 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5813442f-6af0-3bc2-bb5c-3c76abe6e60b | -8.8134 | -46.61811 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43956d20-904a-3e56-9257-487e62789c5b | -6.79375 | -59.79584 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e61627a3-5f83-3ed5-961a-73f5e922137d | -6.89835 | -55.69828 | 2026-08-23 04:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2749619f-1dd7-3d70-b89e-30000b2aa9b2 | -6.94655 | -59.08769 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a7e1996-30c2-3eb7-971f-f81a1119cae7 | -6.79428 | -59.8067 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19e06bb0-a123-37c8-9540-c738c638fe2f | -4.97472 | -47.51704 | 2026-08-23 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| beeeec2d-5991-387f-9a84-f14aa3dd2e89 | -6.54578 | -56.17265 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1070c0d9-a42c-3709-8205-c14311b2d754 | -2.50028 | -48.13682 | 2026-08-23 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be6639f7-18c9-3967-899c-d7a777e6e297 | -3.01457 | -51.05359 | 2026-08-23 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 38910144-5c61-3982-b454-c52ca12e01c9 | -6.80386 | -58.64181 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee452afd-88b4-359c-82a3-0df743093fdb | -7.84991 | -56.56784 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da8ddf3d-296b-3f92-9522-c9c555845201 | -6.80731 | -59.68549 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ae35781-bbf6-33ec-adf4-995525a3498f | -6.88133 | -59.41127 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be32256d-83a5-324b-bd07-1897434b7a11 | -6.20224 | -53.51998 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90ed5b3d-8f93-346e-9806-41022fc9fd85 | -7.09051 | -45.00697 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0cd9135c-c518-3ca8-a4d8-0dc86746abe5 | -6.19255 | -53.52621 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f8926c2-cd7d-3ef0-853e-ff8c68d60bab | -6.81792 | -59.66255 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 887fa3a4-517e-3a6a-b588-e2b153079c72 | -9.01828 | -40.99862 | 2026-08-23 04:44:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 579be236-738e-3c4c-b6fd-aadb70af5951 | -6.6827 | -58.73056 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 78c3363a-faea-301e-aea0-4732ef5c460f | -6.24995 | -55.39405 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a47f866c-0680-3a25-bfe1-f62ce28d59ce | -2.55616 | -47.24828 | 2026-08-23 04:44:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2938956d-cfbe-3c02-af1d-871d75c28dd1 | -6.37629 | -54.95432 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beff2bc1-6d7d-3f01-9942-4ca32be6d56e | -6.68347 | -58.72627 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e32dd74-13f0-3372-904e-ce91b7bca5f9 | -6.80128 | -59.43866 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20630a1e-d084-30a6-9f51-208557f5b79b | -4.92861 | -56.13037 | 2026-08-23 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| accc5f37-12a8-3173-88db-fd67fbaaad6d | -7.14597 | -43.10178 | 2026-08-23 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b793718-849f-38bc-8328-8dea9b18b28d | -6.83903 | -59.95197 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd07fd61-0f38-38c3-a1ec-1c6818efbbdb | -5.75205 | -47.75705 | 2026-08-23 04:44:00 | NPP-375D | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c7845b0-d343-3b6d-861e-330d290e26a7 | -7.99395 | -45.23809 | 2026-08-23 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cda631e-8341-354c-a665-3c8b242df60d | -6.19914 | -53.48793 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e40560b-8a37-303f-a8db-988252b9da68 | -6.18879 | -53.52257 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 624361b1-0499-32d8-a00d-27a3bf1c7e8e | -7.48589 | -45.15095 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b9a95ef-dc5f-386e-8109-b94b65a8b1c6 | -6.9757 | -59.07127 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f309c50-fe37-3023-ae99-f684c1837ca5 | -4.17043 | -42.44471 | 2026-08-23 04:44:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 12f15c51-516c-3d0e-af9e-1ff0e34b779c | -6.18815 | -53.52645 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea1adfbc-b305-33c7-9996-51499aa1c012 | -6.37962 | -54.97142 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a320be7d-5525-36fb-8994-fbef02d00b1b | -7.0695 | -44.99918 | 2026-08-23 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7785f4bf-c58a-308c-a068-137762fe4957 | -6.8066 | -58.65969 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2442204f-4248-3860-93a6-2a71265b41a4 | -8.09799 | -50.05519 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 715def5c-8185-3f32-91cc-e2e7be9a26fa | -6.18332 | -53.52961 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15eb8092-3d2d-3753-8642-91cc876a791f | -6.66943 | -58.73674 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 1afeaae9-6b17-3457-abea-8c46668c0ee8 | -6.11484 | -59.94002 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21506121-bea3-35bc-96e2-ea0d20b25521 | -8.09458 | -50.05464 | 2026-08-23 04:44:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2880791-21c4-39de-8d82-56344d108964 | -6.78983 | -59.43187 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95d1413e-6c2c-34aa-82de-62cb6e582eae | -8.16447 | -52.05402 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a095d1-c407-32fd-9af3-945ece0cf1d1 | -6.95774 | -59.06788 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc36382c-03a2-382a-b8c1-22e0267c13a1 | -6.9594 | -59.05893 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2f454cb-3867-3a7f-a19b-a771bedd78b1 | -6.79975 | -59.67493 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08da8bec-959b-3f55-b4db-cd7b8c208ac8 | -7.18158 | -42.74566 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f826e04e-2b97-39de-9406-4b7e7cc6ec4b | -7.84885 | -56.57368 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 504edd0b-d41a-337b-b4d4-d5e8e8070e9f | -6.78599 | -58.67293 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1cc428ea-f77a-3744-9d44-023e662419d6 | -6.80375 | -59.59914 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c5cdfa6-03a4-3515-a23b-742144507061 | -6.78675 | -58.66881 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d24ade5-5753-39bb-842e-311f40c5cc85 | -6.80151 | -58.65451 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8b079d1c-d8de-3762-b41d-a6c1b265b3e5 | -6.20093 | -53.52765 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1c11e84-5e5b-38d6-a842-ecc6d80f32c9 | -6.68708 | -58.74023 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| dacd1219-c9e6-3a6f-b5b4-40612511fea7 | -6.78893 | -59.43671 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79a7ab67-488f-3c5e-bbc8-d8fd23ac8e91 | -2.99071 | -48.96371 | 2026-08-23 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0048a0c-5d77-3f6d-b90e-10d506b2f157 | -6.94659 | -59.06124 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c012cb56-5f07-3864-88dc-cf5e046ae667 | -6.2556 | -55.38971 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f2b4672-4668-3768-a4c9-babb6c9af508 | -6.76191 | -58.68407 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3697d3d-ff7a-3049-b6d6-5f76de90aa0a | -6.17998 | -53.52405 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c235ed2-d44e-32c7-b4c6-b6bb94e5e81f | -6.82541 | -59.9547 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1081f96-f799-36a0-8680-6e7baa11bf99 | -6.95176 | -59.06674 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a895902-7e66-3738-94ea-348f21d8ba43 | -6.95137 | -59.06065 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2cb7e79-3f73-3273-b601-84e009e15c9f | -6.87725 | -59.40464 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b4e11f-ea39-331b-9b76-30c8f06c3651 | -4.53699 | -55.51472 | 2026-08-23 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b1478cd-18a6-31ec-b56b-f77925597032 | -6.09497 | -44.89306 | 2026-08-23 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39381a21-f9c7-35c4-bd19-09a620d63be0 | -7.15512 | -42.75293 | 2026-08-23 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| edc10b73-5770-3a13-9770-c4395b4d4213 | -6.66873 | -58.79447 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6c8b767-106d-3c9e-b6eb-32edf1d97421 | -7.01571 | -59.57372 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1cd3c37-4588-3514-b01e-eaef059a6194 | -6.19783 | -53.49551 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
