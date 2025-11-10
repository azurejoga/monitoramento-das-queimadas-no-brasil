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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50fab713-9575-30b8-b447-320c6c9bb962 | -4.20792 | -50.63351 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ea4eabe5-3bfa-3ab9-bccf-a99837b5c414 | -5.76744 | -40.79293 | 2025-11-10 03:57:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a9b376b9-f495-3139-bd89-8cff273fd84e | -5.12382 | -44.73111 | 2025-11-10 03:57:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d7c0aad-cda2-38c0-acd7-3513eeacb60c | -8.04678 | -39.68769 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 481d4fcc-f337-32f0-a24b-cc87e67c0db5 | -4.68595 | -45.84926 | 2025-11-10 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1538251-35e9-3f08-a150-4d8ebe9b2a26 | -3.09383 | -50.32763 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 366f7003-0ca1-3a68-bc05-bfb900d36c65 | -3.10915 | -50.19798 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2a850a3c-98f6-3b87-b157-3ce5188562cb | -4.14609 | -39.53728 | 2025-11-10 03:57:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 108eb614-a2e7-3acc-ba0c-660e4330543c | -3.09064 | -49.26564 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec77dd1-0244-3c77-a590-0727525a4d86 | -2.82605 | -48.65874 | 2025-11-10 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f50145e-e8aa-30e3-a1d9-2032cffbed9c | -2.60389 | -49.22938 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7371cfa3-3572-3925-a5ae-005dcfa44b8c | -7.41452 | -40.07064 | 2025-11-10 03:57:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52d15a85-7a3c-33a4-8cba-a2535f341c96 | -3.09693 | -49.26675 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3688efeb-c334-3bee-a2d1-1387f4b5d9c7 | -4.10687 | -47.28328 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 737044cf-47f3-3ccf-b75b-68a83d9c057b | -8.0447 | -39.68741 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c25fd3db-1146-30d0-8f3e-1afa46e1460c | -4.0242 | -41.62877 | 2025-11-10 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3436c0d5-2f49-346f-92b5-d29036df1677 | -3.32962 | -49.9221 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ecac698-84de-32ae-9b8e-64cf1f2429a1 | -5.04776 | -49.56398 | 2025-11-10 03:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 437a8919-4ad6-31e0-afba-3a6fd2b5005a | -9.31307 | -41.05545 | 2025-11-10 03:57:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 89623e21-8f4d-32f6-b5d2-8a072b45ce83 | -4.58643 | -45.54803 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fe0d7a2-49a7-3f9a-ab70-119a62d1c426 | -9.10172 | -35.41175 | 2025-11-10 03:57:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e9761113-fb0c-379f-8a9a-1ad07a193553 | -6.11026 | -38.16345 | 2025-11-10 03:57:00 | NPP-375D | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85b3f8b0-c1ac-32cd-ab2f-a2c0a357a1bd | -8.56178 | -40.86139 | 2025-11-10 03:57:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7b3e6987-79ba-34bf-bb7d-8a1ab06277bd | -4.25994 | -46.70711 | 2025-11-10 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74718f7c-5707-315e-b513-0c92e49392ab | -6.9429 | -39.7629 | 2025-11-10 03:57:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3ab98c7-1690-3d1d-bf5e-00ff4d3ae0c9 | -2.28818 | -46.44387 | 2025-11-10 03:57:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38fb87a4-3ed8-345d-a467-155655be9520 | -5.15193 | -50.873 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a71fb4c-b550-37be-ad81-20a64d2e4265 | -6.56035 | -38.69687 | 2025-11-10 03:57:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95fda30a-840e-3e01-ac09-c98ff31e7341 | -5.63283 | -43.92537 | 2025-11-10 03:57:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f498769-76af-3be4-8531-315491b480ed | -5.37695 | -44.72776 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2f52751-35d4-3ca1-9e6b-623b2a679112 | -2.11371 | -48.18335 | 2025-11-10 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 376eacc2-4ada-3e0d-8796-c186af98eaf2 | -4.91008 | -44.88585 | 2025-11-10 03:57:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 587ca66c-4abe-3a2f-bef4-5258ed75d1d1 | -3.15557 | -45.32382 | 2025-11-10 03:57:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5402ae1c-84c6-3181-898a-63c822241064 | -2.11581 | -48.18627 | 2025-11-10 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3bbe7a5-8547-3b9d-9b8d-f5360e14da02 | -6.85831 | -43.62453 | 2025-11-10 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c81b1a26-fc8b-38ed-bf31-e58d7923471b | -1.79148 | -48.06411 | 2025-11-10 03:57:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d39bab1d-a9bf-38ce-b3c4-b871987f80c9 | -4.64831 | -46.34494 | 2025-11-10 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33271050-efee-39e9-91f6-a204f9bd9317 | -4.91569 | -46.7365 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 820cdac7-21cc-3c4b-957e-23a9c2d9b3d6 | -5.07454 | -45.57821 | 2025-11-10 03:57:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c44924da-f480-36ab-a8e1-7c14d2210942 | -6.59338 | -44.65363 | 2025-11-10 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 948152f4-c950-3e54-aff1-ebecbf6030dd | -7.43285 | -35.1279 | 2025-11-10 03:57:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3424fb34-c16e-3c9a-bf2f-06de62584c4a | -4.58951 | -45.54994 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb89ae3f-e196-3755-9356-d501db785487 | -8.01103 | -41.60007 | 2025-11-10 03:57:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e07c7db0-75c2-30d7-ba52-2c70a7b6c235 | -5.63123 | -43.90925 | 2025-11-10 03:57:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908ed662-a095-3fc4-b8b4-b7f10fc72cf5 | -4.68498 | -45.85498 | 2025-11-10 03:57:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdb85fb5-74b9-3757-b24d-2d54fa6de131 | -5.14998 | -50.87318 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1131dae0-b0d1-3f90-a4cd-b91bed0f4956 | -2.94546 | -51.58204 | 2025-11-10 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f564e94-65b3-3209-a678-9f002adce8c1 | -4.57776 | -45.54063 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 68e14a5d-6de7-38e0-8a43-b8faa08b9056 | -4.533 | -46.61877 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bdc930f-3fcf-31fd-84dd-6ebee0eb72c9 | -7.34518 | -35.21155 | 2025-11-10 03:57:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3d2a459b-5962-34fb-941d-687fb9345733 | -7.98616 | -38.67048 | 2025-11-10 03:57:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eda65b72-7e9d-3a4a-b92e-9be72e1cb2d6 | -11.75267 | -40.22003 | 2025-11-10 03:59:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56c7d66c-cb10-388e-86bd-c4be0479095d | -13.31208 | -46.77585 | 2025-11-10 03:59:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 490fce3c-4fd3-322c-9b60-e23d28c1518d | -10.13906 | -44.19841 | 2025-11-10 03:59:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d11de1c9-3ddd-395a-95a6-2ad995fad025 | -10.37678 | -49.91364 | 2025-11-10 03:59:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a950bdc8-eafb-3f68-aaeb-a4aa07d07ea9 | -14.69199 | -46.58547 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e12f78e6-1da7-3179-ab2c-4e26a2a32b68 | -13.96502 | -46.91712 | 2025-11-10 03:59:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79d2fcb6-5977-3314-a077-ac0948c1bf2b | -14.69648 | -46.58548 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8c5986c-bae1-3887-9243-d51dd2605ea3 | -13.96397 | -46.91441 | 2025-11-10 03:59:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6074581f-e12e-3ebf-bd86-50d3d488c5dd | -14.70276 | -46.59993 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e51027bd-5c55-3735-8e18-19d5ee8b3aeb | -10.45821 | -44.94293 | 2025-11-10 03:59:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5829b375-0619-3f2d-8605-9b0d32ae5968 | -14.70641 | -46.60443 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32c096c2-c14f-32ed-9176-80fedd982d79 | -10.01863 | -44.14818 | 2025-11-10 03:59:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5687f90-7b17-3dfb-bde2-a033ff5ffd3c | -12.40886 | -48.15149 | 2025-11-10 03:59:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 340e3713-f649-3066-82b0-e47f127b4805 | -13.6963 | -47.26562 | 2025-11-10 03:59:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfe854ef-bfe9-3283-961e-37cb26a88685 | -12.01379 | -43.85431 | 2025-11-10 03:59:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffde480c-2cab-3cdc-8ff2-fffe81a40731 | -9.12829 | -50.09016 | 2025-11-10 03:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7c5f8bac-6910-36d6-a34b-00a78713eae5 | -11.53334 | -44.02798 | 2025-11-10 03:59:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74b29895-2562-39c0-8f25-41a5cb93cc7b | -12.01463 | -43.84955 | 2025-11-10 03:59:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd04666c-6b13-3b9a-9b73-dc4c13055e1b | -14.69553 | -46.59053 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6120baba-41d7-3ce9-9cd4-b34c9f0d4eb8 | -11.21713 | -41.54641 | 2025-11-10 03:59:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68a777ae-9200-373f-8be5-95318f2a6d98 | -14.69748 | -46.60412 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86a1846e-96e7-3086-8ff8-d91159f5ed74 | -12.31301 | -37.91998 | 2025-11-10 03:59:00 | NPP-375D | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c95b58f0-60c6-3b6f-977d-ad8af14d7539 | -8.75031 | -48.31898 | 2025-11-10 03:59:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 204da8d4-3ce3-382e-bdac-5e708b1892d6 | -13.72935 | -51.46003 | 2025-11-10 03:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec377a0c-707e-3546-8862-66a469eac8d6 | -13.72845 | -51.45987 | 2025-11-10 03:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 959a6eca-d7d7-39ec-89bd-fc5e08f6127e | -9.91084 | -44.21674 | 2025-11-10 03:59:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d056bab0-906b-3dda-b323-7b873cda4bcd | -11.75324 | -40.21648 | 2025-11-10 03:59:00 | NPP-375D | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d003dd0a-12fb-3e79-9ffc-4223c6ba09c9 | -10.61444 | -52.18303 | 2025-11-10 03:59:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9733f8b8-0cf3-361e-876d-66411fe26541 | -14.68923 | -46.57627 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4df46ee5-8651-30ad-bc41-1a4585d95265 | -11.17018 | -43.57077 | 2025-11-10 03:59:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c0e5ca5-e419-3e9f-a2c0-dd2d793d76f3 | -13.72838 | -51.46464 | 2025-11-10 03:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a1e88a9-2859-3f3e-9295-287dd5a27bf6 | -14.68751 | -46.58542 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a54850b0-ae2e-3999-9dbf-edb2339e0b71 | -13.9648 | -46.90984 | 2025-11-10 03:59:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bf01176-4dcf-3374-baa4-36a66ee93325 | -9.66043 | -44.50574 | 2025-11-10 03:59:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b3f87fc-9459-398a-b6f9-74308e1d711c | -14.69826 | -46.59993 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7660e66-a06f-3f79-acd3-3ed30b3bc3c3 | -12.01601 | -43.85292 | 2025-11-10 03:59:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42944f45-93e4-394c-8987-c8d0385123c5 | -11.22122 | -41.54319 | 2025-11-10 03:59:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 719e74eb-5b4a-38e8-82eb-8f906f5f2027 | -13.96589 | -46.91256 | 2025-11-10 03:59:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fd8c161-c766-3547-b8a3-46447aed23cd | -10.79652 | -44.24966 | 2025-11-10 03:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e11efcd-ee23-30af-a522-62539f2c062d | -11.21777 | -41.5426 | 2025-11-10 03:59:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4c11e22f-fb23-34ab-b330-14c166801a6d | -8.73794 | -48.31687 | 2025-11-10 03:59:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63313934-d012-36e5-b5c5-78a2a3f81a5a | -11.66505 | -48.46582 | 2025-11-10 03:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ae5f79-718a-373d-be31-1cf37952324d | -14.70356 | -46.59565 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7fae0c1-4589-34fe-a900-8852958ddfb6 | -11.12328 | -40.82391 | 2025-11-10 03:59:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b97bd01e-7b17-3bba-8eee-901385c602e4 | -13.73031 | -51.45544 | 2025-11-10 03:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20aef335-8823-38f0-9baf-3b8b0547ae42 | -12.39664 | -46.58847 | 2025-11-10 03:59:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2e699b5-6ec8-382c-8b8d-d0e148fd7a5d | -9.66962 | -43.89999 | 2025-11-10 03:59:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a7589bb-ea48-3513-bfe6-a44f38819dbb | -14.70198 | -46.60412 | 2025-11-10 03:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aacee3c1-b2dd-3f6c-bda4-519be5bf4c77 | -10.3776 | -49.90947 | 2025-11-10 03:59:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
