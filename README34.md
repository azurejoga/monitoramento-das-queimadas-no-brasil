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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed152c51-85c3-3ad3-9792-dd876bd702ad | -13.70425 | -44.27018 | 2024-10-12 03:19:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f37a543c-958c-3f7b-bfd5-12b6f2804227 | -13.70359 | -44.27286 | 2024-10-12 03:19:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50f1e849-e803-3305-ac55-5c77c06afeea | -13.63819 | -41.35787 | 2024-10-12 03:19:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5a369337-62bd-3735-980a-52c44fa454db | -13.46516 | -40.84393 | 2024-10-12 03:19:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 488369e1-4b37-34a8-9607-50a6d533f2c5 | -13.35499 | -43.6685 | 2024-10-12 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a85b6a9-ec0e-3e71-8018-a32048aca65a | -13.35211 | -43.66692 | 2024-10-12 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21830956-aaaa-37e7-9216-27628cd3faaf | -13.35082 | -43.67302 | 2024-10-12 03:19:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1275acd2-e876-348b-8d99-d3ffee0acb76 | -13.03213 | -43.26164 | 2024-10-12 03:19:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9be88c2e-aa7e-3968-b950-9dd94f112f6f | -12.78039 | -38.49903 | 2024-10-12 03:19:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ae19e43c-e069-3eed-881f-cda36e6328a0 | -12.20309 | -38.2476 | 2024-10-12 03:19:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f7d8fce8-496c-361d-803c-f43e6ea9de44 | -2.77 | -51.3829 | 2024-10-12 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c98fbd2d-651d-3bde-b5e7-c945904beff2 | -2.7701 | -51.3622 | 2024-10-12 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 7a7e2ec5-94a2-310a-8679-37845fb9813e | -2.7884 | -51.3825 | 2024-10-12 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 41ac27a7-ff64-39a3-a3d4-5f16014c1834 | -2.7885 | -51.3618 | 2024-10-12 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| b9e63d3c-551a-3303-a439-f8d7a4886d93 | -2.8254 | -51.3401 | 2024-10-12 03:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 7a1cdbde-a7a0-3f6d-a34e-725a03539b09 | -3.6978 | -50.1225 | 2024-10-12 03:25:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 964dce9a-fe10-3439-a80e-16bd24758311 | -3.9394 | -46.445 | 2024-10-12 03:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| e66e3725-5ca6-3ef5-b729-55a43ddc0abb | -3.9396 | -46.4229 | 2024-10-12 03:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 447014d9-eeea-3972-a3be-6f70098a2f65 | -3.958 | -46.4442 | 2024-10-12 03:25:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| a7c156ce-a74d-3f3d-bbf6-2f846b2c2fac | -4.1148 | -48.2515 | 2024-10-12 03:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| c47f0fbe-7a9b-3b72-ac5a-9f5cff868a91 | -4.285 | -50.9586 | 2024-10-12 03:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 84540702-e416-38d5-8e81-9424519d9790 | -5.2486 | -48.0424 | 2024-10-12 03:25:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 23ca45ea-c36b-342c-b80e-8d1fa0763217 | -5.381 | -45.3586 | 2024-10-12 03:25:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 2c492e36-6924-3b9d-8eb4-10e70d7a73a5 | -5.3997 | -45.3574 | 2024-10-12 03:25:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 6e571f85-d100-3bef-91ce-e68b18858a8c | -6.7495 | -58.8817 | 2024-10-12 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 5f24c2d9-89cb-30fe-a0fe-5ae3f625c020 | -6.747 | -59.3259 | 2024-10-12 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 93bb1e57-b63e-316d-849d-0b1c368069f3 | -6.7469 | -59.3452 | 2024-10-12 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 941cd8fe-f0c6-381f-8ab0-8925c1c5d6ec | -7.8529 | -54.7027 | 2024-10-12 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 8c779ea6-a80e-3fe5-93ef-ecffcb0e0be8 | -7.8715 | -54.7016 | 2024-10-12 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| d3702f5a-7daf-3475-b4a2-921d787933fc | -7.8901 | -54.7004 | 2024-10-12 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| de75513d-8f56-3ffe-9ec1-d203e7459b74 | -7.89 | -54.7206 | 2024-10-12 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 2a1b0e83-0020-3802-b4a4-28994023cfda | -7.8717 | -54.6814 | 2024-10-12 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 06fca335-d09b-3a89-b7c7-950894d26e95 | -7.8713 | -54.7217 | 2024-10-12 03:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 8b861670-f8d6-3f94-ab75-48ab82aba35b | -10.4662 | -58.7625 | 2024-10-12 03:26:06 | GOES-16 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 83ab24c1-f1dc-3a09-bdab-1302ac71fcfd | -11.8377 | -58.8445 | 2024-10-12 03:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b64f9497-6b5f-3a57-a02f-065b56d77955 | -12.4558 | -54.576 | 2024-10-12 03:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 97790625-40f6-376e-a49a-b56894207412 | -12.456 | -54.5554 | 2024-10-12 03:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 01b88762-534d-34f8-9a3b-6df67160f8a0 | -12.437 | -54.5573 | 2024-10-12 03:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| fa8ea029-f9c2-352e-bbeb-1e393049ae71 | -12.4367 | -54.5778 | 2024-10-12 03:26:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 08204f7e-3569-38eb-b087-62f9952c85c7 | -12.8896 | -53.4986 | 2024-10-12 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 063c75b9-a681-380d-9cf4-a8177c6d6df6 | -12.8893 | -53.5194 | 2024-10-12 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 9ecbb492-a930-3443-a80c-b4409c2bae35 | -12.8323 | -53.5048 | 2024-10-12 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6984c827-33cf-361c-8fa9-152fb83276f4 | -12.8135 | -53.4861 | 2024-10-12 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9524a1f1-3f15-3571-a1ff-80950115ccd0 | -12.8132 | -53.5069 | 2024-10-12 03:26:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.4 |
| d7b1bd86-0b11-3468-8c22-327a0a0f36e5 | -12.9658 | -53.511 | 2024-10-12 03:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 168.8 |
| d81a3a77-98ec-3616-98e3-cd095e470e4e | -12.9655 | -53.5319 | 2024-10-12 03:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 293.5 |
| 357bd59f-8030-323a-acb5-7c07b39536a9 | -12.9652 | -53.5527 | 2024-10-12 03:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 5f9964f0-3402-311d-be1d-7d36c50d4ee2 | -12.9467 | -53.5131 | 2024-10-12 03:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 59e7ecfb-7805-3c66-b862-5813f7bc5fad | -12.9464 | -53.5339 | 2024-10-12 03:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 290.0 |
| 8c3541cf-8a86-36e0-b39a-dfdf5d6bd056 | -12.9461 | -53.5548 | 2024-10-12 03:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| b99e9149-bf11-3002-a2c0-b43747c75bce | -14.3246 | -57.6002 | 2024-10-12 03:26:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 4aa210f0-f76c-3757-b08a-72fb7f7c7219 | -16.9805 | -57.4404 | 2024-10-12 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| ac0caffc-4650-3838-a0e2-1f9b4a86c32f | -17.1761 | -57.4585 | 2024-10-12 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 97ef46f0-a1ae-3ab1-bfb1-08c960e5a9a1 | -17.1758 | -57.479 | 2024-10-12 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 2c54cf2e-3683-35ba-8afd-675a41048182 | -17.6467 | -56.3292 | 2024-10-12 03:26:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| a2c42d30-29eb-30dd-928b-659043f87e95 | -2.8254 | -51.3401 | 2024-10-12 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 745832db-d5a1-395c-910b-0cb5c0ef4da6 | -2.7885 | -51.3618 | 2024-10-12 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| f10eff3e-1682-315f-b8dc-c883bb27b7b6 | -2.7884 | -51.3825 | 2024-10-12 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 579c5660-ba18-3bc7-b328-6818ffdb5d27 | -2.7701 | -51.3622 | 2024-10-12 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fa39afee-ecb4-3c4a-bf45-6698cea5660b | -3.7163 | -50.1219 | 2024-10-12 03:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 7c334eb6-7437-31a9-b492-c4d676a509df | -3.6978 | -50.1225 | 2024-10-12 03:35:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1f1a2fed-a816-30c4-82b0-a714381d56f2 | -3.9396 | -46.4229 | 2024-10-12 03:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ed97da27-2928-3d9b-a0ee-40fe786523af | -3.9394 | -46.445 | 2024-10-12 03:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 77f9ee54-8118-3935-9b4e-07c57eaa8cf8 | -4.1148 | -48.2515 | 2024-10-12 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a288ba2e-43c5-3875-af94-48b9fadcd434 | -4.2665 | -50.9594 | 2024-10-12 03:35:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 92b9d264-5e99-304a-9590-d3692487d942 | -5.2486 | -48.0424 | 2024-10-12 03:35:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 743899e9-7792-3179-a424-caf908c26703 | -5.3998 | -45.3348 | 2024-10-12 03:35:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| da949d60-4f14-3b76-879e-32e7ab9a02e1 | -5.3997 | -45.3574 | 2024-10-12 03:35:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 333.4 |
| 0877221b-bde7-33cb-8c99-2436ee97270f | -5.3995 | -45.38 | 2024-10-12 03:35:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| de5b5ebc-93d2-34cf-83f3-306e36b2310a | -5.381 | -45.3586 | 2024-10-12 03:35:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ffdcd147-c49a-31ae-b183-ec19035972c7 | -6.0791 | -44.6276 | 2024-10-12 03:35:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| d9a10ac5-72cb-3243-9720-7e0951f89d74 | -6.747 | -59.3259 | 2024-10-12 03:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| a7fb624e-e9e4-32c3-8ba4-7163ea7a7af2 | -6.7469 | -59.3452 | 2024-10-12 03:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 76f4cb91-1073-30a9-9b39-d28c0eae63e4 | -7.8901 | -54.7004 | 2024-10-12 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1994f05c-bb65-3c70-99d6-b55d8385fe02 | -7.89 | -54.7206 | 2024-10-12 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 56e58d83-3725-398c-bdcd-e40591987ec7 | -7.8717 | -54.6814 | 2024-10-12 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0902032b-d165-3c51-810e-85d57295e919 | -7.8715 | -54.7016 | 2024-10-12 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 45ce6ed4-b64b-359d-a002-87206b3d6238 | -7.8713 | -54.7217 | 2024-10-12 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 10b4c1a8-e06f-3a66-9537-0bf646d60acd | -7.8529 | -54.7027 | 2024-10-12 03:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| efbe1126-c0f9-3616-8583-f6980cf9a8bb | -11.8377 | -58.8445 | 2024-10-12 03:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 3e44092f-c58a-3abe-8079-33093c57afa3 | -12.4367 | -54.5778 | 2024-10-12 03:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fb79f280-ac41-3dcd-9dc5-3cf166ab2a81 | -12.8135 | -53.4861 | 2024-10-12 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| e3bfb11a-08fb-3a02-8bee-ec723352e2e4 | -12.8132 | -53.5069 | 2024-10-12 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 23e118e7-8fdd-3c05-a7bf-4e2732ed0b36 | -12.9467 | -53.5131 | 2024-10-12 03:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 949dbb79-bcc0-3a76-9b93-c4c0c8e58fb3 | -12.9464 | -53.5339 | 2024-10-12 03:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 164.2 |
| fa3e22df-820c-32d3-a419-f3df889fcc03 | -12.9461 | -53.5548 | 2024-10-12 03:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 1428d16a-4854-3e94-a885-95016a168760 | -12.9658 | -53.511 | 2024-10-12 03:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 7600010f-0a6d-31f7-b0bd-bfa3ffab5cdc | -12.9655 | -53.5319 | 2024-10-12 03:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| a9e9a685-eb77-3187-859c-5a02e992ca41 | -12.9652 | -53.5527 | 2024-10-12 03:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| bc9d43a9-e8c2-36c5-b2b3-78d09c0ce4b2 | -14.3246 | -57.6002 | 2024-10-12 03:36:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6ef1c258-e0f1-3f71-94a7-4de6a6629c7c | -16.9805 | -57.4404 | 2024-10-12 03:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| e766606f-6215-3f37-b2b1-f8541bac96b4 | -17.1761 | -57.4585 | 2024-10-12 03:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| a8967f75-f615-3be7-8bc2-7fc49fdaa829 | -17.6471 | -56.3084 | 2024-10-12 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.4 |
| 6a00ae9e-7402-3040-b5e7-ed5325c8d290 | -17.6467 | -56.3292 | 2024-10-12 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.9 |
| 4f1664ba-e329-34b4-a4b0-48db381424ff | -17.627 | -56.3318 | 2024-10-12 03:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 3058b1d1-dd34-3378-9681-f2a936a19d34 | -17.964 | -57.3843 | 2024-10-12 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| e9949c20-d128-3596-8e9c-6fd8e96dbf0e | -17.9841 | -57.3612 | 2024-10-12 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| e5f88f80-d036-3f84-94ac-fa9a54db5550 | -17.9837 | -57.3819 | 2024-10-12 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 9e602bcf-4ac7-3411-95f2-7bd065e3fae0 | -17.9643 | -57.3637 | 2024-10-12 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 74f788f4-a6cf-3fc1-821f-27921495d599 | -18.196 | -56.5275 | 2024-10-12 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.6 |


[Clique aqui para ver as próximas entradas](README35.md)
