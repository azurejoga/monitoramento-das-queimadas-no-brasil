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
| 30dbd21e-13ba-3143-8116-eac24e1c8336 | -12.6729 | -45.8052 | 2025-08-19 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 280e3178-d525-38fb-a193-d6f325f5a5e0 | -5.557 | -49.0801 | 2025-08-19 00:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| e7a7d84a-350a-36c0-a7b2-d54f1e8b0f64 | -9.1711 | -59.618 | 2025-08-19 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a40e9ca4-6683-30f0-b22d-b48062c903ba | -5.5785 | -44.0914 | 2025-08-19 00:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 8323c779-154f-3964-abe6-2feb37928389 | -12.9971 | -56.8395 | 2025-08-19 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b0492913-4683-3ac5-a60b-dad59e41f853 | -5.7887 | -43.6134 | 2025-08-19 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2efb921f-09b2-3875-9154-5a3eca567fa9 | -9.1895 | -59.6364 | 2025-08-19 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 6f96eff9-6f97-3a7e-9273-88fae7578a5d | -12.6536 | -45.8082 | 2025-08-19 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 272.9 |
| f611cee1-f37e-3606-b4fa-f4e536633c8b | -5.8807 | -48.1125 | 2025-08-19 00:20:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e2e8f40f-116c-323d-82c9-9e0abe2e206a | -13.0162 | -56.8378 | 2025-08-19 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fbc4434d-f623-35b2-b81d-d5153872f498 | -6.9524 | -43.6083 | 2025-08-19 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| fe273f7e-a73f-3ee3-b7c0-f225ab230998 | -11.7488 | -58.3187 | 2025-08-19 00:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 8e496be4-921a-362d-a64a-2262db2aae7c | -16.4659 | -45.098 | 2025-08-19 00:20:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 112.5 |
| e4b1a5d1-0602-37ca-974b-99a2fcf0d961 | -11.8705 | -51.5569 | 2025-08-19 00:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 5c933461-2361-3723-9fbc-829e0b08ecf8 | -11.8512 | -51.5801 | 2025-08-19 00:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| a31ea07c-b050-327c-bb75-c79265d2051f | -12.9778 | -56.8614 | 2025-08-19 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 1c9541fa-b4ce-3416-88ac-a7214b123137 | -11.8705 | -51.5569 | 2025-08-19 00:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 44c751b8-5d39-3dcd-a979-83006f6750ef | -3.982 | -42.516 | 2025-08-19 00:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 365.9 |
| c7a1269d-62d6-3f85-9de5-0c56e92bb67d | -5.8807 | -48.1125 | 2025-08-19 00:30:00 | GOES-19 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 08a1e046-967e-3b8a-b2d6-d56eb71537b3 | -6.9712 | -43.6066 | 2025-08-19 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| e1c4759b-ac61-37c5-91a9-8ac414ce1254 | -12.6532 | -45.8312 | 2025-08-19 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 0764618e-c68c-3eba-839e-3a9df181833e | -13.1746 | -54.9337 | 2025-08-19 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| be218cfd-5c67-3bec-b257-453c8adc6188 | -6.9524 | -43.6083 | 2025-08-19 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 08c2180d-a7b7-3332-9647-87e359dcf24c | -11.7488 | -58.3187 | 2025-08-19 00:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 4a615ce4-369f-3b56-bb93-70cc1fb16824 | -9.1708 | -59.6568 | 2025-08-19 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6181640b-4e1f-3f77-b6bd-dfbe1acdbd70 | -16.4863 | -45.0702 | 2025-08-19 00:30:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 88.7 |
| f397fc90-057a-3b44-b9be-24f785930c1c | -15.0389 | -54.8089 | 2025-08-19 00:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 249d7993-b6bd-3bc8-9db1-9920a7e0e735 | -15.0006 | -54.7928 | 2025-08-19 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 96ec0c79-7783-3f1c-96f6-a3d2b99556e1 | -4.0007 | -42.5149 | 2025-08-19 00:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| f4a4a0e8-1336-330c-8ddb-6c0047015122 | -9.1895 | -59.6364 | 2025-08-19 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 4fe7bdf1-6882-3836-8f20-5eb2046f20d6 | -5.7887 | -43.6134 | 2025-08-19 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8a3542e2-efd8-3bce-81a7-e8512fe74e33 | -6.9339 | -43.5868 | 2025-08-19 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e2561476-32f9-3faa-a8df-75080b49bc3e | -12.9778 | -56.8614 | 2025-08-19 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 0b5f821e-5600-3e1b-a443-65a07b5e86ad | -9.1709 | -59.6374 | 2025-08-19 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 24f0d1f2-2dd8-33c1-9516-a4c637229ef7 | -5.5785 | -44.0914 | 2025-08-19 00:30:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| a4e248ac-50cc-3deb-a6de-a2a66fcae910 | -6.9336 | -43.6101 | 2025-08-19 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| d504de62-a705-3560-b2ec-94bc2922ac07 | -11.8702 | -51.578 | 2025-08-19 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 175.5 |
| fae9e6e3-0141-36cb-9303-6d10a46c6c7b | -16.4857 | -45.0939 | 2025-08-19 00:30:00 | GOES-19 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 151.1 |
| d5a6ee67-1a70-346d-9f0c-fa11035a9474 | -9.1894 | -59.6558 | 2025-08-19 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3599fe75-4eb1-365e-9a8a-0f97ac661073 | -16.4659 | -45.098 | 2025-08-19 00:30:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4d0dd28e-8be1-35c8-ab4d-2840852b692c | -12.6536 | -45.8082 | 2025-08-19 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| b5823f94-2539-334b-b49c-7cd585ce9788 | -6.9527 | -43.585 | 2025-08-19 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 034797b9-7882-3762-85d0-3f626fa96263 | -7.7807 | -66.9577 | 2025-08-19 00:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 1541b1c4-a46b-356b-bc40-c61a6a61c143 | -7.2602 | -50.1613 | 2025-08-19 00:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| fcfccbac-02a2-3624-9a16-46dfa853cc41 | -3.9819 | -42.5396 | 2025-08-19 00:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 679639a8-559f-341e-be40-c0fb44274648 | -3.9633 | -42.517 | 2025-08-19 00:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| c60c7848-35e4-3738-ac64-50f1486a48e6 | -13.0162 | -56.8378 | 2025-08-19 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 55685ac1-9d05-363e-ab03-cea29310ece0 | -6.9715 | -43.5833 | 2025-08-19 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.7 |
| cb476f9c-7de2-3a41-95aa-133f03d83b74 | -8.9788 | -60.4964 | 2025-08-19 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 902dc07d-b9e2-3bfd-8d9d-6dac42531429 | -5.5787 | -44.0684 | 2025-08-19 00:30:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ea8e88cd-b2bf-34b9-bcd7-e5717e4521b7 | -15.4047 | -49.5733 | 2025-08-19 00:30:00 | GOES-19 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ad00b7d3-7b36-3f13-aeb6-a82ee37a0f5b | -11.8512 | -51.5801 | 2025-08-19 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 091f9c09-d193-3bbb-a46e-f8d8f61fa743 | -14.9812 | -54.7951 | 2025-08-19 00:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 509285cb-bebb-3d77-af0e-90e2dc9616eb | -11.8515 | -51.559 | 2025-08-19 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2f484f07-d89d-3d73-b81a-caf046429c4f | -9.5351 | -63.5771 | 2025-08-19 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| bf6cf4f1-647a-30f5-bd09-e8dae480f4f4 | -15.0349 | -54.818802 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4eb6ee3-0ee0-36ff-a709-76ad319e06a3 | -15.4108 | -49.583801 | 2025-08-19 00:34:00 | METOP-C | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ea2ecee-a86e-3831-8b68-6d87af96d64c | -6.9277 | -43.595299 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a533ea1e-fa77-37b5-a756-aec2a30ae15f | -2.9122 | -48.291302 | 2025-08-19 00:34:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70bf4317-7c1b-323f-8edf-9f8ae6377501 | -4.4315 | -47.764702 | 2025-08-19 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 421a55b8-d111-3abf-9221-0cc7961428c1 | -4.1494 | -46.451401 | 2025-08-19 00:34:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9a0fbd95-4fea-3b04-8c8a-1c58f409818d | -7.2647 | -50.178101 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 664e15f1-c51b-3ca9-8ca7-d284620d3a60 | -7.2728 | -50.168098 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc8b54a6-9ad5-3a12-971c-0635796ed966 | -3.9779 | -42.5098 | 2025-08-19 00:34:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 241b7d07-c477-39e3-b84c-bfa9eaa1c85a | -11.4557 | -47.327301 | 2025-08-19 00:34:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08105e2b-34a6-3544-83f9-7715ed3a5018 | -9.1678 | -40.609402 | 2025-08-19 00:34:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 59b89edd-0e42-35ab-8054-9aba4ddb71eb | -12.5022 | -45.573101 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd8101c8-7fbc-3f0c-8843-3f38b2a9c39b | -5.9766 | -44.287201 | 2025-08-19 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d0a75ac-fa7a-36e5-af1f-171dccc9c407 | -15.0446 | -54.817001 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8b79ad18-0f36-3b08-8b8b-2ab85bc81890 | -7.2549 | -50.180302 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f16962a7-5067-395c-a91f-49309191342e | -13.0039 | -45.195202 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e296dc07-338a-37c4-8d3d-1c90d106c7f6 | -5.7495 | -46.6772 | 2025-08-19 00:34:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db37e162-19c4-3958-bcb9-51fca51bb620 | -7.2189 | -49.603401 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55b05559-ce38-3787-b7cb-18775edbd82c | -5.5443 | -49.072102 | 2025-08-19 00:34:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ff68c7-9b9f-346f-9d62-43480c279c2b | -11.8513 | -51.582001 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e6f4e53e-36fc-3b16-b156-e10fda3c7d13 | -11.849 | -51.571098 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 346eeecf-41a2-3f48-8eca-0ed26bf6c65f | -12.6577 | -45.802399 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c03b628-6b7f-357c-945d-3e8a3ba6fbde | -12.985 | -56.857101 | 2025-08-19 00:34:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 669c6cdf-3adc-3ab5-85ff-541a7c5955ec | -4.4299 | -47.7579 | 2025-08-19 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3072f27-66c8-3dc2-afd9-046358a881bc | -14.9923 | -54.806099 | 2025-08-19 00:34:00 | METOP-C | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c29d2027-861c-3512-b603-55e7c474ae2f | -13.2513 | -50.800999 | 2025-08-19 00:34:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47f76ce2-6de8-3ae5-b054-f4af82551de0 | -3.9709 | -42.523499 | 2025-08-19 00:34:00 | METOP-C | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 64dcac53-6378-35b6-9ef0-bcc0ab2ab306 | -13.596 | -46.998501 | 2025-08-19 00:34:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d19c830a-f314-357d-82cd-e4635c00db9a | -5.5809 | -44.097401 | 2025-08-19 00:34:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dbd53536-2479-3b84-9c44-1d0a75596427 | -6.9558 | -43.626598 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1d500e23-3a25-308a-9dfd-2f309429a203 | -3.4601 | -48.9725 | 2025-08-19 00:34:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc8b2385-fa43-3bb1-87c3-6ef23bf6edc4 | -7.271 | -50.160099 | 2025-08-19 00:34:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17f9c007-d551-3cc7-a144-1c8dc8b0c77c | -7.3003 | -46.287201 | 2025-08-19 00:34:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0232f18-ded1-362d-b0f7-4dc472e4fcee | -14.5051 | -45.947899 | 2025-08-19 00:34:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 408d28fb-2c97-3440-914f-1fa14d1f51dc | -11.8709 | -51.577999 | 2025-08-19 00:34:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ac6d0a56-a1e1-3bcd-9947-465bb8263316 | -6.9375 | -43.592999 | 2025-08-19 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40e0a14d-a2bc-3d9f-8aad-df815d854a90 | -3.9865 | -47.893299 | 2025-08-19 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007909fb-07b2-3e0e-a33c-f5785829da82 | -9.1775 | -40.606998 | 2025-08-19 00:34:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 02a393e1-04ae-3950-b080-638f4014da2f | -5.5789 | -44.088699 | 2025-08-19 00:34:00 | METOP-C | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fde4dc8e-d64e-3ca5-b050-3d279cba0ce5 | -12.6609 | -45.816399 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c10c7afd-0a08-371d-82f5-1458c397fcba | -5.79 | -43.890202 | 2025-08-19 00:34:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c760845d-a277-3b82-9904-60df9a732b47 | -7.3101 | -46.285 | 2025-08-19 00:34:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 557ffefd-8bff-33a4-8212-a96814cd49f1 | -14.8685 | -48.075199 | 2025-08-19 00:34:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1164fd9-c8ed-38bb-ae0e-49908165b836 | -12.9958 | -45.2047 | 2025-08-19 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 231e1139-e24a-349f-b5be-9aa9f4b1f4e8 | -5.5525 | -49.062801 | 2025-08-19 00:34:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
