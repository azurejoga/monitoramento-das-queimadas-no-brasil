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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bafda738-41c8-3043-9d82-cd305d9ccfe3 | -6.66381 | -50.94998 | 2026-09-24 04:44:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cbcf41b-399e-31f1-b517-5699588b1475 | -4.75696 | -42.7408 | 2026-09-24 04:44:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a8030a0-9f48-33a8-89a2-c072a7ed0023 | -4.48266 | -50.48002 | 2026-09-24 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b970cfb-420e-3960-95a5-df47ea3ffd7c | -3.96564 | -48.12632 | 2026-09-24 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db9e9e02-9d9c-3f3f-ab3e-e02513b2026b | -6.71723 | -44.15481 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 01291b94-962c-3e89-81f7-b3f76a137bad | -5.77536 | -45.10494 | 2026-09-24 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d03637ce-bf88-33cc-bfca-e9b796d83c05 | -5.60071 | -45.95304 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 933acbe3-2174-3304-9f89-ff75e9014019 | -1.27696 | -57.03743 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7de5a33-1626-3f9c-96fb-da026a16c624 | -3.52024 | -51.63514 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e7a4d6-8371-30eb-afbf-3e50409360d1 | -5.79075 | -49.18211 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 396694fd-1c44-39d3-aaee-4f188f83c3ec | -1.39321 | -47.94267 | 2026-09-24 04:44:00 | NPP-375D | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7df0bd99-3eca-3748-ac78-d5000cc45ea1 | -3.4507 | -50.07779 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9e241486-4ed4-3b24-b156-f2c504eacd14 | -4.35227 | -47.76212 | 2026-09-24 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54b3b0ef-a03f-36dc-83e9-f9ed65188b8e | -3.44516 | -50.08935 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 309807c9-8873-31bb-a252-aeb66c24227f | -1.82312 | -55.33376 | 2026-09-24 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5080bf66-bdf0-322a-8e22-d8d7167acfc3 | -6.77684 | -45.87923 | 2026-09-24 04:44:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b04818bb-487c-3b8a-b408-d093b96470fe | -6.14656 | -52.74968 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c80aa5b-eb5c-3b7e-8d45-b5704dbd53ff | -5.3305 | -48.98312 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f69316ee-84d6-358c-9cf9-eb1de12346b3 | -0.27705 | -50.47187 | 2026-09-24 04:44:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9713a03-aa66-32d8-b441-49b57a8e5edd | -7.76087 | -44.81376 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61d60115-87b4-3652-85bc-771757016d7f | -2.45256 | -49.22141 | 2026-09-24 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51119fd0-3bb6-3925-9826-175d8b57d01a | -2.29746 | -48.58205 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| deb09102-0713-39e4-b80b-4a8c27eb38c5 | -3.7903 | -52.42602 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf331967-eb94-3665-8a9e-eaa148c06cf0 | -2.96762 | -52.14914 | 2026-09-24 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb53eaab-fd41-3ac1-9eb4-79679e7c4e11 | -3.35419 | -43.24326 | 2026-09-24 04:44:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55c01028-2894-337a-ac49-658c1073a0fa | -2.45318 | -49.21759 | 2026-09-24 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22e2d1e7-44ad-3dcf-ab9f-1708acc1f095 | -6.02685 | -53.89408 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd2d7fba-b1a0-3883-a75c-b558fc8841be | -3.03934 | -50.43481 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c974913-966c-3585-b73d-c00b21719cca | -5.82587 | -52.02757 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64f446c9-8004-36b1-ad1e-d0f189123a51 | -4.277 | -48.62897 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e69a5de6-23e7-3fb7-9583-d4b0f7b95bfd | -5.60014 | -45.9567 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91626e0d-b66c-3472-881d-d1a7daf384ec | -4.35172 | -47.76559 | 2026-09-24 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2445046-dd58-3e05-905e-84035c38b3b5 | -5.25943 | -49.22856 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d470133-fa3b-3e29-984c-7e8ba59c67d1 | -7.62118 | -46.80104 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21f4a912-82f7-3a0a-86cc-b974a1091a63 | -4.47597 | -54.97229 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 396eac29-7a4b-3ba8-a373-e338c48f5a32 | -6.58144 | -43.85446 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdf11641-09f8-309b-a9d9-119de55ef291 | -7.19218 | -47.44956 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799e6d67-fc98-3931-950a-4e2d3c09351e | -5.22843 | -49.22787 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7d3aa85-bb8c-39a6-a963-a6e746f1608e | -6.78389 | -48.67892 | 2026-09-24 04:44:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c21438fd-f586-3a69-a156-f3c3ba10de00 | -4.53871 | -54.9734 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b3466ab4-71f8-36c3-b504-b1323cd2abba | -6.32124 | -43.04392 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 153bab51-2d57-356f-80c6-2aef978bbd83 | -5.78678 | -49.18518 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b1e28ad-139d-3357-949a-ef6fa29e1dad | -3.68313 | -60.56131 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27bd19e1-3a26-3241-a76c-674e5e84c551 | -5.99653 | -44.10666 | 2026-09-24 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0da273ac-af8e-3a37-bf04-57ef2d100363 | -4.12036 | -51.07689 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 682b6750-6e56-3d2f-93cf-5342bc4be6e8 | -1.21761 | -54.55868 | 2026-09-24 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c10a2feb-3d52-37d4-92c6-52dc144980c9 | -3.71071 | -54.19865 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ab82b2e-0b30-3dd9-afd8-00b8cd7ed3c3 | -6.82038 | -47.87675 | 2026-09-24 04:44:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f9c7f94-cc90-3baf-813a-f5e69504612e | -5.25602 | -49.22802 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e5ca063-b0ad-354b-a82f-6c8d079fc218 | -3.00898 | -51.53148 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65e95b0d-0aaa-3c5f-a24d-2d6fedefa417 | -3.68533 | -60.5484 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dc9176e8-8b0b-37ad-a7e7-e97b0cbdcc57 | -2.36451 | -48.35862 | 2026-09-24 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f42537bb-456a-331b-b877-84e8dc191fd0 | -3.51695 | -44.24823 | 2026-09-24 04:44:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 287c1903-98fc-334f-92d0-0734fbd3edf7 | -3.21435 | -53.40469 | 2026-09-24 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b20f5b5-da51-3e16-9863-d4cdb1f203dd | -5.44242 | -45.87301 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ab1fac9-5188-3b00-9bf3-d948684d33ce | -7.19276 | -47.46756 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14294163-ac99-3559-945c-dc2e43e5f843 | -5.8397 | -53.85694 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6257c39c-3204-35d2-a8fe-fd618dcc38fc | -4.02374 | -52.07336 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 449a15c3-6f2e-3dd6-a1de-da72224688d8 | -5.76969 | -56.52389 | 2026-09-24 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee213229-9522-31a1-93e8-e84ebd9813f4 | -5.4789 | -51.00867 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1d3cb52-cbce-3e26-b9b4-6cef7dc0c955 | -3.55048 | -43.46712 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dcc74348-bc41-3fae-a2c3-b56898c8481b | -6.88961 | -43.74831 | 2026-09-24 04:44:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c562493-5b46-30ad-a6f3-bc633665a9e7 | -3.67977 | -60.58094 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01bde156-d672-3744-8ee5-d982343b551c | -2.71012 | -57.51027 | 2026-09-24 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 712c5f6d-a499-35a9-9260-568bff5204e1 | -4.11962 | -51.08143 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c18bead7-73c2-3c46-b357-4b491320951c | -7.36971 | -45.9509 | 2026-09-24 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08686d02-537f-374b-ab1a-d59a772a9329 | -3.71997 | -54.19999 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa08610e-9170-3eee-953a-bc6362fecde7 | -6.00884 | -42.7314 | 2026-09-24 04:44:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98aec4dd-4abb-35c9-ad95-5572a3703a5c | -7.61725 | -46.80411 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ee9fa06-ca61-3a49-8897-ba41f32c166b | -2.943 | -51.29588 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce74861-d75d-32bc-86b3-f4f0572a5b9c | -6.57598 | -44.14371 | 2026-09-24 04:44:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 859c9338-6409-311f-a731-9d89fd60e753 | -2.36955 | -48.37049 | 2026-09-24 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7d5f3a4-83c3-3262-b4fc-e5977ab79266 | -7.45239 | -47.1698 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 350e0be1-3fb2-3933-a836-2330bae9c6eb | -4.11659 | -51.07646 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 4a173f3b-9d40-3f25-8358-03d32b4c83d1 | -3.23322 | -54.32209 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2723b21c-d0cd-31cd-904a-bd6a69dc2f60 | -6.22027 | -47.50006 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 496a0f1c-3d77-3567-b462-7a044a827cf6 | -3.16874 | -51.3628 | 2026-09-24 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 081f1250-d0eb-368e-beda-2717291969c9 | -7.61836 | -46.7969 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c8f4749-937b-3e75-aad6-3e469c7b06c6 | -5.20083 | -44.69021 | 2026-09-24 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18d1b87e-938c-386a-9189-df11c22df909 | -5.87706 | -51.94073 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0a4c2b0-0d0a-3e87-a91d-f5c714b256ac | -4.02219 | -52.07118 | 2026-09-24 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 978b93f0-672e-3a0d-8f9c-284551de3f0a | -6.19643 | -47.49987 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 509105d4-dfcd-350e-b89e-a93b08b4ba6a | -5.71709 | -49.83087 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1780d409-d501-3319-9698-001407f734a5 | -6.17771 | -53.28566 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1cfb021-b2b3-3035-9fa3-e893430fb4ee | -3.41521 | -54.00386 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eb966be-9f4f-3451-b936-351f60760bf3 | -3.58899 | -50.02822 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ffa56e-b33d-3fcf-8462-df3c353470b4 | -2.97503 | -50.39463 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d6dad61-f613-3173-87eb-1323342a702f | -4.28382 | -48.60811 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb814acf-8e12-3a63-b01e-c5f92cb649f8 | -2.91767 | -48.10523 | 2026-09-24 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52640a49-ab26-315e-8bfe-1b1832cb9f09 | -5.66589 | -42.58535 | 2026-09-24 04:44:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8c19372c-4af1-3cb6-b746-139b02f3c355 | -7.19555 | -47.47155 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b0978c8-7501-3d43-9c7f-6eeab89bd2ac | -6.21417 | -47.49554 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 38cc9b09-4654-32c7-98c8-bbafefbd0bde | -2.14622 | -50.89826 | 2026-09-24 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2eda88da-e2c8-3079-881b-bae5f21a0102 | -1.27792 | -57.03483 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3197dd89-0d5a-325e-8a93-1e2c25059580 | -6.72712 | -43.9397 | 2026-09-24 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a51e014-c8c3-3086-9de4-d062e455eca1 | -5.81477 | -47.75293 | 2026-09-24 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de039412-120e-3260-99cf-859e4ecf5469 | -6.26994 | -43.27369 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d385ccd8-4792-325d-bfd5-bc4a202cfc83 | -2.63974 | -54.68925 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| aba6bb65-f917-3f59-8209-4239c46a9741 | -6.77768 | -42.36751 | 2026-09-24 04:44:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a49e5357-d4a9-3515-bc44-fe398046b8ba | -2.89969 | -54.09472 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README46.md)
