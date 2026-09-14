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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9907938e-316a-3bf2-aa5f-6e220c7a538e | -5.84153 | -52.04965 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbc5f40b-c92b-3b7f-ba16-be88bf7a32c5 | -5.36125 | -50.17146 | 2026-09-14 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 334702c1-6c72-3452-860e-6c56f2aad979 | -8.12258 | -54.81299 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92b2e79a-49fa-3624-a51d-c0a6379797c7 | -6.31595 | -59.96598 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcdd80af-bff7-3ff8-a6e5-39b89ea99fa2 | -8.4629 | -50.76775 | 2026-09-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7964e84-59f8-3934-ad3e-6ce95d82c706 | -5.88029 | -52.08129 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38e353bf-fc2a-3bce-b585-9c9d4be13661 | -5.17547 | -49.36319 | 2026-09-14 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a7dbe5-a0d5-3244-92c6-0f6f7bc0c226 | -9.43122 | -50.1286 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 39cf5b98-c0bf-3fd5-b716-0c582009a596 | -6.29351 | -59.94233 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c2d27d3-89c5-3163-9523-c56216e01f28 | -9.71641 | -54.35455 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c948157-b792-31cf-a0be-663d60991bf8 | -10.65279 | -54.14278 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e84625ad-fc42-325f-8295-e1138b74220d | -6.50039 | -58.38505 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6070510-a300-303e-abd4-a954c8b87ca6 | -9.44527 | -50.13065 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 802d4fb2-0381-3808-be8e-71b24735d99a | -3.73987 | -61.75356 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11d4fee3-a5e1-3e8a-bf9d-17fd82684acd | -8.5344 | -54.70695 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afd43e6d-6c4d-38df-803a-43b890962e32 | -9.4494 | -47.87132 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4637e03-b049-32cd-8aba-9403b0bd94dc | -6.28302 | -59.93274 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8c73f22-f1fd-39b6-b278-c239c451e55d | -6.29834 | -55.28865 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fa2436c-cf4b-3ca7-9938-e5d5613ec0d5 | -10.07131 | -48.77771 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b89e8873-68bc-3aca-9cb0-11bba5902d44 | -10.66158 | -54.15137 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a2023ecc-6137-3529-bbaf-3d7ec4e1db3a | -4.53736 | -54.9334 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3b08c5b1-aaa2-389e-90d9-b3fb15b3672d | -6.23685 | -51.68039 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b82a29cb-4d7a-3c8b-8656-fef8700ae0de | -9.26586 | -59.6404 | 2026-09-14 04:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2365d9da-64ff-31cd-ad51-5ddbcb0b7994 | -4.13156 | -54.01436 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6c1bd11-f913-3019-89b1-b3a44456ece4 | -6.13601 | -59.88289 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4975fac6-5f53-3c01-a34e-942395e8651c | -6.22505 | -56.04232 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7267c46-e6a9-31e9-847c-f82b178c3183 | -10.41244 | -57.22782 | 2026-09-14 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feee0c12-9154-30d6-84eb-110ced7db110 | -11.77796 | -46.40673 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01446217-a89f-3038-bfe7-4b5df94c2a76 | -9.4447 | -50.13435 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 728505e2-1fbe-37f4-ac1a-0aa702fa9961 | -15.56435 | -48.79685 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 433d0151-8c9e-307d-9b75-c83f591aac4b | -8.53729 | -54.71164 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8396902-c5e6-36e4-80c9-1c22b2fc4a40 | -10.65816 | -54.15078 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c021e4e4-8fc5-39e2-8441-3718eda792b8 | -7.68478 | -46.65123 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09314731-8328-349b-af30-17b07ae30f3a | -10.65319 | -54.13837 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85cbb4ef-6240-3277-896a-06e8c6d4564e | -10.95289 | -48.36642 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e737a31-d89b-374f-a385-8f25e2bf0877 | -10.58577 | -51.34433 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8acd546c-c55c-39ab-8f14-e83d7de82d3e | -5.8409 | -52.09645 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f22b46d8-efab-34df-a76c-257638341d5d | -6.28848 | -55.27758 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82ead2ff-0bd1-3bc9-ade3-e340eeec0b3d | -7.11564 | -41.80032 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4b03a5ef-ec59-336a-ae5e-a6c7bb0087f1 | -7.78366 | -46.65784 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4083609f-1d80-3c67-8173-f4ce03dfc412 | -10.47195 | -51.33348 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbd32c1e-9957-325a-9af8-640d97b62a68 | -8.53865 | -54.70345 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc446748-59a7-3790-aaf5-941b309afb31 | -10.72842 | -54.00146 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9473d313-de8c-3d2c-a79f-b748a57d4f4d | -9.18025 | -49.6683 | 2026-09-14 04:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 016f7c82-f020-37e8-93df-a3862147df72 | -9.4193 | -50.11533 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8cbeccd4-0978-3aa8-b698-f2bfdfafd3c9 | -3.52683 | -59.0664 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b301f8-4d03-3fef-bc95-23579d28e750 | -9.42097 | -50.14975 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1c01b42-8d26-3c04-be42-9c4c749871dc | -6.32307 | -44.17585 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbf47da5-46ea-38d4-95a1-282f87e6f8ff | -10.72998 | -50.60965 | 2026-09-14 04:53:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25d1d100-1bc1-309d-8033-672fbc6338fb | -8.12327 | -54.80878 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c28e96-1a78-327d-b8c2-04c66cf86771 | -9.4079 | -50.16666 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 3dd340b0-e378-391c-9db6-215911f68ceb | -15.54575 | -48.78806 | 2026-09-14 04:53:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 833336fa-303a-38af-844a-c4f5a1a798f1 | -10.69269 | -54.17601 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8de4a747-4f74-36a1-ac13-84dc392b8192 | -9.43746 | -50.13335 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 848b1c28-3619-3a89-b28d-02a2d8e5cfff | -6.30743 | -55.28083 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a69c7f3-8e4b-3220-a12c-09112c96f727 | -11.23396 | -43.447 | 2026-09-14 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d9716d3-3ff7-33f2-9575-323ff8a9af40 | -3.87439 | -58.90151 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5acd5d45-43e8-3a84-8f68-5a3cbe0ed606 | -10.67962 | -54.16992 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fcaf9a8b-2091-31a7-9d74-3b7b0d35bf0a | -7.01554 | -44.63245 | 2026-09-14 04:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9bb68a36-7490-3aea-9f57-005ed5a85452 | -3.3548 | -59.8249 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bff9d477-f233-3ce8-b608-7d578a7bda4f | -6.33599 | -43.36105 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7387a7d8-e5f1-3f1f-837f-915063db14bb | -6.87081 | -55.29935 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4586fb8-149d-38b1-9b11-1647df6a1d77 | -3.35238 | -59.38928 | 2026-09-14 04:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10f4e271-30a9-32ec-b053-29056e69d8ad | -4.3412 | -54.78427 | 2026-09-14 04:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aecbf363-a883-3829-a55c-41eb8eaa4116 | -8.53593 | -54.71983 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d9ecc2-1e9a-37d4-a6f2-04d82f67d341 | -6.20136 | -53.08612 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1e676a9-5fac-3ffc-9036-ef00389b5f1c | -5.12781 | -55.95767 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4978ac41-6f48-3a04-aac6-ed76ffeed1af | -6.58325 | -58.84219 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93d44c0c-ad19-3696-88db-5654e54a993d | -6.29406 | -59.93924 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7358a7b2-4266-3a7d-ade1-8c793cae9d67 | -10.96533 | -49.70089 | 2026-09-14 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d9e0fad-e7cf-3ad8-94f1-71048ad81a61 | -10.11235 | -48.85651 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15c765a7-b9cb-314d-87d5-274f125e7073 | -5.82309 | -52.10081 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97293f00-572d-3e15-a59d-35fb4164afbf | -10.10451 | -48.85951 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f25bb0b-eb2d-307e-831e-2a1070b1a519 | -6.28779 | -59.94451 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4ecb4dc-e320-3be9-9f95-cc0deea97d89 | -11.42223 | -45.13817 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 813c670e-a95c-3673-b451-e7ef82e3625a | -6.87156 | -55.29285 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56f6f48d-e831-374b-94a5-8d95b85a0f25 | -9.41473 | -50.14499 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec84114a-3683-33eb-b76b-5234bf049c1f | -4.57311 | -54.90638 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03bb86d0-ef72-3ed2-a765-fece57cd5317 | -5.35792 | -50.17093 | 2026-09-14 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d648d92-68c8-3476-a867-b7376a400f7f | -6.78969 | -58.78571 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dbc5be4-b6e3-33a4-aa50-9e5012152023 | -6.30819 | -55.2762 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3036dda-85c5-308e-a050-140ba9519528 | -6.28197 | -59.93884 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cee3c9e9-52f1-3efc-9843-493907b64959 | -7.09242 | -41.80514 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd77102d-7b28-3893-8ce2-2b63764b0e4b | -12.17213 | -48.96004 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b21f05c1-581d-306f-b9f8-750c8aad6f8b | -3.72827 | -61.7534 | 2026-09-14 04:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 053ebc6f-47f0-3641-80a7-251156038cbb | -6.3067 | -59.95796 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 483fcdbc-ebe3-3423-b805-990ae421f592 | -10.33002 | -55.35783 | 2026-09-14 04:53:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e56dcd2-c7df-3afc-9baf-8dd434139fd2 | -9.70691 | -54.36885 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c7b4aab-11df-3c9b-87cf-c6aea1549127 | -10.10046 | -43.95647 | 2026-09-14 04:53:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f37e4fd6-395a-3249-bf9d-e59174246404 | -3.52525 | -59.07556 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eac6a132-a517-34f2-97d1-fff4f6f5cf36 | -6.15359 | -57.69769 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adcf62e6-0278-378e-af38-33286a664498 | -5.1329 | -55.95742 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b948a357-ac93-3095-8105-5657298b4e33 | -10.66997 | -54.16443 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dc5ea30f-948b-3875-88d1-5d1e6caaa15e | -7.5769 | -57.69955 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 737ce62a-1dda-351e-a725-e57d9c2d4862 | -10.64707 | -50.57792 | 2026-09-14 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eedadf87-375a-3956-836b-999d221c5a3e | -9.43919 | -50.12221 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6e0b1b26-b951-35b7-96f3-af4c3f5451af | -6.28714 | -59.93976 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1c1c777-c38b-346f-b166-d9f49ab4f799 | -11.25537 | -54.12644 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fdeb047-0639-3945-8dc2-ea099992bc0a | -6.29078 | -55.28719 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 053f8c41-4828-3f5c-ba48-ba99e9025d0e | -10.73182 | -54.00202 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README40.md)
