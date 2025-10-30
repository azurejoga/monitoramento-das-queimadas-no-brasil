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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92d1c174-8964-3469-a829-8f5f955a2861 | -4.2731 | -43.7139 | 2025-10-30 05:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| afc08cca-4ca9-3e1a-a790-ad681cd5f2a8 | -2.76134 | -45.39249 | 2025-10-30 05:53:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fa033c4e-55a0-37d5-aaa2-6ea40048adfa | -1.34212 | -49.0269 | 2025-10-30 05:53:00 | AQUA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a3c3a02d-6124-37ff-9f71-24647180e5bb | -6.01162 | -41.98155 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| f7c549b3-c4f6-3c0d-8d80-a3c4cf83ca3e | -7.29599 | -45.65449 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 879f2f33-cf25-34f2-b8ff-a181dce81910 | -11.06715 | -47.53175 | 2025-10-30 05:55:00 | AQUA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 618d60fd-e081-3fc4-ad51-0f59903144d8 | -10.45266 | -44.31881 | 2025-10-30 05:55:00 | AQUA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f07d725e-b5b6-3a09-93c2-64300a466f2b | -5.3778 | -47.20192 | 2025-10-30 05:55:00 | AQUA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4420be57-91bf-315c-bf1e-d09e68da7485 | -12.39812 | -46.82214 | 2025-10-30 05:55:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3bd3f5a0-a6e2-3e93-9a4a-111324dc5234 | -3.80144 | -43.89274 | 2025-10-30 05:55:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 791047c2-2ce6-366f-907c-e2f9ae88c8fa | -7.62613 | -43.57995 | 2025-10-30 05:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 20cf381c-2dce-3c55-a3ef-ccb9f1458710 | -10.23701 | -47.62903 | 2025-10-30 05:55:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ecd7a0b6-a1d4-36dd-a7c9-fbf67150620a | -4.05099 | -44.2604 | 2025-10-30 05:55:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5eff68b5-dfcf-3b4b-be09-14bcdf6909ef | -13.16083 | -48.4451 | 2025-10-30 05:55:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 56bc7f42-58b2-39d2-a616-abdfd267e0ff | -13.17166 | -48.43687 | 2025-10-30 05:55:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c32157dc-9abf-35c3-8f36-8c93140977ba | -13.1593 | -48.45461 | 2025-10-30 05:55:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c6febf82-a2c6-386c-94fd-de35dc628902 | -12.48388 | -50.55663 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 9d5d070c-448e-3825-91af-5886f9111f24 | -6.13236 | -41.69818 | 2025-10-30 05:55:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a10ab7f1-c381-36a4-98d0-7cdc1aa2aa2d | -13.37523 | -47.37975 | 2025-10-30 05:55:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23f89963-72eb-342d-b08a-9b20ab8434cb | -10.48559 | -45.03747 | 2025-10-30 05:55:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb53bdf3-6e1f-3604-a2d8-8ea5f358e2dc | -7.95821 | -46.71386 | 2025-10-30 05:55:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 410b1036-f526-3dc3-b0c0-9be780136d5d | -4.15511 | -43.87948 | 2025-10-30 05:55:00 | AQUA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1623e39f-ae9d-326f-a9da-caa6305c8095 | -6.91497 | -42.24844 | 2025-10-30 05:55:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.9 |
| fb652c6c-268f-38ea-b00d-0a287cda4628 | -7.32297 | -42.47807 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 51fd0edd-e1db-37b4-ab55-5bb122d8e5ac | -9.84359 | -44.88911 | 2025-10-30 05:55:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 640e87f9-e0a0-3877-a0b8-188dc658205d | -7.0828 | -44.93646 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed64c201-533a-3c10-b989-7c51d218362a | -6.10941 | -41.71762 | 2025-10-30 05:55:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 27f8874c-75e6-3f33-9b5c-ddb3957e8fd2 | -10.86001 | -47.61486 | 2025-10-30 05:55:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7d090b27-d6fd-3289-9900-a830e401e2b4 | -6.12131 | -42.43598 | 2025-10-30 05:55:00 | AQUA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 74cf7901-78df-3c12-bb77-d3ec2a93b9b3 | -6.52343 | -46.90192 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 69b31781-0c28-3373-8c2d-fb479b5b1f71 | -12.18004 | -47.74991 | 2025-10-30 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a0d9e56b-0777-3e0d-92c6-48c9e047d637 | -6.12055 | -41.86036 | 2025-10-30 05:55:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9357d6a6-15e6-3472-9929-114157b7fb0b | -13.07083 | -48.20488 | 2025-10-30 05:55:00 | AQUA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0a6a9f71-6605-3ce9-b01e-92ac66acd7b0 | -3.79133 | -43.90023 | 2025-10-30 05:55:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 5a4734ee-e1c5-3ca9-bec3-aa0b62d6cda0 | -5.43123 | -45.34248 | 2025-10-30 05:55:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| a2ebdcc7-6e40-3d5d-b805-12c12c5eadab | -7.07402 | -44.93516 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e731f007-48ce-3e75-b7b5-6f7be3796fcc | -5.61056 | -47.11747 | 2025-10-30 05:55:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bcd09a6f-6e4b-3318-b551-460652d9482d | -3.63184 | -44.46878 | 2025-10-30 05:55:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7d713ecc-51dd-380a-9032-acd96ec101df | -4.2534 | -43.70455 | 2025-10-30 05:55:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e169e522-9856-317d-a26a-265a2acaee55 | -3.80276 | -43.88396 | 2025-10-30 05:55:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2eb47906-9add-301b-ab54-b3dc4b4efa0c | -4.46908 | -43.43871 | 2025-10-30 05:55:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9310bddc-73b4-3def-9e52-4f09dc8d38b6 | -12.30095 | -50.24424 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 29cc675a-a83e-3647-b0eb-a4ea7c977b2c | -6.01316 | -41.97077 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 3848b6ed-3767-3753-854a-b1281bc561d3 | -4.43621 | -43.2308 | 2025-10-30 05:55:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 08a337af-9710-3b54-adbd-f940882ffc0a | -12.51609 | -50.56218 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| dc6bf3f2-c906-329a-b41c-4a05b4ae23e5 | -7.07534 | -44.92638 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 664025c1-1eba-36fc-9933-5ea49d9073d2 | -13.29911 | -47.69242 | 2025-10-30 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cd59c1f3-f3a5-3153-9624-2e6d562b2621 | -10.27674 | -44.5793 | 2025-10-30 05:55:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2d96fe17-1ce1-30fe-bc01-fd7a3d0bea17 | -9.90549 | -44.89834 | 2025-10-30 05:55:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8586aa29-a3f0-3f7b-bf14-9779bff92990 | -13.35554 | -43.08667 | 2025-10-30 05:55:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| dfe0173c-9d33-3130-949a-acd7afabfb41 | -7.95677 | -46.72326 | 2025-10-30 05:55:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1b7dbc50-8f4c-355d-a699-7708a92bf73a | -12.70843 | -46.29425 | 2025-10-30 05:55:00 | AQUA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 40c3129c-72f7-397c-9fac-e097fabb9553 | -10.27808 | -44.57015 | 2025-10-30 05:55:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 72fce0fa-e10d-3934-aa90-6f8b5e9b95ee | -5.59784 | -49.07505 | 2025-10-30 05:55:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 2084496d-3a5e-3227-9b70-1e3566748434 | -4.25208 | -43.71337 | 2025-10-30 05:55:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8aa3593c-b6df-3cbb-9fad-7819015b6c9b | -7.61844 | -43.56924 | 2025-10-30 05:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| df317e1a-db06-3666-bce3-8f32f95cd6a2 | -7.34473 | -47.63039 | 2025-10-30 05:55:00 | AQUA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5717b2a7-b7bc-36f0-8c5a-157810bc0f2d | -3.21997 | -46.87786 | 2025-10-30 05:55:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9881b20f-e007-3c61-a9ab-5f2fa08d84d4 | -5.43258 | -45.3336 | 2025-10-30 05:55:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b9196573-da2d-3649-a385-2469273fd87e | -8.32741 | -47.91656 | 2025-10-30 05:55:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 013b8837-c613-30ac-bcfa-37762fe56c65 | -6.51416 | -46.90057 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1efc9c35-8351-3ec3-8828-6db33253364d | -13.2723 | -47.7457 | 2025-10-30 05:55:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d0111a4b-996a-3b2d-a671-e16dcac82e93 | -4.47932 | -43.43103 | 2025-10-30 05:55:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1b55309d-04c5-35a9-8886-dac4aaa01e90 | -7.92729 | -46.00934 | 2025-10-30 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| adf707a8-82b3-3dd4-8b2d-f7a15001f1ed | -6.37032 | -40.9711 | 2025-10-30 05:55:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0c5933d4-1027-3e4e-bd6d-78a25f30f02e | -12.29665 | -50.27062 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| caac002f-47bc-31bb-97e9-b8a5174324e1 | -10.23546 | -47.63881 | 2025-10-30 05:55:00 | AQUA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ecbc969-0456-3d19-8eaa-425cfa97aa6b | -12.49462 | -50.55848 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fa0eb41d-a125-3510-9eab-e53713d0e231 | -6.26503 | -43.60235 | 2025-10-30 05:55:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0aa20fdb-88bd-3abf-b503-076b280016d9 | -7.96765 | -45.43615 | 2025-10-30 05:55:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 84164ab1-9f3a-3b48-904a-182c355baa6c | -5.60891 | -47.12793 | 2025-10-30 05:55:00 | AQUA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 13e286b7-e013-34bc-97d2-1771d4aff044 | -12.18462 | -46.70499 | 2025-10-30 05:55:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3c52bb63-4391-325e-a2c4-66055c12b205 | -9.84492 | -44.88015 | 2025-10-30 05:55:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b01d22e7-8c24-3118-8385-90e58e7cf000 | -4.26224 | -43.70581 | 2025-10-30 05:55:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| bfc5ff1e-2e03-3126-ab97-1de9f96e6c58 | -6.5219 | -46.91182 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca93e71f-877e-31bf-a11a-4443d6c5b606 | -3.79264 | -43.89146 | 2025-10-30 05:55:00 | AQUA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8c71b7b1-ecc8-31c2-9513-e14f98f532e7 | -9.9333 | -47.15601 | 2025-10-30 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e65bb2cc-cc1f-3810-bc6c-b882fe82fbd7 | -12.50763 | -50.54659 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f4049f4b-13a8-32f0-be00-a1d9217f827b | -7.29954 | -44.96306 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 20d78f3f-0fa8-3ac6-a6e1-37de2e4be384 | -7.16635 | -44.99151 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73327278-7337-3215-81a9-adc6ad275f55 | -5.7036 | -43.15549 | 2025-10-30 05:55:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1170b7d4-53bf-3270-89c2-1ac67c1f8a73 | -5.69453 | -43.15421 | 2025-10-30 05:55:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 26427781-2e35-326f-8a34-dae253ebc5db | -12.50535 | -50.56033 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 2b7947f3-c108-329b-a77e-6a66467799a3 | -7.61572 | -43.58797 | 2025-10-30 05:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ba0ba92d-f077-3d84-a32c-e69cef78a518 | -7.60989 | -43.56234 | 2025-10-30 05:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d93cd073-d8e0-3427-9275-bd98a17243d0 | -7.28582 | -45.66203 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a924d3e8-ebb2-3d8a-b424-748df03dbb5c | -6.13414 | -41.69395 | 2025-10-30 05:55:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 953ffc3c-4485-3686-bb69-d2b3b7cf2ebf | -7.62477 | -43.58931 | 2025-10-30 05:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 0f5a75ed-c390-338d-8d34-d7a7d3e6fee2 | -12.47083 | -50.56855 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 605bc12a-849e-316b-8cf0-2f2301a3bbda | -6.11104 | -41.70649 | 2025-10-30 05:55:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 65099ddc-8be3-3571-8e8a-4f00092c394f | -4.46773 | -43.4477 | 2025-10-30 05:55:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1fe25a54-7246-38df-9809-d855d7ea2905 | -6.47867 | -46.88517 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a59d3ddc-d5d3-3c92-ba5e-683d9a973d15 | -12.2988 | -50.25742 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 216d6fb8-3a4c-36f8-8857-32018849008c | -7.79235 | -46.40945 | 2025-10-30 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 14cfe5f3-9ca9-3f29-b3b1-10464fb57f64 | -7.29465 | -45.66334 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 93cc14b7-7c32-3824-8c3b-b86953384067 | -12.11899 | -47.13246 | 2025-10-30 05:55:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 972d6528-4f15-31c2-a99b-e669807e1da3 | -7.08412 | -44.92768 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8bf3dfea-4a6a-33ab-a2a8-f535415a46a3 | -7.8799 | -46.74049 | 2025-10-30 05:55:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd2bc331-45c7-34b8-8769-6e516f25de62 | -8.04497 | -45.17519 | 2025-10-30 05:55:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d0cb9a18-448b-33fa-9795-a462c00208c6 | -7.7616 | -46.48983 | 2025-10-30 05:55:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README67.md)
