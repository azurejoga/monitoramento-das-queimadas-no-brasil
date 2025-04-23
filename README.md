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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29a727bb-8fee-3b04-87de-7ad3bdfbce83 | -17.40277 | -39.3516 | 2025-04-23 00:09:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a89390a4-1ad7-38bb-938e-238dba2f0d7c | -8.09321 | -43.12083 | 2025-04-23 00:11:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a59c9e0f-7d1e-36ce-a6e1-48853ec31bac | -8.09175 | -43.10972 | 2025-04-23 00:11:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e8eff5fd-4cec-3f6b-95ee-425ea79e0f94 | -21.2432 | -49.497898 | 2025-04-23 00:27:00 | METOP-B | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77085871-b7bf-3b5e-8580-2aa49f329cd1 | -11.3311 | -52.945202 | 2025-04-23 00:27:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8f6de8fc-c75f-3d73-84ec-d9366e2c3c36 | -20.1847 | -50.489601 | 2025-04-23 00:27:00 | METOP-B | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d4e4b417-982f-3435-a164-48d7d58fde16 | -21.2416 | -49.489799 | 2025-04-23 00:27:00 | METOP-B | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57dc4ae4-4eba-3a8c-9a37-33d8dd4ec0c5 | -11.3329 | -52.9538 | 2025-04-23 00:27:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dad9e2e7-2572-31e3-acf4-dc14f72085d4 | -20.183001 | -50.481098 | 2025-04-23 00:27:00 | METOP-B | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c96911f8-2e86-3c79-b3d3-d9b0802306be | -20.192699 | -50.478901 | 2025-04-23 00:27:00 | METOP-B | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c92831f1-e997-3d25-95ef-4e57306294cc | -19.999901 | -49.375599 | 2025-04-23 00:27:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 406a5b23-47b1-38c2-a532-3625cc4e44d8 | -19.998199 | -49.367802 | 2025-04-23 00:27:00 | METOP-B | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05707349-9c7e-3e88-a620-9719b54fae2f | -10.33802 | -38.48415 | 2025-04-23 03:25:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2346cc79-3e0d-3dfc-aa41-49af51d68f58 | -10.697 | -37.04943 | 2025-04-23 03:25:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0d6b4cb3-9618-370a-a5f2-6049cf2f673a | -20.07758 | -48.45623 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0052151-0d1d-30c0-a8c2-58298b4cad14 | -20.07892 | -48.46331 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 147b1cb4-68dd-361e-b235-ae7b4c6bb59a | -20.07192 | -48.46124 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 475b6d05-e89c-3b90-b166-cdf9a38c1fc0 | -22.54025 | -48.81442 | 2025-04-23 03:28:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1cebd02-1070-328c-943a-8b7ea9a17c75 | -20.08078 | -48.45596 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 923974a2-59e1-3dde-a54a-8d7712081f32 | -20.06875 | -48.46157 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 889a0bc4-7afd-3687-8457-e943ca1ceb81 | -20.07575 | -48.46364 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1492d836-3171-325f-8a78-f77364bd8e38 | -20.07379 | -48.45388 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b9376491-676a-3f68-bdb6-73424110f45c | -20.07058 | -48.45415 | 2025-04-23 03:28:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 576e80aa-a0bc-3ea9-b03e-9634790eb41b | -13.45611 | -43.56529 | 2025-04-23 03:47:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63b8a6ec-73cb-3315-b655-bde51428046a | -14.14213 | -43.17421 | 2025-04-23 03:47:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ecb3dbf3-e570-3f7e-a965-15331b790a95 | -9.56212 | -35.69296 | 2025-04-23 03:47:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 91a94486-3c75-3a40-aef6-2c8e7afa8de4 | -10.69611 | -37.0476 | 2025-04-23 03:49:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e888cf02-09af-3914-8a39-b4ab4499e1fd | -20.40803 | -45.88586 | 2025-04-23 03:49:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d71bdc1-2a15-35fd-940c-ceeb1bda898e | -20.06171 | -49.36618 | 2025-04-23 03:49:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ef1f6eec-1aea-395d-9e24-3285f7a10dcc | -10.85501 | -37.53011 | 2025-04-23 03:49:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1fe83efd-394f-3710-a35f-538add7c0af7 | -20.52397 | -47.49911 | 2025-04-23 03:49:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e1d2fc0-e166-3475-a00c-f736760e2404 | -10.77221 | -37.71028 | 2025-04-23 03:49:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8a803955-6b0a-3fb9-bf19-28dcd0867d75 | -10.33704 | -38.48389 | 2025-04-23 03:49:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| db511b71-462a-39e9-b626-bb124e04f5ac | -21.31202 | -49.4887 | 2025-04-23 03:49:00 | NOAA-20 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c9a813a8-5bb2-3d81-b189-f2dfb2c2707c | -21.13171 | -47.80179 | 2025-04-23 03:49:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c10f8c8-94fa-3a33-8a4e-7e8b513a58b1 | -21.31132 | -49.49198 | 2025-04-23 03:49:00 | NOAA-20 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 09a8ea4b-9cd3-3878-a41d-124e571ae8ba | -16.68087 | -43.88337 | 2025-04-23 03:49:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 632386ac-d7c4-3dc8-b6db-881a0ff1277d | -22.54015 | -48.81182 | 2025-04-23 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c368285a-b963-3c49-a909-cd8a9bec602a | -22.79494 | -49.44187 | 2025-04-23 03:51:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25831282-10b3-3cf3-aad5-73652eda4811 | -29.77959 | -51.17523 | 2025-04-23 03:53:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 2ab8575f-52c3-3dfd-84a9-c20fd74a34d9 | -29.77867 | -51.1757 | 2025-04-23 03:53:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 44d5d4c9-4f5c-3107-a6d3-1e9907937a7c | -29.68101 | -55.52097 | 2025-04-23 03:53:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| c68feeec-9835-3b61-8d95-3b5b7cb6ee0e | -6.38264 | -47.2559 | 2025-04-23 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a59aee7-77ed-3be5-bee2-0f12368c9162 | -8.09088 | -43.11165 | 2025-04-23 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d539d05a-ba8f-3b73-ba5f-dd9ae15d6d5e | -8.08641 | -43.11102 | 2025-04-23 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 212454c5-5584-3172-845c-02e3cce807a4 | -6.84046 | -44.32135 | 2025-04-23 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184b1e63-99c6-36dd-93b0-7c715ae8ca07 | -8.09535 | -43.11229 | 2025-04-23 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| a970f34e-7e45-3c88-801a-085b64d7089a | -6.22864 | -48.05994 | 2025-04-23 04:38:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05246931-7722-3036-a52c-a8ac77e2c6a0 | -11.39824 | -52.95486 | 2025-04-23 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93540fa1-5c27-3189-96ad-64e20bf45885 | -14.14083 | -43.17343 | 2025-04-23 04:40:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f7964c0a-e4da-34fc-8034-71496a03fc7f | -11.39888 | -52.95092 | 2025-04-23 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02b18cf0-b5ef-3e63-a12c-4115df25d255 | -11.84305 | -58.04322 | 2025-04-23 04:40:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9cdcc37-cc14-3311-a25e-1a381c1343b8 | -12.42441 | -51.52638 | 2025-04-23 04:40:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51a90850-99a0-38d4-80cc-2cfd34db1906 | -11.39952 | -52.94698 | 2025-04-23 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 24c6255f-1e61-335e-bd4e-a9ccb1e34fb2 | -11.27514 | -52.45901 | 2025-04-23 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5e053cd-a4e0-3839-933b-a4954b627dcc | -11.27495 | -52.45906 | 2025-04-23 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77a0034b-e6bc-384d-ad52-59ae9395a366 | -11.84082 | -58.03967 | 2025-04-23 04:40:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c08d7250-3e18-3818-b104-48253e6bf71b | -18.90999 | -47.00984 | 2025-04-23 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59422557-2898-3177-95aa-c723e9c35020 | -18.90954 | -47.01332 | 2025-04-23 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70ec1d82-6b4a-308d-864e-b55a3d5242f0 | -21.38735 | -48.23341 | 2025-04-23 04:42:00 | NOAA-21 | GUARIBA | SÃO PAULO | Brasil | 3518602 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed0da797-533a-3f0c-99b8-12b8b4152777 | -21.94771 | -48.03114 | 2025-04-23 04:42:00 | NOAA-21 | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd3f6334-0e13-3dd9-8dce-341136160bda | -20.06399 | -49.36573 | 2025-04-23 04:42:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3e44a11c-83e1-3499-8b21-e0644442db9f | -22.5423 | -48.812 | 2025-04-23 04:42:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18248e37-9e1d-3481-a487-32b5b57c0e6a | -22.24998 | -52.97945 | 2025-04-23 04:42:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 23657126-5d7b-3885-b85b-2bab7f71740f | -22.79813 | -49.4409 | 2025-04-23 04:42:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fdc59f2-7184-3907-a893-9253a5d9b877 | -22.24939 | -52.98317 | 2025-04-23 04:42:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73cef344-feaa-38c9-a2fe-9427a7017258 | -22.32417 | -48.79986 | 2025-04-23 04:42:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 154da129-655e-3073-9edd-512da944a159 | -25.03689 | -49.27252 | 2025-04-23 04:44:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81fc0561-f686-3ee8-866e-c9a6366ee0f3 | -29.77998 | -51.17731 | 2025-04-23 04:44:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 57e5d3b8-0cbb-32f5-933e-d8f3d3374960 | -28.76355 | -50.156 | 2025-04-23 04:44:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3da1610-a74d-350d-ba31-997e73adc163 | -26.33913 | -53.18964 | 2025-04-23 04:44:00 | NOAA-21 | PALMA SOLA | SANTA CATARINA | Brasil | 4212007 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 65067e0d-e8bb-3fe8-bbf3-7adf1cdca756 | -28.76438 | -50.15515 | 2025-04-23 04:44:00 | NOAA-21 | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c92051c3-256c-3059-905e-712eef40496b | -30.46351 | -56.38517 | 2025-04-23 04:46:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 59c5fcd3-d86b-3acb-af82-a8bdd39a409d | -3.49684 | -51.17782 | 2025-04-23 05:04:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd0de035-5901-357c-86cf-f0fb5c290878 | -11.842 | -58.04071 | 2025-04-23 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0123cef-f3bc-3b5c-adbe-9a0d666842e0 | -11.39949 | -52.94936 | 2025-04-23 05:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33e36044-afc3-3d34-84d7-d24906941e48 | -11.84258 | -58.03712 | 2025-04-23 05:06:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6901503d-fd80-39b6-be2a-553fad88d28a | -8.30742 | -55.10565 | 2025-04-23 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0dddf224-50c9-3147-b001-42e8110981bb | -21.34883 | -57.64306 | 2025-04-23 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1025ec49-699d-3f27-8fc1-a18d7cd5951b | -21.34941 | -57.63917 | 2025-04-23 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| fa93e26b-d861-3152-bd93-cec8212cf88d | -29.68469 | -55.51809 | 2025-04-23 05:12:00 | NPP-375D | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| f051cbdb-af65-3051-9ea1-2b5b52aa7572 | 1.11364 | -60.5269 | 2025-04-23 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72dee0a4-2215-3624-94fc-ab29c7f881c1 | -11.84295 | -58.04205 | 2025-04-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d38628d-64a6-33bc-9e9e-0233d8c2750d | -11.39549 | -52.94833 | 2025-04-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c14477d-9c71-3c1a-9b57-49bb2447c0f7 | -11.39501 | -52.95227 | 2025-04-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8552d90b-da81-3540-8d80-e5bbc2cac7cf | -11.3997 | -52.9459 | 2025-04-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12d85e49-31c1-36c4-afd2-f6b655197d19 | -11.83939 | -58.03776 | 2025-04-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38caa50d-c1f2-3514-a18c-3ce8c0494e5f | -11.4012 | -52.949 | 2025-04-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13ddee7c-0a29-32af-bcae-e15ee0ac0e8f | -11.3992 | -52.94984 | 2025-04-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54ea13fc-206b-34ec-a53f-e7df308b09b6 | -11.83888 | -58.04144 | 2025-04-23 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dcc588d9-3fa8-3697-8c0c-d9726d1a0091 | -11.3987 | -52.95377 | 2025-04-23 05:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 115f8e67-5472-3d84-a0f8-2f9e07c8a164 | -15.38877 | -60.1808 | 2025-04-23 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06b152bd-a7ed-3bbe-a224-f753ef44b00f | -15.38941 | -60.17612 | 2025-04-23 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f4702ec-3232-392e-8ea3-53d8c64581f9 | -13.21702 | -43.56453 | 2025-04-23 12:36:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f1dbda72-b19d-3fcd-bc59-999991df0d5f | -11.40512 | -52.93894 | 2025-04-23 12:36:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4a39e330-76b0-3dc1-b27d-467ac5936b75 | -29.60039 | -51.31778 | 2025-04-23 12:42:00 | TERRA_M-T | SÃO SEBASTIÃO DO CAÍ | RIO GRANDE DO SUL | Brasil | 4319505 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 52a77e32-1906-3e25-9d65-d5b62e187da3 | -29.48631 | -51.12295 | 2025-04-23 12:42:00 | TERRA_M-T | PICADA CAFÉ | RIO GRANDE DO SUL | Brasil | 4314423 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2d821abe-be9c-3116-a6a2-85d62790fc7d | -29.48768 | -51.11209 | 2025-04-23 12:42:00 | TERRA_M-T | PICADA CAFÉ | RIO GRANDE DO SUL | Brasil | 4314423 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |


