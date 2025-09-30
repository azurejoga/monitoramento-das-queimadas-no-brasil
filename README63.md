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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| febbc721-81d2-3d9d-bb9b-f9a8052a2e84 | -9.05807 | -47.62606 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 763ad330-d636-3788-ba31-beb6db2e62fa | -13.57387 | -48.06161 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40dc7a18-2ad4-3d0a-84a7-e8ec1071fc3d | -8.69643 | -44.8184 | 2025-09-30 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cf15cc9-1368-3847-8a67-443a1fba1bc3 | -13.66061 | -44.31051 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 262d5d94-e4c1-3c07-b5ea-1a1f38fb5e8c | -11.15136 | -54.12789 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 4ed372fc-b292-3b2b-9f0c-2efdd900f1c0 | -13.84207 | -47.48751 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b8708817-9f74-33ff-ad67-135114fe0f1c | -11.22058 | -47.21492 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9d54e1d-9781-3ee2-b7f6-5baa0c75b2fe | -13.61801 | -48.035 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290ee562-a3aa-3fbb-8a85-859c89be923f | -11.31478 | -47.78107 | 2025-09-30 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5188ae0c-45a3-36af-a05d-73397f73b96a | -7.42711 | -45.23788 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4aa8d24-645d-3644-8c3b-de3ae283cfbd | -8.32204 | -50.88224 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d2e3ff9-8154-3b05-bb6a-e97375f10a6b | -7.72107 | -44.94856 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ddb7f47-e727-3678-898e-9c21945e7a57 | -10.12308 | -45.32252 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd9f3449-8e3e-3afd-9961-cc686e3f40f9 | -12.96765 | -46.41418 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0515d5c-df5d-383a-a47e-eeb623327ed9 | -13.62732 | -42.53266 | 2025-09-30 04:40:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f94bd276-95d8-3969-ae9f-42b69a92a7e8 | -11.90692 | -48.06216 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ce3fd0-b554-370e-b8e9-125385447e3f | -11.45316 | -45.05416 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1eb8b396-d76f-3865-aeae-1ae743e54c1c | -13.1325 | -44.61494 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98d8ede9-0294-3028-b27c-f92717e4abc7 | -9.746 | -47.78965 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7e8c642-bcaa-3739-867e-07d4db07a087 | -13.71775 | -48.6407 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ee8ef5e7-55b0-3865-b92e-165d4bb856bc | -9.06181 | -46.70961 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ec3b2fa-57b0-34f4-87ac-297fdf1a9ee3 | -11.36056 | -49.37378 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4414a49-ebae-391a-bd15-c3830be9e156 | -13.23579 | -48.44578 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13a14f26-b6f7-37d0-b32c-c04369ae484b | -10.63008 | -53.69363 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 69fd8f39-48d5-3513-8303-6fafb20a4014 | -7.51235 | -44.28586 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5131dd5-0e8a-3e02-ba52-7602056809a2 | -7.36919 | -47.05062 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e2e6a43-1874-3d5f-bb39-a0a446273be9 | -10.07632 | -45.63486 | 2025-09-30 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44ee57fd-ea83-344f-a0a1-1b8e36ba23b3 | -10.81155 | -45.35955 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 743dd077-326a-3965-8333-26aae4713f9e | -8.87734 | -46.61458 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a38ee9a9-63a7-31c5-869a-256cb1907fab | -7.83081 | -46.99303 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 223139ac-71fa-32b5-961e-648048fc08f9 | -11.03099 | -49.81456 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 546362c2-341c-3fdb-9e86-28a25ad94a37 | -7.66587 | -47.42036 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9683ce9-adf6-39bb-8425-04c8eaa25116 | -7.37004 | -47.05013 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b9d48c2-b48d-38e1-9567-dcb80cceb91d | -8.54788 | -44.66423 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58f2a378-58aa-3de6-b6d8-088ad43e4b4d | -13.30308 | -48.70101 | 2025-09-30 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d462f069-e248-35e1-9d8a-ce18fee8539f | -8.09246 | -48.00901 | 2025-09-30 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65ee6bde-7c55-3d19-808c-a5ee87072fde | -8.53173 | -50.15945 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05b2f6de-15ec-3437-a86f-dcd155c1628b | -13.65816 | -44.40051 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f618598a-7da5-32e3-8d4d-ce1258c4950a | -8.17086 | -55.16793 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ba9ce4d-52f3-3204-929c-3cc62a4e7d06 | -7.76547 | -45.76437 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f67d3dc5-3d71-37d3-81c8-7b89b8ebc2c6 | -11.14845 | -54.12202 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7ee21ad4-c1ac-3d04-bd30-5d48a10a12d5 | -9.06601 | -46.732 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5ba47e8a-8a72-31eb-bcd6-038fd8154bfc | -8.67491 | -47.70952 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 558f9064-aac8-3c9f-bdcb-e61354dc51bb | -12.8755 | -46.95824 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1e02940-3bfe-38f0-b172-4ea23d9ea9e5 | -10.39875 | -47.80722 | 2025-09-30 04:40:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1254026-2200-3d9e-97ee-8fa9705e89ea | -12.85144 | -46.99271 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 92fc76a9-b863-3869-9b88-88c3ad038567 | -8.96558 | -47.44413 | 2025-09-30 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1def064e-4868-3da6-a850-e3ee0eadce1b | -10.40114 | -49.04453 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1aabebd-db2e-364b-b60a-bc6007caf23e | -8.86311 | -46.68681 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae257f7e-e398-38db-a30e-92048c14b7e6 | -13.21822 | -50.93391 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e9f5660d-5e31-3a23-8f99-fdfcde5cdb5d | -12.02255 | -46.61739 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb941268-a394-308d-b111-8778d368780a | -12.94668 | -46.75693 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e640bb5b-5603-3559-ad04-2e10275e59a9 | -12.84131 | -47.01027 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 743e4b94-db62-37de-b4b9-ad9098afa25f | -9.33085 | -49.83199 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a5d142e-25dc-3da1-834c-3fa2562c110c | -11.19442 | -47.24156 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1f35ad72-71ac-35b5-a6a8-bb8efac3f781 | -13.02774 | -42.80785 | 2025-09-30 04:40:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 73dd2c46-b54c-394d-9c28-ec933dde42a3 | -7.36628 | -47.04615 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b02fa56-193e-3bb7-afb2-c875d9c8c71c | -9.85519 | -49.16927 | 2025-09-30 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 286ccf69-aeb8-32e2-b240-9e7a0a8c84a3 | -13.24344 | -48.44255 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eb38065-0562-37d8-af4a-ec4f28cae783 | -11.35441 | -45.06284 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72fd69bc-f5c8-3bb0-b40b-4232a9e1431b | -7.85489 | -46.7545 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1bb9962-5146-3bd6-8dd4-41c0a6306b3e | -8.89075 | -45.03364 | 2025-09-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b1304ce-90cb-3a17-afc2-9f60323a22c9 | -8.71437 | -47.9794 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f74b3eb2-f2ed-367d-90b8-a540dcdb00bb | -9.12723 | -47.64059 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6056843d-2d8c-360a-adf4-3d320a18bad1 | -7.75999 | -46.64917 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97f73d95-f8dd-3093-badf-53057b294072 | -8.28203 | -45.37119 | 2025-09-30 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37bf656d-b2f1-374d-9ae5-2b8d38bef294 | -10.3974 | -48.13826 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08ddbafb-744c-391d-b7f6-62cf429ed863 | -13.523 | -49.47826 | 2025-09-30 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ed7bdc4-f9dd-34ea-8f0c-96aebb216e4e | -9.75539 | -47.75103 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b292df-489f-34fc-8d86-3273541bf2c4 | -13.77074 | -48.32658 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33261535-4aff-3c29-b775-5c849a414e91 | -9.58216 | -40.34999 | 2025-09-30 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bd8344ec-f747-34e5-9c6f-c17bf8776c2e | -10.09259 | -46.07737 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be5992b9-928c-3085-90a8-55c1a6509e59 | -11.70744 | -44.32736 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 348357f9-7a1e-3862-ae62-b06fea538e75 | -10.66825 | -53.7089 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 827a742b-08db-3e02-ae2e-7022d7d46e11 | -13.35525 | -47.84319 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1934b827-1007-3d8b-b1ec-937452661296 | -15.00134 | -42.42359 | 2025-09-30 04:40:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15831510-600a-3cb5-84ee-5a7d3bbfe715 | -12.8944 | -46.76889 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c47fcdd-d166-38c1-95c8-a5499a834deb | -13.78625 | -47.85968 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94eccadf-2526-33e8-aa4b-8f3709c0f6e5 | -9.50735 | -48.53153 | 2025-09-30 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77514097-cff8-3fec-9f90-beda2e514f26 | -10.11607 | -47.78998 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84d046b9-bdb8-37dd-8d83-45095027b9aa | -10.18987 | -44.8947 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 650c9e33-f59d-3367-844b-41dd54eb9d4f | -11.24932 | -47.22659 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87db92cb-b9bc-3361-b62b-4e1daebfc604 | -12.80007 | -46.88888 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6772344-eac3-36a1-ae3c-e3dc0ee5e43a | -13.36641 | -47.31493 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abdb8dff-7513-31d9-a99e-3e10d041b72e | -10.63891 | -48.56508 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 189fc89c-ecda-30c5-a578-1d16e5a3e3a4 | -7.47871 | -47.26632 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e779d545-de8b-3e6f-ae38-9f27728eac7f | -12.69864 | -45.29535 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c3a133e-229a-341f-93d9-c1e2ada62a3c | -9.30297 | -54.50946 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18e7addc-b571-3c3e-9585-1491132ffe02 | -10.64964 | -48.5399 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35853de8-5a58-3cf2-962c-ddfb696e0e4e | -12.69917 | -45.29147 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f19e651c-c2d9-3e02-91ce-7ea266dff74e | -11.16671 | -54.12519 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b5862004-cee9-3501-b368-14d07ccb5bbd | -13.60313 | -47.28031 | 2025-09-30 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84d7fc22-f3df-3d28-931f-fe0ddaa852d0 | -7.30253 | -47.30058 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6219a0e-60ce-3210-b52f-47c5a2d2782d | -8.65058 | -46.60563 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b0f958a-1cc3-343f-ad5c-7276a332e003 | -11.628 | -52.84651 | 2025-09-30 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93a765c3-c117-3cb5-ba8d-259cab2de24d | -11.26024 | -47.22822 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64ad7b77-33d9-30c5-81b2-2ad010e45f37 | -7.56758 | -42.40508 | 2025-09-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4f5a850d-267d-3994-969b-15d5c4d67fd3 | -11.43763 | -43.50364 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9c3a432-0074-37d0-8650-8492d5238fcb | -13.81493 | -47.49267 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1060bf93-8336-3dc3-bdb3-120c00e24761 | -13.74417 | -47.9124 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README64.md)
