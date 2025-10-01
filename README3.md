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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d85aa89-72fe-3ef4-bdf1-b26399cb475b | -11.8246 | -44.9669 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| c6d55585-f57c-3fc6-8b94-21b14a840720 | -9.9193 | -43.6508 | 2025-10-01 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b4671e85-25d7-32d1-bd28-2a0b6b39e0ff | -13.3467 | -47.8508 | 2025-10-01 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 5275b2f1-cdcf-3e33-9ffa-5f2ff6bd8352 | -22.6279 | -49.0535 | 2025-10-01 00:30:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 622e5040-4b72-354c-89e7-d4f8642fbdb7 | -20.6309 | -46.2046 | 2025-10-01 00:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 237a9ee8-ac45-3beb-acb9-646604aa796c | -9.4394 | -54.5739 | 2025-10-01 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| eeb149cd-562d-3dd4-80ca-f0725f50488f | -10.9769 | -46.5443 | 2025-10-01 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 3db2b782-578d-3e71-89a3-69f4ab662ea6 | -13.7687 | -47.9659 | 2025-10-01 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 9c541db3-92c2-381a-a0e2-21f3b0cc822e | -9.9189 | -43.6743 | 2025-10-01 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 253.2 |
| df2fd53d-b498-38a5-a829-d5d062b4bba5 | -9.9186 | -43.6978 | 2025-10-01 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 02104d77-27b6-30cd-a2d2-541732c0518a | -16.2959 | -47.2667 | 2025-10-01 00:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 4afb1b1d-fe21-3280-94b0-7b4e304beee2 | -9.938 | -43.6718 | 2025-10-01 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 353.7 |
| 382524e5-cab6-3d37-8023-200482fddb8f | -11.4049 | -44.8895 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| f7205c3a-90cb-383f-b8f7-dd84e88908bc | -13.2973 | -50.6605 | 2025-10-01 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 65bbe6ba-39e3-3946-83e8-219a1f5b0343 | -10.1081 | -50.3203 | 2025-10-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d3b5444c-dad6-3ac3-862b-32265bf670c4 | -3.4577 | -50.089 | 2025-10-01 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1ff688a6-9025-37a7-9efb-4693fe77bfb4 | -13.7881 | -47.9629 | 2025-10-01 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 087468d7-c31a-3a62-91e4-c3075cfa3158 | -3.1013 | -47.0082 | 2025-10-01 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 2e6e0bf9-6f08-36b2-a2eb-0b6104c7ed25 | -11.8054 | -44.9697 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 870f0691-690d-35f2-90fd-31b05609bcd2 | -11.8242 | -44.9901 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| f5dd8c6a-3dfe-3d9d-abf6-b484b3d120a1 | -3.5161 | -49.4528 | 2025-10-01 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| d9b810d0-41e8-3b8d-a7cd-ba7a50691f9c | -13.3471 | -47.8284 | 2025-10-01 00:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.2 |
| d2f119e9-d3ab-3b0d-9753-0648d8acf3fa | -10.8429 | -45.4044 | 2025-10-01 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 023cb4c7-4922-3c5a-8277-2e5bb80c6fc9 | -3.5162 | -49.4315 | 2025-10-01 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 357a03d0-7fe3-3b4d-8af3-4823b32da757 | -10.0145 | -50.2657 | 2025-10-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a4c0ec2c-b676-3fee-8335-9c22c506051c | -9.4396 | -54.5537 | 2025-10-01 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ac6c81c8-123d-36af-b244-a8839ada93bb | -20.6316 | -46.1806 | 2025-10-01 00:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 88.2 |
| a99783b7-d181-323b-9311-7f94d50b020e | -15.2464 | -48.7352 | 2025-10-01 00:30:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 5b2d4c8f-7139-3dea-af62-e4a0403e699d | -10.9773 | -46.5217 | 2025-10-01 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| cd597526-316f-34fa-ab16-3c9dd70f770e | -21.0365 | -45.6693 | 2025-10-01 00:30:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 483086d5-30c7-3e65-bbe0-b1bd5ab63e35 | -9.9383 | -43.6483 | 2025-10-01 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 266.9 |
| 2b7fff1c-e9f8-330c-9b76-96be97a9ccd4 | -20.5998 | -45.878 | 2025-10-01 00:30:00 | GOES-19 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f744e003-f2d6-3505-908a-b66ec3c958b0 | -10.0334 | -50.2638 | 2025-10-01 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| cc93ed42-4966-3419-858e-16b71a007b2d | -14.3652 | -47.1518 | 2025-10-01 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1d6ca2d1-8a94-3491-8ead-ec25881e3db0 | -14.3657 | -47.1291 | 2025-10-01 00:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b2e6823a-ba3e-32ee-903c-7ff5d449545d | -20.611 | -46.1858 | 2025-10-01 00:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 34e24718-53fb-36d7-8777-ce278896fd0f | -16.2562 | -50.9275 | 2025-10-01 00:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 5653651a-7b88-3306-91b3-af4b528718f0 | -11.8438 | -44.964 | 2025-10-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 4fc11c20-2efc-3cc0-816c-87f12c797f82 | -12.8202 | -50.5495 | 2025-10-01 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 5af25306-9541-3492-9302-a0570719088a | -21.0572 | -45.6638 | 2025-10-01 00:40:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b29315a4-8ae8-3885-b35b-59cfe2190b43 | -15.9431 | -48.1245 | 2025-10-01 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 8bde244a-a0b9-365b-a303-9337361917e5 | -9.2902 | -54.5242 | 2025-10-01 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 892a649f-1c81-3a93-a34f-8495accdf363 | -5.8657 | -43.3981 | 2025-10-01 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 37b1bba9-3ed1-3eb9-8222-a25069f72064 | -13.9823 | -45.0347 | 2025-10-01 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 2e4a7ed0-82c6-3aff-8c24-51c0177b1402 | -20.5998 | -45.878 | 2025-10-01 00:40:00 | GOES-19 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 723edfa4-7e0a-3a6f-a7a2-53a9c940590d | -14.7826 | -45.7981 | 2025-10-01 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.0 |
| f361f6f5-1248-33c9-aa69-d322400a3b59 | -3.5161 | -49.4528 | 2025-10-01 00:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| da3f3a80-36a4-3eb3-8b5a-5aa4fb09a080 | -12.8198 | -50.571 | 2025-10-01 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c8e0730d-77c8-39ad-80e1-4887d460915a | -9.0821 | -48.0252 | 2025-10-01 00:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d96e7f37-982c-3698-b1f6-3f3c6bdc8751 | -14.7831 | -45.7749 | 2025-10-01 00:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e8a76d43-0dea-3167-af09-709d552e318f | -20.6103 | -46.2098 | 2025-10-01 00:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| de4bd81d-ba51-315c-ad71-12e9ae98fde9 | -11.8242 | -44.9901 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 303.8 |
| f69be70e-1bca-36ca-b63f-fd3c0a5992e7 | -13.1774 | -50.9549 | 2025-10-01 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 6755aef4-ff6e-3c05-9958-f9bcaedf438c | -11.4049 | -44.8895 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 55b15933-614e-3e0a-8024-54f22d95c59b | -11.8054 | -44.9697 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 81433c88-bef6-3ca3-97c2-192f2e2ee5df | -5.8469 | -43.3995 | 2025-10-01 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 897437c5-625e-398b-af82-dc1964926765 | -11.8246 | -44.9669 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 295.8 |
| e4ec62e4-7f25-37ac-813c-489198632b38 | -20.6316 | -46.1806 | 2025-10-01 00:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 28dd3932-f3ae-3885-84d5-00e068ad942f | -6.949 | -63.1048 | 2025-10-01 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e8080e28-8cce-3303-960d-4946f4448ad0 | -14.3519 | -45.9206 | 2025-10-01 00:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 9049e326-c4d7-3805-a6a9-b1d49c3b7569 | -14.9914 | -46.9549 | 2025-10-01 00:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| be220b8e-9ebe-3bd3-8067-4346c6bea2bf | -11.3858 | -44.8923 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1a2f11de-5402-3910-8954-502e0f001dd0 | -11.805 | -44.9929 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| f67682d7-47d9-3804-9393-ce4a7f7352d5 | -21.0365 | -45.6693 | 2025-10-01 00:40:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 86090fad-4331-36d3-80dd-c92530740884 | -9.3089 | -54.5229 | 2025-10-01 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1ade1ba8-a48d-3fb0-8423-150698e0cde6 | -15.9234 | -48.1279 | 2025-10-01 00:40:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 43.5 |
| fe2120ff-86b7-3521-9b75-ad7586c1cbc6 | -13.3467 | -47.8508 | 2025-10-01 00:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 597948dc-ae55-3380-a365-67235e7cdae8 | -16.2366 | -50.9306 | 2025-10-01 00:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 738afc40-78cb-3352-923b-fdfd449a4cf7 | -14.7137 | -48.1525 | 2025-10-01 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5bf70fe6-9540-35aa-beec-4cfea9b59221 | -3.1012 | -47.0301 | 2025-10-01 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bddd5b3c-10ab-3f2e-9a7a-1319f5d014e5 | -10.862 | -45.4019 | 2025-10-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7e935678-84a2-3ac2-a332-c878c84bad57 | -16.0225 | -50.8771 | 2025-10-01 00:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 6db4eaf7-d290-381c-a284-e9ad5b59b6cc | -16.2562 | -50.9275 | 2025-10-01 00:40:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 61d545ec-09e1-3d2a-a552-d05c34ed7360 | -8.559 | -44.7184 | 2025-10-01 00:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f5dd7eeb-68a6-367d-85af-b3cb660af823 | -14.4041 | -46.2106 | 2025-10-01 00:40:00 | GOES-19 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| fc776d19-1368-39de-a629-ea4987fa129b | -13.3471 | -47.8284 | 2025-10-01 00:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d9a13ef0-b5aa-3b83-8a7d-16403a9b5f9d | -20.6309 | -46.2046 | 2025-10-01 00:40:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 28349878-6fe2-340b-a902-331b7ac8cad9 | -3.4577 | -50.089 | 2025-10-01 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 42f2b1f3-72b4-3456-a4d1-9193e3b49799 | -10.8429 | -45.4044 | 2025-10-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.0 |
| a6887129-dd63-39f1-b818-959cc5b5ba18 | -10.8238 | -45.407 | 2025-10-01 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 863d9b38-05a8-32ad-b489-cb8509610c3a | -3.1013 | -47.0082 | 2025-10-01 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 182.7 |
| 9db2d13d-f32e-3f45-a394-cb0914bb245e | -13.1966 | -50.9525 | 2025-10-01 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| fb263b54-0aea-3b71-a5b0-237d4da64c55 | -14.3524 | -45.8974 | 2025-10-01 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 30358589-4900-3b27-bac0-fd7f22ef00fd | -11.8438 | -44.964 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 225.0 |
| e0fb58bd-9ace-3089-ab24-cc84b52e6c07 | -3.0827 | -47.0088 | 2025-10-01 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 334dc29d-e14f-3687-b062-f627191ae61b | -11.8434 | -44.9872 | 2025-10-01 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 283.7 |
| 715f7114-f2ac-3cec-bffd-aeaabc8be04a | -13.9818 | -45.0581 | 2025-10-01 00:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 64bf5890-b887-392e-849b-7803ac741c9e | -6.949 | -63.1048 | 2025-10-01 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| cec2a6e5-5f08-3f44-a4cf-bb3c9f1a5b82 | -13.3467 | -47.8508 | 2025-10-01 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f0b9dab9-8dac-36a9-a1cc-43811e7136ca | -10.8429 | -45.4044 | 2025-10-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 1e81c2d1-8d19-3567-8f1c-9235af06b521 | -10.862 | -45.4019 | 2025-10-01 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 0ac58353-d399-30e7-9644-0e9765b07895 | -3.1012 | -47.0301 | 2025-10-01 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 0d543b5d-f6ce-3891-b479-1748ff8f0013 | -12.8202 | -50.5495 | 2025-10-01 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 362.4 |
| cd8eac7e-2dde-3ee9-99e2-7cd415cfc4a5 | -18.71 | -49.1621 | 2025-10-01 00:50:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 787a7d09-eac6-3133-8ed0-f91adbac2149 | -13.1966 | -50.9525 | 2025-10-01 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 23459daf-6e21-31e4-8755-898058caaa07 | -13.3278 | -47.8313 | 2025-10-01 00:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 028e8d50-db38-3222-93ff-12f20a967821 | -18.7094 | -49.1848 | 2025-10-01 00:50:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 22eb10a9-4b4f-343b-8f6e-9b6f07e57722 | -5.3382 | -43.7391 | 2025-10-01 00:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 27b095b6-0d87-3c74-8f1b-d3f2de8a2703 | -3.4762 | -50.0883 | 2025-10-01 00:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9438e313-862b-3e32-854c-c7599e5616c0 | -3.1013 | -47.0082 | 2025-10-01 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |


[Clique aqui para ver as próximas entradas](README4.md)
