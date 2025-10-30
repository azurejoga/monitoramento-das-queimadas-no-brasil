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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e62cb64f-d20a-3b94-8dff-4b1b5ee03fec | -7.73607 | -41.37523 | 2025-10-30 04:04:00 | NPP-375D | PATOS DO PIAUÍ | PIAUÍ | Brasil | 2207777 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49f7d15a-5ee0-3d1e-b6eb-eb583f331ffe | -3.78932 | -43.905 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 96fd215e-24bd-3a28-be45-bfcff36c578c | -5.72478 | -44.40854 | 2025-10-30 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 462ed45d-53dd-391d-82ec-b95c3840c3ec | -7.39118 | -42.46531 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f243d918-82b8-3d28-9807-5a5cd44ed454 | -4.46846 | -45.75812 | 2025-10-30 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bd7c376-0822-323b-983c-e7967a74ba78 | -6.96848 | -39.11156 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 958f770c-3308-3951-bf69-648ce866de8e | -2.76702 | -45.39334 | 2025-10-30 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6643cac9-1cd6-3176-a5e1-2b8e626831ee | -6.55749 | -42.3541 | 2025-10-30 04:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fd03c1a-eb13-3d8e-be2a-e3ea26d8fe57 | -6.3123 | -42.10073 | 2025-10-30 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0aa316f9-89a0-3f91-9126-b347b5b08fdc | -5.05894 | -45.31932 | 2025-10-30 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd88ca84-2599-36f9-a724-e486808365af | -6.48128 | -46.88767 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7c628b3-73c2-3e70-a66c-280a5b3cf85b | -7.3453 | -47.63313 | 2025-10-30 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e374de7-c966-382e-8ce7-cf5e6f5ef03e | -6.40391 | -47.0692 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 436dd992-d304-3b0f-bf90-38af520e38bf | -2.25453 | -47.024 | 2025-10-30 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 458ab7cd-cfb8-3916-b437-d9d25fbb7355 | -4.2513 | -50.67552 | 2025-10-30 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d3ec986-4b3a-3eaf-b852-9b2f2c23b000 | -5.53689 | -41.70499 | 2025-10-30 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8d260894-9f10-3422-b7e5-f83066276af2 | -6.97428 | -47.31733 | 2025-10-30 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| feab7c83-db87-3c49-be26-1077086c05f6 | -6.16303 | -41.61338 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 945b5c2e-d843-3b58-a14b-1c070886d62a | -5.31057 | -40.85011 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 18027566-9b3c-3cfb-a297-5a83ae8f0027 | -7.15424 | -44.86137 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c4afd92-f52f-3990-9f63-99882864e99e | -6.53366 | -43.5722 | 2025-10-30 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 874954f6-f14f-32ab-917a-0fc5e7ac46ff | -7.79964 | -46.4587 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ee6390-79df-342e-adef-4ebbe5414544 | -7.60989 | -46.79678 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 606ec3f2-be46-3972-99b8-faa76c4fa89e | -5.63546 | -41.09496 | 2025-10-30 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2ea7c16f-77d0-3751-9af0-616f5f3efc97 | -2.85471 | -48.2458 | 2025-10-30 04:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66a3592e-a522-3caa-8c1a-24623b0c1da7 | -5.33711 | -44.84984 | 2025-10-30 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 794408b5-fa39-3d4f-8551-d59c1aa58fd6 | -4.26282 | -43.70288 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 4e6ff4f1-8c74-3376-8718-f58d2339d9d6 | -6.15057 | -41.60379 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee58d712-03f1-365b-917f-3dc711c9f306 | -7.59092 | -45.37357 | 2025-10-30 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7511219e-e1ea-3970-bd1f-14c0041f1410 | -6.13685 | -41.7113 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6d5d9c8-ae14-3f86-9cce-d11668602298 | -6.27547 | -41.82468 | 2025-10-30 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a06c8e57-b438-3947-84cc-e3cdb49dec3c | -7.15908 | -44.85687 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c6f4273-8d59-3a4b-97b4-700a51d7a4cc | -6.88171 | -45.55729 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1ede1ad-31ed-3829-8020-f526250fdde0 | -7.32978 | -42.49089 | 2025-10-30 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8ccc2c1a-e237-3ab4-ac8f-01649651c52e | -6.22036 | -41.82367 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6da211b-80c5-3773-9c55-a656ebc2e086 | -6.97968 | -42.66357 | 2025-10-30 04:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d6e2b3f5-002a-38a8-a915-8cbc5ccbd82d | -6.14368 | -41.71254 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 96f184a2-b99d-3673-858a-e5cd4ac8277a | -6.09129 | -41.77606 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 89f2b445-8e9c-36e3-a2a0-64c907612535 | -6.10891 | -41.71046 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b21e672-1bf2-355f-915e-17bfdf874f32 | -5.59083 | -51.12867 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70196ee7-0db1-3a86-adb0-d4b6c638e121 | -5.80156 | -40.81876 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8640ecaf-8786-36f6-b80c-1ee3aefedfc9 | -7.2793 | -46.78364 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96e92b6c-8bbb-3d63-ae35-7a81238d759a | -4.33096 | -47.89218 | 2025-10-30 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b070fa6-5bb8-3fad-a456-5e6155f1db99 | -6.13483 | -41.5712 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca360759-d8c4-3a94-bef7-cf3eecbbe07e | -6.99528 | -39.13764 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c7320e95-1fe2-3437-9a13-b89bb1ee34a9 | -6.15821 | -41.66546 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d5b2e76-adba-3b4b-9f94-b74a9ad43de5 | -7.65358 | -42.25006 | 2025-10-30 04:04:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27e924d8-1cfe-38be-99cc-eb3b9cc03e7a | -4.69879 | -37.80172 | 2025-10-30 04:04:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffd06c9c-40cd-3ec6-8a3b-a59c5c799b79 | -5.06448 | -40.47541 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2f5b422d-ac23-35ea-b332-054e33ef2ccd | -4.64111 | -42.52739 | 2025-10-30 04:04:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18813333-c278-331a-b95f-f08849c8d1ed | -6.19011 | -41.51241 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b20abbba-ea18-3253-8ad1-4569cedc2c57 | -5.80657 | -40.83033 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47873e92-7005-31a1-bbe6-3cbcc0acbb7e | -4.3166 | -48.23063 | 2025-10-30 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e886978f-e1d1-3b81-afc7-f893c3d385ac | -6.11576 | -41.71151 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 946a82ab-e1c0-3aad-9dae-f6654df15e4c | -5.67367 | -45.88672 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0b6102c6-1760-3f5b-83d3-e57b29551756 | -3.79013 | -43.90005 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cca54c0d-f7c3-3509-a895-f298dd50411f | -5.65348 | -45.98162 | 2025-10-30 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72e7ff4d-306e-30eb-85bb-963c658cafbb | -7.08132 | -44.94024 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 461a18fe-a1b9-3e99-aed6-a64211d7d6d5 | -5.53629 | -41.70873 | 2025-10-30 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 37672bff-7bee-332f-bc4f-d7bebc73334f | -4.9903 | -45.51841 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a01b63c3-0071-3e7a-a0f9-6d00090236cb | -7.77712 | -46.48515 | 2025-10-30 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd7d72d0-c341-36d2-ad5d-ed79d44b0097 | -6.88235 | -45.5535 | 2025-10-30 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbcdd08e-287a-31c8-8bd4-95790a487764 | -6.22889 | -42.53126 | 2025-10-30 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c8d647fa-81dd-30bb-b6b5-23b15135a1ad | -6.13537 | -41.67678 | 2025-10-30 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 397d2685-3074-39ce-a94d-13f75fa82579 | -5.53052 | -43.22755 | 2025-10-30 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4061375e-2e6d-33e3-80b3-7a68e13c490c | -7.28077 | -46.06451 | 2025-10-30 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a5ad7e8c-4c9e-38dc-a3a5-47ae095b6df6 | -5.65848 | -41.1023 | 2025-10-30 04:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 145ee47e-8e33-34a1-ab14-31e5bcebb629 | -4.26051 | -43.71706 | 2025-10-30 04:04:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 1bc87eba-2f39-38de-986c-63c25d5d5f8e | -6.99585 | -39.13405 | 2025-10-30 04:04:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a577f37a-fb04-3e12-bebf-96b311bdfe7a | -7.87047 | -44.22476 | 2025-10-30 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39857422-7f3d-3374-baa1-fb32ca9d3ca6 | -5.77593 | -44.38853 | 2025-10-30 04:04:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c74f008-f288-33bc-b619-80f6742b9a1a | -5.30571 | -44.32283 | 2025-10-30 04:04:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a3ab0913-afa2-33e3-90ae-b53b52d13c09 | -4.84692 | -45.42728 | 2025-10-30 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5114d896-d790-3eef-b172-b1c4b6b29f69 | -6.98759 | -46.23383 | 2025-10-30 04:04:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cddb935c-8861-39b0-a1ae-840c444b2b62 | -4.43415 | -38.88278 | 2025-10-30 04:04:00 | NPP-375D | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 327eb98a-1f1c-35db-a7ab-3cea2a2c15ce | -7.52266 | -42.85392 | 2025-10-30 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11428524-0772-3a34-aa5e-b11b392bb75e | -6.64577 | -47.28824 | 2025-10-30 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2e9bdd2-f530-324f-b3c0-b861cbc99d4f | -6.9145 | -45.21411 | 2025-10-30 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75134c67-6456-3346-b2ab-054e315cdca8 | -6.13062 | -41.70636 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 640633c9-3b60-362e-809c-78270690d33e | -4.47651 | -38.06273 | 2025-10-30 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f84f73f5-c1b8-3dc9-a5a6-454568e202f6 | -3.66279 | -51.71748 | 2025-10-30 04:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7a8ca8f-7a99-3a3b-9118-b2ec43453eb9 | -5.12392 | -45.95116 | 2025-10-30 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ce65e39-b864-3d75-8573-14f4d6088d29 | -6.11233 | -41.71098 | 2025-10-30 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 437757b7-9d8c-376d-b791-3188619a72db | -5.06782 | -40.47593 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f56db337-f77d-30ea-83b1-63f649a84b0b | -5.43137 | -45.34117 | 2025-10-30 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7388b27-5292-3f54-82ea-0d38bc55980f | -4.46406 | -45.75747 | 2025-10-30 04:04:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f77ccf7-58b2-3629-a4d9-09e083fa81c0 | -3.80268 | -43.89713 | 2025-10-30 04:04:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1083cad-98e8-39d5-881c-d5bf73c7fa89 | -5.65422 | -43.24686 | 2025-10-30 04:04:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d37149cc-7932-3657-a7b4-fe2a259af968 | -7.38491 | -43.00848 | 2025-10-30 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e91441ea-c33e-38be-a918-8da98021072d | -5.91833 | -41.91457 | 2025-10-30 04:04:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca083c7e-7ab3-380f-abeb-0c8e1efe222c | -7.30383 | -44.97717 | 2025-10-30 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32e01d86-4afa-3bbc-bc19-5d30e5573f8e | -3.36053 | -44.26678 | 2025-10-30 04:04:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f7a4f0f-f5c9-36c5-ae98-4f0e816d83ac | -5.42313 | -40.91864 | 2025-10-30 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3d5262db-3603-344b-8381-13f89ec44d8f | -5.80489 | -40.84084 | 2025-10-30 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d65c577f-3d29-3e95-aee8-4487a91959da | -7.41988 | -44.66854 | 2025-10-30 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f50f3a04-9d27-3c1c-bcb0-689c3f75e882 | -3.46972 | -49.9214 | 2025-10-30 04:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4883f220-8cf6-3b35-b06b-1a2d38f905c3 | -6.26759 | -41.80822 | 2025-10-30 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4b1eeff4-1d3e-3e8a-a6cf-290f90f3bea2 | -7.07289 | -44.46598 | 2025-10-30 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59ad906d-9b88-3f72-b70b-3508626e2564 | -7.61508 | -43.58029 | 2025-10-30 04:04:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e6a74ea-cf27-3d33-842e-b3c0679ccbde | -4.57739 | -45.51103 | 2025-10-30 04:04:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)
