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
| ba72c0d5-37cf-3539-b4b4-bfebf7e5395f | -3.02692 | -45.23531 | 2024-12-18 04:25:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b971622e-7191-3491-b54f-735e0001b868 | -4.52768 | -45.8667 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e94aba19-b98e-3d45-b86b-3a259587fd6a | -1.40598 | -47.47475 | 2024-12-18 04:25:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1192bc9d-acb7-377b-8bcf-139ef9a5e343 | -4.15406 | -43.57165 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9190320e-0199-3982-913c-75be89d1ca53 | -3.07534 | -40.0521 | 2024-12-18 04:25:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a30cdbd-6b23-3fed-964e-57cb379fe8a4 | -4.57498 | -45.88519 | 2024-12-18 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1deb6af0-dfe1-3591-bfb4-2159fdcd3be8 | -4.48358 | -42.86938 | 2024-12-18 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a704eeb9-9534-3d25-9acb-dc05d88463ec | -4.52381 | -45.86963 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3feebef-77ac-32c1-b3dd-c66f96fb6407 | -2.35153 | -48.48674 | 2024-12-18 04:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 061d3b63-cbac-397a-b1a0-9c5e46579346 | -2.87607 | -45.24738 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e59ae96-b425-3293-a41d-d8d776f4e239 | -2.92757 | -45.24476 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8e81432-3ccf-34fe-8991-b21fe21bf82f | -1.42557 | -55.45566 | 2024-12-18 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b5cc8bf2-d04c-3fb5-a5f9-825425bce70b | -3.95908 | -47.97657 | 2024-12-18 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 071abb6b-764e-3c13-b5e1-c379a9e850eb | -6.63765 | -47.34617 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3ca556a-428b-35c2-a2e2-787ae77ef7cd | -4.18672 | -44.03314 | 2024-12-18 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f4b8508-63ac-3081-b383-b224dda88617 | -3.87005 | -46.58104 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65912296-e402-3025-97f8-3f41ccf2e6c7 | -6.22101 | -46.222 | 2024-12-18 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e95e26-1650-3ddb-9a7a-00d61ec45ea9 | -4.04959 | -47.01068 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ebc626-1b2e-3b05-8936-673ceb3d0ec9 | -4.3848 | -42.14593 | 2024-12-18 04:25:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 147724e3-2f99-34ca-a0ae-01163d3876de | -5.39466 | -43.24393 | 2024-12-18 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c479036-6d5f-3de3-92b5-93f1508c5ff0 | -4.15346 | -43.57546 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e93c76bd-01a3-3d20-b303-60c223f21265 | -4.11862 | -43.57021 | 2024-12-18 04:25:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be718446-ac1b-33c2-a1a3-aabab6e6129f | -6.11361 | -44.0465 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ef79939-af70-363d-a1f5-910357a52ea4 | -5.98493 | -41.66043 | 2024-12-18 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 10ebcf2b-e02c-3872-9cd1-dae70af19faa | -3.91019 | -46.66624 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0ace02a-31e2-3c3c-a2c2-d133b157778b | -3.24459 | -46.87395 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0e281261-f0fd-38c6-a91b-40cd8963493d | -3.16382 | -45.9754 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a5e0af1-a0dc-37ed-85bd-b0eb59f0ac89 | -6.14078 | -43.91671 | 2024-12-18 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd3f8937-2882-366d-98d3-64688949b101 | -3.16104 | -45.97143 | 2024-12-18 04:25:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f93817f-ac32-3d1c-a961-d6b9ad117c66 | -3.24122 | -46.87343 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27fa1ef7-0b9c-307b-937b-aa6cc6679539 | -2.76374 | -47.39366 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4916972b-4df5-3d14-8834-6c0a83dd3279 | -3.85763 | -47.03877 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea1f1693-a92f-34f0-8188-5fadf5fb54f7 | -3.8762 | -47.03072 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f9812af-fecc-31da-ae30-e18fc5765446 | -3.92964 | -46.93331 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d990f702-b338-3a04-b2c3-ad8e05146c10 | -6.19474 | -44.42467 | 2024-12-18 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1f10289-e88f-3586-b6de-9680272001db | -5.81781 | -42.76386 | 2024-12-18 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7646def2-e708-3252-91e8-7c27c1850123 | -5.96996 | -42.31298 | 2024-12-18 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8692ee50-1f2c-37c3-a97e-e7e3f67c5242 | -4.06087 | -47.10011 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80e718a7-b748-3315-9825-27cb40d423ff | -3.87901 | -47.03479 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7555f47f-c7d9-384d-ab0f-b3fd5e8f40cf | -6.29549 | -46.04511 | 2024-12-18 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d65c1aeb-2732-31df-a675-23c0019f3492 | -4.00685 | -43.75469 | 2024-12-18 04:25:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0095e094-a943-3b62-a2bd-2a5fa5ca24ed | -4.07717 | -47.10634 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e67cb47a-4449-31d8-ad92-ca215358dcdf | -4.53953 | -43.29319 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c2bfe449-58a6-314b-a77a-7dfcc3650250 | -4.42262 | -44.21877 | 2024-12-18 04:25:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b46abe5f-153c-399f-824f-2e59ae7069b8 | -2.45997 | -47.8307 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95461344-2d51-3ff6-947e-73199dc5aafe | -4.26507 | -48.56401 | 2024-12-18 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8305f017-a06e-392c-8fec-b2e084188a57 | -4.21986 | -44.31097 | 2024-12-18 04:25:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f7ed4c6-9cde-3179-af61-4e94b40b5edb | -5.40405 | -46.57254 | 2024-12-18 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f3bf59f-71b6-3540-bcb8-0f9c57c17d7a | -4.01319 | -46.9357 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3dc1e08-517b-3349-9a2d-d93db1f66a30 | -3.8582 | -47.03521 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b1a7097-124e-3481-9c08-d6c0ba39ebe1 | -3.69314 | -44.64812 | 2024-12-18 04:25:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5e1e12c-f758-3483-93d8-3849f22b0984 | -6.30119 | -38.90804 | 2024-12-18 04:25:00 | NPP-375D | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79846249-f5df-374a-90e8-28406d9df031 | -2.57113 | -47.94645 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6b2708b-104e-3d93-a465-20e426c1a707 | -5.98747 | -43.48449 | 2024-12-18 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5acb8e99-ed9b-3973-9364-5bb8a9d20ab3 | -4.03555 | -47.03397 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc7a29c3-c74b-33d0-ba45-49fe5e1d9958 | -3.87562 | -46.58909 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66d950d1-6bdb-373b-8ce8-4e08f4e22bdd | -2.05262 | -46.6554 | 2024-12-18 04:25:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfa52d69-36f3-31ed-866b-d08d53567dab | -4.50986 | -46.04456 | 2024-12-18 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98addbfe-f189-3861-9b05-4b63e56d7a82 | -5.60452 | -46.8045 | 2024-12-18 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8190947b-06be-3b35-97eb-282fa9e0ce62 | -3.07115 | -40.05145 | 2024-12-18 04:25:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f16dc071-7019-3f3b-abb4-0131cab313c1 | -4.02768 | -47.04005 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e8e829-aa17-3cef-aca2-8a30434eb1d9 | -6.63429 | -47.34563 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5b6173f-9f7c-3006-a4d1-46e4f15e1407 | -2.3617 | -48.49256 | 2024-12-18 04:25:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23518540-b57c-3561-ad0f-26beeec4405a | -4.57776 | -45.88916 | 2024-12-18 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3f23e246-cc50-32b5-baa0-b99fac6a2254 | -3.24009 | -46.88052 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 99a42fc8-4a6c-33c5-8d5f-4551799b3bc3 | -4.06473 | -46.91476 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 143eeecf-3dd9-3ae1-82b5-03558caf37d7 | -5.94548 | -48.06529 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbc102eb-8cd6-3086-99a2-d5d264e05dc2 | -4.04902 | -47.01425 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51e0754c-b8ff-3a1d-8938-241164659425 | -4.01431 | -46.92865 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbde3c53-25f8-3d9b-b34e-cec1dcbf73e0 | -2.79754 | -46.71313 | 2024-12-18 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0408fca-09ae-38fb-8bbd-b21e9401d215 | -3.34126 | -53.01727 | 2024-12-18 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d747c2f-249d-3903-a1b1-41cc73002fe4 | -2.86074 | -45.49609 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 92cb0b4f-3afe-3600-8d2b-b223c03f3778 | -2.76717 | -47.3942 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d21f049d-5f61-34c2-9f23-7164a9d697f3 | -4.39239 | -44.10159 | 2024-12-18 04:25:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d77d3f2-70ee-352e-9c51-2f47b00e0c33 | -6.21158 | -46.21697 | 2024-12-18 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8b7de70-2566-386b-9e94-82532b4bed27 | -5.97259 | -42.31543 | 2024-12-18 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 56bf9056-a46f-36f0-854e-47ae217c7890 | -4.54721 | -43.29029 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65d2a70a-6d79-3ace-b21a-2920c4466d31 | -2.87329 | -45.2434 | 2024-12-18 04:25:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fee226c-5fce-343e-9f06-bf1f172aaf93 | -4.54661 | -43.29426 | 2024-12-18 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85043398-7bf9-35b1-a3dd-fc865412fddf | -2.53614 | -45.53697 | 2024-12-18 04:25:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca8f6c35-5291-3920-a501-dbfa6b429835 | -4.93549 | -45.09659 | 2024-12-18 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93f1478a-9df8-3ddd-88fd-e9fd1216868c | -6.11709 | -44.04704 | 2024-12-18 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb4ef48c-044d-35e3-82a5-daf9b65ee058 | -2.79681 | -47.42931 | 2024-12-18 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 469cd2e0-9ddc-33ab-bbc8-aa3ea9f1bdef | -3.87564 | -47.03427 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c2df952-690f-322a-a0d2-fffe5f0a8441 | -4.00744 | -43.75094 | 2024-12-18 04:25:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eacc01f6-2f13-39ae-9ab8-f1d343766e4d | -4.02833 | -46.90541 | 2024-12-18 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 962dd0d9-deb7-36e1-8336-558be1887555 | -2.08805 | -45.28656 | 2024-12-18 04:25:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f9cbb04-23a5-3035-93a3-9c4b13600d9d | -1.62071 | -45.85017 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9c33b5d-8835-3ccc-907b-71e22b14625b | -1.70198 | -45.78474 | 2024-12-18 04:25:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 979b3ab2-a0db-3560-b5d6-2d7d07930ac5 | -3.6937 | -44.64458 | 2024-12-18 04:25:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34d1c50d-67fe-3ec9-b8d0-bacb6d740d9c | -6.63486 | -47.3421 | 2024-12-18 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 062a360f-616e-30f5-a077-dc02c20819bf | -5.13544 | -46.15411 | 2024-12-18 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e02bc15c-4b52-36b1-851c-4b04e968a234 | -7.86067 | -43.08507 | 2024-12-18 04:25:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bcee56b9-7a88-3589-bf6a-3d202298ff99 | -5.94891 | -48.06585 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1709560-260f-3b01-8499-becb9166ce31 | -4.04846 | -47.01781 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d741bf0-c072-3590-9ccb-02d43665cdb4 | -1.65337 | -45.89799 | 2024-12-18 04:25:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7500e12-9ee4-304a-8fac-4039ff8c84d2 | -4.01308 | -47.045 | 2024-12-18 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 372a57ba-be57-3f28-8871-20118caf5fe8 | -6.32949 | -46.13225 | 2024-12-18 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ec03b20-b05e-37c1-9583-aeb6f545b8b4 | -3.91298 | -46.67028 | 2024-12-18 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a94896c-5e7b-3a7a-8a52-4f194264ee1c | -5.9483 | -48.06957 | 2024-12-18 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README16.md)
