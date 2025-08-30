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
| b744f3d8-d4f2-3f84-bec8-1469a45725b4 | -7.72992 | -50.2692 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7c4bb0a5-e479-3834-9fc9-0065e2abdccc | -6.18068 | -43.33632 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 6da89335-b45c-3153-8704-b0849b5d82ee | -6.70623 | -43.09082 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bda51a19-a4b1-3d29-9243-e9944637862c | -7.96011 | -46.35661 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5875ce1e-f4c3-38cc-94c1-da440558aec6 | -5.22151 | -44.80102 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48ddec27-04aa-33ba-874d-ba3c80613b97 | -6.29475 | -44.46602 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 861b8bba-10b5-3e49-81e9-13f3af76e93f | -5.72743 | -43.93628 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b3339e2-0c5c-38ff-aafe-dfc60441102b | -8.12763 | -42.93578 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7bc10507-2be2-39de-b47f-f73d71491411 | -6.76978 | -42.99443 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2418b778-4915-3b8d-a1f3-6fabf7635bab | -6.94832 | -44.30845 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87519967-fb96-3fa9-894b-ed1b6da2ef13 | -6.942 | -44.06412 | 2025-08-30 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9c0390c-00b5-3539-be1f-f9894527a2b9 | -5.69576 | -45.96323 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7913fbc9-e1b3-3ce9-b526-e949bb950fb3 | -5.91558 | -43.35448 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f62cc4e-a9b1-32c6-8332-f52865fdc07b | -7.08091 | -44.28672 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03ed09cf-5c54-386b-9bf7-79212cdd9357 | -7.0535 | -46.24055 | 2025-08-30 04:19:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2816f386-62fc-395b-8725-fd261c8f23ad | -6.16762 | -47.27811 | 2025-08-30 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe8a7cb4-457e-35ee-b395-1cfafc785071 | -6.26634 | -43.83698 | 2025-08-30 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0744daa6-bb73-3317-affb-d00c422a191d | -5.75097 | -45.37406 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c596235b-0234-3458-86e2-531800f747bd | -6.83418 | -42.84678 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 159c35a4-fd12-340d-b301-f897319da81d | -7.15625 | -45.13614 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8902c14-80da-3840-8bfa-b1a81667658b | -6.42139 | -44.17665 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 64741905-c1a8-388b-8510-4cb4abe664b9 | -5.70004 | -45.13517 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d31a3054-e1ec-39fc-a386-34623e87e451 | -6.7633 | -43.79047 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e27b4fb-0009-31f2-aef4-3ad41caa1007 | -7.17063 | -44.14674 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab2817a0-3604-3284-aeeb-c5a580ce8e20 | -8.10917 | -45.00038 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 672fae88-3692-326b-8c61-9b254221b697 | -6.49965 | -43.53954 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 440acea2-d455-315b-9598-975dd77ccd15 | -7.9617 | -46.38966 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a6aa470-6068-3803-b941-ca6dcbaf23f7 | -7.71663 | -50.27406 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4b42085-91e5-38d8-92f1-7a337fa8b12f | -6.38533 | -44.69228 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d646a21-8582-30f9-9b29-e9f48f247a17 | -5.7471 | -45.37703 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc8850a-8fff-3ab6-bbd4-9ef78e57fef8 | -8.46814 | -43.63503 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9d37a2-fc80-3045-8a5e-75a79bf35ab1 | -6.88352 | -44.44098 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6b7ad56-a218-312e-847a-2a92fd025bef | -8.46082 | -43.63759 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57369f49-328d-3e31-9cd2-3e772553f1c4 | -8.10586 | -44.99986 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76334678-75c4-3f11-8d1a-10667fdf88cd | -7.90595 | -45.17079 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1954a5ba-43eb-3a73-8c23-79d02e5aa914 | -6.14095 | -44.18602 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 704ff8da-2b91-3b59-a1f7-ca8a78454994 | -7.59694 | -42.72142 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9fc45a90-8b53-3f3a-bdb9-0d2ce8487d6c | -6.00357 | -44.72039 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ccfae739-35ae-3668-866e-f1093d3856da | -7.20792 | -43.70624 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5053ae68-848c-33ff-919e-a8555ec866db | -6.80224 | -43.03361 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d2be396c-d3a7-33f9-b052-01335042ac84 | -6.5984 | -43.64928 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d480391-4366-39d7-8c2e-47608bd52f1a | -6.56663 | -43.67733 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfd99428-d6c6-350f-b044-a7020704f277 | -7.04061 | -45.82607 | 2025-08-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d46793c1-0f58-36f8-b511-86a3a66af203 | -6.17299 | -44.1982 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 55864f61-1776-38c4-82ef-4847b9ee9cbf | -6.16691 | -44.1937 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3775d2af-3fc4-3181-9e24-e88382d6616b | -6.30877 | -43.73881 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83a5129e-d2b4-364c-aa9d-871cf5dbe3c6 | -7.20065 | -43.70879 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d20ee99-670d-3a6a-a4a7-f6a09028c69b | -6.49033 | -44.38998 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89e7a68f-c432-3eaa-819e-6b1c8c0c76ca | -6.18627 | -43.32237 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf1f6d82-4f4f-393a-9ed1-07efe3b31b98 | -6.9938 | -44.36558 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e94a7b4-80a8-3aa6-8e5c-ff7a543f9149 | -6.49853 | -43.54675 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 482e837c-dc3e-344e-a455-99854fd03f8b | -6.62116 | -43.73987 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4e61915-ef7c-330a-ab57-a748dad2dfb7 | -4.50306 | -47.29086 | 2025-08-30 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db915a25-1a22-3953-ab83-96b57de7422d | -5.61491 | -45.00505 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6f57cbcc-ecfc-3226-bc70-325af8a034ee | -6.53902 | -43.10431 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb314c15-a0db-3d38-89ef-6a5effc38651 | -6.56165 | -43.68739 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb3a832-4b08-309a-a8c3-976eeb8a3126 | -6.34084 | -47.73095 | 2025-08-30 04:19:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca295221-fed5-3089-bb13-fc715b7808c9 | -6.59449 | -43.65237 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8265e055-f7a2-3826-85d1-688c904eba68 | -7.47964 | -45.99747 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6817b7e4-563c-32e4-8339-8ef2abf1c772 | -3.8155 | -41.06485 | 2025-08-30 04:19:00 | NOAA-21 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8e06d1f5-8766-38d5-ab4e-ddf0a556da46 | -6.3127 | -44.10927 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbd5d4b8-66c9-3042-89e5-d819916df706 | -7.59523 | -42.70927 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d35e007b-b896-3bb4-825d-8fbfe12a5c65 | -6.36357 | -44.45895 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38aedc8d-5fe9-304a-bad2-2c9003aeb523 | -6.62171 | -43.73632 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ecdc606d-c0b5-3ca3-a456-fec66dd8fe72 | -7.20121 | -43.7052 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8a484ef-52f0-3266-a8a7-bf5cc027c275 | -6.59895 | -43.64573 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ad49184-db37-37b9-a461-f94de9c870bb | -7.43251 | -44.80456 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f05cf79a-e452-3052-85ef-8c38532ab507 | -6.69711 | -43.08195 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2df1441a-b3c0-3466-b46b-08a23888aae1 | -7.09634 | -44.60255 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81260fbc-ad8b-3385-b271-3d343df4ab24 | -6.38247 | -44.33774 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eab1d1a9-124e-37cb-af71-45188179ddf5 | -5.87774 | -50.28968 | 2025-08-30 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47c8339a-9767-3a66-857a-2198d77a441c | -6.54242 | -43.10484 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d74104cb-55bc-30c1-b331-e32585445507 | -7.11986 | -44.60623 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4f57457a-fea4-3308-aa87-fbb26a8673ee | -7.21773 | -44.06032 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b54e6269-533f-34ac-9e7c-f507ad8b927e | -4.87753 | -45.51918 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b98401fb-3187-3486-8b50-377f67fe2b4f | -6.18349 | -43.34044 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a46b21d0-e3d2-35ae-a911-ce99d283f83c | -5.80032 | -42.5675 | 2025-08-30 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 69c64c80-50d3-37be-b7a6-5d3814516012 | -6.29888 | -42.79512 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 74742058-2db8-3030-bc7e-8ca3e75777f0 | -8.12364 | -45.05946 | 2025-08-30 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aeafec1-c4af-3565-9345-774636662df2 | -7.59405 | -42.71701 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1f9cca89-2960-3c3c-b462-ad87bad60589 | -6.1902 | -43.31931 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e9fdb0a-db2e-3441-a07f-bb5a9c683031 | -6.2125 | -42.76288 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6b49431e-cb83-3ac3-90bf-e5fe842289f2 | -7.75819 | -45.46254 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22631670-3b2c-33f9-8137-9cbd8f5c5bda | -6.5956 | -43.64522 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ee16ee93-1645-306c-972c-53287383dee1 | -7.59057 | -42.71645 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00de5e9a-8485-3b79-a738-c27e631dada5 | -5.91524 | -43.42398 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8934568e-cfab-3aea-b026-3f14bb676dba | -7.58633 | -45.12693 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcf2150b-9fac-3005-939f-22bfddc74e49 | -4.64494 | -41.39481 | 2025-08-30 04:19:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f3c2179-2938-325d-be9b-f950c499b26b | -3.35987 | -43.37137 | 2025-08-30 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a191c18-19b3-3850-8812-52945628c83d | -4.1448 | -38.27168 | 2025-08-30 04:19:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4bf348b-5e67-31be-b583-a867afd1d6f8 | -6.24165 | -41.81731 | 2025-08-30 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 61a9084a-a585-36b6-bf32-0e3bfafa792d | -6.95198 | -44.06568 | 2025-08-30 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c94f8766-38be-3f91-bd17-da38d60593ac | -7.15114 | -44.9052 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea762eab-332c-3f72-856a-6b68fc2fe467 | -7.77527 | -45.46168 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 306b6dd1-3e2e-3d24-99ff-052bb093b7e1 | -7.78408 | -45.4702 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f82a6340-2cb3-385a-bc2a-c45733c1718a | -6.28868 | -44.46152 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4af26e26-0fdf-3436-afd6-f183d28bd445 | -7.08647 | -44.29476 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cba41514-8ade-3dc2-9683-6d71159e9aa1 | -7.1506 | -44.90866 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7843f9e7-49f0-3ed0-8916-204510c0b5b4 | -6.49796 | -43.52821 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f164935a-e948-3c22-91a4-dd255d31b70c | -6.17671 | -43.31721 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README20.md)
