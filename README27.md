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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c31e03c8-64e8-3c94-a00e-ff13e034c237 | -2.33763 | -46.48986 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23838cda-2366-3fd6-93bc-0fe65ef931e9 | -2.33718 | -46.48304 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb5b664f-9808-3809-93a1-3db4933f5086 | -2.27772 | -47.90617 | 2024-10-18 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d5ef2cc-e0b5-337b-a002-da0d86392525 | -2.27705 | -47.91026 | 2024-10-18 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fc66628-ab0d-3ef6-8d27-347d8b55959f | -2.21644 | -46.30413 | 2024-10-18 03:51:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25ba1e56-f084-31dc-8ea2-aa19d90ae71b | -2.21591 | -46.30737 | 2024-10-18 03:51:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb9df4dc-a13e-370b-b147-29b05c93bda4 | -2.1865 | -48.73248 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 800c5361-428b-312d-ba0d-39cd4bdfc81b | -2.18623 | -48.72924 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72839842-6cc1-3159-8ef5-bfb798be875b | -2.18542 | -48.73405 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55d5bf61-d8db-3527-9453-a2fcfd19924c | -2.18035 | -48.73134 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 863c1978-2f44-3e74-b0bb-3d4f76bf3d43 | -2.17957 | -48.73616 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cfc7d91-5b8c-3bfc-aaae-2e707a2b9859 | -2.17928 | -48.73293 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d48312a-f2a9-36de-8bb5-66ec31c20591 | -2.17421 | -48.73023 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f93f8d9-831e-3ac2-a7e5-296884bbd2f6 | -2.17342 | -48.73508 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec17efe9-5274-3524-9fd1-692292ef18cb | -2.17313 | -48.73185 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23d7815d-a7a3-30c7-bd4a-e669d26e610a | -2.16437 | -48.40849 | 2024-10-18 03:51:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ac71bde-25c4-303f-bd74-38b088b4654d | -1.99221 | -44.77901 | 2024-10-18 03:51:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa2c0ca1-b9a1-3374-8180-02d542bfe0d2 | -1.99138 | -44.78409 | 2024-10-18 03:51:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e498908-3fb5-31eb-8272-0cc59134ec7d | -1.86024 | -47.83823 | 2024-10-18 03:51:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f117f7ab-e308-363c-ae56-8622429a4708 | -1.85955 | -47.84248 | 2024-10-18 03:51:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68402a15-a741-3aba-a6c2-2966611b03ca | -1.61897 | -47.09264 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8eeaf23-542c-3a10-ab26-914b0ef9449a | -1.61399 | -47.08797 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6439772-8c20-3f87-8136-d69d9289220e | -1.61336 | -47.0918 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b242ffc8-4258-3e6d-ac05-f1ed7ddfe22c | -1.43346 | -48.14743 | 2024-10-18 03:51:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c858eaf-98d6-337c-99cf-ce6fa0d99a27 | -1.14537 | -48.09797 | 2024-10-18 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b718dd8-06cb-319f-b87b-c6c0515152db | -1.14463 | -48.1025 | 2024-10-18 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7787f6e-8dbf-31b3-8c63-39b03ed4112b | -1.13863 | -48.10144 | 2024-10-18 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9546ba88-45fd-3ca8-81d4-26b2fbf3cb8a | -8.03655 | -37.86264 | 2024-10-18 03:53:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f17718fc-22be-34d2-a119-3bd1a6405288 | -7.92382 | -44.89088 | 2024-10-18 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b35224b6-1b5f-3395-a8fa-081ed00b67f4 | -7.92309 | -44.89507 | 2024-10-18 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52a4783f-02d8-3816-92e6-41dc4e1345fa | -7.65061 | -43.68372 | 2024-10-18 03:53:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94358ff0-7447-321b-9dd0-4dcdd1d0354b | -10.8828 | -44.16941 | 2024-10-18 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 878985d4-c598-31e4-a005-80d251286d94 | -10.69636 | -37.04859 | 2024-10-18 03:53:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fd75cb99-1152-39a8-bd21-b8fd23778e4d | -10.34178 | -36.68339 | 2024-10-18 03:53:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 041a79ae-9a99-3795-9994-7e382735a7f8 | -5.29305 | -50.92572 | 2024-10-18 03:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10fc0f3b-1ff1-3a79-b086-4053485e2d38 | -5.29194 | -50.93171 | 2024-10-18 03:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba101d02-7ea4-39b3-aa99-0d799747fb6d | -19.203 | -46.33556 | 2024-10-18 03:55:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76df1fc1-5916-3619-a7ce-daa4790b88a7 | -20.43085 | -43.97736 | 2024-10-18 03:55:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a26246e7-ae8f-3d90-b89a-ee5d33a29df1 | -20.34714 | -42.77982 | 2024-10-18 03:55:00 | NOAA-20 | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5c1faaae-1b20-360f-8e24-e41e5f9195e9 | -20.34045 | -44.19117 | 2024-10-18 03:55:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d786130f-a2a5-379a-8374-28d8df771174 | -20.2081 | -42.13242 | 2024-10-18 03:55:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 268720ac-f301-3444-ab74-c276b63e9226 | -19.91293 | -42.25437 | 2024-10-18 03:55:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 56ae4024-6938-3398-8912-75a17edfc96b | -19.9114 | -46.11009 | 2024-10-18 03:55:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 196d44b3-bfa1-3ada-9723-a35ebe13d00b | -19.88041 | -46.06217 | 2024-10-18 03:55:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54c9c654-573f-3ecd-a11c-b3d8b8888382 | -19.87909 | -45.71046 | 2024-10-18 03:55:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 111193aa-4959-35f5-be3a-099c13e978e1 | -19.83759 | -45.29332 | 2024-10-18 03:55:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 602d1e20-a81e-3ee8-bed5-261b8ed41288 | -19.7107 | -45.92825 | 2024-10-18 03:55:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45cc2f68-e8bc-3152-aea1-ffb06b0ffdef | -19.70675 | -42.22617 | 2024-10-18 03:55:00 | NOAA-20 | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c4e9dee-93e7-36de-b7d2-711c0bd53505 | -19.66617 | -46.23496 | 2024-10-18 03:55:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7bf17e0-28a0-3bf6-b890-e2e37bd1e876 | -19.64559 | -40.7824 | 2024-10-18 03:55:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee78228a-34ee-3369-9b65-df1d0efd1b10 | -19.64227 | -40.78185 | 2024-10-18 03:55:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64ce9e9d-9681-3ada-acbe-08cdebc43a02 | -19.37821 | -42.40798 | 2024-10-18 03:55:00 | NOAA-20 | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3111198a-2264-34e8-87f3-1a33a8ac0901 | -19.36379 | -41.6088 | 2024-10-18 03:55:00 | NOAA-20 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| f12e0714-583e-3fa4-8f52-a6b529383fd9 | -19.34439 | -41.45185 | 2024-10-18 03:55:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9f26ead3-58d9-3ae1-abf3-5d9b31ab4e41 | -19.31317 | -39.97729 | 2024-10-18 03:55:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9bd77018-fc7b-3ea8-a14e-1d249b5c4ebd | -19.28163 | -42.84922 | 2024-10-18 03:55:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5c0b1ae9-73b3-3202-9759-2fb1fe062f8b | -19.202 | -46.34092 | 2024-10-18 03:55:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02d97fac-edf0-389a-b729-b0abc555af99 | -19.19805 | -46.34017 | 2024-10-18 03:55:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df8d34cb-dce9-377c-b41b-00165ec4a358 | -19.19605 | -46.35091 | 2024-10-18 03:55:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6797e2d-ade4-3838-9eda-640064431581 | -19.17246 | -42.89357 | 2024-10-18 03:55:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 646ebe06-c2d1-3213-b214-4668e75dbaa4 | -19.13807 | -42.29324 | 2024-10-18 03:55:00 | NOAA-20 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dab6689e-1897-3e51-9956-ec73d65625ed | -19.13248 | -41.54623 | 2024-10-18 03:55:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8091ed8d-e01b-32de-a56a-5d90edbee8f7 | -19.11685 | -42.91418 | 2024-10-18 03:55:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 470ab935-eb92-3855-8b38-8e37389f4ce6 | -19.11428 | -42.00132 | 2024-10-18 03:55:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 130ca3b0-46e4-3b7d-a24a-61fce5e81788 | -18.86441 | -47.52311 | 2024-10-18 03:55:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 416629e4-5895-3e3d-bcb5-fbd13a276640 | -18.86096 | -47.51802 | 2024-10-18 03:55:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3617cbb3-16be-3295-85b9-fb8daa10ad80 | -18.86014 | -47.52225 | 2024-10-18 03:55:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da248d07-787f-3b61-9fc9-c03957e56aeb | -18.74284 | -43.06876 | 2024-10-18 03:55:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6f922d6f-65bd-36ec-ad26-9bb2629bbe7a | -18.61855 | -40.99213 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 934a27b0-06b2-3c39-873f-c089a69228b7 | -18.61524 | -40.99156 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 23b6bb63-e3aa-3b85-bf4d-10ee82a7c258 | -18.61129 | -40.2459 | 2024-10-18 03:55:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a9073280-a140-35ac-8e21-812ddb974208 | -18.60418 | -40.99713 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 916c451e-6c4b-3201-8575-949a98487823 | -18.60361 | -41.00076 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9fcd636c-daef-3eab-a7e9-3ae3a37e2af5 | -18.60087 | -40.99656 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 9aedff2d-2666-3554-ba42-aded632f8288 | -18.6003 | -41.00019 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1beadd4c-ba56-33e8-818a-8b0cf7789fd6 | -18.59973 | -41.00382 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6044829f-895d-3f4c-bed2-40b2b1d60e04 | -18.59623 | -40.56694 | 2024-10-18 03:55:00 | NOAA-20 | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3e1d6ba-4b07-3a4b-aca5-137524ca2299 | -18.59201 | -47.96713 | 2024-10-18 03:55:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d95c152f-d60a-3926-881d-c66d877cf1e7 | -18.55735 | -40.94873 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9291d275-0bdc-3fc6-ad1c-9727b3053a02 | -18.55679 | -40.95235 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 83398696-9f54-3abe-b115-8c0061d24797 | -18.55404 | -40.94818 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| dae93e23-fb52-3938-b351-7c279f821d4b | -18.55348 | -40.95179 | 2024-10-18 03:55:00 | NOAA-20 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3402a2a9-6c05-3427-bbc6-eab0899ee53b | -18.44597 | -41.46188 | 2024-10-18 03:55:00 | NOAA-20 | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c4d79e1d-a340-31b4-8dc5-d492dd9ac828 | -18.39489 | -40.88034 | 2024-10-18 03:55:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b6259003-3d40-330e-9b49-8713df435508 | -18.39434 | -42.20454 | 2024-10-18 03:55:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 027e1ab2-c397-3f86-82af-82eec0f085ed | -18.38432 | -42.20274 | 2024-10-18 03:55:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c5984136-b5bc-39f4-989c-fbca9181e5f2 | -18.38371 | -42.20646 | 2024-10-18 03:55:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 80ab682b-96e2-3860-ad55-11924ba5ff87 | -18.30104 | -43.1704 | 2024-10-18 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a30dfdd2-c4dd-324f-92b3-83a3cfc259e0 | -18.30086 | -41.88228 | 2024-10-18 03:55:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| abbe4544-a949-30e5-a38a-52757b4a6032 | -18.30038 | -43.17431 | 2024-10-18 03:55:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b0d8ab62-fff8-3eaa-9437-673c268b4f50 | -18.30027 | -41.88592 | 2024-10-18 03:55:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 035389e0-e7dc-3d0a-9484-7b86a7f2f2ec | -18.13398 | -47.84359 | 2024-10-18 03:55:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a1d07b7-1d96-34ea-8a30-17072b283294 | -18.13308 | -47.84816 | 2024-10-18 03:55:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 014b8d77-19c5-3a9d-930d-90841cce5328 | -18.105 | -42.72358 | 2024-10-18 03:55:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6ab20293-3d5a-37ec-a9e3-10e90a9102f2 | -18.10225 | -42.71914 | 2024-10-18 03:55:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 381a6439-4d82-31f8-8b9a-1a8d5b684403 | -18.10163 | -42.72289 | 2024-10-18 03:55:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5d99783a-aa36-3d53-a491-13f809a2c5d0 | -18.09978 | -42.92326 | 2024-10-18 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 31fc4739-dd32-3cef-a60a-80810ae62d6f | -18.09888 | -42.71847 | 2024-10-18 03:55:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 56709549-c723-350b-8498-31e27f952a01 | -18.09878 | -42.65626 | 2024-10-18 03:55:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b6d84ce6-a911-375e-9586-7a6d2cbcc1a2 | -18.09826 | -42.72221 | 2024-10-18 03:55:00 | NOAA-20 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |


[Clique aqui para ver as próximas entradas](README28.md)
