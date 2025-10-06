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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16f94507-cc38-3d26-9544-0e2d1ec80bf8 | -4.30967 | -48.2379 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 311f0fd5-1dc5-3350-9d5c-55e28af1a9a2 | -5.49446 | -42.80378 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b2432dbf-972a-33c0-b9fa-203c79f61970 | -9.19917 | -46.91289 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00f7b102-47d8-3ed4-94ea-5740ab904027 | -8.63452 | -46.32173 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b5412b60-bd42-34ad-9d02-023fde8003b6 | -7.42205 | -41.12669 | 2025-10-06 04:25:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ad4a6a59-52bc-32bb-8901-05b6d004ee0a | -1.12419 | -53.05458 | 2025-10-06 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 342f4816-0913-3b09-b1a1-f3694cd392eb | -5.65031 | -50.30861 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8574bd-c5ba-3d1b-b982-65184ceace18 | -7.29488 | -48.62183 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4385a38b-3661-3ce5-9038-e9ad4f9fbe19 | -2.61668 | -49.39416 | 2025-10-06 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 727f49b5-8cf9-303a-84ed-2811d317ea20 | -8.6291 | -46.33159 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| edc5c88b-7718-3a75-9181-23e483011fb5 | -8.67786 | -49.46953 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fd410d0-5b7b-32a8-b593-1caec4e77d68 | -5.64524 | -45.96275 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fbe187a6-6a22-3d42-80e6-100e568aa03f | -6.11617 | -48.08466 | 2025-10-06 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77b303f1-d2ea-3b9a-8959-ff35282bc888 | -3.81542 | -51.29482 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad1ac640-7000-3a0d-8562-bbf3921c5889 | -5.64116 | -50.31677 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67e692bb-5884-39a5-b194-68a6b4da7287 | -5.33672 | -43.3734 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85e4dcb2-938c-3bb4-9602-a40f0e6af5d8 | -8.92294 | -47.37014 | 2025-10-06 04:25:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f1bcbc7-9ff2-37be-9fec-66d0bc0ac870 | -5.7231 | -49.28514 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91623062-36d3-3ff4-af7b-4b3d27b287b1 | -8.37211 | -51.07982 | 2025-10-06 04:25:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87769ba0-c559-34e9-b817-209b8e3471a0 | -5.33181 | -47.28008 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66d41dac-1bbd-31f6-9806-1c84ebf68037 | -7.22912 | -44.88538 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5b7563d-05e5-3cd1-9881-31acba2ed1aa | -7.71878 | -46.25853 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2a358f24-f8f7-3ef9-aea3-6dd9f12b6424 | -6.397 | -47.71239 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5582fb48-700f-3407-ab0c-c67751e933a2 | -5.79638 | -45.46993 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f431c7cd-e7b9-3702-a131-9cf6518ff5cb | -8.53298 | -46.38417 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f65708e-0e1d-3722-964a-ec70a8c62571 | -5.46268 | -42.78693 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7cb21289-2a5d-3207-8aa7-5dbf306718ba | -5.77727 | -45.52742 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e90c366-a1e5-3304-ad24-d48175c314df | -8.66144 | -41.67721 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2cf9cb36-e196-33c0-9738-3e4b08f381f0 | -5.32733 | -47.28668 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8f8e547-922d-3092-b463-f169d2b05689 | -5.64954 | -50.31332 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96f2ff18-b1fe-381e-8a7c-3044de7c109f | -8.61744 | -46.29772 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55b6dd90-b467-3f40-8698-687cd2e9a94b | -8.16962 | -44.25549 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ec1f6935-db99-3865-8f3e-2a4b02b81480 | -7.55194 | -44.93055 | 2025-10-06 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0975b85e-033b-3985-a2af-4efa5074280c | -8.19722 | -44.1678 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d64a624-3e06-31b1-9886-646ac5472797 | -5.69818 | -44.8323 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f444142-1988-36c4-96ea-7fd45e6ee5ae | -8.62075 | -46.29824 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 109795f3-a9d5-36ee-ba6c-711e7cc51e5e | -5.47816 | -47.51932 | 2025-10-06 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f77ffd8-a27c-36f1-ad28-525cae143c0c | -7.7875 | -42.59164 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4c3df3e3-7bd3-312d-9c0a-6baa3a222d55 | -9.12988 | -44.39729 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48c82e8a-de11-3fc5-ac6f-e51cff44bf07 | -7.19987 | -46.85544 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72186ccb-965a-3576-8dc5-bbc13ee27a8c | -7.85729 | -47.2632 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ff1999c-0cd6-3016-bb4e-7427571b6751 | -6.62715 | -41.98009 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ef9a780d-59b6-3599-8153-be66c15a63a8 | -5.30072 | -42.54568 | 2025-10-06 04:25:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8b7d6a9c-964c-3a56-9ed3-499eaf7f0d0f | -6.99768 | -42.83527 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e56ea99d-c003-3067-877d-b76463020957 | -4.26267 | -48.55028 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 259fd20a-ff27-3cbc-8530-c91f598ac2e5 | -6.90337 | -47.33216 | 2025-10-06 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da1ae241-aede-399a-a372-1aaeca21c707 | -7.43442 | -41.12851 | 2025-10-06 04:25:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3452af10-3011-3751-8086-9212768f99ce | -6.40734 | -43.80987 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5281678-5a7e-32a1-b0f3-dcbc515c39a7 | -5.33514 | -47.28062 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 78280bb9-2c5d-33cd-a134-a7dd3436b672 | -2.24826 | -47.86518 | 2025-10-06 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8827b617-76a8-3c0e-a186-255b0f0b05eb | -5.98581 | -45.47778 | 2025-10-06 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51c32e2a-5b5d-3434-984e-786439194132 | -7.77997 | -44.20584 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a92ffda2-69df-3e1e-8891-323eb7efeb5c | -8.54768 | -47.67528 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb4d12d3-326b-3f28-b75d-31d5bd0311bf | -7.43388 | -41.1322 | 2025-10-06 04:25:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 05b03ff0-50f6-3f5f-9947-7f7eeb1b3d29 | -6.58724 | -44.11813 | 2025-10-06 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9bb6bd2-bc0c-31c9-9902-7ffdc7466883 | -7.18297 | -41.68943 | 2025-10-06 04:25:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cafc490d-e58d-388e-8b87-56d3bc778d33 | -3.93857 | -52.15528 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9429b583-f9f9-3ffd-8b78-3a6f0348c6c0 | -5.20585 | -46.20262 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9de19f68-409d-3725-a58c-452f4789c3bd | -7.81808 | -47.38202 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d785a87-ca89-3755-864c-cad6292f0cec | -3.50762 | -50.47826 | 2025-10-06 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de513d07-43a0-3cf1-85e9-fe84c4dcdaa6 | -5.3227 | -43.7214 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d38faeee-ee6f-3e21-9916-884f5a6bd3f3 | -3.28966 | -52.5486 | 2025-10-06 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e5a007d-037e-3d02-a6a3-dee21ef1c8cc | -7.73153 | -42.39205 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b1b5b5fa-bc2b-388d-84e0-3c64b091adcc | -4.21239 | -46.74003 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5fb9c2f-4a59-319b-963b-bd7dcc30deb8 | -7.52215 | -45.41865 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bc2d699-4f66-3998-91bc-64cf18d7f37a | -4.65466 | -43.19065 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e20a33ce-0524-3311-bd4b-ce7e2356781b | -2.58939 | -48.12038 | 2025-10-06 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4f23281f-b562-3b5d-a9bd-7612b890c952 | -7.61667 | -46.67422 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b877e57-b546-381f-8494-1a1390328362 | -2.58876 | -48.12429 | 2025-10-06 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f9de645-2615-32ad-a21e-7b3960883c18 | -5.70153 | -44.83281 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4245d25-2d9c-34fe-9c44-2ff76ee76b2a | -7.32622 | -47.28493 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 09c93de4-c91a-33e3-bf64-4a0050786239 | -9.13048 | -44.39335 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a0b6915-ccf8-3463-92a2-e67bb1121163 | -7.43138 | -41.12047 | 2025-10-06 04:25:00 | NOAA-21 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cf0d2981-aa57-3edd-b0f1-3e3c013a947e | -5.52916 | -45.41739 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba172629-fbb0-3d3a-8dac-d0dce87ee25b | -8.53871 | -47.21567 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f6d3ef2-5e4f-3246-82b4-ac014772db7a | -4.32099 | -46.80708 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ca854bd-bb6a-3b3a-ba37-80cdc9bb593e | -6.07208 | -42.54195 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f2ccfaec-7c64-3eeb-8ddf-7dc63486a5e2 | -7.06885 | -45.11882 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d371eee-5779-3ab2-917d-ab6e989719aa | -6.63872 | -41.98186 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3a981c67-5064-35a0-8fff-cb9a91f3046e | -5.70754 | -44.85515 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61973201-44ea-3494-a829-5ce230aac142 | -7.79274 | -44.12001 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 917911b0-375a-3013-a7f4-e5990487000f | -7.21947 | -45.90268 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9aa66fed-466f-3b17-badd-1c9829764fc2 | -5.69314 | -44.82059 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b632f4e5-47a3-3c44-97b6-c4941a527f4a | -7.25053 | -44.13704 | 2025-10-06 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a94dd853-b9b1-3c28-afaf-1e2aba783877 | -5.77205 | -45.77798 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe495f16-594f-352d-8581-e0f975b7216a | -8.86356 | -46.09291 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05abc726-f6f6-3fa6-9f40-d1d885ca2a87 | -8.524 | -46.33294 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e06b2154-a3a3-3f22-96c5-88aa6191a9ed | -8.18223 | -44.1251 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b51ae1f-b6d7-326a-bfb3-2f4d569c6074 | -5.8384 | -43.92627 | 2025-10-06 04:25:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc0407b-88e4-33b4-baa4-e9991d4888a0 | -8.18073 | -44.22926 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d142ecde-1935-3779-a455-de9ac966eb6d | -5.60659 | -46.23145 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74f17d16-159f-3fdc-9399-1bb0b9f3a992 | -6.31481 | -44.25105 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 864eea80-f719-3449-962d-b1182c9681e6 | -5.30069 | -43.74924 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb014402-36db-3c71-b034-2104baa78ffb | -8.21388 | -46.9893 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94a070cc-7a7b-3d63-b8d4-ddd42c8ded84 | -4.6213 | -47.45001 | 2025-10-06 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 443bbe7d-0186-3ff9-8a74-f0a703d5befc | -6.79618 | -46.04187 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4c20d01-10f9-3218-8405-d047bbdc31a6 | -5.26983 | -50.9878 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93974b9b-2062-3ec7-ba95-f941691ce1fb | -5.70042 | -44.83993 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 296069a1-7286-34a1-b200-cb98c515d10d | -3.89443 | -47.18177 | 2025-10-06 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75412a0e-6f47-3a2f-a652-1ccd763ad775 | -5.83463 | -45.83705 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README29.md)
