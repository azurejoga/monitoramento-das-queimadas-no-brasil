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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3879ee5-2b31-34ad-a586-a1f8584b205b | -8.521 | -45.69048 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb8feadd-0886-3104-9478-e4178b3200dc | -7.33377 | -49.61522 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b92e8167-8920-30ff-9d20-a49ec3cc44fe | -5.68334 | -43.33342 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bbb71db-73ab-3eb0-9db4-5e1e4486e3c3 | -8.52411 | -45.69889 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0908abdd-383a-3d6c-ab40-5f1c69fbeb38 | -5.59547 | -45.36003 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff272e42-daa8-3b12-898f-96f2bc5c8cb0 | -7.31002 | -49.61153 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80448494-17e4-3b44-991c-43fe52bf33ca | -8.0435 | -48.67697 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83b10756-6dff-3397-8545-9820ef212bb1 | -5.73808 | -45.29793 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a7c01fd-1691-3b3c-8b6c-da16734969ee | -7.46137 | -45.28931 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 157cdd0a-6422-343d-be0b-6ba1c5ea0d3f | -7.20464 | -44.95167 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f20c23b-9edc-3fcf-93b2-85c5610466df | -6.42796 | -44.49019 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17c33a29-f91b-3775-9af3-47f9330307a1 | -6.41392 | -44.49263 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 239e87f0-f6b8-38d3-92e3-f79db93ce52d | -4.93506 | -55.81326 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28941716-0b19-3599-9ddd-debf17201400 | -9.05343 | -46.97239 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c741b96a-bc6c-365f-b6e7-0a25fd413946 | -6.86097 | -47.91879 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e5f3813-3c37-369b-82cf-f139574d1faa | -5.7625 | -45.5212 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 962c1bd8-780e-35b2-a40c-5ef7fcb691df | -7.09883 | -50.75868 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1798c660-4f2a-3e4d-b7c1-adeb27dad04b | -6.43241 | -44.49096 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 04b405c4-dc00-3c5a-9e6c-759325142308 | -6.28963 | -42.19837 | 2025-09-11 04:44:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1d7b2bc9-9965-3c72-8c2a-493f7f6bd384 | -8.52467 | -45.69505 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5969dab8-cd7d-3aff-b315-e84ce4b84411 | -5.22107 | -45.42598 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4ef2970-fc01-38cc-908a-2d7c4f26dc5e | -9.09988 | -46.95729 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 877f2063-f677-320c-99ef-92c455c5a9b8 | -9.10704 | -46.96328 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ebf2a34-6d40-3867-8527-6740d2852295 | -5.65784 | -43.8969 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1561a014-ccbb-3945-8d2b-80c006ec166a | -5.60213 | -48.11703 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b168cd8-2fc0-3da3-ab28-0ebda0604c71 | -5.52761 | -44.34657 | 2025-09-11 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a696d227-7605-3109-84de-be5ebc6daa4e | -5.59504 | -48.11599 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e361156-b562-3e56-8609-5d6c7e49879c | -2.22144 | -48.22511 | 2025-09-11 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17187426-d0aa-315f-b8bf-d3835e73234a | -6.25172 | -43.42369 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0fd2ea6b-a0e6-3769-a909-74c23b406dbc | -8.04224 | -49.04935 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e6f22eb6-8cc0-3e79-917c-f93994855667 | -7.50451 | -48.27877 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8974302-ea66-3dfb-b78f-5cba7d587525 | -4.87057 | -42.76498 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6a73bc76-ac1a-3c1e-a9fc-f9cf7dbfd24c | -5.97341 | -45.81308 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf33b02b-b671-31ed-9c96-2050e791aea2 | -7.4674 | -45.27792 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74f51922-303f-3e74-bfa3-8d1890292f03 | -8.44584 | -47.27098 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faf59215-3358-3ce8-8455-948843f38150 | -6.67387 | -44.12302 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a2356f5-c438-3a0b-811e-233c5e8992f3 | -5.36709 | -45.96713 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a745b6dc-cb70-377e-977e-6083b11539d9 | -8.07743 | -52.38517 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 753759e7-5389-3392-a796-0adfe7938d46 | -8.01811 | -48.65332 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6e1a25b-4570-3a0e-8a5d-9908209aa05c | -7.47427 | -45.2911 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3cdd17c-6ee7-3bce-9289-c65056b028bb | -7.42603 | -45.87196 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 042f072a-c05a-3d9b-be43-33f1399c0c16 | -5.52697 | -44.35097 | 2025-09-11 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00d5d92c-7dc0-365b-aeee-15eb58f56456 | -7.65217 | -49.50158 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 746c62dc-edb2-30a0-b954-27e84e781f86 | -6.2346 | -46.15611 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 970dba50-1c43-3493-a7c9-ad74612f7ce9 | -3.68873 | -49.57349 | 2025-09-11 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26909e38-cebb-33a7-afd2-49299d33e38b | -7.84563 | -45.40295 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 760a3cff-aa2e-3e51-9bf6-d125916f6173 | -8.07099 | -42.95285 | 2025-09-11 04:44:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 893e3174-5d77-33aa-af65-58797cc75796 | -3.79551 | -51.15868 | 2025-09-11 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ccfa2286-e6b9-31c3-93b4-babeab4c8c74 | -7.23598 | -55.06079 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 521692d0-fe5d-33ed-bd7f-78dad45e0f1e | -7.51395 | -48.27931 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce594144-f83d-3ebc-820f-ff79cfe81ed9 | -9.07283 | -47.08634 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bd84e371-36be-3af8-8a91-37af22eceaed | -7.5847 | -47.75437 | 2025-09-11 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711d744c-40b4-3672-8875-c489c9dd6772 | -5.56133 | -43.05252 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22ec056e-c54b-3e56-b656-45934646e811 | -6.83321 | -47.9063 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9742c8de-ecde-3078-a3a7-5fce1f0861b6 | -8.02323 | -48.9994 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36b2cfff-6326-39e7-8699-2267bb53327a | -8.07604 | -50.17641 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d0bf9eab-4a8e-3410-92c7-7fa3f4fb940f | -7.91865 | -44.85055 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aed4479c-7fda-37c5-b720-5998212ab826 | -6.54447 | -43.10819 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba69f1b8-e223-3a99-9d96-1443b40eda72 | -9.05605 | -47.06454 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3acb7173-9659-3364-b39e-05aa314fe73d | -5.65226 | -42.62008 | 2025-09-11 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 913ab82c-0d51-3163-82bc-9ea5fb016012 | -6.38285 | -42.58963 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 39c3250b-cd9f-3dd5-a597-6ec56d284e15 | -5.35439 | -43.41035 | 2025-09-11 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b459ffe6-72f2-3728-9c50-1bb552cbf652 | -7.37625 | -47.42353 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2b495fa-c82c-3c9a-ad06-156669d07c46 | -5.24784 | -45.97573 | 2025-09-11 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0323ea6-d47c-39cb-b7ec-24edb0037003 | -8.56923 | -45.5903 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3eb24e9c-4637-3c3e-a779-9057a1c0456a | -7.42343 | -45.87169 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 478ff153-41b4-36fb-b755-81516723d57d | -8.74695 | -47.12247 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 964f5c8e-31ab-32b8-a68e-47fa1462c80d | -7.75923 | -50.7699 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b422c9f3-fd58-36b7-bdb3-6ec0139bc0d4 | -7.39395 | -50.89107 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17a267b4-b0f4-3e3f-987a-9ca76f38ceba | -8.04166 | -49.0532 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e27f7ec5-1f8c-32ce-bfa5-2434b0562842 | -7.4809 | -47.05424 | 2025-09-11 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6711d323-d863-317f-816e-8009d1e04a08 | -8.79595 | -48.09291 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03d80c9b-63f4-3134-ac41-a983410a21a9 | -5.81015 | -45.68157 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09ab3f4f-9e7d-39fc-a6ac-6a773d9289e3 | -7.49688 | -48.25667 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67162d21-a782-373f-b6e8-12b26d0aeafb | -5.86109 | -44.21052 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77cb450b-e145-353f-b3d6-40b493b0d09f | -4.86798 | -42.76838 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b96a8d2a-34fd-3953-8471-bb8d727ad3ec | -8.72727 | -47.09446 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 58b1bc1e-440f-36b9-b89c-3afa4f01bb53 | -6.39682 | -43.50156 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 614db122-e65a-3f53-9597-2125b3cfdce3 | -7.65887 | -49.84343 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 239e23db-1798-3017-b632-bec708c690e3 | -8.0716 | -49.71193 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2ccd945-c3c6-34e9-9a5d-88744ec4c86c | -5.81477 | -45.67859 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bb84d24-979c-3d57-9a7a-4f8e789b4069 | -8.02309 | -49.04687 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90a86930-5256-313e-a1a5-765770731357 | -5.25088 | -43.76553 | 2025-09-11 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20538507-de22-395b-a32a-2663667b2223 | -7.85289 | -45.50529 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d046c12-945c-3a40-ad0e-dfe0e8e333c2 | -6.54267 | -43.10725 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55f2f47e-4145-3b2c-832b-c74a0c2157b0 | -6.31185 | -43.41295 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 409aa8e2-a8d2-343b-954a-2ae82d34e6be | -5.93281 | -45.72256 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24eb370f-5e81-3a73-be57-0992d7b7206d | -4.92359 | -55.78231 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2d2a16ec-a776-3553-9f40-6b45ae16ef26 | -5.72419 | -45.61702 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb6df25b-b862-3f2b-9075-4160e534e255 | -5.7518 | -51.69708 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe8cd33f-b976-34b9-bfbf-791c4df6fd81 | -6.31372 | -43.81943 | 2025-09-11 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56abbaf1-501d-388a-8084-a19ee2db8e3a | -8.1704 | -46.06551 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 28b87cbc-ea40-334e-86b0-fdf7bb9569da | -5.40631 | -45.93694 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1fde8a9-dccb-3f97-bd75-f7d816bfed3d | -5.66311 | -43.89285 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd439006-4874-3592-b053-9bd8036a2a15 | -8.02191 | -49.05454 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c65b5945-1ad0-3d94-bc5e-2239400e4c9f | -5.60273 | -45.78782 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96e08e69-6306-37e2-9e2a-8f0e893a02c4 | -5.52633 | -44.35537 | 2025-09-11 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75094740-c7d7-3181-8d03-e1df49f9d42d | -8.16206 | -46.09486 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ace23654-a8b9-3296-bffa-da0ef64b2448 | -9.08065 | -47.08747 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c285c96e-55ee-3230-a536-41c3386640dd | -6.55401 | -43.97749 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README88.md)
