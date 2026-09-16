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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce095820-c887-3e18-a00b-ed23b14e90ec | -10.89048 | -51.49955 | 2026-09-16 04:59:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58824c87-0fbd-3d4d-9062-484379bfcb4c | -13.37897 | -57.02441 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b0c0c603-7647-3c81-8406-e1dc3c3e35eb | -9.62695 | -49.02177 | 2026-09-16 04:59:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88cfdb52-7f88-31c2-aa87-1c75c052b75b | -9.57504 | -46.61118 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b971b606-dd46-3675-93f2-510fc238b348 | -8.54045 | -54.69897 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8940882f-7a40-3f7d-94f3-e0eebdca93b4 | -11.19236 | -55.0272 | 2026-09-16 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 40361046-e651-3403-922b-a22b3c42074b | -12.11903 | -57.1957 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fbfc5b4a-9386-3e89-af02-8c51bd3e2b76 | -13.75035 | -48.7912 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05c07ec7-5754-3bea-ac70-d010fef7a99b | -11.19853 | -42.81089 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 08e00231-e3c4-3b37-883e-eb9cf5ae1127 | -9.80604 | -48.92316 | 2026-09-16 04:59:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a45cc001-9b26-31f9-91aa-999463beb760 | -9.17565 | -49.9966 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e82caf-9442-31fa-8440-8a20a37244de | -8.24901 | -55.32103 | 2026-09-16 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adb7f44d-b863-3c5b-a491-efc59d48003c | -12.38361 | -51.41268 | 2026-09-16 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4327c2c0-649f-37a8-8ba7-b773f14f49f8 | -9.60085 | -55.1168 | 2026-09-16 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a9f2f23-cf51-398a-85e9-7ae9682bcc6b | -9.39482 | -60.30681 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e20fdc5-6fc3-3545-be35-f86afd90f131 | -10.66634 | -54.13886 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee6abd5a-c399-3a8b-bdd0-841e2d7f4d5d | -13.3053 | -51.75379 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ab355bc-57fc-378f-876e-d3a5c8389c76 | -10.67359 | -54.1363 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8f5541c-2ca3-37dd-be3f-6ef594ea069b | -11.19567 | -55.02772 | 2026-09-16 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7965cee-ecf7-347f-9d32-cfb529471ed6 | -11.32177 | -47.23793 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2481c5b-670e-3231-a9e6-f10c654796b4 | -12.38569 | -51.41547 | 2026-09-16 04:59:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 566deb0a-0bc2-3237-bcba-f4a05daa2f62 | -10.25885 | -57.6982 | 2026-09-16 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 44ae5fbd-1a2c-34df-bf03-f617d8d16428 | -11.80794 | -60.46208 | 2026-09-16 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ab476e0c-73ab-3183-9a15-050288ff4f2e | -10.75962 | -44.81882 | 2026-09-16 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07a399c5-296b-3b5b-b034-b9468e008f74 | -7.63566 | -67.16909 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 84e73c4d-ead0-31b8-8dba-c5331d634790 | -8.41409 | -54.7211 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d51abc9-fe56-31fb-87e2-98381c2e650e | -9.62483 | -61.82236 | 2026-09-16 04:59:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 768761dd-7288-301b-9b5d-760271bba40e | -9.49487 | -56.75637 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e294d454-438e-3214-ba03-1090f4ca3a33 | -9.49148 | -56.75584 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bac59b2-df6f-38ed-9ef7-5705d905342f | -9.39076 | -60.3061 | 2026-09-16 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3f3607b3-2799-32fd-b46f-dddbd7e2fe6d | -9.50828 | -59.5044 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e936b371-1d26-32ad-8238-7b6a193323c8 | -13.21381 | -51.63552 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b10f17e-1fa3-3425-aef3-096f7f067fff | -9.70246 | -52.02225 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef4cecb8-11dd-3fde-a679-4501f045b0cc | -9.58126 | -46.60289 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daab41a6-ef34-3104-8e84-93279945b502 | -9.58635 | -46.60362 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3348dd5d-20a1-3bd7-8b25-84ca307f98a3 | -13.40274 | -57.02089 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aec5e265-dc8e-3ea6-8cce-34235d010419 | -12.7539 | -52.84036 | 2026-09-16 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0b9547f-3b0c-39b2-ba02-8e2bacb6064b | -11.5429 | -46.86168 | 2026-09-16 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c5ab1acc-9367-3067-86d3-def2240d3038 | -9.71431 | -64.97314 | 2026-09-16 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4f1b7ff-7373-3aac-99d3-d4e97e63ea1f | -9.84393 | -48.35486 | 2026-09-16 04:59:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f06647a5-989d-3891-8bb9-370f41c39ee9 | -13.7269 | -48.97724 | 2026-09-16 04:59:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 745d0b6d-f5c8-3b50-909e-1767643e0afe | -10.40707 | -48.66361 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63b3c776-f648-353b-b3ba-9a6039bb075e | -9.86127 | -49.82117 | 2026-09-16 04:59:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c65792e-7076-3a39-8514-3a8764779228 | -9.02086 | -61.01608 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad6b862d-e9a1-3209-a79e-97cd40dd16f7 | -12.11684 | -57.1878 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18633ddc-2997-3bbd-b883-7ec520c3167a | -9.02839 | -60.3682 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80871b61-9930-354b-a528-b02547ed71bb | -11.31676 | -47.23741 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c01d6c-120e-3698-b94b-150a04aa7ed1 | -8.54099 | -54.6955 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b348093-45ac-3080-9ba3-6d6d3e09e6e2 | -9.76416 | -46.57794 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 64dba09c-3614-34f5-a104-162cef81544e | -10.40875 | -48.651 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1bb2988-6e54-3ee3-b1ec-a886673bae1c | -14.66533 | -48.02357 | 2026-09-16 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c36438e9-b5d5-3b91-9565-3c07c2e85b84 | -9.49206 | -56.75217 | 2026-09-16 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 512416b1-b56a-317d-8ccb-662f716205b9 | -7.55636 | -62.32882 | 2026-09-16 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 499494b0-a6b4-3bdf-9990-1a205345e228 | -9.35319 | -50.18384 | 2026-09-16 04:59:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e175a27a-e76b-3b3a-8b66-1e1be90c3a99 | -11.80883 | -60.45691 | 2026-09-16 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa9c22b8-8240-3e80-bcf5-1838a88c63d2 | -10.59431 | -47.75187 | 2026-09-16 04:59:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfe2282f-b243-3e9b-8829-cc47ca16436e | -13.39158 | -57.0264 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9187ff75-0b13-30bd-8016-bdafa013ffcb | -13.37839 | -57.028 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 287dd702-fd6e-35b8-afc0-e7967c28f7fb | -13.30042 | -51.75572 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15b1a02e-f6f7-380d-994b-1d4f0b88b1a4 | -10.86695 | -50.81156 | 2026-09-16 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 53e6e09b-2254-3741-a678-830683bde1a2 | -12.12081 | -57.18469 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d75a352c-7faf-3275-bc11-d21867b21e1d | -13.75561 | -48.78699 | 2026-09-16 04:59:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8fa77ed2-ac6a-3c30-bbcd-855b742ffea0 | -13.20625 | -60.13067 | 2026-09-16 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71a40d95-8c02-3160-85c4-e766258ac7cf | -9.37406 | -58.00055 | 2026-09-16 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e85e5e1-7e33-3480-8775-a35e460bbd76 | -9.1272 | -51.5784 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e3793f7-6b10-3d5f-b979-437aa41958d6 | -8.53992 | -54.70244 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3feaeed6-22ba-3c91-a5a9-b24084b7182b | -7.64327 | -67.1646 | 2026-09-16 04:59:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 195c3d08-b396-38aa-a079-74c6559609b2 | -8.83182 | -62.47408 | 2026-09-16 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82f5e89b-8bae-3cf7-ad58-827b1e62c6a4 | -10.30835 | -45.27287 | 2026-09-16 04:59:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dadba9a4-d89c-37df-8f6c-22c0bdeba878 | -11.89736 | -43.81892 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1cac8ae7-7fd8-3db4-95d9-721e29b8014c | -10.69788 | -54.17344 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 03e65e78-c38e-36f9-9c87-3b5fb248f0ae | -8.53884 | -54.70938 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c5b7e0-5166-3370-af53-a50d960568d2 | -10.41317 | -48.65201 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7558da3c-40a8-3509-b6ab-663b1e53a025 | -9.57446 | -46.58723 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9172a558-b9e3-3b8d-9766-6cbc8081e91c | -9.56402 | -59.31613 | 2026-09-16 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08d98626-aed7-36d6-adf8-9d4feb79bcf3 | -11.25196 | -43.44169 | 2026-09-16 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1d150ce-440f-38bb-a6cb-f65efbc93841 | -9.12712 | -65.85276 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc5b0711-1f67-3a4f-bfc9-c69f5e76a7f8 | -8.60129 | -64.10027 | 2026-09-16 04:59:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| def14de5-ab3a-3d65-b9f6-69ec9c137034 | -11.98024 | -52.47125 | 2026-09-16 04:59:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d96feb8f-08c5-3ad2-a07f-02400ecf4988 | -10.81007 | -46.17825 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42336853-a539-30fb-8058-3253c755e1f0 | -11.88936 | -43.83316 | 2026-09-16 04:59:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e8b666b2-54c5-3d51-b49c-6fb39ed5b249 | -13.2124 | -51.63694 | 2026-09-16 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9fdf3383-ad0a-324a-a1e7-eb058105bff3 | -8.37174 | -54.73222 | 2026-09-16 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dad58174-bcd0-300b-9883-95cc84fe38e2 | -12.72345 | -56.56681 | 2026-09-16 04:59:00 | NOAA-21 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af3f7754-dd01-3b1b-af98-5a491c5c798a | -11.31622 | -47.23849 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8cfe0187-8e2e-368b-b808-0ea240ab35af | -10.7867 | -46.20401 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2b59c75-c307-3e38-9b07-3e1e03de3c30 | -10.42217 | -48.65285 | 2026-09-16 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d39d5fc-180d-3f11-a7b9-852d371c1c10 | -10.47616 | -50.96253 | 2026-09-16 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb30d409-f82d-308f-b0ae-3240126e7a9d | -9.05869 | -65.925 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f32b9008-2e74-3ed3-bdf1-f0ba423d2787 | -9.101 | -65.9281 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60c32802-d8d5-3c46-b1a3-bcb4be9e9262 | -9.13086 | -51.57891 | 2026-09-16 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d00063c-28c6-3935-95bb-9ee4b11ff639 | -11.19871 | -42.829 | 2026-09-16 04:59:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7fb9bc54-3b6c-3e01-a121-3974f13ae301 | -11.1978 | -54.12865 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c2da5cb-08c5-3156-94c9-fbf234f02448 | -13.77004 | -48.82217 | 2026-09-16 04:59:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 462ad848-bd6c-3063-b039-ffdc0e8b5706 | -11.32065 | -47.24343 | 2026-09-16 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af90b6d9-6248-3ac5-a54e-93ee7c52f93f | -9.06971 | -65.9316 | 2026-09-16 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2eb01c38-a2dd-3e5f-ac29-a8b3281b1d94 | -10.9361 | -54.08071 | 2026-09-16 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d514d694-40cd-3fdc-98f2-0fdb16715923 | -15.04517 | -48.56724 | 2026-09-16 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8bfef16-fbbb-39ba-8fce-59f2fd5c9d15 | -9.58264 | -46.60351 | 2026-09-16 04:59:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3856d970-b397-38c4-8c38-1fdb527ed8f7 | -13.3762 | -57.02026 | 2026-09-16 04:59:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README46.md)
