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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e6e641b-ea38-37c2-aa08-5781f47c4c13 | -6.20491 | -41.0069 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13436f6c-3278-3921-a0fd-1046315d1871 | -6.62752 | -53.3594 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f48cc2d7-ff50-3470-957f-8a731f459e75 | -6.06824 | -43.11329 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7815f266-8d27-3d96-8dbd-937892b6e118 | -6.35908 | -42.58165 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2e66fdd6-25bd-33c7-9fc2-0fec149cfe99 | -6.11896 | -44.25261 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6dc6cb1-9808-3cd5-ba60-14153b2cd9c5 | -8.2196 | -44.77617 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7449282-6fd1-34e0-ac8d-c6a24411aabc | -4.56171 | -40.33953 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59a56fd1-e4fa-32fc-bbd4-a79bc7be2597 | -5.79605 | -45.65577 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 986496a4-f779-3089-89c2-85070ddc91c3 | -5.44425 | -42.66005 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 411f1d68-7889-3fe2-84ee-83abd20f5355 | -6.40928 | -44.41673 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17061c8d-8529-3237-b6ab-3c5a6a7d4c2f | -6.20439 | -43.37857 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 402d9294-cd46-31f6-a807-599995c8e49a | -5.44692 | -43.433 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa26276e-fd3e-34af-a8e3-487663f9ec22 | -5.92668 | -43.19778 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b2d6db43-e09e-3be3-8787-a9e25d938811 | -6.25818 | -43.69242 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9d8964b-0636-3681-9272-4d2765919b60 | -5.94825 | -45.75304 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bb0e214-abde-3ee6-9bf4-2610c381b8ef | -5.88125 | -45.07198 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09be5fdf-5db1-35e8-932d-8f7080a105f1 | -3.76451 | -41.66157 | 2025-09-08 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 55185134-a8bd-32e4-bad0-f080add77aa4 | -5.883 | -43.97091 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4219d274-d923-3eac-acec-dbb7c4ac7b5f | -6.37615 | -45.91622 | 2025-09-08 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e30de795-9efb-3e4f-b4e6-1922fe096dfa | -6.29967 | -43.32269 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fe07c19-4722-3b49-ba3e-02489fc7aff7 | -5.43579 | -42.66708 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e721a9a-dfff-36d1-b1fd-6580ddf7d2ab | -5.82271 | -44.12203 | 2025-09-08 04:00:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3492d4c7-dbd8-3c20-be24-971af4e7d861 | -8.50083 | -45.111 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f4ba4ea-2df4-3f14-a4ad-fa94858f09b8 | -5.41958 | -42.85869 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 94935bf9-9c71-36e9-8e3f-89784a062229 | -6.13882 | -43.299 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 27d2fce2-4779-3928-a72a-e4f1f49d0d09 | -5.82735 | -44.11789 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db9eb644-6418-3e22-adb8-c897def2fcbd | -6.19624 | -43.60466 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5c3de109-e5c3-3018-8236-6c8fe9c6549b | -6.21879 | -44.18655 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 796b2481-daf7-3ff5-9f12-55993cc700b2 | -6.10255 | -44.14874 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65b2adf4-2366-34f9-8390-d2f2c25772f0 | -5.77256 | -40.92664 | 2025-09-08 04:00:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6e8e5839-5427-3b35-8358-6631cf9c80f3 | -5.35895 | -45.94463 | 2025-09-08 04:00:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03999b1e-0a97-34d8-8d07-9d129337e8c3 | -4.56836 | -40.34061 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7006ca5e-56ce-3969-934d-81c77bfc684d | -6.19646 | -53.26955 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017dab20-9a6b-3d52-8535-ee62a306a8d4 | -4.41533 | -47.61051 | 2025-09-08 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a2e8780-ea3e-3abd-bfd0-e2563c85f884 | -7.56018 | -37.18891 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7655f7f9-a329-3ee4-b2bd-1995816f6a7e | -7.81562 | -45.43348 | 2025-09-08 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab9581af-618d-307d-a382-a705025b18d4 | -5.76466 | -40.95451 | 2025-09-08 04:00:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 7fbb5ee6-18f2-3cee-b668-3090ac0000c1 | -6.8746 | -45.53959 | 2025-09-08 04:00:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06b4dfc9-6661-39d7-bf77-e9c75dfc3230 | -6.99846 | -44.93223 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c81f8c2-efb6-3d5a-b791-ca59697e45fd | -2.14129 | -47.71414 | 2025-09-08 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e58d64b9-cf42-31d6-b61d-18bebc03a729 | -6.10218 | -45.46391 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c9e1093-30aa-36b8-8e08-25b5d9c25703 | -5.73715 | -43.93631 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c82d61ad-103a-3673-9620-f4285adca2e4 | -5.67402 | -45.45441 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771cbae4-15f2-32fc-b4c5-fae16df56de5 | -3.30851 | -48.71534 | 2025-09-08 04:00:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0e68558d-4be3-3751-b8aa-73ac250e5973 | -4.66105 | -46.36073 | 2025-09-08 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f6788cc-253e-34d0-853f-8c31a2d0a601 | -2.7892 | -42.8464 | 2025-09-08 04:00:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5526ae5e-1184-3ea2-a55d-db175e8f7ac9 | -6.04116 | -44.42835 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d0f5f92-7c21-3eda-b3c4-55d1e2a8aafe | -5.74053 | -45.36643 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9910df21-2fa2-3b48-b6f9-23fa27abe6be | -5.94567 | -46.16109 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0cc1ef6-7edc-3aa7-be53-9c1fa39ccf4a | -5.35319 | -42.64246 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8657d0ec-a819-3f94-acd6-d7b8598a8161 | -5.87716 | -45.07133 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 292152de-5f9f-34e7-93a2-0a3430d21de4 | -5.75603 | -43.1188 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c2ece48-c308-39e9-b638-a8b1634f6974 | -6.68555 | -44.78369 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13dd2eee-4339-3c49-b913-10c7261742d6 | -7.39563 | -43.99457 | 2025-09-08 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 125144ca-606e-3bcd-b6e5-92047ee06c14 | -6.27196 | -53.43835 | 2025-09-08 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0993036-ed86-3470-a366-bfc6ec9f0913 | -6.2075 | -42.64417 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 44d79cb5-993c-3ce7-9145-ac016c4937e3 | -8.49061 | -45.17141 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92eaf48f-f57d-369b-a3bd-a0bb08be6af6 | -7.42773 | -49.25952 | 2025-09-08 04:00:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e6968e6-6d70-3a22-b4a2-02725c709c14 | -8.03598 | -43.81345 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5602230e-ef94-3e98-ab31-4f284aaf2d74 | -5.72056 | -43.89505 | 2025-09-08 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e31c2fe-ff9f-3f23-a299-6ccf7b3fa625 | -7.97622 | -44.83579 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ae5f2332-a17b-3957-86fd-de0de5ac428f | -5.87266 | -44.1794 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90536741-ba55-3d8d-89f9-37dda611bcf0 | -8.03231 | -43.81286 | 2025-09-08 04:00:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5c328b70-30c7-32a4-89c3-83a60c23c182 | -6.4002 | -42.98897 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cab50e5-043d-3bae-ae61-f56602e88ff7 | -6.20281 | -42.47265 | 2025-09-08 04:00:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3c0eec99-1a1a-32ec-b5b6-675649d694a3 | -5.73006 | -45.17548 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b638331-c15e-36f2-bc95-98d23e11d8ed | -6.19722 | -40.96935 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f907a52b-097a-37cd-9518-bafc664a4745 | -6.19409 | -43.37247 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a84c9e3-e172-3a96-920d-8464ca0641ea | -5.42989 | -42.81762 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 23228d13-1ba9-3d3f-8cd9-51594c4b9147 | -6.36711 | -43.52736 | 2025-09-08 04:00:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5f05f1b-32a2-32ec-9596-48aaa1ddecec | -5.5473 | -43.79454 | 2025-09-08 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e75f0d47-6a0d-365a-8d20-cf9c63200747 | -6.19204 | -42.64996 | 2025-09-08 04:00:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0a074f3-4113-3721-b367-368aefc5d585 | -6.23279 | -45.61199 | 2025-09-08 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee5800bf-7874-332e-9ee8-1ae615ed3fc8 | -5.72668 | -45.37225 | 2025-09-08 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f089da57-a896-3a9e-b76b-8f07921a3008 | -5.44992 | -43.43809 | 2025-09-08 04:00:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f043758d-7d49-3534-bfb0-54b82f256486 | -5.45052 | -42.80399 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 44bce9cf-fedd-3a8d-9024-4da35a37e256 | -6.59838 | -44.00705 | 2025-09-08 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6140a38-96ff-33f5-9614-f9201ff62d60 | -5.91009 | -44.17879 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9fe879b2-1800-3dd3-9812-91f85fb17e64 | -6.03059 | -45.89199 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec1fb51-6de8-31bd-aa31-56dab70c8d0e | -6.62629 | -53.36583 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1cf30e9c-e2b3-33bd-bf46-bbd218800a8c | -5.86724 | -44.18835 | 2025-09-08 04:00:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be753459-e82e-35f5-b269-5563523b0c6c | -6.13591 | -47.30827 | 2025-09-08 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20d6c42f-374d-339b-b8a3-6f2fc987b35b | -6.17912 | -44.7364 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 39e4ceee-79e4-3062-999d-65722778976c | -6.17675 | -44.77535 | 2025-09-08 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d0b486-aed6-31e0-8151-0d171fdb2e5c | -5.32453 | -42.68376 | 2025-09-08 04:00:00 | NOAA-20 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a66c0064-0f3f-31d8-aac8-91de592661aa | -6.122 | -44.25818 | 2025-09-08 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc47ec88-6b06-38ed-bd7a-83c3a2f2fa3f | -7.08654 | -43.8932 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 257120c2-240a-3b3c-9623-6df4a0219492 | -6.19549 | -43.60911 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 378adc3f-1c48-39ac-9850-1aef3eec90e5 | -6.31405 | -42.20457 | 2025-09-08 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bc30b267-04b3-37cc-b773-bafbf2a50bd1 | -6.36046 | -43.13258 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db4c6432-e879-3bd0-99c4-36956e70f751 | -5.43613 | -42.80175 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2c9b0ae2-c76f-3e17-b7db-8103675ce574 | -7.42186 | -49.26186 | 2025-09-08 04:00:00 | NOAA-20 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d2a53b1-b12c-3df9-9b16-ea7f87d7ff1b | -6.30291 | -43.82323 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7092afd-fc1a-3460-8dbd-348ef6fd774e | -5.49404 | -42.66242 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8449f4fe-fd2f-30c8-b247-74510c70ceed | -6.08144 | -43.35153 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aecba741-c649-37e7-89fe-af8ef43bd6bc | -6.9233 | -44.34345 | 2025-09-08 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93c717bf-8cd1-3947-be52-b3552c7a2019 | -6.14062 | -47.30917 | 2025-09-08 04:00:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 66d6a53f-4abd-32f0-81d4-851ec4082d3a | -6.0837 | -43.36071 | 2025-09-08 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c74587c9-dcf7-304e-b677-71dad39bf4a8 | -7.08134 | -43.90154 | 2025-09-08 04:00:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a30ebc25-f3fd-3b98-9b23-fc2f074a167d | -6.46038 | -43.95021 | 2025-09-08 04:00:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README30.md)
