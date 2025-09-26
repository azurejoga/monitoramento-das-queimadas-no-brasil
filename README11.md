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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c14803a-7db2-3343-aa99-d9c33b0b68b0 | -5.58152 | -48.95513 | 2025-09-26 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 88e268aa-ec99-37db-a953-f6738699a3b5 | -8.03147 | -42.06871 | 2025-09-26 04:14:00 | NOAA-21 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed92a19b-1ada-3441-b9fc-477657612ee3 | -10.40563 | -46.17831 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af3602c5-9a54-309b-a764-77dad1681ae7 | -9.67772 | -46.02946 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35c87292-c79a-3037-b29b-38ca824e359a | -4.74596 | -43.61172 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f18dae71-3f80-3127-b22e-4a0b44b1e604 | -5.30049 | -42.7673 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c053e6-bfa1-371e-bc77-99f27defc8d2 | -5.72552 | -44.99485 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df8ff7b6-fd0c-3b3d-9b09-2282109cb3e6 | -6.88198 | -44.14089 | 2025-09-26 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfafec0a-cd2c-3b88-acf8-c392572af49a | -4.8174 | -42.74714 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8a08cb94-ab54-3ea2-84c7-61063de96299 | -9.75749 | -45.94967 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19a621f2-2189-3f38-a5e5-f8091886d875 | -5.76904 | -42.90791 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 451da15e-b38a-344f-84cd-89d403a711b4 | -5.77802 | -43.32517 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cde28217-4dd9-3248-bb93-7053feb8d9da | -6.34806 | -44.37302 | 2025-09-26 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 506169f1-055d-3be2-abca-2d9a015d57eb | -6.48021 | -41.91608 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f61b51b0-2adc-3d03-b3fd-0b4f6742780a | -3.85402 | -50.97393 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1a074c0-8d7e-35f1-9494-e57e39567a31 | -7.45888 | -41.91879 | 2025-09-26 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 66b20f5f-e060-3246-8e3e-0a7343d7ea71 | -5.72908 | -44.97246 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 968744e8-be09-32c9-ba82-7f8e7dd47b98 | -7.11737 | -42.17435 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 90418e16-f522-3afc-9a09-b1fda1d43b0a | -3.32525 | -48.70718 | 2025-09-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64b3a09d-d31e-35ab-a2df-057e4e38272f | -5.7273 | -44.98363 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0dad455-e53c-3b0a-be21-563fe19497dc | -5.00543 | -42.73822 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69ad4074-5995-3f16-8be8-e85b7581932e | -7.3134 | -45.76262 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea0b247f-4438-3ad0-8bde-31eb12eb9fbc | -5.24987 | -43.06923 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77ebf843-ecb7-3ee4-9a36-396a7ae97c2e | -8.86136 | -46.20551 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41e57a39-2801-3217-a42e-78078fda3f33 | -6.99634 | -44.70291 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbbee72d-9187-35c5-9b6c-3ad201c62d31 | -5.82383 | -43.90074 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7edb88bf-da99-34f0-803c-c6d56e6b30c0 | -5.78516 | -43.32275 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0b4a100-981f-306e-a6fb-b58e1288d4ba | -8.78019 | -43.03527 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bafd310-144b-360b-aeb1-bc0a9833c409 | -5.46235 | -43.06018 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95c70fe3-33e2-340a-bd89-9bc1a58ca79c | -8.7714 | -43.04819 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a03be520-6563-3614-ae5e-a334ad0d5242 | -7.68348 | -45.99112 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e469804-4918-34ee-9ad9-3a0c16b6ca83 | -9.80921 | -45.71803 | 2025-09-26 04:14:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 361ddd62-22dc-33fa-aa75-e68dc0eea7cc | -7.67586 | -45.99391 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fa29eb1-99fd-37d3-a14b-d1a8adf71fdb | -6.27084 | -42.19474 | 2025-09-26 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca5192b0-1969-3daa-bef2-c7939f8f1161 | -6.25549 | -42.4931 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 63f19980-ae10-3392-8cc7-e8dde0c8c918 | -8.78691 | -46.5919 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b3aabec9-8210-30a8-be1b-1e20d920d801 | -3.44318 | -44.1246 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a65d9dc2-f9f7-33db-91a3-9d9926ef3db6 | -5.52715 | -42.73216 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c89da31-d5df-348b-b198-371075700fde | -4.79595 | -47.27951 | 2025-09-26 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6a45ae81-ff81-37e8-aab1-9eaade0818b6 | -4.81181 | -43.54073 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e34aa486-2e66-341b-b6db-15461ab2eea2 | -9.55148 | -47.52843 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3184f46a-5979-3374-b442-8963d287f0b3 | -10.57297 | -44.08464 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 867a060f-9e8b-3146-80dc-3304ad59eeb2 | -5.46618 | -43.05725 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| f7065fc5-a8d3-3cf2-8eda-0b8b72aa9add | -6.99927 | -46.99604 | 2025-09-26 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df98e2d8-e8e4-367a-8d75-9f413d0f2cc4 | -5.40336 | -42.28147 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59cf0d23-3b29-39f2-9eb3-3edaadbbba3c | -5.73249 | -44.97299 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb0b13ce-ee65-3358-98d7-c6f95a5a0bb3 | -5.6391 | -44.72155 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4993b3bf-1488-3c72-b3ba-70f31fda7571 | -3.32594 | -48.70303 | 2025-09-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce70546c-5821-3a10-858c-affebcfca503 | -7.25625 | -43.01178 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e436ce9-19e2-36d7-8dc3-200d67d45660 | -5.6362 | -43.92445 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6157b4f8-bb0b-317e-9ea0-3d56dd67aa4a | -10.9314 | -44.29617 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7dd1e5-acdf-36a6-9820-05cd3f796407 | -7.67173 | -45.99725 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34debb15-af8b-3d39-ab32-ab220a2cf2fb | -9.87005 | -48.87455 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0041e63c-97aa-357c-b159-9ca4300d1a5c | -6.99421 | -42.59727 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b5e90cc2-0449-3f83-9200-d36ceeb0066a | -7.31056 | -45.75822 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 51291ab2-6363-39fc-ba44-95af6d4946f0 | -8.71658 | -47.12708 | 2025-09-26 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce7b6a55-85cb-3c6c-a272-b627832d96fd | -5.71483 | -44.97408 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 909da3d2-d0ad-3530-ac27-7951c10af96e | -4.68707 | -45.40776 | 2025-09-26 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ae44332-7458-3396-a593-eca46ff8ffe1 | -7.112 | -43.73902 | 2025-09-26 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e441b21-19e2-3af9-84f4-c6617e6a9d90 | -4.75591 | -43.61325 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7dc6902-a14a-3782-a126-52192d95009c | -5.72236 | -44.94874 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4cc7267-e6c1-35a2-a5a9-976829acf82a | -5.64284 | -43.92552 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4460815e-4981-3d20-8225-d19a934f7682 | -10.10346 | -45.30986 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7186976a-c972-331d-a1c8-20a4a6f23d06 | -9.67429 | -46.02892 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f46687fc-cbbc-3832-b735-8281c4f451aa | -5.76022 | -42.89949 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 016025ef-1129-37be-b643-4668fe40fff2 | -6.55285 | -44.32606 | 2025-09-26 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26680d62-17c3-31c6-bde1-7236f4fd6547 | -5.60127 | -45.37352 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f60c1f35-0f02-34fd-b9f4-00fb6b452e93 | -5.8927 | -47.59651 | 2025-09-26 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c49f15a3-2f84-3641-9fea-477659347127 | -5.2192 | -44.49148 | 2025-09-26 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| baad157a-9d6a-3f74-9f66-75eddad0e17d | -7.04719 | -43.82817 | 2025-09-26 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dc84a69-75d3-3b65-97a2-bfe4b253dc58 | -5.5647 | -42.73509 | 2025-09-26 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 641edd80-642d-336c-936e-b09c10a01679 | -3.80646 | -47.58902 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16a7cb4e-0250-3545-9f88-f9d2c1a6b865 | -5.75915 | -42.90637 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 33a03b52-bb56-386e-b821-c0ae6b2ce9c4 | -3.49603 | -44.76834 | 2025-09-26 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5e2bc35-e2ae-3bd6-aef3-ed8c07d11aaf | -10.30194 | -47.95421 | 2025-09-26 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1323d765-586a-3974-ad35-bff446ed4e3c | -7.77223 | -44.12969 | 2025-09-26 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8173716-cb70-3917-a1b9-1ace505aa11a | -5.7439 | -44.96719 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 7da48072-9aec-3dbf-9a91-a1282a8e82e8 | -6.12011 | -44.22124 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad49d5a4-6bef-3d2a-8a7b-4c171bc554ab | -9.75554 | -45.6559 | 2025-09-26 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c978b67-6509-3f64-b353-9b9077520d8f | -5.53093 | -43.87934 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| acb5f903-6107-339a-a46d-d8cc98179b60 | -3.45782 | -44.11948 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f297dbcf-0088-35bb-aba1-9cbe72c5336a | -5.97919 | -43.7789 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5cf224df-e8b1-3b61-926d-52b1cfdfc358 | -3.78058 | -48.63236 | 2025-09-26 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dc2924e-8a5b-3e15-ab28-051b56d72981 | -3.45725 | -44.12309 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c187330e-73ab-30a7-b2da-3a63fcff4881 | -5.22762 | -46.09183 | 2025-09-26 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 673c01cb-72b4-3c6b-a3d7-10c420eb0714 | -6.06223 | -44.84408 | 2025-09-26 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 017b1fba-9b1d-3c99-8cf6-444f675e2d91 | -6.2681 | -42.47736 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c3e1923a-2de1-3f9f-9b47-7ad7e4acc5b5 | -3.33372 | -50.19811 | 2025-09-26 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27e0769d-9922-3fa1-a9ab-7d1c5b4f5fa5 | -5.84667 | -42.49607 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a5e32fc3-98e8-3463-a739-1ec2bae68068 | -8.71247 | -50.05218 | 2025-09-26 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 550f4030-4ad9-32b9-968d-926425725e3c | -9.94963 | -46.28 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 251e6f92-325c-32a8-9c27-b8784c7aad3e | -6.75401 | -44.7123 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7e1a653-5f9e-3528-a966-5ef7e9a00d86 | -3.3209 | -48.70646 | 2025-09-26 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daaab604-e210-3e60-8db4-f0f3641eb0e8 | -8.67539 | -43.99296 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59c4bcbd-e00d-3986-8ce5-33d1e6d6088a | -5.51132 | -44.24059 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eba9ce6f-78a5-38e5-a861-a94b1add1243 | -6.98812 | -42.59276 | 2025-09-26 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4db1cbc1-0d28-3e7c-b583-6a30931f840f | -4.26691 | -48.55481 | 2025-09-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ea88cfd-3944-3d9b-9415-c6a6e33c436f | -5.73977 | -44.99327 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c855a34f-05b9-3a88-9cc4-f8a3bb33bc1a | -5.63177 | -43.93092 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b8cb136-9053-33cf-9a15-b5dd648d94ef | -6.55957 | -43.53097 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README12.md)
