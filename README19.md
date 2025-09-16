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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c51b0913-c6e0-30a1-a1b0-da1b6c72b3e9 | -9.04628 | -44.84627 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3761c4a-9975-3e81-b010-9de9ea104a8c | -8.96449 | -46.03372 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9a356d3-fdd6-399e-9129-765e4b68db8f | -5.55023 | -44.96898 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41718b23-fd3e-3574-b9a6-24fdbf1c6968 | -7.56448 | -43.95399 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e18f012f-f5a0-3ed4-a875-8ba0065ecc53 | -5.89902 | -45.73185 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8306b24a-a66b-3bd7-a90f-32d8561a5db6 | -6.75914 | -48.11555 | 2025-09-16 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96ef0041-edae-35bf-88c3-25ed2136bf82 | -8.41809 | -45.75143 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 882d01cb-c7df-35fd-9ff9-92f9497b88a9 | -7.67831 | -46.28688 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 166af7de-7234-3a70-a3c0-48eb5a9bb0a8 | -9.05545 | -44.83807 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82a8604f-f9c3-31d3-abbe-b0919c7ca544 | -6.34673 | -43.15841 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cc8582f0-7058-32a6-b3e8-08936757599e | -10.78326 | -49.13716 | 2025-09-16 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be3c2f5d-e269-32cc-9b03-47f4231b0026 | -7.20718 | -39.96235 | 2025-09-16 04:02:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b95cc32-6ba7-3d84-aa33-71c049c11485 | -7.98622 | -45.65856 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83fe4664-4726-303a-a32f-1c32ea6ad7e9 | -8.08755 | -46.82867 | 2025-09-16 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56d4f75a-af4b-3516-8c4c-2dc903cdf521 | -7.44451 | -46.17846 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a84ec474-f619-3e5c-8bc8-3d0f0b738f31 | -5.97324 | -45.85707 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdcd9e40-2228-38b0-9142-88c43b7f7650 | -7.99725 | -43.83248 | 2025-09-16 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| de09d9d0-5b7a-3307-9f79-20e261b2f261 | -11.69916 | -46.88974 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 280055eb-2e69-39bc-a84c-9e8fff7e5d0a | -6.09404 | -46.49929 | 2025-09-16 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6faa088-9a00-346a-9edb-b6fd6068bbf6 | -8.18974 | -47.12779 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9c358d85-8fde-391e-82f6-08b1b78a1661 | -7.93432 | -47.65029 | 2025-09-16 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4885a92f-97d3-3214-9e18-ec9499e862d0 | -11.02533 | -45.06049 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fea2e5ee-b0e3-3943-b985-15dbdb9195e5 | -7.25267 | -44.48221 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e15b3d18-6fb8-31b3-8d3c-1dc6abd1b0bd | -11.43947 | -43.5442 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a491f04-32f2-3827-995b-b3cf8c4d9d08 | -8.09061 | -50.15316 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 031d79d1-4e1a-30d1-94f2-54ca2fc3e50c | -8.5896 | -46.34772 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcdb14d1-4d80-3138-ba62-48858b3540b9 | -10.71621 | -44.74002 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 94fbad01-f67d-3371-8737-a3c6fe785885 | -10.64428 | -46.45622 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 575f51b0-73d8-30f4-886e-70ee99996d2a | -7.37289 | -44.29429 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b1396bf-b45f-3097-b2cf-f824e6119bf1 | -7.66498 | -44.47939 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 422602b8-0ad8-345b-883c-109da10c9507 | -8.09121 | -50.14986 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4290e26-8fe9-3b55-9f72-326a200232cc | -5.22835 | -43.70085 | 2025-09-16 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6c784cec-f436-3e9b-a616-e5518e84c541 | -9.54293 | -46.29466 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11bc064e-de13-3911-9a98-0cb1938e2d97 | -6.18095 | -41.20566 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0c484c2d-3acd-3dba-b0ae-1f5665767415 | -6.1733 | -45.14511 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2defa331-5dc2-363c-b9d9-7a77e19f7364 | -11.45843 | -46.922 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 42576c73-8be9-3cea-9570-59f2a9e1c7ff | -8.89274 | -46.15614 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dad77ffd-daf5-3c69-a626-e8edf1c0a1c4 | -5.34608 | -44.81242 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83d466fc-6d59-3664-8389-c57bef7ac475 | -5.76438 | -43.93767 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07849c29-1287-310c-851c-599316e63bc6 | -7.66879 | -44.47997 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86b6f51c-e9a6-3b2c-b13d-e7d95ff6b61c | -6.52809 | -41.82167 | 2025-09-16 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e2363b6-4d8c-31c9-97a5-19b40076e46e | -9.21499 | -44.50906 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7342d656-a6e1-31c1-95fa-c233f3a73b52 | -5.34381 | -44.82632 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bc80b30-8797-3c42-a01e-ddbfe9a5d694 | -8.9818 | -46.24536 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5713a8f1-0e4c-300b-8279-d9e44e0bc8b2 | -10.72433 | -44.75982 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 924c02ea-e2dc-3a97-854f-97f725eeb04e | -4.85507 | -46.79255 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 154322b8-d7be-302b-8c4c-bfba8170d717 | -8.60001 | -46.33732 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f62754e-5a70-3d70-8a8b-07aa8d7c3e36 | -8.60481 | -46.33752 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d88f1ef1-5b04-36fe-a79b-05279ccbd786 | -7.30557 | -43.92765 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88d96da8-6e72-3d5f-8693-141a13af607a | -6.97435 | -44.53931 | 2025-09-16 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8de2fe29-1761-39ad-b1f4-9360ac6f65fd | -6.27406 | -44.00269 | 2025-09-16 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 494b1cdc-1371-39c1-b577-fcc2bc2a9105 | -7.2785 | -46.58681 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d024c3c-287c-37c2-b99e-e6c1905d2c7e | -5.28624 | -43.21519 | 2025-09-16 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| daeb2ac1-bb0a-3500-bdac-9ec8354e0be5 | -5.5684 | -41.18493 | 2025-09-16 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92d17340-cf35-3d8e-b9b8-2cfee8ad4d53 | -9.14486 | -46.94377 | 2025-09-16 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd83012a-80ea-3a6f-8c39-1a47662d31d9 | -7.68051 | -46.29962 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26ed51e0-f784-37e0-be90-1a325aaed1cc | -6.82446 | -47.86287 | 2025-09-16 04:02:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0367b4a-70d2-3a89-884c-47d9c2c36386 | -5.53996 | -46.41154 | 2025-09-16 04:02:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eaa5310d-2c1d-3fca-bcab-86509868deb9 | -11.49303 | -43.72987 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3a5fb4d-ce28-308e-94d6-39307187b0c7 | -6.50118 | -43.19497 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d620b21-584e-3f08-be9e-0873c977abe1 | -6.09479 | -46.49491 | 2025-09-16 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a72f66a-1ed4-33cf-b76b-08ade4b026cf | -8.66816 | -46.37225 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8114a289-bbd3-30ed-b650-fd96ff17fa4d | -10.727 | -44.75832 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7373c5a5-06cc-3a0b-9b59-5dd72b192ffe | -10.67218 | -48.68777 | 2025-09-16 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7894a2b1-00fe-38c5-8da0-51e0b34c6586 | -7.48505 | -46.12003 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4627d09-055c-312b-ac35-60ec78282e29 | -7.46406 | -46.14098 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50d1dda3-f8c1-35eb-88c7-cdb93c530d91 | -5.22718 | -43.70245 | 2025-09-16 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 12b7d63a-41ed-3f08-a37f-97c8d4b5cb1e | -8.61136 | -46.39935 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38f1426f-4e0a-372f-bb76-08a7a605f773 | -12.11053 | -44.82443 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf393612-0619-38f4-9f4e-61ae67054b7f | -8.93095 | -45.51232 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fe41d43-f67a-3197-8560-0eaff129efb7 | -8.61966 | -45.7234 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dd0f591-be95-3ca5-8ae2-3cce2caa98b5 | -7.71143 | -45.30753 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ae811c53-ed35-375e-b2a9-d30e0a90128b | -7.81128 | -46.12035 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f16c3de6-7de5-3b86-81e6-a39b276a732c | -6.16994 | -41.17078 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6b4e033b-9974-3890-8dea-42b1c789216a | -11.99766 | -46.67216 | 2025-09-16 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31b8301e-7c3c-33e5-b8f7-611d8d86ea53 | -11.12638 | -45.33432 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c98469e7-ebca-38dc-a9be-2cd4beaeb520 | -5.74249 | -43.92947 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d88c00a4-7050-3c4c-9821-7106293d7f47 | -10.71472 | -44.74898 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cd162c9c-49de-370c-b78c-733445231afd | -7.13931 | -47.97567 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 413cdd4d-6e88-3c8e-9459-c156338628c8 | -5.05254 | -45.20162 | 2025-09-16 04:02:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba32e5d6-21c6-3c93-be05-9e3b1de5e858 | -11.44246 | -46.93903 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c30e1496-f286-3e46-b5f7-4677f41bf7c1 | -8.11865 | -48.2669 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 37d65bce-f29c-3f9b-a3f4-282613a49706 | -8.13171 | -43.65386 | 2025-09-16 04:02:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 374efb49-8cc3-32d6-a641-c652c1d1d63a | -8.91459 | -46.15289 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9edcb7b-035f-3cac-8edc-3bbc1a650127 | -7.42648 | -40.08223 | 2025-09-16 04:02:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78449112-22ba-3b73-b709-320d35ff7547 | -8.95875 | -46.01777 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a09cf45-14ba-39a5-bef1-0f55a5721911 | -11.24222 | -49.94875 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 93520316-d855-396c-8dda-f1d446e48dce | -7.13744 | -47.98625 | 2025-09-16 04:02:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d210ca00-f64e-344e-9a9d-4511458abcf0 | -11.12475 | -45.34392 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ae3efd3-0a93-3195-9daf-64e9932c47b8 | -6.00963 | -42.7083 | 2025-09-16 04:02:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 80073a4b-7b02-39bd-a747-2b72bcb10fbb | -11.5013 | -43.72318 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b959c9b1-e30c-3648-8df2-d1f06c763c04 | -9.05568 | -47.01814 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac1d2d41-f9a9-31d8-a5a6-93f9d83ec232 | -7.44305 | -46.16173 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a4088aa-71eb-3477-b780-2237ee847e73 | -9.09419 | -44.83769 | 2025-09-16 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d9f69461-9f51-31ae-b6ae-4364ba23b96d | -10.78664 | -45.97616 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26112c88-7d1b-3243-8125-261e924961c7 | -10.72328 | -44.7578 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5995cb50-f7be-3938-82fd-45b0026ca847 | -5.73882 | -43.92561 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 187566ee-9dcf-37b4-b3cd-f9389a5e7777 | -5.67496 | -45.05208 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0091ed6-cb58-3476-823b-5fd7c6e2fc72 | -10.79059 | -45.97697 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26e8aa97-f256-3023-9f76-48cab7c0953b | -8.66393 | -46.37159 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README20.md)
