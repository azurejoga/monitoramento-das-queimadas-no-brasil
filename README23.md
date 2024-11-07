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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c65f0bb8-a9e3-33a9-9b27-ff1bcd1c6544 | -6.07229 | -44.72291 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4741c1ce-081d-3a0f-a5bb-ec268d90c661 | -5.98789 | -45.36282 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 278da044-5482-3f97-aab1-c99d49076bdb | -9.73717 | -43.58761 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b9df491-9893-3e51-928d-860a903967b1 | -9.74545 | -43.57981 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 86dc0a35-87e9-3db0-bc7d-4f6049d06040 | -6.0801 | -44.71782 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 08dba194-c21b-3cfe-987c-f8a60989b5d2 | -9.74468 | -43.584 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cb0ed985-5f29-3a42-82f9-95d7386014dd | -6.0825 | -44.71753 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6264941-10e4-31be-9df0-0aeb5a778dae | -8.50246 | -42.0827 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 62f53ff6-5768-36a8-999c-f53ffff16f32 | -11.14223 | -42.73528 | 2024-11-07 03:32:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f06fa918-3691-3b7b-acc3-b68e04edcbd3 | -9.82127 | -36.37704 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 861fc770-5254-3684-b7da-85f403d1efa8 | -7.18078 | -39.10875 | 2024-11-07 03:32:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 859211e9-12f8-3f70-9151-402d12cbd0e4 | -8.30659 | -43.6217 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 328a06d4-43f2-357c-8422-5c1bc9fec431 | -6.69678 | -43.95336 | 2024-11-07 03:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 590a7ade-2743-3307-b1c6-0344b5463c48 | -9.59192 | -43.14606 | 2024-11-07 03:32:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 88c48004-bbe2-3afa-8e69-d7df8eb7d6d1 | -9.73806 | -43.58713 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 56582464-23a2-37b0-845f-3e06eecbb3b7 | -5.97998 | -45.36788 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 96ad0be8-e33f-3d60-b67c-5a2733ce12b3 | -7.77657 | -34.93876 | 2024-11-07 03:32:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e6b4e323-aa1d-3d71-857f-cc2c8cd28570 | -5.98806 | -45.36274 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| d298727a-1c50-3566-b0e0-3d389fbf6207 | -9.8234 | -36.38484 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1178d23e-8509-3d68-bbc8-e3b98b485037 | -9.14383 | -43.13885 | 2024-11-07 03:32:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 591bf083-9dd6-32ee-862a-e338c3406108 | -5.98561 | -45.37558 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 6521e9d0-d9b9-3dbb-8c31-89f1a2aa0e2f | -6.96015 | -39.82916 | 2024-11-07 03:32:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9084d4dd-39cc-3066-924c-a0c68c91468b | -9.14305 | -37.09985 | 2024-11-07 03:32:00 | NOAA-21 | ÁGUAS BELAS | PERNAMBUCO | Brasil | 2600500 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aaf1722f-22ea-37d4-a500-50b3eddcdf65 | -10.59974 | -36.96775 | 2024-11-07 03:32:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c8c80c5f-3626-38bd-be57-c557b87311f1 | -9.81974 | -36.38419 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 6ad0e381-5712-3338-86be-02dfb0e96a14 | -5.97985 | -45.36796 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 872885a4-462c-330f-a877-fc264fa3586e | -9.8224 | -41.79564 | 2024-11-07 03:32:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 367f8dda-14eb-350b-8e8c-c234a73e95e4 | -13.51916 | -43.0071 | 2024-11-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1975ca15-60b6-3279-b834-8aaa6b8aa13a | -6.07341 | -44.71693 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1519252b-aa86-3010-89d7-db2a7d843bf5 | -8.50062 | -42.08221 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c18f0e37-885b-3651-997e-015f622fd25e | -9.14959 | -43.13973 | 2024-11-07 03:32:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc3e8220-db1f-3903-9b0b-bdaf555e90da | -6.08142 | -44.72358 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a8d746e6-80f3-3eaf-842c-7488b8c64829 | -9.74382 | -43.58446 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a660cf1f-6c1c-3f28-913f-b25a1092b42a | -6.537 | -44.45885 | 2024-11-07 03:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| abbfe467-96a4-3ee1-93e5-b564bc8849d2 | -7.55215 | -38.77185 | 2024-11-07 03:32:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6c68f721-e860-3b77-a3bb-d351ec1482c6 | -5.98117 | -45.36149 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d61af3f4-f7b1-32be-a3c5-196f4e6b5bb5 | -5.9869 | -45.36898 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 4ca62a4b-06af-3ffa-bf79-d312dd863166 | -8.10782 | -35.39896 | 2024-11-07 03:32:00 | NOAA-21 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5de4507d-ca95-31d4-8d35-e998ba224af5 | -5.981 | -45.36155 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| be755281-e754-30f3-9236-99ceaf6d2015 | -5.97877 | -45.37435 | 2024-11-07 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 220bf576-b704-3b6f-af23-b6ccc1d7c8de | -6.53603 | -44.46401 | 2024-11-07 03:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3f3d874-775e-3246-a9db-c7cad3ec802e | -6.96586 | -39.82468 | 2024-11-07 03:32:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 4fe5a223-d488-3177-b75f-99b9168024d3 | -6.57638 | -43.50436 | 2024-11-07 03:32:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 359eaa49-a98e-36d9-a4db-803aa122c95e | -9.74543 | -43.57611 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15ad3be3-9419-36de-86c8-c50f0d3e7689 | -9.73635 | -43.59188 | 2024-11-07 03:32:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e7ccdcc-786e-35a3-b6ea-799c57193fa9 | -9.59427 | -43.14547 | 2024-11-07 03:32:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 06f2220e-f6a8-3180-8a8c-bd38dce92c88 | -9.53095 | -40.3433 | 2024-11-07 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f155b6b-13b7-36a7-8010-07ba60d8c035 | -11.2695 | -41.04586 | 2024-11-07 03:32:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5418289c-752e-3d68-bfd5-b293792e7020 | -9.89554 | -37.89042 | 2024-11-07 03:32:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d7fdc166-ea2c-397d-a94c-cef33e5743b2 | -8.31095 | -43.61087 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 946b4837-5463-3475-8b3d-84bb005463d5 | -8.30486 | -43.61032 | 2024-11-07 03:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7f93158-d43a-31ab-b521-61ed93c387db | -6.48649 | -44.69057 | 2024-11-07 03:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eeba4c6f-0bd1-3ad8-a819-853258eabdd2 | -7.55656 | -38.77249 | 2024-11-07 03:32:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 991889fa-ba2f-32dc-88d7-9424bdd12524 | -8.50322 | -42.07863 | 2024-11-07 03:32:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d5c19e62-5e71-3222-bfe0-e458c6d9d631 | -9.82048 | -36.37984 | 2024-11-07 03:32:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 3764e7db-eb45-3b7e-b09c-343c97e1ba63 | -16.20029 | -43.70684 | 2024-11-07 03:34:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 647c8f3f-8837-31d9-8007-001877eff07e | -16.19465 | -43.70855 | 2024-11-07 03:34:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a9f4e3f-6a20-35af-9377-d35d8dec3966 | -14.07292 | -44.14146 | 2024-11-07 03:34:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e72b8c41-ddb9-320e-bc5a-47e047be9430 | -14.07213 | -44.14534 | 2024-11-07 03:34:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91403566-99bb-300b-943a-7e087143a540 | -14.41286 | -43.18407 | 2024-11-07 03:34:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c980e4bc-8ce7-3c4f-a7c8-1a2f1d769bf1 | -15.69645 | -43.29045 | 2024-11-07 03:34:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e0dc628-7208-3195-b016-264e658bdf78 | -14.41351 | -43.18073 | 2024-11-07 03:34:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b9f9d21-d161-39f7-aabe-67fd2c50828a | -15.86796 | -43.79503 | 2024-11-07 03:34:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9097008b-4bd0-3d71-bb02-9ee5911d19d6 | -15.61207 | -43.57583 | 2024-11-07 03:34:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5ba139b-db4f-3a05-bc28-aa488ecb27aa | -16.19953 | -43.71052 | 2024-11-07 03:34:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86211bdb-d707-38ad-aa5d-232daaca6e2f | -14.96092 | -43.43287 | 2024-11-07 03:34:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 848182a2-b582-38d3-bc76-4cff5c473655 | -14.95633 | -43.43205 | 2024-11-07 03:34:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4bcd1e59-5ed3-3fb3-be28-e788d6034314 | -14.96168 | -43.43267 | 2024-11-07 03:34:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cca726a7-e982-3a80-b48f-6e860801ebe5 | -16.19983 | -43.70991 | 2024-11-07 03:34:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e93918e-3065-39d6-8a24-e571813551bf | -15.8663 | -43.7951 | 2024-11-07 03:34:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 90a48fe4-6b64-3f4f-81ec-29d786ded6b6 | -22.90096 | -43.75285 | 2024-11-07 03:36:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3618acfc-f44f-32cb-88cf-0364e6160b31 | -28.58924 | -49.44265 | 2024-11-07 03:38:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 26fd21b8-5228-3779-bc8a-97b5dea957b5 | -3.1617 | -50.2038 | 2024-11-07 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 774e10a9-9e0f-382f-9e59-9c75a0f14af2 | -2.82 | -52.9613 | 2024-11-07 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| db030aa4-7b10-34f4-8cd7-95e1abcb79d4 | -5.9788 | -45.3621 | 2024-11-07 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| e60c3387-0136-3bfb-84cd-0353df55c861 | -3.0396 | -53.2805 | 2024-11-07 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 88a4a640-1721-3f87-a541-5bedc3273ac6 | -2.82 | -52.9409 | 2024-11-07 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 996e102d-0c8a-310a-9e11-2a4877aad048 | -3.7033 | -48.9986 | 2024-11-07 03:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 59cf055a-65f4-3a1c-b797-386568b2b971 | -5.1395 | -47.7008 | 2024-11-07 03:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 40b54367-40c5-324e-9d10-2c0958b29769 | -2.6228 | -51.3038 | 2024-11-07 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d95dd549-49b7-3d85-85f4-9a093638c470 | -5.0342 | -46.83 | 2024-11-07 03:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ea7c1e3d-c190-3bb4-92ec-80c995a43dce | -2.8537 | -48.6642 | 2024-11-07 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 93de19ab-2879-3d4b-9587-3b1384918e01 | -5.9975 | -45.3607 | 2024-11-07 03:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| c6152ae6-f143-360a-8bfc-e9cfe673d9a5 | -2.8536 | -48.6856 | 2024-11-07 03:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 7b93ce94-0ef3-3b23-87e7-f345ac9bf070 | -5.034 | -46.8521 | 2024-11-07 03:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5a8c4e75-25ad-3195-bc2a-37ed8cff5ac6 | -2.6228 | -51.3038 | 2024-11-07 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| cd28911b-f3e0-3141-849e-7a1e3f0d8a46 | -3.0397 | -53.2603 | 2024-11-07 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 3461d6ae-ae9e-3087-97fa-c0850e3059ae | -5.034 | -46.8521 | 2024-11-07 03:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ad94bc52-9e6e-3b09-8cce-860706dd2696 | -2.82 | -52.9409 | 2024-11-07 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4df4e6ef-1c44-33cc-a3da-2b3046f4630c | -5.9788 | -45.3621 | 2024-11-07 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| df04bc12-2de7-3f04-a052-9e715b4d8f92 | -2.8537 | -48.6642 | 2024-11-07 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 90de761d-6477-3ec9-b2a1-4667f57fe625 | -2.8536 | -48.6856 | 2024-11-07 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2dd846db-2858-305b-9b8b-751e9476c870 | -5.9975 | -45.3607 | 2024-11-07 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 3329c3d3-c917-30be-a8a8-9e941f5d6ff5 | -5.0342 | -46.83 | 2024-11-07 03:50:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d08aa56b-5c94-39ee-809b-f427f05b93a6 | -3.7033 | -48.9986 | 2024-11-07 03:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f79be535-129b-3e84-b333-fba933a6ba73 | -2.82 | -52.9613 | 2024-11-07 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d86c71ce-7d1e-3d36-bfe7-c9dab7707696 | -2.8386 | -52.8998 | 2024-11-07 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 55382bec-e121-3868-9374-f164b970f34d | -5.0342 | -46.83 | 2024-11-07 04:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 06580271-1d9a-3d8d-8906-b1c04bea927e | -2.8537 | -48.6642 | 2024-11-07 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 2917c9af-8bf3-3572-913e-8ba45f249dd9 | -2.8201 | -52.9206 | 2024-11-07 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |


[Clique aqui para ver as próximas entradas](README24.md)
