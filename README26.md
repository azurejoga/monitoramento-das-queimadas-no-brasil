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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e51ec1c-1189-3abc-a0c8-284969788623 | -11.1893 | -39.9159 | 2024-10-14 02:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| b4f7eacb-83a7-3f3c-9204-327cb7c2f477 | -11.1898 | -39.8906 | 2024-10-14 02:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 167c15bd-3791-34b0-9f4a-cf2dd19204a7 | -11.2287 | -51.3303 | 2024-10-14 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| bd735dd3-aa8e-3ea5-871c-db31e284fb39 | -12.4 | -53.0938 | 2024-10-14 02:06:17 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a7026b31-3795-31c2-97b6-58ba0dfcd0bc | -12.3997 | -53.1147 | 2024-10-14 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 239.9 |
| 8e569c01-6462-3a85-bf0e-3dade43afa09 | -12.3994 | -53.1355 | 2024-10-14 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| d902eb29-8b94-3375-8285-46dfd570e9e2 | -12.3807 | -53.1167 | 2024-10-14 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| c64ee4ce-2746-39b5-a294-42169c9df490 | -12.3804 | -53.1376 | 2024-10-14 02:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6808db00-6908-339d-b9c0-f19e5dc0f379 | -13.1273 | -51.6861 | 2024-10-14 02:06:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 9e78fa0a-3caf-3e0d-bbd2-0c84daa97a7f | -17.0823 | -56.0076 | 2024-10-14 02:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| 5d08845e-8755-3a32-ac1d-cf6fe64e6a26 | -17.1957 | -57.4562 | 2024-10-14 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 7e291619-85e1-35bf-89f1-cc9ecd9c0148 | -17.6471 | -56.3084 | 2024-10-14 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 73a5ce68-5cff-3fd5-931b-795df3cbb575 | -17.6474 | -56.2876 | 2024-10-14 02:06:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.9 |
| a4dbadb5-658d-3ff3-b1ee-24ea7222e42b | -18.2338 | -56.6263 | 2024-10-14 02:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.1 |
| dd4936d8-f027-3b9a-9efb-078fd9e5d89b | -18.2555 | -56.5196 | 2024-10-14 02:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.5 |
| de58f3dd-8e60-3335-9069-4431eb22d6a5 | -18.2559 | -56.4988 | 2024-10-14 02:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.8 |
| 07564f7e-2d0b-306b-be47-90a2b40e4efa | -18.2562 | -56.478 | 2024-10-14 02:06:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| eeb45f76-be96-35b1-b389-b8a00c81e494 | -18.233101 | -56.457001 | 2024-10-14 02:14:43 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c10a5dd-41c4-3104-9034-5490d7de2a01 | -18.2321 | -56.4893 | 2024-10-14 02:14:43 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dad5bbb5-443e-3a2e-a37a-a864c41ef795 | -17.929199 | -57.307899 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a8ca4c4-3a1a-30fb-ae6f-1da0b0bf6cc5 | -17.936701 | -57.3339 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 989be5af-b828-37e3-b4ce-8625878c5136 | -17.9196 | -57.310902 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f7cb5799-b819-3626-9a64-dfddf8cc1f0e | -17.927099 | -57.337002 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6ddfd141-86c9-383f-97f9-6fc0c744344e | -17.910101 | -57.3139 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0b3f99f6-df23-308e-906f-60cacd34d159 | -17.917601 | -57.34 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 479af599-48aa-3b9c-b213-47c3721622bb | -17.908001 | -57.342899 | 2024-10-14 02:14:52 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 269839e7-d89d-386b-8e92-96e999a8ed35 | -17.8664 | -57.2705 | 2024-10-14 02:14:53 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1e40817c-353f-3545-8542-9ee56f4a26a5 | -2.4344 | -46.9195 | 2024-10-14 02:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| d1b7e317-da18-3e58-80df-ab67a6983abb | -2.4529 | -46.919 | 2024-10-14 02:15:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c1e90624-24d9-361b-b76a-ae761b5f05ac | -2.6118 | -49.0985 | 2024-10-14 02:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 3e3b1333-7a38-3a02-bffb-e19818cb9b09 | -3.289 | -42.8327 | 2024-10-14 02:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 960a8465-68e0-3dda-a615-316795d03366 | -3.3076 | -42.8553 | 2024-10-14 02:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d759131a-0f47-3adb-89a5-dfa1d40c0566 | -3.3077 | -42.8318 | 2024-10-14 02:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 66e81ccb-88e3-3b4a-a801-3ad84ed6b211 | -3.2889 | -42.8561 | 2024-10-14 02:15:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| b5427663-9d1c-3b8c-b429-adc730af430b | -3.9299 | -56.034 | 2024-10-14 02:15:29 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| aa26f473-bf39-3182-9c89-4a0b37ebe8fe | -4.3718 | -37.9175 | 2024-10-14 02:15:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 8d7859e2-f78a-31ff-98d7-38452dc6d492 | -4.372 | -37.8918 | 2024-10-14 02:15:31 | GOES-16 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 73.6 |
| d97dbb2e-1ec3-3569-8fbc-f4b37133bcf2 | -6.3933 | -59.9929 | 2024-10-14 02:15:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7154dc03-5255-3d7d-b381-fef4bccf9d76 | -7.9603 | -63.6359 | 2024-10-14 02:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 17f87b8a-4746-3450-8945-1cc081ade699 | -7.9419 | -63.6177 | 2024-10-14 02:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c234312e-8720-3b9e-8b89-84a4e2a97704 | -7.9418 | -63.6365 | 2024-10-14 02:15:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 9bb997e3-a992-380b-842a-d0826bb8926d | -9.1021 | -47.9355 | 2024-10-14 02:15:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 73e002b4-9141-3af5-82f1-4365841aa615 | -9.1043 | -61.162 | 2024-10-14 02:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1ac7fba2-a6f8-3759-bd41-774e26b3b805 | -9.4888 | -45.8228 | 2024-10-14 02:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 16a590cd-7d55-351f-94fd-e6414e497f54 | -9.4702 | -45.8023 | 2024-10-14 02:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| ac38c458-2cbc-32f3-84f9-4faae091393b | -9.4699 | -45.8249 | 2024-10-14 02:16:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 33eee044-d2a6-367e-a30c-ab8a2d5ed770 | -10.0619 | -44.2624 | 2024-10-14 02:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 144.3 |
| 099819df-f3ac-3ed6-a9a8-f9caaf20bf29 | -10.0622 | -44.2391 | 2024-10-14 02:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 16cc2963-ac1f-3f6b-8cb1-2aae7a5aad95 | -10.0809 | -44.2599 | 2024-10-14 02:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| eb3fb755-d1e5-3662-b624-e33ebe939642 | -10.0813 | -44.2366 | 2024-10-14 02:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 180.3 |
| fa0e1723-5357-3388-ab4f-e668fd0f32c8 | -10.0816 | -44.2133 | 2024-10-14 02:16:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| af8ecb1e-2f39-3694-87a1-40c782359135 | -10.0166 | -47.3085 | 2024-10-14 02:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 712ee288-3280-38c0-af3f-574c1839b672 | -10.0163 | -47.3308 | 2024-10-14 02:16:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 2c319652-1a58-3ea9-a36f-af3489cf4db5 | -10.4504 | -44.9516 | 2024-10-14 02:16:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 697a80cd-cef9-32b1-858f-febd33f3bfdb | -10.4918 | -42.433 | 2024-10-14 02:16:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 186ce993-ec92-3c15-adb5-202185180135 | -10.5307 | -49.7843 | 2024-10-14 02:16:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9a20890f-e5cb-31ef-b5ec-5959c91a1172 | -10.5118 | -49.7863 | 2024-10-14 02:16:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| fcd096d8-1e49-3f74-9ddc-4eefdc899ab3 | -13.1273 | -51.6861 | 2024-10-14 02:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f13dfb9b-fd9c-3c6d-9fa0-db4afd0762a1 | -18.2342 | -56.6055 | 2024-10-14 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.6 |
| 310651b2-d5dd-334b-816a-037f6179b83e | -18.2346 | -56.5847 | 2024-10-14 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 8b32e9b0-47f9-3e24-b4c7-67fac2675b8b | -18.2555 | -56.5196 | 2024-10-14 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 6bb31ba2-0f9d-3dc5-ac07-7ea3249e63be | -18.2559 | -56.4988 | 2024-10-14 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 42ec1f49-f9d7-3e95-9a83-91127f3bc944 | -18.2562 | -56.478 | 2024-10-14 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 8ffe3c3f-d401-39b4-aed1-7416ff6b421d | -9.089 | -61.1348 | 2024-10-14 02:17:31 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c117bf23-2835-3c41-a49a-9f30ee595516 | -9.0944 | -61.155499 | 2024-10-14 02:17:31 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44d5f59e-c782-35ac-9a75-3e93efbdfcf4 | -9.0793 | -61.137299 | 2024-10-14 02:17:31 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9510366-1e6c-3a7c-bd14-32e3535987a8 | -9.0847 | -61.158001 | 2024-10-14 02:17:31 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac456bfc-c0ad-32e5-88c7-8d66a4cff187 | -2.4529 | -46.919 | 2024-10-14 02:25:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4daf48db-1a18-39c1-8c47-d40ac256a2e1 | -2.6118 | -49.0985 | 2024-10-14 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| eba6a1cc-dedd-342d-8035-8d2f0ef4dbef | -2.6117 | -49.1198 | 2024-10-14 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| eb987bf3-5211-32a1-8387-58ae9ba0e72b | -2.6119 | -49.0772 | 2024-10-14 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 349a10c7-dcdd-3ea6-a7f4-9f72f3513a96 | -3.2889 | -42.8561 | 2024-10-14 02:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 6ede7c18-8e04-3d7a-b37f-2bca9fc210d6 | -3.289 | -42.8327 | 2024-10-14 02:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| fb479453-9d75-3188-9395-a9e046437065 | -3.3076 | -42.8553 | 2024-10-14 02:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 9ca45f97-10ab-347a-b255-3543ae3778b9 | -3.3077 | -42.8318 | 2024-10-14 02:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| a633b1da-eab5-3b8d-b8e3-8d66f41d2122 | -3.3264 | -42.831 | 2024-10-14 02:25:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 4185ce21-256a-3e4b-bc58-19e96b27a23e | -3.9299 | -56.034 | 2024-10-14 02:25:29 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9d95cb6d-39a1-3963-b7db-8fbbafd6f5fb | -6.2141 | -48.329 | 2024-10-14 02:25:42 | GOES-16 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 90865f5e-d1ff-3e26-961c-240704239921 | -7.9603 | -63.6359 | 2024-10-14 02:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 8fff945c-bb4d-3dee-80e3-6df8d5fb827a | -7.9418 | -63.6365 | 2024-10-14 02:25:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6d14a433-7773-3338-a22d-be8918f1ef91 | -9.1043 | -61.162 | 2024-10-14 02:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| df9088b6-ca26-338e-b918-31cd17f2fcea | -9.4888 | -45.8228 | 2024-10-14 02:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 1fe0d009-cccd-3c78-ae01-06778e009bd8 | -9.4885 | -45.8454 | 2024-10-14 02:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| d6bb5066-69a9-3c8f-baa0-d4a4d513b813 | -9.4702 | -45.8023 | 2024-10-14 02:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 773214c3-6e04-38fc-9fbf-2511a6464788 | -9.4699 | -45.8249 | 2024-10-14 02:26:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 173.4 |
| f89fc732-dd0e-3037-a542-ecf85b003cea | -10.0352 | -47.3286 | 2024-10-14 02:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| dbfeccb0-7f46-3d8a-9ce4-1bce1b4e3707 | -10.0166 | -47.3085 | 2024-10-14 02:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 85dcb6da-bd8c-3763-89e3-07d9e328ee65 | -10.0163 | -47.3308 | 2024-10-14 02:26:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 56f011f8-a41a-35c2-a9ad-f886ddf5dde1 | -10.0816 | -44.2133 | 2024-10-14 02:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 5c66c8cc-3ef4-3f5d-997a-8a2befb87cfa | -10.0813 | -44.2366 | 2024-10-14 02:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 609dc6b9-6ae6-3dbc-8694-8c9ffb191697 | -10.0809 | -44.2599 | 2024-10-14 02:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| b53d5aad-0ba8-3dfe-abf2-f8683e09062c | -10.0619 | -44.2624 | 2024-10-14 02:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 6d36b139-c7db-36a8-a477-7ab4260eb558 | -10.0622 | -44.2391 | 2024-10-14 02:26:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 179.2 |
| cb0f1ba8-5925-3d36-ada1-82841a981934 | -10.5307 | -49.7843 | 2024-10-14 02:26:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| f8bb6bc1-b7a6-3b92-8b76-7a789bfb5ddc | -12.889 | -53.5402 | 2024-10-14 02:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| b7b7fe95-abe0-3cd7-a3e0-082afabbf2a9 | -13.1475 | -62.3215 | 2024-10-14 02:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d83e031e-0586-3cc9-8260-8b111611c184 | -17.0823 | -56.0076 | 2024-10-14 02:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| b0ebef0b-01d9-3a29-a542-d64b06475971 | -17.02 | -57.4153 | 2024-10-14 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| eccee9ef-a670-32f2-9023-1130b0861297 | -17.0197 | -57.4358 | 2024-10-14 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 8719f2d6-6ed7-3816-82c7-f03bbe5096ad | -17.0004 | -57.4176 | 2024-10-14 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |


[Clique aqui para ver as próximas entradas](README27.md)
