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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41b57882-e96c-3b96-a60d-8c87acef873c | -4.73732 | -41.99315 | 2026-06-16 04:17:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 774aa7ce-de17-3131-9a9e-20694630a418 | -11.99126 | -45.15075 | 2026-06-16 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bfc083bd-4867-302e-849a-fed742199a42 | -10.13854 | -52.40649 | 2026-06-16 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1c4a988-a6d8-399a-9017-de50238e4d6a | -9.32979 | -45.48761 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 72a9fd84-1eee-3520-8ae6-cb8ff2358e47 | -5.95396 | -38.63036 | 2026-06-16 04:17:00 | NPP-375D | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 741b008e-d408-3714-bc5f-f6215eb38a2e | -9.6273 | -49.01391 | 2026-06-16 04:17:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc96b78a-15dc-3e21-8c71-2f1f1e1eb7e7 | -10.55093 | -47.03403 | 2026-06-16 04:17:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69cd22a7-f86a-3dd4-a3fe-cdab947c88c6 | -9.22598 | -48.5885 | 2026-06-16 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f62fb4a6-ea15-30fe-8a00-4d4db00ae61f | -11.27531 | -44.5282 | 2026-06-16 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 374589ce-51b4-3b7d-83bf-60129b02efa3 | -9.69947 | -48.6111 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c123813-ded0-3458-a37b-5b8e93e4e712 | -8.94707 | -46.96356 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a0cb640-ef6c-34ff-b1de-0a942a310c73 | -9.32618 | -45.48699 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ef41170-5ea0-35c6-bcef-fdb33daf6c01 | -8.94399 | -46.95786 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad7eca9d-383c-36c0-b2f1-d5fc80b9b027 | -5.8382 | -43.48654 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d82daa31-bf7b-3858-8a30-3ca02a6111f5 | -8.93524 | -46.96164 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a08572d2-fca6-37b0-bea9-ddc4a4fa70e2 | -9.20824 | -47.91435 | 2026-06-16 04:17:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e6bf7bc-d118-34f3-89fc-8f9ef01dc405 | -5.8376 | -43.49026 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| daf6e8a3-44da-3467-a091-8065297ec6a6 | -10.75399 | -48.16004 | 2026-06-16 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d2d6138-76de-3c18-93d2-906c30c1ea49 | -9.37212 | -48.41829 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcbcc2bd-0e38-352a-922e-d249b44e80c4 | -12.42415 | -40.24137 | 2026-06-16 04:17:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d14fde65-2811-3978-8abe-c0b4131ef89f | -5.837 | -43.49399 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8adf797-41fc-3c79-8491-8878195b5e4c | -11.69179 | -44.16038 | 2026-06-16 04:17:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91815d09-5179-3a08-a57e-da48073cd8e3 | -8.19176 | -46.76231 | 2026-06-16 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bca8553-c454-3b16-8d8f-c1fafd59daa5 | -9.36695 | -43.2828 | 2026-06-16 04:17:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 81ea20d8-ed8a-3205-9bca-2f4545cf15f5 | -8.28192 | -48.21794 | 2026-06-16 04:17:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dbcacfc6-2411-3d52-af71-eaf13ac4300b | -11.2747 | -44.53192 | 2026-06-16 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0adee4c3-6f41-333a-8e12-9c277c3c652e | -9.36809 | -46.48915 | 2026-06-16 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d353306-6cdd-3335-87b1-5155c92deb2c | -9.22671 | -48.58435 | 2026-06-16 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5cfe4b3c-1422-3f14-b4db-12133ca0b41d | -5.83881 | -43.48281 | 2026-06-16 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b69bbf4-dd91-359e-89b5-2892f659eb9b | -9.3597 | -46.49247 | 2026-06-16 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd75b41f-b4f4-38b7-bf14-45f2a04bd2d0 | -11.16821 | -45.36869 | 2026-06-16 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dfe0ad6-5fdd-3e65-94af-263fe8459311 | -9.32035 | -45.47743 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0434246-6d9f-39ec-83cf-7164bdb1fdfa | -9.34707 | -45.47678 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8943217e-4da4-3dbd-9817-eeb58f14cf47 | -9.22456 | -48.57088 | 2026-06-16 04:17:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23708d50-c2d7-36fc-ba13-ad88ce8aa2ce | -11.99189 | -45.14691 | 2026-06-16 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66eb5191-8812-340b-a5be-8be45bbce5e6 | -9.33906 | -45.47636 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f447f89c-9362-3ec1-bf39-276bf83fc98f | -3.50575 | -48.03874 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2edbe79-9fc2-3ec2-a6fd-f219b6016ddc | -8.28121 | -48.22202 | 2026-06-16 04:17:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 950f4019-5a76-30ed-a846-e5f576688a7c | -8.97665 | -47.97755 | 2026-06-16 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e21e768-5ecb-3e79-938d-fa595c70dedc | -9.33048 | -45.48345 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 69ccbff2-8a31-3a4e-80f8-f9edea5415db | -10.74505 | -44.05271 | 2026-06-16 04:17:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76fdaab4-3881-385d-ae68-cdcad307c2c1 | -9.34266 | -45.47698 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78714a3b-6b23-31ff-8347-5bd97160ec6d | -8.964 | -46.93541 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9050eb4-66da-338f-81de-33cb62b165e7 | -8.9361 | -46.95658 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 481e3d00-8650-35d2-a9f4-ca7cc07db75e | -10.13922 | -52.40285 | 2026-06-16 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be435a1e-09aa-3e4f-a786-de25808881df | -3.51385 | -48.03685 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a14a5b7e-78fd-31fa-b911-4ec2f0d0995c | -11.15594 | -48.26252 | 2026-06-16 04:17:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00f91276-b9ef-3551-8584-e2a2e36d9809 | -12.13479 | -39.41157 | 2026-06-16 04:17:00 | NPP-375D | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b1214cd-2d84-3502-8f90-522cb079e283 | -8.95272 | -46.95415 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aafa5756-4d73-3e5a-af56-4cb2f6cab723 | -9.00986 | -40.99459 | 2026-06-16 04:17:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e4c1dff-9db6-3f3e-896f-ea5657ffc503 | -3.50112 | -48.03802 | 2026-06-16 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04602051-0a62-3c30-8287-fb4a79f04773 | -5.35233 | -45.18922 | 2026-06-16 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5bbfdba-5c5f-3180-b595-2e0a19ef9178 | -8.95358 | -46.9491 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73a1b4eb-f234-3688-abfb-38a7884003a8 | -8.99327 | -45.73507 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 141dc1a3-38ef-3742-87ac-297b06d4fa96 | -7.36513 | -49.86839 | 2026-06-16 04:17:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9c9ea92-e069-33fd-9244-41f23cfc5cc1 | -11.9887 | -38.96138 | 2026-06-16 04:17:00 | NPP-375D | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e67489f-edc8-3cb1-a03b-f3fec4c32774 | -9.3822 | -48.43698 | 2026-06-16 04:17:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16b0dcf3-030e-34e7-b8fa-f69a4f5e2384 | -11.25655 | -47.52076 | 2026-06-16 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 527196a8-0c5e-352f-8ca8-7a262d56aaa7 | -5.80281 | -43.79365 | 2026-06-16 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fb92a82-45ec-350c-92c8-e948b54336bb | -9.33837 | -45.48052 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af7bd433-a00e-3dc2-9f4a-0a8f77b48e52 | -9.32756 | -45.47868 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 465a7ea5-9a42-38d7-a984-3be9a60b489c | -8.86877 | -46.97052 | 2026-06-16 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dfdc24a-0f86-345d-a00c-eea8f19ef011 | -9.34987 | -45.47822 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bc02046f-81d4-3f18-a754-63604751bfe1 | -8.9896 | -45.73444 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6a55be0-cd1d-3c9f-9475-bc7bdcd250e8 | -8.82477 | -48.82025 | 2026-06-16 04:17:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa78f9ec-40d0-3d39-90b5-42d7cbac27ea | -9.34627 | -45.4776 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c77f3c3a-1d5b-3a83-bb2a-21edb256429c | -5.30709 | -43.05586 | 2026-06-16 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a81e7d1-1e06-35d9-813f-3498555fdbce | -3.56127 | -43.20143 | 2026-06-16 04:17:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 066ba0c6-441f-34bc-a656-a661a5674493 | -9.34347 | -45.47617 | 2026-06-16 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 061f72ae-8e95-3f4d-9dfa-2062efc63023 | -11.59342 | -55.33606 | 2026-06-16 04:19:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cf9bfb0-006e-3874-a84a-a59b8aa8a5e9 | -11.79392 | -57.00208 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7d6f7455-6802-3dc3-b3d4-cc012eb4ded1 | -11.35485 | -51.38352 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 374e1c65-1a8d-3c91-9dd7-cc57f80cca06 | -7.7236 | -44.1627 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d4a8f33a-be53-3398-acea-c3c18c2f49b3 | -12.80738 | -54.86394 | 2026-06-16 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e3b0b1c-26a1-3e7a-be7b-2e1e9b97c649 | -6.83616 | -47.90952 | 2026-06-16 04:19:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79e4a13b-8eb8-318b-a7df-4e2caa058f57 | -11.35888 | -55.82303 | 2026-06-16 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c6feb221-e101-37ba-a618-bf4fe7b6d45d | -11.35371 | -51.38949 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 780cef94-aa30-3049-9420-8cb26cd2acf9 | -12.92229 | -54.22843 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41df80b2-1bd0-38db-b0f0-3ccb8bce6442 | -14.85677 | -43.36914 | 2026-06-16 04:19:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 34857378-a8a2-3e0e-8ec5-7b4fd105cc6d | -13.83963 | -46.17466 | 2026-06-16 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d2d75ff-cf86-365f-8e2d-450e6b746706 | -14.55319 | -42.08641 | 2026-06-16 04:19:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4cc5b9b2-9bdb-3a72-a0cf-585643a02b48 | -11.9124 | -55.9188 | 2026-06-16 04:19:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 696c29c2-55a2-3d5c-8da1-f99c0ad8ad6c | -6.46254 | -46.90172 | 2026-06-16 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c37482d-07b6-3ca6-a7a3-27b13dad3d47 | -11.35428 | -51.3865 | 2026-06-16 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 242d10dd-a84a-3e7a-a4e7-295b50b098e1 | -11.35766 | -55.82893 | 2026-06-16 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17a040f0-a497-336e-8b75-aac841c92d7f | -10.1497 | -56.61481 | 2026-06-16 04:19:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1d992f31-e7a1-36ce-98d8-f55662a35bd9 | -10.90013 | -54.13373 | 2026-06-16 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 395d3107-1674-3f37-9191-bc4a3b719a00 | -13.5581 | -47.85103 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d8db66b-faed-3fd7-8e0b-999f37b272eb | -7.71952 | -44.16594 | 2026-06-16 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ca0a980c-5ebc-345b-8328-2f69aa5e633a | -12.33369 | -50.00604 | 2026-06-16 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9445d4ad-5ef4-3d16-8374-1836c431bbfc | -13.55081 | -47.86977 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 836c07ba-80dc-3516-bbe1-1256230d84fd | -6.97275 | -42.88638 | 2026-06-16 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fc50c111-7e37-3aab-995e-275e7a89252e | -11.47445 | -57.12483 | 2026-06-16 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5079ad40-7cf6-37e9-990b-41bd88536093 | -5.98462 | -47.07259 | 2026-06-16 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a629ba7-5242-37f9-a136-c07aaece1163 | -5.803 | -45.07982 | 2026-06-16 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba83d982-0625-3d09-84a1-2553f054e2d9 | -13.54483 | -47.85828 | 2026-06-16 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44c996fb-c8d8-38f9-826a-e3f1510f51fe | -6.11915 | -48.48379 | 2026-06-16 04:19:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbbe1bca-c797-3c43-bf20-cd736802920f | -12.92558 | -54.22658 | 2026-06-16 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f56fd02-b13e-3627-a143-3b89902e7551 | -12.14921 | -48.46839 | 2026-06-16 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e41934e6-f0da-30f7-b6c7-f8f7b0b80457 | -7.71986 | -44.56653 | 2026-06-16 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
