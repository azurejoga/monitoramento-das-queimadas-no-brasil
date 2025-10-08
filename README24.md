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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96cc89c4-6a48-3afc-aba1-1b1a76942816 | -13.80578 | -45.78864 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4c520ab-71be-3c58-892f-a73042595cbb | -8.18899 | -43.3353 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 96d732a2-a539-3c81-8d1a-c6514ab16be7 | -3.1351 | -40.99643 | 2025-10-08 03:49:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8a5f481-e713-3073-a83e-3eb0e062769a | -10.9452 | -51.03025 | 2025-10-08 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e357fd4-36af-38a1-8d53-49bf4efa6938 | -11.48957 | -42.47238 | 2025-10-08 03:49:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7a816943-40a8-3033-a899-84d56c2da52a | -14.10192 | -44.305 | 2025-10-08 03:49:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46878815-72f9-3afa-a66b-95a5dfdf5d3a | -11.18273 | -49.77914 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01dc9e73-c98e-31cc-8899-b1fa2fd6cec7 | -13.29861 | -48.0331 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9028ff44-8302-35ce-a247-5d0a0fa17726 | -8.77978 | -48.00271 | 2025-10-08 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97db9e56-630a-3aa0-bf75-b5b55ffc5341 | -13.72769 | -45.69723 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38dcf05b-1c0c-3487-a91f-59d73a3dc94f | -8.65633 | -44.90701 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3e0df38-e630-38fe-a6c7-877a673248ff | -8.22322 | -44.16058 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5247c805-58b1-38c7-8391-a00d152db9cb | -2.52422 | -44.12043 | 2025-10-08 03:49:00 | NOAA-21 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0230e82-e8bb-3138-832a-4b5dc9fe2461 | -11.66985 | -46.40231 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43cb8d7f-45ed-3588-b225-d1136fe79d6c | -9.39624 | -45.95414 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0265ec29-7bd5-3e41-a2af-ee25702ad7d5 | -8.2329 | -44.1893 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| bd308454-153a-3df3-8bea-60a9e736dee4 | -13.29053 | -47.15804 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9516d9b-cc27-39b4-8e69-59fbfda364b0 | -14.79856 | -41.63126 | 2025-10-08 03:49:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 668cff36-5900-3262-bb9c-c9a23f002f5f | -12.93273 | -46.86525 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0357c402-f114-3f06-8f30-6ed08a44a105 | -11.85787 | -44.93002 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5425dedb-4515-37a0-b74c-70346bd10a90 | -8.25252 | -50.09607 | 2025-10-08 03:49:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e7b764c-c934-34f0-b806-bf302452be76 | -14.89778 | -46.84996 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8fb7fde2-45ba-308b-af6e-3eccfc443d1d | -13.26088 | -47.78707 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7fc1843-18f5-31ef-8d2d-3ef5b25885b6 | -15.08584 | -46.61602 | 2025-10-08 03:49:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56dd1ecb-19b3-35f8-9750-bd3395d33a3e | -8.97405 | -47.48036 | 2025-10-08 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d1be808-6b96-3e90-83b0-49f3f6f06ccb | -11.71012 | -50.95644 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 042a005a-f4cf-3eb5-b06c-dd6afe029f77 | -13.31744 | -48.02279 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59ec80da-3d4c-3d90-bd00-95efc2efe16b | -12.71576 | -44.37426 | 2025-10-08 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7a01230-8b1f-3054-917d-9d26e7b75225 | -14.36134 | -45.23235 | 2025-10-08 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4684f97-1d08-376c-9983-486628a679f5 | -13.36607 | -47.55527 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e0fd8a0-c545-3108-88ba-93aeb7427e70 | -11.21407 | -47.77269 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb9eb74e-7141-33f8-b810-22cba2549260 | -8.228 | -44.16418 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0baa608a-8a42-3a7f-8c04-0009bd6ffd1f | -3.09994 | -47.01977 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58a2c8e7-b31c-36fb-b9dd-a1d7c6c293e0 | -12.92554 | -46.82076 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6097c1c2-9234-355e-ae52-f899b1cdaee5 | -15.24956 | -46.36286 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7b4e509-d22e-3aa7-874b-1479b9d4cfc0 | -11.44805 | -50.21672 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c18bacdd-10ed-3398-81fb-91c3ec0e095c | -11.72208 | -50.95384 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| b467a857-7731-3f7b-ae1a-fd9997bd1873 | -14.36943 | -47.73091 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1818a450-fd51-314a-857b-5e8901260d0b | -11.70887 | -46.35907 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b385e575-3d58-3257-a005-a4fc55bce2e8 | -13.7268 | -45.70428 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bab87865-c126-30ca-b8a0-9d588ec28d99 | -11.71328 | -46.36301 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dd70aa4-697f-3f9b-8616-a8db7a85d276 | -13.28523 | -48.47081 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 603a05ce-9a4e-36c4-834d-078c611c84f1 | -8.92796 | -46.59361 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 087868f4-5e70-34a2-8c25-8dfdee18558b | -11.70516 | -50.96877 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 166ee4aa-10a5-30c6-a6d5-604a0598fc41 | -11.71911 | -50.94604 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f52eec5f-35f2-31e0-a196-66b7ca00753d | -12.41973 | -45.62476 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.9 |
| fe975074-c7c6-3dce-8742-f124f15b2fc4 | -13.32284 | -48.02374 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d1bec50-8844-3d6a-b524-399b01f20987 | -11.99706 | -46.77411 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7d09c054-ec15-3612-8f03-b5a8a6fe26f3 | -11.81622 | -45.1334 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7d939e78-7c6f-3998-b12b-df055ffea82f | -14.70969 | -46.09308 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81d7d2d1-918f-3ee0-8901-181157fc5d6f | -14.88328 | -40.56238 | 2025-10-08 03:49:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 84febaa8-5474-33e2-99e5-03e21338a8de | -15.25514 | -46.359 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4586009-2d53-3d34-9007-7f8599f3aede | -11.52209 | -51.49435 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6d8a6890-7ee6-3853-9834-b3edf677758f | -13.36598 | -47.55452 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab81948f-8046-3b9f-bec9-39d826e07a62 | -12.4225 | -45.6231 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 49630453-223b-30fa-9962-01c1e32abbc6 | -11.71547 | -50.95248 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| df3aaf60-7e4b-334f-b75c-1a1c02003ae1 | -11.73349 | -50.94297 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 758004e9-862e-3218-a592-6acd8247bdfa | -14.52709 | -46.64182 | 2025-10-08 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 476ddbce-9b0b-38da-b6de-a4b13b41671a | -15.3158 | -46.16845 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 616dbd47-bba0-3cc4-a3f1-7aa1e7cfa6a9 | -8.52187 | -46.23986 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 75f93e43-d84e-3beb-9f5e-95cb7fefe071 | -13.27056 | -47.15204 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9701b47-fa7a-3bb1-9d89-e6bb3cc97d45 | -14.10121 | -44.30889 | 2025-10-08 03:49:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b96dd1a-6c03-3601-9e8f-3f023aa951c1 | -13.38567 | -47.56585 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a88f7d25-e879-324e-8d20-456341560cb0 | -3.56825 | -44.46486 | 2025-10-08 03:49:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 354deffb-0da5-38c3-b15c-d0a686833706 | -15.16917 | -45.74297 | 2025-10-08 03:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90245712-24ef-3007-81e1-bd33a1e453d1 | -11.78208 | -45.05885 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0768f581-814e-338c-90cd-9eee96142c8c | -10.42334 | -48.10001 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27dee245-278e-3aa1-8f3b-2d75156f3fe8 | -3.09735 | -47.02119 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a19a5b6-f617-311a-b589-447c96aa6ada | -14.3943 | -46.0331 | 2025-10-08 03:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c08255d-c70c-3165-839b-debce1799846 | -4.00345 | -38.33101 | 2025-10-08 03:49:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14e4844c-7622-39df-9362-de2e9170652e | -13.37988 | -47.56769 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9006737a-58cf-31ab-af06-713e65f24803 | -12.85796 | -43.81764 | 2025-10-08 03:49:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 36bdc3f1-6f78-39a1-99a8-916c27bc4afe | -8.47387 | -46.29357 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30c9ccbc-eb70-364c-888f-135f38c3964c | -11.73529 | -50.95657 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 7901252f-515f-35fc-b998-88083bd86495 | -13.72403 | -45.66662 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e2438d91-6e9d-3587-a44f-605ce6d4e487 | -8.50659 | -44.21609 | 2025-10-08 03:49:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf22997c-386b-3acb-bbf1-12d312e7e77c | -8.18756 | -43.34351 | 2025-10-08 03:49:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 23374fd7-ea48-3390-9fd3-17ad051fb8c1 | -13.809 | -45.79279 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bc0c4bb5-a71f-3542-98bc-79b7924a0833 | -14.28923 | -44.75847 | 2025-10-08 03:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c856cb94-e337-3c18-8f32-643730e211f4 | -12.32157 | -50.27406 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef1aa5b3-f4aa-3d0e-8c5c-27024db0b46d | -10.61335 | -48.67553 | 2025-10-08 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa5a6de6-a158-3a31-a64a-72c1b245de3d | -11.70763 | -50.957 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 199f89ea-4f0f-3d73-82b9-1d72279daaaa | -14.2507 | -45.86311 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa5d2b6a-48e4-3e69-abbf-43ae44efbf7c | -8.97331 | -47.48429 | 2025-10-08 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97d12c42-13a3-3f6d-abde-041070045a38 | -11.72993 | -50.96061 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 44a16ce5-6771-34d5-a8ac-659293ba655d | -12.94775 | -46.84077 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41ee6707-cb3f-30f5-b070-4aff9f389ee9 | -12.95855 | -46.83656 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3054f7e1-b3e9-3417-8354-f1a317a7ebcc | -10.36446 | -50.28706 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 67357a34-3538-3194-8f07-efab3eba2431 | -9.00788 | -45.50487 | 2025-10-08 03:49:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d94cd293-64d1-3989-bd62-4f333843e7bd | -11.6945 | -50.96548 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c184889-82ba-3238-9b46-1724227aebdb | -12.93385 | -46.85928 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7eccd2a4-c1f6-36e9-9261-e698991fd858 | -13.93957 | -43.74256 | 2025-10-08 03:49:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85bebdf-9005-3a0c-9936-73c2d8a5c011 | -11.72689 | -50.94157 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 6665a1b0-7014-3b9c-b92e-a6a5fd2edc44 | -11.71672 | -50.95783 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 2cef83bb-4642-3ad8-bac6-33a21c777eb4 | -8.67309 | -43.90972 | 2025-10-08 03:49:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2f79112-2bc0-3384-a053-619c5429eacc | -11.99138 | -46.77619 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e8ff5ef6-05bf-3a17-b7c4-9b1a4d84b001 | -13.06084 | -47.95637 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adfa72a6-b3ce-396e-85cf-81a6014b0cb1 | -12.21381 | -44.26078 | 2025-10-08 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df1b42b4-44ba-34c0-b47a-7b542cb52c95 | -11.99451 | -46.77061 | 2025-10-08 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7c254b4-30ce-30c5-afd3-50f79bc3e844 | -13.26584 | -48.04692 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README25.md)
