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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a90883ba-9749-33ca-84b5-74438954b103 | -5.09477 | -46.22175 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3406d7df-bc1c-3c18-b72b-c0096fd05ba1 | -4.97938 | -46.0387 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 521bcf8d-98cf-3a7c-860b-a57f9832a72d | -6.14752 | -47.28298 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8f031a73-831e-3566-acf6-eb8b49b13814 | -6.00352 | -40.9806 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 20acdb17-19f1-34d2-861d-76415f068495 | -5.96123 | -40.91716 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03c4b55c-00d2-30a5-af89-169ca284b3f0 | -5.88522 | -43.42462 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad85f77b-8e53-314e-a668-bf0500b858b7 | -5.99103 | -40.98095 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b268d0ca-2c05-3675-8fd6-c486b74720c7 | -3.56457 | -38.88042 | 2026-10-09 03:42:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7f07dd99-577a-30a6-af30-c4fc07d4d5eb | -3.03454 | -42.11049 | 2026-10-09 03:42:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e31b83b-da73-30ab-970f-7fef79cdddf9 | -6.24388 | -45.32915 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1bdd03be-3f70-3ff3-b74c-b3e9afd39660 | -4.01747 | -41.76969 | 2026-10-09 03:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e0c4f4b2-aeb5-3cfd-9af5-32e9dd66e0ad | -5.09876 | -46.21885 | 2026-10-09 03:42:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d64ea2c-9706-3899-bec9-18c1292c599b | -5.74735 | -43.27145 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96e259bf-2865-3b96-a1d8-269efb4b5d83 | -6.15803 | -39.44964 | 2026-10-09 03:42:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9dc14958-9541-39d5-b7e0-1447ecd5cf1d | -6.15384 | -47.27905 | 2026-10-09 03:42:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| fa724d25-8062-3f02-848e-6ee56134cabb | -5.18755 | -46.22287 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 913836ac-2abe-3e07-99a0-217241334258 | -6.42484 | -45.94622 | 2026-10-09 03:42:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38916301-a396-3fa4-a85e-75d306b45dd4 | -6.00129 | -40.9776 | 2026-10-09 03:42:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 00c1335b-4d59-31ba-9126-741ed100c65c | -5.87986 | -43.41712 | 2026-10-09 03:42:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 44eb7c47-1825-3545-abf5-88ae9950d5c4 | -4.98224 | -46.0461 | 2026-10-09 03:42:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3989047-640c-351b-96da-28937552c48f | -6.25016 | -45.32993 | 2026-10-09 03:42:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 008230a3-e4bd-3826-a86a-8f309b4193c8 | -5.87045 | -35.55642 | 2026-10-09 03:42:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86fc72ab-bd6a-3491-9681-9b7e27004dfd | -7.40998 | -44.76068 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4db0915d-9870-3033-87ab-6bd94f95eb21 | -11.00282 | -45.42045 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 698a84dd-79b0-31b1-a5a4-c86357e98666 | -8.90187 | -45.22038 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 38dd340a-9a58-34f2-80c7-5dceda14fd14 | -10.29712 | -46.60397 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe507e3c-c953-3741-bfb4-87eaa065483b | -7.45686 | -42.84967 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64533069-8103-35ad-beab-71eee7cae74f | -9.04806 | -47.74583 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4654ddfe-b78d-309b-9b4c-2340a30972df | -11.05187 | -44.05289 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e066aa37-98a4-36b2-b456-a6ca7c8d74a7 | -13.49926 | -44.37007 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9bc15cc8-8564-3a80-8a11-9f6247b545e5 | -9.2964 | -47.47398 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4569ee64-7299-3efe-96b9-ca947685bf65 | -9.29423 | -47.43629 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 21f90ce4-2ae9-3bc7-9355-6185b5d5d7e4 | -11.75024 | -44.9326 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 470fef21-9fc8-33bc-a391-9ff41cad7513 | -12.01225 | -43.46477 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f92aac0b-ed23-3a73-adea-b5dde9d4c36a | -13.36665 | -43.88978 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56fb186b-9bb8-31f9-ac8c-d367f2d0b5ad | -10.57398 | -46.29249 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2e5f98f4-2000-371b-9b34-8fedd693f605 | -12.46673 | -41.31793 | 2026-10-09 03:45:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 20adba92-6771-3c90-93a6-9ce2bd25d620 | -8.73207 | -45.14137 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d8c7f2a1-ae4d-3100-b71c-3a080e2d898b | -11.76082 | -45.47542 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a72abcf4-0b92-3b6a-b2a9-e2de299ce3b2 | -9.90124 | -44.78886 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fbbb012-21e6-3b58-8ca6-3378faba849a | -11.01351 | -45.42712 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 7673649c-3c5b-3159-a64f-0d4f571e8f4f | -12.00457 | -43.47811 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f43d61d0-3712-32bb-881a-446a68e72d44 | -12.00399 | -43.45364 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4278d642-d008-3460-a5eb-a0ce2187d696 | -6.96424 | -45.2563 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db5701c0-3709-3b35-9291-55ab81010c91 | -14.44551 | -43.92542 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f59d650-3b17-3d11-9862-580b945aea6b | -11.18019 | -45.31226 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6791f7e3-6aee-371e-ac5d-e0eaf8b9b44b | -9.07862 | -45.11392 | 2026-10-09 03:45:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f23bb822-7201-3a94-a938-b55a57dbc098 | -11.00319 | -45.42006 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| ec26c9a4-1e22-35bc-b95c-6e8f7f3691aa | -11.1964 | -45.32036 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d9a41717-0c8b-3088-a6fc-ccf09d32b7d4 | -13.4073 | -43.73373 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9dc1968c-a668-3f3f-9ee3-53d713b4960b | -9.91324 | -44.78734 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78a73232-39cc-3541-b6a6-cfe20255336b | -13.48327 | -42.48534 | 2026-10-09 03:45:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cd622e70-23b6-329e-a439-3c383e19f3ff | -11.9985 | -43.48282 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8148276e-8e02-3687-9dc5-6af2b9bf22be | -11.23802 | -44.87708 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16d73f95-0266-3272-b023-2a0596bd214a | -11.22096 | -45.31604 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 974c3e52-c9dd-3d5b-987d-5038b5ae7193 | -9.55088 | -36.16071 | 2026-10-09 03:45:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 24901cbc-b3cd-3040-92b8-be298a64f42f | -13.25198 | -42.25266 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 1e738665-1155-33b4-b8d9-90b810268006 | -8.91286 | -45.22689 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cae2a6e9-5b94-36c7-acd5-7fa852e02b57 | -7.45743 | -42.84644 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b84bcd35-a394-3f7e-b227-5c6210006ac8 | -9.12512 | -45.83231 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a548e663-2fd1-3be9-9ba6-731445536ebd | -13.50271 | -44.37393 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b15c019e-39ee-384b-bca0-fc065bf1f9a3 | -11.99509 | -43.47342 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e80072b-4ffd-3e9b-bbaf-9df2cf3db4e9 | -8.72371 | -45.15322 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27d92b3f-1eb1-313d-998d-45ae11d8a492 | -8.73713 | -45.14692 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| eff6f67e-70be-3a3d-83c8-5970e5e4fae6 | -11.84972 | -43.53165 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 235339e5-1bf0-38c5-af95-640758e7f926 | -11.07212 | -44.08396 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a35c0c0-eb26-33a4-93a8-089118606adb | -10.59954 | -46.41638 | 2026-10-09 03:45:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae627790-7fb0-3509-b20e-30df5081b324 | -11.01384 | -45.42673 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| f2b5cda2-dac6-3dfb-beee-57b820a92749 | -12.00353 | -43.48364 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7af3e666-b6b6-3c4b-abd6-5f671f86c951 | -11.62572 | -43.59679 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6af1b2f4-2529-3b90-9f3c-f549e2aeff5b | -8.90863 | -45.21709 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7333767e-a398-32bb-a849-7369f761bbd3 | -14.22218 | -41.6702 | 2026-10-09 03:45:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d09d6b82-2509-3c2e-b438-7ae83eecdb03 | -8.90103 | -45.22474 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1b48f89c-7f21-3a0a-a6fe-9ec55e60b31f | -7.47414 | -42.84287 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 59cbfd00-c725-355c-914d-c6ce1553f4e5 | -11.84927 | -43.58898 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18be4475-9c05-30ca-b34a-aebc5ad25323 | -11.99676 | -43.46457 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a00f4d4-926f-3502-9d75-40c3aa38b83f | -7.39903 | -44.75409 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 1e11d07a-1d2b-3eec-8b93-20b74df7d5b9 | -11.61292 | -43.71975 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19edf5ee-809c-328b-8242-86822046de81 | -11.06619 | -44.08624 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c64f04-613d-309f-98e7-e2caa65012f4 | -9.30555 | -47.46329 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a5e3e3fe-b831-33c8-aead-d63eab99c98c | -11.41752 | -47.58385 | 2026-10-09 03:45:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71dadbc2-a7d2-3bee-aa82-0e23dde285a8 | -11.24985 | -46.30335 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f35776d-5b25-373a-921d-3f0fd1062474 | -6.88148 | -45.9065 | 2026-10-09 03:45:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d942244f-4316-3021-9424-2814035e7fea | -11.30699 | -44.84016 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c85fb32-e99f-3db4-b513-4cbc61979ba1 | -12.01444 | -43.4531 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2373a676-7e9a-3620-98ad-42131be44180 | -10.86521 | -45.54425 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5585fe5f-77a9-36f4-9446-c93688f49eb4 | -8.9838 | -45.91237 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fdd118c-2ab3-3987-b746-ab14bd6a6a42 | -12.41359 | -41.78025 | 2026-10-09 03:45:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84d5c3c0-cc87-32ed-9929-e77540af7be1 | -11.06864 | -44.08049 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0516a52-8732-3607-8bba-3637741aaf5c | -11.25072 | -46.29893 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3d2a7cd-15fa-3ef5-961b-6474370c9791 | -11.4601 | -43.38174 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f24c0ef-a696-3512-985b-9ea0fa84362c | -10.87511 | -44.80804 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd4768d7-85e7-335e-82ea-3401107f7eda | -8.90779 | -45.22146 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb21d315-24af-3d28-b065-4e6e2e6b6a18 | -10.45422 | -47.8577 | 2026-10-09 03:45:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ed93474d-d16c-3f81-9b37-4f6ec65e906b | -10.98787 | -45.40484 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bece1739-0a47-3d93-9fb0-6f93984e864e | -7.48812 | -42.79414 | 2026-10-09 03:45:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6bd2ebb6-9d1c-393d-a5ee-a99e3a7d26a1 | -11.01302 | -45.43085 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c842cd11-058a-3a4b-a6ce-5f028ebbadc3 | -12.00285 | -43.45974 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dabd851-ffdf-31d4-b420-050d1604402e | -11.24894 | -46.30796 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2db187fa-12ec-3a25-afc8-566fcba8877e | -8.73042 | -45.15005 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README62.md)
