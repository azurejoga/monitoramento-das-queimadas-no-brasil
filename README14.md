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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41a41939-d49b-368b-8041-fe107d762e73 | -7.7847 | -46.0397 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 011464ce-4ff6-3cc5-a8cd-833619cc231b | -7.7194 | -46.157299 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d86af92e-3e24-3aa7-8ce1-24dfd0caf8a2 | -8.5881 | -54.740398 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d60b8003-8c45-3810-b88b-bd5c793ad4bb | -6.0205 | -50.205502 | 2026-08-21 00:42:00 | METOP-C | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1678b35e-79c6-3c8e-93ce-8ef34a2e2487 | -14.3349 | -51.894699 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4696373-a47f-3440-8e9a-89a02af5c6d9 | -3.98 | -47.201199 | 2026-08-21 00:42:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 87adc6d0-c339-3532-9e59-f03ffb625219 | -8.452 | -46.951801 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 264ae98b-0fc5-3f14-bbb5-2d99ac6da9a1 | -13.6796 | -48.770302 | 2026-08-21 00:42:00 | METOP-C | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d97acadc-e350-3dc6-828e-72b9573f450e | -10.7558 | -47.905102 | 2026-08-21 00:42:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30b0e47f-1870-3e7d-84dc-715862dab244 | -20.956699 | -47.198299 | 2026-08-21 00:42:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0777f05f-6dfd-3931-aded-aef8d37cd58e | -11.6602 | -48.348301 | 2026-08-21 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b978934-1c43-344a-b963-f99a40a9d2ac | -4.0962 | -42.4967 | 2026-08-21 00:42:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e417973-a632-3db5-b948-dfc5bf465073 | -14.4482 | -45.6049 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e45d359-8205-3fd2-b883-965343895e6c | -6.4396 | -52.768501 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8a569c-c716-39a5-b1fb-7fd1803ac36e | -12.2311 | -43.1623 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e881e6f0-2e20-34a6-ae7b-1b3ec7066090 | -20.837099 | -47.361099 | 2026-08-21 00:42:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b9b31f7b-fa0e-3da8-95b5-7624d12f644d | -10.5233 | -50.785301 | 2026-08-21 00:42:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 555816a3-ae39-3c2c-9d3b-dc50d76887b1 | -6.3746 | -54.9501 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc620c05-3785-3c66-9aee-919923a4e3b1 | -10.8125 | -50.276299 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 364cfdcd-723d-3ae1-8e55-b7d89d36aa02 | -10.8298 | -51.013699 | 2026-08-21 00:42:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e78484a1-dd95-3466-bff9-3527ff864561 | -10.7635 | -50.334099 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14559068-bd34-3add-bfe9-92a7129ab2cb | -11.1987 | -55.046001 | 2026-08-21 00:42:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dafb9ba-a50f-3904-a388-9d1b2e93a151 | -19.8531 | -43.8694 | 2026-08-21 00:42:00 | METOP-C | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c21746d-d4d4-321a-b537-1ed91b28d2c7 | -5.6113 | -44.010399 | 2026-08-21 00:42:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4eca829-7f3c-3720-bfd0-3892f1872f82 | -15.7081 | -47.795601 | 2026-08-21 00:42:00 | METOP-C | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| 6863c8d3-cc08-37fe-8cdf-49a2ed59e5fb | -6.856 | -59.450901 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 195fa8b2-58d2-3542-a8bc-796420d29c4a | -14.4597 | -45.6101 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1603697c-2913-39e0-bdd4-6cde8d4f5dc1 | -15.4436 | -41.380699 | 2026-08-21 00:42:00 | METOP-C | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b027e32-7b88-3507-8122-4f769eadacbf | -6.4223 | -52.736599 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab8f5ac4-9c77-3204-b570-6953e8d00fe4 | -8.6558 | -54.626598 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a21f6d7a-8e5f-349f-8f34-a7007cabac0e | -8.107 | -51.665798 | 2026-08-21 00:42:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27c78df-2099-3769-bea0-4ad4f7090fba | -7.2685 | -47.455799 | 2026-08-21 00:42:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a23aca81-8943-3118-8d17-7ad5d25a3ade | -18.194599 | -50.741798 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 358eec5a-cdb4-3f1c-9333-7d65d4eba570 | -9.2032 | -59.751999 | 2026-08-21 00:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98f0939c-88f6-3d45-85db-a1e9bab64526 | -8.1156 | -50.040001 | 2026-08-21 00:42:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d67d7b24-3538-35d0-a46f-2d93e5e099d8 | -7.7311 | -46.162998 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f84cd57-a62d-39fd-97da-2ddb4d7c9d20 | -8.4966 | -54.886299 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f5f4d7-5038-3ce1-a35d-85294fb9ec4e | -4.9213 | -56.255001 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2c5d4b7-ff9d-3881-b33a-12f08317edaa | -7.7828 | -46.031601 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8928e27a-e149-3d6f-a8e3-16ab15f15835 | -8.0972 | -51.667999 | 2026-08-21 00:42:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e68a9d83-5c8d-3927-b090-133035c3d842 | -10.3125 | -50.3867 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aca22ce0-3688-3525-b9df-ad9fa3367350 | -6.4321 | -52.734402 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94817769-29e1-3fb2-87b7-4630468b0f92 | -4.1758 | -49.394001 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4496d785-9f74-3d3b-8335-06c65d147711 | -6.2374 | -55.4007 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f65aea5-d531-3d91-b3ed-1c06a5f09ffb | -7.3683 | -45.805599 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4b14802-4fee-31b7-b06f-953602344cab | -6.3386 | -46.519798 | 2026-08-21 00:42:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54ada3c8-c765-3812-9242-46188cb115a5 | -7.3477 | -55.6726 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a274dbd6-b207-3a36-9835-3107d9c48782 | -12.5108 | -54.750599 | 2026-08-21 00:42:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7ec006e-ed14-30c6-a7ca-39a018293807 | -14.339 | -51.9142 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a29d10fe-0884-36ba-896f-e733cf0d0fd8 | -7.382 | -45.820099 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8731063-1595-3539-8d37-1dc5a981aa04 | -8.5431 | -55.299099 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed1aabd-5b9b-3623-9dd2-3ea15d0f0db2 | -12.2459 | -43.180401 | 2026-08-21 00:42:00 | METOP-C | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e554fcce-5a0c-3ae6-ab8a-1c743f5a3d63 | -8.1624 | -46.727402 | 2026-08-21 00:42:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 779ce8cb-2c1a-359c-a9b3-49d1f7f8b711 | -8.6908 | -47.492699 | 2026-08-21 00:42:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83a17051-4dd6-3b9a-9667-5dbbd463506c | -6.9654 | -50.4212 | 2026-08-21 00:42:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 115d3d03-7aed-39b9-8d3d-3656b108bd9c | -13.4533 | -51.783501 | 2026-08-21 00:42:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fea5f338-9b4b-3222-a43a-7a7a233ac3f6 | -20.868999 | -45.283199 | 2026-08-21 00:42:00 | METOP-C | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8268336d-cf9c-35b3-a3e5-fed1ae3802df | -8.5978 | -54.7384 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72335ef7-e424-340d-bec1-81f5e24b8be1 | -7.3702 | -45.813999 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71344c84-bda6-34f4-a72a-e13e368f8cdf | -3.2689 | -49.532101 | 2026-08-21 00:42:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bb1781c-caff-384a-a2ca-839be1b2ecc6 | -7.3585 | -45.8078 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| adf53e13-f4a8-3c62-8453-2d9fd70f77d2 | -6.8793 | -56.629799 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ed43bac-4c17-38ac-951d-e46edf8c252d | -2.7688 | -48.566299 | 2026-08-21 00:42:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 584696be-a478-3019-b2de-e84e384d6ef7 | -12.6545 | -47.775902 | 2026-08-21 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6aa10f-51cb-3f9b-b5eb-d0beb22e4582 | -2.7705 | -48.573502 | 2026-08-21 00:42:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67827a30-363a-3421-8e84-6c6541f932dc | -9.4672 | -51.6394 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955fc000-20d2-3c10-ba46-a17d25573949 | -8.5809 | -54.754601 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c86fd1a-8107-30b9-88bb-5f0bab4ab3e3 | -15.1901 | -49.4319 | 2026-08-21 00:42:00 | METOP-C | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c9ee03a4-77b1-3ffa-a66b-bcebc28fb0b5 | -5.323 | -50.9482 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80387fb5-9204-37ec-b79b-cc69f76ad610 | -7.2569 | -49.8866 | 2026-08-21 00:42:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37537a1c-1447-3a8d-9df5-c00ecd9d7bd9 | -6.434 | -52.743 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aef5724-d72f-32e2-9974-4e4ef49355e8 | -4.042 | -50.298599 | 2026-08-21 00:42:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8c1f8b8-da4d-35b3-b295-d41edbc6be76 | -12.8428 | -48.431301 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 237dda82-af74-3a8a-b1e2-c756af413ede | -12.8608 | -48.4198 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7a73b9c-0e29-369f-bdb1-872e09b68147 | -13.3914 | -43.679298 | 2026-08-21 00:42:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d727a00a-d41e-3c4e-85d8-f7a118b7d2e4 | -5.6632 | -51.636398 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55c9ac22-2d0f-3bf2-97fc-122a49c1f98e | -10.8165 | -50.999901 | 2026-08-21 00:42:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac53a64-4181-36c7-8c5d-e0aa1c46f8b0 | -7.4643 | -49.7094 | 2026-08-21 00:42:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09b93c9d-a91f-305b-908e-9fd226fd88ee | -10.7422 | -50.330898 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 984c5153-d7ee-3713-a7cb-0ee08470104d | -10.1305 | -47.696499 | 2026-08-21 00:42:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebb22cf-73b8-34e2-a71f-d1906bdb226d | -4.1888 | -49.405499 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0f8fbc8-c6c7-3b05-bc4b-7b0ad01075e1 | -14.458 | -45.6026 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4869ab15-cc0a-3544-adda-67ffbe336a43 | -10.2716 | -50.294601 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7f2315-92b7-393f-9ecb-62bf8a9d5d47 | -2.7607 | -48.575699 | 2026-08-21 00:42:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 880631d1-8207-3469-b7cd-27489b08f1db | -9.5074 | -51.682201 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c75213c-3f01-34d0-9d01-6323587d2b2c | -11.1751 | -54.039501 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46c3a24c-c5bb-36dc-bbb3-f2bf54c8d70b | -14.9005 | -44.7999 | 2026-08-21 00:42:00 | METOP-C | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ed66f83-4430-32ad-89ac-d1a6ae6a408d | -9.5056 | -51.674 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 955ed223-0a23-3fcd-9688-722db7e38d74 | -13.9784 | -49.4324 | 2026-08-21 00:42:00 | METOP-C | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d67b154-46f8-3fa1-a1bc-75926a552c5f | -3.954 | -43.105301 | 2026-08-21 00:42:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 46884d2e-8798-31f8-b510-fce0e29104ca | -8.5762 | -54.780701 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e232d3-20c7-3463-b138-711b9a0b265d | -4.9506 | -56.248798 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d827078-f92d-3624-8dc1-988c4663e90d | -8.7196 | -49.611099 | 2026-08-21 00:42:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d65ee0a-b1cb-3394-a37e-284fdadb6e21 | -19.6964 | -46.928902 | 2026-08-21 00:42:00 | METOP-C | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f2598541-2fbd-3d62-9fc7-ed218bea91c6 | -11.9205 | -50.173401 | 2026-08-21 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a50e9aa8-6914-36c6-84fb-d22fc3659a8e | -18.0581 | -44.420601 | 2026-08-21 00:42:00 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e702b741-271d-3cc3-bdc4-e36110d0365e | -9.4074 | -60.430698 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8886c141-bc1d-3974-92ff-14c3f14f87a9 | -11.18 | -54.013802 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf371f4a-d7a1-3e51-a8fd-d71b206f93f3 | -6.8754 | -59.446999 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf020ab3-bd37-3723-b0e1-9fcc733ae280 | -21.3605 | -44.126202 | 2026-08-21 00:42:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README15.md)
