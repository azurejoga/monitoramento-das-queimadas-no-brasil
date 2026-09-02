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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d6e79ef-19e7-38a8-b32b-fe63ff5b9135 | -17.78897 | -39.70573 | 2026-09-02 03:19:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 49f861a0-20fc-3b66-9146-e751bbe9f3a1 | -17.67493 | -40.14213 | 2026-09-02 03:19:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 9b991ee2-d945-3ec6-992b-6d9782fde6d4 | -17.65539 | -40.25469 | 2026-09-02 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 18b4ba9a-ca44-345f-8a23-e35f41ee9749 | -17.65569 | -40.25856 | 2026-09-02 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 59d96f58-457f-3def-ae3f-33910f9dee17 | -16.99679 | -39.49775 | 2026-09-02 03:19:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90fc7f5f-45e6-378e-8b5f-1d25fb466257 | -11.3524 | -50.6159 | 2026-09-02 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| f0ab2886-0183-3f36-8adf-9a4bca7481a7 | -11.3147 | -50.5987 | 2026-09-02 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.9 |
| f12caabe-70d8-37fa-9f6d-9baf59ab7674 | -12.1504 | -47.1283 | 2026-09-02 03:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2e10f970-2d9e-314c-aa22-f56e3303f7d2 | -11.3527 | -50.5945 | 2026-09-02 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b47473e6-9964-363f-b74a-55c58936076c | -12.1312 | -47.1309 | 2026-09-02 03:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e962bcec-7482-3db5-8812-e7d5c96bc393 | -11.315 | -50.5774 | 2026-09-02 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| af165ec7-c449-3c2d-88e2-03c8e7dbc4af | -11.3337 | -50.5966 | 2026-09-02 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 7c4d2edd-fd98-31a5-bdf4-2e152955ed90 | -11.334 | -50.5752 | 2026-09-02 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9fa04c38-806d-342a-bc7e-2087c04df52e | -11.3048 | -45.1575 | 2026-09-02 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| f0e72e73-0465-33b3-892a-88972423c60c | -11.334 | -50.5752 | 2026-09-02 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| a65b16e6-b35e-3498-81b0-abbb58f84be0 | -11.3147 | -50.5987 | 2026-09-02 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 7c121674-1985-3fea-b483-e169743e5892 | -4.3588 | -47.7636 | 2026-09-02 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c12578c4-3d7a-35c0-8d56-536a029a447f | -8.4671 | -54.7035 | 2026-09-02 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| 117a4570-3eed-385d-9fee-f15276c4e1f7 | -6.6948 | -58.7678 | 2026-09-02 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c2604437-163e-3a3f-9fcd-b798b593260e | -11.3337 | -50.5966 | 2026-09-02 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| f9892576-d07f-34aa-88e1-b16925188e61 | -8.4485 | -54.7048 | 2026-09-02 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 93e59996-76c7-3f88-bbf7-06d84aff6363 | -8.4483 | -54.725 | 2026-09-02 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 87e9fe13-8104-3768-85fd-aa1a2762ecd3 | -11.6815 | -50.1932 | 2026-09-02 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| fdfb8850-13bb-3e06-85a1-ada75c7d5473 | -11.6627 | -50.1739 | 2026-09-02 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 968ee965-5d9e-312b-807f-ac3ea6de4a67 | -8.4858 | -54.7023 | 2026-09-02 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 89cf4abf-053d-32c5-8b7d-df31e83ceabe | -8.4298 | -54.706 | 2026-09-02 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 6a0c6412-8810-3b3a-b0f0-6f28c22650d1 | -11.6624 | -50.1954 | 2026-09-02 03:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 2af00e3d-b865-33bb-8272-9c9fa241284e | -6.6764 | -58.7686 | 2026-09-02 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| fc5a33db-e0bf-33c9-9ff1-c5af40c4d007 | -8.4669 | -54.7237 | 2026-09-02 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 881a06e9-19dc-37ca-a36e-ebc2812f58e2 | -4.3587 | -47.7853 | 2026-09-02 03:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ad407d92-8796-36e2-a3a6-8ca491ab5c77 | -12.1504 | -47.1283 | 2026-09-02 03:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| ece867c4-d2b2-3827-93f9-c6c06492f731 | -7.2006 | -60.6706 | 2026-09-02 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 65c419ad-1d94-397a-945e-ad2f3f9cdbad | -10.6841 | -54.0451 | 2026-09-02 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| db86a20e-dc66-3aa4-b3e3-670edd2c2458 | -4.51795 | -40.55405 | 2026-09-02 03:34:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fa6b183-9cb2-3189-b113-3c9088b23add | -4.46854 | -38.50866 | 2026-09-02 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8d661b14-d742-39e0-85a9-f3ecce95e6dd | -3.21594 | -39.36157 | 2026-09-02 03:34:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ce8ac021-6db1-3e40-9d5c-9e786bf8ff1d | -4.99388 | -37.10011 | 2026-09-02 03:34:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| feaa3f3d-7141-3bd9-97ba-fdc80045c8e1 | -3.21783 | -39.36323 | 2026-09-02 03:34:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e0108f25-6323-3a83-9428-986ce7ef66a1 | -4.55868 | -38.45251 | 2026-09-02 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a58de076-0a9e-352e-a156-bcdd78700ced | -4.51848 | -40.55088 | 2026-09-02 03:34:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1461c33b-8fc9-3635-bb1e-6a34e904eec9 | -3.85619 | -44.06076 | 2026-09-02 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f05676d0-bd5f-3460-b834-72e55d9d0a58 | -4.55649 | -38.45378 | 2026-09-02 03:34:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0841227c-9801-3f8b-b698-6379ce645143 | -3.84964 | -44.05954 | 2026-09-02 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27f842d6-11fc-3936-bef0-440047551169 | -3.85067 | -44.05365 | 2026-09-02 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2734f469-e524-3917-bb05-40e93df1197a | -3.84306 | -44.05848 | 2026-09-02 03:34:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35122249-4b37-3fc9-b96b-6627acd0a0ba | -7.65946 | -45.86368 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d8c5b3a-2dd8-3dc4-aaac-3dc5db14d962 | -7.2318 | -42.77235 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c31d3d79-f28c-37aa-90c6-b8fc0348cfeb | -6.80192 | -46.20509 | 2026-09-02 03:36:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ae28cd5-a2da-3927-8eb5-6046b0354e74 | -7.65582 | -45.88235 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a6b9477f-4f4c-3938-a4eb-cb0f6c2bdba1 | -6.91287 | -45.71114 | 2026-09-02 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 743ed732-f4e1-3a9b-a3e7-5d3777ad9e83 | -11.1429 | -40.29996 | 2026-09-02 03:36:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a1a84662-138b-3281-9a21-56f487ef2c04 | -6.8033 | -46.19803 | 2026-09-02 03:36:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12f4c4e4-7f3b-3257-8a31-0e52af08c04a | -7.66421 | -45.87761 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9a737c5-fb88-3339-bb53-471dc7c2df6d | -9.63664 | -45.71817 | 2026-09-02 03:36:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 620c5977-4f80-3d9b-aa51-d22116dbb53e | -9.63774 | -45.71268 | 2026-09-02 03:36:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 46f0b923-48c3-3a77-8e14-41348e96ff87 | -7.65708 | -45.87593 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49a0990c-4942-3814-990d-5925ae171886 | -5.39205 | -45.63512 | 2026-09-02 03:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a103280-d11a-3175-814e-faa075b8c3c4 | -6.42697 | -46.27027 | 2026-09-02 03:36:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4e16fcd-f2b3-3a13-8111-4e13750a970b | -5.3933 | -45.62833 | 2026-09-02 03:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa18f540-4bfb-3237-a8e9-95d96cad8351 | -7.65737 | -45.87606 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 86c96976-a5a6-3aea-b042-49a9261b788f | -7.2189 | -42.74533 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 93d89e72-70ce-3ee9-a906-3650a68d32d8 | -6.09454 | -44.13346 | 2026-09-02 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2c1cd05-fefd-3862-b5f8-243d74a5382c | -9.69405 | -47.20813 | 2026-09-02 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b2ee93af-354d-3482-a556-3e23f17205c4 | -6.98104 | -35.13465 | 2026-09-02 03:36:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| ebf48bde-defc-3b9b-b7b0-e3842fafc09a | -6.8545 | -41.65292 | 2026-09-02 03:36:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a532f9dd-b879-3b50-b426-a8a0a1fac63b | -7.22679 | -42.76725 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 96178636-e640-304d-9467-e916b7f01de8 | -9.57269 | -40.34842 | 2026-09-02 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 25.7 |
| cc29b5c0-bfda-396c-a618-2b8a70c77d33 | -7.22824 | -42.75925 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 39d34d7b-c443-3bd4-863c-c5b9c78f6ac0 | -5.62165 | -42.93707 | 2026-09-02 03:36:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6bbdf115-b1c7-314b-aed7-7c5ddf996fe1 | -7.22463 | -42.7464 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d4978989-3ac4-33da-bbe3-851464d4ac28 | -6.91169 | -45.71748 | 2026-09-02 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c568305-4384-36ca-bcc1-dcefea565c28 | -7.65616 | -45.88251 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 066dec1a-40c7-3692-931d-6d0fa3fd7c62 | -6.80578 | -46.20405 | 2026-09-02 03:36:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 441e0a2b-8c49-3b08-95dc-2978c6fff4ce | -6.84849 | -41.65553 | 2026-09-02 03:36:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93b0c421-9727-31e4-8e8d-c39b51bb60f2 | -7.64934 | -45.88085 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1196cc05-67dc-3c48-a9f1-7cbc0c81e261 | -7.649 | -45.88072 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd89eea2-9adb-360d-8a4e-5d733f05d549 | -7.66516 | -45.87106 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12e3f072-7918-38b7-a9d3-3a51af1b4ad9 | -6.0936 | -44.13865 | 2026-09-02 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58a085b0-e065-34fb-87c0-87763ae68809 | -7.22895 | -42.75527 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 266f90fc-4925-3ff0-8a34-da269b308c7c | -7.6583 | -45.86967 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d3c9aa0-1089-3aa3-b271-d3ca7d98387d | -7.12259 | -40.08963 | 2026-09-02 03:36:00 | NOAA-20 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a504659e-422a-39aa-8056-5c50c2cc27c3 | -6.42566 | -46.27744 | 2026-09-02 03:36:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30976ee0-08d8-3ccc-94c1-ceabf1364c8e | -7.22393 | -42.7503 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5651980-a993-397f-9d8b-d340b81e88aa | -7.66392 | -45.87744 | 2026-09-02 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a4d6a64-22cc-35f7-a8bf-631c55531ef3 | -9.1445 | -40.50989 | 2026-09-02 03:36:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1edef623-a129-3c2d-9f3b-98e61b66d22e | -6.58147 | -44.79076 | 2026-09-02 03:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27b38a56-a80d-3142-8c1f-2135c6cb742a | -7.22322 | -42.75422 | 2026-09-02 03:36:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e30b45f8-a1f5-30a4-a047-aac50b226750 | -17.65845 | -40.25628 | 2026-09-02 03:38:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| d70fa3e8-d887-3557-80a7-d474aab8dfbd | -12.14396 | -47.12811 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 212f5537-3d97-3912-9eca-316bd3137dd7 | -12.07237 | -47.12918 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 227b1386-6869-3aaf-adf0-b92e3ed47131 | -12.13388 | -47.10891 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc7dd279-731a-3702-bffd-6b67a6233205 | -14.96259 | -48.10925 | 2026-09-02 03:38:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aca705b3-b1a3-3719-9d19-4d3e2dde3c9c | -10.89869 | -45.35179 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 8375d5dc-edae-3f0f-b353-69022fd2d6f7 | -10.78065 | -44.76951 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0cf12f98-e419-30e4-a2c8-d8fa95f0e98b | -13.40514 | -43.87591 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 751051a3-849f-3849-92e5-e9cd83fbb58b | -10.90912 | -45.36545 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ceb20b9-44d2-3659-bace-9e129dbcab7c | -15.38002 | -47.6876 | 2026-09-02 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd9b7288-2633-3df0-ab13-b2b02f5cd75e | -10.90163 | -45.36992 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4712725-f352-3155-a939-0bddd8d2387d | -10.78254 | -44.76005 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 614669e6-771f-3427-ae9d-657dccbaaed2 | -10.90085 | -45.34105 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |


[Clique aqui para ver as próximas entradas](README15.md)
