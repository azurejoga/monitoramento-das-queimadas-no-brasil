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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca297646-cfe5-3c6d-b300-7ff8d55ba9d7 | -8.46932 | -49.61868 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8208315-0c68-3804-a17e-c519acb10004 | -7.48088 | -47.51315 | 2025-07-12 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3d3a7f7-c5dd-3bdf-83f3-a5d0648b481e | -10.67304 | -49.49954 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8230114b-263a-39a2-bb7a-133c02f366ab | -9.01857 | -61.22943 | 2025-07-12 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8d82d22-65e6-3b46-a006-cd6fd6a161fb | -7.22989 | -44.01445 | 2025-07-12 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c05e522-4bb6-3437-a83c-a2af0640eeaf | -13.01811 | -47.82649 | 2025-07-12 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ac5cd57-82e9-32f5-9e47-b36e581bb023 | -9.02453 | -61.23049 | 2025-07-12 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95da1687-546b-36a7-a2e8-a78d8b7c9a15 | -6.70862 | -44.3286 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7cdeedde-9815-3200-8804-bb33f4d5d12d | -7.23169 | -43.10423 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2ea8e7e7-4ad9-35c2-974b-4d40f579aca7 | -8.91603 | -47.34961 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c6d7cfd-0586-366e-a69b-2e48c2777aac | -7.60996 | -49.93734 | 2025-07-12 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3b2fa0f-3b46-3bf0-a5b1-eaa5fb3302e3 | -12.41385 | -45.3582 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f957972-a2b5-3d97-8997-79a9a533fbeb | -10.69833 | -48.306 | 2025-07-12 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8f9fed7-b4e1-3935-bab0-c1bcc825a129 | -9.80309 | -48.57093 | 2025-07-12 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6e7e77a-37ae-38c1-b1bd-17efd507bc41 | -4.66123 | -55.9679 | 2025-07-12 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c477864-95a3-3aa1-a684-c63015c05fa7 | -9.91869 | -47.83095 | 2025-07-12 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cabbf6c5-85ea-34d2-8d9b-54f8a7f88a2d | -12.41854 | -45.35491 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 276e488b-dabe-3cfb-8d32-676baa94cc51 | -8.30889 | -55.1083 | 2025-07-12 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| feb43a01-a4a7-36e7-8355-e1e341bb90aa | -7.86658 | -56.62315 | 2025-07-12 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb7e0af0-440d-3684-b34e-2e23f3592844 | -11.43032 | -46.39434 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b60d79b3-565a-36e4-9897-05836fdc55a4 | -11.93312 | -51.69095 | 2025-07-12 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3f8bf03-3c05-3dea-85f9-bbb469088ec7 | -13.00689 | -46.27726 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eda3754e-b5f6-3859-916f-701ad40d90a3 | -13.16356 | -47.29638 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1656decc-178d-3b4b-aa60-120922774c3e | -13.15482 | -47.30451 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 26b79e0b-80d2-300a-bc90-c9e7a8ca2f9e | -7.67784 | -45.9763 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad80c40a-d664-3037-88e6-37214f30401a | -12.98345 | -46.33105 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f599371-f11f-34e1-ae14-f0fa00b42101 | -10.68798 | -48.30418 | 2025-07-12 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04074360-6c9f-3ffc-a63c-23fd7371d5a0 | -11.42766 | -46.3971 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 275c002e-5710-3d19-a283-e291c1d0e3fe | -7.18785 | -42.99046 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3a13f5ac-c77e-313b-b4ae-3d9ad959c713 | -7.09764 | -44.06074 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa314c4d-e75a-3732-8500-e6aeb7830dbe | -10.84389 | -49.11199 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eb1d0497-ebe8-3b44-ae74-0f27da167f9f | -13.16049 | -47.26348 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12e03e1a-9858-3c1c-b81a-9a4c57f338ed | -7.0971 | -44.06443 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5890e8e4-524e-347f-b9f3-873f596cdad4 | -13.15859 | -47.30467 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c56a3da7-bd21-3584-a9e0-7a12a50861b9 | -7.98993 | -46.41563 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c886428-3d25-37d6-b1d0-38b5f27db52a | -10.57362 | -49.13035 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2856a53b-9c23-3829-b99a-bca061a3fe9c | -7.95024 | -49.65435 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f32998b9-b9a5-3010-89b7-832a749acc76 | -11.46412 | -45.10954 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 824c880f-be69-370b-af07-58c057402a80 | -9.02536 | -61.2261 | 2025-07-12 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5d56b5a-9f7d-3ff1-87a7-5d17657c2597 | -10.6943 | -48.30923 | 2025-07-12 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 612ecd8f-15a0-36a0-b208-4f6994294cc4 | -8.23109 | -47.55558 | 2025-07-12 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb795d80-e4fc-33f0-b8b1-1a3f62ad3206 | -13.14853 | -47.31087 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 687cbf1d-e351-3e69-bf50-ff6a2e65b7d5 | -11.73196 | -47.46919 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f91608f4-b5c7-3516-ba1a-a6b26b59d674 | -9.27331 | -46.61232 | 2025-07-12 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a7af112-647d-3692-a96e-f1f9fcb360a7 | -11.78146 | -45.21705 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c275db0f-ffac-32b7-8caa-bd933fb4301f | -7.18976 | -42.97675 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0739f24a-6da0-3ec4-b299-2189886e78c1 | -10.21751 | -55.44684 | 2025-07-12 04:40:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc368476-097d-3fa7-bfbc-1af25cb4c960 | -11.74025 | -48.52919 | 2025-07-12 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e497d83d-8cc4-392f-8611-f507317454dc | -13.14983 | -47.31302 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d895bb04-b336-3118-b0ed-7928b30ac783 | -8.68598 | -47.98679 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8634da9d-eee9-36ce-be77-db18bbcc5159 | -8.64841 | -51.45981 | 2025-07-12 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1ed56a9-f324-3b92-a0cd-cb5f5aa63b72 | -11.94766 | -49.2961 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 42612310-1284-37fb-abb5-2fb5866c32a6 | -9.85449 | -47.87737 | 2025-07-12 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8bb15b78-1fc8-33ee-ba84-e9793a0f58f6 | -13.11978 | -47.29898 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6adf8724-25a8-322f-b2cd-fe75f1f7e06c | -6.63118 | -56.28703 | 2025-07-12 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 56f37cbe-f80f-3c54-a9d1-723b879adede | -11.77195 | -43.86642 | 2025-07-12 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f405517-6f04-3999-8ccd-95f549f6e5ea | -9.80025 | -48.56672 | 2025-07-12 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc766008-a8f5-3e4a-aa3f-82bb48e4a266 | -9.85798 | -47.87792 | 2025-07-12 04:40:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0100d1e-2139-34e2-8258-33275a9eb031 | -10.84781 | -49.10887 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b560a98-e1a7-3783-ab49-186ab2f14793 | -8.92312 | -47.3507 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbab093-ccbc-3067-923a-ab1bb708c540 | -10.90423 | -49.21444 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d2884ed2-2cd3-3f7e-980a-1994fda5de0d | -12.41956 | -43.48537 | 2025-07-12 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| af5b9a19-2699-3342-bf25-8d3c9991a1d2 | -6.52032 | -43.32891 | 2025-07-12 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d365506c-4a08-3947-96b5-154b9a608a4b | -7.52323 | -49.75297 | 2025-07-12 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5708d032-f8b2-3363-ab7f-5b029b2f73c0 | -12.49177 | -51.27837 | 2025-07-12 04:40:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e44de4b8-0ce3-34ea-976d-504e4d957f3a | -10.57417 | -49.12674 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4a736412-ac0c-3d40-8fd1-2ea2f8b3b0e1 | -8.03614 | -50.10423 | 2025-07-12 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d364936d-2e80-35e6-a013-f169325797ad | -7.08325 | -49.60899 | 2025-07-12 04:40:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c18f0b2e-823a-3386-8961-35938b190fc2 | -10.84726 | -49.11253 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6581d976-8fb3-3c7d-916a-123813adf030 | -12.41891 | -43.49048 | 2025-07-12 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b55a6e74-2c07-3ce8-966a-a1fe00e1dc1e | -8.48659 | -49.85631 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fde7531-9a78-36af-bd1c-3090216775a0 | -9.5134 | -47.56573 | 2025-07-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 248074d1-166b-355f-a63d-c45d6b6c86b0 | -13.15676 | -47.26283 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 015ff9ec-cc5b-3054-8c18-e5f2763e2dcf | -5.84355 | -48.39191 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 960b315b-0f56-3065-8881-463268e3f79a | -9.65445 | -62.91824 | 2025-07-12 04:40:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 148b4129-42d3-3277-9f5d-729481fd2497 | -10.80252 | -49.63258 | 2025-07-12 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7353a717-5da6-353b-b0af-130be2ec91a4 | -6.86635 | -42.77478 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 96172ae8-391b-3532-88ae-df7f33112c65 | -7.99552 | -46.40306 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebed8a75-4de9-3c7a-a36e-ddc19d4d1aae | -10.94625 | -54.36964 | 2025-07-12 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f962ef2-81f5-3c12-a032-955ef73d0af2 | -11.83932 | -47.50164 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 77a589f9-c46d-3163-b141-e77a9ed7c850 | -7.2195 | -43.09312 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1763ebd4-e913-3412-839e-10cdf5f5a7a6 | -10.2284 | -56.76665 | 2025-07-12 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c4c1899-8e0d-3341-a18f-4fbb17a7a9a2 | -13.12919 | -47.31306 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0c053cb7-796a-3f05-aebb-c3a94b21d69a | -12.41073 | -45.34993 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee74e28e-8c16-31da-af33-be91c8be8819 | -11.42834 | -46.39236 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a291deb-fc37-34ce-b898-8fbcb5a3b6cb | -7.90778 | -61.51132 | 2025-07-12 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0cc9994-6d63-3e64-bc6a-11ddb28c6734 | -7.9497 | -49.65781 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7718b091-afe1-3555-a274-6c0a25e51cd7 | -7.98867 | -46.42427 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa08dce6-313e-36eb-96b8-dd67d798c430 | -12.41437 | -45.35435 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36bcf2f4-8f4d-337e-8df5-6c7b9901fdd8 | -8.69799 | -47.1628 | 2025-07-12 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf792b0-45b0-31b0-b7d3-3282eba10549 | -6.86177 | -42.77409 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2ff05ee2-bf17-3d67-b3c0-f673bd253acd | -10.70177 | -48.30665 | 2025-07-12 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed3c202d-275f-3784-8d02-1fab4ed8a91b | -6.88278 | -45.22271 | 2025-07-12 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad9f7e37-0689-348d-be72-4d9de8e8f72e | -10.96551 | -49.25394 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76cfcee3-f291-3962-8c31-4a4c178583ee | -7.2227 | -43.10286 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0ee18aac-5a80-3230-9908-3e7d6c26a1cf | -12.41797 | -47.50383 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abec0613-845d-3b56-9a25-54781bdbe53b | -5.84076 | -48.38789 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 948bc941-5c3b-306e-8c69-29923a58fd3e | -6.71629 | -44.33351 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56e967c8-00c7-302b-baa2-f23e02c73ad5 | -12.03843 | -48.76175 | 2025-07-12 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcf409ba-dde6-389d-8653-f8f701449209 | -10.90142 | -49.21027 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README11.md)
