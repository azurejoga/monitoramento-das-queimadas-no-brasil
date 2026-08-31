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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba667b69-26fa-3627-8ac2-c0e48ebe1d2c | -12.0925 | -44.996 | 2026-08-31 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 3346397c-90ad-3b2c-90c6-54e1e857e6d9 | -7.7752 | -44.0628 | 2026-08-31 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 45f30b62-2326-3a6a-bfba-4ec10f6cf2e6 | -3.6398 | -60.5656 | 2026-08-31 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 25df2429-e9dd-3025-8990-96074ccf997d | -9.6441 | -48.2959 | 2026-08-31 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b5c30847-c78f-3b60-a4d5-a4cc5d8fe181 | -10.8425 | -50.5005 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6e112912-1432-366b-a0ab-1e785570d52f | -12.1109 | -45.0395 | 2026-08-31 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b0b97b0e-1ef5-30e3-b9ab-9c3905e51ed6 | -11.229 | -45.1221 | 2026-08-31 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 92fed071-1154-3518-92b7-8f745322274f | -5.4876 | -57.1416 | 2026-08-31 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b3378f02-36c7-31fa-b929-2f8527867e18 | -7.917 | -61.3481 | 2026-08-31 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c9580848-ac5c-382e-b443-5439888f4fae | -11.3423 | -45.1982 | 2026-08-31 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a5200d9d-e1da-31bf-9fa7-93e911aa7d25 | -18.2904 | -52.6818 | 2026-08-31 14:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 112.5 |
| af5b2a54-bebd-373d-8ae3-9409900af704 | -11.1824 | -50.5706 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| acfd1c4c-4456-3a61-91ea-03b48b5abdf3 | -11.5475 | -45.4906 | 2026-08-31 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| e8bae17f-072f-392c-8349-6923a3b7f563 | -9.5967 | -47.5983 | 2026-08-31 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 59d92900-aea6-32e8-9c89-86a01bdb94b0 | -15.2669 | -53.8851 | 2026-08-31 14:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 359e893e-c2a1-379c-b8ad-93f9c6767ebd | -8.7631 | -46.4418 | 2026-08-31 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 53b72bfc-6fe4-39ac-b924-b506442f286a | -18.27 | -52.7068 | 2026-08-31 14:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 10c42a63-1461-384a-aecd-9387577160df | -10.7428 | -50.8727 | 2026-08-31 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ee20fd7f-93f3-3dcd-a5a8-2a2019a257d5 | -14.1459 | -52.7871 | 2026-08-31 14:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c16cd51d-16ca-3591-b7be-19d3c414d5ec | -10.1087 | -50.2776 | 2026-08-31 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 405b5023-71bd-3fed-8fd4-adf26f6d4639 | -9.4345 | -45.6477 | 2026-08-31 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 952751f6-75af-3d2e-a16f-9589cfab073d | -7.3117 | -60.6089 | 2026-08-31 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 3fab8c1b-a875-39bd-a987-db74ea8d0c67 | -12.9401 | -45.9241 | 2026-08-31 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| e826a7ee-27a2-343f-aed8-c7ee94c8ecfd | -11.2125 | -54.0181 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 6f9ddff2-9c67-3603-a5a6-42c41d663ad9 | -7.6149 | -44.8833 | 2026-08-31 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 13b81d53-fa81-3515-a7be-56487247265c | -9.6942 | -65.0582 | 2026-08-31 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 39c33a64-db2f-35be-9318-bad3d568de32 | -7.7938 | -44.084 | 2026-08-31 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| f4144555-994e-33e7-8453-85190c9bc783 | -10.7405 | -54.0606 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ffe23bfb-dde4-349b-9a3d-09465d3fed4d | -9.4339 | -45.6931 | 2026-08-31 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| f9ef7562-1024-3d0a-b70e-d932203b01ec | -12.9054 | -59.8857 | 2026-08-31 14:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c3be901f-fe2d-303b-b618-06c7807f7b61 | -5.8967 | -59.9719 | 2026-08-31 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ec785169-3f93-37d9-b42c-718ed2458f6e | -3.6216 | -60.547 | 2026-08-31 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 73bb1a8c-d74f-3fcf-beaf-a607f4883d3c | -11.2314 | -54.0164 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c1540df0-3021-30c2-954f-1b4c8e8a33ae | -7.6253 | -55.2787 | 2026-08-31 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ebaf9af0-a614-3e29-b36d-9514dcbbd092 | -14.4004 | -52.5438 | 2026-08-31 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 706f4db3-98e9-3ca2-b2f7-78c06ec082a1 | -9.6676 | -47.9429 | 2026-08-31 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 483b47ff-3567-3f78-bbb1-c734c1de33ce | -8.7989 | -62.5095 | 2026-08-31 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 890db0bf-5d02-3f09-8dcb-b79fdacc6a3c | -14.2792 | -52.8758 | 2026-08-31 14:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 87973e77-7648-3ede-905a-2cea8f96d5f1 | -7.5139 | -55.2851 | 2026-08-31 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| eb5677ec-2606-3a39-81cf-9f7e836f4347 | -6.1109 | -57.684 | 2026-08-31 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 193.2 |
| 9884f594-04cb-3910-8369-309ed6b23fcf | -8.9481 | -62.3704 | 2026-08-31 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 158d6dbf-9e91-3eb8-9474-070aaa57019a | -13.9474 | -54.4179 | 2026-08-31 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 269.3 |
| 23eec584-866a-3747-9026-0d45a484ddbe | -5.2548 | -55.8907 | 2026-08-31 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 55da3c2f-431f-3468-a1ec-4ab206c26c62 | -11.1723 | -51.294 | 2026-08-31 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 690c02a8-d552-3456-8fce-888b2420b0bc | -11.2103 | -45.1017 | 2026-08-31 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| eab46765-7e48-3b69-a9fc-480c4aef207d | -9.4535 | -45.6455 | 2026-08-31 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 5602ce50-e70a-3d4d-8cdb-4620d02dbf22 | -18.2695 | -52.7284 | 2026-08-31 14:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 054a638d-20ad-3313-84f5-42780adcc7a3 | -8.1672 | -54.9246 | 2026-08-31 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 83947dec-b265-3673-af57-c99dbc5bf6e5 | -9.5964 | -47.6204 | 2026-08-31 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 233.5 |
| ea9670fe-31d9-371a-88fb-2a6725f021ad | -9.4342 | -45.6704 | 2026-08-31 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 9f2e61ac-4918-30f3-b5b4-72f0691f9810 | -4.9604 | -55.8424 | 2026-08-31 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 1ce1e222-c8fc-3588-ac00-4a3a79ffb987 | -10.7593 | -54.0589 | 2026-08-31 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 137784d3-0548-332c-94b0-c727e7907611 | -13.6233 | -51.8371 | 2026-08-31 14:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 9a025054-75da-33ab-8f29-e21a1e22d9c8 | -8.7439 | -46.4661 | 2026-08-31 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| c4a41382-eb78-3ba2-aae6-ca13b162b030 | -3.1998 | -61.161 | 2026-08-31 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 91dade5e-7eb0-3896-b00c-42df31bc78c6 | -15.653 | -56.3854 | 2026-08-31 14:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| e61ef3e2-8927-3506-a481-3512c5d21e2d | -11.7782 | -47.6697 | 2026-08-31 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e7a18ffe-3c6c-3357-898b-8c2753da39e7 | -11.1913 | -51.292 | 2026-08-31 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fafdcaa6-dee5-3caa-ae86-2bd3cb83c368 | -6.9367 | -55.636 | 2026-08-31 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| b655ecac-a690-3017-aca1-4f34566d0085 | -11.2109 | -51.2476 | 2026-08-31 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0d929de7-b5e9-38c9-8eff-0eea8bf0128e | -14.6899 | -54.912 | 2026-08-31 14:40:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5bea5c2f-8d7c-3609-bc24-5909fbb2e03a | -18.2704 | -52.6851 | 2026-08-31 14:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 1c79d46b-f2da-3ca6-b0cd-3b30a6a534ea | -5.8537 | -57.5576 | 2026-08-31 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 0027eeb3-cb1f-38c5-8119-4b2560c57b95 | -11.8215 | -51.0109 | 2026-08-31 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 14dfb073-1b53-36f1-b0b3-c7e2d829ca90 | -11.1821 | -50.592 | 2026-08-31 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 4864090a-f534-339a-b4ce-3fb3edec3c57 | -7.5659 | -61.362 | 2026-08-31 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 322.4 |
| e9eb6bd0-c20b-328f-86fb-ca87cf71ea76 | -11.2298 | -51.2456 | 2026-08-31 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| b680c90d-394b-3ba5-9c4b-e8908225c0f1 | -9.7873 | -59.4479 | 2026-08-31 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4b8511bd-d8b9-3fa5-897d-d4c55b38b63b | -18.2904 | -52.6818 | 2026-08-31 14:50:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 3b2fd46e-a634-370c-8041-2f4c79a70cd8 | -10.3394 | -49.9547 | 2026-08-31 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b30330e1-29be-3c9a-bc4a-1241e0b7f220 | -14.1456 | -52.8082 | 2026-08-31 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| fb3af516-161d-3944-aec5-685f6de25db4 | -10.3205 | -49.9567 | 2026-08-31 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 63368815-55fd-3a23-98ba-39449ee4e29e | -10.1531 | -45.7438 | 2026-08-31 14:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 72c04e33-bdae-3791-8491-b50f8c5f5bc2 | -10.8801 | -50.5179 | 2026-08-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 474fd24c-23b7-3056-81cf-3aa617e3ac07 | -10.9864 | -49.6915 | 2026-08-31 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 25d6e3bd-f509-3fa1-98c6-e63b537c0a42 | -9.6942 | -65.0582 | 2026-08-31 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 253a864e-fe23-33ff-9d3c-62267f27070d | -6.7514 | -55.6654 | 2026-08-31 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| ca6a27a4-0faa-3727-b945-9d2619c53242 | -10.3391 | -49.9762 | 2026-08-31 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 68f94c6e-6848-3ded-a6e0-d1936096cfe8 | -13.9282 | -54.42 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 33880b08-0d37-33fe-aa26-8b1a6b225db7 | -11.9378 | -45.0656 | 2026-08-31 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| b95030c4-062b-3e11-a6ff-244d4353d65f | -7.6253 | -55.2787 | 2026-08-31 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 14f77989-7465-35fc-9a71-3809415073a7 | -9.5778 | -47.6003 | 2026-08-31 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| ad422aea-36df-38a6-a924-575e6ee1ed32 | -11.7028 | -47.6129 | 2026-08-31 14:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 6a72892b-b6a4-3cc1-81f7-f846d5250aff | -10.8614 | -50.4985 | 2026-08-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9d4295ff-f05a-3e64-99eb-388eb233926e | -13.8567 | -54.0759 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 125.4 |
| bc7b64b3-3156-3b10-b532-b85ef36c4ce5 | -15.2475 | -53.8876 | 2026-08-31 14:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| c4c418e6-3eee-3473-b1ed-7d570c84af06 | -5.8537 | -57.5576 | 2026-08-31 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a8d0634e-8070-305e-814f-e1c0f4f8fafb | -14.1459 | -52.7871 | 2026-08-31 14:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| ca0b25fa-3a3d-3e69-855a-b1ad1b0de679 | -10.8444 | -45.3126 | 2026-08-31 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 7e368c91-23c6-3aa6-8de1-a34d66b85286 | -9.5964 | -47.6204 | 2026-08-31 14:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 291.9 |
| 6aff7f24-4b15-3981-b6d6-445201f2002e | -11.0563 | -51.4751 | 2026-08-31 14:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| f50a8e21-2c49-3af9-9325-14fa6abc9b21 | -9.4345 | -45.6477 | 2026-08-31 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 0f6e40ce-2af4-307b-9aa4-d2c8cc5f04fd | -13.967 | -54.395 | 2026-08-31 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 558.5 |
| b1a3ab68-b4ed-3fd1-8c0c-a50e9e354adc | -14.439 | -52.5388 | 2026-08-31 14:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| fc2988c0-e7da-3fe2-a3da-43609b564b3a | -5.2548 | -55.8907 | 2026-08-31 14:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 9098068b-0333-397c-9bc7-d5f9cf26e4ef | -7.9797 | -44.2962 | 2026-08-31 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| c5a96af6-6704-3ee3-b24e-2cb80a28a2c7 | -7.3476 | -55.1945 | 2026-08-31 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0c852d5f-d973-347d-b978-22024a0f75ab | -10.7407 | -54.0401 | 2026-08-31 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 181.4 |
| 210a889e-9f87-33e2-bd8d-7ec71dd0baab | -10.9367 | -50.5332 | 2026-08-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 7a8239f1-18ce-36a4-b82f-920136c29e2f | -10.8046 | -50.5046 | 2026-08-31 14:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |


[Clique aqui para ver as próximas entradas](README96.md)
