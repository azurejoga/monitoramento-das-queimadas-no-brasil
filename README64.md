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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cbf7e09-e6b7-3f70-99f8-b210a223a8fe | -13.69491 | -50.92443 | 2024-09-30 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d5116f1-5726-399a-832b-cf35e573344b | -16.11637 | -50.36879 | 2024-09-30 05:25:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7730aeab-20ff-3c6b-b30f-0f70e2c1149d | -16.11038 | -50.36368 | 2024-09-30 05:25:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3ef196ee-fd68-38cb-b3c8-2e2d85b52900 | -16.10497 | -50.3526 | 2024-09-30 05:25:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 17587073-1abc-3c96-821c-13a77b09ee88 | -16.10438 | -50.35852 | 2024-09-30 05:25:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff22e920-1e3a-372e-a5c6-d94a278215d0 | -16.08396 | -50.36738 | 2024-09-30 05:25:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3cde283c-ca13-3fba-b920-dfa727b61006 | -16.08347 | -50.37232 | 2024-09-30 05:25:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f2c9f484-e463-3f07-af18-5c075e86acde | -16.08294 | -50.37765 | 2024-09-30 05:25:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1505089d-d07c-381a-84a0-f4f0503d7026 | -16.08242 | -50.38301 | 2024-09-30 05:25:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0bd03bff-e14b-3e94-8923-a521bee80be3 | -16.08189 | -50.38833 | 2024-09-30 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| af44bbd6-8ae1-3c9a-926c-9ad9fe1fe07b | -16.07746 | -50.36724 | 2024-09-30 05:25:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 446bfc82-b57f-3494-aa96-1847c31414f5 | -16.07651 | -50.37696 | 2024-09-30 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f2e7a6e6-623d-3d89-9449-786beb8491b1 | -16.07602 | -50.38189 | 2024-09-30 05:25:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 01b532fe-aa9c-3f9e-b9ee-32d3629341ac | -16.67545 | -51.72099 | 2024-09-30 05:25:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7095e6da-597c-34d7-8b77-118f8e3f7f91 | -16.67501 | -51.72531 | 2024-09-30 05:25:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95c32c1e-4588-33d2-8dd1-9ef4aa662c52 | -5.72157 | -51.07309 | 2024-09-30 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5e2a6e3-cc86-3019-95d8-b09498cc702c | -5.72115 | -51.07603 | 2024-09-30 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d05add0a-af34-3d86-b50b-8512df0ea5b6 | -6.31819 | -50.00197 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e1e07a9-cbf6-3b38-a1ea-6c9c77e143b6 | -6.31795 | -50.00251 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f879fd4c-bd4d-3954-a249-3fba5e52b2b7 | -6.3121 | -50.00295 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11ae1d8a-b9c5-3eec-b853-b1435a4705d2 | -6.31186 | -50.00356 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5a45232-772e-33e9-a7c8-ef80521784bc | -6.31156 | -50.00677 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40206f72-3ad6-3f11-b596-d88fc5cec6ba | -6.31134 | -50.00743 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c2db515-ebb9-3688-9d26-cea3b91b4ddd | -6.311 | -50.01084 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df411494-e9c2-3bc7-8581-068c924ec6a4 | -6.3108 | -50.01153 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8adc008b-142d-3886-bde5-073c7700d9fe | -6.30559 | -50.00603 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13a3f6a5-3961-3bbf-9e96-752cd54b0d01 | -6.30523 | -50.00954 | 2024-09-30 05:25:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f1f5373b-ae4f-30b4-8db9-93f447328252 | -13.20706 | -51.22615 | 2024-09-30 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a5fcc8c-7854-386a-a9d4-62515b46ce21 | -13.21296 | -51.22694 | 2024-09-30 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac9cde37-24f3-37a2-a3d3-933eeaf5d67d | -13.20857 | -51.22605 | 2024-09-30 05:25:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1278ed0f-e3fb-3e9b-a498-607e8338ca3c | -17.72962 | -53.19524 | 2024-09-30 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 943674f3-a0d3-3e2d-afd9-d4462fd28e3d | -17.72016 | -53.17939 | 2024-09-30 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 168b6794-c0ed-3501-9055-83ae988cfff1 | -17.64989 | -53.1539 | 2024-09-30 05:25:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c0ede9b-b2f9-37c6-a2e8-eec97fba26e1 | -17.64501 | -53.15062 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1badd679-c7a4-3115-9451-e738e140a0e7 | -17.64463 | -53.15436 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf92b95-97d1-399b-b82b-ea47019c4b2b | -17.64439 | -53.15317 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b26f48be-9ef0-35e5-a50a-c16963ad352d | -17.64398 | -53.15695 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55a309bf-7c8d-372d-9487-eb29015fcdd0 | -17.64357 | -53.16073 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| de8b3aa3-7cd7-3ae6-9209-9756aef55bae | -17.63804 | -53.16023 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa5b07e9-f471-30ff-a046-d91788025236 | -17.63765 | -53.16391 | 2024-09-30 05:25:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 459f5ac1-df2b-3412-8a91-2c8565ed94e0 | -17.12083 | -53.27812 | 2024-09-30 05:25:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63a55f8e-1a11-3869-b856-2926ac1f4d78 | -17.11709 | -53.27772 | 2024-09-30 05:25:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bd815f8-533c-38be-8aee-fc8499b7b1c0 | -17.11541 | -53.27744 | 2024-09-30 05:25:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47643fb5-fb65-331c-83de-ad69b4f8414f | -18.65313 | -52.47467 | 2024-09-30 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24fe533e-e42e-35d9-9ebb-c2f5f2f03a19 | -18.65272 | -52.47878 | 2024-09-30 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14475b82-bdc5-3278-b8fa-74f41b6e9e57 | -18.64687 | -52.47836 | 2024-09-30 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 216a3ade-34c0-3dd9-9c80-88573b220fcc | -12.66784 | -53.20666 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ede06400-5067-3fc1-b1b0-1298acbb316d | -12.66747 | -53.20975 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c83bc5eb-eebd-3dd5-83fd-db75725920e7 | -12.51917 | -53.14484 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69b855ed-a7b3-3ad8-927d-482effeeefc3 | -12.51878 | -53.14799 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83d055f0-a5dc-337d-8455-3eced80be5f3 | -12.51838 | -53.15113 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1149eb0e-d0dc-330a-a2cc-5458e2a2be79 | -12.51363 | -53.14724 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5026488-fedb-30b8-abfc-520f02bd887b | -12.51323 | -53.15039 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053e3e93-c03c-35fd-ae0b-36578b2359d7 | -12.51284 | -53.15353 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e288574a-a945-38cf-94db-ab722e9a01bb | -12.51244 | -53.15666 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3a68285-8dbb-3814-9c93-12e0207e1f88 | -12.51205 | -53.15979 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67e51f27-f26f-3053-8275-b408d9fd7be4 | -12.5069 | -53.15908 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b7876d5-c020-3c4f-84ea-1504b3009642 | -12.50612 | -53.16531 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 943bf7ca-6a2c-3bbe-b436-6768d916358f | -12.49428 | -53.17628 | 2024-09-30 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b1395c3-f1c1-33bf-b81e-b911b4525289 | -16.43919 | -53.93015 | 2024-09-30 05:25:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25554b27-f94f-399c-b49c-9cf6aee7abfe | -16.43885 | -53.93313 | 2024-09-30 05:25:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4c7f629-cafd-3ca7-b318-abe785ed7290 | -16.43371 | -53.93233 | 2024-09-30 05:25:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edf2f5ac-8480-3cfb-b5df-74ccaf18bcaa | -16.08983 | -53.52746 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b44f988-c4f9-3e7c-ac67-76726967af08 | -16.08489 | -53.52386 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14c0b26c-9e04-32d4-8891-a4635a97068f | -16.08452 | -53.52709 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cbe4aac5-34e5-3b52-8e89-8808a7f77129 | -16.08311 | -53.53948 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 018fc66b-4da8-32a3-ab2e-fc920970a27b | -16.07922 | -53.52671 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4010209-47dd-3e1e-8b93-29fa150953a7 | -16.07886 | -53.52982 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1d8aec0-5c57-33ca-8ad2-638a8337e226 | -16.07852 | -53.53285 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59e2ee64-4388-31ef-8f6c-e7067b72036a | -16.07818 | -53.53584 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10479950-b6ba-33dd-9c29-97d09745912c | -16.07401 | -53.52539 | 2024-09-30 05:25:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1b4d652-b663-37c8-bca1-38f56c3c6814 | -15.24085 | -53.77564 | 2024-09-30 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22006bb0-7094-3ea4-8920-7c800faeb4ce | -15.23807 | -53.77605 | 2024-09-30 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34f579b4-1fe9-3189-a0ec-c95c5112922f | -15.23571 | -53.77501 | 2024-09-30 05:25:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa782fb3-9142-3b97-9967-0e63ed906323 | -18.84983 | -54.50738 | 2024-09-30 05:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 244664dc-6bbf-37b6-a9e6-1f56e0632554 | -18.84916 | -54.51356 | 2024-09-30 05:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f097388b-95f2-3903-ae24-3629aa4335e0 | -18.84882 | -54.5167 | 2024-09-30 05:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc6f4f83-62dd-33b9-81fa-92366edb4747 | -18.84534 | -54.50094 | 2024-09-30 05:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23e75502-97eb-34d6-afd1-c7ea97a882be | -18.84501 | -54.50391 | 2024-09-30 05:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04027d5a-ddae-3550-959b-75aadf9a06ea | -18.8437 | -54.51606 | 2024-09-30 05:25:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8ae36c7-3cb8-3de5-8c98-30848a2194ed | -11.78115 | -55.12732 | 2024-09-30 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7159077f-525e-3476-9b22-ddbc68b59293 | -11.78056 | -55.13182 | 2024-09-30 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 563ac2c4-1a75-32c3-b73d-9b2c312061f6 | -12.68568 | -54.67335 | 2024-09-30 05:25:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01897f00-8c97-3451-bd75-ea8a5ce721b5 | -16.65365 | -55.22747 | 2024-09-30 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c1e04690-ca34-3879-8df2-06a7fc3d7ade | -16.65018 | -55.21631 | 2024-09-30 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| ac943a68-f287-3c6b-8ba2-62cc615f331b | -16.64891 | -55.22685 | 2024-09-30 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 08890096-83bb-3e89-b6f9-a0a6b8d381bb | -16.64827 | -55.23211 | 2024-09-30 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d0afa8ab-d036-3417-aa56-53568debfbdd | -16.5976 | -55.95836 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 09121d3b-af0c-3a3e-a758-84e244c77539 | -16.59703 | -55.96307 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1ca8126d-ddea-3bed-a5fe-3e2f5d588c8c | -16.59647 | -55.96776 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 37ac15c2-2d4a-34c8-923f-fe7757481d42 | -16.59535 | -55.97714 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bbf29712-ec98-3a0b-92d8-ca677cbb7844 | -16.59487 | -55.96589 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 35ed95f5-e8c9-361d-8a47-a5ba9d2406ea | -16.59479 | -55.98181 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bcd08673-38de-37b8-8d9e-67ad8f108664 | -16.59308 | -55.9799 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3bb02bed-bf45-3bca-8cb6-fbdce07ccd76 | -16.59249 | -55.98457 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 57320ef6-9ba4-327b-be7b-a6969c5d1d38 | -16.58973 | -55.98585 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dba3e2ed-c042-322e-9323-cb262330a099 | -15.90024 | -55.40121 | 2024-09-30 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 577d3811-0daf-39f6-a008-1b963eb3afd9 | -17.13015 | -56.18329 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| dcce0295-d249-3c73-8e48-8de05f08322a | -17.12623 | -56.17802 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 722295b2-751e-3475-9e7a-c93297970087 | -17.12567 | -56.18268 | 2024-09-30 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |


[Clique aqui para ver as próximas entradas](README65.md)
