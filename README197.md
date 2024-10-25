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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c4d51b5-9795-3e21-83cd-9abcd813d212 | -5.2838 | -48.3218 | 2024-10-25 19:25:35 | GOES-16 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0ee9782f-c35f-3b6f-ab95-1d6ecaf55f48 | -5.1937 | -45.4384 | 2024-10-25 19:25:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| ebf73c97-7a2d-3261-8111-00e1e02cb987 | -5.2236 | -41.7945 | 2024-10-25 19:25:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 192.4 |
| db7aceba-6118-3506-89ad-2990a5aaad92 | -5.2426 | -41.7692 | 2024-10-25 19:25:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 3052fe7d-2531-359f-a017-f88637fe34bb | -5.3916 | -48.8325 | 2024-10-25 19:25:36 | GOES-16 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d452e9aa-b5f3-33ec-8c04-2b0152b675e2 | -5.4363 | -43.2206 | 2024-10-25 19:25:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8ea26680-36f4-37ba-b066-09dd0444b739 | -5.7298 | -43.9189 | 2024-10-25 19:25:37 | GOES-16 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 30db45a2-4d30-37b2-b545-d6bf3ef21910 | -5.7858 | -41.9179 | 2024-10-25 19:25:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 181.9 |
| f7c52b70-7fb7-3843-9bce-8999c46521ff | -5.8961 | -44.16 | 2024-10-25 19:25:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 794b0362-9e2c-376a-95ab-d71c76f118f6 | -6.0849 | -44.007 | 2024-10-25 19:25:39 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d5df5165-1ca8-3fcd-9f8c-fb0855db5e7e | -6.1361 | -42.6017 | 2024-10-25 19:25:40 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 33b61587-75c4-3996-90eb-0b9142c9c726 | -6.2085 | -48.9973 | 2024-10-25 19:25:40 | GOES-16 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cbce9eea-6517-3842-a3ce-b9f10ae0ddbd | -6.1901 | -48.977 | 2024-10-25 19:25:40 | GOES-16 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 07f5163a-7549-3818-8e24-0180fdd4e6da | -6.2931 | -47.824 | 2024-10-25 19:25:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 323.0 |
| 8359c9a7-ba79-3cbc-9c5c-b762be315a7b | -6.2744 | -47.8253 | 2024-10-25 19:25:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 465d39c2-a9e8-358d-a15b-ae3c5d9bfdee | -6.3286 | -58.3175 | 2024-10-25 19:25:41 | GOES-16 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| dc905dad-2f41-3d14-a130-ce6d45e82e46 | -6.7045 | -43.9554 | 2024-10-25 19:25:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3c9c456b-728b-3d17-809e-87ec7cc525a0 | -6.7096 | -43.4673 | 2024-10-25 19:25:43 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 9cab465b-e078-38b3-841c-d2dd9729785a | -6.9952 | -46.6714 | 2024-10-25 19:25:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f26efe17-6dd7-3d57-b111-9933bfc27d3f | -7.3131 | -44.98 | 2024-10-25 19:25:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 46d929f0-0add-388e-b81d-15163b4e33a4 | -7.1861 | -46.3217 | 2024-10-25 19:25:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7d84b556-e175-342f-842f-e1cee8174a1a | -7.2943 | -44.9817 | 2024-10-25 19:25:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 30cfcca9-f4e5-3246-93c3-dd7e763e012c | -7.1673 | -46.3233 | 2024-10-25 19:25:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6c013e1b-1b98-3438-9907-a9e898772352 | -7.5289 | -45.8434 | 2024-10-25 19:25:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b37533a7-97a7-32d0-aaaf-9c9cb540a607 | -7.5559 | -46.8017 | 2024-10-25 19:25:48 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 134c26df-9afe-3bdb-ac66-cbe13007b26e | -7.5477 | -45.8417 | 2024-10-25 19:25:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 9db71fba-7ebf-3424-ab31-a7f389a16beb | -9.0635 | -48.0051 | 2024-10-25 19:25:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| ea260d1e-8a24-3368-8a87-c3a03ce5b9f0 | -9.0824 | -48.0032 | 2024-10-25 19:25:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| b42a16f1-0262-3ad0-8495-a1015727f0d8 | -9.2024 | -43.3429 | 2024-10-25 19:25:57 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 512c134a-a16c-34ce-8bd5-78ed00a5f4b2 | -9.4699 | -43.215 | 2024-10-25 19:25:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 69.2 |
| b62e806f-7c5d-3524-827f-802995d5cabd | -9.5073 | -47.2319 | 2024-10-25 19:25:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.0 |
| f98c1acc-b844-3c5f-b457-508c0315ed15 | -9.6072 | -42.9371 | 2024-10-25 19:25:59 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 367.8 |
| 9d082c4c-0c50-3b49-bcbe-b27ab778b79d | -10.6249 | -55.9757 | 2024-10-25 19:26:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 166.3 |
| dc050429-fc2e-3f55-8c35-82148d57e7d5 | -10.8793 | -47.9378 | 2024-10-25 19:26:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 67179dc5-6d41-3de7-8381-403ebd334c61 | -11.5357 | -43.9853 | 2024-10-25 19:26:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7858a8fd-c7b2-3a26-9200-8cc070de8320 | -11.9642 | -44.6676 | 2024-10-25 19:26:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 9debb2e8-769e-311d-aa25-af2583be49fd | -12.1179 | -43.6354 | 2024-10-25 19:26:13 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 44b0e67f-47ad-3011-8550-8290a30b1d0b | -12.4612 | -43.7921 | 2024-10-25 19:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 014c065a-7704-3bb5-a59d-38c6bceaaf25 | -19.6028 | -56.8996 | 2024-10-25 19:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.7 |
| d4fc8299-0cf6-3142-9013-76d03c808b28 | -19.6024 | -56.9206 | 2024-10-25 19:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.9 |
| ea51736d-b15f-3468-860a-fd2d49fcda1b | -19.6229 | -56.8968 | 2024-10-25 19:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 140.3 |
| 8d3054ad-9a9f-3822-8312-079b1d11d008 | -19.6225 | -56.9178 | 2024-10-25 19:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 5fe9a8b4-674f-337c-806d-f7f875d62db4 | -1.0733 | -53.658 | 2024-10-25 19:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5ce7ad94-91b8-32cc-b591-a04af5632498 | -1.0368 | -53.5171 | 2024-10-25 19:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5dafe51e-5f9a-3b96-8e30-e67c9d02e483 | -1.1834 | -53.6771 | 2024-10-25 19:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8a090151-18c7-325c-8103-d1c93b2d0ae8 | -1.2762 | -52.9275 | 2024-10-25 19:35:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0f9530eb-a1d8-3646-8616-07d3156f7478 | -1.1834 | -53.6569 | 2024-10-25 19:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| db96e607-6a5f-3f82-8579-1176bbb0e973 | -1.382 | -55.847 | 2024-10-25 19:35:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 966ef536-d06d-30f0-a1f6-f25603649c64 | -1.6214 | -46.0774 | 2024-10-25 19:35:14 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 369237fb-e4f8-34f6-97c7-d9b5b616936d | -1.8811 | -53.5876 | 2024-10-25 19:35:16 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| a1741305-c8e6-3798-bbcc-6f641231f750 | -2.1534 | -54.9256 | 2024-10-25 19:35:17 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d7a01d09-43a0-37f6-9691-440ee1dcaac4 | -2.0232 | -55.7798 | 2024-10-25 19:35:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 5ac6ea15-d053-3aad-b40f-b81ea1a27dbb | -2.3056 | -46.637 | 2024-10-25 19:35:18 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 414f22f6-e072-3d0a-86de-ad06c04b2d34 | -2.3628 | -46.1709 | 2024-10-25 19:35:18 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 03b54dcd-68de-34a8-8848-bc9cc277d6d3 | -2.3892 | -49.3807 | 2024-10-25 19:35:19 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 349f56d0-6dd5-3ac1-a1fa-a9eaa8c8f1f1 | -2.6118 | -49.0985 | 2024-10-25 19:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 900740e4-fc17-3167-9733-f8e735c253bf | -2.6473 | -49.5225 | 2024-10-25 19:35:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2e26446e-0da7-318d-a3a9-693efa4f29e7 | -2.6473 | -49.5013 | 2024-10-25 19:35:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| bfc27945-912b-3a7e-aa1b-22dfa6346c33 | -2.798 | -54.0933 | 2024-10-25 19:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 08bd6cdb-e4dd-38ae-8640-54ee727ba614 | -2.7979 | -54.1134 | 2024-10-25 19:35:21 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8af278b8-4426-3111-af82-506453982126 | -2.9578 | -50.4198 | 2024-10-25 19:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 08370718-0073-357a-be9a-98dd21303755 | -3.1232 | -50.6033 | 2024-10-25 19:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| b7964f73-f81f-3d1c-98ae-640bb0796d10 | -3.1116 | -53.7234 | 2024-10-25 19:35:23 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 2929be6c-2224-30bb-817f-b67b850c3e3a | -3.0834 | -51.3537 | 2024-10-25 19:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 58803850-182a-3af2-a605-c61a710ff30f | -3.1019 | -51.3531 | 2024-10-25 19:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 2ba45009-83c8-33af-b0d0-e5a066ed9168 | -3.2357 | -50.1805 | 2024-10-25 19:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 69ccaf34-1712-3b77-8393-9a3183b783e6 | -3.3045 | -47.1761 | 2024-10-25 19:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 2fab60c6-e89e-374d-9310-024a3302a575 | -3.3044 | -47.198 | 2024-10-25 19:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| b367d3bc-5d58-3b9d-b3dc-15548053f0ec | -3.4767 | -54.4371 | 2024-10-25 19:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9a2e84cd-0883-383e-bb9a-3edd8d4456d5 | -3.4951 | -54.4366 | 2024-10-25 19:35:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 6083c919-b64f-370b-a1ee-735785b467c3 | -3.4653 | -64.9684 | 2024-10-25 19:35:25 | GOES-16 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| d6de9c3f-922b-370f-aca7-a163ec1971cb | -3.6381 | -55.5084 | 2024-10-25 19:35:26 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 70b315b7-eded-3a2d-9aa1-1b50e91b7e2e | -3.9351 | -44.0317 | 2024-10-25 19:35:27 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 98020e5b-3449-3611-b80b-8c730f14e931 | -3.9521 | -44.3061 | 2024-10-25 19:35:27 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f343ef4c-dd3a-3593-a3db-86d4a08ce5a6 | -3.8144 | -48.9729 | 2024-10-25 19:35:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| ec6a05e3-1799-339d-8623-3ebd62830068 | -4.1097 | -43.0021 | 2024-10-25 19:35:28 | GOES-16 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 191.1 |
| fd2d2878-4ae8-3769-874f-4add86f65aed | -4.1116 | -42.7206 | 2024-10-25 19:35:28 | GOES-16 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 9778498c-084d-397c-b70b-4da587787d9c | -4.4844 | -42.8866 | 2024-10-25 19:35:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 9bb4f480-0c10-36ec-addd-b35f312ebfe5 | -4.4655 | -42.9112 | 2024-10-25 19:35:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 8a0dced7-eed3-380f-a9b1-e0e72e7c14cc | -4.4657 | -42.8877 | 2024-10-25 19:35:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ad7a3846-6bcb-3196-921f-2713b24b3c56 | -4.58 | -48.0132 | 2024-10-25 19:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| ce11cf45-bb93-30c7-a57e-2f3b7cbfdafb | -4.5613 | -48.0358 | 2024-10-25 19:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 647ac64c-e47c-3a8a-806d-861f2de6c805 | -4.5614 | -48.0141 | 2024-10-25 19:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 156.1 |
| 5cfcc9ad-87c6-35d5-83d5-5c7823d90d94 | -4.6452 | -46.5646 | 2024-10-25 19:35:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a1d4a3a7-82fd-3058-8053-928fb9c17294 | -4.7336 | -44.5828 | 2024-10-25 19:35:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 8aaccfd5-57e6-31ed-a280-b1a80a191d51 | -4.6638 | -46.5636 | 2024-10-25 19:35:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 44cda4d0-77dd-32f6-b6c7-8688f1692ab0 | -4.6637 | -46.5857 | 2024-10-25 19:35:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3f7810f1-9d2a-39d9-b952-4c7f81f2d814 | -4.9123 | -45.6581 | 2024-10-25 19:35:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| ea907608-4097-3ce8-a30a-0b0ab8cef25f | -5.1211 | -45.1722 | 2024-10-25 19:35:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 728fa5a4-0478-32af-a4f2-ab90e2c3c92b | -5.2424 | -41.7931 | 2024-10-25 19:35:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 377.6 |
| 565d1981-8ec2-39e0-90bd-3b02a907c896 | -5.2838 | -48.3218 | 2024-10-25 19:35:35 | GOES-16 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 8bbd80e9-605c-37d5-8915-bedf94b6cf93 | -5.2102 | -48.2178 | 2024-10-25 19:35:35 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| b7a0811f-95fc-386d-acbc-89b1512f6f15 | -5.1937 | -45.4384 | 2024-10-25 19:35:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9dfe14a3-e452-3b37-b6f8-8238d9c1f473 | -5.2236 | -41.7945 | 2024-10-25 19:35:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| e2e4b3fe-64a7-37e8-885d-d11f5fe0a533 | -5.2426 | -41.7692 | 2024-10-25 19:35:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| de9ad022-dbef-324f-9682-712df091f83b | -5.4228 | -44.812 | 2024-10-25 19:35:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| cc2c6bfd-47fb-3c93-b401-31e9958ab78d | -5.4074 | -49.2169 | 2024-10-25 19:35:36 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 323bcd2a-17e4-39c8-8e6b-c3e75392ae5f | -5.6538 | -44.0399 | 2024-10-25 19:35:37 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 733e8998-fffe-30ad-9f1e-ffbaaba5639d | -5.5815 | -43.7448 | 2024-10-25 19:35:37 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 684f09ef-abc3-3056-b049-6b1480d979ca | -5.801 | -44.328 | 2024-10-25 19:35:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README198.md)
