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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 973d9ecc-95c4-352b-a0ec-3990610f0898 | -4.45063 | -38.39668 | 2025-11-11 03:59:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44df09e0-faf5-31ae-8cb5-4ea19de64b74 | -6.56097 | -38.69785 | 2025-11-11 03:59:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 901880e2-02d7-32bf-b155-6d562828491e | -2.71898 | -48.35238 | 2025-11-11 03:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d670c7-0d5b-3f7c-99b3-40ef2079d2d8 | -5.32064 | -45.05542 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 521b11ae-c264-3740-93eb-b1b72df002f6 | -3.95251 | -43.78077 | 2025-11-11 03:59:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4d423e3-248f-31af-ac36-e63fdc5dc5fc | -5.30122 | -41.41349 | 2025-11-11 03:59:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9cad5b40-19a8-33a4-88ed-f33de30a79fa | -5.9494 | -36.76124 | 2025-11-11 03:59:00 | NOAA-20 | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dc945baf-ad64-3f5e-a292-8de76fc36ab1 | -5.40372 | -45.24585 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1fa6c0c-fe7b-339c-8ed5-c6b6879d33bd | -5.42099 | -44.65002 | 2025-11-11 03:59:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2af63ffb-8404-3eaa-9b7e-cc5bcf4a0e3a | -5.05166 | -44.11318 | 2025-11-11 03:59:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac8a0d22-8192-3772-8967-053084c1a50e | -4.90803 | -44.32536 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af6e44f6-aa29-3bff-b906-c18ef796f8d6 | -5.23359 | -40.5647 | 2025-11-11 03:59:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 91f6dd0a-345b-37ad-b9f6-bbd3cef9a345 | -6.2407 | -44.65992 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be97de2-4ee9-38a5-aae2-559124b51b16 | -4.27475 | -50.53271 | 2025-11-11 03:59:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57574c2c-3953-3995-b7c9-bad6a474b9ac | -2.96397 | -44.59675 | 2025-11-11 03:59:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a1bcd4c-7b30-3c54-9f31-5052c3e37730 | -4.91166 | -44.33412 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16ed2047-d646-3950-a587-f16dfef39bf3 | -6.89995 | -39.61201 | 2025-11-11 03:59:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9b633067-eaa9-3f1c-b8cd-b882e5a03be3 | -6.93516 | -41.85316 | 2025-11-11 03:59:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58cf6cd4-b4f0-3243-940e-e98463e2dd7b | -4.68365 | -43.24868 | 2025-11-11 03:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b6cd5b7-ad24-3705-ac5a-eb4e0c6c893a | -2.72246 | -48.34862 | 2025-11-11 03:59:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b1e7f15-3d91-3640-b841-c7a7b93473e6 | -4.71898 | -46.77703 | 2025-11-11 03:59:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5536f7b-eb36-3df4-b541-fc463edc7a19 | -6.09413 | -41.62929 | 2025-11-11 03:59:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b87f2927-9aee-340a-bb60-062ec7fb26c7 | -3.73784 | -47.65152 | 2025-11-11 03:59:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cac76cb0-185f-315b-84a4-9f1221f5bcab | -4.71815 | -46.46622 | 2025-11-11 03:59:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90bd9a61-3808-34ba-8fde-0bb3e400e788 | -4.68594 | -45.68941 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55215c4f-6519-3351-9ca0-76b2bd24786f | -4.90853 | -44.32831 | 2025-11-11 03:59:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a935c59-a258-3901-9777-fe447c400f2f | -6.08933 | -41.57207 | 2025-11-11 03:59:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 61608230-cfc1-3c2f-b07c-9c070d1812e7 | -4.67622 | -43.24744 | 2025-11-11 03:59:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73f0f5ea-f7ae-3b67-b1eb-bbcb8fb4be4b | -5.42313 | -44.8358 | 2025-11-11 03:59:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd7fc1dd-7a65-3881-903f-6f67440f5af9 | -4.64215 | -45.75757 | 2025-11-11 03:59:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6981a1f-3c7c-32fb-82c5-0395bc37e881 | -5.40517 | -46.00149 | 2025-11-11 03:59:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d545d26-f2d1-3263-a00c-3ee0947ab46d | -2.38109 | -45.74811 | 2025-11-11 03:59:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c67ab5a6-d4c8-3829-b940-489bf3776f5d | -5.12192 | -45.59903 | 2025-11-11 03:59:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e73c83e-fccc-31f2-8f39-e84bf35a5a72 | -7.15032 | -41.73737 | 2025-11-11 03:59:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a0265873-964e-36d5-984a-d0548e82cdd1 | -6.39444 | -44.50659 | 2025-11-11 03:59:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6244ceed-7c1e-39ca-9b1e-accefd6cb2db | -5.39864 | -45.24117 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1f99b7d-53ef-35e6-bbc8-ff6b06276fcc | -5.4044 | -45.24188 | 2025-11-11 03:59:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f46bccf-8cd1-3ea4-b0ce-029fd7d7c2fe | -21.4282 | -47.6633 | 2025-11-11 04:00:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 194.7 |
| 232b1da5-9f7d-342d-86da-0264032da508 | -18.3827 | -54.9942 | 2025-11-11 04:00:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f1df8909-1ec9-386f-a8b9-de5c4293cbb4 | -21.4275 | -47.6869 | 2025-11-11 04:00:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 6f4d9856-71db-3066-be05-5ac0d7f01353 | -21.4075 | -47.6683 | 2025-11-11 04:00:00 | GOES-19 | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1b946568-8cb0-37f7-ba9f-0736736b77fb | -11.71085 | -37.92036 | 2025-11-11 04:01:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa296d88-f02f-300a-a71c-1b5f1bcabfe5 | -10.50294 | -45.04023 | 2025-11-11 04:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9551e781-f3aa-3c00-881f-0998c4635815 | -10.84991 | -44.98647 | 2025-11-11 04:01:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c1b71f-9cf1-3ff5-9470-0b9d26b3c53c | -10.18034 | -39.29717 | 2025-11-11 04:01:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6eeeabc2-3977-3f1b-b81c-67b5577cef6e | -10.28074 | -36.30017 | 2025-11-11 04:01:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8e75423e-205a-3bd4-8040-f7083e8c932d | -10.36635 | -39.40044 | 2025-11-11 04:01:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa9c563b-48a7-328a-8276-6fe12f312b15 | -10.92462 | -44.61157 | 2025-11-11 04:01:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e62772d3-3ac6-396b-9167-6b3505b32cda | -11.05071 | -45.39792 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 98e550f4-c455-3d70-acf0-0d43536b9bed | -9.67076 | -43.90316 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dda9eecd-60c7-3ced-bde1-9ae908a36329 | -12.56499 | -43.90817 | 2025-11-11 04:01:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c363f185-521a-3fb0-9863-c4e1ef52bd02 | -13.67453 | -44.28176 | 2025-11-11 04:01:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63c9b8ad-3585-35c2-901f-8ad89336ade3 | -11.58285 | -44.97316 | 2025-11-11 04:01:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3489bcc9-d1a6-3138-96ff-c472bc67a403 | -10.92093 | -44.61092 | 2025-11-11 04:01:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7ce65c6-e1d1-37c4-b8cc-b7ae9ee06a0d | -6.95321 | -46.35281 | 2025-11-11 04:01:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dce4dcb2-a51d-3e0f-a905-91d120d13dd5 | -10.70476 | -44.79276 | 2025-11-11 04:01:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 156fe582-0395-3235-88da-601f03e2c448 | -13.51321 | -43.71175 | 2025-11-11 04:01:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d90808c-7942-306a-a95d-7b8a51e3fdc5 | -7.80806 | -39.84436 | 2025-11-11 04:01:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 910cb5b6-4309-39bc-ac7e-ae5cd41332f8 | -13.53446 | -42.98996 | 2025-11-11 04:01:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf3f675b-1219-31c2-adc0-19e793472d3f | -9.67147 | -43.89894 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e69777b-4d4b-395a-b392-cb14fb80b9d8 | -10.50084 | -44.93811 | 2025-11-11 04:01:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5e65d71-f5f9-3e27-b7b4-6a94efb577f5 | -8.49881 | -40.59049 | 2025-11-11 04:01:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4b7bb849-eda9-3d96-97f4-ad7a97be0c52 | -11.05539 | -45.39382 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d42e83b3-83d1-311b-9120-5ac372c1c2e7 | -9.97593 | -44.45599 | 2025-11-11 04:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8140cca1-b1c0-3d56-8954-0bd748d2a61e | -9.35732 | -40.33969 | 2025-11-11 04:01:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1e6574d4-1ce3-3bc6-a776-353b086e3247 | -7.89033 | -42.47787 | 2025-11-11 04:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7499075a-d80d-37e4-a790-2bd8d1ac8d2d | -11.17287 | -43.57845 | 2025-11-11 04:01:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8c384f7-7be7-3f1b-8337-20229dfbb652 | -11.04516 | -45.40696 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ac1c7cd1-9112-3c24-9a06-0dd5d54d827c | -13.37429 | -43.49271 | 2025-11-11 04:01:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5baeb8e-c7f4-3ca0-a64e-f39efd936ad8 | -10.41027 | -44.67327 | 2025-11-11 04:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68d21881-0ddb-360a-b81a-04a1511fece3 | -12.01546 | -43.85467 | 2025-11-11 04:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b4fbb0c-4cc6-3c81-a55e-c5c72b6b76ee | -8.67652 | -39.19124 | 2025-11-11 04:01:00 | NOAA-20 | BELÉM DO SÃO FRANCISCO | PERNAMBUCO | Brasil | 2601607 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f1ec80f-ff73-31ca-baa0-d1a837db1976 | -11.17069 | -43.56995 | 2025-11-11 04:01:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9690b4fa-6a2d-3faa-bf20-352b6ecb9952 | -11.05455 | -45.39866 | 2025-11-11 04:01:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5cd7165b-4b27-3003-ac93-fb4dfb76d3bb | -11.17003 | -43.5739 | 2025-11-11 04:01:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09423942-746a-30c8-8172-7abe980c4ee5 | -9.66936 | -43.91149 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f70d0a75-df65-30ab-a2c1-bacc6c9f3e6a | -11.57997 | -44.85628 | 2025-11-11 04:01:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02ddc43d-e9e7-3b1f-bb68-1ab8d0c81668 | -11.90729 | -43.82853 | 2025-11-11 04:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73980e0a-06b8-3539-b5e6-b43e1b09cba7 | -7.71516 | -42.73137 | 2025-11-11 04:01:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fb3e27b8-6f9a-345d-8452-165de13d34d3 | -10.28135 | -36.30266 | 2025-11-11 04:01:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 05802ff9-9051-3065-978b-4e1e8da3aa27 | -7.28139 | -45.05486 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff45d8a5-6c43-3c74-9db2-cd52d50c64e7 | -12.33563 | -43.65557 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c553f7a-ea02-3c94-843c-fccfae1c2210 | -9.67006 | -43.90734 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9c97da0-0cb3-3025-b2e1-0a9916cdc6ea | -11.57255 | -44.85498 | 2025-11-11 04:01:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d35de512-b102-3f86-a185-fffec929ffb6 | -7.29785 | -45.06473 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b15c8fc8-9b48-33c6-8b80-7454dcabbf01 | -12.33151 | -43.65887 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ce9730d-aaed-3636-a8c2-7c5fedcb65e1 | -11.81161 | -42.83558 | 2025-11-11 04:01:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 019f71c2-bf2b-385c-8a33-7e46ec80045e | -13.53843 | -42.98684 | 2025-11-11 04:01:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0d45e066-e4a0-3b73-ac90-c582497378f3 | -9.67437 | -43.9038 | 2025-11-11 04:01:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 51296e59-9e06-3569-8893-05344eb891ad | -11.58363 | -44.9686 | 2025-11-11 04:01:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 746c55a4-716d-391d-8db5-878704ca5d5b | -8.60885 | -37.72376 | 2025-11-11 04:01:00 | NOAA-20 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19df5906-62ee-382f-85ea-f71fd2bafa1a | -12.3391 | -43.65617 | 2025-11-11 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd0077fc-4034-3896-9c88-0b17ef057625 | -9.30663 | -40.48843 | 2025-11-11 04:01:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5188b9b-671a-3d7b-9987-47233f93aeea | -7.88971 | -42.48167 | 2025-11-11 04:01:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88deb4e8-a1c1-36d8-84cc-5bf26cec8a26 | -13.53782 | -42.99053 | 2025-11-11 04:01:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4fb84072-daf3-30e8-b5b6-0f67de8c08d4 | -12.01195 | -43.85406 | 2025-11-11 04:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce564869-c49c-355d-b527-af0bc62332cc | -7.29726 | -45.06822 | 2025-11-11 04:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f16a9d7-1bd5-32f6-9962-4487237c6f73 | -11.57626 | -44.85564 | 2025-11-11 04:01:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7220d47-969c-3090-a9fb-58e682fc04f0 | -9.88866 | -47.86156 | 2025-11-11 04:01:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf5e792b-a4e0-3317-a0b1-4d351462f7ed | -9.97667 | -44.45152 | 2025-11-11 04:01:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README14.md)
