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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eacad9c1-3290-33b7-aa33-2e0d532fc1b5 | -11.28771 | -47.67356 | 2026-09-18 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d016c9b6-9e1a-3a5d-8b96-4ff27a82b073 | -14.16685 | -48.74714 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 142336a5-aba3-35d8-84ae-6e562bd41e43 | -12.65619 | -54.72259 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f637594d-6cea-3f04-bd89-9bcfedef4211 | -8.5401 | -44.55294 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6d5c037-88e1-3c95-afc8-8df5c8babad4 | -10.94871 | -54.08908 | 2026-09-18 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 39de55ce-8b1f-3613-ba33-a44c12eb3a64 | -11.36128 | -43.95061 | 2026-09-18 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77557401-c71f-3f93-b288-0a7a7de09bf7 | -8.43253 | -45.78988 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a96b6405-4c4a-315d-94ee-2eac2346a9ab | -12.36695 | -50.68547 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8599bb75-c647-3b37-bafa-c7364c396763 | -12.65119 | -54.7217 | 2026-09-18 04:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 710c9f15-6f7b-3063-a420-561edef32926 | -8.44886 | -45.83942 | 2026-09-18 04:21:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a119907-4fbb-3842-bb29-f8e01bc2687d | -8.9085 | -45.00865 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ae358bf-657c-3903-b295-bbf0e604c37e | -8.90796 | -45.01214 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83009981-f3c5-372f-be8d-05d9b5f05a8a | -9.93743 | -46.53877 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c596f6ca-f5c6-3fad-8b86-34335c009d2f | -11.31232 | -46.77325 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d14363c5-dba0-3725-94c0-92cfcfe72e50 | -12.55319 | -50.72083 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3f1a4bf0-29ea-301a-966f-3038a68bbabd | -12.30487 | -50.73741 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a40b3a96-92bb-3a3c-9bac-7446a227b06a | -8.16941 | -54.81811 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7004cd56-8a8d-3b60-9470-3609d6553269 | -10.49276 | -46.29732 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4057896f-6e06-3128-b16a-ff601668c4ad | -8.77639 | -46.90544 | 2026-09-18 04:21:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4cce3e57-deea-3b1a-84f3-2a9cdd938a58 | -13.74709 | -48.7944 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acad7d1e-2981-374c-a9a9-01cec72bed13 | -9.71705 | -54.81717 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 20df5546-aaab-3672-9b68-49d6cf4a12c2 | -10.09398 | -48.18817 | 2026-09-18 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f27e4faf-212e-3a5a-9979-2ed154907f22 | -8.65127 | -43.86586 | 2026-09-18 04:21:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9a745c8-ae60-39cd-a143-456241c30e28 | -11.31733 | -46.76314 | 2026-09-18 04:21:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95ca900b-570a-38e7-867a-d95e6505626c | -9.71885 | -54.80734 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3723e718-a820-3c2c-9a33-c2b2f3887fb1 | -10.61266 | -46.55078 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca213eb4-a0f0-3b56-874c-1f0d4da86285 | -11.3882 | -47.29633 | 2026-09-18 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b47fc2af-81eb-386d-bf79-f8bf6a6eccdb | -10.32153 | -45.32516 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb9187bd-41aa-3091-abe2-c98278dcf284 | -13.64165 | -46.93177 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14a8ef71-ccf9-351a-963e-7a66ec69c966 | -8.46085 | -44.49407 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9fabcd7-2a6c-3624-8e50-4335e6fff889 | -8.57994 | -44.55931 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ad84829-c6a5-3df5-9df0-8047c3d29b9b | -9.75054 | -46.57796 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2fddea2-7adc-31fe-92b2-9e9f9292dcab | -9.68094 | -47.89638 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 457fcc15-99d7-3723-b0c7-d6f89dc0b137 | -13.42635 | -51.89891 | 2026-09-18 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75d0405f-4b85-3b34-87ef-3cdfc236dd59 | -13.64826 | -46.93285 | 2026-09-18 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf1f8dbf-bc36-33de-872a-392b08f6a2ac | -8.9296 | -51.46298 | 2026-09-18 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77dd75b8-04cf-3bce-819c-763f510bc77c | -9.94519 | -45.34065 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11775934-afe2-3a86-823f-66ee47001336 | -8.16269 | -54.8242 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d48337d7-992f-35ac-9439-915ef3a80728 | -12.5523 | -50.71291 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c2fdd4d-5fa6-368b-9250-5cd2b8178648 | -13.74451 | -48.7947 | 2026-09-18 04:21:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb4415b9-2769-3b5a-ba70-3edfd3487ffd | -9.95511 | -45.34221 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09080820-f57e-32a0-9d57-d66b7c03ddc0 | -10.11855 | -46.29789 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e56afcd0-eacc-367a-83bc-c09ec0ab5e76 | -12.17424 | -46.98065 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8e6ec56-a933-37ff-adfc-db370e0edf7d | -12.38554 | -48.14159 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfedbf45-d96a-3a98-9a2a-064bf33b98af | -9.54182 | -45.46206 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4725fba-109e-3992-96e5-2a7eb32a2cd2 | -9.72813 | -47.75884 | 2026-09-18 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2d85cd3-5994-3fa4-b7c1-26a5d440ac8d | -14.16622 | -48.751 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2770210-8d9e-3307-9b75-5164133b882b | -12.16816 | -46.97602 | 2026-09-18 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aa2764a2-b094-3707-b31a-1327ec1b1ef5 | -10.53797 | -44.84664 | 2026-09-18 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69f93019-53f7-33d2-8e06-182de0cded9d | -13.62038 | -48.30782 | 2026-09-18 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b96336d8-9979-3b5b-a25f-09d5b9015232 | -13.26409 | -46.909 | 2026-09-18 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e179f9f7-94e1-3134-bfaa-d480e15a6ce5 | -9.55947 | -45.47904 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6339221b-7311-305f-8af5-228a78fda621 | -12.39504 | -48.46809 | 2026-09-18 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8de3fac2-dbaa-363e-80ec-e165b8c6680f | -14.17437 | -47.85886 | 2026-09-18 04:21:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22f91c8e-69c8-37b2-a7d3-47d027368da9 | -14.22593 | -48.51385 | 2026-09-18 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ad3dbd34-ccb0-332d-bd69-5ce52fce4e0f | -10.66045 | -50.25689 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 48868cae-a8a0-394c-908d-b562aba255a9 | -12.31767 | -50.82998 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99e348d9-d5a9-3995-b79c-2130c7db53a5 | -9.83591 | -49.23032 | 2026-09-18 04:21:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b4078aa-aa6a-37ee-be07-a8fe9fb10ade | -11.00002 | -57.05756 | 2026-09-18 04:21:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2288a31-4c77-36ca-ba97-b76fe1b0cd45 | -11.29292 | -43.35087 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c99e00b-0010-3994-8edc-6c9ecdc08570 | -10.9454 | -53.05789 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7397909-8be1-3dc7-ac5f-bf9ef89822ea | -11.32726 | -43.39139 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 164f1541-a57c-31aa-b3bb-aa5c44043c56 | -9.95012 | -45.33071 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a25d0d38-8ff5-3498-a931-db47bb6596ff | -12.43722 | -50.68007 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42767cec-c9d7-3f34-8422-3f9788ecd0bf | -12.26508 | -47.13797 | 2026-09-18 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5ac3150-359f-3673-b084-66fc6a9ffed4 | -9.94281 | -46.61252 | 2026-09-18 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc6aedb9-f545-31db-819d-0ca6b3b6de67 | -10.49332 | -46.29381 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8424072f-5f1a-32ec-9f34-3f2b139b6f0f | -10.59883 | -46.55211 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5e128d7-b0d5-336f-b44b-a7a373e4d411 | -12.28815 | -50.76511 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 051f676f-cec4-3771-8b53-fd4b2b4ab060 | -10.33139 | -45.3052 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b85c598-8748-379e-a9ac-8a549210844c | -11.52649 | -46.88143 | 2026-09-18 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d34bd54-8188-3932-9055-132f472d5a20 | -9.08923 | -45.72396 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ee4a7a5-c99d-33fe-a264-19257905a701 | -9.84381 | -48.38566 | 2026-09-18 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c20abd39-b8a9-3698-a5a3-8bf9feb62077 | -12.37483 | -47.00314 | 2026-09-18 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1d659bb-edfc-3feb-a89b-1a401f99b49d | -12.27308 | -50.78298 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 956a9941-114e-33d9-8927-fd34dabac0c7 | -9.18596 | -45.69356 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe9381f7-129d-3d76-85fa-ca49d13b48de | -8.53467 | -44.54488 | 2026-09-18 04:21:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2347d6c5-b1cb-3e44-9aa1-cb1a8ec8ccb3 | -9.71827 | -54.81052 | 2026-09-18 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 50e47aa4-5a56-3811-8ba2-d75ac07ebdd3 | -9.60365 | -45.3257 | 2026-09-18 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c93b4e5-89e3-3926-bef7-86c7ad0d3732 | -11.681 | -54.43699 | 2026-09-18 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de510c7f-a3db-3bfd-9e04-a9c9b6356d20 | -13.23586 | -42.33227 | 2026-09-18 04:21:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 6c45fa11-d98e-3174-bd61-b27ffea68e2f | -10.65326 | -50.4925 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08593944-f2eb-350b-a1df-62021686d9bf | -10.50986 | -46.27495 | 2026-09-18 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d4db8fa-c453-3f0c-8c37-09cd5d2fc9dc | -8.51169 | -48.49489 | 2026-09-18 04:21:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e44adb8c-6aeb-3297-9d4b-355e2d1cd742 | -11.88363 | -47.57951 | 2026-09-18 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f52808a9-205c-330b-b313-7d11423a8585 | -9.38488 | -55.96909 | 2026-09-18 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebda801a-dd4a-3e7e-9470-8eb381bae2cb | -10.81279 | -50.19909 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5976df4d-b30f-392e-a222-33f4615b6836 | -9.95986 | -45.46436 | 2026-09-18 04:21:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc0aa90d-8c42-34db-a146-ee29478569a3 | -8.15792 | -54.81961 | 2026-09-18 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58985f31-5a71-342b-bca7-8be69e3514aa | -9.25048 | -45.88932 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0cc48acd-4dec-3a35-857c-7157f8985e0a | -11.28062 | -43.36127 | 2026-09-18 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f359f03-e681-336a-a7ea-78751cb579d6 | -9.39555 | -46.86119 | 2026-09-18 04:21:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 921c1870-6c01-3e8e-a9eb-69113bfdbbd9 | -8.91127 | -45.01265 | 2026-09-18 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 679b6998-68be-3ec8-9dc2-0e175d68ad49 | -10.31599 | -45.31712 | 2026-09-18 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5ff9526-abbb-33e1-83e7-8dab07daeab8 | -12.31367 | -47.95685 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2e463add-2e2d-3eac-a2f9-0352cf928df2 | -10.66454 | -50.47376 | 2026-09-18 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 21cd6546-9722-3a9c-81ef-17853c7f4829 | -12.31586 | -47.96486 | 2026-09-18 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85d5984f-3a1c-3a90-8ff7-2495c7c8b067 | -12.4358 | -50.67746 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c86a471-aed7-3d8c-a416-352248ea6455 | -8.55917 | -45.52564 | 2026-09-18 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6ef858d-c5bf-30d3-aee3-659ce139a433 | -12.55569 | -50.73879 | 2026-09-18 04:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README44.md)
