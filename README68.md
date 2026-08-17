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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74de77d8-38db-33be-9428-ce3b7e42928f | -7.3824 | -55.4924 | 2026-08-17 13:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 55a62052-c0a3-386d-ab6a-605b7ead2824 | -7.8071 | -47.8372 | 2026-08-17 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 047eddb8-0a2c-35b5-97ba-499cb6817fe9 | -6.6384 | -58.9636 | 2026-08-17 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| efac0215-cfe6-31c6-8d5a-1b454bb311fe | -7.8068 | -47.8591 | 2026-08-17 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 1445b35d-6aae-3044-9543-10577031e9b7 | -9.3382 | -62.3344 | 2026-08-17 13:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 116.5 |
| fa0f13f9-2e9c-3621-8a85-cd9ec58c4f18 | -7.7881 | -47.8607 | 2026-08-17 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 126.8 |
| e31bd7df-c79f-3fa7-bddb-ea3eaaf6e59c | -11.5099 | -46.5866 | 2026-08-17 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ad9e95af-f5cd-33ca-bea8-645acc17ba9a | -11.7914 | -51.7767 | 2026-08-17 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 612cde81-c8ed-3dc2-9066-9ce5fddcd953 | -7.6053 | -45.7238 | 2026-08-17 13:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 263.6 |
| 6728b696-c10c-3cdb-b623-f5935fb73712 | -6.6568 | -58.9628 | 2026-08-17 13:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6877eb75-660e-3e81-a5ba-89b01e6b0278 | -14.3722 | -51.932 | 2026-08-17 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 91417455-e825-33b3-b776-a8af1e186e23 | -8.5214 | -54.8814 | 2026-08-17 13:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 121aa231-d7fa-3ac7-a6e5-282a6b9e9e81 | -11.3235 | -46.3182 | 2026-08-17 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 12f83cd4-64ae-3fd1-aa88-d913ee0ecfa0 | -12.5588 | -47.875 | 2026-08-17 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| e101b653-d217-3eea-898a-46fb78deb210 | -13.2805 | -51.6886 | 2026-08-17 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| abe55c23-103f-3e31-89de-c54d2473f779 | -14.3878 | -53.3037 | 2026-08-17 13:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1de08150-b18c-3ad4-b8bd-e7f6fa887c4f | -14.8614 | -46.6581 | 2026-08-17 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 1cd26cb3-3448-34a7-8761-f92780572d3d | -10.5085 | -50.0228 | 2026-08-17 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 140.9 |
| fbec9813-cabf-3ce7-b8cd-adafef0be045 | -9.7553 | -45.7237 | 2026-08-17 13:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| debe8b5f-373c-3885-9b7f-2612eb11b2e6 | -14.8619 | -46.6351 | 2026-08-17 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| c19e8cb0-ae70-3ca9-b3a7-e4a61662feed | -14.3726 | -51.9106 | 2026-08-17 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 7f6e655d-2ab5-379d-92e2-a83ccdc5d4c4 | -11.472 | -46.5692 | 2026-08-17 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 60fc3327-bba1-352d-9749-141c962db55b | -7.1551 | -47.5191 | 2026-08-17 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 27acb168-2231-388d-ad2f-783c253bfb27 | -6.6568 | -58.9628 | 2026-08-17 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5636bbe1-2b6b-350e-b259-a87912d16243 | -12.6817 | -48.5221 | 2026-08-17 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 63332bb1-dca0-3c42-8cfb-98a9e0e6cb3c | -13.5128 | -46.2219 | 2026-08-17 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| b091da61-1172-35aa-96fd-cdbe69cc22d3 | -14.412 | -51.8628 | 2026-08-17 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 117c5e39-41d9-36a9-84ab-ddc2b6da22e5 | -9.3381 | -62.3535 | 2026-08-17 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 5d307cd3-da38-3061-852e-5b6da5d06390 | -11.149 | -46.4994 | 2026-08-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d2563a53-5d14-3920-b349-6157a8466d36 | -7.8068 | -47.8591 | 2026-08-17 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| c8fcfdd9-ece9-3dc3-836a-aaa8ddd7db84 | -15.8246 | -54.1904 | 2026-08-17 13:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 09fe455e-af3d-30b4-81b8-f01331dbfa18 | -11.1483 | -46.5445 | 2026-08-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| e84d3e63-9b24-346e-b6b2-7f52936895d4 | -7.6053 | -45.7238 | 2026-08-17 13:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| ec34f5d6-3f5f-3365-b753-3ddae3f7e0d0 | -14.2751 | -53.1287 | 2026-08-17 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 5c552a01-e9e1-3607-84e5-c805917570df | -7.7881 | -47.8607 | 2026-08-17 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 6824ef5b-80d3-3c27-b76b-c6fe1a6596a7 | -11.1296 | -46.5244 | 2026-08-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| ed3a72d6-c464-3e5b-ad2f-e6a083bcc2e3 | -11.5099 | -46.5866 | 2026-08-17 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d679acfe-5f77-3696-9756-b92cef0288d2 | -6.6384 | -58.9636 | 2026-08-17 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5c3e684d-0f91-32da-9449-5ac9a4fe7165 | -14.8619 | -46.6351 | 2026-08-17 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c474750d-9612-36e8-95ac-4f5f1fb0abf0 | -11.8294 | -51.7725 | 2026-08-17 13:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1f471c95-2068-3b5e-9290-200ae935a21c | -14.8614 | -46.6581 | 2026-08-17 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 739d9667-0b6b-3fcc-9a3e-f7ff0075f943 | -13.5124 | -46.2449 | 2026-08-17 13:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 72dc30db-0f98-3e6c-94d1-4a47ff2a974e | -11.472 | -46.5692 | 2026-08-17 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| a07e2b79-ce7a-39b2-8cae-b93f8529c2f1 | -6.7647 | -59.4601 | 2026-08-17 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e320a856-78e9-3891-bc57-f9be3cd9680d | -7.8071 | -47.8372 | 2026-08-17 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 64c776e0-c466-30c3-8f9e-41c581f1555c | -14.4871 | -51.9806 | 2026-08-17 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 02713eea-a33c-3236-b275-b305bb61e615 | -8.5212 | -54.9016 | 2026-08-17 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 06fd173a-246b-3504-bfc6-61c36e93b00d | -14.2947 | -53.1052 | 2026-08-17 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 962bff8a-3ac0-392a-bd86-d044a2094202 | -10.5085 | -50.0228 | 2026-08-17 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 18a97708-af91-3409-be1a-08fdb031acb9 | -13.2805 | -51.6886 | 2026-08-17 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 260518ad-027a-3ca3-8763-51d68abeb931 | -9.3382 | -62.3344 | 2026-08-17 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 7befcaaa-b6c6-3c98-8157-64ed75f5434c | -7.3824 | -55.4924 | 2026-08-17 13:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f5ebe2fd-8c2f-3090-a3bf-dc882c2a149e | -7.1363 | -47.5205 | 2026-08-17 13:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 425c72a5-6e85-3692-940f-d1943dbeaf3b | -12.7009 | -48.5195 | 2026-08-17 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| c50eec50-f474-338b-8d80-56916d41c748 | -11.1487 | -46.5219 | 2026-08-17 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 7be02bc7-782e-317f-b2ae-c450d48b8009 | -11.17 | -46.57 | 2026-08-17 13:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa9f9a6c-e4aa-33dc-a218-c76b97e8cec0 | -8.5212 | -54.9016 | 2026-08-17 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 1e8d64e4-93d7-3dfa-86ba-e5cd1b7f165f | -11.1487 | -46.5219 | 2026-08-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| cdc1257b-6500-3597-92b6-8e39f88a9b69 | -11.3235 | -46.3182 | 2026-08-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 9d4111cf-0adb-3aba-9798-434785cd927b | -12.5392 | -47.9 | 2026-08-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| ff858fd2-ca5c-3773-9bd1-a0e2f4667b60 | -9.3196 | -62.3353 | 2026-08-17 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.7 |
| f26b3b94-4afe-3ae7-9db7-6c75042640dd | -14.3722 | -51.932 | 2026-08-17 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 1d904512-8c4e-3157-9562-c4a70873668d | -14.3726 | -51.9106 | 2026-08-17 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| e1c19e1e-4be5-38f0-b3b6-96bdddc33b55 | -14.8619 | -46.6351 | 2026-08-17 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ac0c3ee0-e10b-3b9b-a532-4c2847b2ca96 | -9.127 | -46.0214 | 2026-08-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 638dc9de-19d3-3931-80d9-f50847d49696 | -11.1483 | -46.5445 | 2026-08-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 20877d52-6f14-3a04-a44a-184fb0a63e82 | -13.2805 | -51.6886 | 2026-08-17 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a42e23cd-548f-3036-b255-5e2f95309acc | -11.8294 | -51.7725 | 2026-08-17 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 83f54a48-8cef-323c-810f-88266679b574 | -7.7881 | -47.8607 | 2026-08-17 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 9fb9ca1f-d868-3be7-91ff-fe34767c1870 | -11.472 | -46.5692 | 2026-08-17 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 4a8b633d-9fe7-3726-b462-6f90a65e94bd | -14.4868 | -52.002 | 2026-08-17 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 98607bb1-c6ad-3b6d-b032-c0fd0a1a42d6 | -11.4907 | -46.5892 | 2026-08-17 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b6b9a9cf-34b2-3e15-8d9d-13dbe8663d4d | -14.4871 | -51.9806 | 2026-08-17 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 150.6 |
| bb365246-4bf3-38ac-ac71-32ca26042b0b | -6.6568 | -58.9628 | 2026-08-17 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| bca402f7-32c0-3674-85f5-e289def9001f | -13.5128 | -46.2219 | 2026-08-17 13:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 9294e5a4-b481-37ae-9ab6-882e52a7f971 | -7.6053 | -45.7238 | 2026-08-17 13:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 987ef312-4349-3131-87d5-dc1a44fe5990 | -12.7009 | -48.5195 | 2026-08-17 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 132.6 |
| ac974f1a-84a2-3287-bf54-17676535fd65 | -12.5588 | -47.875 | 2026-08-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 7f77f500-04ef-3f09-9b92-ef7c0935b0fc | -10.5085 | -50.0228 | 2026-08-17 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 6433ab32-e582-31f0-a878-ca499efdd8ae | -6.7647 | -59.4601 | 2026-08-17 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 49408abd-b958-33a0-915e-3f40967f8f3e | -6.6199 | -58.9643 | 2026-08-17 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| e48c91a0-4ac9-38a2-832e-eb8a326ee5d2 | -7.8071 | -47.8372 | 2026-08-17 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 8487850a-42eb-325e-a0be-8c3cd149f6c0 | -9.3382 | -62.3344 | 2026-08-17 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5117b8e2-3f5e-3f87-b769-cb8af3002a92 | -15.8246 | -54.1904 | 2026-08-17 13:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4bb6a2b8-a53a-3607-ba61-bc71b669ee59 | -11.4911 | -46.5666 | 2026-08-17 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| eecb60ef-4641-30e5-93b7-531d465a2901 | -6.6569 | -58.9435 | 2026-08-17 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| ce8f12ba-1790-3546-a236-5c7b5b7c83a2 | -7.3824 | -55.4924 | 2026-08-17 13:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 3179db17-e3d4-34e1-97c5-bb5ffa3f1c30 | -14.3718 | -51.9533 | 2026-08-17 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 3f451885-4922-3898-aa10-d2e57864ac2f | -12.7201 | -48.5169 | 2026-08-17 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 97177ee0-2420-3f9f-bdff-500b732f57b5 | -14.8614 | -46.6581 | 2026-08-17 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e7f4c5e6-7781-3d1d-aae2-aeb7216d6238 | -6.6384 | -58.9636 | 2026-08-17 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| bfb01d9b-b441-3911-82db-19e2b85e2605 | -11.1296 | -46.5244 | 2026-08-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 6a6a37dd-d7c1-35dc-aa7e-3eb7a9691b9e | -14.4678 | -51.9832 | 2026-08-17 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ae40d5c3-3f9b-3170-82d6-8322d8b9d803 | -7.8068 | -47.8591 | 2026-08-17 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| 3cf9132e-e8e0-36a7-a8af-e5b108ec862e | -14.4678 | -51.9832 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 1690d0de-b3dc-3ff9-89bb-8a02a252abd7 | -11.3235 | -46.3182 | 2026-08-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 195.4 |
| c55763d1-f8fa-32b9-ae3b-b13767729379 | -10.951 | -57.1497 | 2026-08-17 13:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 108.7 |
| bde27b55-e75a-3866-8f4d-1aee2958846e | -11.4907 | -46.5892 | 2026-08-17 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 62060a07-969e-329a-9ceb-689d5d226c81 | -14.3722 | -51.932 | 2026-08-17 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 152.2 |
| c5a162c9-b4f3-3677-97e6-f8603ebdcc3d | -15.8246 | -54.1904 | 2026-08-17 13:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |


[Clique aqui para ver as próximas entradas](README69.md)
