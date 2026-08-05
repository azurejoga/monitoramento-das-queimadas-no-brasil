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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d03a8d69-708e-3c5e-8649-e5c5e5eff01c | -11.2112 | -54.903599 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e07ed8e2-87d4-3031-869b-c505422feba0 | -11.1954 | -54.880501 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9560bfdd-1abf-36b1-aa04-caf20329f000 | -11.1584 | -54.898399 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90f588cb-b03c-3542-9790-6a1d056a1a8d | -11.2054 | -54.923 | 2026-08-05 00:48:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f2f8bef-f374-396c-989f-c50225804995 | -6.5376 | -55.1642 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 805b4571-562c-375c-872d-7785a06341a4 | -14.1825 | -54.4095 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 99ea4c6c-6933-382a-afb2-bc34b2fb8019 | -6.5496 | -55.171101 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 196b8385-a5b4-3821-8819-dd1615785e47 | -6.6533 | -56.4123 | 2026-08-05 00:48:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c61874-c6a5-384e-b333-f131a4061d75 | -4.3653 | -47.787899 | 2026-08-05 00:48:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80bc3fa5-a490-347a-bf06-7e21458a218f | -6.5355 | -55.1549 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 759db309-a3c7-3b6c-b83a-e8efc5eebe3f | -5.3775 | -55.889099 | 2026-08-05 00:48:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63b24355-10fa-3c6d-bfde-a4e61287a405 | -15.1049 | -55.667702 | 2026-08-05 00:48:00 | METOP-B | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4efbc96d-870d-300f-88da-f46e2151d7b9 | -6.5431 | -55.143299 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a34afcc-2bd0-3b34-a51c-9759972a5852 | -11.1642 | -54.879002 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3434d7da-9192-3fd0-8f37-e27a9b482b86 | 3.4814 | -61.3106 | 2026-08-05 00:48:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 72e8dfea-ffd1-37b9-be00-63f787caa41e | -14.1709 | -54.403599 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e60107ad-08cc-3e01-92da-13abb0fcc2b5 | -16.795601 | -55.6628 | 2026-08-05 00:48:00 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7c4b00b-a51c-3373-896b-4c7d41a9b9dc | -12.5826 | -46.941299 | 2026-08-05 00:48:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d89baa55-b2f9-321c-ac0b-2c8dd9827873 | -12.2014 | -52.869301 | 2026-08-05 00:48:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f644167-4a59-3700-8b5d-0b9288c0f12a | -11.1914 | -54.863499 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03ab48b6-c965-3101-ab71-7ae51886e871 | -11.1857 | -54.882801 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72b67390-96ae-3d5d-b993-2df8ecda7d85 | -11.1602 | -54.862 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b66993af-f685-3764-81d5-8f9fd2e26336 | -12.5852 | -46.912701 | 2026-08-05 00:48:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91decfc0-d01f-3180-801d-c2ea9fcd9693 | -3.6594 | -49.480099 | 2026-08-05 00:48:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0040cd5-b5b9-3d10-845f-dd3cde343b02 | -14.1387 | -55.237099 | 2026-08-05 00:48:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df461a66-2d86-364b-a5a8-44f429a1e815 | -11.2092 | -54.8951 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45d17d35-93ba-3d81-8567-e36058bafcee | -14.1806 | -54.4011 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce5ed44-ab78-37c6-914e-18155da91272 | -11.2132 | -54.912102 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd47a9a-f750-3243-90cb-fabc7ac85a74 | -12.4371 | -50.530201 | 2026-08-05 00:48:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2545d11d-6ffc-34c2-9581-6e48580c5008 | -6.5518 | -55.180401 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4282f49-7c23-3462-9330-82a99ea1a2ec | -11.1779 | -54.8937 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 267599cc-a0b2-3d09-bd3e-9c8081a43cd9 | -3.1847 | -52.893902 | 2026-08-05 00:48:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecec8e2d-9aa4-3136-b8f0-5fc2deb55083 | -12.3187 | -53.182499 | 2026-08-05 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4bc49ba6-a5b1-3877-96e5-20cff8c06b50 | -6.5453 | -55.152599 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5557fa69-7049-36d6-baf1-79d6031b2447 | -14.1963 | -54.423801 | 2026-08-05 00:48:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f8c94480-b984-33a2-a74b-eaf308fc5cc8 | -11.9187 | -55.900501 | 2026-08-05 00:48:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3b2a92-f86a-36a8-b418-1b4530d87fab | -11.221 | -54.901299 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 752d9290-1c53-39f0-ba30-1a3ca1459757 | -11.1819 | -54.910702 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 813bdf10-510c-3eb5-bc05-12904381639f | -11.1994 | -54.897499 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c27cfbd-baef-34f0-ae5c-c0e273821329 | -11.2227 | -54.864899 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16247943-f8d4-340f-adf7-599572ee32a6 | -6.3402 | -55.7304 | 2026-08-05 00:48:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0efe11dc-8e3f-3bfe-a4a6-4ad14055c9a4 | -11.223 | -54.909698 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe59297e-c4ff-3bd5-90ec-9752772e864a | -11.1702 | -54.904499 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9926ab26-fc2c-33b1-bb5b-2ff0527101e9 | -9.2861 | -60.638401 | 2026-08-05 00:48:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54305b7b-9930-31e2-b3d5-9fbb8c92b7b2 | -6.5626 | -55.138802 | 2026-08-05 00:48:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c22a1884-1fec-3a31-84f1-13e89a03c49a | -9.4916 | -57.321602 | 2026-08-05 00:48:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 691e85c8-ae4e-31ae-ab8b-462ed733b356 | -11.1937 | -54.916801 | 2026-08-05 00:48:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec7552e-2085-3137-917f-bdb2ff284bdd | -12.3162 | -53.172298 | 2026-08-05 00:48:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23190e43-0388-3fe5-a45e-4ca5c9cd1e4e | -6.5514 | -55.1569 | 2026-08-05 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| b5a51324-815b-39a9-b187-6cf366d84cca | -12.5754 | -46.9329 | 2026-08-05 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 656ba56f-d454-3682-8d30-05f4680a2e9c | -12.5942 | -46.9527 | 2026-08-05 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 206.8 |
| f96bab1b-4f1c-3955-b127-d03d09262974 | -12.575 | -46.9555 | 2026-08-05 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2b5bcfec-77c2-3176-a96d-44bee52e2799 | -9.4765 | -40.3613 | 2026-08-05 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 4be31e58-e4d0-3ad4-bef4-f5f77fcf457d | -12.5947 | -46.9301 | 2026-08-05 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 297.1 |
| a4f2cd58-48eb-3c9e-a886-a978f9d3c6bd | -12.4386 | -50.5109 | 2026-08-05 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 3bb94035-5b14-37e5-a948-93bc5f55d518 | -23.13796 | -50.29618 | 2026-08-05 00:50:00 | TERRA_M-M | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| ca8a1a98-f55c-3e87-841e-09a75b49fcf5 | -23.13009 | -50.30347 | 2026-08-05 00:50:00 | TERRA_M-M | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| b38e175e-a51a-3a30-948e-187fb00f9afd | -11.17725 | -54.90705 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 267.3 |
| f6c8765e-1cea-3153-aad7-15979ece6ee0 | -14.17487 | -54.40079 | 2026-08-05 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| a87471f0-f13d-32c4-8849-2bb9ed515743 | -11.1982 | -54.92655 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 44682f4b-bb17-39b8-b387-ff841702769d | -11.1745 | -54.89018 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 18baa086-6879-3410-bae5-f5021ca6e6d9 | -11.15721 | -54.89856 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 37e3febd-2e4b-32ca-bc24-726de9cdb53f | -12.21048 | -52.86846 | 2026-08-05 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 49c2eb7b-b44e-3d62-a756-bf2de3c02e64 | -11.17843 | -54.87761 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| dda5b84a-f525-3c3c-bf46-c7b57c8d3588 | -11.91622 | -55.92088 | 2026-08-05 00:52:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7015c7a6-e863-356c-891b-7f445f5d7e04 | -11.18916 | -54.90507 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 187.7 |
| f7ff6f9c-7df5-3c80-952b-c9ef7bdb87ee | -11.33726 | -62.22032 | 2026-08-05 00:52:00 | TERRA_M-M | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9516bb95-2f9f-3bc4-a3fa-177f24f162cd | -9.28461 | -60.65562 | 2026-08-05 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80f9b795-15d3-38ff-9ff9-af3e88fc66eb | -11.19833 | -54.88607 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 4144adae-e16b-3f6a-a975-bac87c3bdb24 | -12.4403 | -50.50602 | 2026-08-05 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 909b629e-413a-3801-977e-40225f16bafd | -11.19297 | -54.89252 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 026192ac-381e-31d1-a6ca-b2ac88e6cede | -9.28338 | -60.64672 | 2026-08-05 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 212726cf-82e8-3a01-9101-bae035751c44 | -14.16325 | -54.40334 | 2026-08-05 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 8d07ae84-3aea-330c-8c48-2f1d1057609f | -14.17766 | -54.41777 | 2026-08-05 00:52:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b49351d8-0ead-351b-9dbb-5668daff8d9d | -11.16914 | -54.8966 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 322.5 |
| 56960a65-0c10-386a-a1ea-8abf7c27af0a | -11.92486 | -55.90493 | 2026-08-05 00:52:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| af7a7cff-2f32-30dc-85fa-d7dad357f382 | -11.18001 | -54.92396 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 200.0 |
| 2da61085-ffe5-30b0-a6fc-a075081b877d | -11.17442 | -54.93053 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 564cc886-dcf7-3350-ad4f-d54689504404 | -11.97369 | -61.95151 | 2026-08-05 00:52:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9b022927-ac8c-3a06-b9af-e1b462e4fcbb | -11.17176 | -54.91346 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 373.5 |
| 422932a7-73ca-3d0b-8d5e-438d7a456638 | -11.20107 | -54.90309 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 09210234-3da4-3d48-b4cf-96bc8eb0aa01 | -11.18106 | -54.89462 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 3d622d8f-5b30-3de4-96be-671985edf904 | -11.18365 | -54.87104 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 052d7ef3-da97-378c-a885-9c37dbd4012c | -11.91401 | -55.90685 | 2026-08-05 00:52:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ab1f6816-f2d8-394c-b0a4-062d3479d807 | -11.20379 | -54.92003 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e765babd-3c41-38bb-98a5-36a6b3a39cc0 | -11.18632 | -54.92856 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 92560f37-2537-3ee8-991c-c1d8e7419ad7 | -11.15985 | -54.91544 | 2026-08-05 00:52:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ab86d94c-a2d1-3e1b-b320-8b4f1067c193 | -11.23138 | -54.86287 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7af38f68-d4a6-386b-97b8-adef7767cf3d | -10.8145 | -65.09247 | 2026-08-05 00:52:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e614b7e7-d5a4-36a8-9f4c-2df747be4b89 | -12.43427 | -50.51241 | 2026-08-05 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| b1f4dc43-d78d-3216-b389-8690a22f224c | -11.18642 | -54.88815 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 7694b570-c9a3-3a56-b51f-d48021191702 | -11.17172 | -54.87311 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0759a85b-43ac-3b67-86e1-2d1c2e332d1e | -11.21296 | -54.90102 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.8 |
| 96dd499b-462d-3edd-b4d4-f671dc74f8a2 | -11.19189 | -54.92197 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 143.2 |
| a01a6b6e-9074-3e53-9a84-e1e65092c46b | -11.19558 | -54.9095 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 83.6 |
| b70545e8-72c0-31e9-a07b-de5c18ee59ad | -11.18369 | -54.91157 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 290.8 |
| d2c462e9-7a95-3161-962a-6b6f14b001c1 | -11.21568 | -54.91801 | 2026-08-05 00:52:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 0db83b48-82a3-38c9-a5f5-16952cca87d4 | -11.16648 | -54.87959 | 2026-08-05 00:52:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 156.0 |
| 1591c71e-ee0f-38a1-b224-a78e8cbd8c90 | -4.95593 | -62.35653 | 2026-08-05 00:54:00 | TERRA_M-M | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 564fb81b-ec33-3e5b-9d41-8d3f0a80e589 | -6.72354 | -58.92587 | 2026-08-05 00:54:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README3.md)
