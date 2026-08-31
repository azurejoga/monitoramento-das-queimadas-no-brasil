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

## Dados Diários - Página 178

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0d0d12e-890d-39ac-9959-a468b74a32af | -10.7268 | -50.6618 | 2026-08-31 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e904be02-74a0-36da-852a-a3029b97911f | -8.5739 | -66.9754 | 2026-08-31 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6be6aeb9-72ef-3ffc-83f9-0f93d22c2ce9 | -3.4185 | -61.3273 | 2026-08-31 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 16e0e35a-7e12-33b3-9b0e-35f1569116d5 | -9.0057 | -65.456 | 2026-08-31 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 9ebb3e2a-2d0f-3b6e-9549-5ac96a788d5b | -7.9425 | -44.2538 | 2026-08-31 17:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 19d24248-1e71-3cd5-a7e4-f5aa81329fce | -3.1083 | -61.2191 | 2026-08-31 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a7f6197a-36b1-3a30-b50c-e54088fc4742 | -11.0244 | -49.6872 | 2026-08-31 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 7ea724cc-7b3e-38aa-82c9-4f80383f80e1 | -6.8411 | -58.9939 | 2026-08-31 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b806ac25-7bfe-37f9-a564-3222419c8497 | -3.4002 | -61.3276 | 2026-08-31 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 8009da12-9b59-3038-8b88-8a107a72b752 | -9.6939 | -65.1145 | 2026-08-31 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 5cb4363d-4fbf-35c3-b977-f7a54acb9ab3 | -7.5662 | -61.3049 | 2026-08-31 17:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 81a7bdbc-fb8b-34f2-bdd4-1cd9d93e11c0 | -10.7081 | -50.6425 | 2026-08-31 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 7df0c0d3-1efc-3dae-b47d-a5951f432b70 | -10.7856 | -50.5066 | 2026-08-31 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1ab6bf4c-d5dd-374c-b25b-b6f8b3b9c05c | -7.3119 | -60.5706 | 2026-08-31 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 192.9 |
| c6057c66-181c-3896-baf7-01744dcc1c72 | -9.4156 | -45.6499 | 2026-08-31 17:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 83080d58-d6e1-3f4f-9147-ebcb99b4b622 | -6.8568 | -59.4757 | 2026-08-31 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 4e3c5331-9e7a-3e87-b151-7d7d556fa643 | -10.1531 | -45.7438 | 2026-08-31 17:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 46518689-4e70-356f-8993-2b3538485095 | -10.7271 | -50.6405 | 2026-08-31 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 263.2 |
| 8b9558ce-8681-33f4-a1dc-969eb15fca34 | -8.2414 | -54.9601 | 2026-08-31 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8f282889-78c1-36f4-884b-8f8d667f3c76 | -11.6786 | -54.5484 | 2026-08-31 17:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 7e9f54c6-d79e-3013-8fd4-5a7d9aee0443 | -10.1528 | -45.7665 | 2026-08-31 17:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ed4fc05b-73a1-3f9d-88af-dd848920f266 | -14.8316 | -55.7399 | 2026-08-31 17:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 40.0 |
| a7c72362-a213-3396-b29c-279a4db53631 | -8.9664 | -62.4076 | 2026-08-31 17:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| db09a781-0730-3a0e-af5f-55f4eface0f0 | -9.4342 | -45.6704 | 2026-08-31 17:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| d73e0f76-e77b-3d8f-bb32-3d2b0444450f | -9.694 | -65.0958 | 2026-08-31 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| eede65d0-70f7-3d10-8c0a-1450867f83bd | -8.9873 | -65.4379 | 2026-08-31 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ae4d10db-d17c-3cb7-80ef-36cbedd530d4 | -8.2229 | -54.9412 | 2026-08-31 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 43cfac74-4802-3a01-85fc-1de8f7cb1484 | -11.381 | -45.1697 | 2026-08-31 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| ceabc157-5ba3-3756-8bbd-fd2b33b247e7 | -6.8412 | -58.9746 | 2026-08-31 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 20446ffe-8fc6-361d-a2b1-0a064160c760 | -9.6679 | -46.5455 | 2026-08-31 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.0 |
| be97455a-eb62-33a2-9ac6-ed5b499ef713 | -8.7628 | -46.4642 | 2026-08-31 17:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 4316ece0-8779-390c-9c90-0066a953a9bc | -11.1634 | -50.5727 | 2026-08-31 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| db577cbb-5cc9-32be-af89-d4349363622d | -7.6343 | -44.8358 | 2026-08-31 17:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 7b1d6669-e3a3-3a6b-9b9f-13493c9ddd8c | -11.3475 | -46.0203 | 2026-08-31 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4d16483c-e9d8-3e57-99e9-ec81c8d7d5d3 | -6.1295 | -57.6637 | 2026-08-31 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c0be8cea-9689-330d-8d86-8bf7e8c31880 | -8.8705 | -66.7822 | 2026-08-31 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| c3f20a3b-0030-3c26-9fda-c49ff6c17dda | -3.6399 | -60.5466 | 2026-08-31 17:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 63d55ded-4ba9-33c8-9670-114ddead5a1b | -10.4794 | -64.5012 | 2026-08-31 17:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 273716bb-5808-3f19-a82d-064ff0f93f29 | -8.0634 | -72.0557 | 2026-08-31 17:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 2e0dd885-c74e-30b9-b5cb-4c261d930699 | -13.4767 | -51.4086 | 2026-08-31 17:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| c159286c-63c3-3246-a1a2-61aa035cc2ad | -8.5555 | -66.9574 | 2026-08-31 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2246d12a-e16d-3303-a646-56cd763501b3 | -8.9478 | -62.4084 | 2026-08-31 17:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b42e68ef-51bb-3325-ad1c-ce09f5a59d3e | -3.9708 | -60.0067 | 2026-08-31 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9d618eb1-2197-3d89-bd79-902f37105f35 | -3.0901 | -61.2005 | 2026-08-31 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 37706ef3-d1e4-3c01-affc-b37ada8b15f2 | -8.9428 | -63.2797 | 2026-08-31 17:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9c9c4695-1645-30ee-8eaa-55108574edd7 | -11.1995 | -55.1008 | 2026-08-31 17:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 2d528cda-e38d-3e56-9c7e-9c74b7c65615 | -8.8031 | -70.8217 | 2026-08-31 17:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 95b61c99-cde2-322b-8f7a-ade2d2569da3 | -8.631 | -66.5473 | 2026-08-31 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 92dce01d-a967-3f4f-9774-9b5c24efdaa1 | -8.6673 | -62.8369 | 2026-08-31 17:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 78cbfcf6-f700-311f-ab4b-28174a7b6593 | -12.1902 | -50.5409 | 2026-08-31 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0787b41b-c4f0-3c0c-8114-92e2ad2d6606 | -8.948 | -62.3894 | 2026-08-31 17:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c6d0326b-46b8-3f81-9030-209d86a0bb5d | -3.1267 | -61.1811 | 2026-08-31 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| c4c28532-9bfb-3be6-a3d5-cb9522b2b2cb | -6.8201 | -59.4386 | 2026-08-31 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| bddf2e82-a88e-3b0f-b851-b5ccae81490a | -10.8617 | -50.4772 | 2026-08-31 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 32eb62bb-9411-3f71-867f-057cbb2d05b2 | -8.631 | -66.5473 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 2cfd253f-3eee-3b6f-b8bf-6236400368eb | -7.9797 | -44.2962 | 2026-08-31 17:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 2f57ae19-2c8c-3aa2-b6bd-718150bad955 | -8.9481 | -62.3704 | 2026-08-31 17:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 2f96b335-0a85-3003-a011-758cfcb74a7a | -9.4156 | -45.6499 | 2026-08-31 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 343f9edb-2c16-3120-ae18-b35e9e4170a3 | -10.7268 | -50.6618 | 2026-08-31 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 02c7fc8d-7051-3fe1-8553-90b8ccb39b82 | -6.8017 | -59.4394 | 2026-08-31 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b5bdd63d-0802-3d38-9e89-c146e20b74bc | -8.574 | -66.9569 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d1598ed0-4796-3947-81a8-97693d219f41 | -8.803 | -70.84 | 2026-08-31 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2bf5b92c-9b54-3a86-8e38-63fac0d7b338 | -7.5659 | -61.362 | 2026-08-31 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 7bf0e051-4946-37a7-bb4f-140f39312328 | -13.4575 | -51.411 | 2026-08-31 17:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 2b0105fc-9c25-30c7-95e6-a2e6a385bf85 | -9.4342 | -45.6704 | 2026-08-31 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 54a8b6af-582e-3276-9c2b-56a0d56cf2b2 | -12.1711 | -50.5432 | 2026-08-31 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 46ba1c61-b21a-36c5-8bb7-8c2408a81b34 | -3.8478 | -65.1297 | 2026-08-31 17:40:00 | GOES-19 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| ca5d5d0b-f60b-3e55-99a6-3c675a5ab4cf | -11.0244 | -49.6872 | 2026-08-31 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 90365fb4-2c3a-3c68-8597-3a88a5e31d33 | -13.4767 | -51.4086 | 2026-08-31 17:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 6c79687e-9a75-30ac-9769-8eb93644b0e8 | -8.87 | -66.9121 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| c52d0b78-0851-32a0-b215-d5bab8cab178 | -3.9707 | -60.0258 | 2026-08-31 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a73b683d-144e-39c4-a165-41771d350f39 | -9.6676 | -47.9429 | 2026-08-31 17:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| 8a3945c9-6818-354b-99dc-80c67024e8a9 | -13.4707 | -57.0574 | 2026-08-31 17:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c0f20315-22e8-393e-9afa-8b534a94ef62 | -15.2275 | -56.3716 | 2026-08-31 17:40:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 09be5898-2498-3edc-a48c-d617a2115cc4 | -10.3199 | -49.9996 | 2026-08-31 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 235.5 |
| f559ae37-f5cc-3a30-aa2e-1d97e6e87ea1 | -6.9514 | -59.0666 | 2026-08-31 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 117562a1-9cb5-322f-a18e-ad24e10e369c | -9.0057 | -65.456 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 85275dec-8255-34fb-b4fc-ea3221d46a02 | -6.7833 | -59.4208 | 2026-08-31 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9f97ad21-c315-3664-aebd-16e4872f6a63 | -8.9873 | -65.4379 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d5e37a36-df1e-38f6-92d9-f18e193217cf | -8.5739 | -66.9754 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ef6a5eeb-5de8-32e6-a89d-0b7920f234cc | -11.3611 | -45.2185 | 2026-08-31 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 72ca27fb-5dae-36c1-b1a3-0565c89f0008 | -10.7081 | -50.6425 | 2026-08-31 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| d87fd518-7519-3c6b-a112-85b7592066e5 | -9.694 | -65.0958 | 2026-08-31 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 7f4173eb-35d5-355e-8dd5-95f8a0dac93c | -3.3819 | -61.3657 | 2026-08-31 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 2bee196b-d386-3728-8b5f-131c442f9801 | -8.9664 | -62.4076 | 2026-08-31 17:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a0b32bb3-2a83-38f3-b89e-330131b54c63 | -11.229 | -45.1221 | 2026-08-31 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 529c1382-e83d-32a3-afb2-3d205cfe2f17 | -3.4185 | -61.3273 | 2026-08-31 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3e44c8c9-0925-36a6-8133-64377c65ab2e | -3.4002 | -61.3465 | 2026-08-31 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 32bd7884-61e8-3abb-9aec-b5628726c5d4 | -11.2482 | -45.1194 | 2026-08-31 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b7fc6251-8a63-3ad5-8b7f-d1ee8c954702 | -8.3717 | -62.716 | 2026-08-31 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8a6a4e88-c964-352d-9623-50756091fe22 | -9.0717 | -60.4918 | 2026-08-31 17:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ec7fb39f-d348-362f-a777-f507763d948e | -19.0744 | -57.3876 | 2026-08-31 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| f6910bdc-f777-3b90-a3d7-4482fb98211d | -8.8031 | -70.8217 | 2026-08-31 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0f97ba55-5955-396b-a1fc-09a993dd7d4f | -6.8608 | -41.7013 | 2026-08-31 17:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 65.0 |
| 8ee27a05-c6ad-3e19-9efa-157a830c2661 | -8.6859 | -62.8172 | 2026-08-31 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1b5a7622-160f-3ef1-980d-2e7f6bf14861 | -9.0797 | -65.491 | 2026-08-31 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 947c0f72-6889-3ac3-aa9e-646f32dadbfc | -3.4185 | -61.3461 | 2026-08-31 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 84928341-fa57-3ce0-9321-797d85186b25 | -5.9636 | -57.6704 | 2026-08-31 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c95fe405-c1ca-35de-946c-e0653cea7214 | -10.3394 | -49.9547 | 2026-08-31 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 7f368470-1361-35d7-92c6-05fd4c61064e | -13.9474 | -54.4179 | 2026-08-31 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |


[Clique aqui para ver as próximas entradas](README179.md)
