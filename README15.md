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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| afff754a-3b65-3508-bb84-48ac2ab5b85b | -20.14148 | -50.72154 | 2025-07-15 04:14:00 | NPP-375D | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c102afdd-940e-3a93-99ed-dc5afff83736 | -23.33574 | -46.13939 | 2025-07-15 04:14:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 891233f2-a2ef-3171-ae0d-c88d7a09a789 | -21.24003 | -49.19271 | 2025-07-15 04:14:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8eec6cdf-c4e9-3748-9a3b-5b2c42fd0e45 | -21.24389 | -49.19548 | 2025-07-15 04:14:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5f713c4e-385c-3ed7-b2cc-11602301e8b8 | -18.65235 | -55.71976 | 2025-07-15 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7650bdeb-2281-3421-8fa9-5063d67360b6 | -19.28689 | -55.16012 | 2025-07-15 04:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c60171ba-463a-3090-95c9-a66da855c2b0 | -20.31042 | -45.58444 | 2025-07-15 04:14:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a688e7e1-b9a4-336b-b127-b0d6d8c5ae34 | -25.45634 | -49.60979 | 2025-07-15 04:14:00 | NPP-375D | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 894d58a6-e066-3b51-9a3e-16e3b82812dc | -22.67675 | -42.85571 | 2025-07-15 04:14:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7f97cefe-503b-3553-b555-8146483a8ecc | -22.51557 | -47.0155 | 2025-07-15 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae25b4e6-ab85-3b54-9503-98ba9b1234cb | -20.76508 | -46.76892 | 2025-07-15 04:14:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 18079a73-5ad2-313b-a5f2-06cc528d4ac5 | -20.57955 | -44.57649 | 2025-07-15 04:14:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e0d0e7c4-7611-3653-ac61-61b521fedc11 | -21.77325 | -52.76193 | 2025-07-15 04:14:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7000c6a0-eb78-3e96-8767-64941e0fe737 | -25.24958 | -49.926 | 2025-07-15 04:14:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9743734d-5936-3f6a-b4ad-dd6fd802e8aa | -21.85909 | -56.7524 | 2025-07-15 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fbaf1e37-2328-3e2c-8e0f-e148591cc4ed | -23.68219 | -47.34097 | 2025-07-15 04:14:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8d345bae-66e6-3313-a132-b72f9be28ab5 | -23.98357 | -48.91902 | 2025-07-15 04:14:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8edec27f-3f1c-38c9-a39d-4aa9008016a8 | -19.28917 | -55.15823 | 2025-07-15 04:14:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68e53320-6d70-3cab-913a-a1a542b985c6 | -25.19303 | -49.3266 | 2025-07-15 04:14:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0afe512e-307d-3a74-a9c9-bd95426414b4 | -22.51623 | -47.01159 | 2025-07-15 04:14:00 | NPP-375D | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da7abb6e-eb75-3843-98b9-b3f109986670 | -21.2438 | -49.19348 | 2025-07-15 04:14:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cfb68f06-15f2-3afe-abc0-98cafd889fc2 | -22.54053 | -48.81339 | 2025-07-15 04:14:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae518e2-952f-3c24-b1b8-2e79b4ec6d9b | -27.08992 | -50.51619 | 2025-07-15 04:17:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 991f8c31-0e6b-3671-be2c-fd5fa54964aa | -28.17047 | -49.36089 | 2025-07-15 04:17:00 | NPP-375D | GRÃO PARÁ | SANTA CATARINA | Brasil | 4206108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac345aeb-c47d-30cb-8b9b-c9e8f56ccaa3 | -11.4393 | -45.1154 | 2025-07-15 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d1954026-f299-359e-9222-84411533e1f0 | -11.4588 | -45.0895 | 2025-07-15 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 81d23867-0826-3256-9cc2-fc9947c381cb | -10.5776 | -49.1316 | 2025-07-15 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 7019de27-4856-372f-9ae0-ac1a702485fc | -11.4397 | -45.0923 | 2025-07-15 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 37e86724-8da5-32b5-98e3-4ec919b786ec | -10.5586 | -49.1337 | 2025-07-15 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| b673ba99-b609-3696-976a-a3607e845c08 | -11.4584 | -45.1126 | 2025-07-15 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 11958464-e2f2-3216-a780-7587fcb62b91 | -2.54788 | -47.70401 | 2025-07-15 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb991be0-405c-32f3-9463-e5e22530e794 | -2.44616 | -47.46583 | 2025-07-15 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 70823235-8bca-309d-adde-d7a117387921 | -2.54457 | -47.70349 | 2025-07-15 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8019e0e0-b731-350f-8af2-1b1af3fabe50 | -10.5586 | -49.1337 | 2025-07-15 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d9e728d9-d5b5-367f-9422-9f37945c0388 | -11.4397 | -45.0923 | 2025-07-15 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c2c2abe2-4217-3fba-ba36-351ae871b3cf | -10.5776 | -49.1316 | 2025-07-15 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| fee36d72-92bb-36a5-9364-9405d894c85f | -11.4588 | -45.0895 | 2025-07-15 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| d3e23812-191e-331d-858a-c1bd57db08a0 | -11.4584 | -45.1126 | 2025-07-15 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ce57e1ed-e377-3f4e-9b11-f0bbc28115e9 | -11.478 | -45.0868 | 2025-07-15 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| dfda1eac-8b18-33e1-8741-3adad3e41f4c | -11.4393 | -45.1154 | 2025-07-15 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0eafa634-234c-3e15-aab8-dccfe710e34a | -9.98257 | -48.08346 | 2025-07-15 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 186e3e49-7ffb-3aa4-95a9-73c1979e8672 | -5.70043 | -44.24857 | 2025-07-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d462c431-6766-3b22-a5f9-e4de5758153a | -10.2789 | -47.61636 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cae6d66c-43f1-3ed8-8ed0-6da10daff2b7 | -7.09252 | -49.17448 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e423fe12-d701-389f-a436-18fda0384390 | -4.03408 | -48.062 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4eef05ed-8a1e-380d-836a-049e825a03fd | -4.61435 | -43.3214 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b33709da-fe7e-3ff0-8e7a-f7dcb77406c7 | -9.36659 | -48.54812 | 2025-07-15 04:32:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 07aad1e7-f3ba-3ca5-b127-fb77bac3dff6 | -5.37047 | -43.92764 | 2025-07-15 04:32:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6af2f49a-9fd7-3fd9-a5c9-26b3a69d83c1 | -7.28323 | -44.03682 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab2d7c26-b538-38fc-a932-ee4b75c725f5 | -7.99106 | -43.38289 | 2025-07-15 04:32:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 611fb8c6-3947-39b7-a298-e952bcc46bb5 | -4.05104 | -48.75057 | 2025-07-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e727aef8-fc05-3edd-b3f5-5e2cbbc03028 | -8.38462 | -51.07182 | 2025-07-15 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6af63fcf-6a7e-3282-88a3-5e42059e6a53 | -4.03463 | -48.05855 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7655714b-67b4-306e-80e3-a5e6747bd604 | -5.78785 | -45.09519 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e249aef5-aae2-3f5e-9fdb-24f256f08934 | -7.20925 | -45.32848 | 2025-07-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af22ddea-2853-367e-a92b-eaa83c02336e | -10.37536 | -47.14573 | 2025-07-15 04:32:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 125ecbc7-1fcd-3815-8ed5-1c30d1036230 | -8.60622 | -47.43772 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f6f4ed-3b4c-3811-96a2-e64264c790f7 | -7.20104 | -43.10426 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 085c6341-efc1-33c5-84e8-27ee783f6c08 | -7.03972 | -55.4361 | 2025-07-15 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 895b9eae-c1e9-37b3-9a6e-cd6e451d8ddb | -7.09494 | -41.47744 | 2025-07-15 04:32:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7e5d8316-5b93-341b-a70a-fecb727e283f | -8.60288 | -47.4372 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56b3f957-a7f0-3029-99aa-9c6655b6383e | -8.57128 | -45.54503 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8b7e7bd-4328-38a6-9c18-c8488ed7a00d | -7.63977 | -44.42331 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d717af3a-8b03-30fe-ae43-0a65185ae16e | -4.01152 | -49.46697 | 2025-07-15 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62a7efb6-1c3c-3bfa-ba0a-ee1a75da12ac | -7.92969 | -42.88889 | 2025-07-15 04:32:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4477b957-e664-3d5f-8af3-f33056bd6c24 | -4.04769 | -48.75005 | 2025-07-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28d8183b-6fa8-38b4-8268-99eb79c47705 | -7.16266 | -42.96692 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c4a3fa36-85b0-3f72-8de5-289d218008fd | -7.19984 | -43.10791 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b280f4c9-799a-322a-a67c-6429a06da9e5 | -4.87368 | -47.76049 | 2025-07-15 04:32:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc8e3579-f421-3339-8c43-f65f8f938005 | -7.09631 | -44.38383 | 2025-07-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d65c644d-5858-38d9-86ba-b9d1af0a5acd | -3.58578 | -47.52135 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44204214-9b86-3fe0-9682-338549e2babd | -9.61919 | -49.09925 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9e77633-4976-3436-a7ce-f09b4fada4f3 | -7.89315 | -44.49139 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ca5362e4-ca2d-3262-8f71-65f2ec690a9c | -8.56927 | -45.54176 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7c50932-5024-30be-acf2-49fbca5374e6 | -10.28281 | -47.61329 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5e3c09d-9084-3185-af08-1a5cd38ff80b | -9.37217 | -48.2313 | 2025-07-15 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cc8528b-75c2-3eed-b151-e9373fd6409a | -7.8894 | -44.49083 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f222eb54-4212-3f28-bc6c-935fb16dcfe8 | -6.38048 | -43.71339 | 2025-07-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 056194ef-a9a8-31e5-8923-5c2d0cc0a189 | -6.15421 | -45.8517 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 658ad9b7-7cf1-3ed3-9100-832003ed9770 | -5.53574 | -43.88132 | 2025-07-15 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51577a5e-ecdb-351b-b026-02a87f1afe0d | -7.08743 | -43.69696 | 2025-07-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2958d80f-dcfa-36ff-b34f-347bd0f242db | -7.66498 | -44.40857 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78d8628d-cf29-3d44-8b7e-065aef2b7809 | -6.17024 | -45.88503 | 2025-07-15 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c0b3378-e660-3f5f-9203-720c8ad78696 | -6.99354 | -47.08641 | 2025-07-15 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66df5958-b055-3b20-ab76-9665627e2fdd | -4.03685 | -48.06598 | 2025-07-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c4786de-bd10-3060-b9ce-9a21a6dc59fa | -5.53506 | -43.88583 | 2025-07-15 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a8f7d86f-b69f-3713-893f-57e0d54d3786 | -3.75799 | -47.11913 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac3c911a-08bf-3b07-990b-effa91fe1ba8 | -9.80754 | -47.74476 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8e0a56f-3be7-3d18-acfa-02c66c30e8db | -9.80421 | -47.74424 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f1c81e9-6276-332c-8ed2-42bcbaeba2d3 | -7.29955 | -46.26321 | 2025-07-15 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dce2d1a-99e6-349d-b2c7-67ee4135785e | -7.63602 | -44.42276 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 317062ed-543c-3cdf-a6cf-14625ff3b02b | -5.53813 | -43.89091 | 2025-07-15 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 19cb33b2-e10b-383e-9633-efca4312e2dd | -2.91188 | -48.23938 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27ad7535-a880-36a0-a607-abb917924955 | -8.6001 | -47.43313 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcdc0d94-6ef8-39b0-b8ea-c201d1742b3a | -3.42626 | -43.34986 | 2025-07-15 04:32:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7baaf3fe-f2fd-3d01-a6d0-1decc9e6e14c | -7.2792 | -44.04435 | 2025-07-15 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f0307e2-4d32-3b2e-89a9-26c8bd0ee984 | -5.78067 | -45.1184 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae137e5-004d-3d6e-8c88-638576956f4f | -6.71175 | -47.80308 | 2025-07-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08faf500-d7c3-3599-b028-90bdb77e4c13 | -6.91393 | -52.85582 | 2025-07-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0aae04b-a9fe-3f29-ac53-81a5d5c4ce67 | -4.27002 | -48.18114 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README16.md)
