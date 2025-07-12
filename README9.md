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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035d394c-7049-322e-bdb7-4aebf5464a34 | -6.53591 | -55.0357 | 2025-07-12 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1868671d-a3f0-35ca-9ea2-c048a7505269 | -11.42697 | -46.40185 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0ce815d0-f2f4-3172-83fb-7bdb480a919a | -11.72833 | -47.46864 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d1462ae7-920b-3f4e-8302-2a8073077e20 | -6.72148 | -44.32668 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be0f9929-0498-3e12-845b-b44d8c882453 | -8.47317 | -49.61572 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d728c7ca-3d75-3478-90f5-f46341ab08a7 | -7.67436 | -47.32774 | 2025-07-12 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c613a3c-528f-3924-abd2-78ea014491e9 | -6.87589 | -44.0691 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 855b577d-29e5-3933-bff1-0ed2159fc399 | -7.21821 | -43.10217 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b756aaf0-8e15-313f-8cb4-28823d6cf277 | -9.50574 | -47.56864 | 2025-07-12 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec247de3-6170-379b-af4e-168111a03c29 | -7.66618 | -47.33452 | 2025-07-12 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c81c608d-0eba-3227-9364-bcdbaa45e33d | -5.84689 | -48.39243 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ca45cf05-2085-3561-9507-0852372458f2 | -10.67709 | -56.54935 | 2025-07-12 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6538d092-30ce-3152-ba7d-70b02b622f5e | -10.89469 | -49.20918 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7afca70e-8feb-3afc-84e1-2be65e5360d0 | -10.66862 | -49.50616 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 27a70a96-954e-38b0-95e3-a15d3726da76 | -6.85768 | -42.7713 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 38a188cf-dcee-38ab-857e-56841901decd | -10.90478 | -49.21081 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0090f684-be51-3b11-8c82-cb32ff8e820e | -11.72955 | -47.46003 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 70614820-91ea-39fb-a656-e225d0f7d282 | -12.11178 | -44.97841 | 2025-07-12 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9f3e1bba-f1ff-3062-bbd3-65d74cc1f718 | -13.14099 | -47.31035 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddb95ee8-4e62-3d36-b172-9b211c1093a8 | -12.99737 | -46.31746 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 579a20ec-8bc8-34bd-85f9-0e6dca9f139e | -6.71326 | -44.32551 | 2025-07-12 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a396e3d4-3a25-37c8-b52f-10491dabc0fd | -7.22335 | -43.09833 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad806188-31c8-39ed-90af-8545e93376ed | -9.45871 | -48.159 | 2025-07-12 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e0108ef-4a33-3035-bd23-f9f260be64c1 | -10.85064 | -49.11306 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c8172294-8f50-3244-9fb9-6f9f0948dc6c | -10.54742 | -52.03538 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c526b5a-4203-3176-81f2-477e2a30c2ac | -12.61067 | -48.36897 | 2025-07-12 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3331a212-708a-32dd-bb1c-51005b2e2e4d | -13.0233 | -46.27539 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5991e080-0d2f-3b42-88e4-52a52b1f3814 | -8.04274 | -50.10525 | 2025-07-12 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8c43360-16b3-3f63-9617-902e52efeb6f | -10.35313 | -49.92386 | 2025-07-12 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f2766c2-e360-3293-8d3c-687d73b10839 | -7.68387 | -44.37307 | 2025-07-12 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 524fb4ec-bdd7-35a4-9293-41887563e682 | -8.68941 | -47.98733 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e691571-819c-3ca2-ab07-0acce8d1de4d | -12.41021 | -45.35378 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ceb3a55-859b-3bbd-99ea-16b0c728b7f4 | -11.84234 | -47.50647 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e5ef318-5a48-37a2-81f2-730d065d8f70 | -7.92966 | -61.55851 | 2025-07-12 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78b1e6e1-356b-390f-a733-8b8aa5d4e239 | -11.42453 | -46.40794 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6ae67f8-ebb9-3644-b05c-975bc9c143c1 | -7.10387 | -44.11272 | 2025-07-12 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec54462c-cbe8-3338-9c66-7a1795517e8f | -6.64868 | -43.21681 | 2025-07-12 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a8c5e735-91ac-3cfd-a3cc-e312965e1fe1 | -9.91518 | -47.83044 | 2025-07-12 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87257cb4-71b5-36c0-8003-e995f9458251 | -10.85738 | -49.11411 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6affe2db-043a-34aa-b294-65a8c501fbaf | -11.42967 | -46.39907 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fbd9f1d-2632-38e2-9f7d-7cc6a8d81bc6 | -10.22091 | -55.45107 | 2025-07-12 04:40:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 300956b7-7af2-36d0-9959-d0d75d2001f8 | -11.42587 | -46.38221 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91c7cb30-a60b-365d-9513-d543eb2b07af | -7.48031 | -47.51701 | 2025-07-12 04:40:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd41eeb1-68bc-33f5-9d0d-71d6f2492df2 | -8.46986 | -49.6152 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec650b08-828b-3f90-b5dd-b5c0c696a2b8 | -12.99579 | -46.2698 | 2025-07-12 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bcf6e1f-241d-34f6-9184-d68a22112a04 | -12.41802 | -45.35875 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 677c9173-9671-3cd2-b6ad-5ddba9c4b924 | -8.47263 | -49.6192 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e7d7fd05-fa56-38d6-8a2a-7e3126d44c83 | -10.66916 | -49.50259 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 94d35878-49c4-3bac-9004-56fd47738803 | -6.62824 | -56.27744 | 2025-07-12 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1020f7ff-27b0-3b32-b67d-31057fa9d505 | -13.15508 | -47.2655 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9372734e-cbd9-35a0-bdb4-0dce551be57e | -8.92371 | -47.34666 | 2025-07-12 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aeb614e3-ce92-341b-9bbf-7f111faebfaa | -8.47594 | -49.61972 | 2025-07-12 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 76d23680-0310-3df6-b3ad-9d28878b2549 | -8.64505 | -51.45927 | 2025-07-12 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebcf7055-6288-3689-9298-679bc39f6203 | -12.41543 | -45.34663 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 416c045a-11a9-33df-a8cf-7d1d18fa65b4 | -8.1145 | -46.22528 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08bfdf8e-dcd6-3afc-a053-6cebc5436152 | -7.18522 | -42.97608 | 2025-07-12 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 81531eb0-71e9-3a99-b773-b2b8a25691f6 | -10.69086 | -48.30861 | 2025-07-12 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5b1918a1-fc7d-3db0-8d4d-7af5953e93fa | -11.89444 | -44.89429 | 2025-07-12 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e30b75f-8317-368d-8ffa-3b977f0fb7be | -10.37552 | -47.55882 | 2025-07-12 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5593781a-9b0c-30fc-a749-4e46ee203ff1 | -11.72771 | -47.47298 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e78d8f41-dee3-35a8-ae24-28f5dd2de70c | -11.79708 | -46.65009 | 2025-07-12 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0d387d8-0e68-3c4a-a6e6-547a6c42c23c | -10.6697 | -49.49902 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 572cd868-8c7b-3ad1-a040-40170b64f3e3 | -11.60664 | -47.61344 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b93d9bc3-4282-3d59-a87c-cade50d42dbe | -7.99616 | -46.39866 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18620fcf-b35a-3d31-a937-8c7f1c4cc4c8 | -13.15918 | -47.30045 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35904e45-9032-3add-b174-6582b9ac5eaf | -8.66153 | -46.98851 | 2025-07-12 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e729497e-fc6e-3583-9d82-4c73d5039784 | -10.55672 | -49.43755 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7e1e380-8119-3aa1-822c-7c32b6bb7a10 | -11.42715 | -46.38883 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dca849e2-8a10-3753-9d3f-9f0a0a339b44 | -8.69786 | -47.18793 | 2025-07-12 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f4e86d2-19c7-32ef-a785-1fe6e8b20d17 | -11.94822 | -49.29241 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 701d884c-dc93-3930-b19e-071118190aa3 | -7.93058 | -61.55371 | 2025-07-12 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 547921d8-283f-35af-84da-29f773cedec4 | -11.40671 | -46.37881 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1de06c32-418e-3ad1-80fd-1e9c483cb03d | -12.41907 | -45.35105 | 2025-07-12 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 066113a0-001e-3dbb-ad01-8a94a7ffbaeb | -13.13051 | -47.27721 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ebb28e9-8bad-3d72-9d0c-9f85aa08fdc8 | -6.85721 | -42.77333 | 2025-07-12 04:40:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35d766b0-e06c-36e7-ad88-06a918d4ad6a | -5.84969 | -48.39647 | 2025-07-12 04:40:00 | NOAA-21 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| e3b20be4-6bbc-31dd-b7a3-2143cc195d25 | -13.12858 | -47.31728 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4620a845-44e8-37f0-86e0-59f3ffa5db9c | -7.80589 | -46.21669 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07d3917f-2057-3e86-b54a-e16b8aef9132 | -10.84107 | -49.10782 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9b393a43-f7a1-371a-856e-90a8fa30e8d5 | -13.12484 | -47.29023 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f632432-fa1d-3cc4-93ed-22cc26f170fb | -11.72894 | -47.46434 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cd387781-3fdf-3edc-8354-e18f47cbaffa | -10.85401 | -49.11359 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c4b6fa06-d401-3486-a7e7-71656176ed25 | -13.14104 | -47.28349 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c37fb0af-5e27-3f9b-ba42-615cd7dcb94b | -11.27962 | -46.40186 | 2025-07-12 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f0c5b6a-84ce-39e5-8f27-63ca87f62705 | -9.17588 | -49.66583 | 2025-07-12 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccdef66b-500d-33b4-9ee7-67f86e8094ae | -8.75501 | -43.95666 | 2025-07-12 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ad7189d-7a23-3d77-b266-7988e907c7d0 | -12.03499 | -48.76121 | 2025-07-12 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34ca7e7b-a786-301b-a09f-cf6d9cd824f2 | -7.99248 | -46.39812 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00ec0306-5016-38ae-8de5-53031d43843b | -9.91577 | -47.82652 | 2025-07-12 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f1c9079-d435-35d0-984c-9709bac99796 | -11.94033 | -51.68848 | 2025-07-12 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e798de24-fbc5-3eef-90b7-0a7f461b50e0 | -11.73257 | -47.4649 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 957acec2-65d3-3ba4-9a9e-1c410c5305b4 | -11.83809 | -47.51022 | 2025-07-12 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21e28f79-801e-3216-adf2-833164cbb2b3 | -10.57191 | -49.11895 | 2025-07-12 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7ba250b7-e77b-3c93-b9d9-b1a7285054e4 | -13.14038 | -47.28809 | 2025-07-12 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8023ace-c302-3394-8ad2-b95b70e07e47 | -8.75683 | -43.95565 | 2025-07-12 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c15ba2b2-7e0c-345f-893d-262c476c59f0 | -10.87592 | -49.10566 | 2025-07-12 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b1b30dc-8563-368b-8d3e-cd4625935946 | -7.885 | -55.36496 | 2025-07-12 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ff2b27e-5881-3e2c-a310-eecb4531b901 | -7.99184 | -46.40256 | 2025-07-12 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5b25abc-5ef3-3173-940c-b2cbb5089f75 | -8.8459 | -50.4938 | 2025-07-12 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19ef1c7b-0bdf-3056-90b9-4b73d5e52e81 | -11.49626 | -48.0761 | 2025-07-12 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
