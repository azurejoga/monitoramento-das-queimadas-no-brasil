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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c6aedc3-4df8-3e43-933c-fab2d72f95d5 | -18.2371 | -56.4389 | 2024-10-14 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 92c056b1-6b35-3128-a97a-17e6efa6c577 | -18.2375 | -56.418 | 2024-10-14 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.8 |
| 7b180811-73a1-32de-b5a7-ca843344d379 | -18.2555 | -56.5196 | 2024-10-14 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 7cb70b99-ea49-35d6-828a-a7e7d4b325ff | -18.2559 | -56.4988 | 2024-10-14 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 1fe1ca85-b916-3e6d-a0ba-26cd3477360b | -18.2562 | -56.478 | 2024-10-14 01:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| 813bf5c6-1473-32ed-9766-988ebaad49e6 | -21.7593 | -48.3086 | 2024-10-14 01:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 179.5 |
| e91cf999-822f-3e8f-a561-b4010db0ca84 | -21.76 | -48.2851 | 2024-10-14 01:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 246.8 |
| a641b63f-b796-387b-ada5-91065bad56fb | -22.294 | -49.1109 | 2024-10-14 01:27:09 | GOES-16 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 27978258-2265-3c33-a39a-3943ebd53071 | -2.4344 | -46.9195 | 2024-10-14 01:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 3869ed82-c331-36ab-ae92-fbaa9bcdb2be | -2.4529 | -46.919 | 2024-10-14 01:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 94eade53-b0bf-3c2e-bab8-ef396e7ae581 | -2.6303 | -49.098 | 2024-10-14 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 52781478-f5df-35e8-9b54-f052222eccd0 | -2.6117 | -49.1198 | 2024-10-14 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 2e6a9a3f-2ee5-37a5-bd3e-5e47320d9efc | -2.6118 | -49.0985 | 2024-10-14 01:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| b3dc972d-c4ee-3efb-a030-09eb70c0eb30 | -3.0656 | -51.1883 | 2024-10-14 01:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 4a03fb00-d9b8-36fc-a61c-42b6cafbb8af | -3.084 | -51.1878 | 2024-10-14 01:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0007f795-b679-33d6-a856-19cf40d8d2ee | -3.2889 | -42.8561 | 2024-10-14 01:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 78a41287-5d20-3a75-900d-ce871ec599a0 | -3.289 | -42.8327 | 2024-10-14 01:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 1f0f00bb-2647-3e9f-a2b6-d034be1df14d | -3.3076 | -42.8553 | 2024-10-14 01:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 05848c52-9df7-3725-9b34-30a542a24d40 | -3.3077 | -42.8318 | 2024-10-14 01:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 176.9 |
| f9710b48-7175-35f2-a1b7-0b17ff0e9607 | -4.3718 | -37.9175 | 2024-10-14 01:35:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 62d4d42c-b95e-36fb-9116-780bf30cc944 | -4.372 | -37.8918 | 2024-10-14 01:35:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 62.9 |
| 341fc503-8931-3626-9ba0-ac470ab31af5 | -4.3428 | -50.5172 | 2024-10-14 01:35:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e7d0a2be-e80c-38ad-8a07-986a3252c423 | -4.3565 | -55.1291 | 2024-10-14 01:35:31 | GOES-16 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| a348c266-b459-31f4-a75c-16de9d1be55a | -7.9604 | -63.6171 | 2024-10-14 01:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 97b14394-da18-3e71-b816-d5faddec1b3c | -7.9625 | -49.0607 | 2024-10-14 01:35:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 38483bf2-6ec9-3d5c-8ea7-d54ef13107a4 | -7.9418 | -63.6365 | 2024-10-14 01:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 03c93fc8-8c86-37ae-8a3d-a8a663ca4d31 | -7.9419 | -63.6177 | 2024-10-14 01:35:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d86dae92-2523-3348-ba58-0cc1c2f53559 | -7.9603 | -63.6359 | 2024-10-14 01:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 00f94b77-05e2-34b6-9797-79b0eda3f8b2 | -9.1043 | -61.162 | 2024-10-14 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b8a86942-d8fd-3a01-863d-014fa124a14b | -9.1042 | -61.1811 | 2024-10-14 01:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 870110ae-78f1-36e7-afb4-408b0053d8f1 | -10.0622 | -44.2391 | 2024-10-14 01:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| cb001c02-acc6-3eab-8580-1807e78bcea6 | -10.0626 | -44.2158 | 2024-10-14 01:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a817bac4-bf8e-36af-83a6-eeed43ab07ef | -10.0166 | -47.3085 | 2024-10-14 01:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| e940d9e8-c146-3fd0-9b6e-464b3827aeaa | -10.0352 | -47.3286 | 2024-10-14 01:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6019b366-73e6-3678-895e-f761505c3655 | -10.0813 | -44.2366 | 2024-10-14 01:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 9c9f2746-48ba-3134-9a14-8956e14ce564 | -10.0816 | -44.2133 | 2024-10-14 01:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 0074bdf1-3d8c-3e59-87f0-19f2be541082 | -10.0163 | -47.3308 | 2024-10-14 01:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 160.9 |
| 51c50b7e-9c7b-3170-9229-fe0abe5e0a0f | -10.4504 | -44.9516 | 2024-10-14 01:36:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 05eb26ab-1f95-3936-81ea-2b983bb08408 | -10.4918 | -42.433 | 2024-10-14 01:36:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| ac25b38d-ba91-3820-bab2-409b395d2b4a | -10.5307 | -49.7843 | 2024-10-14 01:36:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7aa8d39f-5c8a-3043-bba4-230341e07b01 | -11.17 | -39.9192 | 2024-10-14 01:36:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 119.8 |
| 1d70bd9b-d7b4-320d-901b-252ce0a2d4bc | -11.1705 | -39.894 | 2024-10-14 01:36:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 4b7dc05f-c171-3f81-901b-3ac13632702e | -11.1893 | -39.9159 | 2024-10-14 01:36:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 889fa77a-38a5-3183-948c-4966bd162e10 | -11.1898 | -39.8906 | 2024-10-14 01:36:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 8df09ed0-1390-3e78-b954-18b8762b6e37 | -12.3804 | -53.1376 | 2024-10-14 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 29cc7f8c-6d75-371b-bac1-a595eb7144e0 | -12.3807 | -53.1167 | 2024-10-14 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| ee4055c5-919c-30cb-aebd-0260bf03f16d | -12.3994 | -53.1355 | 2024-10-14 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 0554e88d-920b-38a4-a6de-9ac707aa3f98 | -12.3997 | -53.1147 | 2024-10-14 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 0ffd2f4f-2ae0-3d78-9d7d-797181e98493 | -12.4981 | -63.0148 | 2024-10-14 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| c6237a78-6605-3a1b-833a-b6960cb3bfe0 | -12.4983 | -62.9956 | 2024-10-14 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d54fdbb4-cb38-3973-a6e2-8d96eb217ca6 | -12.517 | -63.0137 | 2024-10-14 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| fc35aee3-37e3-3195-9a80-3cd6f9f7e852 | -13.6245 | -50.6175 | 2024-10-14 01:36:23 | GOES-16 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 84baa824-6bc2-3f50-a68b-5e8330877da4 | -17.6471 | -56.3084 | 2024-10-14 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 81c21a04-25fc-3584-9c4e-0d60846c554c | -17.6474 | -56.2876 | 2024-10-14 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.1 |
| f95ad356-3f93-320c-bcdf-1bed54efe1cf | -17.6876 | -56.2409 | 2024-10-14 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.1 |
| 390b20eb-501b-35d6-9d14-4437c9fa05ed | -17.7264 | -56.2774 | 2024-10-14 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.4 |
| bef69587-56d2-34c1-8b3c-f73741c953ce | -18.1902 | -56.8601 | 2024-10-14 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 7d9251a6-c7a7-3c0f-abf5-66a564c1b544 | -18.1905 | -56.8394 | 2024-10-14 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 7889dc19-2490-37de-9acd-6be779008a17 | -21.7593 | -48.3086 | 2024-10-14 01:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 119.7 |
| fe1bf752-88a9-3972-b238-948eeb0cb45d | -21.76 | -48.2851 | 2024-10-14 01:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 135.8 |
| 6b033abe-e3af-31e4-a4eb-e3d97e4710cc | -21.7801 | -48.3036 | 2024-10-14 01:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 100.5 |
| a9f39134-b9e5-3299-bb0f-381fd9208d66 | -21.7808 | -48.2801 | 2024-10-14 01:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 116.1 |
| d0df1845-273e-3bd6-ae31-ac4652ab6faa | -2.4344 | -46.9195 | 2024-10-14 01:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c0447049-557b-399e-8ac2-d2571919e1ad | -2.4529 | -46.919 | 2024-10-14 01:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 020e1642-63f0-393e-bbfd-944913237ac7 | -2.6303 | -49.098 | 2024-10-14 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 457c6c00-444d-3d50-b000-7182f999918d | -2.6117 | -49.1198 | 2024-10-14 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| f4e251b6-1fe8-3699-baab-dc0ea58adf9b | -2.6118 | -49.0985 | 2024-10-14 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| f7aa924b-ef11-3073-90cd-ac50854ec4a5 | -3.0656 | -51.1883 | 2024-10-14 01:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| c7e486c0-4d5e-374e-a928-cd4f7f2223ba | -3.084 | -51.1878 | 2024-10-14 01:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 95786152-151d-3dfe-8cf7-b06c792cc232 | -3.2889 | -42.8561 | 2024-10-14 01:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ed38cc5f-395c-3045-af31-cedab36cf03c | -3.289 | -42.8327 | 2024-10-14 01:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 78f4cdfd-3616-3fda-b6cf-4b04eda3d70f | -3.3076 | -42.8553 | 2024-10-14 01:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 69745dc8-0f6e-34e2-b16a-096a8bc261d5 | -3.3077 | -42.8318 | 2024-10-14 01:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 19e6bc2d-6342-328f-9645-0c53ff83ff69 | -4.3428 | -50.5172 | 2024-10-14 01:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| e20bc9ad-d622-3976-b5bb-cfc21ad2e8fb | -4.3718 | -37.9175 | 2024-10-14 01:45:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 3d921af5-0409-382e-baac-5074dc9143a2 | -4.372 | -37.8918 | 2024-10-14 01:45:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 70.4 |
| b70747a1-9f9a-3453-84c2-e09c03515b3d | -7.9625 | -49.0607 | 2024-10-14 01:45:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 98.4 |
| e886358c-4b9f-31d1-9917-a04444643f10 | -7.9418 | -63.6365 | 2024-10-14 01:45:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| d8dda9d4-e89a-3d8d-9d7b-f38fa3a9dec5 | -7.9603 | -63.6359 | 2024-10-14 01:45:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 211a9840-9d66-3a49-9c04-b6517feccf8b | -9.1021 | -47.9355 | 2024-10-14 01:45:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 13e6a55d-a96f-3b88-9fea-fc85dfb5cc35 | -9.1043 | -61.162 | 2024-10-14 01:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 3f6233ec-5cd3-30e3-ad22-45608976299c | -9.7983 | -36.1484 | 2024-10-14 01:46:01 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| 264961dc-ffa3-3f44-aeca-4c6012a45db0 | -10.0163 | -47.3308 | 2024-10-14 01:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 3c8a5f61-2090-364c-b994-91680ced650a | -10.0166 | -47.3085 | 2024-10-14 01:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| aeaf1f47-efb6-35fa-9400-90f86d0d43a8 | -10.0352 | -47.3286 | 2024-10-14 01:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 94c512f4-ca8e-3316-a0b4-31183515ba85 | -10.0622 | -44.2391 | 2024-10-14 01:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 649fac99-7891-3c44-952d-e89d295c6d5e | -10.0626 | -44.2158 | 2024-10-14 01:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 9413c953-d1f1-3641-aad8-e3a66c3557c7 | -10.0813 | -44.2366 | 2024-10-14 01:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 170.2 |
| eb76739b-68e2-33e6-9f5f-f36ad314bf51 | -10.0816 | -44.2133 | 2024-10-14 01:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| dfff042a-1e8e-30bf-a7a6-72a42830c810 | -10.4504 | -44.9516 | 2024-10-14 01:46:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.7 |
| eebedb09-818b-31ee-8ef2-badcd2852602 | -10.4508 | -44.9285 | 2024-10-14 01:46:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| bd925296-234d-3836-ad9c-9e1007f9e6f3 | -10.4918 | -42.433 | 2024-10-14 01:46:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 5c31ee0d-b04e-3463-bfec-924778dc98ae | -10.5118 | -49.7863 | 2024-10-14 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9c43b5e3-0fda-3922-aca1-b385add84293 | -10.5307 | -49.7843 | 2024-10-14 01:46:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| b69777fc-0d39-3821-99c8-e618fc60048e | -11.17 | -39.9192 | 2024-10-14 01:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 83a6b0a0-d53d-3425-8f92-ffa981206222 | -11.1705 | -39.894 | 2024-10-14 01:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 120.0 |
| c4bded23-fbd0-351d-8f09-1f13f57ec738 | -11.1893 | -39.9159 | 2024-10-14 01:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 572ca380-484a-38cc-98e6-30101f76b964 | -11.1898 | -39.8906 | 2024-10-14 01:46:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 6d453e3f-1086-3db7-bf0f-0303c566385c | -12.3283 | -50.2449 | 2024-10-14 01:46:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 6f0f6320-03bc-3d42-85af-459a5808d1b5 | -12.3994 | -53.1355 | 2024-10-14 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |


[Clique aqui para ver as próximas entradas](README25.md)
