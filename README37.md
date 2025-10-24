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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a737c8a3-1474-3dfa-be9f-d1bb66308f42 | -4.24334 | -48.54905 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d762284-995b-31f1-ae4a-4d14915e455c | -2.58759 | -51.34413 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f66eb0bc-5806-307a-9d3e-4a1f61a8cc52 | -10.18067 | -49.67581 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4333bb0-59e2-3c7c-8455-37839bee8b5b | -7.5496 | -47.36148 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e33c47c9-5ca5-301f-ba5c-e89b5eca8b91 | -6.30015 | -41.87597 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 313f8a49-f4fb-3b6e-9b70-2d0e451de635 | -6.75029 | -46.54826 | 2025-10-24 04:38:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbe2ef9b-2fdb-32d7-8d6f-34ca44e9cf68 | -8.20143 | -46.99122 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 779da5f7-3255-30f7-86a5-43a27a3b873b | -7.39971 | -43.91512 | 2025-10-24 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 156facf8-dc54-377f-bc63-0af787ed7d4a | -3.5582 | -47.30598 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 102e300d-f9e7-36fc-8727-b3a615d12fcd | -7.49243 | -42.57954 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b727c1b2-6f23-34b6-af31-a42330930bb5 | -3.0519 | -48.7136 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfab8d56-e2bd-3ec4-9180-5106c9087d39 | -6.80237 | -45.4378 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99bf948f-9bdb-33c0-8427-125aa956ed76 | -2.86892 | -50.7115 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 532ec794-2392-3a4e-9a21-6a6fc69034e6 | -10.63634 | -42.3027 | 2025-10-24 04:38:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21bb48eb-96b8-361b-919b-9aacc545529b | -8.64047 | -44.79215 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60460719-3d8b-3dba-af90-cb78c261e268 | -7.44916 | -47.2606 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a98a796d-b381-30e6-bc29-6cd2a896f170 | -6.59004 | -48.76931 | 2025-10-24 04:38:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5960b215-c1eb-3036-a226-0f46c7996301 | -8.65262 | -44.79332 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 17194aef-f84a-353e-ac4c-48414680b0ce | -3.23875 | -48.75742 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e0d43fd-ab67-3d91-b854-7145fadfe644 | -5.65368 | -46.57709 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15237de6-e968-31bc-b8f9-694755476f2d | -7.83501 | -45.59151 | 2025-10-24 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39beb654-e3e9-34e4-859b-93b5505a831b | -3.47399 | -52.98802 | 2025-10-24 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f69f46d6-7221-3b7a-a84f-2f311cbe70a1 | -4.2522 | -48.12571 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 593a6f03-bfb7-3bbd-9e8e-c257a9198831 | -2.80053 | -54.38142 | 2025-10-24 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05569e7a-87a8-3112-9d29-0242ff69c4ea | -2.86713 | -50.72287 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b822412-8708-3972-a019-fc11fedfa099 | -3.55586 | -49.43731 | 2025-10-24 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| faec22cc-910a-3d93-8339-19fae93eb42f | -9.60439 | -46.88736 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6935b5d2-4dde-3195-b225-e0a90e9ae6be | -8.32431 | -46.24973 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| da8a6ad6-a318-3949-81e2-f4f5dfe3e23a | -6.90891 | -41.53992 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bb898ab1-0b53-3a9c-a076-efc852623776 | -9.60246 | -46.9252 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8f2621ca-f384-3e04-a951-82662625ef16 | -4.55154 | -49.62994 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15899363-1702-34d9-8344-8642935ac416 | -2.96202 | -48.59361 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f834c6-bac6-3e7f-8bc5-881d4bc170f8 | -11.0541 | -45.39529 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57bab7bc-4341-3065-912d-56e8a3fab9d9 | -8.11387 | -47.04396 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81d49f78-6222-39dc-b672-cba79df99f11 | -6.79171 | -46.46789 | 2025-10-24 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1b842a98-93ba-3f00-b5f2-db4dff8a582a | -2.85602 | -50.7483 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4a5c843-4f25-3bff-8ced-d030939c3b2c | -10.64124 | -42.30338 | 2025-10-24 04:38:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3938fbb4-f0fc-353f-a229-29bdcb881862 | -8.32064 | -46.24917 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cbcff25-870f-3199-a98f-461a4cb849e0 | -10.11333 | -47.74059 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0c13d1-0eda-36b7-a983-91bb89f412ee | -3.08889 | -49.25312 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebfa776b-5813-3b3d-a6f8-483071a077c9 | -3.87256 | -48.33556 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd4b09b2-c962-3740-ba4e-0af9aede9288 | -11.14678 | -44.94159 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7212b208-4a14-3e86-b9f5-b33c4a18ff91 | -2.87834 | -50.71272 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e68dcd9-09ae-3286-823c-28113584fa19 | -4.85591 | -46.73195 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65a8f3b5-cb11-3fc4-94e0-cea73148620f | -3.60344 | -48.98763 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dd1d11c-5f4f-3b25-a666-11447612b745 | -7.40242 | -46.96976 | 2025-10-24 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a274b06e-aecd-346b-acc2-27b406add1ef | -4.70722 | -48.12525 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a674228d-e605-3f13-82bc-0b93c403b893 | -4.24888 | -48.12519 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 549a3977-a37f-3d21-88b2-4c350f6fad73 | -4.21099 | -48.60395 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91586cf4-8eec-34c6-bdee-b40c651cc989 | -6.74532 | -48.05816 | 2025-10-24 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b92d0841-b24e-3fe7-b263-d3929c623d14 | -5.54115 | -41.37273 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a7dd2f7-99a7-366f-a4c8-c72742adf165 | -6.8092 | -45.44361 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc91ab09-9baf-3ddb-ac5d-8177fb5f7c7c | -3.14557 | -50.16019 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9649635-839e-3112-ab76-74b6b7404ce0 | -6.80785 | -45.4526 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cacec61b-de58-354d-8b1a-56c2a91f089f | -4.85649 | -46.72815 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65281ed9-e43d-3509-aebe-071074b59aab | -6.9209 | -47.16792 | 2025-10-24 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8ab529b-4d71-3c3f-a4aa-3f08e8b35e24 | -6.4387 | -45.6694 | 2025-10-24 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2e7d25f-5108-3a1a-a302-b0cc71dfb355 | -9.63981 | -46.8968 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52b25c97-4017-3aed-a519-a18b32f203f5 | -9.21452 | -48.59158 | 2025-10-24 04:38:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4ef47ac-ec7c-316b-869d-40b9f09d05d5 | -3.01982 | -49.45272 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd8b3417-bd97-394c-adcf-b60f32a06241 | -6.7754 | -45.48965 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fabfb818-ad61-3467-a485-1bc3b9a42a31 | -9.23259 | -51.83746 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74af2cb5-631d-39f7-be7c-5925b9d86c6a | -8.17833 | -47.76342 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9959af0b-13d2-3eb6-8201-ebe94e835c66 | -3.85268 | -49.12963 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea47b37e-a9ea-3a0f-a3bf-9c55c1aac397 | -7.55651 | -47.36254 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc1fef5e-900e-3aeb-8211-0eb84ebd7ad3 | -8.69051 | -47.05622 | 2025-10-24 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39d1877b-b731-3c27-8ab7-ab43dbf5c2c4 | -4.28137 | -48.02692 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f5d4a73-5be8-360b-8ec4-79bd8d18005e | -5.85127 | -53.43063 | 2025-10-24 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c617996-93a2-38cf-a2c9-483898fd62d5 | -3.22418 | -49.36374 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae5662d0-dc07-31e2-a0ab-8d5c91c499ce | -3.64639 | -48.9732 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6629a56-466a-302c-b3aa-36f36a56e041 | -3.05521 | -48.71412 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b2c0c4d-b215-3a70-8218-871afad11f19 | -3.12907 | -50.61634 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82be44e2-0aa2-3f26-bddf-0ad2934eba97 | -6.43936 | -45.66501 | 2025-10-24 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9d7af7a0-45ea-39a8-a0eb-adedcc3352a4 | -6.91802 | -47.16357 | 2025-10-24 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f473195b-23fd-3a56-8e04-75a6d1eecc1d | -9.19937 | -44.54455 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca695ffe-6866-3ef8-87d6-6732bf4a1ce4 | -2.84155 | -51.36604 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14d94caa-583d-3500-b462-420b79c88cfa | -8.34372 | -46.19557 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d308c4df-5c16-3619-a67f-3685146dcf88 | -9.86789 | -44.89392 | 2025-10-24 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd84416-b0e3-3edf-8ad7-eeab95497cc4 | -3.23545 | -48.7569 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6c5cbdd-96e5-38d5-96b6-bac47840e987 | -2.81806 | -49.13924 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 86aa64f1-2ff3-3f17-bb94-e81546fe1699 | -5.59725 | -45.19564 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9734e272-a61d-3ed3-abdf-5ecfdd998136 | -9.60307 | -46.92107 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e10b2f4e-e7c9-3dfe-97e1-4de9036b6b37 | -9.63918 | -46.90097 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e11ac6e-502a-31f6-9350-74fe29769d55 | -7.63011 | -42.20767 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4d46ac88-a340-325e-aabd-55fde8bc3da7 | -10.01109 | -47.09217 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4e9d8aa3-5511-34d8-9446-ca6d5b2b135b | -5.52086 | -43.87659 | 2025-10-24 04:38:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e67fed7d-4e7e-3f36-9a09-389ac6f9250f | -7.2748 | -50.00634 | 2025-10-24 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cca9292-8e96-3b82-aedf-877ad2ccb107 | -6.97616 | -45.28551 | 2025-10-24 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32e3cb30-aa8a-377c-8b81-7af0a4e435b8 | -6.89752 | -43.62184 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ab2d97b-673b-3e64-8f14-e0f1c55269dd | -6.65135 | -51.0084 | 2025-10-24 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71bcbf03-f208-3d27-b0ef-db922aa26284 | -6.83989 | -41.54988 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a2b69bde-ec33-3182-894d-bf3f41e2fb1b | -4.66294 | -55.96717 | 2025-10-24 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e819250-1ea0-3dcc-b52b-050f91ea1b9a | -5.47453 | -46.47089 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21da3f08-fb02-32d7-90f8-8b30bcf73f1c | -8.0721 | -49.71468 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0be6b388-51b1-35b8-9d64-26cd108d0e0d | -8.20265 | -46.98316 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f4ac001f-6c7f-31fe-aa77-21631c648c28 | -3.98226 | -50.52144 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82ebd3eb-6b97-3d1a-a610-82cc63a31c3d | -2.87118 | -50.71962 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3db249d5-364b-3a27-b1eb-31037606c2d0 | -11.16813 | -44.68972 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37db0963-6317-37c2-bcbe-0e1fd89e67a4 | -4.15244 | -47.6766 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea54d4aa-bc22-3d2d-a01f-06479652bcac | -4.81018 | -50.93768 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
