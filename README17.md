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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a24a285-b44c-3bc3-be93-8a64e9cc8f85 | -10.48899 | -36.84572 | 2024-12-17 04:23:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f8c3dda7-9624-33c6-8183-e291a19fea55 | -7.82042 | -35.23204 | 2024-12-17 04:23:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| f588176d-28d6-302e-9962-c3ce10ced019 | -6.9577 | -42.83192 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6b0e3f2-3bb0-33dc-ac6f-9268680cd0cf | -6.16497 | -44.42331 | 2024-12-17 04:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73f66792-8943-3ff1-bf0d-10c45cdd0c33 | -6.19581 | -43.45681 | 2024-12-17 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f21cda3a-315d-3f8f-9993-f46d02676fa6 | -10.48391 | -36.84426 | 2024-12-17 04:23:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 971c2256-7386-3854-a0f0-539197cf89a4 | -10.81681 | -40.49494 | 2024-12-17 04:23:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9134f1f1-c42a-33e4-b97a-2a2ee6ed648e | -6.59704 | -44.15966 | 2024-12-17 04:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c95cf10-52d0-37aa-a221-be5dcc335dd0 | -6.92848 | -43.50887 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| ed600c50-b810-303a-857d-b75c7656cd1e | -10.65759 | -44.49307 | 2024-12-17 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da4b84a4-e49b-31f5-bbf5-bfe193244fd5 | -7.86611 | -43.0865 | 2024-12-17 04:23:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| baf8f6e1-a88b-32df-8a22-635bcd05b523 | -15.87541 | -53.27211 | 2024-12-17 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b2fe77d-0b89-35c6-9093-07463aa20474 | -17.33317 | -51.19984 | 2024-12-17 04:23:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d77845a-89ea-3315-b56a-009417d67126 | -6.96805 | -42.83351 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a165ffc7-0d26-3665-9064-3580c19e7307 | -10.15944 | -42.44323 | 2024-12-17 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0d3dee2e-1ee0-3662-9162-d2a20d8efa5b | -5.58067 | -46.14862 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27219d3f-a8fd-39ca-ba3b-bb21d2a386e5 | -15.08179 | -59.64405 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d32fb2d-4de2-37df-9f45-b2ea1de932fb | -5.98455 | -44.5999 | 2024-12-17 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99e6fdb9-2a23-3f13-94b7-67bcc4565df0 | -6.93241 | -43.50576 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 03e98fa1-0ba5-3da6-ab2e-c35d2497752d | -7.15455 | -46.69386 | 2024-12-17 04:23:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad5a6766-9e96-3fb4-be2a-959b4c5b359c | -15.10221 | -59.644 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3997bc72-95e4-3be7-aea2-b097094ed8fb | -10.45834 | -36.95881 | 2024-12-17 04:23:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 10ab27c7-cc86-3d2b-bb12-e3339d2b79f2 | -10.4892 | -36.84468 | 2024-12-17 04:23:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a062469c-ec1f-3338-bd2a-da7298a71c0d | -10.4837 | -36.84529 | 2024-12-17 04:23:00 | NOAA-21 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 366f046c-71f0-37d0-923e-baadeb064001 | -5.70152 | -47.53497 | 2024-12-17 04:23:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e5c4861-1fb0-313f-b429-74b61afc999d | -5.47582 | -46.73594 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d86ea7d-f856-3037-8038-5114de5bae2e | -5.62794 | -44.83665 | 2024-12-17 04:23:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 83dd2602-a546-3899-aadf-0f7a05450920 | -6.03359 | -42.15682 | 2024-12-17 04:23:00 | NOAA-21 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6c2a4d93-250f-3d60-be86-4306cc5e74c8 | -15.09331 | -59.65383 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb3bfd08-70c2-3817-88b4-8c5193d33b57 | -9.33744 | -40.49432 | 2024-12-17 04:23:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 21bb44a0-0104-3952-9240-a40285fcc37f | -6.34181 | -45.01365 | 2024-12-17 04:23:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 401db353-db0f-309c-823a-18862dd086b0 | -15.8789 | -53.27713 | 2024-12-17 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 857146ae-c203-3328-9b89-bbba6109b435 | -5.31744 | -46.49782 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6c50f94-ec2d-3c3c-a6bd-6a5c0277de7a | -6.20983 | -46.2223 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 535460b4-36b1-3a57-be44-91aea3cf1d44 | -12.0824 | -38.01268 | 2024-12-17 04:23:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7ecbdf3f-d526-3819-a520-634dfa8dc8df | -5.91131 | -42.89205 | 2024-12-17 04:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6aef483-4a29-34e5-b7b5-0cf40bd428de | -6.92793 | -43.51248 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6a56f328-6b68-3ebf-9212-6872994e13b4 | -6.08263 | -44.14346 | 2024-12-17 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9589c3c7-e8c9-3155-b25a-1f4aba726190 | -6.9914 | -43.5595 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18fe2a7a-c93a-3998-9fb2-1d8a6a5982ff | -15.08047 | -59.65076 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 40b51efd-105b-35ae-ba32-866feabfa0d0 | -5.63891 | -46.42102 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 509ef0f2-bf40-39a8-ba68-8b36cefb2e82 | -6.97898 | -42.8313 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a27f145-91a9-3995-b9bd-5011ed929bf6 | -15.07535 | -59.64259 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 98c847ab-e95b-312b-b4d7-5daecc44c092 | -6.97151 | -42.83405 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aea7d545-26be-3a93-a8bd-eeaa24a59d52 | -6.96172 | -42.82866 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 959789e0-18b6-3a73-b361-66221c8ef97e | -10.45315 | -36.95796 | 2024-12-17 04:23:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c908bb61-974b-388b-acf4-8bd985a41ee3 | -5.94287 | -43.77068 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 250903e5-8b08-332a-99f7-8b557dcb3735 | -16.26129 | -51.89583 | 2024-12-17 04:23:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed74c500-7aab-3b01-b10a-230578b2f0f9 | -5.98508 | -44.59645 | 2024-12-17 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08cf05fc-740b-394a-9e52-2f3cbe593bb4 | -6.64188 | -47.3497 | 2024-12-17 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fedc3222-f4b9-3a30-a204-050a5b97974a | -6.91559 | -43.52538 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eb05c600-940f-39e4-a590-a3603bd496d1 | -5.91187 | -42.88837 | 2024-12-17 04:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c83c3ae-d059-3495-bab7-6c922e3f4d10 | -5.72755 | -44.89523 | 2024-12-17 04:23:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f13bf6e-6473-3180-911b-0c217532a8d8 | -10.82093 | -40.49553 | 2024-12-17 04:23:00 | NOAA-21 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7993d9a-6bed-386e-be6e-f02f924f0727 | -6.97207 | -42.83026 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d2488e34-5c73-3aac-a6a9-d3bfb44ca0c9 | -6.98803 | -43.55898 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cb67b70e-24ec-3dea-8bb5-a8730c2446a4 | -15.08688 | -59.65232 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 505e2269-446f-3626-b373-908199ecde31 | -6.8658 | -44.77076 | 2024-12-17 04:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f004b18-05a7-3ca1-aa78-5c20bb44759b | -15.10098 | -59.64963 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6fc80c11-3445-3baf-8108-fb625d295961 | -6.25596 | -47.2863 | 2024-12-17 04:23:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a9e2aba-f5ca-3b96-a3cd-7798aaf5aab9 | -6.21253 | -46.21886 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf26d3ff-4661-310a-bded-3e08d804e4a6 | -6.09118 | -46.66515 | 2024-12-17 04:23:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd3cdd26-698e-3cb5-be5b-b3ee5555d85b | -11.0625 | -41.69098 | 2024-12-17 04:23:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c64599ac-feb5-33c8-965e-096e83a9ca01 | -6.96115 | -42.83245 | 2024-12-17 04:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e929283c-cd44-39e5-af5f-b0f90f100535 | -6.07931 | -44.14295 | 2024-12-17 04:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dc6514c-d4a2-3b9a-b3bb-24be94e75378 | -7.82278 | -35.23095 | 2024-12-17 04:23:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6d04cc45-c23e-326f-b6fc-166048fa955b | -12.08738 | -38.01316 | 2024-12-17 04:23:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 07bde9d6-dc25-37ce-8ff2-ef47e0fa784a | -7.81717 | -35.22997 | 2024-12-17 04:23:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 0c4854d7-b9d6-3a78-bc9d-2b61e5867fde | -15.07525 | -59.6437 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d0110f00-94f0-35ae-b4cb-d9e0c79de048 | -15.23766 | -59.91986 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba9dea0a-2718-3e0e-b18d-2f85fbe228a4 | -8.37256 | -44.48262 | 2024-12-17 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81c1c529-23b6-3bf6-9d8f-fb2438a734dd | -6.20367 | -46.21765 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ab2ab946-924f-300b-884d-b11fc530dba9 | -6.94814 | -43.49335 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acbf9068-98c6-3576-bf97-ac70242b1628 | -10.65813 | -44.48944 | 2024-12-17 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 305d2ea1-fa90-3c95-af34-9e8cca286437 | -5.70584 | -46.79126 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f61742f-e397-32c4-97b1-16d5e8a37517 | -6.92178 | -43.53003 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6914883e-2f7a-3e04-a02c-6a8923027fec | -6.08777 | -46.66463 | 2024-12-17 04:23:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0b9f56d-db03-399e-a0fc-538d783486ca | -10.66095 | -44.49359 | 2024-12-17 04:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96532750-1662-3097-9729-d7e85d51d4bb | -6.20927 | -46.22589 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48c9d911-377b-351d-adc4-549d6a41dd29 | -12.75059 | -48.347 | 2024-12-17 04:23:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d88560a6-39ef-3c96-9ece-e7c22ad2642f | -6.21311 | -46.21526 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff60a5ca-9b16-3e75-918a-74368b767765 | -6.20424 | -46.21406 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 341c76ed-0bd7-3712-ac38-2ed8a2e9c5ae | -5.94017 | -43.7883 | 2024-12-17 04:23:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee0afd3-7e24-3515-9e80-b48d9dc7a7c4 | -10.15981 | -42.44576 | 2024-12-17 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d4f721f6-5dfd-37f2-a259-467f21511b9c | -7.81481 | -35.23103 | 2024-12-17 04:23:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 41ccdc01-2827-36db-a18c-df2693f77c9c | -6.63779 | -47.353 | 2024-12-17 04:23:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa5cffe4-f2ca-3f07-ad22-c52fb402b907 | -7.90891 | -35.23824 | 2024-12-17 04:23:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 4265a22f-dd2b-3aff-b8c8-3dae52aaf438 | -5.70524 | -46.795 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e0f0bcc-b812-32c1-9763-255b1bf48275 | -15.23894 | -59.91409 | 2024-12-17 04:23:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81d957ce-3a2e-3cb9-8a71-7f140adc3f13 | -6.20311 | -46.22125 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e32362f-5989-3130-8886-d8a617eb667d | -5.47591 | -46.7364 | 2024-12-17 04:23:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26611a07-3bb6-3ddf-a6d8-82b0d015e84f | -10.15619 | -42.44521 | 2024-12-17 04:23:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1c060e4b-2f10-3289-8d78-57b9c679baa5 | -18.01565 | -54.43045 | 2024-12-17 04:23:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a203e614-d7d8-325e-9d6b-1644f76cd3ac | -6.21096 | -46.2151 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 054dd3a4-ee5d-3dac-80d5-a70e86b3b572 | -5.99008 | -43.48392 | 2024-12-17 04:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99868103-d027-3b03-9e4e-1061d6260429 | -6.20031 | -46.21712 | 2024-12-17 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0719f08d-9145-3e62-ac5e-9963a54a3606 | -8.3731 | -44.4791 | 2024-12-17 04:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f44bcc9c-081e-3d20-ac80-00546f7c9b10 | -15.87968 | -53.27291 | 2024-12-17 04:23:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a3ed6fdb-417b-3448-b03f-03ba3dd22423 | -6.96517 | -42.8292 | 2024-12-17 04:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7dcf3a70-1268-34ac-9bf6-717223ebef5f | -6.97847 | -43.55381 | 2024-12-17 04:23:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
