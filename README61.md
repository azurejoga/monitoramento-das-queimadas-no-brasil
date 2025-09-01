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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2da1c55f-b894-3270-bd79-8009207b33b5 | -7.28272 | -60.66118 | 2025-09-01 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fbbe6680-fc8a-354d-b2e3-ced006c94fac | -7.06966 | -44.33509 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cea0ca4e-3fc3-3617-9880-ab20bb03a0f5 | -7.48047 | -45.9962 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4d86e18-55cd-3400-bcca-602a9805d5cb | -6.23395 | -41.81081 | 2025-09-01 04:32:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 801d45e3-68d2-3fad-a66c-3b76e697d569 | -7.58276 | -42.71357 | 2025-09-01 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e5e2851-b0f7-3c88-aa9d-f51975f74916 | -7.62318 | -44.95573 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 941293ea-37d6-3c9c-bd7b-af47192db5a3 | -11.07542 | -44.6572 | 2025-09-01 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 058bb907-2270-38c9-8cbd-95e60d56875e | -3.63605 | -49.20676 | 2025-09-01 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4526a433-3440-3036-b37e-ec03ee67818a | -6.83813 | -52.81705 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| af1bfc9a-f359-3805-8eb5-428bec5f91b6 | -6.16872 | -44.12204 | 2025-09-01 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f1fb061-23e9-3e32-86c3-c347d51a7ab2 | -6.75292 | -43.78978 | 2025-09-01 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 16d29e72-122c-30bc-b665-bd5f9ef17f66 | -7.93991 | -46.44756 | 2025-09-01 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90e5c056-9e7f-3e26-818f-551dd68f02c2 | -7.40025 | -47.4386 | 2025-09-01 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87fbfbba-a31f-31d9-b67f-92aedba57736 | -8.85071 | -52.02227 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cfdf766-d03f-3a46-868f-99a259b0d2d3 | -7.061 | -46.24406 | 2025-09-01 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35dacda9-4917-31db-bc27-09873cde0c73 | -9.50281 | -48.83968 | 2025-09-01 04:32:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9983ca67-9952-3249-b3ae-4b2feef9c316 | -6.09365 | -43.18941 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0281923f-e08d-3e6b-ae27-1050bb1ddf0d | -7.11242 | -44.77325 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 981dd2d2-cd94-3ee1-95b7-a9c51174efec | -5.75973 | -53.40577 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a417032-a9d9-3fd1-a40d-26c653eb673e | -6.33519 | -53.43733 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e6db16f-258d-3445-b171-96844d494509 | -7.11432 | -44.76057 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5492c941-a9e5-3089-af46-6e8727176f17 | -5.83385 | -45.20099 | 2025-09-01 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e62ec808-d3f6-3550-807b-d30711d2659d | -4.24455 | -48.64486 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4926d41c-87a4-3abd-b022-485795f62f6c | -6.58139 | -43.71451 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8346c86d-d6e7-3bb1-a9c9-66b3ac94fb01 | -6.15941 | -43.33916 | 2025-09-01 04:32:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f16795d-1665-3d89-b62d-28736a2b713f | -6.42436 | -43.96703 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5cceec3-c442-3299-9cd7-4aa6f302a5e6 | -9.93134 | -51.61353 | 2025-09-01 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3e1acbc-269e-337b-9279-065ba2a11eba | -6.29971 | -43.63734 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0aebb8b3-c192-3bd8-9e64-79f7e144677f | -9.67212 | -47.82365 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 621859bd-53d9-3087-8805-250b931064f4 | -6.32975 | -43.56749 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27fbd184-2858-3e4f-b151-a0b2798fdfc0 | -7.57917 | -42.70919 | 2025-09-01 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a94bdfe2-b95f-368e-b48a-5523ccbf0b9a | -8.84458 | -47.49114 | 2025-09-01 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ea9a4de-4c07-365c-a0a9-377290909682 | -5.99304 | -44.71718 | 2025-09-01 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 682e4b7e-e806-32e1-801f-968ce127cae5 | -7.46001 | -44.82198 | 2025-09-01 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebba7407-7b81-3a08-962a-285ab141deef | -6.46408 | -43.96223 | 2025-09-01 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee860c5d-0078-352f-b841-f6b41e08e42a | -7.07205 | -44.34452 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85a84434-f123-32cd-867d-d0f19d3fcad1 | -7.87514 | -45.17339 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d695d02f-81bb-3e36-b3a2-780b91d29f49 | -10.04353 | -48.12048 | 2025-09-01 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58a34f44-fb5e-38e7-a0bb-f58e3f6f4353 | -9.27195 | -47.07684 | 2025-09-01 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d4bd370-f7fa-3393-81e4-d31d78ed4849 | -7.1057 | -45.3465 | 2025-09-01 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98aeaddd-602e-3aa9-a24a-df191aef2848 | -5.62599 | -42.62347 | 2025-09-01 04:32:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 03e35f63-cde0-3095-afff-29df860142c3 | -6.33998 | -53.43424 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d60bce2d-8edc-3588-a350-5d19976bb798 | -6.93439 | -42.01854 | 2025-09-01 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 276c1581-87c7-33fc-b88b-4c0c12ff0270 | -7.55825 | -45.94141 | 2025-09-01 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8d481ad-ab33-3eb8-9780-a34de59442af | -7.41929 | -44.08787 | 2025-09-01 04:32:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a7cedc4-47fa-3aba-ab99-3b2cf38e2bd1 | -4.07123 | -47.9598 | 2025-09-01 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 394b33eb-f54a-3671-b1bd-acfb3692b8bb | -6.31688 | -43.78375 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0bf18db-ea0c-333f-8cf9-5e9b9cc492ef | -6.32686 | -53.43592 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8118e7b-eed6-3c3c-8815-9df9e6db8e8a | -6.48253 | -43.57038 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bb58885-fbe9-3f7a-84eb-6dec07a3ab7a | -8.85 | -52.02662 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8572be37-82cb-3eb5-826b-fc084c7c2b5a | -4.92468 | -43.18537 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a409404-fe48-35a0-9e7e-57191c4c5b61 | -6.63796 | -43.96176 | 2025-09-01 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a84fdf64-eefb-360d-a0e4-72f00172be48 | -9.64105 | -47.82598 | 2025-09-01 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fc3bb66-3a75-346c-a249-c6fa73d27afb | -8.33671 | -47.44115 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cec2eb2d-1724-3456-960a-7269d4c81b67 | -5.81334 | -43.86753 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 319cdc0f-0b73-33f3-a6e0-8658bdf0fa70 | -4.79322 | -48.12054 | 2025-09-01 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cfc157e-8c68-31f6-99aa-ecea47cb35fd | -4.91219 | -43.18138 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df409d08-4869-3743-9c0a-12c894754e9e | -6.84606 | -52.8184 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0eb03c8-37b9-3e1b-9f9d-7dabcb0aea30 | -8.91675 | -45.86916 | 2025-09-01 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6f8dcc1-0a6b-3c6b-a0c3-53c9a4ce96df | -7.5822 | -42.71735 | 2025-09-01 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd264211-49b4-3acc-8d63-67379c8cbbfd | -5.56743 | -47.41128 | 2025-09-01 04:32:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1653594-ba7d-3993-aeae-4c997d5971e1 | -7.08456 | -44.33718 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98df96c1-30a2-318a-aca2-beb5638142b5 | -11.04388 | -45.14292 | 2025-09-01 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f0feede6-269d-3422-8e6a-24985b004930 | -7.61358 | -42.65955 | 2025-09-01 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c515bb6e-552f-37d2-9cf7-eaa312174887 | -8.86756 | -47.95602 | 2025-09-01 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaced081-cea9-3d4d-9a0e-847a6cdf377d | -4.92153 | -43.17988 | 2025-09-01 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a82c8014-b975-36e8-b187-95759da3be11 | -6.29901 | -43.6421 | 2025-09-01 04:32:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a0cc95-2471-3388-91f5-43128f25504e | -9.13756 | -47.96664 | 2025-09-01 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96e54fdc-3a12-3b3c-805c-560b35c32850 | -10.57981 | -44.85041 | 2025-09-01 04:32:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2be3618-a408-339c-8525-0e7b996a3e54 | -5.86971 | -46.49709 | 2025-09-01 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92a2fd4a-fba2-3e9a-804e-46b4b40b7b2b | -7.78089 | -50.05842 | 2025-09-01 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e0bb1cd-2b21-3c3c-af73-418582a8161d | -7.08322 | -44.34611 | 2025-09-01 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e0133678-86ea-3fb1-8cbd-8e8eb5a20b68 | -8.43077 | -47.35795 | 2025-09-01 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ba885f0-5db0-32b7-b8af-460d3ddb3daa | -6.81625 | -45.69753 | 2025-09-01 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 530bc653-286f-353f-a9ba-c90b45522912 | -6.09291 | -43.19431 | 2025-09-01 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 02eb2b3a-a93a-30ba-83a3-5457dcca1447 | -6.37044 | -43.55915 | 2025-09-01 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 727907a2-ffaa-3af9-9734-94fdb16c8070 | -5.88327 | -42.98845 | 2025-09-01 04:32:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f9bbacf-8b34-3391-8c30-b7798cb09220 | -7.16599 | -48.19513 | 2025-09-01 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54687beb-71e1-3907-b982-7ab89a56d968 | -6.29094 | -43.82715 | 2025-09-01 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27baf80a-8751-379a-9289-612620302c71 | -8.1229 | -45.03675 | 2025-09-01 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bda6210-20b2-3912-afd4-9723c5897f85 | -3.00998 | -47.83918 | 2025-09-01 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3c34408-3f30-3d23-a8eb-b70b7d898c2b | -5.6615 | -43.64156 | 2025-09-01 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93f680aa-bc6b-36f7-b50c-44917326a02b | -6.34077 | -53.43752 | 2025-09-01 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1b5c6c3-ba23-369c-a114-f9d85b8e17cc | -13.9883 | -44.53014 | 2025-09-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4353ea6-5508-304b-858d-b877b37ea730 | -12.14175 | -47.18982 | 2025-09-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d1667df-da32-36b3-a343-2ce5edee0fd4 | -13.51415 | -46.99019 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dbdfbfd8-6b78-3476-a60d-de3e3d89ae48 | -11.80494 | -44.94466 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4c1a0d4-d0bf-3647-a714-c0b269a65c29 | -12.38824 | -46.47289 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb4788ec-8453-3c3b-8e40-08327ce8f6d0 | -11.01105 | -46.9415 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd2ca8b3-f56e-3679-be3a-f9de3cba1738 | -11.63801 | -46.83822 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9264299-3210-3de0-9eff-b63889c3422a | -16.29517 | -52.93842 | 2025-09-01 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59eeff93-83a3-333b-8180-8ae8000c99f8 | -14.00797 | -44.5069 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd6aee24-22f2-302f-8a99-ab03f772d09f | -11.36857 | -43.62264 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be33b25-201f-34ad-a8a3-f298978242f3 | -12.78234 | -48.09336 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcd1d553-7d7d-3d26-ace7-559101d2910c | -13.50617 | -50.80936 | 2025-09-01 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9238705f-8f47-36d2-ae39-b57e1aff8bc7 | -15.70501 | -48.89682 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d64a4468-43a1-312d-85a3-b7e3c6d46b77 | -8.76169 | -61.43444 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 559870ac-9801-3f45-aed5-76021b1ddfa6 | -11.82335 | -51.46659 | 2025-09-01 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39a659a9-d140-377a-8ae2-361461041fe3 | -12.8053 | -48.07825 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3f33f01-8439-321c-8f83-e2592197b28e | -14.45998 | -53.0535 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README62.md)
