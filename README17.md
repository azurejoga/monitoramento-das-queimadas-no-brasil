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
| 58dc486b-be96-3554-a157-77c67fa708d1 | -4.94628 | -48.24614 | 2026-07-28 04:51:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89058a71-9cb5-32b2-8d04-801f49e2c0ab | -7.71021 | -46.52971 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23904870-6b4e-3cd9-982b-478f8574048a | -7.2459 | -43.14371 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e4472f2-c9e4-3493-b2f3-6f15891e9e54 | -1.50131 | -54.93265 | 2026-07-28 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 257f538b-c060-3984-a571-11cc4dc6c861 | -7.01173 | -45.42503 | 2026-07-28 04:51:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6214edde-1b3a-31c7-a1b4-1d47c7068aa1 | -7.29637 | -45.28526 | 2026-07-28 04:51:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80b9dcf5-c9d9-3750-8f5f-46f16b4c4397 | -7.24631 | -43.14079 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8b7c8884-84d7-3512-bdb1-4c9a15dd5b1c | -9.10684 | -49.65529 | 2026-07-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a089f1a-de32-3d0d-8cad-2febac62c354 | -7.00687 | -45.42848 | 2026-07-28 04:51:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81df7384-a7c4-3f13-a3f8-b0addd2ad108 | -7.45998 | -49.7291 | 2026-07-28 04:51:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ae91a0d-aa25-35c1-99e8-91835224f8a0 | -9.33947 | -47.90579 | 2026-07-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7e31699-7124-3763-a37e-fa50ee7de56d | -1.51697 | -54.53802 | 2026-07-28 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f13299c8-bf93-3649-81fc-c8bae25caf08 | -4.94337 | -48.24167 | 2026-07-28 04:51:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 600f4689-05c7-341d-9d4c-5adca5a10445 | -5.82389 | -43.48923 | 2026-07-28 04:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 204dd694-3e65-373b-8d8b-cb20634dd1d0 | -7.25175 | -43.13854 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba2b3d24-6ace-3475-836e-46e94f1769eb | -7.4625 | -41.11531 | 2026-07-28 04:51:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0bfcfd9a-715e-3848-b18e-a4fe7d04b53e | -4.545 | -47.80128 | 2026-07-28 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca4b4821-3033-32b1-a448-995e87c0a2c2 | -6.16393 | -44.64605 | 2026-07-28 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec02d191-2cef-375a-a5cc-12228a502626 | -3.26557 | -54.88055 | 2026-07-28 04:51:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8034a171-9eb2-31bc-bfef-ae6b2a4e8b3f | -9.33879 | -47.91042 | 2026-07-28 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9f5ba42-3bb0-38cb-879e-5c9670b8f9e4 | -9.52621 | -47.1395 | 2026-07-28 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eefe7899-2b74-39ed-9106-2f4efdcd0b3f | -5.48924 | -45.11769 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50d23278-a4c3-35c6-a5d2-f3cb01e3b3e3 | -7.40911 | -46.83515 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fef9394-19a8-3aa7-bd81-c180f821879d | -6.87373 | -46.00273 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fc780d2-1a42-35d8-b6de-6725fe0ac42a | -7.44174 | -49.48415 | 2026-07-28 04:51:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f43834a5-4aee-38a3-9df4-efbc23484568 | -7.7253 | -46.51063 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c18b8fbd-d492-3540-bd4a-8bb3e1d09588 | -7.40984 | -46.83009 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 516d3f32-6f0c-3bc3-aeb7-afa9e29fdaea | -9.53089 | -47.13498 | 2026-07-28 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02ec002f-81c4-3374-8e45-37930120fc88 | -5.48867 | -45.12161 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76687736-116a-3451-a387-f196f80569ef | -7.29397 | -45.284 | 2026-07-28 04:51:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d98052a-b26f-3df9-8eca-8aade880afe6 | -4.36864 | -47.76785 | 2026-07-28 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e1151056-9e07-3572-8ec3-fb3ecf686161 | -9.36735 | -44.72955 | 2026-07-28 04:51:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5029c919-75cb-36a2-b9cd-aa00e3088d73 | -6.15948 | -44.64542 | 2026-07-28 04:51:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eeb6727-8c3e-3a96-a92c-99253599e166 | -7.00745 | -45.42447 | 2026-07-28 04:51:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9093d1c8-eb0d-38cb-a7b1-99f0c829ac58 | -8.93006 | -49.25095 | 2026-07-28 04:51:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 438eb619-4f98-346a-bf98-414cd3ce5ac7 | -5.59696 | -44.92207 | 2026-07-28 04:51:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbd7cd26-03e7-3b7b-9c7e-5c28d88c0365 | -2.48207 | -47.08858 | 2026-07-28 04:51:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4b48e80-1dd6-3323-aba0-73c6bc06fc29 | -7.87587 | -46.90182 | 2026-07-28 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f57e1f7b-dfa3-39aa-943b-3bb975c9d4b4 | -9.3634 | -44.72387 | 2026-07-28 04:51:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24f6e92e-ab48-34d3-8f02-bd812fa4a082 | -7.24673 | -43.13787 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45adc110-4a12-3efc-adb6-a960678e9ec5 | -7.29699 | -45.2811 | 2026-07-28 04:51:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39658750-ae03-38e7-8ca8-d892101bef2b | -7.87513 | -46.90686 | 2026-07-28 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49cc2df1-a1eb-3161-b079-7a99b7a35f1d | -3.67572 | -49.47907 | 2026-07-28 04:51:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd2d6f3a-3c83-3363-8200-9b35a5aa4c1b | -1.67665 | -54.46721 | 2026-07-28 04:51:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23ea92ca-d3a1-33ae-8efe-5af53d55fe5a | -5.82317 | -43.49434 | 2026-07-28 04:51:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d402cec3-aaec-3bd7-8cb3-41c7cc434c72 | -6.86499 | -46.00517 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4b9fd1e-0fa3-3424-ab27-bee0ddcd7b9f | -8.80413 | -46.71893 | 2026-07-28 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e7fbcc12-4d9e-3867-a860-b82fe779f479 | -5.47731 | -45.11711 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2f8ce4a-b41a-371a-8543-b3a4f1242a8e | -6.86964 | -46.00209 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e59c5d1-5d53-359c-b09f-02a2cb39402a | -4.36926 | -47.76381 | 2026-07-28 04:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4c7b50f9-0dac-3070-8e2a-bf76f2c01c16 | -7.17144 | -59.31478 | 2026-07-28 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1ca23ab-f1ab-31d7-91cf-87e0072bb63e | -7.89543 | -48.27596 | 2026-07-28 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a7a7caa-c33c-3e0d-b7eb-d6f928b4e055 | -7.73132 | -44.5594 | 2026-07-28 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 288d3131-83fb-3af4-8c9b-74f36a6350f4 | -7.25134 | -43.14148 | 2026-07-28 04:51:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4391be0-068e-368c-8ba9-4277fc4ea888 | -5.93634 | -43.65998 | 2026-07-28 04:51:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ae13c5e-f06c-32d0-9a49-f50ff7b2e5db | -7.72179 | -46.5066 | 2026-07-28 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47068568-b055-3b3e-880e-8e0f55da520a | -6.87298 | -46.0012 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09ed5bfc-ca6b-3753-877d-54b8a2fe77f5 | -5.48497 | -45.1171 | 2026-07-28 04:51:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35096997-a354-3b8e-b4f1-6f0f283761f8 | -6.87245 | -46.00487 | 2026-07-28 04:51:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 038c16e0-a7e0-3957-96a1-0c4de5adc30b | -7.732 | -44.55473 | 2026-07-28 04:51:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 052fea69-a4c0-3cde-b7fb-dca2d61edeb5 | -9.3357 | -47.90522 | 2026-07-28 04:51:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71502da2-9c9b-3f4e-9123-526bdd91f861 | -7.89905 | -48.27652 | 2026-07-28 04:51:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d90857f4-76db-3c07-bebd-435c71242020 | -11.98372 | -45.55191 | 2026-07-28 04:53:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85e60a45-738a-3bcc-b397-80bcdc87f824 | -11.15291 | -54.1247 | 2026-07-28 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2431fa61-fac9-3841-9521-dcf8cabad77d | -14.30604 | -58.9683 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c8011d7-5066-3cb0-9688-14bb515d4731 | -15.76711 | -48.39156 | 2026-07-28 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15d3584f-6da8-394f-a8a5-6e37a916dbe0 | -15.32801 | -43.02234 | 2026-07-28 04:53:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d54149b-1c52-34cb-bc9e-88d59a0907a8 | -15.24209 | -48.58138 | 2026-07-28 04:53:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 445b966c-5a7d-361a-8112-c421d1e10a9a | -11.38104 | -48.8246 | 2026-07-28 04:53:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 384068ee-90d4-3352-8b4d-2500eff767a4 | -13.35168 | -54.28849 | 2026-07-28 04:53:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5931c134-6899-363c-be8c-37abb4dc2556 | -22.05695 | -56.52754 | 2026-07-28 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43a09329-2d29-3451-a2fc-697863b972a1 | -12.31761 | -50.35658 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11e191c9-f8e8-3d79-ab5d-a5354ee3f382 | -11.7787 | -47.08845 | 2026-07-28 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 062a8982-d2c0-364c-9044-7232bfcbfb5f | -12.32411 | -46.7396 | 2026-07-28 04:53:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85f68d6a-5e32-319e-a798-d226bd9cb0d2 | -10.67625 | -49.65898 | 2026-07-28 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bf52674-ae77-3200-b9a7-e11c9901feed | -12.30494 | -50.34673 | 2026-07-28 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9ffa3bf-a89f-31d9-969f-2f204678a7a9 | -15.77109 | -48.39209 | 2026-07-28 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a86df1a9-c60b-3d5b-bc00-61e382d29f53 | -11.78386 | -47.08156 | 2026-07-28 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f7f6df82-7621-3ae3-a3e3-b896b3f03ca5 | -10.94152 | -43.04972 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 0be56243-6bca-396f-923f-d0b8afd69ab7 | -9.10981 | -56.85345 | 2026-07-28 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 365d0004-218d-3da8-862d-45f5a97fceef | -10.3807 | -49.58072 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cb3dba7e-3f1f-336d-9cec-707bf2291dc4 | -12.83774 | -44.35383 | 2026-07-28 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e26e7c7a-1d2d-3bfa-ac4a-234fc8d301d9 | -14.27973 | -58.9926 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38c3bc3f-c886-3949-b3d3-6a967677e35d | -10.26445 | -49.72723 | 2026-07-28 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edd465d7-269a-3714-8edb-7e6a623b6812 | -10.94411 | -43.05871 | 2026-07-28 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f5f761a2-bf93-3dd4-8320-92786bdfa122 | -10.73817 | -49.62815 | 2026-07-28 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0721198-faa4-3296-b597-2ea36a00da93 | -13.29315 | -45.09946 | 2026-07-28 04:53:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| baee2877-7214-3214-b3dd-2b9525ef9b90 | -16.52535 | -47.74075 | 2026-07-28 04:53:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37fae0a8-1841-3235-bbf9-300f0bc28072 | -9.93129 | -47.90158 | 2026-07-28 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3fd92585-c4d4-35a5-858c-bcb272305c44 | -16.45516 | -48.99817 | 2026-07-28 04:53:00 | NOAA-20 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 093329be-5057-38f5-a8ae-d8d8482227af | -11.88692 | -43.82877 | 2026-07-28 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 93ee0720-f820-32cc-b999-e11fcc3a2875 | -20.65193 | -57.27512 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f19b18e-7df5-3dbf-9b68-235003210bb2 | -20.56345 | -57.28145 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25ef15e0-406c-3ba2-8563-ba62dde9070a | -22.06436 | -56.52497 | 2026-07-28 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb206a50-becf-3a37-a925-c1111d325fc4 | -15.41115 | -55.92347 | 2026-07-28 04:53:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8d986a57-f389-300e-890f-48b4018cb957 | -12.34039 | -48.22622 | 2026-07-28 04:53:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0aaf70e2-a0fe-392f-8ad0-6ccbf30cf486 | -11.77922 | -47.08474 | 2026-07-28 04:53:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 053774bf-6fdd-3e08-9dde-8a114d462b83 | -14.22944 | -58.98333 | 2026-07-28 04:53:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01244af9-ee59-3d6b-900f-987e4ca9c25d | -20.65471 | -57.27994 | 2026-07-28 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7851503-70fe-3464-9721-5b566c76748e | -10.67275 | -49.65845 | 2026-07-28 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
