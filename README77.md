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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e62fc60-732e-32e8-8795-389eaa32d80d | -6.1624 | -52.6397 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb528bcc-0eb3-3116-8ae7-fcb14cbbf3e1 | -6.7872 | -55.6402 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8799601-5e4d-3c73-8f8c-65a8eed61aa4 | -9.03339 | -65.40182 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0806f9e-fed9-36df-8e1d-7f0fa147d91b | -9.52633 | -68.56496 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d41ec71-ec61-3bfa-851a-3db683776c41 | -8.40583 | -62.6616 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c56f5717-dd43-3020-a0c1-e113eae2d7ee | -8.75458 | -70.81049 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 272ca0e3-df34-349f-b900-24c05e9c69aa | -9.17696 | -59.63457 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad07f6c-3ef8-32ab-8a99-edc7994bd005 | -7.62734 | -55.29659 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f5d38e6-f4a5-3a3d-8f27-df5d9f5d51a8 | -7.05172 | -52.71645 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d3596b-c73a-3bd5-8b71-6b5a3b73ba5d | -8.75181 | -70.81136 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7f93680-5468-3b7e-8a12-c3060cedb5a1 | -6.8871 | -59.40865 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a087c9bb-b023-3b31-9d0d-dd7f6dbde43f | -6.73901 | -56.34027 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eec9cf8-0c6f-3887-95bc-b4f1ec677bfe | -7.56152 | -60.46739 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c69a40-7203-3d43-9b2d-9d47ad61453f | -7.25624 | -60.63238 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ef43e62-c9a1-3539-a08a-2657e1c4e529 | -5.95585 | -57.68339 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 609d7f14-4e9d-39f3-84a3-1ce461f89e04 | -7.92904 | -61.35161 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5e6eaca-5dbc-31a4-b2dd-1017a9c449b1 | -8.5849 | -66.97248 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb5a4af1-c38b-3ba5-9235-dd761ba539da | -6.5588 | -58.5617 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69c252b1-1108-3651-9486-2968d86e77fc | -10.84174 | -54.03994 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e38b808-d9bd-3437-a30a-6d4d6cae55df | -8.67411 | -66.51442 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 375f8253-863f-3507-9f40-5ea92c1e7aba | -9.18466 | -59.45953 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5c6b7674-bd63-357f-a7ea-ba84ac891f02 | -8.60416 | -70.21161 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20b6396a-731e-36ef-8d38-075707be3a3d | -7.04096 | -59.23042 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c06261-704e-3e95-b872-6af072eb42f9 | -7.29684 | -60.57402 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4a270ef-5d35-3fc8-aade-b62e680e893b | -6.95922 | -55.64372 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1ff07f68-8bdc-3d5a-b9db-bbed341dcc93 | -9.02446 | -65.45672 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bdb351c-c084-38ce-a739-364aa65f3950 | -5.48772 | -57.14462 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aae437c6-ff00-3149-867e-7907e981012a | -7.34187 | -60.57689 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 103a4000-f552-3b64-b8bb-fca2f78172d4 | -7.30471 | -60.56736 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 89bc0882-3071-33a7-90d8-24a8448754e6 | -8.26114 | -62.75981 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5e1f555-59a2-35d3-acc7-0f25aac0d01e | -10.76841 | -61.74584 | 2026-09-01 05:36:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fef3aca1-ce24-36ef-890c-4523bf2d285e | -7.03861 | -59.22151 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85880e8b-90b5-3a04-bc0e-2cd3de78d067 | -7.18618 | -60.67857 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af3d2ebb-35fe-3a9c-b0f5-3c085f3633fe | -6.7824 | -59.78848 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d8da0b9-bce0-3650-9c5b-4fe438e5df2c | -7.05728 | -52.71724 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7385239-6eb3-349a-97b7-a5de0087d31e | -7.62263 | -55.29591 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a000e8fe-3cf2-3c0e-9f38-5fdf741b98aa | -10.41669 | -57.23301 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d048835b-6427-35bb-9d30-fb68afcb748f | -8.78984 | -62.4879 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1e20dd5-4057-35d1-9862-8bbf738bcc40 | -6.80826 | -59.57234 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 935c1121-a86f-3f1d-8522-3bbb1dab1e8e | -7.93128 | -61.35932 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1423a22-cdb0-3117-9f49-e7f953dd6b7a | -6.59725 | -58.58565 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f80d985-bc6a-35b8-82d7-b3b362756c58 | -11.30394 | -50.58442 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f3e56d9c-3054-3812-a5c8-42fefa7ce881 | -6.9591 | -55.65139 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f7bbd2a9-2818-3529-bb97-40d0539c037b | -9.39293 | -60.57052 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c9bd075-57ae-3e9a-a32a-1e4384864fed | -8.26169 | -62.75634 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929157d0-ad56-3b14-ad6c-0aa569eb25db | -9.0606 | -65.48201 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 621f90d1-92fd-3726-9cfb-d689b2b6fccc | -7.03006 | -55.64248 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 177f057d-c9dd-3669-a8c0-d101a6ab2464 | -6.79883 | -59.39615 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f50ba933-0247-38a0-a210-ad5796cd5a4e | -7.02482 | -55.64653 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7752347e-976f-3a1a-b1cc-41ae14e5bfbd | -7.35329 | -60.59391 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b380c3a5-8372-30f7-b6f5-258d5009b235 | -9.47608 | -57.02632 | 2026-09-01 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e34e1a49-1e41-391d-88be-88148376eacc | -8.50491 | -55.31367 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eba4b5b-925f-3b8a-a7d7-b55d5447dd6b | -6.93715 | -55.63586 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eeb9868-f536-3046-9607-c1c59b0f61a1 | -7.351 | -60.58596 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0520a9fb-5188-3a06-bf94-756b6e890d6a | -9.02603 | -65.45197 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1871678-04d7-3ad6-a4a8-d116f187ace1 | -8.78379 | -62.50481 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dba2e007-9505-3834-9755-74db952783bc | -9.25095 | -60.43056 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 914bd194-0f55-39e1-8128-5c9d13d9d778 | -8.8825 | -66.88926 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5e9c41f-148a-3077-a910-2d6e9bc31b06 | -7.72813 | -60.97926 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a62f8ab1-112b-36aa-aed7-db9e5b3af71c | -9.06345 | -65.48653 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfcf8141-190e-3d76-87f5-382f3bcee705 | -8.94093 | -62.36866 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21f00709-d24a-35e7-a128-1b8d07a9daa6 | -7.34464 | -55.19716 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac24e5b7-5cef-354c-89d6-e9b43acfe64c | -6.37479 | -51.75931 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 992f91d8-466a-3e91-9f74-bc9ef96ad413 | -8.1198 | -54.96166 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d2a7ecb0-a421-30e8-92b9-641b31f04373 | -6.08652 | -57.72079 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28eb680a-73ba-3ba9-9565-20247c9dc37c | -6.79463 | -59.39968 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 160bb94d-fd4d-3b90-bbc2-5ec7fddaad4b | -10.74759 | -54.069 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67fee994-e047-3d2c-953c-af89c2ab9d8e | -7.41184 | -55.1651 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 019ad379-f92f-31e5-bfaf-426f97aaaefc | -7.34739 | -55.20173 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 49e2d5ce-c1d7-32c3-a749-9e678210656c | -9.15206 | -60.93931 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ccd4ed0-2410-38c5-a5fb-8b398bce5642 | -6.67735 | -58.74604 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a718911-666b-3c03-aa76-0908c19d337e | -6.02056 | -57.68034 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea9d2deb-2976-3276-a9d6-440cafc5953c | -8.3637 | -57.67814 | 2026-09-01 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28f5fdca-1258-3edc-8e18-3951c9431dab | -7.58681 | -60.4636 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 310fe456-d3e8-3b7f-9cf4-b25ce2d62dc9 | -6.38366 | -55.22161 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 431f823a-ee14-360a-bb70-5f0d0daa045e | -9.92473 | -60.49426 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29c556bb-f678-36ec-a23c-9c9702b478c6 | -8.27476 | -54.92767 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6842b41b-1618-37ea-9a69-a35073a6efde | -5.88063 | -57.78177 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fb6b4ce-64ad-33c4-9a39-9b82a07a93d5 | -9.15163 | -59.52987 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc166fd1-a4d6-3092-a6b6-4249773230bf | -7.19357 | -60.67595 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 749366ea-ce4d-39a0-9a00-26995107e096 | -7.35043 | -60.58969 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48e93db6-0115-3a0c-a427-5726ac5734c3 | -7.5264 | -61.38048 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9704cc65-a051-384d-a9da-18ed01801204 | -10.57225 | -57.48041 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f30e61b-0dae-3837-b1a5-3d401d7a9ee5 | -8.13682 | -54.97164 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61b24ca9-a964-3fcd-bc95-2c0a34900750 | -7.56783 | -60.47227 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bebe9c41-bc2b-3bc7-b5a2-010b52786b76 | -6.80373 | -59.4598 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a4e1735c-8f92-3401-bb0b-705d596c649a | -7.193 | -60.67967 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abbce6b9-3dd7-31f5-baeb-6c78c300e7e3 | -9.16926 | -59.61155 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1cdc343-29df-303c-a4b1-8437f2ef5f83 | -6.15688 | -52.63891 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dbde2e9-9031-316f-a663-ce5fbe0a119a | -9.09977 | -65.48455 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 378460c6-d23a-3516-8b56-4fbbadac6e01 | -8.04492 | -61.73762 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93b2675e-7145-3bf1-a052-795c4f7fb0e1 | -9.14166 | -61.09871 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da9e062d-48c5-3a61-864c-146375888d6d | -9.17291 | -59.6121 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe7d8271-ac96-36f6-903f-f50182fb839e | -7.57014 | -60.4571 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41a8f6b-ff48-314b-8f8b-4b329f56b1d9 | -7.62192 | -55.3009 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2ef8707-5a30-31b3-a825-c7034ccf553b | -7.35216 | -60.57845 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 8cf0818f-cb19-33eb-bc39-23c74fd8676c | -6.86853 | -59.03737 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b52dd44-b025-37b5-bf1a-e7f4bdd9b531 | -5.87364 | -57.77557 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0ed8ef3-06e6-39be-9fbd-f60c99854ffe | -6.38014 | -51.76387 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 080e7756-9d31-3f63-9e47-2d2ae32fd591 | -7.311 | -60.57217 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README78.md)
