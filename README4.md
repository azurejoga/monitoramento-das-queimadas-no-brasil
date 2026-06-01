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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 421ce6c4-f06b-38b3-a5c1-7ddb682de309 | -12.556 | -57.1798 | 2026-06-01 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| edafb5dd-b57e-3224-825a-adbd7726a684 | -12.556 | -57.1798 | 2026-06-01 15:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 67da62c2-4ea2-36dc-beb6-21f2cc202d75 | -11.5647 | -54.5794 | 2026-06-01 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4064743c-bb1c-389f-907e-3294694dc1a9 | -5.52033 | -37.48384 | 2026-06-01 15:14:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 456434f8-0411-35a2-8450-4d5030577b95 | -5.52006 | -37.48442 | 2026-06-01 15:14:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1f29a465-bb73-3ff9-865c-4e6ce447c310 | -12.556 | -57.1798 | 2026-06-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 4a55be2b-74de-3fd9-a295-6fb1e6ef58b0 | -12.307 | -57.4008 | 2026-06-01 15:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 185ebb2e-18bb-32ea-9c91-6ad27fcb307a | -12.307 | -57.4008 | 2026-06-01 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 84c7bcf1-020a-3404-a398-6c8dfba52748 | -12.307 | -57.4008 | 2026-06-01 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f0c11f29-4b2c-3e33-a76d-e5dbf7aef608 | -11.5647 | -54.5794 | 2026-06-01 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 82fcf76e-bcce-3317-8834-d349bd7d5bb3 | -22.96576 | -47.13181 | 2026-06-01 15:56:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d02272d4-333c-35e4-a795-29acd2c13229 | -21.67062 | -41.2872 | 2026-06-01 15:56:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| d5709592-f632-3d29-b76b-01650bab5790 | -22.04069 | -48.23401 | 2026-06-01 15:56:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 110dfb8f-b123-31ed-8493-9e4017fdfb7e | -19.37598 | -40.2574 | 2026-06-01 15:58:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9ea5357d-b659-30bc-9775-ed0808551dc9 | -18.57354 | -40.98953 | 2026-06-01 15:58:00 | NOAA-21 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 29d73394-d5a1-30ad-9901-49b3e1de74d6 | -15.8117 | -41.82799 | 2026-06-01 15:58:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 4207e4b4-7f10-38e7-8ee6-78f11dac1255 | -20.14901 | -40.98177 | 2026-06-01 15:58:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 20.6 |
| 1d789fd8-ca31-3b21-9325-b04eca50f892 | -19.37679 | -40.25765 | 2026-06-01 15:58:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| ad20a6cc-893d-3f20-9d31-c51da0be7255 | -18.99459 | -40.35046 | 2026-06-01 15:58:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| ccc11337-5459-3e0d-abff-b26f9ff7b53c | -22.04155 | -48.23672 | 2026-06-01 15:58:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c373576c-3c9a-37f0-9d7b-a2219ab8e6c0 | -16.00371 | -41.67585 | 2026-06-01 15:58:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 75c2393c-76b1-34f2-812a-8e3fc60bca4d | -20.95802 | -43.93185 | 2026-06-01 15:58:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3f6cddeb-bf4a-3963-9ca0-bae23d5b102f | -18.64687 | -43.48604 | 2026-06-01 15:58:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46e17a21-5807-351d-91df-d3574a18b71e | -18.17518 | -40.3217 | 2026-06-01 15:58:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 9517dbda-b931-3793-9b31-34de977a972c | -15.99942 | -41.67646 | 2026-06-01 15:58:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 44bf1151-faf9-3f55-af94-2fa72ccff775 | -16.00084 | -41.67454 | 2026-06-01 15:58:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 1aef7c06-c6bb-31bb-bae5-a08662671428 | -20.26505 | -45.74262 | 2026-06-01 15:58:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ca7dada8-213e-37aa-922a-35592a743930 | -19.31298 | -40.28139 | 2026-06-01 15:58:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 188f3e9f-ae6f-3ae2-b312-9757fd6a068b | -15.46083 | -42.32762 | 2026-06-01 15:58:00 | NOAA-21 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 93fabb7c-1a89-311d-9d15-d4b37fa973cf | -19.08793 | -43.42919 | 2026-06-01 15:58:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 815dcfbc-9d23-30c5-ad4e-1faa80e31738 | -20.26462 | -45.73806 | 2026-06-01 15:58:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1929d4d7-5c6e-3ab5-96bc-1bbe0ce82748 | -16.85197 | -45.43193 | 2026-06-01 15:58:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49812dd2-7530-3fb7-b289-d9a5bd96c4fd | -17.90086 | -42.22004 | 2026-06-01 15:58:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 72da3897-298b-3b25-ad32-475b57b8ea20 | -20.68806 | -44.35863 | 2026-06-01 15:58:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a876acae-32a6-3b78-ab57-546a83ea019d | -20.15333 | -40.98105 | 2026-06-01 15:58:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 6543ed02-354a-36a7-8e12-6dd25596d126 | -19.1858 | -48.76212 | 2026-06-01 15:58:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e06bec6f-a399-3e79-8b9f-60d7b5f64133 | -19.65442 | -40.06179 | 2026-06-01 15:58:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f2035720-54b4-34f6-a8b4-a0453dbb8218 | -17.35524 | -39.58737 | 2026-06-01 15:58:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| a55a4f8f-9cde-3e2e-a56e-a18478631a0d | -18.17111 | -40.32214 | 2026-06-01 15:58:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| da4d0d31-dd49-366b-89f2-1aa0c7c09a89 | -19.01198 | -45.02088 | 2026-06-01 15:58:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53c7f203-3ddf-3f15-ab4d-ce7212c46bf0 | -18.62619 | -40.58073 | 2026-06-01 15:58:00 | NOAA-21 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dcafd071-2f3d-3476-a3a0-976bf9b17935 | -17.35416 | -39.58924 | 2026-06-01 15:58:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 223504b6-7e05-315b-b70d-8014f7a5af11 | -19.0656 | -40.08759 | 2026-06-01 15:58:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0c492538-dbd1-3b6d-bcae-7efc5a724cc7 | -19.3763 | -40.25376 | 2026-06-01 15:58:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1dad24ec-6a1b-3779-86ce-f8eb7daeb6a1 | -16.85314 | -45.43258 | 2026-06-01 15:58:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cca946e3-ea19-38b6-bb43-94b7a2caa22f | -17.93659 | -46.40445 | 2026-06-01 15:58:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75f3765c-2a5d-3c44-9f5d-37a69a47d59c | -20.68951 | -44.35742 | 2026-06-01 15:58:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| debce8f6-2d51-3a87-a00f-b26af6f88454 | -15.80975 | -41.82768 | 2026-06-01 15:58:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fdf860a1-4fd2-3806-8b68-1db6e427ff26 | -19.52545 | -43.57442 | 2026-06-01 15:58:00 | NOAA-21 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0924e2d-67da-3ce6-b56c-cf640ae30137 | -8.59893 | -47.47009 | 2026-06-01 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 60a98034-6f7e-37c0-8442-a02be9d66922 | -13.97421 | -46.0257 | 2026-06-01 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d89cb8dd-2d2f-3ba6-81c2-9003149af927 | -11.59179 | -47.44174 | 2026-06-01 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e4c8152d-61e5-3af5-a218-cfa6a4991fe0 | -8.36359 | -46.69646 | 2026-06-01 16:01:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2d45680-66f1-3b93-9681-508854a02c2a | -9.98016 | -37.46799 | 2026-06-01 16:01:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2430a75a-c2ac-3864-946c-3ea79e98fb9e | -8.65315 | -47.48418 | 2026-06-01 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 24854ce5-e185-3bcb-a41c-b96b5fc880fa | -7.75816 | -40.39432 | 2026-06-01 16:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 86007d67-3e20-340f-a4c0-7bfa869d9635 | -10.77108 | -49.92389 | 2026-06-01 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8b039954-40f9-30fc-9f92-5056a1d369ee | -10.75808 | -46.90884 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69d0af3e-c643-3433-afac-268288a54401 | -7.06426 | -36.20313 | 2026-06-01 16:01:00 | NOAA-21 | POCINHOS | PARAÍBA | Brasil | 2512002 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9269669d-1368-3318-b193-2667c15e22d0 | -10.81132 | -49.3348 | 2026-06-01 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 76088cd3-0c11-3363-a49a-3c88247740d6 | -9.13037 | -46.91874 | 2026-06-01 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 72360e45-7f94-370a-bf27-2f91db41adc6 | -9.59428 | -41.6314 | 2026-06-01 16:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 853ac598-f746-3be1-8281-460cebb84ce2 | -10.65984 | -46.31504 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 98b2ea25-414e-3fba-8a1b-8977be1c97c3 | -10.87975 | -46.63405 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14641006-8ef7-3e81-84f2-e4179b0ed605 | -10.46435 | -50.01278 | 2026-06-01 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 23d89e7f-2449-3e01-811f-10ac87c1cd79 | -9.63308 | -42.23232 | 2026-06-01 16:01:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0f517153-64bd-3292-a52e-4f6a16ada93c | -12.27673 | -43.49529 | 2026-06-01 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4cf45d25-3917-3b70-ab90-2fa1b393e85a | -9.746 | -37.06468 | 2026-06-01 16:01:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ae8426a5-d2bc-31cb-9861-e0c7049b5afd | -10.49223 | -50.00289 | 2026-06-01 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ceb03609-e298-3d49-8944-765c6e07e5e0 | -10.70654 | -49.92705 | 2026-06-01 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 5d16e0b6-bb7f-3f90-a450-b6f6d9a0e9a5 | -7.27619 | -39.25714 | 2026-06-01 16:01:00 | NOAA-21 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b99acd3c-ebbd-30dd-b68d-1d0326f6cd10 | -12.20577 | -41.58107 | 2026-06-01 16:01:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 66eda447-3d90-3ad1-83c5-23f6ab5099ce | -7.27631 | -38.93448 | 2026-06-01 16:01:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b380cb5b-865c-3188-b048-b956db2757a7 | -10.46548 | -50.01215 | 2026-06-01 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 73f29361-ddd2-3107-9d5e-d1f4ee647138 | -9.0239 | -46.65713 | 2026-06-01 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e9acc7ab-459a-36ff-b600-5ba3525561df | -10.9482 | -49.88228 | 2026-06-01 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6e841621-5cf3-3bce-87e8-2e29267a468d | -9.02802 | -46.65842 | 2026-06-01 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d1ac8c48-e2d9-3542-ab4b-4a28d1b98a5f | -10.6358 | -46.615 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5753507-bd4d-3e44-b719-dc2ede1711a2 | -10.64135 | -46.61427 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a5c3189-2343-3657-bdc7-5f437db400e4 | -9.23008 | -40.99686 | 2026-06-01 16:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 22f1f8dd-fcbd-334e-aa05-0c38d6b2a302 | -8.59756 | -47.47276 | 2026-06-01 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 81e6181f-6437-3de8-8a95-707fd2ceaaeb | -10.70758 | -49.92294 | 2026-06-01 16:01:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8749df7c-10ea-3672-bb29-3cfe178a3883 | -10.81264 | -49.33312 | 2026-06-01 16:01:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 06205894-2f85-3a7e-8958-50272c33bfd8 | -8.60417 | -47.46556 | 2026-06-01 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6de34181-0399-335c-918f-0165c17718e6 | -10.88021 | -46.63778 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47574a88-4e81-33d5-aed4-ea899c4dea63 | -8.64741 | -47.48485 | 2026-06-01 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9f4ee4a-940e-3b6b-861b-b14866d9530f | -10.12117 | -45.99615 | 2026-06-01 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 95228e4c-3438-33e9-8f39-90fdf4428410 | -7.8141 | -37.994 | 2026-06-01 16:01:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 496e82fc-ba6f-3173-bbdb-3ffdfdb8cc57 | -9.11732 | -46.90532 | 2026-06-01 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 627f60c9-da1f-3c8c-bb1d-0e1b26c52789 | -8.36313 | -46.69307 | 2026-06-01 16:01:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bbea092d-c44a-36dd-a221-ce2c0efdbfae | -9.00926 | -40.99305 | 2026-06-01 16:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f866dee4-2d04-3d64-adf1-e8592d5a5818 | -10.46618 | -50.01849 | 2026-06-01 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0e61a411-d5b5-351f-91f3-b1007737dead | -10.85578 | -45.88744 | 2026-06-01 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83dbaf52-d894-3823-bbb1-31c6ee8de1c4 | -9.03524 | -36.17616 | 2026-06-01 16:01:00 | NOAA-21 | PALMEIRINA | PERNAMBUCO | Brasil | 2610103 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a96a6a62-ec59-382a-895a-528d88e5602b | -10.70399 | -46.93761 | 2026-06-01 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| df2e6d5e-c5c7-3dcc-9064-5c716f35aec7 | -10.70966 | -46.93678 | 2026-06-01 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a4767eba-cece-3bd3-ba23-a459cbfe199a | -10.72293 | -46.95063 | 2026-06-01 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3b694f31-f1bc-39e0-87c8-efcc647b2cce | -10.27293 | -46.22374 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 34a55f75-0966-32e0-95ba-859730240c3f | -10.26709 | -46.22083 | 2026-06-01 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5d6eb363-a6b1-31b1-9515-3c41190d934d | -9.57368 | -37.1391 | 2026-06-01 16:01:00 | NOAA-21 | OLHO D'ÁGUA DAS FLORES | ALAGOAS | Brasil | 2705705 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README5.md)
