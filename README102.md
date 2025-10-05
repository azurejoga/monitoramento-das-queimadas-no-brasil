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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00486ae2-107e-3b1e-bb59-cc8655e947eb | -9.45522 | -56.65304 | 2025-10-05 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ad852382-8fc4-361d-86ab-3829d10069ba | -11.86726 | -44.95548 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc7ffc27-c235-3cbe-9940-451709428adf | -10.5751 | -48.71106 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9e02850-e1d7-37eb-906b-2c138d8df4f5 | -12.77638 | -48.81763 | 2025-10-05 04:46:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c404da0f-9b5a-36e8-b792-dfc1a74f1200 | -13.26427 | -47.19872 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 794e1581-3138-3718-923f-46ac5176009f | -13.33554 | -47.19128 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9315b260-39fd-35a9-988e-3470c7e06953 | -6.60116 | -44.31493 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ee5638c-b8a4-32b4-9fad-e991df0ba67b | -9.9958 | -48.29696 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a37aa8fd-6f1a-32b4-830a-1def2072c663 | -12.45587 | -44.73268 | 2025-10-05 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a6c5dd12-ad98-3581-827c-308d5209ad88 | -10.01851 | -48.26965 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abd13b56-b838-32c0-809c-e98967389310 | -12.8237 | -46.8564 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46f3caa7-3b2e-302d-9edf-d2063a0c8efd | -8.91552 | -51.31611 | 2025-10-05 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9c87d3a-7340-3901-97f7-f3a8cefd31e7 | -9.65378 | -45.85472 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6cccaf29-ee9c-3639-bfd8-973f87f9d4a2 | -13.2745 | -47.18513 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ecc71a6-c9b8-3255-964a-50a4fec6234c | -10.84075 | -47.98115 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 611afbee-e4ef-3f7c-a472-d375f7760284 | -8.6536 | -54.96182 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c7807c4-49f5-3035-9637-8c6a28bbf916 | -7.75904 | -46.3149 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a658245-505c-3b34-8993-5ed3c1c15a47 | -11.83257 | -45.05438 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ec8dc8c-48a4-3d22-bb54-4b653a436d98 | -12.31569 | -55.1217 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd1ec804-ca5b-3358-b890-393965213c7f | -11.25842 | -47.78264 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4464d515-6c3d-3eb9-8ee2-42f6b31c0c70 | -12.30481 | -55.11667 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77322e4e-9791-3520-a482-151995ecf928 | -8.86491 | -46.81805 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9402956b-d673-37da-8f4f-6cfa6b03c5ab | -11.63614 | -45.05598 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83e7c892-f3c6-3ca7-8259-fe184adf8e1c | -12.41262 | -51.1011 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 349e7b94-ad4d-354a-865e-138d4ab3cfc3 | -13.27351 | -47.62259 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 613cb61d-f77d-3469-ab37-6afc32e247de | -11.35436 | -47.66106 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e883f248-0db4-3350-9e18-25c5c3eaace8 | -8.94244 | -48.64105 | 2025-10-05 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39256d0f-d9bd-3fbe-827c-48c72a687d5f | -7.25208 | -44.89527 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7080db6-f1f1-3bf0-b61e-0d94469cbdda | -12.23184 | -47.83024 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24407a6c-fa22-3515-9149-eb61fefb6d13 | -12.82628 | -46.86905 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f82e2b2-471e-359c-a898-2fa7ecf689aa | -12.28071 | -49.20403 | 2025-10-05 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5154d655-3b40-3f59-8290-33ea455ea53a | -7.78169 | -42.6068 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5f003ce4-1c43-3a0c-a063-6939364b7ae8 | -11.95024 | -51.48459 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad26ccf8-5d67-3597-b985-e99bd67bd932 | -10.39291 | -45.41691 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9c5b2486-a073-37e3-a90b-04874879fb34 | -8.09053 | -45.69521 | 2025-10-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 730b6fa5-9567-380d-8421-b0233808d31b | -11.70471 | -47.50588 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 37532b07-40fd-3e05-967e-fa6475fccc74 | -11.48523 | -45.02682 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8ffbfd2-4526-376a-9b15-8dff2a6cf3db | -6.60051 | -44.31955 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02a679ee-e92a-3089-8c27-f22b7797b98b | -9.30973 | -54.53428 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da16da48-f76c-3d35-b27c-62a64542ce85 | -10.39085 | -51.65128 | 2025-10-05 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54ee0f39-1663-3c9f-b7c8-b80777728526 | -13.57953 | -48.16346 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c0c42e19-c4fc-328e-96eb-c696c8d75db7 | -7.35094 | -45.21424 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77c04996-7ab8-370c-bfde-4398510b409f | -11.5323 | -47.67984 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2f78f093-d3c4-33a8-8bf2-75ee9d23ef65 | -11.86121 | -45.05297 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c46a51fe-aae5-3d32-b00c-b54ae8c34bff | -7.66073 | -45.46704 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 966c2d5b-e212-335e-8de3-e6042cd2cf73 | -12.26922 | -55.13546 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 789aab05-79c4-3bc8-82ff-e2a0f4571b5c | -10.83394 | -57.17632 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3210c37e-3b20-3d61-9798-b8c5e267c0e2 | -11.90109 | -44.98919 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c2341101-919b-326e-9cd6-1c10087d6b4e | -10.46856 | -57.4996 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f188bc87-abbe-30a8-9957-b7fe53ccb9fe | -8.59818 | -46.29573 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e506961-f31b-3165-af04-bf08ae537f0b | -8.66779 | -45.80061 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4565e4cb-baed-3ade-86f9-a77a497f8215 | -9.83843 | -59.46968 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b43d8ff-e073-34c4-80c2-cf995707e736 | -13.64895 | -47.29918 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 576c8a07-c1f3-34ff-aa63-4c649ab1c724 | -7.77012 | -42.61422 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ed950c65-bfe2-31d5-87e9-3b83b8c12348 | -13.27776 | -47.59111 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a4a77db5-bf0f-3362-a17b-577a3c9a7603 | -7.44802 | -46.52567 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d89d3abc-54a7-3477-bc14-8dffcfe3edeb | -13.09474 | -47.84756 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ef42a11-b25e-3958-8256-2e60f657274c | -11.07177 | -47.87814 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f3e077e7-9d86-3908-83f5-5eb080b4fc85 | -12.81851 | -46.86341 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0174ede7-985e-3d69-87f1-9de555fb7447 | -11.03176 | -54.25941 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62ad1887-1461-3c72-94cb-58b74b556f5a | -11.07245 | -47.87331 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6462e052-1406-367d-b192-79e269a30371 | -11.09986 | -49.86422 | 2025-10-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9be7d9ed-331e-3cec-bac7-9d4f4ea42a7e | -9.20235 | -46.92517 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0920c19-29a5-3dd7-b17e-16091397e09c | -11.13507 | -47.92619 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac219b24-62f6-3dcf-ba0d-651b1ebc7b86 | -12.97595 | -51.03782 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9076dd49-360f-3c30-adcf-8de8d2d8eecb | -13.24712 | -47.23248 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a848862a-e8e0-3219-b300-8f6e27acc2f2 | -8.90166 | -46.58976 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f6d8623-6e9c-36a0-bb52-d7d7469f1ec8 | -9.45202 | -56.648 | 2025-10-05 04:46:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb19dc0d-943c-306d-ad11-1ecbf235c744 | -11.14995 | -47.92543 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19643421-2fee-3f36-83c3-379243a80981 | -11.86077 | -45.04437 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 934aca9b-09f0-3e98-9591-482e9f057f97 | -10.00418 | -48.29575 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dfbf897-1387-3b79-bfce-091eebe6c828 | -12.4552 | -44.73806 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82778c26-934d-36ee-b0c1-cd4c9314f594 | -7.43813 | -46.53185 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1d203fa-f1cb-3081-aa49-e739f0aa8a7c | -12.56863 | -54.77218 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 309086cb-136c-3c99-aa07-0296a6bf2508 | -13.65135 | -47.87463 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66aac7b9-8559-33f5-95f1-20c026abfec1 | -12.31299 | -55.1377 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62ba436d-1e42-3e83-b9c6-f6c3d5cd9537 | -10.34968 | -48.16009 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 24b807cf-0108-32ad-aafb-26baafb6fe17 | -9.05733 | -46.98566 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dec658b6-12dd-3d67-b0a8-be067d740896 | -11.81541 | -48.8761 | 2025-10-05 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9349d0a-21c1-3bcc-a77a-910840842229 | -13.32682 | -47.78805 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15129191-13e4-3731-a728-41afcf2b18bc | -13.43941 | -47.28358 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1425853-44ae-3193-bdbc-0d772d2d7824 | -13.08965 | -47.88586 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e04c171f-709c-3fd4-8cb9-35377ae4875f | -13.34483 | -47.59108 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 350f51f4-5350-3c94-ba84-be75150d1252 | -11.90616 | -46.22643 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 881482cb-b22b-343c-abb3-cc9f29a809a4 | -10.59891 | -54.36542 | 2025-10-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73f51b01-b876-33c6-a4f8-54c5b146d733 | -8.56591 | -44.6418 | 2025-10-05 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c22e90-08b7-33c6-9905-ae543b822315 | -12.39933 | -51.10622 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47e9184b-b874-3585-b840-db986b0f7d41 | -12.41208 | -51.10474 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82c1e4b4-bd9f-3a43-ac81-4188ef5e2525 | -8.62676 | -54.623 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b81dd615-5a15-3dd9-8996-a1bf74a8c289 | -10.29994 | -48.54965 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15bbdaf7-0d61-374a-a801-f4846e6694d9 | -9.76176 | -47.73528 | 2025-10-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480c35c1-1816-35d4-a0bd-6f0e9cb785d4 | -10.49398 | -48.10757 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1596f79c-64a0-3783-bc3a-8e2871919726 | -11.48639 | -44.98193 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 741972db-87cb-3619-98d2-aa4e9905cec4 | -11.49973 | -44.98864 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4e42944-cd24-3785-a21b-160cb7dcac8c | -12.82004 | -46.8518 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b66b1897-9c0c-308e-9764-d1d50eee189d | -9.1443 | -60.29572 | 2025-10-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e4b606-0315-3e6d-a6e5-a78c56201e99 | -13.16497 | -50.87025 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0536a90-2bcd-321b-85d2-7f3f163aeb33 | -13.14071 | -47.97971 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77c8811b-f3b4-3e5c-b450-5a80fdc8d794 | -10.84535 | -57.18205 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a9066f6-2040-3c09-8bb4-96314ba7e477 | -7.24858 | -44.88821 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README103.md)
