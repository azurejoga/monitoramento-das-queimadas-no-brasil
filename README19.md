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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1dc6f3b2-8aa9-3433-a4b1-590244b0c25d | -9.63417 | -44.55338 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12057616-6cc5-3cb6-9fa2-52fb3a457246 | -12.11284 | -43.64923 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fd28d64-4796-3865-99f5-9cf9de41d5e5 | -5.57475 | -47.10639 | 2025-11-13 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7ac7ee50-7c48-390d-8f09-915900bbf58a | -10.42471 | -44.67498 | 2025-11-13 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de45d16f-4dda-3d17-998a-093c2c82bce1 | -10.54978 | -48.08587 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9dc49fd-a174-34d7-8e46-bd7d5b9f2506 | -7.09125 | -45.45765 | 2025-11-13 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40cacc01-2644-3947-baa2-b3dbf26372d5 | -7.11515 | -42.72427 | 2025-11-13 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a8a66ba1-01aa-3369-a0b8-5f59b9370a05 | -10.62958 | -45.24232 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 832dcb4c-592a-3db3-857f-7b929d011021 | -6.28852 | -41.73497 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 43ae5bbf-db7d-389a-b965-25e9ca317564 | -7.18526 | -44.98214 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bd631ae-fca4-3640-ad69-5e994a3c32d6 | -10.52625 | -45.10725 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 272f1dde-8951-3b4a-9cf8-4b206b729144 | -10.86747 | -44.5016 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07adb7c3-df32-39ca-9094-755b34712d3c | -10.50128 | -44.94182 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bacf58df-f748-3be9-a1ae-26e52cdcb4ca | -12.11393 | -43.64216 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37e34e5f-a85a-37fa-b495-7ddb1e3a0abf | -11.73737 | -48.53187 | 2025-11-13 04:14:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44a734f7-c820-3bb5-975b-a079839b22e6 | -9.35306 | -46.59622 | 2025-11-13 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16c14ff2-e48a-3125-a671-409cfc89d456 | -7.12625 | -41.85662 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d8e497a4-2dc0-3623-a0bd-738ff2cdab48 | -10.20532 | -36.22702 | 2025-11-13 04:14:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| b6b6f300-5a19-35f0-8cd5-1db653ce7c01 | -11.06426 | -45.37659 | 2025-11-13 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc3e512e-e996-3148-a7a0-2f7a293f9177 | -6.48778 | -43.96438 | 2025-11-13 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e285c82-7539-3205-873a-9eb6139b7905 | -10.66617 | -45.10093 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9c88d0d-eba1-378c-85ea-8aac9e597e78 | -8.94701 | -49.82587 | 2025-11-13 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39e16ab2-a26c-3228-a520-49c9d230cdc6 | -11.79603 | -44.20027 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca704df8-4d23-346b-bd1d-8ecc2ddaccf5 | -8.94266 | -49.82512 | 2025-11-13 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04f9b8ac-af61-33cf-a2dc-3576e915dcf1 | -9.6375 | -44.5539 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4d932c3-b472-33d9-98c3-6baa6ebe263f | -10.5533 | -44.82996 | 2025-11-13 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7af695a3-5851-36f1-905d-6f71726eb0b1 | -7.08791 | -39.26352 | 2025-11-13 04:14:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8ef20fc-57df-3ae6-8d19-5dfa40b613fb | -7.4185 | -42.76155 | 2025-11-13 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d6aeb926-e842-3b97-947f-b755f1cfbc97 | -7.10917 | -42.36713 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11b55c09-33bb-33c5-8a94-cfd63be43375 | -10.52902 | -45.1114 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecc2446c-b745-3308-9317-4eeb81bb2955 | -5.62614 | -45.04399 | 2025-11-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d553076-100b-38ee-b7a6-81a3fdd83760 | -6.54117 | -43.04384 | 2025-11-13 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b85152d8-cdf4-3bc4-93c6-9d55e3c97099 | -4.74169 | -50.72868 | 2025-11-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24ce8cf8-ae7e-3e79-804b-d169149018c4 | -6.29187 | -41.73549 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1ceb3287-f033-3d5c-8a29-dbb65b3add58 | -10.1754 | -44.78667 | 2025-11-13 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91302a0a-982a-3cde-a0f2-1b62a2509349 | -7.49047 | -42.75858 | 2025-11-13 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93d3635b-f491-346a-8ba7-cb67bac1ccc5 | -11.02596 | -44.63894 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dffb576f-dd00-3744-bc92-a2e15dfb910e | -9.44658 | -44.8765 | 2025-11-13 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d04f11d-d74f-3449-9018-e5462a98bef0 | -6.20141 | -42.14653 | 2025-11-13 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b0f75ca-a623-3b40-b35d-91208cc8136f | -6.8886 | -38.1477 | 2025-11-13 04:14:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b95cd870-c98f-32eb-a8e8-f4767c9445cd | -6.65705 | -43.51942 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c84f7fea-6f90-35d4-8b8b-33ee47bd7c07 | -12.31069 | -47.91201 | 2025-11-13 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43820a82-f77c-391d-ba56-ddd1b8438e51 | -6.90076 | -42.06501 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fc1cdb6-3ea4-3646-81b6-ae27cf9bbf79 | -5.86221 | -47.58621 | 2025-11-13 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 745c17f0-7199-3a05-8c6c-75a8e302852c | -11.7359 | -43.84507 | 2025-11-13 04:14:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebb3ea7d-0bf4-3115-8c2c-414e7c7d6522 | -10.8805 | -44.1376 | 2025-11-13 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1c63317-f900-32f7-8796-e27e4279e829 | -11.79934 | -44.20081 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e7fd06d-3ab9-39a1-a699-5499471a24af | -6.7832 | -42.84552 | 2025-11-13 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 72447ed3-df35-337e-9f60-1797d604cc18 | -7.47543 | -42.54949 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecca4c0a-d8d5-3aa6-b0da-2e307ea1e910 | -10.62623 | -45.24178 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26e2f322-d231-3337-88dd-3ee02f2a80b0 | -10.64327 | -45.03441 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abfd246c-6d72-3318-af82-a48c822b1c86 | -12.70049 | -43.34085 | 2025-11-13 04:14:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65ec482f-4f7b-31f1-a6e9-dd86c11143cb | -12.50202 | -46.30054 | 2025-11-13 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f5a1f8f-7141-37f0-b3ce-4e4fe36ca87a | -8.20941 | -47.88219 | 2025-11-13 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ceda2620-d2ea-3cef-b694-3f106082919d | -5.33295 | -48.38494 | 2025-11-13 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9138163e-3a97-3317-947f-177ff86364c4 | -12.66455 | -46.74874 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 4aa5a73d-4970-3b5b-be35-b6d157df5ffa | -9.94288 | -44.49514 | 2025-11-13 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5da1b5a7-2740-3000-beb2-56f1058007e7 | -5.394 | -48.32784 | 2025-11-13 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f604b381-af49-325c-8e8b-e6d69cfaf672 | -9.34882 | -46.59975 | 2025-11-13 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5a4cff91-3f22-3f86-ab05-1b6198965ff0 | -9.63029 | -44.55639 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf16477d-ad3f-32db-8f8c-d0e32490d945 | -7.71901 | -47.18385 | 2025-11-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15d62dfe-563d-304a-966b-291300a94943 | -7.14462 | -49.12904 | 2025-11-13 04:14:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39c109d0-06aa-37ac-85c0-f942fcd0ccf7 | -5.85166 | -46.44487 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7490773b-c15c-36b7-8894-9415d5c44d24 | -7.0758 | -41.58752 | 2025-11-13 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9530a268-cbc5-3880-a3db-76eb97f059bc | -5.72999 | -44.83261 | 2025-11-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dd6e701-ab7e-3c8c-a40d-1b97390b8643 | -10.42415 | -44.6785 | 2025-11-13 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c705d79-e9b5-36e3-bf1c-bf4aebe1b611 | -6.58711 | -48.04075 | 2025-11-13 04:14:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d053f21e-eb9b-35f4-b592-10991bd01455 | -5.88992 | -46.44221 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac085371-eaa3-39cd-b76d-d1fc9d7829f7 | -12.83449 | -46.71602 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c7cec6a1-370b-3ce0-a444-4a79fc2eacca | -6.54902 | -43.10163 | 2025-11-13 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b2fa39f-ce79-340f-a3c6-23075e42e1f5 | -6.13688 | -48.05652 | 2025-11-13 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c3d31d-90b0-3c1e-8cdb-26f5bc99eb33 | -5.75569 | -45.10709 | 2025-11-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e456409-e13b-3c6d-b1aa-eb7ddd50045f | -6.6929 | -47.79908 | 2025-11-13 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 599244fe-f880-3b9d-93cc-b2d3f3180358 | -7.58059 | -47.0528 | 2025-11-13 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25c38064-7617-34d2-ab53-dbdf5bee3cd5 | -7.10199 | -42.36961 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f25522ff-5f8a-3c43-be4b-ce181fffbc5d | -11.81478 | -44.2536 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05eee404-1f6f-3c61-bb9e-4f1bf5cf57d4 | -7.12688 | -41.87501 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f72375d-bcde-3abe-8716-87cbe10da440 | -6.46975 | -48.36556 | 2025-11-13 04:14:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18cc702d-2019-352c-b89e-e9c65eb3cfa2 | -10.53477 | -47.99075 | 2025-11-13 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f8d41cd-bfa8-3fc9-b033-08fa86784547 | -7.13303 | -41.87962 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d4cac7b-820f-3a1c-8875-cb1892cece49 | -6.56936 | -48.73331 | 2025-11-13 04:14:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e805a26-b5f1-3767-894e-7ecff0ef531a | -7.39436 | -48.65844 | 2025-11-13 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22074193-f141-34f0-a950-74d873547f1c | -8.86966 | -50.19298 | 2025-11-13 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eebf54e2-beb7-3ad8-891d-473cafe64c47 | -10.7582 | -44.91095 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80b4dd54-4f9e-3a71-b434-97a318aa5d4b | -9.35017 | -46.59156 | 2025-11-13 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 73e06896-6552-3f3e-adaa-1cf2e5c460ce | -12.41146 | -44.89195 | 2025-11-13 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fa67ab0-4e19-3037-851a-e0e4d0e5c242 | -6.95513 | -46.35215 | 2025-11-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca6cd126-5c42-3814-8431-fee7daa9cf97 | -11.00657 | -49.04415 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c81713e-a0bf-3923-9f97-96f3cee942d3 | -7.45508 | -42.57137 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d570417-9b62-3d40-ad7a-c813891dc608 | -7.75233 | -45.16741 | 2025-11-13 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d364a8ab-e683-32b6-a337-8e38fcad3606 | -10.17418 | -43.98056 | 2025-11-13 04:14:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4089657-3877-3af9-b5d2-55ff821eaff7 | -10.37055 | -45.05624 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d1bbe61-edfc-34b3-98ab-279c779f83b3 | -8.25122 | -44.36963 | 2025-11-13 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 006e99a6-353b-34ba-8796-616617c6c6a5 | -7.81963 | -41.76797 | 2025-11-13 04:14:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f6e4bd1f-2ca3-300d-a132-75d021aeae38 | -7.8303 | -41.76591 | 2025-11-13 04:14:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a17339df-b2a1-3702-b686-f4023800be54 | -6.31308 | -44.31074 | 2025-11-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac672ae6-10d5-34bc-9f54-83e794a872ed | -7.16088 | -42.56071 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ec708ab3-a584-360e-909c-4d3d5c36d1ce | -7.81688 | -41.786 | 2025-11-13 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 733eeb8d-cf04-3f73-90e0-0264fdcd6f17 | -7.22204 | -39.95773 | 2025-11-13 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 51640e35-a713-378d-a6ee-4b750dfd6b45 | -10.2054 | -36.22903 | 2025-11-13 04:14:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |


[Clique aqui para ver as próximas entradas](README20.md)
