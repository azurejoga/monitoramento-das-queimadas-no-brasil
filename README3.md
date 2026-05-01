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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3b72f7c-23f2-3d64-b920-1bcd712e078c | -20.21332 | -46.45322 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ceb65f0-59d4-3191-9644-9a39892bed54 | -20.81022 | -45.1832 | 2026-05-01 03:42:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73b9ff7b-cd78-3611-b433-0c1d72bdb5e5 | -20.21188 | -46.45919 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f0e8e05-dfb0-31f9-8025-631a2a5a5339 | -20.21093 | -46.46345 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| babf492a-acdc-3f9d-94fd-745f57b83919 | -20.20558 | -46.46061 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c002d22c-69d8-300c-b56c-06dec228214e | -21.9509 | -48.03896 | 2026-05-01 03:42:00 | NPP-375D | IBATÉ | SÃO PAULO | Brasil | 3519303 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa64f8ae-4a8b-3995-a3bd-90ad7a2ca8af | -20.21137 | -46.46173 | 2026-05-01 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8270de3-2688-37c9-9f24-e8b5e6e17d92 | -20.81542 | -45.18468 | 2026-05-01 03:42:00 | NPP-375D | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d53c5f5b-bd96-3dd1-b91e-ee02067ede09 | -19.28176 | -41.77961 | 2026-05-01 03:42:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 39a778e0-7eee-3f9a-be2c-29d0b69faca7 | -19.09624 | -40.66787 | 2026-05-01 03:42:00 | NPP-375D | ÁGUIA BRANCA | ESPÍRITO SANTO | Brasil | 3200136 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5e6e373f-1158-3803-bbb0-1d8c49cd85ac | -19.27651 | -41.78315 | 2026-05-01 03:42:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ea5375a2-443a-388b-b983-9d58662b7593 | -18.89233 | -39.92292 | 2026-05-01 03:42:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 68747e01-faa9-3ca2-8c99-59999f3466d5 | -19.36587 | -39.73418 | 2026-05-01 03:42:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b36d9997-fed6-3155-9710-ffc58c0889cf | -18.89136 | -39.92816 | 2026-05-01 03:42:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 64c0430a-57f7-351c-b570-98d96f2eb146 | -18.89626 | -39.92371 | 2026-05-01 03:42:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2760280d-797c-39c6-9066-4707f65922ab | -11.0006 | -45.0847 | 2026-05-01 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 9dc98ead-44f1-3b8b-8013-594299de2208 | -10.9811 | -45.1104 | 2026-05-01 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 1ab0b035-8a27-3245-a38e-44ebe0c3bc4c | -10.9819 | -45.0643 | 2026-05-01 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| cb8c7e95-bc22-36ba-acc5-8738f0e17bf3 | -10.9624 | -45.09 | 2026-05-01 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 4f427174-7e3f-357e-a33f-823ce0caac74 | -10.9815 | -45.0874 | 2026-05-01 03:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 360.8 |
| 41661d69-7b5b-36e6-b72d-a0c6c09c3657 | -5.78883 | -45.12323 | 2026-05-01 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b915bd3-6054-368e-9450-d4f1da9c81b5 | -5.78802 | -45.12799 | 2026-05-01 03:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 778e9839-225f-3e31-9eee-8a943841c6f3 | -5.61105 | -37.53051 | 2026-05-01 03:55:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 2a7dc022-7c33-3e56-aca1-d024657c28cc | -10.97012 | -45.1022 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| fb60a99b-8988-3767-82a9-bae029f66078 | -10.98198 | -45.08402 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 4f238a68-7b1c-34c4-8116-026abcf03f27 | -12.3693 | -50.03034 | 2026-05-01 03:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fcdcea1-1ec5-3c9a-a47f-b9d3df5a3468 | -7.31516 | -46.20438 | 2026-05-01 03:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ac98304-b68f-3689-9fca-c6ac39d7a4ec | -13.26707 | -40.31945 | 2026-05-01 03:57:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 50e22790-d037-3de5-85f5-7bca5f0c2d04 | -10.96591 | -45.10151 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 597b9642-4b96-3c3e-9122-d455b6ba44b4 | -10.97641 | -45.0911 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 3bc8a647-be8a-3e4f-81ec-496dbd7d81c9 | -12.28332 | -44.62331 | 2026-05-01 03:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c1668c3-1c1f-3f73-b88c-8d91755287b9 | -10.97502 | -45.09895 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 5e590f7c-f4ed-3eae-9919-3e6e65f5a819 | -12.3415 | -50.01009 | 2026-05-01 03:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88737d87-491e-3a5b-8d1a-1e41ecda9637 | -11.95057 | -43.3746 | 2026-05-01 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 766cd5e8-b96f-37d9-b900-1f4e66db76bf | -10.98617 | -45.08474 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 753509ca-f92f-3028-b0d5-36bca29b861b | -10.9687 | -45.0858 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8df512f9-035d-370b-acd5-b469ea1e11c2 | -9.56363 | -44.57233 | 2026-05-01 03:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 729e9aea-4b35-36a9-b22a-8ce453daa00b | -11.94977 | -43.37932 | 2026-05-01 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8938673-5d98-3da5-9c3b-9ee9f81a209b | -10.98685 | -45.08088 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 902b46c9-69b9-3168-bd91-26896b48ff7c | -12.34229 | -50.00611 | 2026-05-01 03:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc456caf-907b-3690-b0b7-9f7e0bd15df8 | -10.97152 | -45.09431 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 983371af-60b5-3c3c-b3b3-14445daf07b3 | -12.2821 | -44.63033 | 2026-05-01 03:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2df7fc99-7751-3d36-abe3-a6f55c31c3a1 | -10.74565 | -44.31178 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b15c1ca1-a47b-3a23-9d88-b82b01a0075e | -10.9771 | -45.0872 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 4e6bcd9d-011c-362a-8d15-5d43825440f2 | -12.37494 | -50.03154 | 2026-05-01 03:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 354b3675-4ab5-3b54-a5e0-9c60b0ba079b | -13.36989 | -39.90836 | 2026-05-01 03:57:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1c316dc4-bcff-3b8e-bcef-bbbf2e640309 | -10.96731 | -45.09362 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3f58ce29-3cb3-376e-bc58-db55754ef2bb | -10.96662 | -45.09755 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 992ab957-b9aa-36a5-a91a-3516130e2dec | -10.55321 | -44.33408 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 028e3471-f248-3432-993d-189519dea791 | -9.66999 | -43.7866 | 2026-05-01 03:57:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cce8c2cc-61c1-3bb3-8f87-707a35120e93 | -8.33352 | -45.35945 | 2026-05-01 03:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb928f54-9506-3471-b7b5-c89cf3fe3f53 | -10.54919 | -44.33333 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 169f916a-efd9-3bf2-b601-02d7e00c561b | -13.40401 | -45.64188 | 2026-05-01 03:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5f6f2da-a5b4-3052-a29a-56c56c83179a | -12.37792 | -50.03428 | 2026-05-01 03:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99c672dc-6606-3031-892f-a62c675e8dbc | -10.98266 | -45.08016 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 96d01087-3828-3818-b08f-daf0f7d27f7a | -10.9848 | -45.09253 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cff70303-27aa-3abe-ad83-716c1d5ad2c2 | -10.54857 | -44.33689 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ba5d557-7096-34fc-9ca7-667e1a937c32 | -7.05231 | -45.06138 | 2026-05-01 03:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eff752e1-1e3e-3d0b-bcc8-eb93cb0478d8 | -10.97427 | -45.07871 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| b3bb704c-5b81-385e-9901-d9066537a0d6 | -13.36658 | -39.90781 | 2026-05-01 03:57:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 19cb6e4f-bf4a-3928-9f2f-d80edcd02e46 | -10.98061 | -45.0918 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8ca5d1a-a886-33a4-b05b-89acbb10b165 | -10.97432 | -45.10292 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| d706bc76-e9a3-339c-9b2d-52fff898d18b | -10.97572 | -45.09501 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 6c87462f-b9c5-327a-92f7-cf7dbaacb3ff | -10.55259 | -44.33763 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2155d024-ee22-3325-9404-aec2b366d084 | -12.41122 | -43.79252 | 2026-05-01 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 902b0b67-d074-36ac-af0b-0de2b449cd1b | -13.36327 | -39.90726 | 2026-05-01 03:57:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 498be3c8-d9e3-395d-97c6-73a304dbeab6 | -10.97778 | -45.08331 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 4a368693-6be0-3b78-b2af-82a36864879d | -12.40745 | -43.79178 | 2026-05-01 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1ebe59e-1784-3fbf-b61d-3fe91d8c2572 | -12.28271 | -44.62682 | 2026-05-01 03:57:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 437b8bff-9fb2-3dc2-8875-5de45105a1ec | -10.968 | -45.08972 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5bcf6216-8af9-3df6-bc5a-6b7c4d980588 | -10.9729 | -45.08651 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| f5d4223a-579c-364e-a50d-c02c752f6f31 | -10.98549 | -45.08862 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ba22e7b-d7c3-327c-b0f5-0d99e98ce1e6 | -9.67392 | -43.78732 | 2026-05-01 03:57:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 191b1de5-2a5f-3a20-abf1-07d7053de7b5 | -13.27038 | -40.32 | 2026-05-01 03:57:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 55fcc8ef-2640-3fe2-a5c6-b34a76c9b9fb | -8.23229 | -43.8843 | 2026-05-01 03:57:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f8e7563-f2b8-354f-b8e2-3e91cdcd467d | -10.99037 | -45.08547 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| dd93f483-5cbd-37a6-b5f7-940a582c4d4f | -11.95271 | -43.38454 | 2026-05-01 03:57:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1b721d0-0225-30df-83e1-16e6f39504cd | -7.88031 | -42.66972 | 2026-05-01 03:57:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a3c9d333-e09f-32a4-ae8d-6663af3e9753 | -10.74627 | -44.3083 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdacd655-8f5d-349f-af2e-2b1453d7d892 | -10.99105 | -45.0816 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b2c8b2c9-24fd-30c7-9087-4e67c1a6dfdf | -10.9813 | -45.0879 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2af9ef93-45ff-34ed-8c73-192b67a3c571 | -10.55722 | -44.33482 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f199e54b-5221-3364-bde3-14a15e72c141 | -12.37227 | -50.0331 | 2026-05-01 03:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa4b97c1-4a44-36bf-a9f6-84c4f8b49c30 | -8.33276 | -45.36383 | 2026-05-01 03:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d30f7117-45a4-396c-b771-d4b7c60e9d44 | -10.97359 | -45.08261 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 245c32f2-dc70-3b1b-ad2b-bedf43ba045d | -8.22887 | -43.87995 | 2026-05-01 03:57:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a130df83-faea-3fea-81f1-1f443c1749e0 | -10.97847 | -45.07943 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 5ac1a682-ea27-313e-89b6-daa4edfde402 | -10.97221 | -45.09041 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 6918e0ea-6d3e-36a0-acab-cdca3de25410 | -10.97082 | -45.09824 | 2026-05-01 03:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 96952efc-beb9-33b8-b27b-1e4d77525fa9 | -10.54506 | -37.20486 | 2026-05-01 03:57:00 | NOAA-20 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e4de5c20-2f03-354b-8439-e6be12d2b2af | -10.5566 | -44.33838 | 2026-05-01 03:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90d8de39-54d7-300b-bb87-c2a7c7536a49 | -9.56779 | -44.57302 | 2026-05-01 03:57:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8eef5194-5e02-3d4b-82d8-42de44e2a7f2 | -15.42205 | -43.05278 | 2026-05-01 04:00:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b893a2c8-9ec6-3e52-ad71-0b4fb2baf5fe | -17.25237 | -47.08244 | 2026-05-01 04:00:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afdf4aac-d6b4-33b6-b364-64771772afbe | -14.45953 | -46.9851 | 2026-05-01 04:00:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce9a5276-993c-3547-baae-7f7328df0d75 | -18.00822 | -48.17859 | 2026-05-01 04:00:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18ec7036-535c-39f4-8026-289f279613d7 | -18.89145 | -39.92265 | 2026-05-01 04:00:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d001c91f-d785-3998-bbe3-eb6ed3fd8964 | -20.31286 | -41.22435 | 2026-05-01 04:00:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 627e0c2a-f254-3452-b3a8-0ad5f9435216 | -18.89482 | -39.92321 | 2026-05-01 04:00:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 800551af-3a38-3dc7-9d40-96d49def9b68 | -19.43413 | -46.89394 | 2026-05-01 04:00:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README4.md)
