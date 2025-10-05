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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8da1799-3ac3-3d7f-8ac0-e97b373f3285 | -5.79099 | -42.59143 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0fc03684-da26-30da-9bf2-2525d7a7ec72 | -9.75784 | -47.74022 | 2025-10-05 03:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e84ea35a-8eab-3441-9d3d-07adc1b56bad | -10.01105 | -48.26748 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19676fad-fa4b-3af2-9c41-2c96745738b9 | -7.79897 | -42.56988 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1fff1e5c-1cff-3a11-8044-e4cfd009584c | -5.78677 | -42.93023 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 4fa96407-5434-38a7-812d-e1c736c62de4 | -9.04452 | -47.01721 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8b2e43c5-494e-3ac8-b612-392a18af92cd | -6.08249 | -43.48499 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fd4bf92-c196-3d0a-aa3e-a35647886f37 | -5.54908 | -42.66975 | 2025-10-05 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2e7ae85c-2764-321c-ae64-9e15f200f32e | -8.56113 | -46.26997 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ca196921-49d9-32e1-8173-0842740dc31e | -10.01801 | -48.26853 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f22fe466-2550-37c2-b1bc-67e4dcb5108c | -6.60949 | -43.7181 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17ab7cc6-3093-36c4-9ed5-5ff15b3142a5 | -6.6273 | -43.71347 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d19a76-77d2-3e19-a1a2-02b599a3ae3a | -6.9786 | -44.37691 | 2025-10-05 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 825e4dbf-0835-31b6-87a6-3c111cda4728 | -7.05351 | -43.21873 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5eb186a7-530d-3ba9-ad1a-c44f54680dc4 | -7.76266 | -46.30734 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 041bc188-8112-3982-866f-00645f41406c | -9.91916 | -50.23756 | 2025-10-05 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 410c6277-99f3-330e-8b73-a37025921e5e | -10.62335 | -43.31725 | 2025-10-05 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3cba175e-125c-3f33-8690-6bdba59f24db | -7.64735 | -45.42134 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cbce966b-7002-3a55-ba37-9b2363146407 | -5.9701 | -43.50872 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df82d564-4aba-307d-a465-f12107023907 | -5.19733 | -45.07398 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 573cb0c8-6b9c-385c-b3b7-68dc1e4221f2 | -10.64865 | -46.33244 | 2025-10-05 03:53:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fb869484-3af3-35f7-9137-b2eb6c81c911 | -5.6263 | -43.2152 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5b2173d3-e66b-3773-9507-27e22a510fa9 | -5.84472 | -42.87615 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2552776e-14be-37d8-a195-beec9456fc14 | -5.98199 | -42.65277 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f82f1765-c25b-373c-b5e2-b0eb9c6d7a14 | -10.3947 | -45.40045 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fd7d24b1-778e-3c17-bba8-cd8eecb288ce | -8.55536 | -46.27474 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3ae7689f-ce34-3334-b63d-20c421b434ba | -6.40238 | -43.07034 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| deb9bade-57de-3b58-aa26-0d27df7eb9e7 | -6.33296 | -43.45454 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 733e73ea-235a-364d-9c5b-9e255b7794af | -5.47419 | -42.8034 | 2025-10-05 03:53:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f257d76d-d7af-3383-8d0d-0cf10d871018 | -6.46044 | -44.58144 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 786f15e0-1a02-33db-bf35-d849e58e6ea0 | -6.0618 | -41.25145 | 2025-10-05 03:53:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 886c01ca-19d0-3398-88d1-f5c51335f213 | -8.16247 | -43.34782 | 2025-10-05 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 32b599f3-85f6-30f1-9259-30ae330ea1c3 | -6.29229 | -43.9207 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b878a8af-d619-3bae-815a-ed60e103c49b | -6.39968 | -43.60107 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2532680a-8969-30bf-ae3a-a7582639255e | -6.67608 | -42.78414 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b13f8fc3-c605-36f9-ae53-cedfa26df83e | -7.72531 | -46.32119 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7994b41e-e78d-3b96-a914-7024de6196c0 | -5.82329 | -42.44207 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6862bd19-750c-3265-be1a-6f4cf314f8da | -9.12319 | -44.40155 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e9666df-e09d-34cf-966e-31e81e823033 | -6.59494 | -44.3171 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37ac9ae2-14c5-316c-b1e3-bf82b2155d5f | -6.09698 | -43.49077 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39bdbf4a-1568-373b-8795-5bf88ea74156 | -7.87474 | -45.2288 | 2025-10-05 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37fe55bb-0712-33ee-b981-36cde838d1e4 | -6.41296 | -43.05614 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a3a822a-d21b-3ad1-8750-e26afa4c5782 | -9.06436 | -47.0208 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3dff9d8-9207-386d-adbe-29409ce5d1a8 | -6.26863 | -42.44569 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f8b81826-ac1a-39fc-94b8-062f2604d185 | -10.25407 | -44.93971 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d92ad2fe-dedb-3f2a-9043-6fa4a5c357cb | -4.24697 | -48.57042 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f7c2613-874d-3554-bed6-1bd07e27be5f | -6.69541 | -41.95194 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c28294fb-e5af-3358-b5bf-c189ee0901f2 | -8.55483 | -47.6694 | 2025-10-05 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46dfe4b7-d1cd-3eda-9c51-6265ebaec031 | -6.33963 | -43.89639 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f100692-2c76-3a92-ae46-48be7fe7fea9 | -8.53929 | -46.30919 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e41e211d-8f78-3d60-a5e5-1646346ed643 | -5.36302 | -45.95425 | 2025-10-05 03:53:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63dc620e-9dd4-32b9-8eca-8ebc04119ddd | -5.89436 | -42.91228 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 37.7 |
| 746e283a-ad5b-3f4c-bf3d-372b0e8a3ada | -8.93519 | -48.6604 | 2025-10-05 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a47504ec-0a63-3712-91ad-21bbceb64e26 | -6.9211 | -37.43825 | 2025-10-05 03:53:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e6e188c2-7959-3744-aa60-091cab58b3fa | -10.34543 | -48.16144 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c9930d8-85f9-3cd0-be67-f9b6779a62f5 | -6.70449 | -42.17411 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e0dfd25-25ce-3a4c-8dcf-ae3da2a6f296 | -6.10374 | -43.47595 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3b6ef870-27f4-32ae-ae89-4a4f529a206e | -10.38805 | -45.38734 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c9acd97-0f2b-3dbc-8259-641b31b36a20 | -5.83992 | -42.88059 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| e97373fc-0866-3d5e-8319-744df7f56873 | -6.06641 | -42.53329 | 2025-10-05 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fc71ec60-9f23-3966-b7a4-406fdcb29f24 | -6.15428 | -44.65464 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8e727116-f509-3e49-84d3-a6ad45261647 | -5.2781 | -44.8774 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 357ad926-98f3-3a24-85b5-f0b4b0149a1d | -7.16148 | -44.99327 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2d27c56-c3b0-37ad-a2e7-e7c7c73518f9 | -5.89886 | -43.7581 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a92a6405-b81f-3d6e-b162-ec15edc0a69b | -5.92809 | -43.33125 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0533039e-8f7e-3be7-aba8-5aa343e2113e | -8.14299 | -44.08599 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a82ec616-a3bb-325a-8f07-ea417bb91915 | -6.99767 | -42.30168 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d16673f7-bf29-320e-b00a-9f6b2bd6855e | -6.52544 | -42.48097 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb5c52cb-12b3-3899-8f85-3a1bca677ca9 | -5.2295 | -43.76698 | 2025-10-05 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c8f5d24-d48f-33ee-bfa4-46f6a96969b4 | -6.25188 | -44.23841 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b38fece-d2d9-3d96-bb10-cf0c82220758 | -8.56508 | -46.3301 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e323fff-0dec-3280-989f-3eac4690dc9a | -8.56822 | -47.65512 | 2025-10-05 03:53:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba637880-e5da-341c-a2f1-2a188e22acdb | -6.25483 | -42.45782 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b210571b-bf80-3508-948a-d0d6a9b93710 | -6.14984 | -44.65389 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 07eedc21-645e-35ea-9552-87c7f66246b3 | -5.43293 | -45.5061 | 2025-10-05 03:53:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65ddfc7c-5cea-34a1-b62e-3d7f90824118 | -10.19544 | -45.53115 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a272d2e-e6c4-35e4-98b5-0c7ae8250aca | -6.98457 | -44.21334 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30f21c8f-6525-372d-b981-78913d98264b | -5.64269 | -43.91518 | 2025-10-05 03:53:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88cf6a16-dd81-32c6-8477-b93e9ffb15b1 | -8.59451 | -46.30307 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1fa8f671-edd6-3905-ba8e-23c8717e05ed | -7.79 | -44.55093 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 952d9ab1-92b0-37d9-8a39-549f7bc0b189 | -6.1454 | -44.65317 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 02238695-dbbe-3544-bdd0-da0e17625e7f | -8.1233 | -44.10163 | 2025-10-05 03:53:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ba95af7-ae04-35e6-a4d4-a048d2c62f3a | -10.34967 | -48.16787 | 2025-10-05 03:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15bd581a-ad0c-3395-a352-27dc81d3ea60 | -7.20805 | -46.86115 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0750136a-3317-3380-b54b-05828223dd8e | -6.1395 | -44.66091 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0a372c97-2647-35e1-96e0-74bd1262d07d | -6.14243 | -44.67043 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b21c55a2-997f-3683-9950-a91aaac622c0 | -6.42879 | -46.02649 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4595b91-0d23-324e-a0ec-ba4cf00b0c9b | -5.29402 | -43.10516 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7d1d5e9-abd8-31c1-a398-6904dded1ce6 | -6.84598 | -45.48577 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f377045f-dd7a-3fdf-8970-4ae95f18ed28 | -7.03232 | -42.77026 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fa6e0a2d-a482-3e30-8a39-41c4078ae404 | -8.53963 | -46.33511 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6a4ffce7-a61d-30d9-aa72-49af1b2e8332 | -9.91505 | -50.19435 | 2025-10-05 03:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7b5f88a-fbd6-3e77-a2f5-382f927fb68c | -6.45577 | -43.44537 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4cc849a-4c5e-3319-b1c4-6ee22af3d931 | -5.79992 | -42.48798 | 2025-10-05 03:53:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b06680ac-2539-3413-a5c3-d7c6c79616ba | -5.24147 | -42.6339 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8f57f1b3-67a6-30cd-9dd2-6646f1aa1fcb | -7.61653 | -45.46272 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d83f2c3b-0bc1-3b00-94d4-b76df6bd0863 | -6.33886 | -44.02944 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d53f4752-c96d-3494-9834-8f80eda6fa2d | -5.8382 | -42.89102 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2bee5ad2-f0e0-33c4-848f-43b9f1f43477 | -5.9707 | -43.50508 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e299d895-a5c8-31df-bc5c-52e8f1ab62c9 | -5.8013 | -42.72284 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README51.md)
