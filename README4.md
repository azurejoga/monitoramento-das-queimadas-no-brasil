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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9941705-6efb-3f03-98c1-bc2fffddea1b | -17.1467 | -56.8463 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.1 |
| 56b2710a-8853-34cf-9d0d-dc962ff96a24 | -17.1471 | -56.8256 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 6a590bf0-6e24-3ce1-b89f-6cb27bf805c0 | -17.1784 | -57.3148 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 7f56ca57-2db9-3041-bd96-62f1a13bf9cc | -17.1977 | -57.333 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.7 |
| 6a1481d2-04aa-30f8-ac25-e49a143cdd31 | -17.198 | -57.3125 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 8c9ef610-259c-3f8b-893d-dd3f7ffadfa6 | -17.2173 | -57.3307 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 73eca483-9b9d-350a-bd30-ed2fd880d975 | -17.2177 | -57.3102 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 06e9b05a-c800-357b-9afa-ddc3365d5adb | -17.3149 | -55.0603 | 2024-10-09 00:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 65a8b8d9-8c3f-3b28-94a3-ed79f5a358ca | -18.1193 | -56.3921 | 2024-10-09 00:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 5ffe2321-7cad-3fdb-91ec-f65cfe0316d2 | -18.5993 | -57.2629 | 2024-10-09 00:16:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 1466031d-7017-3800-9f66-dd0b0f0d781c | -18.5996 | -57.2422 | 2024-10-09 00:16:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 98.6 |
| 23c4c5ae-80fc-3fea-a3e4-2429f8645920 | -19.674 | -46.2248 | 2024-10-09 00:16:55 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2e6c3750-b475-3952-90a5-2d46027a8bc0 | -19.9924 | -42.4346 | 2024-10-09 00:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 141.0 |
| 34fdc13e-1ae6-3bda-8560-abe222a0a5b8 | -20.013 | -42.4287 | 2024-10-09 00:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.2 |
| 458c52ee-65d1-305b-9efe-a1155fe98347 | -20.1087 | -48.8261 | 2024-10-09 00:16:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 85d867bc-cd41-33b5-ade9-616a1d7ca467 | -20.1093 | -48.8031 | 2024-10-09 00:16:57 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 119.0 |
| b10947d2-dc21-3eb8-9c90-2c53797c784d | -20.1291 | -48.8217 | 2024-10-09 00:16:58 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 5de16f20-0d03-3523-a519-817c0e00d718 | -20.4351 | -43.9299 | 2024-10-09 00:16:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| 921ab6fc-b343-304d-a2d3-de90c8d46fa3 | -20.4133 | -48.8282 | 2024-10-09 00:16:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 2b7f43e6-11bd-3b60-9d42-23c0ed3ae527 | -20.7839 | -47.2559 | 2024-10-09 00:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 147.0 |
| fd013ef1-ea4f-3dd7-a547-5d40819e2564 | -20.7846 | -47.2323 | 2024-10-09 00:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 201.1 |
| cf2cd6ef-6e5b-33ca-9204-af67b68f3f15 | -20.8052 | -47.2273 | 2024-10-09 00:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 108.0 |
| a9bc5217-6b90-30bc-86ee-93c8d0463971 | -21.5649 | -47.9114 | 2024-10-09 00:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ef89e8e2-ab67-3e2a-8ed6-9ae196e8285f | -21.5656 | -47.8878 | 2024-10-09 00:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 91ec49d8-7afd-3fe5-8004-d814ff8d6573 | -21.5928 | -46.9845 | 2024-10-09 00:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 71.0 |
| be9a5baf-a6dd-301e-b9cf-7a5865bf9d0b | -21.5935 | -46.9606 | 2024-10-09 00:17:05 | GOES-16 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a327e693-73a7-30d8-9c89-088ca5d6367d | -21.5857 | -47.9063 | 2024-10-09 00:17:05 | GOES-16 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 126.7 |
| a5764a71-2493-3ca4-bae7-06b4424007b6 | -21.5864 | -47.8827 | 2024-10-09 00:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 162.0 |
| e350a3de-fabc-3e19-b98c-e2e3e82f6d0e | -21.5871 | -47.8591 | 2024-10-09 00:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 2d9a725f-49b5-325c-be20-29b76a240702 | -21.552 | -46.9712 | 2024-10-09 00:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 63fa8974-df09-3308-8f2c-33e1ffa6872a | -21.572 | -46.9898 | 2024-10-09 00:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 119.4 |
| c41f6f86-886f-33ed-a2ab-d3c8b01cf5e6 | -21.5727 | -46.9659 | 2024-10-09 00:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 9a0fee9b-b556-3eab-ae3d-f87ad38db8c0 | -21.8165 | -49.1774 | 2024-10-09 00:17:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| 788c81d0-630e-341f-bcda-9fa091b0a255 | -21.8172 | -49.1541 | 2024-10-09 00:17:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| f970c4c5-3380-32e9-b7ef-73f3e5c2fcb8 | -21.8373 | -49.1726 | 2024-10-09 00:17:06 | GOES-16 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.3 |
| 4d1ee080-d8df-33be-9ab2-2865d3b7965e | -21.838 | -49.1493 | 2024-10-09 00:17:06 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.9 |
| 344ec086-99a7-30a7-89d3-6dd39d303f31 | -22.813 | -48.4462 | 2024-10-09 00:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 944b6429-30e8-3ed7-b7a1-7de82f582ee9 | -22.8137 | -48.4225 | 2024-10-09 00:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 6a70746f-60b4-3003-a161-1e1a4eaa3e8d | -22.8347 | -48.4171 | 2024-10-09 00:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 6574c11f-6a3c-31e8-862a-60e37bf229a9 | -1.11 | -53.6173 | 2024-10-09 00:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| e8d0ac0e-3708-30b1-b572-71c3395e1f50 | -1.1101 | -53.5972 | 2024-10-09 00:25:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ae59023a-a0da-3f54-9e21-e146539c3cfe | -1.9609 | -50.8404 | 2024-10-09 00:25:17 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 20511d11-1a46-327f-88f7-4c8306ecd942 | -2.9829 | -53.7267 | 2024-10-09 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 17831d9c-21cd-3b24-b056-fe3a0fb95ab0 | -2.983 | -53.7065 | 2024-10-09 00:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6968e977-29d8-3cb6-bd1b-ef118197b235 | -3.8007 | -41.6229 | 2024-10-09 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.0 |
| 8649a896-598a-3b3f-9627-bb474895ffed | -3.8008 | -41.5989 | 2024-10-09 00:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| c953e754-7512-31b5-9b3b-e043fcaaa75a | -3.8196 | -41.5979 | 2024-10-09 00:25:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| e97dc046-cdb8-37b8-8117-16a012eeb0ed | -3.9393 | -46.4672 | 2024-10-09 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| daf5d5f7-6d9f-3df4-b38d-3ea5b3380c1e | -3.9394 | -46.445 | 2024-10-09 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 131.1 |
| a249f91b-680e-3b1c-bf53-51b0638d961c | -3.9023 | -46.4467 | 2024-10-09 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 47edf913-0791-336e-8539-f406bb1714eb | -3.8119 | -49.4841 | 2024-10-09 00:25:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 494047d6-93ac-3045-ade5-a0e3c10a56ef | -3.9021 | -46.4689 | 2024-10-09 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 738db192-ceb2-3278-8591-894a06c1b9d6 | -3.9208 | -46.4459 | 2024-10-09 00:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d5d80566-7dc8-3838-9235-61f08088d893 | -5.2253 | -43.8164 | 2024-10-09 00:25:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| bbe829ce-3af8-3e0b-b134-b809fc66278f | -5.2441 | -43.8151 | 2024-10-09 00:25:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 4399cdb1-a509-3eae-9693-a3bcdf30c4bf | -5.4421 | -49.5559 | 2024-10-09 00:25:37 | GOES-16 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5aad44e5-2230-3c42-8e99-50064fe1c574 | -5.8216 | -44.1196 | 2024-10-09 00:25:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| fcf26853-ebc2-3fd2-bba8-e3ed2d7632ce | -6.7614 | -60.0559 | 2024-10-09 00:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 6580a396-2a1c-3476-bc26-c02ad3e73d05 | -6.7615 | -60.0367 | 2024-10-09 00:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| aaa54306-acd9-36d9-a5de-667f021d722f | -6.7798 | -60.0552 | 2024-10-09 00:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 57b26697-cdc2-35df-9bcb-6168f97062ee | -6.7799 | -60.036 | 2024-10-09 00:25:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| b6362b4e-ca35-3baf-a574-a8c677228e9f | -7.0231 | -59.4303 | 2024-10-09 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b846aa48-8bed-3804-9faf-af0d64660faa | -7.0232 | -59.4111 | 2024-10-09 00:25:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c8b76d3d-d62b-372c-9ea3-1cde03fc10f9 | -7.2435 | -59.633 | 2024-10-09 00:25:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d7622608-09e0-380d-b9d5-36ead6c3705f | -7.2436 | -59.6138 | 2024-10-09 00:25:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 716e10a3-c2bc-3f85-bb61-dc9a206d5e1a | -7.2619 | -59.6323 | 2024-10-09 00:25:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c2c82ba1-c4c6-3442-8c80-3213f5247b6b | -8.4919 | -48.6476 | 2024-10-09 00:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 231.0 |
| 6e0414b5-4c24-3ffd-872f-992a554764b8 | -8.4921 | -48.6259 | 2024-10-09 00:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 185.4 |
| 234b4a90-e8de-34bd-ba0a-127e7ec96a4b | -8.5107 | -48.6459 | 2024-10-09 00:25:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e9906ce0-e370-3162-839e-299153d66d9a | -9.1044 | -61.1428 | 2024-10-09 00:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 33139c85-1598-381c-a441-6088f2d9b48d | -9.1573 | -61.5803 | 2024-10-09 00:25:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 703dced1-156b-3c0f-b04c-a472d0a525ab | -10.3656 | -64.8262 | 2024-10-09 00:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ad168bb9-128e-3f79-a0b0-15382b26255c | -10.3894 | -61.2502 | 2024-10-09 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 804604fb-2c14-3861-83e9-d7d59e8208fa | -10.3895 | -61.231 | 2024-10-09 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 24ca8f81-5394-3201-a282-ebe88043570a | -10.3843 | -64.8255 | 2024-10-09 00:26:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c521e576-3507-3ce7-81f8-2662d6e5275e | -10.4287 | -60.9979 | 2024-10-09 00:26:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 04568e74-8bb1-3e7d-b5fc-21021624d2a1 | -10.5943 | -64.024 | 2024-10-09 00:26:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 5cb10560-1f99-3176-a664-5c9fc5a40f74 | -10.7056 | -64.1516 | 2024-10-09 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 18c7a80d-7e9f-3f08-be3a-a8e314e08eaf | -10.8754 | -63.9169 | 2024-10-09 00:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 7129967e-6fc2-34a5-82e4-c902321c6582 | -10.8755 | -63.8979 | 2024-10-09 00:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 116.9 |
| ea78032d-4ceb-3579-a708-f089b2567078 | -10.8925 | -64.1623 | 2024-10-09 00:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 51395b35-713d-3760-bdb9-63c1c33bbd99 | -10.8941 | -63.916 | 2024-10-09 00:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8ccc8a5d-72d9-3784-a242-7e616f9602f9 | -10.9112 | -64.1615 | 2024-10-09 00:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 148.7 |
| 3c8ff8d8-3145-3c67-926b-adc81711c1e8 | -10.9113 | -64.1426 | 2024-10-09 00:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 179.5 |
| acf096f2-4d6d-33d1-92ac-a2ba7aab8537 | -10.9082 | -68.3988 | 2024-10-09 00:26:09 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 47.5 |
| a1756f71-c53c-3a89-9c26-2bcafb9c7f9c | -10.9301 | -64.1417 | 2024-10-09 00:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.9 |
| af3d0c91-6a00-360f-be5e-be630b9b0392 | -11.5728 | -58.9423 | 2024-10-09 00:26:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 28a46e9c-45aa-3085-8e63-7e0c004fe7a5 | -11.5233 | -65.137 | 2024-10-09 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 197dd547-ae87-3e68-bc06-87c7247e39af | -11.5726 | -58.9619 | 2024-10-09 00:26:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 5d90526c-c4ec-340c-9040-86cdf8d6deee | -11.6806 | -64.0312 | 2024-10-09 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 13fa532e-d593-3f82-95bc-730b5d298978 | -11.6808 | -64.0121 | 2024-10-09 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 87068fa3-42fc-32f5-a5cf-c55dc7d8d576 | -11.9917 | -51.0766 | 2024-10-09 00:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 9edb60a8-9118-37bc-9845-2978f9eb0bc2 | -11.992 | -51.0553 | 2024-10-09 00:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d3f01557-e0ea-35f6-a4f1-56a5b042fa76 | -12.0107 | -51.0744 | 2024-10-09 00:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| cf10ca09-475c-3c06-b65f-6f357328ab61 | -12.011 | -51.0531 | 2024-10-09 00:26:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 6e582135-aec7-3e9e-8215-8868d23274e2 | -12.7673 | -44.8904 | 2024-10-09 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| c0ea11f2-c0c5-39a7-bacb-bbdd205c3327 | -12.6676 | -63.0819 | 2024-10-09 00:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 116.4 |
| f9dfdb2d-9a0a-37d9-b860-660c24419692 | -12.6875 | -62.9656 | 2024-10-09 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c1197478-3098-3f6c-9bc2-3221e18d1f1c | -12.6876 | -62.9464 | 2024-10-09 00:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e17e6495-fc78-3091-8b17-8a3a44aefcd4 | -12.7501 | -62.269 | 2024-10-09 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |


[Clique aqui para ver as próximas entradas](README5.md)
