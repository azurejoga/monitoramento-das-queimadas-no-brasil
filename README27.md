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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d9c3256-72e6-31f2-aada-267e10072bb9 | -1.47926 | -54.96422 | 2026-08-24 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80132436-bdcd-3489-9833-66031288b9bf | -5.77734 | -50.18524 | 2026-08-24 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7041c85e-9e07-39bd-938b-e96a58256ea0 | -7.29614 | -43.0011 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 2f0ae500-66ad-3814-b18f-0f44ec90267f | -7.02966 | -48.01236 | 2026-08-24 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e74d0fb4-a678-3b50-b027-2eda86b8658e | -6.12043 | -57.8392 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcff6099-b035-354b-9d41-53ba9f2f1419 | -7.37136 | -45.80829 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f79cf2c3-bc5a-364a-bd4c-dc4c68c2eacd | -3.47323 | -47.69834 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f316c877-7e64-3a94-aeb3-7a4dc5299a22 | -7.36478 | -45.82623 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 145e9f92-6057-30f9-aa25-3de71c18a4f8 | -7.97399 | -45.2647 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f1323aa1-160c-30ca-aac2-dc6be064d960 | -5.06758 | -49.37034 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88d0e3ce-ec74-3919-afba-ca8b1afb86ee | -6.15351 | -57.94654 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c85f06e6-3d47-37fb-a072-b76e777e53c0 | -7.26713 | -49.89745 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80251f48-2144-30be-afe4-ec9c682b881b | -3.5942 | -54.05147 | 2026-08-24 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea08afc8-e089-3039-b964-ae597ab95969 | -6.18082 | -53.52535 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e14c620-866d-35a1-9f7e-9a7c3b4f6ddb | -6.19663 | -53.5233 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53dfee3c-e878-3e88-9297-5b712a72ac15 | -7.36099 | -45.82569 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8049ffa1-c71c-3aab-8e53-59dd327ed356 | -6.19586 | -53.52787 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43d89941-e1fd-3638-a0d2-3f6c0ab56835 | -6.35065 | -55.86399 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bd196bd-dbec-3f7e-a788-265f32308bfd | -6.33541 | -55.87433 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88a5582a-f646-3372-b7d3-4a3f7d091f81 | -7.29094 | -43.00502 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d6d5de3b-9d74-3f10-a7a9-252ed746d303 | -3.54005 | -48.18047 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c1144966-7f51-3d89-9e6a-a5c5bb12bbf7 | -6.7021 | -52.08738 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f59cd71-54c2-3c85-b3c6-7d3569975f6c | -6.19287 | -53.52266 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26cf649c-5ffb-3678-a807-2db285988779 | -7.02284 | -48.01133 | 2026-08-24 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46bf338d-05de-3807-8184-a334b4543856 | -7.36029 | -45.83029 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 694f8e65-7772-3679-afa0-95ee41912ce9 | -6.3477 | -54.75682 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa3cc383-a543-321b-b61d-3669e276de1e | -7.26437 | -49.89346 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72541579-1cca-330f-8f90-01cea45763ae | -7.25167 | -49.8666 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 63c78555-b2a0-33e3-973c-c1cc7ebbae28 | -3.4234 | -50.0961 | 2026-08-24 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb4d2764-832a-3502-9471-7c5769fbce60 | -7.36449 | -45.80247 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ab8faf3-498d-3d71-8ee7-858ce8c9e8e8 | -4.9305 | -55.77544 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4d4c750-f285-3f24-af56-1c14b95234da | -7.02625 | -48.01184 | 2026-08-24 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50636166-7e85-3188-a313-f7ee35efedce | -3.42396 | -50.09258 | 2026-08-24 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 516f0f5e-626b-3491-9441-ab192d9cd19c | -7.09537 | -43.37459 | 2026-08-24 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 77c56a29-137a-39c7-9cbd-9ee197668e65 | -5.27697 | -45.1057 | 2026-08-24 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46ab3c6b-ab20-3475-b68e-90c9c13768e0 | -5.65215 | -51.76989 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d6f0f2c-4c0f-34cc-88ff-c94b31b5e5c5 | -3.9678 | -48.95633 | 2026-08-24 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8951e8ee-639f-3d5c-83dd-a3f68abd95f4 | -6.34557 | -55.86747 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a32504-b921-33e1-9860-1600e8c5bd29 | -7.1915 | -42.75443 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0cd74c3-3469-380d-9ffc-fc2da215dec2 | -4.99928 | -56.13449 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e34af4b2-cf62-3cc4-bfb7-56561b6a2741 | -7.17904 | -42.74272 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fd4b86d6-e73b-3f70-974a-75f9fd3f151a | -6.70148 | -52.09122 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12c37d32-a2e4-3e45-bf01-a47dbdf08219 | -7.36926 | -45.82217 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f29eb3f8-3eaf-3ba9-a836-ca1323c46689 | -7.36069 | -45.8019 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 037bac94-dcfb-3020-8f60-624bbae7b9fc | -7.89401 | -46.32341 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd28e2e7-df06-33d8-be23-48e9583447e6 | -6.59549 | -52.45331 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cd40c951-73c3-32ff-8ba7-ddee5d6398f3 | -3.53672 | -48.17995 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d4ef2d05-0cda-33cc-96f0-efa3b114fb88 | -7.24672 | -49.87646 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b50138e4-500f-3462-9c25-0e13af4165a9 | -5.90447 | -56.93175 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3076014-391e-3bb1-bee0-c829916f64c5 | -6.51233 | -51.44041 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72dd0365-50f7-3395-9dfe-784a1a31452b | -4.93636 | -45.79688 | 2026-08-24 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3fd07af2-8ead-3d51-9bb6-c8e221406c07 | -7.29159 | -43.00043 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b0e34f2d-8e2a-39bf-a5ba-30e4296b9e14 | -7.3562 | -45.80598 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a3599a9a-857e-329d-a610-5e6f2181badb | -6.14342 | -57.94483 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e432271-3bf2-32a1-a7ed-ed4591c7d857 | -5.63159 | -48.4199 | 2026-08-24 04:44:00 | NOAA-20 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 90be1b18-f5f0-3f15-97e2-e0061a30d88f | -7.29549 | -43.00568 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| be477215-6051-3e8b-8f73-b219e0f49706 | -6.12146 | -57.83334 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c23e61a9-143d-30f8-86fa-48e99acde772 | -7.24505 | -49.86555 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b488b56d-3c15-3a68-b83b-33bfba77bf70 | -4.60708 | -55.74128 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efc4c116-ae72-3044-ac3a-3fec44d28bbf | -6.83739 | -52.50368 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 7c06982c-26fa-3234-8821-57693b693d14 | -4.99852 | -56.13897 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1df6147b-585f-3d6f-a4d4-5424c4fa4f1c | -5.7801 | -50.18926 | 2026-08-24 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5456277d-628f-3789-a4c5-1fdc2268a1c4 | -7.48109 | -45.126 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2c80964-eb6a-326a-a6b2-4c61d9b75b68 | -4.46607 | -55.66279 | 2026-08-24 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bebbde9d-94b4-39b4-b6a1-aee6dad92934 | -6.38092 | -54.97929 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8992d18e-fa64-3de1-a4c4-e7b233b16939 | -4.48948 | -55.46801 | 2026-08-24 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1b708f67-e15e-30e7-8a81-87731d3bcbb5 | -6.12544 | -57.84004 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d71a751-2aef-3818-98ec-ebba938178c9 | -7.89772 | -46.32394 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4c167c8-4e2b-36ee-8627-e37648270b80 | -6.12092 | -57.7488 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 893ef16d-0fa4-308e-8aaf-a1ccbbee4402 | -7.48821 | -45.13275 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c108697-39e0-3750-92bb-c8d606cf7a9a | -6.80094 | -42.66805 | 2026-08-24 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2cd13456-c833-36f8-9af2-183ed657094a | -7.37305 | -45.82273 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| efaf5da9-88ab-30fa-9cdd-4e5f81fa5587 | -1.7442 | -55.25039 | 2026-08-24 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eea1783-985c-38f6-ba76-467e70fa90d6 | -7.25222 | -49.86314 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b19d183-7502-336b-be94-438a07792672 | -5.94342 | -57.73317 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e0d2eb1c-3a63-3f42-b2a5-b99c800fd26e | -6.62049 | -53.34764 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2ee49d2-faba-31f4-a8b6-832df0750907 | -5.0742 | -49.37138 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 369ab1a2-026b-3453-a3c1-d7513e5ce09b | -6.12493 | -57.84295 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76d15066-7dfd-30ac-b89e-4aafb45613c6 | -6.84158 | -52.50026 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1b29cca7-dbb6-32ec-8d0b-034640913410 | -2.82691 | -48.65315 | 2026-08-24 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5f7a5db-83cb-36fc-81c3-2540b463444f | -7.14646 | -43.09126 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c443abaa-1a7d-33f5-828e-bd2ab68b16fa | -4.47051 | -55.66348 | 2026-08-24 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fad89e88-875f-337f-8ae9-392404025eb5 | -6.95247 | -42.69039 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 649fd076-b7c9-3d71-98e2-9f4a9f000617 | -6.12053 | -57.74824 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db03a5a4-98d9-3fa3-aa17-4a87e4c56e63 | -7.14964 | -42.78261 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ff4f416-8d3a-3581-b3f6-214c4c70909a | -6.38379 | -54.98721 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96929a61-b75b-3d9b-8bd4-7e67cca2f0f1 | -7.15356 | -42.78812 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c9792828-d6d4-3e79-b360-ee71be977ee2 | -6.3309 | -54.75768 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96cab5f4-5207-35d3-91fd-1673de87a077 | -5.00907 | -47.06416 | 2026-08-24 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afe02bda-4178-32db-8bde-4b0823662cd6 | -4.64779 | -50.93134 | 2026-08-24 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c1d6e1d-2dc5-3fb3-8765-09e9b0c0eb39 | -4.48582 | -55.463 | 2026-08-24 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 492ee145-2270-3e52-85c8-cfcd623e72f4 | -7.75575 | -46.1562 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f1b4917-0b6d-3ba9-8a02-84ddb8a2d128 | -7.36757 | -45.80771 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8360a3da-bb07-3767-a307-1243b462cd2b | -7.97004 | -45.26411 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0f15ce9b-5200-3cad-b57f-3446bc4876de | -6.77114 | -44.90129 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b63957d9-d017-35b8-b736-c031fb949a81 | -6.41434 | -48.58511 | 2026-08-24 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42b09b65-8c52-3eb5-9c22-12a44f34f537 | -6.38029 | -54.98296 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea5b9a97-210d-3f6c-8788-1ff396bb4dfb | -5.97861 | -52.21504 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a83fd293-e2a6-3ae3-8d99-edefdc7b305a | -7.25003 | -49.87699 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d9f9919-aeaa-3ffd-9802-87cdff5572da | -6.84445 | -52.50491 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README28.md)
