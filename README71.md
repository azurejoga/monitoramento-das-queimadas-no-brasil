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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ac9a177-612e-37f8-a573-cc74ee402ec5 | -10.88988 | -46.63329 | 2026-08-28 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4599728e-c765-3f72-b37b-d603f9cdbdd9 | -4.79179 | -43.14229 | 2026-08-28 11:51:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 86b61267-26d7-3baa-8942-413e91f0bd48 | -9.98431 | -48.59111 | 2026-08-28 11:51:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| d030bcb3-dd20-3929-80ec-6a094c950623 | -8.11493 | -45.4715 | 2026-08-28 11:51:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 408421b1-dc6c-3653-bc37-cb5920fbde2b | -5.25894 | -50.95873 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dccb3496-bd98-3b0b-8823-4cde80b3b403 | -11.14352 | -45.57432 | 2026-08-28 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 32b910fe-b508-300b-ae6e-f53e86b30ae7 | -10.55224 | -50.41585 | 2026-08-28 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dc8ac5a9-ee5a-3d62-b628-de28c4a19e90 | -5.89387 | -52.11715 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| abe81ba7-00f1-36f4-95ed-f389b3b861e0 | -8.94873 | -45.726 | 2026-08-28 11:51:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d043d1c3-b358-33a2-b38b-03f95977e15a | -11.23765 | -45.04954 | 2026-08-28 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| ca118224-8eac-3a74-858d-445ac4137ae5 | -8.06522 | -45.83552 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 78401bba-8f3a-3428-91d5-59de5cc9d51d | -4.02128 | -46.95574 | 2026-08-28 11:51:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 608265cf-47b8-3488-a956-f5ff8e2c7bb9 | -8.0292 | -44.15696 | 2026-08-28 11:51:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 351f5ff2-2d2d-31d6-9d20-ab4047bd49c2 | -6.82801 | -45.53926 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 56ac66fa-d27e-39f7-bc18-e1272f820be3 | -5.25735 | -50.96942 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| be992919-8e77-3d7f-b5ad-8f693463d6b2 | -6.82647 | -45.55034 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d2aaf6b0-b0f2-32f3-a70f-2c007165f717 | -6.51641 | -47.43507 | 2026-08-28 11:51:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 583a50ef-a986-351a-9799-b9318d91db31 | -5.3392 | -45.14919 | 2026-08-28 11:51:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d97f7218-e132-3015-88cb-c4b5afaef0cd | -10.90103 | -46.62377 | 2026-08-28 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 324c60c6-cf56-3e21-bdd1-f84d3f922647 | -10.90925 | -46.63599 | 2026-08-28 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 0a26a73d-fb85-3714-b34e-7b16d7fd2c2e | -10.07498 | -48.66532 | 2026-08-28 11:51:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5d181eed-5151-363f-b9f6-ef8a718eb484 | -7.26681 | -45.8577 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| c0f7c895-e99a-3395-8bdf-d7d5f3a49a48 | -11.24854 | -45.051 | 2026-08-28 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e5491c8a-0a18-3ad6-a294-0bede0294736 | -8.94327 | -45.68996 | 2026-08-28 11:51:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0d888462-713f-3437-86d6-da48f78309f9 | -9.34482 | -48.16363 | 2026-08-28 11:51:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a8fa1700-b526-360c-8cda-c31427158f81 | -10.07625 | -48.65633 | 2026-08-28 11:51:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ed68f2c6-3ee5-3b81-b8ea-67628b4e7064 | -10.5518 | -50.48177 | 2026-08-28 11:51:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 95571940-937b-3576-9db2-c1aac86ee2cc | -11.07161 | -47.11689 | 2026-08-28 11:51:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aaae53e0-a4e0-39ad-a8a7-ff0b4690bb45 | -7.26306 | -44.21756 | 2026-08-28 11:51:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 87159262-9540-33e1-abe2-389f2cd16074 | -9.21934 | -51.55434 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 520984ba-d8b3-3cd6-9849-3c7fe00e1ca4 | -7.26843 | -49.84705 | 2026-08-28 11:51:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b42ce626-87f6-3479-a5dc-3b7f4b4aded5 | -10.63949 | -45.22028 | 2026-08-28 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| a4d70d69-2715-30eb-abc5-778b83d8a21f | -4.61029 | -43.21397 | 2026-08-28 11:51:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| eec82241-a820-333f-b7d9-ed4b75928912 | -8.06221 | -45.85755 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 8c81cffd-b6f5-38bc-898b-30ac688b12e7 | -3.79532 | -47.64315 | 2026-08-28 11:51:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e5878e36-b442-3bed-bc7b-bfd126ee2b81 | -7.27322 | -45.35076 | 2026-08-28 11:51:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6c960b76-735c-3e91-a280-e1e6db77a8f6 | -8.95561 | -50.17093 | 2026-08-28 11:51:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ac7d7a7-e396-39b0-bef5-dbf1816db2bf | -5.89585 | -52.10427 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fdf11039-5b8c-3388-ab70-ce156d655a95 | -8.26082 | -46.35065 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2e7c0c6a-8887-30cc-8e64-2df9f5a28607 | -8.04109 | -45.86596 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dd897e71-099d-3fef-8c77-692027118c98 | -4.85517 | -45.39942 | 2026-08-28 11:51:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 259139a8-8973-39a0-84fc-a7aeec347794 | -10.91073 | -46.62508 | 2026-08-28 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 77e5b49d-2bbe-3d8a-ae6e-0c917394b966 | -7.25709 | -45.85645 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| cbd2dbc8-a005-3f7d-8cd2-215ce1ba6ca9 | -5.16601 | -42.75549 | 2026-08-28 11:51:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 538b8763-203e-3793-beca-bb586e485800 | -5.8978 | -52.11132 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| f3190a53-c276-3194-b736-03bab21af531 | -10.89957 | -46.63465 | 2026-08-28 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| f0dea098-01e9-34ae-85f7-259e44dd1fb6 | -8.17496 | -46.16225 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1cf26cf8-116e-3ee9-ba6a-24957ea45615 | -7.26535 | -45.86854 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b21c22bf-6c46-31c9-8634-c5dd20218717 | -6.75988 | -46.13491 | 2026-08-28 11:51:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4b5d63c3-1d7b-309f-a1d9-1950a4c7646b | -3.79407 | -47.65195 | 2026-08-28 11:51:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ad545143-e328-39da-a194-0a5cc5248e29 | -3.53454 | -48.17657 | 2026-08-28 11:51:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4c8702e-2b81-39bb-a7f8-1d1012164fab | -8.06069 | -45.8686 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2835be3d-80cb-37d6-97e7-af33ff19470b | -7.25565 | -45.86728 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4d9c3557-d8ec-36b2-98cb-ffff7b85612c | -8.17352 | -46.17285 | 2026-08-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c6ded045-adbd-3e4d-8b5b-99536eb115e1 | -4.84549 | -45.39812 | 2026-08-28 11:51:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 971d2e3c-ccb2-3988-b4d1-4e3ca7f81e6c | -6.03068 | -46.75533 | 2026-08-28 11:51:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| de4a2b84-6f0a-35fc-9101-0209826cbdab | -5.1683 | -42.7386 | 2026-08-28 11:51:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70627a17-7734-33ea-8409-fc6148a7dbdb | -11.14921 | -45.58162 | 2026-08-28 11:51:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4dd42b48-bcec-310e-8e33-5ec46054bdb6 | -7.25351 | -45.86058 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| c1e0208b-8ecb-326e-8337-339abe36a527 | -4.66693 | -43.22146 | 2026-08-28 11:51:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1969db5a-3b53-30aa-9a56-cf2fe8aa63c5 | -4.65561 | -43.21992 | 2026-08-28 11:51:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e4b8c23d-61a5-31d3-91c8-e5073a3eb4a1 | -9.43143 | -51.69567 | 2026-08-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3c292853-40fa-3826-87e1-743654d28daf | -14.15916 | -52.83453 | 2026-08-28 11:53:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60bed00e-0ad9-3154-bc5f-a268cd7278d0 | -16.20617 | -50.33786 | 2026-08-28 11:53:00 | TERRA_M-M | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 45406f8f-5a61-3ed0-a712-bf86e759114d | -13.32698 | -48.19768 | 2026-08-28 11:53:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6f183f1c-12a4-3a49-9b2e-303a328edd2e | -16.67428 | -50.15719 | 2026-08-28 11:53:00 | TERRA_M-M | TURVÂNIA | GOIÁS | Brasil | 5221502 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c941c45c-a810-34f3-bb7a-eaca6d9ca4c7 | -11.21533 | -51.23545 | 2026-08-28 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d483d564-3583-3049-ac64-1871e0c39416 | -14.79414 | -42.842 | 2026-08-28 11:53:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| e4618e13-73db-3b7e-9aab-90b4bf5201ae | -12.02151 | -47.17934 | 2026-08-28 11:53:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 564e2369-92ad-32b6-bab3-666d662a0177 | -16.05819 | -48.25927 | 2026-08-28 11:53:00 | TERRA_M-M | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 24873197-a736-3b11-a1bd-f8876be38d7b | -14.80849 | -48.806 | 2026-08-28 11:53:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6bfaf661-250c-3fa3-84d4-399421494149 | -10.75573 | -54.04148 | 2026-08-28 11:53:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 1a0acc76-484d-37b8-a263-d7a82fe2df69 | -10.89821 | -50.51036 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| c98c2fca-570e-3835-b487-340fc384f107 | -13.34411 | -46.91205 | 2026-08-28 11:53:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 31cfb893-cc15-305d-9d2f-7f29775c9369 | -10.90852 | -50.50245 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5c5defa4-6ec8-3ef9-8529-22d4a9a25e29 | -12.28319 | -50.56387 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 485b6275-2601-36e4-8d65-29184203217d | -12.19691 | -52.86198 | 2026-08-28 11:53:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7f203025-004c-3464-9429-54a70bb34d60 | -12.29211 | -50.56519 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 5876997d-9bcf-3f4a-bd0f-a2eed2f7c06b | -14.4342 | -52.59147 | 2026-08-28 11:53:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1716f174-f3e6-32ec-9881-58ba5f661ca7 | -14.42474 | -52.58994 | 2026-08-28 11:53:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a51fc03-62a6-3951-8cb6-b5630da286ce | -10.77954 | -50.62851 | 2026-08-28 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| bed1d713-9408-3724-bbf3-8f88df570397 | -17.25142 | -48.11191 | 2026-08-28 11:53:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ca9213f-60ca-3bc1-ab4a-325798b30414 | -13.43254 | -54.02158 | 2026-08-28 11:53:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 8aa11911-42f0-3bb7-9aba-5b44a1604336 | -16.40562 | -43.06172 | 2026-08-28 11:53:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 26.1 |
| bdecdd70-b4bf-3019-ba2e-75a11ab56875 | -12.2957 | -50.60318 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 87ae03bd-b4db-3d0d-a241-c1586abd3e76 | -11.34099 | -48.38136 | 2026-08-28 11:53:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8ebb821a-53b3-3969-b46f-d844e28d8a29 | -14.60018 | -47.97549 | 2026-08-28 11:53:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 20404b56-2b6a-3527-afd6-ecbf9c8353ab | -16.41054 | -48.86963 | 2026-08-28 11:53:00 | TERRA_M-M | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90f7f387-fe5c-3fc3-b8a9-5d1132dee0d7 | -11.33201 | -48.38012 | 2026-08-28 11:53:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fe63f46c-6acd-3e97-8b39-c23f2bca8822 | -10.90718 | -50.51168 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 739bc45c-a3a7-3a7d-a0fd-8f167898342e | -15.31522 | -52.74033 | 2026-08-28 11:53:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 99ed73ff-6e7f-3ab0-b369-da7784563ae5 | -10.88924 | -50.50905 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 81c9e6b5-569d-3393-aa2d-a7ab612e1654 | -13.33428 | -46.91072 | 2026-08-28 11:53:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| b5d77c9f-ac93-399a-9a67-b451762414c4 | -10.77053 | -50.62718 | 2026-08-28 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b774dcb9-a96d-30c4-9f60-271a4a2d18a6 | -12.19515 | -52.87346 | 2026-08-28 11:53:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 07c45349-9b98-34e1-8aa4-aab920faa7a9 | -13.41441 | -51.40292 | 2026-08-28 11:53:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| a11cea64-ce16-3f15-a171-1dd40ad02991 | -12.87626 | -44.36878 | 2026-08-28 11:53:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 9ded1077-e025-3269-b5cb-11edb6c37104 | -10.93524 | -50.51247 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3ebc12aa-045d-312e-a848-e7b43ba392c6 | -14.86479 | -52.6052 | 2026-08-28 11:53:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b3192bbe-49b1-30bf-9309-46c189930568 | -13.82485 | -42.16584 | 2026-08-28 11:53:00 | TERRA_M-M | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |


[Clique aqui para ver as próximas entradas](README72.md)
