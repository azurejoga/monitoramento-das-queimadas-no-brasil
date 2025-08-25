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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec8bccc6-5b79-3121-8cef-65168ee2c589 | -5.6284 | -43.44802 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8529356b-106f-365e-b34d-e5dcb4673af1 | -6.77896 | -44.30909 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ce6b542-7746-3a80-8eb3-7e8ed27a17a3 | -4.7772 | -45.33034 | 2025-08-25 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5599b28-1aee-3c01-9f27-5ecfde8e503e | -8.22422 | -49.56269 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6e3943a-a51f-37ac-99a9-e7b03f3ea141 | -5.72128 | -49.10266 | 2025-08-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aea03ca8-105d-37ca-b1f1-1bd0655c45fe | -8.05901 | -49.69258 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 02382de4-8d2b-3367-8cee-ce9b1dcb6d8a | -5.36965 | -41.21297 | 2025-08-25 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5929402f-3e07-33d3-899d-a508be27c30b | -5.6408 | -45.15231 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1008f3d-034a-3467-84b6-fadb39292ce3 | -6.30385 | -43.76152 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d280bf2-60e5-3c9c-bee1-a1cdb220062c | -6.38576 | -43.26101 | 2025-08-25 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7d85209-ef1f-3dd6-944a-d792c1eedeb9 | -6.03263 | -44.2087 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f11d474-9553-336b-b9dc-b364901a031d | -6.30662 | -43.7655 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3663d0d0-7146-3a02-9a14-8f9f7df2bca7 | -7.54023 | -46.02532 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 37c7233d-5cce-3399-a365-c06b2adbbd9a | -8.3885 | -47.9941 | 2025-08-25 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1fab89d-9ce6-32bd-84ad-a2fae4b8d0ac | -8.06969 | -49.68164 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc73487e-be1b-31e3-8465-2834e1ba3652 | -7.89596 | -45.89108 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b47fc233-b299-394d-b62f-d6f4e9136d25 | -8.77188 | -46.72836 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42ad7e18-edc7-3aca-a51a-921852d1b153 | -7.18675 | -44.65767 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46c689aa-3fa3-32ba-a0be-634628498d90 | -9.52974 | -40.32378 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b2e00d0-d7dd-3f53-b19c-2a2997e4db99 | -3.21425 | -50.58973 | 2025-08-25 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd609cc-d19c-34b2-a739-ffede282b9d4 | -7.18849 | -44.66166 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5712de6-34c7-3189-8563-47cdf56143b5 | -6.03151 | -44.21577 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92a11dcd-8649-3d1c-b489-8254994c798b | -3.43917 | -49.04412 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2aa10a0a-8417-3a90-a383-05425de7662f | -7.58455 | -45.23125 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7931347d-2717-3065-b291-b3082e2f4ee5 | -8.21613 | -49.56133 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0545c68a-c7fd-36a9-96b0-47ed0c7d97a4 | -8.24044 | -45.08642 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5e92639-d069-30c8-873b-51e3a7a445e1 | -7.59355 | -45.2402 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05d7e69f-e815-3ab8-87cd-d1411a0e4b12 | -7.59531 | -46.24331 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d214fa6-b3f2-3005-80db-f437c16ab59c | -7.32149 | -44.53319 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a596cc0-d872-372c-8a8e-34ba4a3fabcc | -5.10775 | -43.21053 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1a0ac269-7130-37a4-b524-dce6c2ceb173 | -6.19622 | -44.14115 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a942624-d643-30c3-8511-3d953eea9d32 | -7.17613 | -45.17049 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e9ef061-8c2e-3c4a-b55c-9cdf148df5c0 | -5.95628 | -46.14827 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f938fbeb-431f-31fd-8bb6-7d8d3025c6eb | -6.89385 | -45.662 | 2025-08-25 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bf56f9f-8366-334a-a016-d5efa7ca4f93 | -3.58678 | -49.42548 | 2025-08-25 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 93c7aaec-92f7-3c6f-952e-224362e7b6d1 | -4.63526 | -41.39894 | 2025-08-25 04:14:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd5e98c8-82ca-388b-b25f-f823518440b8 | -6.91788 | -44.41838 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be9491da-afe2-3d8c-a329-fb70b007edfe | -8.06113 | -49.68012 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 588bca8a-3498-3442-af7d-7cec0f8f3f4b | -6.79117 | -44.33985 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0aaf1eb-68b6-3284-8ba2-92bb67ff7782 | -7.32483 | -44.53371 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e70597b3-fd4d-3937-84aa-3eb9e02988fe | -7.5047 | -45.83711 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| aa1f1611-ea93-3872-800f-0be56bc1c503 | -5.71271 | -49.10128 | 2025-08-25 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 971bc0bb-21bd-3464-bf75-0d7e430c56ef | -6.87001 | -44.39987 | 2025-08-25 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a08a7ae-5809-3e3c-8301-531c2512b70b | -5.3032 | -45.26566 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ed1f3d7-ec3e-324a-8d22-43807e444dd3 | -4.10441 | -47.72645 | 2025-08-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa813284-8538-3874-8baf-217ec74bcbe6 | -5.75151 | -51.71711 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b929695d-e076-339c-a925-f47af89493fe | -6.30074 | -43.88913 | 2025-08-25 04:14:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9ba2f49-ff89-319d-bbd7-f0b465f965d5 | -3.73222 | -48.93381 | 2025-08-25 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5515cbe7-0ce3-33e1-84ed-51396c481318 | -7.29137 | -44.53228 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a95175c-0ae9-393e-8387-390a80571a1c | -5.4912 | -51.16379 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e6b1b0-0eb5-3f91-9ac5-2f26c8888b36 | -7.25873 | -43.66168 | 2025-08-25 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a10ad77-0395-3d62-acee-2578f5d4fff6 | -8.06953 | -49.65669 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8fb337bf-88c7-3a8f-8342-ec8503fdb9fa | -8.54382 | -48.85403 | 2025-08-25 04:14:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b98d744-fbad-3654-b077-fdc32587f827 | -7.28697 | -44.47368 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e15804e-6ac0-39d7-a95f-2ec0f0f31512 | -5.71054 | -46.02725 | 2025-08-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5e938aa-2f5a-35f3-9196-7d1055d67a3c | -7.66428 | -42.67176 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2808f23-c1ac-3fe5-82ba-d3f6aedf4a49 | -6.19124 | -44.12958 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d08b0ea2-3d76-3aec-ae9b-1af3bae74eb2 | -6.03096 | -44.00334 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8d70faf-e591-305d-a762-ff3b26a0836d | -4.81745 | -43.5434 | 2025-08-25 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cf88947-332a-3886-a915-3bba8a0f3927 | -5.74507 | -45.35827 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfd32fc0-b2b3-3be8-a325-db153c0e5406 | -7.65653 | -42.67778 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0407b210-6c2d-3597-a372-782ae33b95c9 | -7.5491 | -44.45055 | 2025-08-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ed957b7-b43a-371c-b2c4-8ba1fdca32f7 | -5.90003 | -37.81827 | 2025-08-25 04:14:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb95860f-b1ea-340f-b5a6-38ebd93dbf80 | -7.62246 | -45.23344 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10023109-252c-3c0e-9858-55c21a0cf884 | -5.87482 | -42.9185 | 2025-08-25 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ed41f8bd-708f-370c-9a7b-21e4d141717a | -8.16965 | -45.06412 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8f18a3f-e9d3-3384-851e-9de5d7575d74 | -6.03206 | -43.9964 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b74e583-22c8-3de2-8130-7a28dbf2b5e5 | -5.67819 | -45.22746 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78de98d4-e6c1-37af-95a9-8a7aab33fc20 | -5.65229 | -45.14646 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24480bce-5c19-3e03-b89b-09c9412bbf0e | -6.03429 | -44.00385 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af05e3ea-830b-3721-a499-c5060ed87f85 | -8.77544 | -46.72889 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 655a531a-9c74-3794-a8a2-a120c809e3ea | -7.60198 | -46.2687 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80ddbf2a-9fd7-326a-84b6-af92ba86605f | -8.06402 | -49.68908 | 2025-08-25 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 055c7bc2-f13c-33e8-b134-c5063b558101 | -6.67932 | -44.42352 | 2025-08-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9796749b-e714-3c1b-8b03-c16b3c03b758 | -6.44012 | -44.5599 | 2025-08-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c765911e-b73a-3cdb-a849-30564466bf84 | -7.32986 | -43.79359 | 2025-08-25 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51eb0a7c-baee-385c-9faf-8f8c59e69641 | -8.23301 | -45.11116 | 2025-08-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11184d6f-90a2-358d-8112-6dda2f0356ee | -5.73207 | -45.39535 | 2025-08-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2298e744-f9d9-3e4a-a272-9daa2673d132 | -5.49173 | -37.26801 | 2025-08-25 04:14:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 498fa467-49cc-3f73-abe4-890bc921870f | -9.52362 | -40.31379 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0809c2a4-ba7d-322c-94e0-414bcc72dd6d | -7.17792 | -45.15923 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 51c3f1ff-439b-36d9-aff7-06c029f40fd4 | -6.03123 | -42.80847 | 2025-08-25 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f71791e2-dee0-30c7-a2c0-8d25d317b545 | -5.88778 | -43.3797 | 2025-08-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01933e96-6f33-319e-a51b-773463329b92 | -7.89942 | -45.89163 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11cc39f0-e403-3308-b732-b55da5cf544f | -3.24311 | -39.5274 | 2025-08-25 04:14:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a81a8409-134b-3b4c-a69a-66b43cb63c3f | -5.37702 | -41.21038 | 2025-08-25 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 833fa12a-1a83-3f4b-8f20-a4cdadb89562 | -8.0494 | -47.33575 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bfc6a6b-cbba-3f36-b4d8-d13a4127ec7b | -2.78194 | -41.87853 | 2025-08-25 04:14:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b8c57f8-d240-3655-9409-59622f10a0e2 | -6.2459 | -43.74178 | 2025-08-25 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f47554f3-03b2-3954-8c76-d2c675599ccb | -6.30163 | -43.75408 | 2025-08-25 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 808327a1-f382-35a2-a844-0723644300ce | -6.80392 | -44.99141 | 2025-08-25 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a224f10c-49be-3ec8-ad65-56373e6d4c39 | -7.75066 | -34.91484 | 2025-08-25 04:14:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0397c317-0e89-370b-880c-e34bab61f4d2 | -7.6767 | -45.40092 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41b24519-4cf4-34cc-8d04-18f4b9ca7645 | -9.52427 | -40.30935 | 2025-08-25 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d88a9b03-f72c-3198-bad5-e7fb04e9902f | -6.75561 | -44.81645 | 2025-08-25 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5463f2a-ea2a-366e-9468-f37c88b7b618 | -3.4581 | -43.3396 | 2025-08-25 04:14:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c0faea7b-5a07-34fd-b8c7-234224327720 | -8.31818 | -47.24941 | 2025-08-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfc0d1aa-7a37-33c0-b021-d4257ce417c9 | -6.03151 | -43.99987 | 2025-08-25 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f201488-300e-3781-a59d-98b82caef029 | -7.59296 | -45.24389 | 2025-08-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e77a60f-4f01-3b87-98aa-d24305352dc3 | -7.93664 | -45.92519 | 2025-08-25 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README27.md)
