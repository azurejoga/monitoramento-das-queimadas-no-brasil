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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 160679f2-8309-3412-81da-fda8a0365edd | -8.99401 | -65.4352 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92715187-7ef9-3748-916c-c6b12b8f3b96 | -9.20758 | -67.7806 | 2026-08-28 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22a1ffd1-59cd-3dac-9b96-01eaab5e0d49 | -8.63755 | -66.53343 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 295b6ee1-3488-3f49-a152-c26394769e6c | -10.50261 | -64.50811 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 32569fa0-ca0c-378c-8ffd-2289dcf2a98a | -9.52613 | -70.50407 | 2026-08-28 06:31:00 | NPP-375D | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7488ebb9-8819-3c51-86a8-03b388f6b7cc | -8.39411 | -70.73779 | 2026-08-28 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 855eafca-2b54-39e1-b953-8b089a9b2065 | -8.39255 | -70.73913 | 2026-08-28 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6664b592-e0c1-3bf2-8de1-dfa1de8f89de | -10.49728 | -64.5112 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5d964253-23aa-3892-a03b-9f3b8b5f3056 | -8.99296 | -65.44296 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d68d4e6-3f34-3e30-a211-d409dd0b77c4 | -8.63666 | -66.53989 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b941d763-cd94-39a5-8836-219f36dcaf18 | -8.87989 | -66.90862 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02aa3ae0-4bad-3aec-8db4-45a4b35ba3d0 | -7.57731 | -61.32752 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8701a5a-6d14-38df-8229-a1d4367249d3 | -8.6014 | -70.20598 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 755ca05b-89ea-3caf-9548-0de4e14cc57c | -9.20837 | -65.79327 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c56ef36-45b3-3a1f-b497-83560a5c516f | -7.57969 | -61.32261 | 2026-08-28 06:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3862a86d-f956-3a60-918a-b1c33942ead5 | -7.71944 | -70.09772 | 2026-08-28 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40a1d39f-0c88-374e-a10c-7172627e867b | -7.39999 | -72.62465 | 2026-08-28 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74dba2a3-2cd3-337c-97b8-43ac93f78d14 | -7.53561 | -70.02335 | 2026-08-28 06:31:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc0c07a1-3c70-3474-a5bf-ff25e64ce823 | -8.59678 | -70.20905 | 2026-08-28 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0bd3f2-38e0-300f-989e-bae2a431f762 | -10.49702 | -64.50241 | 2026-08-28 06:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 30cfb6aa-61cd-33e2-bb26-2eac7b364130 | -8.98676 | -65.44607 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71059bca-4883-3aa4-b0f8-6ffd87abc1ef | -8.95345 | -62.39739 | 2026-08-28 06:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28debffd-dea5-30bf-a068-d03dcee1c11a | -8.88115 | -66.89935 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66f5e1eb-f342-39ba-82ad-003ef4086537 | -8.87516 | -66.90481 | 2026-08-28 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59d93b42-98d8-394d-81e5-181ee914920b | -4.85074 | -45.39314 | 2026-08-28 06:33:00 | AQUA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 011bcfcc-a70f-37cd-9482-2b0b5bda6f81 | -4.84193 | -45.39184 | 2026-08-28 06:33:00 | AQUA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4e8438b7-335f-3f6b-b7eb-8c59d7d38d3a | -5.15671 | -42.75145 | 2026-08-28 06:33:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5808f7b6-da7e-3912-ac8a-b7bccbd745b8 | -7.25858 | -45.86697 | 2026-08-28 06:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 6870e76f-9786-379d-8a2b-330b940bf509 | -5.34102 | -45.15517 | 2026-08-28 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| f6f0c43a-d9ae-3c88-bf7c-feb8580c5811 | -5.33969 | -45.16392 | 2026-08-28 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ee1eabe5-15f0-3a23-bf14-d38678193e5b | -7.08942 | -42.79377 | 2026-08-28 06:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 663fba61-f407-3404-93f4-276cf0365900 | -7.25993 | -45.85812 | 2026-08-28 06:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5e1e265f-854c-31ce-9962-518369b55780 | -5.81645 | -46.21911 | 2026-08-28 06:33:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff2ba852-98d8-378e-9d29-828d7f9e8636 | -8.08076 | -45.81223 | 2026-08-28 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 100a0384-0f63-3818-ada2-2c3b38f94658 | -8.17365 | -46.16741 | 2026-08-28 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bd36c443-8338-399d-9276-ee2fb6e5f83b | -3.45899 | -39.5739 | 2026-08-28 06:33:00 | AQUA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| a543a631-7b62-3380-bd1b-4364e53e88ea | -7.24978 | -45.86564 | 2026-08-28 06:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| c22f3b6f-705a-3fc8-b460-f75868ddf0be | -7.26947 | -49.84693 | 2026-08-28 06:33:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e686b1ba-2396-3552-b56c-62c12a3131fb | -10.55919 | -69.24438 | 2026-08-28 06:33:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08b549aa-7709-3684-a015-c6d11f1ac2ff | -8.08415 | -45.84885 | 2026-08-28 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f926d987-f878-31c9-8c40-58d94ea300e6 | -7.8707 | -46.09419 | 2026-08-28 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ea73f058-12ff-377d-a75b-027ed6b7af54 | -8.08281 | -45.85766 | 2026-08-28 06:33:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5e82845b-0852-3d48-a89e-3257fcf1aac5 | -5.5097 | -43.97791 | 2026-08-28 06:33:00 | AQUA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0b54a146-10bf-37d2-92be-6b6bac495d6e | -4.84939 | -45.402 | 2026-08-28 06:33:00 | AQUA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 284c26a2-d873-3495-8a09-777186cb8831 | -7.27106 | -45.34984 | 2026-08-28 06:33:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d4376c8b-2d81-33db-8a1e-bb3c62283ee7 | -5.34235 | -45.14642 | 2026-08-28 06:33:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87523b7b-4717-3acd-b729-55efbb8c1e00 | -7.25113 | -45.85678 | 2026-08-28 06:33:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| fccfe2e1-20fa-3c54-ba46-a832f1ac7d24 | -2.7308 | -47.04081 | 2026-08-28 06:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 26ea5546-f354-3885-803a-559e8cf4026b | -9.97971 | -48.59184 | 2026-08-28 06:35:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 06fbb4a6-55be-32e7-b12d-557b36d77bb9 | -9.65633 | -48.29725 | 2026-08-28 06:35:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a7c70323-e7f5-3ed7-a9b3-f58f024e682b | -11.82543 | -47.21417 | 2026-08-28 06:35:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 45af9ca9-1e3e-3b39-8be3-0bfd98894b54 | -8.59078 | -54.77091 | 2026-08-28 06:35:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 4203132f-b0a0-3bbf-b78d-cfb61014f7a3 | -11.8343 | -47.21554 | 2026-08-28 06:35:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 737b9863-144b-307a-842a-a5bc0b15ce59 | -11.01144 | -45.06713 | 2026-08-28 06:35:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66afefc2-df40-3367-b640-a1b9c5fd8a62 | -11.65741 | -46.73483 | 2026-08-28 06:35:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 857ecd01-8da6-3b3f-b9fb-721d4e91d7f5 | -10.90344 | -50.51033 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 6aa5676e-a745-39ea-967f-25013fcc00cb | -11.48327 | -45.06543 | 2026-08-28 06:35:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12eda200-c5ad-32b1-92f2-831261185d28 | -10.95003 | -50.52377 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6d9b6c4a-82dc-34aa-bf1a-e6c958703a82 | -12.50272 | -43.80914 | 2026-08-28 06:35:00 | AQUA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 05c22594-5519-33a3-8b4f-034e6b4c2d9f | -12.43293 | -43.41097 | 2026-08-28 06:35:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 6d79fbea-1260-3811-9ad7-43ad71ac7bd7 | -10.99508 | -51.07927 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d95c9e57-f669-3cfd-9998-8f7f07a49d78 | -11.22909 | -45.0431 | 2026-08-28 06:35:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f5e54b9b-6cbf-3621-91dc-7d811eefcbb3 | -12.42319 | -43.40961 | 2026-08-28 06:35:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5f0826ad-b3f4-37f2-b85d-b0e37964ad8f | -10.78144 | -50.628 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 1e5379f1-f1c6-3a9a-adce-0b5e811c6ce5 | -10.91757 | -50.51829 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 9f0a7c78-b573-3142-8960-37ed626990b2 | -11.16008 | -51.19947 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4de3d0da-2189-3a27-8e06-9732ed0b515a | -10.91521 | -50.53225 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| af23142e-6c63-346c-8366-f2a4c3940ef5 | -10.75938 | -54.02993 | 2026-08-28 06:35:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e98d6a9e-ffba-3b5b-a79e-c7097248df3b | -10.98379 | -51.07732 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b9845f74-e93e-3bc1-942f-df6ec4e09717 | -10.9946 | -51.08475 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.4 |
| eeb5559f-118c-3f46-963a-a13cee26188b | -10.92839 | -50.52011 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| df71878e-b025-375f-9bb6-e96c0d81f7b7 | -10.98125 | -51.09267 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7a1db683-f8f3-3ca8-877f-5986f3cec903 | -10.99255 | -51.09462 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 72fedc63-b891-3960-8b94-2f03d261128b | -10.76025 | -54.03735 | 2026-08-28 06:35:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 58d5574c-7038-36ee-821c-7b2dc4c1aa2d | -10.89262 | -50.5085 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| bd17cbc1-0d59-3610-9f9b-ae593420d3e1 | -12.01834 | -47.16364 | 2026-08-28 06:35:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c3734a7c-1d9e-310b-ad20-1a1bc25aea13 | -10.92604 | -50.53408 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 4c3f70c9-27cc-3c65-8cc9-7db4fe832be4 | -10.801 | -50.64605 | 2026-08-28 06:35:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6ae03a18-0633-3e74-92c6-fbfbd3881c0f | -11.63982 | -46.73212 | 2026-08-28 06:35:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 25b84c9b-75c1-38ba-a789-23a2a246950c | -10.93921 | -50.52194 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 23bf278c-e61c-3489-852a-21d7a94b8db6 | -10.89033 | -50.52246 | 2026-08-28 06:35:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8c6c4ce3-2527-323d-b8e5-43d2328c4dc0 | -11.02032 | -45.06844 | 2026-08-28 06:35:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2a707f6a-0709-31e9-a2fa-4f1689111702 | -14.89494 | -52.59478 | 2026-08-28 06:37:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| cdc23f5e-f47e-3e8e-a269-503e8a93c036 | -13.85433 | -43.64272 | 2026-08-28 06:37:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f5fe9da0-8eb0-3cc5-a454-80789f4849b9 | -14.88675 | -52.60447 | 2026-08-28 06:37:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| dbe6e1a1-e48d-30d3-ad28-2ee09601ce7d | -12.77425 | -46.45258 | 2026-08-28 06:37:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9b54b7ac-b530-3b98-9a9d-5c8cc2a204d8 | -13.86568 | -43.63278 | 2026-08-28 06:37:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 04b3fa7f-370d-3fd7-8ac2-0ab89794bd0a | -11.23086 | -53.99416 | 2026-08-28 06:37:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| ac8c2d4a-bd5e-341d-b4a5-f4340c180079 | -13.31579 | -48.20953 | 2026-08-28 06:37:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c985fe5a-3b2c-375a-a602-03407a8659b0 | -15.52774 | -41.92883 | 2026-08-28 06:37:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 21ff7eae-61f3-3ead-a94b-78dd579d519c | -12.78436 | -46.44501 | 2026-08-28 06:37:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 3c8e0b96-5c68-39df-8407-985957b6fb9e | -11.28295 | -54.03012 | 2026-08-28 06:37:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 679d589e-9b6e-3e17-a3da-a88567c0ee7b | -13.86411 | -43.64411 | 2026-08-28 06:37:00 | AQUA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| f898fd92-9e54-3e72-a6ba-d6dcd395c668 | -12.29282 | -50.59363 | 2026-08-28 06:37:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 96c8e7d5-a87b-3d3f-b9dd-a730f149f3fe | -14.18603 | -52.83267 | 2026-08-28 06:37:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5dcc2458-ad04-31fe-af68-2d66e36f266a | -12.7756 | -46.44366 | 2026-08-28 06:37:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| cd0caae7-f22a-3a0c-a64f-c69f957c2667 | -13.31731 | -48.19977 | 2026-08-28 06:37:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9479bc82-fd9d-338b-85ef-aa1815ce5f31 | -14.60966 | -47.98329 | 2026-08-28 06:37:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9c485190-5d57-3272-b7a7-1d7aeb0fe818 | -12.78301 | -46.45393 | 2026-08-28 06:37:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6515de8f-c7ba-3176-b994-c9e75f4b9a30 | -15.5297 | -41.91311 | 2026-08-28 06:37:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |


[Clique aqui para ver as próximas entradas](README69.md)
