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
| bfeff526-c90b-3fd8-b48d-da6ab6f4fdd5 | -3.3389 | -50.49966 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e022011b-0b1a-38bd-bb22-cf23186676ca | -1.83705 | -46.28256 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb667ce3-555d-3446-8475-7b7d900c8906 | -12.96493 | -42.44251 | 2024-11-19 03:53:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6d167bc-b4eb-3fa5-90db-70588535c9f5 | -9.69018 | -47.87189 | 2024-11-19 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 932187f8-354c-376c-afd0-56ddcce429c6 | -11.53446 | -45.00738 | 2024-11-19 03:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37f81047-9a8a-3ab0-8b93-69b1d42f0100 | -2.21966 | -46.47524 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a297e9a-3543-3840-b658-123348421093 | -3.48313 | -48.2512 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 17e2ce7d-32fd-325c-b369-cc4554d04dce | -4.94623 | -47.80266 | 2024-11-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74d31d15-bcbe-3958-8284-0744b08b4e80 | -5.98073 | -45.36331 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 979c8821-9d72-3101-bd9c-3404243bdf23 | -9.99925 | -44.07601 | 2024-11-19 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63617ce8-ff8f-3f7b-86bb-4ca1eaf8b398 | -11.8843 | -43.81341 | 2024-11-19 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45608933-ce0e-38d5-963d-9c0321f3709a | -3.04176 | -49.46959 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9606c099-9158-3ab3-9a57-6cb19c968d3c | -6.56478 | -39.43454 | 2024-11-19 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81caa0a4-275b-3148-8552-22fc1602d358 | -2.0026 | -44.79497 | 2024-11-19 03:53:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6ddc026f-5039-326c-b535-54ed63730ab6 | -4.11328 | -43.59152 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d4f8449d-b70f-3418-ae5a-a791391c1475 | -2.47534 | -49.12172 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 13af6b2e-8232-31ef-bf3b-28038132fe9d | -2.22444 | -46.47948 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3901f0d7-018a-3132-814e-01bbec5cbc97 | -3.38008 | -50.34165 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffa05539-a7fd-324c-af06-7cc672c73819 | -10.96988 | -44.5332 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 227f9247-66e1-3f44-8000-45e1cddff004 | -5.54726 | -47.05566 | 2024-11-19 03:53:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| adaec346-f9e9-314c-891b-15e4fb17b1f3 | -6.93161 | -45.09284 | 2024-11-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| faf8a67e-ec47-34cc-92bc-55acc7a58f59 | -3.88697 | -43.15461 | 2024-11-19 03:53:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7982a6fd-4c36-3beb-85fc-8f1b1dfe04e2 | -4.55008 | -48.00552 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05a7d7b6-3379-3097-94ab-66896e7e9e65 | -4.392 | -47.77355 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d1c9fbc-9141-37d0-bc60-3ec60252c147 | -4.68309 | -41.11041 | 2024-11-19 03:53:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9c24dcd-9f7e-370d-a835-9cd16ec3ed57 | -10.4573 | -45.07423 | 2024-11-19 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d84f8495-cd2e-3d8e-8b01-ccf223e0b40b | -4.30142 | -46.74398 | 2024-11-19 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cbe6b8a-94f0-3870-973c-ad499e55d150 | -4.79747 | -37.80694 | 2024-11-19 03:53:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92c1d8ec-1989-3662-9ebb-0da5c62b6628 | -4.11816 | -43.58829 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| fd70f21a-624a-3009-9e10-634813800f14 | -3.66027 | -50.45013 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b34dc7e8-737c-37b2-8bae-e23641766b84 | -4.16086 | -40.71525 | 2024-11-19 03:53:00 | NOAA-20 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| acdce19f-25ac-3a44-8df2-e337e7700a6b | -4.58553 | -48.49578 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57788a3a-7b91-3a1c-bf94-1f77e99a322d | -3.03822 | -49.46433 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5161886e-4063-3530-8a42-ff598e32be28 | -5.72154 | -44.80798 | 2024-11-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c90b1bf2-7571-3e80-95ba-06bb394e68a8 | -5.16947 | -45.71532 | 2024-11-19 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b721faeb-4475-3bb1-becf-5bc516b1aad4 | -3.43474 | -50.30301 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e5af064-f46e-3d53-8080-82d9578cf4ec | -3.50441 | -50.23852 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d4db99d3-00ec-3cc0-a22d-98fdf1b02254 | -6.98411 | -39.661 | 2024-11-19 03:53:00 | NOAA-20 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1b837a38-fa57-3555-b367-0092f63825b5 | -2.68454 | -46.23222 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a76538c0-fed3-3758-9649-d634d2de5250 | -3.48245 | -48.25533 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6417b92d-ecf2-33ed-af28-61c5f1613331 | -6.695 | -43.95312 | 2024-11-19 03:53:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 57ff8e58-0827-39da-871d-adcdee12a266 | -10.84538 | -44.25917 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62c82af1-7420-37c4-8172-fb785ba2f1d5 | -3.29729 | -43.54169 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35ce89b4-93aa-3a51-aa2b-2e3ceff42234 | -3.04283 | -49.47547 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 239f7208-46b3-3d0f-84d2-de208f766558 | -5.50872 | -41.07325 | 2024-11-19 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9dd2fa51-355a-3865-8e50-2af6dd85e181 | -10.54018 | -44.67271 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a462c005-8b0f-3ee3-9f18-35490caadea9 | -7.11653 | -41.36532 | 2024-11-19 03:53:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 328f4307-42ca-3387-9275-e2c330575186 | -10.72487 | -44.50007 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee3ec89-1cd6-3aed-b9bb-8442300ab7ed | -13.45343 | -44.01953 | 2024-11-19 03:53:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 187d31f8-023f-307d-8796-ab2f959c213e | -5.95038 | -39.66964 | 2024-11-19 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 39e65210-0ced-3631-9f0c-9014a90b9600 | -12.64126 | -48.8167 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 865cda48-1ae1-3ce8-9c69-9c2b2d037ba5 | -4.54942 | -48.00938 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d0cf280b-529c-30a2-be8c-bd78b9caeb84 | -3.03734 | -49.46937 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd9c1f9c-a016-3053-b78c-9c99ea56c23c | -3.84011 | -41.56695 | 2024-11-19 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fff383be-1d8e-3737-ba73-83c51e174192 | -3.76147 | -42.73008 | 2024-11-19 03:53:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20411352-01bb-32be-87c7-947c6cb64aa3 | -3.36057 | -50.82387 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aec73131-9f76-3339-8264-2825f483bebe | -4.09881 | -51.06524 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5eac0638-3c95-3cb6-b2ba-62105a60ecbc | -12.27528 | -43.52457 | 2024-11-19 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 00376e29-81cb-3065-8e18-a1d225967c89 | -10.4182 | -44.48418 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1ac4a76-460f-3555-addd-ce2d00c9a8d5 | -5.71756 | -41.63796 | 2024-11-19 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 30c9763e-51c0-3309-b09a-0d2b8d95daf6 | -3.70389 | -43.4711 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f96ea91-a9e8-3c0b-b684-1fc87932d7c0 | -3.3197 | -50.49033 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2e29b44-c932-30b7-a2df-b45effc7eef6 | -12.1159 | -40.50998 | 2024-11-19 03:53:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 99ca5d2b-7d49-35c3-8989-098c3717886e | -7.22948 | -39.96059 | 2024-11-19 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ff0d65f-95c0-33de-94e2-45591301f9c2 | -2.68506 | -46.22908 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2bc2d2f-4fc6-38de-abde-2740b13bf06f | -1.399 | -47.45225 | 2024-11-19 03:53:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2e630705-d488-350f-a57f-e1873c109dd3 | -3.84085 | -41.56245 | 2024-11-19 03:53:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45dc637d-4bad-339a-87c2-8e7b1b648722 | -2.71416 | -46.08421 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a662cddd-547f-3d86-a425-424f21faf4de | -5.8728 | -40.17863 | 2024-11-19 03:53:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 266a8bee-cbfd-3485-9d59-8fdf71ae6ff9 | -4.57712 | -48.01824 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7090285c-0fc9-36c0-b36d-61673d84c643 | -2.0017 | -44.79846 | 2024-11-19 03:53:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6124186f-9b17-39ac-b4d4-bc5b7979accb | -1.8486 | -47.83275 | 2024-11-19 03:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cedbaa34-b3dc-3353-9c98-090c95f8cc5d | -3.32537 | -50.49764 | 2024-11-19 03:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 203108e0-2996-3e54-8ed6-5bf9a1d970a1 | -3.51096 | -50.24009 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71dcbba8-b4fd-3d34-8ac1-04e434d679ce | -3.04091 | -49.47467 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be62c877-e5e5-3b30-81ef-6e1bb7885a98 | -4.37952 | -47.77919 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58377566-e550-378b-82cc-28a8313618e7 | -9.68861 | -47.87272 | 2024-11-19 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d2cd797-6786-3af6-a07a-287804271ac0 | -3.55355 | -51.53671 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2f5be69e-1c53-3903-9c49-462039843f80 | -4.54875 | -48.01326 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e9de0d91-877d-3099-8d2f-ea49f002d556 | -4.55442 | -48.01429 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 391adb51-1d16-322e-9ffb-d5f6e5af56ee | -3.97888 | -49.92637 | 2024-11-19 03:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23df37f4-61da-38b2-8791-0d338d51d189 | -5.9706 | -45.36678 | 2024-11-19 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| e980c7cf-b21c-3a98-aa34-8f632d0cfdc5 | -2.49149 | -49.02712 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2940e07c-9413-3ec1-9773-435f2959aa14 | -2.71466 | -46.08119 | 2024-11-19 03:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed55e530-454d-3ee7-af06-ad75243e9d8a | -4.10788 | -45.63469 | 2024-11-19 03:53:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 527bdc4b-db90-3f65-8b15-14be747dde49 | -5.11903 | -44.33882 | 2024-11-19 03:53:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0c27745-3fd0-31ff-8a26-f84f3c7b5f63 | -11.90821 | -44.37585 | 2024-11-19 03:53:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aab9db4e-a5c9-3f1c-8765-0cedb40fca1c | -11.88811 | -43.81409 | 2024-11-19 03:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40c94130-420b-3ca1-9926-70cd2e7b0894 | -6.29114 | -43.85045 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7c34050-1738-3655-a68c-154d1daa3f26 | -10.68671 | -44.00811 | 2024-11-19 03:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98cfe434-4d68-352f-b878-f8ecbb97333f | -9.84774 | -48.56965 | 2024-11-19 03:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9780ce00-0123-3fcf-9121-b62802d7b6b5 | -7.11721 | -41.36663 | 2024-11-19 03:53:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| be2b7dcb-a14e-37ae-8b97-f4df50136585 | -9.89254 | -44.4296 | 2024-11-19 03:53:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06bb097d-7b4a-333a-95e2-346cb33ca583 | -4.3968 | -43.00122 | 2024-11-19 03:53:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a87ad8c-9fcd-31d9-8230-84b71eef5934 | -5.72077 | -44.81255 | 2024-11-19 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c292383-d1ce-30be-a53d-7e007d4f5aa2 | -4.57946 | -48.01874 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d1c1307-f639-3912-8504-a636530c6946 | -3.4357 | -50.29735 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcefd618-d814-33a1-9f96-7a044e5ff0b8 | -4.94555 | -47.80651 | 2024-11-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 990edeff-fa38-3180-9bd1-c4d0a8621054 | -3.51301 | -50.2282 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b1417c53-6b85-3fcf-9cc7-b773963ec88b | -5.95519 | -38.63243 | 2024-11-19 03:53:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
