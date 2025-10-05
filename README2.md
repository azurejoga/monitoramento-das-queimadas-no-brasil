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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e25ec6f-e028-3ee3-a195-ff30bfc54870 | -6.1723 | -44.666 | 2025-10-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 05b2b200-1b2e-3513-b0ea-fab0b84851cc | -14.3353 | -47.6755 | 2025-10-05 00:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3bb386ed-3ce0-324b-9f93-6658fbe22965 | -6.3946 | -43.0505 | 2025-10-05 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| e7859992-0060-3f25-9d7f-d1de8193c79f | -10.8379 | -57.1781 | 2025-10-05 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| ac8f4b7a-f2ab-3531-af2a-bc6c0b9288d9 | -6.3943 | -43.074 | 2025-10-05 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 87881bcc-df73-3ff1-9b7d-2623ed9f5d94 | -11.7519 | -44.7461 | 2025-10-05 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 23d85feb-a25c-3db1-a25f-86a3debb32ce | -5.6361 | -43.9258 | 2025-10-05 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| cb93501d-685a-34a9-9cff-74e4eb8dc2bc | -11.4535 | -51.5177 | 2025-10-05 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 7a5e5bb8-e834-33f0-9d83-92221f477bd1 | -6.1536 | -44.6675 | 2025-10-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 389.4 |
| 480ada30-32f8-348e-84d9-6f7b4d161da2 | -6.1351 | -44.6461 | 2025-10-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f629aa96-3403-3c39-bf96-31810fab0409 | -5.6363 | -43.9027 | 2025-10-05 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 4f68840d-a29f-3591-9297-5f95227c5237 | -6.154 | -44.6217 | 2025-10-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a8864540-4362-3d3a-8c15-d950f65169fa | -6.4396 | -44.1627 | 2025-10-05 00:10:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| d0da6b1b-d7f9-3d53-8c23-4cd2c1a01bbe | -12.573 | -48.1615 | 2025-10-05 00:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 89b79785-4054-316c-96cf-ff257a5828c6 | -6.1349 | -44.6689 | 2025-10-05 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 132.6 |
| d481407a-98b7-3b43-bdc7-4d570cae75c2 | -8.4354 | -70.1117 | 2025-10-05 00:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f0da4183-ce7a-3e7e-a5e0-b7e1549866e7 | -13.1585 | -50.9359 | 2025-10-05 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 57961e51-6838-3bcc-af0e-982d8918021c | -13.1582 | -50.9574 | 2025-10-05 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 20f78fb7-62b9-319c-bedf-f04d1108199c | -14.9157 | -46.8541 | 2025-10-05 00:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 30c6c3c7-fb32-3a17-8a60-55be2ab22fc0 | -5.6319 | -44.4092 | 2025-10-05 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 885edc9c-787b-3dc4-b228-6f1175425ced | -7.7885 | -44.5228 | 2025-10-05 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5fa4b29b-2801-3840-ac79-ddfca19cbddc | -11.8588 | -56.8785 | 2025-10-05 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 34e28936-a225-316e-af2f-2eb82c0742ab | -15.928 | -48.822 | 2025-10-05 00:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a84f22f8-3ae6-38d1-9f5e-48e991aa1bb3 | -2.6883 | -48.3899 | 2025-10-05 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 944ad07e-49f6-39dd-9e9b-170015b57265 | -4.6317 | -43.205 | 2025-10-05 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 24b59298-1fa4-3ec7-8ef5-c01e5b3997da | -13.3036 | -48.1021 | 2025-10-05 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.0 |
| a3c17279-9874-3c90-bb05-8cbf4b112998 | -5.6548 | -43.9244 | 2025-10-05 00:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 8fcf3f73-02bf-3dc2-be8f-c005ce9446e5 | -13.304 | -48.0798 | 2025-10-05 00:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 2e9e2aa7-871d-3492-b72d-96e288549993 | -8.624 | -63.9888 | 2025-10-05 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 1160460b-40d6-33ec-b4e0-30e3846a9d0d | -12.4669 | -45.5155 | 2025-10-05 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 186.9 |
| a150eede-381a-3131-90d2-614b6cdd6ec8 | -10.6052 | -54.3584 | 2025-10-05 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 531306fc-4278-36d3-b2dc-3c3d7170b846 | -13.1393 | -50.9383 | 2025-10-05 00:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 214.2 |
| 9804fc26-984f-3a4f-bebf-7085d0dac478 | -4.6318 | -43.1816 | 2025-10-05 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 83296985-1fd4-3edb-afbb-064bc6602607 | -6.4398 | -44.1396 | 2025-10-05 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| ea86bc7e-b55e-3062-a940-8ba3b3e9b96d | -11.8777 | -56.8769 | 2025-10-05 00:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 67021205-9322-321f-a5c5-19023c4a6c24 | -5.655 | -43.9013 | 2025-10-05 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 90ed43cb-8716-3563-8d34-192579eed117 | -8.4196 | -46.8108 | 2025-10-05 00:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5cc02046-7d5c-3324-98e5-9b8f3be98c32 | -4.6504 | -43.2038 | 2025-10-05 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 156.2 |
| 7095b023-0e70-3ece-bd87-d4843e32e7fb | -15.9084 | -48.8254 | 2025-10-05 00:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 689d0e68-7f80-3c92-a5c3-2ef684396b60 | -4.4446 | -43.2164 | 2025-10-05 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ea72a1b4-8ed7-3531-9b21-b3569ecd7934 | -11.7524 | -44.7228 | 2025-10-05 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 47ea64d1-81a1-30ba-b022-a7bff45140f8 | -8.6426 | -63.9881 | 2025-10-05 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 24323335-5fd2-3a17-b91f-574c4c74754b | -4.3197 | -48.0908 | 2025-10-05 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 55364e70-64c8-3ff7-aaad-f5cb93c4a6b0 | -5.9226 | -43.3236 | 2025-10-05 00:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 0eb839c2-f289-36e7-809a-70cedb8c188e | -5.4775 | -42.7956 | 2025-10-05 00:10:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 42.2 |
| fd96e404-ec3c-3273-8c04-a9e5832a6210 | -4.6504 | -43.2038 | 2025-10-05 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 1eb62c9d-a3bf-313e-95b5-f657ecf239ab | -13.1393 | -50.9383 | 2025-10-05 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c306c53c-f6ff-30de-878d-795c342e330b | -12.5922 | -48.1588 | 2025-10-05 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 5f6bfde1-474c-3433-818f-57690f7605e6 | -19.503 | -50.377 | 2025-10-05 00:20:00 | GOES-19 | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e7e493b3-6dcc-3316-8d78-ca8f7157f0d1 | -13.1161 | -43.847 | 2025-10-05 00:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cf565d65-416f-3c47-8001-947bc72f673a | -12.573 | -48.1615 | 2025-10-05 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| e7b97eaf-26b5-3fc1-81f1-a6c484f640da | -8.4354 | -70.1117 | 2025-10-05 00:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 9b5e4d3e-0761-37d8-8630-9eafb2e92daf | -11.8777 | -56.8769 | 2025-10-05 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| cb6b94c0-c2f2-367d-abbe-4758cde80498 | -10.6052 | -54.3584 | 2025-10-05 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4744da7c-df02-387a-9bc1-d80a6b9d66b9 | -2.3012 | -47.9906 | 2025-10-05 00:20:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| be16c7b9-f360-328b-bb33-8f38770c3ce6 | -4.3197 | -48.0908 | 2025-10-05 00:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8d221a1c-597c-3b77-a2bb-767041251efc | -15.9084 | -48.8254 | 2025-10-05 00:20:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| ea18335b-770b-315b-ab56-b5037084e05e | -8.4353 | -70.13 | 2025-10-05 00:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 59872ef1-2260-3e9e-b439-22c223233d42 | -14.3348 | -47.6981 | 2025-10-05 00:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4463254c-8eee-3ce4-b47f-4728bb401ce3 | -13.1585 | -50.9359 | 2025-10-05 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 356f9288-467c-3971-bbfe-3abcf2b32530 | -13.139 | -50.9598 | 2025-10-05 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0ea29839-8151-3aa9-b5d4-4fe1c7f790aa | -6.4134 | -43.0489 | 2025-10-05 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 196.5 |
| b6fd6693-b605-394b-8b61-057f9edba1ff | -10.5863 | -54.36 | 2025-10-05 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 6b0aa4c9-77c8-397b-bbab-d5f80b41d192 | -12.4476 | -45.5185 | 2025-10-05 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 42d95a56-3528-33da-a585-bff471c8813a | -6.9181 | -45.0606 | 2025-10-05 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| b4897bcb-141b-3b8d-be0b-c4084637b926 | -12.4669 | -45.5155 | 2025-10-05 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.6 |
| c39ba0fd-d63e-3b80-9256-d6088ada34b9 | -14.3353 | -47.6755 | 2025-10-05 00:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c59d042e-50b0-3e30-bd33-ed30386a5e1a | -5.9226 | -43.3236 | 2025-10-05 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 5d3a7399-438a-3180-93a9-4b3c8b9651ac | -14.6906 | -48.335 | 2025-10-05 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 87667d9e-ab3e-3cdb-8b54-d3cc66dcc258 | -6.3946 | -43.0505 | 2025-10-05 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 33e3b4dd-98fb-3d64-bd00-1655b8ab286d | -15.928 | -48.822 | 2025-10-05 00:20:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7b436565-9e93-303c-9126-94313b126ce8 | -15.3597 | -47.9779 | 2025-10-05 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 362a19f8-6a8e-3ea9-af7b-dc99795f76ed | -13.1582 | -50.9574 | 2025-10-05 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0a5d0964-0ff4-3ca6-90ff-c6c31d3b50f0 | -6.4584 | -44.1611 | 2025-10-05 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 7531ad98-af7e-331b-a545-29e19046a608 | -11.8588 | -56.8785 | 2025-10-05 00:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| dcfbaa84-7414-3284-b885-600ff898739d | -4.4445 | -43.2397 | 2025-10-05 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 74b9822e-d0d5-37a2-9728-b19358a2c384 | -12.4673 | -45.4925 | 2025-10-05 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| b09eb9b0-708c-3996-8dbd-ebfdd93606d0 | -6.4398 | -44.1396 | 2025-10-05 00:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e798a06d-900c-3d3a-9db6-189080c35dd1 | -6.4131 | -43.0724 | 2025-10-05 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 87ef11f0-b97c-36e3-bd97-0c998b5ea153 | -6.3943 | -43.074 | 2025-10-05 00:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 0cc2949f-6612-3657-ab87-e7b4692e65fb | -3.8041 | -51.0812 | 2025-10-05 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| a476fdd5-74c4-3ba1-a128-93a339c26ee8 | -5.6548 | -43.9244 | 2025-10-05 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1934667a-f04b-311c-98e5-c88cde9c4016 | -14.6711 | -48.3381 | 2025-10-05 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 5248e85b-2fda-3344-b0c0-73bc44e7221a | -8.4169 | -70.1303 | 2025-10-05 00:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 940811e0-c61a-35f1-993e-9b869ee032b5 | -5.6361 | -43.9258 | 2025-10-05 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 314ab918-e63b-3111-92b3-a934e927128c | -12.4665 | -45.5386 | 2025-10-05 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f400f07c-6ae5-34db-b855-11fc74654592 | -11.8225 | -45.0827 | 2025-10-05 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 32244912-64a2-39a2-ac89-ef9d8fde1e25 | -11.823 | -45.0596 | 2025-10-05 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 85c32c57-54b9-3835-8769-3c63d2775088 | -11.7519 | -44.7461 | 2025-10-05 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d115d063-8667-3eb7-8d89-0513548a475f | -4.6505 | -43.1805 | 2025-10-05 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 319.2 |
| dc2a52ca-90a4-3ff6-ad7e-0448a6b68006 | -12.5538 | -48.1641 | 2025-10-05 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 3febd3e3-1290-3c80-8c23-b06ce27baff0 | -2.6883 | -48.3899 | 2025-10-05 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 133a9fb8-2f25-3cdc-a18c-0773fd3aedf0 | -5.6363 | -43.9027 | 2025-10-05 00:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 557be51b-49e7-3ee2-8c6e-14ba1a5b0b51 | -7.321 | -45.9743 | 2025-10-05 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 2be40901-28d4-3a7d-9f8d-acb907c9a0da | -11.7712 | -44.7432 | 2025-10-05 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| bd818814-49bf-3640-9ac5-8700dc88db39 | -6.4396 | -44.1627 | 2025-10-05 00:20:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 85e31646-0125-3b60-b5ed-aa06b2ca34c7 | -14.3158 | -47.6787 | 2025-10-05 00:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 60.9 |
| c989ef72-b6f5-3fc3-ab59-6909fffbd9ba | -4.6317 | -43.205 | 2025-10-05 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9f2689bc-acbe-3283-a327-f15b3e4d0cc6 | -8.5387 | -46.3079 | 2025-10-05 00:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| f3dfc358-21d4-30d5-a0b3-0bf0c4f7b116 | -4.6507 | -43.1571 | 2025-10-05 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |


[Clique aqui para ver as próximas entradas](README3.md)
