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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe44e2ed-142f-3ebb-bab6-3d7e8e66b912 | -10.54137 | -46.59842 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7e881dd-e5d2-3da1-bb68-2d6bdc57bb26 | -10.62996 | -46.0509 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc2d70b-25b3-39dd-ac98-ac48d4905dbd | -8.76807 | -44.22562 | 2026-09-19 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f3e4edb-59f3-3e13-865c-40f3a869ec26 | -7.29345 | -44.52758 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d076fc20-9f89-3b04-bffa-7eeeba83cfad | -9.78164 | -45.0577 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 977017e4-32c3-3a2f-b857-914786c9e24a | -4.35717 | -47.78107 | 2026-09-19 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c01eb45-7b35-33aa-aa71-4ef83d7456de | -7.48832 | -46.12331 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0b081f2-3f2c-3ce1-bc8a-1bb68583e9d7 | -7.19199 | -50.82896 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1be5fc61-2cec-3dbc-ae0b-48c6c0df99d5 | -8.37272 | -47.21906 | 2026-09-19 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9270480b-591b-3a5a-b754-2746de2c20a0 | -7.6847 | -46.11568 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fe98945-190a-3478-8b21-77bf38b1af72 | -9.03488 | -48.72254 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a33692fb-d840-3977-bd51-4e59fa975914 | -8.61303 | -54.59462 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9bc7d1d-7516-3939-8997-b205ffef4050 | -9.24899 | -46.20212 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90ed91a1-ab39-3f2b-9aa9-373eb0fffbec | -9.24711 | -46.21307 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18f30e04-79dd-34e6-93eb-aeded294d1a0 | -7.63783 | -46.11197 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6f7a8b5-26a8-33c5-a479-c640c68f74e7 | -6.02065 | -51.76859 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8f6fdff-5251-378b-b1d5-2fc3a2c88575 | -4.56113 | -42.9796 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e56f6a0-4e06-35c1-8ba7-d91b60c65640 | -7.02358 | -44.65494 | 2026-09-19 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2c2941bf-e5c0-39d7-b268-2bc3ed8b2379 | -9.9554 | -46.54568 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f2a662c-a3d6-39a9-b420-2c98a66f6bad | -9.78466 | -45.06299 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d79b215-5882-3ced-94c5-a235d100c298 | -9.04556 | -48.74772 | 2026-09-19 04:02:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57cfd878-5b23-37ed-964c-0419a8bfaa73 | -11.22393 | -42.82858 | 2026-09-19 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 8200e695-45f6-33fb-b258-811fdad36b9d | -9.24496 | -45.93377 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb07d06-b5fb-33ca-b3c8-7db9da502f24 | -8.63917 | -47.53916 | 2026-09-19 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24495b5b-2525-3998-9c32-fd0dc425e5c7 | -6.58098 | -44.15604 | 2026-09-19 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 67936fa9-ee25-3e46-9609-f1a344a24490 | -9.75075 | -46.08108 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eebb288-b613-3191-8b7d-90c48ad9c577 | -6.29942 | -41.77075 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f4287c39-9193-3cdf-b18f-401655953c68 | -7.04382 | -42.08422 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 08995abb-214f-34a5-8035-c4f8766e1021 | -9.55607 | -46.58931 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8875e5e5-44fc-3985-8fb2-4f903a3cacc2 | -3.37646 | -50.45884 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a60031a-2336-3f58-b2e0-f69ab546fd72 | -9.20853 | -46.76934 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c23972ec-9aed-387a-bc5c-1a0d736010c2 | -6.99352 | -49.76561 | 2026-09-19 04:02:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcb7e2cb-4e1f-3672-a083-ffd48e901d6e | -6.99243 | -42.18299 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f032f662-7b2f-385c-874f-bc5a3fac96b8 | -10.61305 | -46.10224 | 2026-09-19 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e81e7535-81ed-3b50-93ff-e64978b40263 | -7.79252 | -44.95285 | 2026-09-19 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d95f433-5230-3177-83c0-4b1afca303f7 | -5.07297 | -44.85489 | 2026-09-19 04:02:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66feb4c9-2016-3039-b860-9408ace788ce | -10.53933 | -46.59866 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4467d0ec-541d-309d-8cf9-07efccd1bd52 | -3.16818 | -48.60975 | 2026-09-19 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5935acac-655f-3240-b22d-972a8590422a | -3.52923 | -44.84282 | 2026-09-19 04:02:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e37527c-8de1-37a7-9ab9-746cd90e7707 | -10.53302 | -46.73064 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c347f67-a292-39a1-8119-129ab9b255c6 | -9.02797 | -48.73296 | 2026-09-19 04:02:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 85cf403f-822e-32d9-8c39-93c6c025cf28 | -10.09869 | -48.42278 | 2026-09-19 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20b17da4-d5d5-3334-90f4-436cc1849546 | -8.66205 | -45.45706 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a27617f-9233-3348-98d8-ac1ff9cd5315 | -10.36067 | -48.89386 | 2026-09-19 04:02:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33ab5131-3590-3acb-9ee9-e7cfd0e8b273 | -7.32689 | -45.3266 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 21ea9d2c-7ddb-3445-96d6-4f574c9095b4 | -6.58475 | -44.15667 | 2026-09-19 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7b5be39e-7f1c-3434-bc40-dfd53159586a | -7.19164 | -50.83151 | 2026-09-19 04:02:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce39862d-8255-3f90-979b-2ebffc869061 | -9.55741 | -46.5814 | 2026-09-19 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 117d97b5-a442-35d0-b052-f3aeca29239f | -10.58227 | -46.54809 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5526f93-499b-359c-8643-18cf8acfeaa4 | -7.08321 | -44.71238 | 2026-09-19 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4455c4a2-a6c3-3364-9dfd-026c82199451 | -6.28751 | -41.78012 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4bf14e04-9fdb-357f-b659-644d604faa68 | -6.48859 | -43.81915 | 2026-09-19 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b359eba-8983-31a2-a313-92518a063097 | -9.93607 | -46.60762 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08a2873a-c443-311c-b08c-e48982943ce0 | -4.14503 | -48.22225 | 2026-09-19 04:02:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 49a75420-80c6-3c00-a263-15cfa354babc | -7.64137 | -46.11658 | 2026-09-19 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 59211bb1-1459-3a42-92db-ac99d464ddb3 | -8.82835 | -44.90134 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7fccede-bd38-3989-bed0-2e3b30a45219 | -5.73146 | -43.28259 | 2026-09-19 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| adf8fac9-df99-384d-8c57-baa891d864a0 | -7.60439 | -45.42025 | 2026-09-19 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e48e7a5-d075-3f4d-89a6-d73539c183c4 | -2.82789 | -50.46699 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| b42eaeb8-88e9-3836-aee4-c43c58b245bd | -9.25314 | -46.20263 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7d93c06-ced5-3159-bf32-42b9a40568f8 | -9.91162 | -46.52646 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec7b04b-d764-3763-b841-3c887fea231e | -4.28365 | -48.58614 | 2026-09-19 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fdcc2b44-037b-37ea-8f6a-f169cfe77ca2 | -7.21615 | -49.63552 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3736f4b7-2bdf-3030-b8f1-1a53bc9a80e8 | -9.56362 | -45.46785 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 890442c9-2556-32d5-866f-82408d3ae185 | -2.66625 | -49.48556 | 2026-09-19 04:02:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90e3eee2-2afb-3476-8bc6-470bfc7943a0 | -9.00877 | -44.91304 | 2026-09-19 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd49e34a-d29a-3086-9f8b-71e409c7f281 | -7.58061 | -43.44716 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 918e1e4e-496b-3e72-9e87-07fd68b84b71 | -5.06894 | -44.85424 | 2026-09-19 04:02:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 124c81b0-2a9f-335c-8c31-c5852282b5f3 | -6.08711 | -44.30131 | 2026-09-19 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a59cfbaa-7823-31cc-bab1-20fa4d308a40 | -10.20974 | -46.59132 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efec0e24-d47b-3e90-b307-73b640b6328c | -7.19921 | -47.86944 | 2026-09-19 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fe2c74a-47dd-3925-b963-1d6e0b5a0216 | -6.90762 | -41.70665 | 2026-09-19 04:02:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3d61b33e-c6b4-3309-aa1f-00b271471e73 | -10.2045 | -46.58599 | 2026-09-19 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4db4afcb-5b2b-3542-a6d5-17e4368e4d28 | -3.33653 | -50.11492 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b08870d4-3f8f-34a6-9e86-0b5e01e36db6 | -4.59777 | -42.95963 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d813a3aa-6220-32b1-b2e0-8ae3bf067d23 | -6.28411 | -41.77963 | 2026-09-19 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b1858016-9f3a-3737-8167-88b7adc6be1c | -7.22092 | -49.6398 | 2026-09-19 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63220200-ebcd-3301-9eff-51e1bfa371e6 | -10.48778 | -46.29875 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2630e522-6458-3a10-ab77-6d54bb1c8537 | -3.33752 | -50.1188 | 2026-09-19 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69cd498a-b7de-3950-8b8a-ec6e5a4cedbd | -6.99303 | -42.17925 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 66e9c0a4-e3b4-341b-8fd0-71cb8844e23d | -8.43973 | -45.74785 | 2026-09-19 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c57e3d8-c933-3562-acc8-f18db836041f | -9.76866 | -45.06514 | 2026-09-19 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4bffe242-833a-3b12-8115-0c779b33b4e8 | -7.58289 | -43.44625 | 2026-09-19 04:02:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e68811c0-3a7e-33af-aa40-c86b2b96f573 | -10.47837 | -46.30465 | 2026-09-19 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f224bb5a-7b1c-3a7c-86f7-c16bb66b54c8 | -8.12665 | -44.82495 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2f251f1-4ca9-3085-bc57-d87dcc3b65ec | -8.98978 | -50.17442 | 2026-09-19 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbdc9743-f9b3-37e5-9e4d-34339b509b8e | -8.66383 | -45.44675 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 63e0daed-8606-3116-b8ab-7c01c1bf5e5a | -3.36658 | -50.45524 | 2026-09-19 04:02:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8b87e74-53fd-3873-933a-35872b377000 | -9.57485 | -46.56046 | 2026-09-19 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43ec2b6d-8304-3377-a3f3-d2905e936623 | -11.15868 | -42.79485 | 2026-09-19 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46184838-39eb-35a1-824a-2414f5eac1bd | -6.98218 | -42.18137 | 2026-09-19 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 61a63b79-3396-3c03-9419-851c1bbded0a | -7.78301 | -44.8837 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dd8a0c1-52e4-3d84-a9e3-37a0e46ca951 | -9.607 | -45.37797 | 2026-09-19 04:02:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe5eed89-2f7a-37e1-8b60-feace7c6c220 | -8.68038 | -45.42656 | 2026-09-19 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37e8404a-9230-364a-a593-c42130ab2fe4 | -7.20459 | -44.0984 | 2026-09-19 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7031ce2d-fc64-3ebd-8cd5-2b2d700cf8d1 | -7.83485 | -44.91465 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76209774-146e-335e-9d84-b7445c8353d4 | -8.12306 | -44.83648 | 2026-09-19 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a4fdf85-1cf0-37c7-a196-cd20f65ab676 | -4.57267 | -42.97718 | 2026-09-19 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 206f1d51-7069-353d-8092-ab5797962695 | -8.61038 | -54.60824 | 2026-09-19 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3ea9b4ec-1738-3b1b-9fa9-8a5ce5d9c4e0 | -8.319 | -50.9213 | 2026-09-19 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README32.md)
