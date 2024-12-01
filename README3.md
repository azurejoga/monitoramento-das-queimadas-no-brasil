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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d9a5ba9-aacd-3779-8d8e-77618fc07b26 | -4.556 | -43.3261 | 2024-12-01 00:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f61b3b9d-15c1-3cf3-9eb4-1e68e8d4bb2e | -2.3375 | -54.6234 | 2024-12-01 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 3055dbad-3211-303d-886f-4e55388685a1 | -4.5394 | -45.7019 | 2024-12-01 00:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 150.5 |
| b51ca889-7069-3000-abec-36ff99780769 | -4.5765 | -45.7222 | 2024-12-01 00:30:00 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 0c6f8274-5072-37a8-881d-457ee87e23e3 | -2.6578 | -51.8811 | 2024-12-01 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 75675a2c-4611-3c7c-a03b-7946a692a6cb | -2.8196 | -53.0629 | 2024-12-01 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 443cb095-5ef8-348f-9689-37cb924c5057 | -3.2057 | -53.1341 | 2024-12-01 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 65ea1b44-de12-3aaf-b6bb-e7286830096b | -1.7139 | -46.1422 | 2024-12-01 00:30:00 | GOES-16 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b8ad849b-1ab8-3ff6-9ca5-146fa369529c | -2.6579 | -51.8606 | 2024-12-01 00:30:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c972f1d7-d510-363a-b81b-ea4072447aad | -3.457 | -50.2572 | 2024-12-01 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ca5a6470-8e2b-30df-bd87-9563722d0775 | -6.9158 | -43.5185 | 2024-12-01 00:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 3d663547-da06-3f35-bf58-bbb89190fa8d | -4.558 | -45.7008 | 2024-12-01 00:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 98.0 |
| a5825cbb-727d-33f0-b1e5-b443ff0a768b | -3.2775 | -53.6181 | 2024-12-01 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| aeb7ef17-511f-3670-b63b-cffe802fe039 | -2.7503 | -51.7553 | 2024-12-01 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| a140e423-9700-3f1e-aeec-c13706ddaf6c | -3.2591 | -53.6186 | 2024-12-01 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 6df3bfa3-ff93-34bf-ab2a-d99df07dbaf6 | -11.69218 | -44.62674 | 2024-12-01 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 184d7e2d-f741-3274-af3a-16de8bd15f87 | -11.83403 | -44.2305 | 2024-12-01 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a310e9a9-3f6b-3522-b2af-6b2159c78244 | -12.82832 | -43.88983 | 2024-12-01 00:30:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de397138-5d51-3495-917c-4e4072f53cca | -4.55895 | -43.30577 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| ee67529e-f927-3e1d-aa49-a24df2d53742 | -6.18813 | -44.43093 | 2024-12-01 00:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f63a8b0a-ed01-3010-bcf8-f082791fd938 | -5.52348 | -39.16098 | 2024-12-01 00:32:00 | TERRA_M-M | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 0700cff7-9830-3f50-b309-03cec1fca419 | -4.90426 | -41.31287 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| e10f687d-a4b8-3695-a804-29a1460bee86 | -10.66435 | -44.4912 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c2d789ac-cf0d-346b-9b11-73ed513fbd4f | -5.18274 | -43.94856 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4955cb51-dee5-3ebe-b0df-a3600416656b | -4.15031 | -43.80862 | 2024-12-01 00:32:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 869a247a-a2b5-36e2-ba43-551706eaa8e5 | -6.11646 | -42.19244 | 2024-12-01 00:32:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f1dfd2b1-705b-3604-a075-22b595c507e7 | -6.92131 | -39.27701 | 2024-12-01 00:32:00 | TERRA_M-M | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 55b0f007-7477-352a-a257-fcbdb2463ee9 | -4.4463 | -45.3556 | 2024-12-01 00:32:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c80cf19b-adc0-3130-a740-d958a20e7eb2 | -10.52368 | -42.42894 | 2024-12-01 00:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d424539b-b2ef-39a8-9802-bc7eb931f122 | -6.28278 | -43.84789 | 2024-12-01 00:32:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 375efaeb-4830-3269-ba15-885da5566e8f | -4.80293 | -44.99887 | 2024-12-01 00:32:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0354531-66f5-3479-ae7d-c67824127ef6 | -6.92494 | -43.56876 | 2024-12-01 00:32:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4dcb8f2e-ca6c-38cc-9e82-1db876b0c73b | -6.41985 | -35.18691 | 2024-12-01 00:32:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| b21e98f5-cde4-3b38-bd23-3563539eb46a | -4.30976 | -45.09841 | 2024-12-01 00:32:00 | TERRA_M-M | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ee68aca3-3951-3aa4-845b-e029c53fb859 | -4.26585 | -48.36334 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e7f36e1e-2906-3eab-bf60-91bbd4c3efe8 | -4.20949 | -48.11841 | 2024-12-01 00:32:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2726f9a8-670e-3c6f-b55f-e7acd351a1ab | -8.93315 | -44.25012 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e3afedda-54f3-3aa6-96ba-fd6ff4b29447 | -5.18398 | -43.9575 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b22f97e5-5432-3861-90da-4eddebc2d276 | -6.86618 | -47.24117 | 2024-12-01 00:32:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 555f9de6-1d36-3c18-b563-654cd0c77903 | -4.54458 | -45.72445 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ff38d93-d81e-3969-9552-95c892d42bec | -5.96739 | -42.70887 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 145b8475-a38b-3cca-9ed9-9477db22feb0 | -3.90868 | -42.41049 | 2024-12-01 00:32:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| be4913d9-ff8c-37d2-9cc7-f1fd397895b1 | -4.88556 | -41.31574 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 08ec44e0-746c-37f3-bdde-a94f63bfeb84 | -5.54132 | -45.43172 | 2024-12-01 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 22178e57-b3c4-3678-acd3-980986535db3 | -6.635 | -43.60042 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 50ab6333-ccc3-35f4-bbae-7691c05d0423 | -6.59594 | -44.18372 | 2024-12-01 00:32:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 333a132e-c2c9-375f-9395-ad317a6c0f7a | -3.69298 | -43.4297 | 2024-12-01 00:32:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| cc40b459-7b91-31a2-a59a-23a47703b28b | -4.44763 | -45.36533 | 2024-12-01 00:32:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8ee78c14-37f5-34df-a16f-7a8ce7187b51 | -4.89633 | -41.3242 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 76b8f18b-9dcc-34be-9298-24d0c89f8cd5 | -4.74501 | -43.70874 | 2024-12-01 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5000273b-d31b-3824-853e-9e2cec2f9fe5 | -4.66781 | -44.95673 | 2024-12-01 00:32:00 | TERRA_M-M | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5f4a9301-22ec-35ac-9fc4-cc83a6dddd72 | -7.0265 | -44.85105 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 86d82522-cd79-3162-9aa9-d68fed3e022d | -6.91232 | -43.54316 | 2024-12-01 00:32:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6e48fc42-49b5-30d4-9a98-fb66221a9841 | -4.55009 | -43.30703 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 056ca9fc-74e2-3d12-9f2b-ee5c22a9d82e | -4.77701 | -44.81138 | 2024-12-01 00:32:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3fb4e72-fb64-334d-8d81-365c31f10cac | -3.8628 | -43.068 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 129f10b2-6cd2-3cd2-bc39-2c383df8220b | -8.94234 | -44.24881 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bf0ca558-a65f-336d-b7cb-5d85de09e795 | -10.65623 | -44.50278 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 91f6b91c-40fc-3a4c-8af3-98a6d63323d7 | -5.50333 | -42.8784 | 2024-12-01 00:32:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4ed25154-e49d-3da4-912c-648392429fda | -5.65836 | -39.7388 | 2024-12-01 00:32:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 1eaf3956-bec1-34f7-825a-474edde20649 | -4.72343 | -45.68703 | 2024-12-01 00:32:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 935d4d5b-ba48-3a45-83e8-9d6c7aaa3044 | -5.50209 | -42.86953 | 2024-12-01 00:32:00 | TERRA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 440ebdf1-8727-364a-992a-80567a4e0465 | -7.38072 | -45.83494 | 2024-12-01 00:32:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b8e5c4f6-bcf5-35b5-be7b-66892c96377d | -9.80448 | -36.96756 | 2024-12-01 00:32:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 8a40d45a-5496-3843-99b6-e8a5b1d74697 | -4.81531 | -47.33043 | 2024-12-01 00:32:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ed037d69-996d-3fc7-837b-fa5a9d913348 | -4.81359 | -47.31768 | 2024-12-01 00:32:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 18ee6e42-a5e8-368d-a58f-55d5ae25bd6d | -4.55539 | -45.73308 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 344ae4b9-61cc-3a48-ae5f-16816747ee75 | -4.73545 | -43.2505 | 2024-12-01 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 278ad0b8-c816-3e74-9966-534787db2a94 | -4.55132 | -43.31587 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 51bd3d53-53b5-3672-b56d-619f4f54b06e | -6.06197 | -41.93862 | 2024-12-01 00:32:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 33170d91-62b4-3df7-b273-74835f1195cf | -4.55772 | -43.29694 | 2024-12-01 00:32:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7162058b-ed2b-3c89-9059-0b362374edd2 | -4.684 | -46.80748 | 2024-12-01 00:32:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 08bfe7df-4af7-3ff7-a32f-51843293ae2b | -4.88698 | -41.32566 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 630965cb-6e95-342f-94f3-9e37198173aa | -4.54178 | -45.70425 | 2024-12-01 00:32:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 151.4 |
| f6a5ff07-360a-3d91-b247-af2ced440a43 | -4.32097 | -48.09711 | 2024-12-01 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 80904389-8d5e-3000-84d2-3c4caf4cf9e0 | -5.6108 | -45.05562 | 2024-12-01 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 640aea83-9cd5-3340-9948-8f793f292f09 | -4.88268 | -41.29574 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 9517bc7e-1561-31cb-b07c-062020365e04 | -6.18687 | -44.42173 | 2024-12-01 00:32:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63fa1f77-bafe-33f8-a1a0-5796952b8a43 | -4.84115 | -44.4775 | 2024-12-01 00:32:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 51069deb-66c4-3f29-9bd6-33c0169471cf | -8.97567 | -45.10035 | 2024-12-01 00:32:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| de339fec-72a0-3503-9713-323dcfe909e3 | -4.7046 | -42.37243 | 2024-12-01 00:32:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 80a55ab2-921a-358e-89cf-f7b679d2c3b2 | -4.54038 | -45.69414 | 2024-12-01 00:32:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e50e7740-7087-349f-8954-8a5eb697d5f0 | -5.91497 | -43.85129 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7843c569-676c-3e6b-958e-e3d649d88140 | -4.40738 | -49.76995 | 2024-12-01 00:32:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| eccce05f-b429-3dc3-b9fd-87ea751dcfe1 | -6.29171 | -43.84668 | 2024-12-01 00:32:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 392014d1-6752-3fef-808b-1a9e621cb225 | -4.84842 | -47.57743 | 2024-12-01 00:32:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 10f19d10-8ea0-3a36-85ec-1a4be95abb17 | -4.5669 | -43.96031 | 2024-12-01 00:32:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4e09dbcf-aff9-327f-941d-839a674f0744 | -5.58774 | -45.21342 | 2024-12-01 00:32:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cbc8fae3-e475-3e29-b8ba-5917336083af | -4.01549 | -47.00169 | 2024-12-01 00:32:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1a2e0cbf-3734-3c2a-85bc-bde9d5a4fa0f | -4.05218 | -46.81865 | 2024-12-01 00:32:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 763f2782-65fb-3733-b9b2-923541acb619 | -3.90996 | -42.41969 | 2024-12-01 00:32:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 9d1a4a35-8dda-355a-b4a5-a54be08face3 | -5.48947 | -46.34535 | 2024-12-01 00:32:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ee4e2fc0-77ea-3afe-9f01-2da6cd90c5e3 | -3.69422 | -43.43854 | 2024-12-01 00:32:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b41237b4-836f-364b-8dbb-2f8b818bf2cb | -3.62334 | -42.73939 | 2024-12-01 00:32:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 758d6f2c-be96-39f0-8451-db9dbfe3a687 | -4.90568 | -41.32284 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 00e48b61-c0e1-3ebb-a91f-f05d5275bc7a | -10.51357 | -42.42126 | 2024-12-01 00:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| e211d6f8-d287-3647-bde0-49121a1dd746 | -4.8949 | -41.31426 | 2024-12-01 00:32:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| b806c7ac-5467-3865-8868-bc3998026acd | -5.57792 | -43.60849 | 2024-12-01 00:32:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33b8894e-c33f-31cb-89f3-7f0ef1f5a7a9 | -6.59719 | -44.19286 | 2024-12-01 00:32:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72c21524-d2fa-3272-af9a-afd4af42b58e | -4.45202 | -43.99144 | 2024-12-01 00:32:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README4.md)
