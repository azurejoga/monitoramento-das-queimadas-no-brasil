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
| 0b8b8a1e-f617-3787-81ae-61ddcadad60d | -8.04724 | -54.84686 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdac2eeb-e676-3a38-8259-e5e166b92fc2 | -13.45185 | -48.51072 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00f88d9e-bc14-3994-9bda-9a9e89a198e4 | -10.54074 | -45.2215 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 099ef1c1-03e6-34e6-ba43-bc2aa376b8e1 | -11.57527 | -46.98867 | 2026-09-13 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3d377052-54ef-3288-941a-9ba7ff94583b | -10.57956 | -51.35174 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f4732a34-ddc5-3b43-840e-5b3c88ec69c5 | -7.86616 | -54.69584 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3eec0609-c8e7-32c0-b622-256042bc806c | -10.48471 | -48.64127 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2140461-9fec-3ec0-8ecd-77304fc20038 | -11.19409 | -42.78131 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d23d692a-1e38-3478-b213-1bb0cd1b80ea | -13.61376 | -47.87247 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f0c4d680-c2c1-3710-9625-f449413592b2 | -11.71694 | -46.73535 | 2026-09-13 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08a0303a-1b2c-3bc9-a482-9becd6750636 | -8.04034 | -54.85036 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a5b3726-f380-3914-88b0-5a3e2b4406ca | -9.30561 | -44.33973 | 2026-09-13 04:17:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af1bad0d-0970-3858-a67d-38451e4be4bb | -10.51485 | -57.45018 | 2026-09-13 04:17:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3505c31d-c139-3d4e-95e0-dfce3887b95e | -8.11527 | -54.79358 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87a70b37-632a-30be-8859-674095322fa1 | -10.68752 | -54.17043 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 48c02eaa-4827-35e7-bf00-9032ef3a2440 | -13.40637 | -57.03013 | 2026-09-13 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad68c122-c2f5-3d38-bca6-781facdc86f8 | -12.49054 | -48.0424 | 2026-09-13 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03591e2b-5c6c-3910-9553-303d5709726d | -13.55375 | -49.48643 | 2026-09-13 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a440df8-4f4e-3214-8dff-0f15802c804d | -9.1617 | -47.57968 | 2026-09-13 04:17:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 833b92dd-70dd-35f9-96ae-f73fabb5df65 | -16.67083 | -41.85159 | 2026-09-13 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 77873e3d-8d14-3cff-ad54-27332f76775d | -13.62012 | -47.87802 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c0b7cb3-e1b8-3020-b8a1-3dcedb1e187f | -8.53451 | -54.71074 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 953fc71a-9f22-31f4-b88a-2425e217291d | -10.69302 | -54.17159 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a12db467-0c3b-357c-8703-5d22afd6e977 | -8.12557 | -54.80479 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71e247a7-bcd1-34c8-8ca7-392f214e4670 | -11.81787 | -46.39526 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bd9db28-d827-334e-ad3a-9d64e1f07d71 | -13.46305 | -48.48932 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff57c45e-88da-33c3-8d4d-cc63208a1aec | -9.59949 | -46.72457 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d754512-1937-3587-a099-c8913f355b08 | -7.86805 | -54.71906 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f997116-0b15-3f93-8066-7bcc685fbdc6 | -10.30659 | -45.28174 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24d466bb-9351-3f62-826e-22c0c6f7521d | -10.56658 | -51.34473 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63f89642-5012-3a44-877d-ed8aa58665b5 | -13.10585 | -44.63423 | 2026-09-13 04:17:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3aede4a-83af-3f11-a58a-200c72ed41dc | -13.559 | -49.4846 | 2026-09-13 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2eef3a0-d946-3090-a96e-27a3d0cb696d | -13.40365 | -57.02761 | 2026-09-13 04:17:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87802174-7840-3b46-98d0-392b1da3e72c | -13.02402 | -48.64331 | 2026-09-13 04:17:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b7ffeb33-c680-3fab-b85b-7d1d34eddf1f | -16.74967 | -45.07467 | 2026-09-13 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19ab6101-6ea2-31df-aac8-235c5fb7955d | -11.43872 | -45.15698 | 2026-09-13 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e4a91a1-6f9e-3716-b92f-4613e87931d1 | -9.58359 | -55.15922 | 2026-09-13 04:17:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 436b7d52-840a-327b-8394-1a2f5c32f822 | -9.80994 | -43.48114 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 18647319-877d-323b-ab9d-3c87246f3bb7 | -10.54025 | -51.38564 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 236d7016-fd42-383a-8bd4-c3ced70bdda3 | -9.54813 | -45.44337 | 2026-09-13 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3dbda25a-f7d4-3c06-9dfa-30eb999807ee | -13.39528 | -48.0046 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e856092b-c322-3e6c-8810-d02bdf8b96a2 | -9.6081 | -46.73832 | 2026-09-13 04:17:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d136c966-9b42-3eaf-ba82-aebc08d4bd5a | -11.35279 | -46.7909 | 2026-09-13 04:17:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 65d9af62-81a9-39c4-8625-a386a5558666 | -15.91426 | -42.55914 | 2026-09-13 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3504d8bf-d038-32e4-8369-a14fde9735fe | -12.85453 | -44.39119 | 2026-09-13 04:17:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5b7ea985-5127-3f4f-a137-f3a02a453265 | -13.55512 | -49.48389 | 2026-09-13 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9003fa02-9435-3c9c-a6f5-bf0f803d7257 | -13.30468 | -43.73648 | 2026-09-13 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba889fcb-7a12-3007-a8ee-7531216e0d91 | -12.15496 | -48.97034 | 2026-09-13 04:17:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 60759261-3ae4-32b2-ae15-59d4141339d3 | -7.86637 | -54.72808 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a8ac371-a06f-393b-91d7-3f686530d6a0 | -10.31213 | -45.29003 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4ae4cf6-6e39-31ec-b74d-c57032f609a7 | -11.82128 | -46.39579 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77880635-0638-3a08-8ec9-5f4c3a401485 | -10.46534 | -48.63837 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a080ef49-e4f8-3765-b224-d5fa7ee26e9f | -13.37036 | -51.7131 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 375cb930-fa62-368c-abb5-65c1b6034c10 | -13.70208 | -44.22947 | 2026-09-13 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7729aac-bba2-3d9a-8d57-99555719d560 | -11.19636 | -42.78915 | 2026-09-13 04:17:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c6c374dd-9271-3506-aa82-e3d3b4a89a77 | -7.8654 | -54.69994 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58cfc265-d179-3b5b-a0b4-069722b2e432 | -10.92283 | -48.35129 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c6cceda-cad3-3b76-99bd-f5acec908c11 | -13.98585 | -54.07064 | 2026-09-13 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a087656c-9d8c-39dc-b429-5d80904d8614 | -10.21944 | -45.18758 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f9c574a-de1f-397c-869d-042e04156e21 | -9.94356 | -48.50634 | 2026-09-13 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c38fa17-41d5-386e-b831-94ac5988d9c3 | -10.35643 | -46.67035 | 2026-09-13 04:17:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d666723-b62a-3756-aad1-031159c1cca0 | -9.75276 | -48.18671 | 2026-09-13 04:17:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7f7c6ea-4a95-372b-9522-52b9ef9b2596 | -10.62645 | -50.56999 | 2026-09-13 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83b3456e-2b97-3500-a9f7-f3e602095998 | -10.95231 | -48.3605 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b49af475-dc1b-3ed9-b113-3878b8c37e54 | -11.82067 | -46.39952 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7124e01d-bc33-3fe2-808d-717f61a8767b | -9.95127 | -48.50768 | 2026-09-13 04:17:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 393c3359-b48d-30af-a62d-257bb156f668 | -10.6868 | -54.17422 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 63a9ff89-1274-3dfa-855c-cf861a4977e3 | -11.2024 | -46.33352 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e3e0560-ef36-3e16-851a-6769ca88044c | -11.83493 | -46.39798 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3024a252-27d9-3d72-bde5-8aed17d1fb16 | -10.08481 | -46.84238 | 2026-09-13 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30e6292b-2233-3e68-82b8-3ef70895ebbf | -15.63422 | -43.33179 | 2026-09-13 04:17:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5b1fe971-875d-3ebc-9495-5553bf990c31 | -13.45571 | -48.48804 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 400cd1ae-e4ef-3815-bdf7-9b60f3f8efde | -11.82091 | -46.37662 | 2026-09-13 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95d290eb-415d-38a5-8051-68e9baeb3ad8 | -10.55542 | -51.32764 | 2026-09-13 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d79cc207-b3ef-3de5-a82f-28725cf2179e | -8.0455 | -54.85612 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4c11627-56c3-3c7d-b396-0e66f3ada56f | -13.31102 | -51.72129 | 2026-09-13 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8521ba1-ac55-32a6-a193-374aa5a3d547 | -13.62713 | -47.87978 | 2026-09-13 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2e45e3b-6d97-3c73-a38b-23fd04a1c875 | -10.43912 | -42.74416 | 2026-09-13 04:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0cb9c76c-b38f-3a15-8cd7-ea796e799bd3 | -13.48504 | -48.49335 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 54f641ef-02c4-3cc8-83ca-892e9e74c037 | -13.45723 | -48.47914 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8da8e172-5e1f-304d-90f1-1b2e03cc07b6 | -10.90122 | -47.81897 | 2026-09-13 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90094d18-77a0-3cf5-a216-b2bfc07ec9d1 | -10.36021 | -48.22811 | 2026-09-13 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb506d7c-9d94-357f-87ee-46b7752e6d1f | -10.75584 | -46.24928 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6afa1ea7-a79c-31d6-8a4f-149d5fd0065f | -9.70797 | -54.36146 | 2026-09-13 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3a81dd-cc35-3e29-9c21-507ffb71bcc5 | -12.29113 | -43.68008 | 2026-09-13 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1f15661-b1b5-3281-a0d7-f8a0e468f673 | -10.46923 | -48.63889 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db0c9d70-1daf-30f6-b934-236c410c8f5c | -8.81338 | -46.91363 | 2026-09-13 04:17:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0827d243-5cc2-39dc-bebb-4634c7244af2 | -13.54126 | -42.54442 | 2026-09-13 04:17:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a05679e7-6585-3e74-a51a-a7d6984825b9 | -10.68198 | -54.16944 | 2026-09-13 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cf6bb8e5-60e7-3e11-818c-20b50a805e80 | -10.64013 | -46.0075 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c26c94dc-4c42-39ca-9be5-b1afc1df7033 | -16.78469 | -43.86748 | 2026-09-13 04:17:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7869d60-2537-362a-880a-ae75ce854237 | -11.48519 | -49.80992 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a2635de-f2c0-32a3-b734-1bcde5a12b37 | -9.55695 | -51.365 | 2026-09-13 04:17:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a4454bfb-f44d-3cc2-9a16-9254fde735f5 | -13.45647 | -48.48359 | 2026-09-13 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e817b0da-d32c-398b-b282-b90c7cbffacc | -10.45522 | -48.65105 | 2026-09-13 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a3967538-a72d-30c9-be58-2d8b29e350d9 | -10.62342 | -46.11177 | 2026-09-13 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0dc6d28-a29c-347a-8413-7967cd981f44 | -10.20638 | -45.29146 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a7df396-6c0b-39ce-8eca-8d256c4d45da | -13.54198 | -45.6673 | 2026-09-13 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a21a48ce-4879-3ffe-b7e8-dfeb1d2d7be5 | -9.49764 | -44.5457 | 2026-09-13 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88ee7a8c-de3e-3c96-80fa-cb0fc16760f4 | -8.12129 | -54.79459 | 2026-09-13 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README25.md)
