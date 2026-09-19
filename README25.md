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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e0a4ec2-8cb6-38ed-9573-95aefa43b549 | -18.0269 | -51.093 | 2026-09-19 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 75d0bee9-1c40-351d-aaad-77c8dae209d7 | -18.0274 | -51.0709 | 2026-09-19 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 51ade76d-2db3-3602-b0aa-ef24c0e6bdaf | -18.0074 | -51.0744 | 2026-09-19 02:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d143b86c-d41d-3a4f-b5c8-01862429c075 | -3.2313 | -46.9596 | 2026-09-19 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| dcd2424b-2cef-3f50-b7b0-0b585457ace9 | -2.8101 | -50.4658 | 2026-09-19 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 1b76a62d-23fa-3052-944b-3c77e60eb586 | -12.7089 | -45.937 | 2026-09-19 02:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 02d1825d-e988-3b4e-b4ab-69578247547f | -18.0278 | -51.0489 | 2026-09-19 02:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| b0cc1e6d-e44f-331e-b65e-581f241373bc | -18.0074 | -51.0744 | 2026-09-19 02:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ee7ab4d6-3788-36d7-b354-91c55e27ee35 | -3.3494 | -59.8097 | 2026-09-19 02:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| d2ae78f9-fc63-3d8b-aab9-de46005ecf13 | -8.776 | -46.9088 | 2026-09-19 02:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| a85aae54-43dc-36c7-bf21-cc2236e9f35c | -3.3311 | -59.8101 | 2026-09-19 02:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5c40839f-d907-33a9-881c-e0a27a6c64f3 | -18.0274 | -51.0709 | 2026-09-19 02:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 11da14ee-a577-3f72-b8ef-54ed2db58f01 | -16.7951 | -46.9879 | 2026-09-19 02:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 2b26846a-757f-31a7-98a5-b36aeb745157 | -2.8285 | -50.4653 | 2026-09-19 02:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| d2f1dc71-cecd-376d-a41a-ca2cf2fcb171 | -18.0269 | -51.093 | 2026-09-19 02:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a214a14d-559c-3b76-9c36-5f7afa2504e1 | -3.2314 | -46.9376 | 2026-09-19 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fb4a3af6-3971-3da6-8176-040447f85277 | -3.7333 | -54.6499 | 2026-09-19 02:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0f69c94c-34e8-312d-9356-27cc9d6b6651 | -3.2313 | -46.9596 | 2026-09-19 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d4de6423-a1a0-3722-a05e-715592255175 | -10.7115 | -60.7312 | 2026-09-19 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 7a47e600-aea5-3d7d-b36d-58b58103c125 | -10.6928 | -60.7322 | 2026-09-19 02:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 31fe83ef-81f7-3e01-8c43-a3e794d93350 | -3.3311 | -59.8101 | 2026-09-19 02:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c5273633-fa79-3732-8e9c-914f2acf1afb | -2.8101 | -50.4658 | 2026-09-19 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 143e6157-da74-39e2-914a-22ea456491f0 | -7.7626 | -46.7612 | 2026-09-19 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ff0c58de-a36e-3556-9193-60098110f8f3 | -2.8284 | -50.4863 | 2026-09-19 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 640887b1-5f39-3c28-b7d3-e3a21af467d5 | -16.7951 | -46.9879 | 2026-09-19 02:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 3710c155-31ba-3491-a7b7-8e5b561e58f8 | -10.6928 | -60.7322 | 2026-09-19 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 7dece001-871e-39ff-a45e-4723f901ea28 | -18.0274 | -51.0709 | 2026-09-19 02:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 66.2 |
| ea78d1d4-8e89-3146-9de4-748fa4ffe5f0 | -3.2313 | -46.9596 | 2026-09-19 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| cebf2983-1074-3dc5-b420-b4b7276b363f | -7.7629 | -46.7389 | 2026-09-19 02:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c023ce2e-a3a9-3608-b353-c8c0830be11f | -10.7115 | -60.7312 | 2026-09-19 02:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| ba00a36e-8f78-3b84-bbe7-f1c83e969c2e | -2.8285 | -50.4653 | 2026-09-19 02:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 127fb9b2-800e-3e70-ad8d-2853278074b1 | -3.2314 | -46.9376 | 2026-09-19 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7b478c8e-a16d-30ec-8c62-571018ce7248 | -7.48292 | -35.27698 | 2026-09-19 02:58:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e6d3f0c-f7f8-3026-be94-a98f90400ffa | -7.47678 | -35.27929 | 2026-09-19 02:58:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f7d680be-4821-30a1-a3bf-a55723c165f4 | -7.48396 | -35.28079 | 2026-09-19 02:58:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a3d1c6cc-ff4e-35c3-b636-d1a1fd4b13fa | -3.7333 | -54.6499 | 2026-09-19 03:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 8e4f448d-21cd-3f15-980e-ce3b65eea1a1 | -2.8285 | -50.4653 | 2026-09-19 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 1efd062e-22a0-325f-9527-7eee59565374 | -2.8284 | -50.4863 | 2026-09-19 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f333a6d6-d679-32b0-b146-d801b7c47ba2 | -10.7115 | -60.7312 | 2026-09-19 03:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 79d6ad08-add8-31f2-aa85-f15efa868c30 | -3.2314 | -46.9376 | 2026-09-19 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| b4a0e867-15d4-3a14-a4ee-e672af096bb6 | -2.8101 | -50.4658 | 2026-09-19 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c571d0a6-08a7-3cb8-974c-f8751cafc1b9 | -3.2313 | -46.9596 | 2026-09-19 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2900dff1-1d03-3d6d-a1d8-ba1481112241 | -2.8285 | -50.4653 | 2026-09-19 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| fd94eac7-f674-3796-bde0-660a277ddba1 | -2.8101 | -50.4658 | 2026-09-19 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c4216fcd-354f-3c9a-b81d-d5b72a8cd15f | -3.2313 | -46.9596 | 2026-09-19 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 12181cab-c44a-3b76-bf78-6e902ac62cf4 | -2.8284 | -50.4863 | 2026-09-19 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 74b0fa68-7dd6-3522-839c-9a3f1fea56af | -10.7115 | -60.7312 | 2026-09-19 03:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| b212d199-dfbb-36d4-a08f-4be4871b65b2 | -11.22017 | -42.83713 | 2026-09-19 03:17:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 43ec9309-8ed3-3c64-a83f-fb3579c69e7e | -11.52122 | -39.0914 | 2026-09-19 03:17:00 | NOAA-20 | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5a78a4b-850f-3eaa-bd55-5b4359489cb7 | -11.2217 | -42.82984 | 2026-09-19 03:17:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ffcb2987-6732-34b8-96f0-4684fd408963 | -6.57224 | -35.1846 | 2026-09-19 03:17:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 21a9142e-84b5-3da2-9f97-dae60742e63d | -5.60945 | -37.53175 | 2026-09-19 03:17:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d77e4761-8a3a-3ab6-ba7b-c2558c93b733 | -7.48016 | -35.27727 | 2026-09-19 03:19:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| abe49b01-9371-3dd5-af9e-165e0a3cadf0 | -3.2313 | -46.9596 | 2026-09-19 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| fa809fea-a19b-3a29-8379-926b3588415b | -7.7626 | -46.7612 | 2026-09-19 03:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| ca5f31a9-e306-38be-8478-15684f441977 | -12.5952 | -49.1046 | 2026-09-19 03:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 0a13cd07-da40-32d0-821a-49166e2cf9d3 | -2.8101 | -50.4658 | 2026-09-19 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 06e95c47-80ab-3511-971b-bd636b6cd596 | -2.8284 | -50.4863 | 2026-09-19 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| edcf470b-92b4-3372-abe7-07e7aecb32a2 | -10.7115 | -60.7312 | 2026-09-19 03:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| b6d6c8b1-7121-3fa5-9387-a55d81407a5e | -2.8285 | -50.4653 | 2026-09-19 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 2edf602c-da06-3df9-81bc-4a04c8eec0f5 | -20.00316 | -44.07956 | 2026-09-19 03:21:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aa642abf-2b77-3273-8f21-5e152a04ef40 | -12.5952 | -49.1046 | 2026-09-19 03:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6b38a1b5-5942-3b7c-8c1d-1bb893637202 | -2.8284 | -50.4863 | 2026-09-19 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 37c0d14e-e014-311e-afba-bf2d95095596 | -2.8285 | -50.4653 | 2026-09-19 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 6b49c138-94b9-3ef8-8b48-6e5927534b60 | -10.7115 | -60.7312 | 2026-09-19 03:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 83a4b3b0-0a43-31ae-8efe-bf0d9a046c00 | -12.5952 | -49.1046 | 2026-09-19 03:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 460f9e80-1823-34b1-afd5-f01f425b82bb | -7.7626 | -46.7612 | 2026-09-19 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 63f4e6dc-fee4-3093-9043-1000d17f39c9 | -20.9166 | -49.0607 | 2026-09-19 03:40:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.0 |
| 79351ad3-d426-3456-8b9d-de7a8e2fae48 | -10.7115 | -60.7312 | 2026-09-19 03:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1391778c-f242-3521-ad12-e3fbe0c86a54 | -10.6928 | -60.7322 | 2026-09-19 03:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 13c2044a-3c0d-3653-9bac-19677c55a093 | -12.2883 | -49.1664 | 2026-09-19 03:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 16f02b11-4840-366f-b3b2-17a90e01cc90 | -10.7115 | -60.7312 | 2026-09-19 03:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 86e0073b-34f2-3280-b712-e51320bac254 | -12.5952 | -49.1046 | 2026-09-19 03:50:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3d82b8d7-05b0-3c3d-bfc2-e453cceff3cd | -18.0274 | -51.0709 | 2026-09-19 04:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| be0fe3f9-9aee-3821-adb4-bc16eb7e899e | -20.9796 | -49.0006 | 2026-09-19 04:00:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 4f9771a5-cd23-3881-a848-2c347fd8fa5a | -13.0164 | -46.9804 | 2026-09-19 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| f1fd6978-431b-3657-9cf6-3ec3b8dfd6e3 | -10.6928 | -60.7322 | 2026-09-19 04:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ed129062-6ee4-39bf-8fed-0c7c85e45fb9 | -10.7115 | -60.7312 | 2026-09-19 04:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6cece5c4-a37d-3e23-8962-cd35007f53bc | -14.6861 | -46.6657 | 2026-09-19 04:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| e20ce03b-6fe2-3874-a631-5b90180ae84c | -20.9802 | -48.9774 | 2026-09-19 04:00:00 | GOES-19 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| d91869c5-6018-311b-9840-f49eab9dfd72 | 1.26109 | -50.74816 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08516d15-c714-36db-bbf6-e37d229b5bfb | -3.23986 | -43.22411 | 2026-09-19 04:00:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ab8cdfb-b0c9-330d-bfca-2b1e91a0b193 | -2.14608 | -50.90102 | 2026-09-19 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a71016a1-d506-3459-a97e-835bf07aa338 | -2.89481 | -40.03635 | 2026-09-19 04:00:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c01f9080-e828-326d-923e-2e14b4da447d | 1.21586 | -51.0071 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d96c866f-067c-3229-a4b7-9d65f60687b0 | -1.62179 | -48.28743 | 2026-09-19 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 915c98c4-4acd-3182-9d5f-687aba4ae548 | -2.14267 | -50.90238 | 2026-09-19 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a5a23d5-15e2-3930-8bb6-e3048b875ee6 | -2.29035 | -47.88557 | 2026-09-19 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 966d8a3f-1f12-3517-a528-a18ddaaf733e | 1.21369 | -51.01165 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d422f04e-45fd-32ce-905a-cd00abdd6c17 | -2.39168 | -48.52822 | 2026-09-19 04:00:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2170df53-5eae-3009-9c0c-5933126cdb40 | -1.21921 | -47.71309 | 2026-09-19 04:00:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d0b7474-7921-3ac8-975a-fdc388ebfab8 | 1.25428 | -50.75396 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60612bb6-9f42-3b44-aef0-1fd844019cad | -2.29085 | -47.88247 | 2026-09-19 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 069d0c5e-284f-30ff-9534-07e19198301b | 1.22616 | -51.00394 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08cb7987-9077-36a5-a2a2-82fc55526924 | -2.29219 | -47.88375 | 2026-09-19 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa02690e-837a-3327-ba31-e7fb1764a16e | -2.29602 | -47.88332 | 2026-09-19 04:00:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b981274-ec59-3072-9ef6-d5d161841286 | -2.03376 | -48.78139 | 2026-09-19 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acd99b6d-2b42-3de8-af23-c4e66cd976be | 1.22527 | -50.99813 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52e1d4e5-2d42-35fd-8805-aa2c395d78a3 | 1.2554 | -50.75477 | 2026-09-19 04:00:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48b2414a-db28-31ab-b20e-d88783c17963 | -1.09464 | -48.06103 | 2026-09-19 04:00:00 | NOAA-21 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README26.md)
