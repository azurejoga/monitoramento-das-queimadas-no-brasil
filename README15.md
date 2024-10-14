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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d658ffa-437f-31ca-b95f-512baa7c86e8 | -4.6384 | -44.8615 | 2024-10-14 00:55:33 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d790080b-8e56-3e64-b2d4-9d74b0c2977a | -4.7224 | -46.1608 | 2024-10-14 00:55:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 73c94d74-3f70-3d40-b7af-0e19b3d4b276 | -4.9097 | -46.0163 | 2024-10-14 00:55:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| e5bb820d-599c-389a-835d-f45f8b453cc5 | -6.3749 | -59.9936 | 2024-10-14 00:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 8a4f4577-ca9c-3761-ba62-6ef7c9b1f1ff | -6.3933 | -59.9929 | 2024-10-14 00:55:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 24259ffa-aa27-3406-9670-c60d99644e70 | -7.7292 | -43.2049 | 2024-10-14 00:55:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 154e40ef-85fc-36d6-bfcd-b55b262ed75a | -7.9623 | -49.0823 | 2024-10-14 00:55:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f135fe42-b416-3b3e-bdbc-05aeea3ca950 | -7.9625 | -49.0607 | 2024-10-14 00:55:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 176.7 |
| 755304e0-472c-3a67-8758-e6234e6bbe98 | -7.9418 | -63.6365 | 2024-10-14 00:55:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| fc318594-e863-3ef0-89bc-24b75b593880 | -7.9419 | -63.6177 | 2024-10-14 00:55:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d455d4a1-235b-33e6-affa-6bbe5130294b | -7.9603 | -63.6359 | 2024-10-14 00:55:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2479ce96-14a1-3651-a0f3-e30ddf9ce4ae | -7.9604 | -63.6171 | 2024-10-14 00:55:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 962e782f-a54b-3a07-bbe3-4b12ec9cbad4 | -8.4734 | -48.6276 | 2024-10-14 00:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 927fc8f6-a6ab-39e6-a4a2-5a03efca1270 | -8.7025 | -63.1568 | 2024-10-14 00:55:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 5ec2af0b-f167-386f-8424-dc58cc6e6e2a | -9.1021 | -47.9355 | 2024-10-14 00:55:58 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 539eef40-c41c-3d7b-b4a3-c993377253f4 | -9.1042 | -61.1811 | 2024-10-14 00:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7ffabb7e-acc0-3acd-a784-9b268cbbffe9 | -9.1043 | -61.162 | 2024-10-14 00:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| dc7112e6-d084-36cd-9431-8b774920ec41 | -9.6928 | -47.4774 | 2024-10-14 00:56:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 3c40a260-4df6-3c4a-b740-91c2db6d3f7b | -9.7117 | -47.4754 | 2024-10-14 00:56:01 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 483aec11-a9fc-3395-8ee8-436b73ad0931 | -10.0622 | -44.2391 | 2024-10-14 00:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 140.7 |
| d90fd82b-afb5-3f31-b2b8-346b3606bf7c | -10.0626 | -44.2158 | 2024-10-14 00:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 646a4a32-746f-3658-9066-8978f21f2ec2 | -10.0813 | -44.2366 | 2024-10-14 00:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 249.6 |
| 647f6963-0b9e-3e75-bd87-39dfc82afe9f | -10.0816 | -44.2133 | 2024-10-14 00:56:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| eda2d7c2-0326-3910-ad85-a3d71a3f7d8c | -9.9973 | -47.3329 | 2024-10-14 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ea0389a1-ab72-37d5-8837-e4fbc39de9c4 | -9.9976 | -47.3107 | 2024-10-14 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| a33bc3ed-0ce8-3edc-9774-1e1ada791af1 | -10.016 | -47.353 | 2024-10-14 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 8eb2e6ce-9575-34db-bdef-d5a56f8bb602 | -10.0163 | -47.3308 | 2024-10-14 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| 703789bd-bf07-3b20-9bcf-75b4a18db431 | -10.0166 | -47.3085 | 2024-10-14 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 3d3038b7-bfe3-3d7d-b26d-8f26e3451a56 | -10.0352 | -47.3286 | 2024-10-14 00:56:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 5eef8c6f-3933-3735-9009-805a19bfff70 | -10.4918 | -42.433 | 2024-10-14 00:56:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 4c8bc9d4-f1cc-316d-a61c-30ca06987110 | -11.17 | -39.9192 | 2024-10-14 00:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 102.6 |
| 0932a242-8b66-3520-bbe7-cb1ef52449fa | -11.1705 | -39.894 | 2024-10-14 00:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 146.0 |
| 4b19a9c4-9c57-3f22-b1d4-61999af231fc | -11.1893 | -39.9159 | 2024-10-14 00:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 58.1 |
| 926230af-97f3-37dd-ab61-3498481e8ebb | -11.1898 | -39.8906 | 2024-10-14 00:56:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 82.0 |
| ef0efbef-01a9-31b6-87f0-e18bdbbc8cec | -12.4981 | -63.0148 | 2024-10-14 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| bac9cd45-4c32-349f-b6a9-7dbcc8f10928 | -12.4983 | -62.9956 | 2024-10-14 00:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 84a7c506-ba5e-3672-a9aa-f4064df320b3 | -12.8699 | -53.5423 | 2024-10-14 00:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| d57c804d-ba11-3984-81d0-ce4ee7b1d888 | -12.8702 | -53.5215 | 2024-10-14 00:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 9715e6b0-a257-30a0-b689-d45bfc504299 | -12.889 | -53.5402 | 2024-10-14 00:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 12910c20-eb50-3152-acaf-5eb89ea9a5dc | -12.8893 | -53.5194 | 2024-10-14 00:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3fbfe357-2e5b-33c9-8453-048fe763f170 | -17.6876 | -56.2409 | 2024-10-14 00:56:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 91ace1c2-1775-3cee-a725-427eed07153a | -21.76 | -48.2851 | 2024-10-14 00:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 22534eaa-dc14-32d4-bf00-0ebfd5bc031d | -21.8635 | -48.9814 | 2024-10-14 00:57:07 | GOES-16 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| e42c0118-d4f4-3eee-b18b-0077d483f768 | -11.18 | -39.92 | 2024-10-14 01:04:20 | MSG-03 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 076b82b3-36ba-3271-b8e1-c799a261addc | -9.86 | -36.41 | 2024-10-14 01:04:28 | MSG-03 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df8666de-7cc0-3947-943b-04e832b9cad1 | -10.05 | -44.22 | 2024-10-14 01:04:28 | MSG-03 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 225238a5-896b-3185-8a85-004d64c5e539 | -3.32 | -42.83 | 2024-10-14 01:05:07 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6df7424d-f20c-378c-b16f-a5265236cccc | -3.32 | -42.87 | 2024-10-14 01:05:07 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b39148b-6793-351c-8908-273bee44f712 | -3.29 | -42.83 | 2024-10-14 01:05:10 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a122ae2-47f7-398b-b5f0-feeabcc70474 | -2.4344 | -46.9195 | 2024-10-14 01:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0f31ffd1-08df-3af2-b0c5-fd25170cb804 | -2.4529 | -46.919 | 2024-10-14 01:05:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0a8dbd3c-4f44-3513-831e-fdfaac6d5b0b | -2.6117 | -49.1198 | 2024-10-14 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| de24b771-bb8d-31ef-90e2-e4d31df19ad0 | -2.6118 | -49.0985 | 2024-10-14 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 42b9cde3-500e-353f-82a8-cc0377b046b1 | -2.6119 | -49.0772 | 2024-10-14 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 06734ad3-743a-361b-8431-963585d811fc | -2.6052 | -57.5711 | 2024-10-14 01:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ab0dc207-254e-3de0-a075-85146c4f7871 | -2.6303 | -49.098 | 2024-10-14 01:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 5560f582-ebcc-325c-afb3-e80436e5bda9 | -3.2889 | -42.8561 | 2024-10-14 01:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 34d297d3-cc60-30c2-828b-3f2cd800de90 | -3.289 | -42.8327 | 2024-10-14 01:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 4193421c-1a02-37ab-9780-c6040f80cf83 | -3.3076 | -42.8553 | 2024-10-14 01:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| d2d0939e-c321-37ec-b5fe-2f17d2a19be0 | -3.3077 | -42.8318 | 2024-10-14 01:05:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 251.2 |
| 7a1ca5d1-9895-3682-afdb-8dc06ad6a6db | -3.1982 | -50.3077 | 2024-10-14 01:05:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 0c9609f7-346b-3c0b-aec4-69dfe263990e | -4.1146 | -48.2731 | 2024-10-14 01:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f6cf001b-0d1b-3208-9a60-e3a583412ee4 | -4.3428 | -50.5172 | 2024-10-14 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 93d91e8f-f440-3286-8810-7c99ac9bf457 | -4.343 | -50.4962 | 2024-10-14 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1a2c9398-e9f0-37cd-99a4-8ccfe5bfad6c | -4.3613 | -50.5164 | 2024-10-14 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1c5fa24d-8bbd-3e54-a2c6-c839ae07bb98 | -4.3615 | -50.4954 | 2024-10-14 01:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 89146185-7c53-3086-8291-6cfc3bb5d3ef | -4.6384 | -44.8615 | 2024-10-14 01:05:33 | GOES-16 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 177456fb-277c-330e-a48e-c61d8e054315 | -4.7224 | -46.1608 | 2024-10-14 01:05:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f396a3c7-fbe8-363c-a6f6-a73d3565d1c6 | -4.7226 | -46.1385 | 2024-10-14 01:05:33 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6f8e7aea-3e26-3f25-a9fa-652d90e27dbe | -6.3749 | -59.9936 | 2024-10-14 01:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| fba460bf-3476-3102-8c9c-608d526200a7 | -6.3933 | -59.9929 | 2024-10-14 01:05:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 1a7680b2-dc5b-3a97-b604-341c8f3a8885 | -7.7292 | -43.2049 | 2024-10-14 01:05:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 1a1d2d0d-70ae-374f-b3eb-727019bb92d9 | -7.9625 | -49.0607 | 2024-10-14 01:05:52 | GOES-16 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 157.3 |
| 5158c2ab-ff93-35dc-bb57-8a7faeea2861 | -7.9418 | -63.6365 | 2024-10-14 01:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f8463a81-3a7d-3351-a3af-61facc34363b | -7.9419 | -63.6177 | 2024-10-14 01:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| fdbccc09-253a-3c00-99c7-cecb01ca2ba8 | -7.9603 | -63.6359 | 2024-10-14 01:05:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| bf15b54e-e0a4-3f24-9fae-b3d58f3d69f4 | -7.9604 | -63.6171 | 2024-10-14 01:05:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 6eaffc30-121c-3970-97e4-116f77c685db | -8.4921 | -48.6259 | 2024-10-14 01:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b8568a3a-0f3f-3139-a9e4-9becd36e2a0f | -9.5168 | -35.7636 | 2024-10-14 01:05:59 | GOES-16 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| fca71599-4c04-3e95-8ed2-0b9b594d4e51 | -9.1042 | -61.1811 | 2024-10-14 01:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5f0d4bb3-fd38-3f0a-bdb7-a2ba71250619 | -9.1043 | -61.162 | 2024-10-14 01:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 267c8ec0-39aa-3ab9-a5bc-e867c5416a6a | -9.4888 | -45.8228 | 2024-10-14 01:06:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ec5be5df-b7e7-3b3f-baac-cc96a7200cb9 | -9.8512 | -36.4085 | 2024-10-14 01:06:01 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 70.1 |
| f129b159-9a3f-3783-b585-3137c27ec318 | -9.87 | -36.4321 | 2024-10-14 01:06:01 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| 8a08c9c4-9c2d-3184-abe4-70409ad44a41 | -9.8705 | -36.4052 | 2024-10-14 01:06:01 | GOES-16 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 196.3 |
| 5bd0c8e4-e698-395a-bbc1-12eb56fbe09a | -10.0622 | -44.2391 | 2024-10-14 01:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 213cce7d-47dc-3484-b771-573d15259bf0 | -10.0626 | -44.2158 | 2024-10-14 01:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| afd7e2f3-44de-3a8a-933e-04794cfa9777 | -10.0813 | -44.2366 | 2024-10-14 01:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 1b1d6c07-5bd8-3b40-9d6f-aae9c320c607 | -10.0816 | -44.2133 | 2024-10-14 01:06:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 538a1c8f-04a8-387f-ab9f-d74cd9822812 | -10.0163 | -47.3308 | 2024-10-14 01:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 91080c69-14a9-32f9-9a61-1b628d07ba39 | -10.0166 | -47.3085 | 2024-10-14 01:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 199e4734-64bf-3d06-b13f-917aba7ef35d | -10.0352 | -47.3286 | 2024-10-14 01:06:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 793ad44a-4b69-37c3-a9eb-c4229d4e313b | -10.4918 | -42.433 | 2024-10-14 01:06:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 6bfee79f-deaf-3b0c-90dc-8ba7be7512d5 | -10.9116 | -44.7048 | 2024-10-14 01:06:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9ddd4e2d-606e-373b-9b45-5dcc65b97af6 | -11.17 | -39.9192 | 2024-10-14 01:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 83.4 |
| b0d3f9fb-738c-3fd4-8340-b14ae2b97b1a | -11.1705 | -39.894 | 2024-10-14 01:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 138.6 |
| fbb54540-4d08-307e-ab53-fae206a3f224 | -11.1893 | -39.9159 | 2024-10-14 01:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 100.9 |
| c4d37774-e4be-355f-a5f3-6f06d88542b2 | -11.1898 | -39.8906 | 2024-10-14 01:06:09 | GOES-16 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 208.5 |
| 676f439b-a4ee-376e-bc78-74bfba20c0ad | -12.0912 | -50.7879 | 2024-10-14 01:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 337f55ef-42ac-374d-9f3c-40667497f002 | -12.0915 | -50.7665 | 2024-10-14 01:06:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |


[Clique aqui para ver as próximas entradas](README16.md)
