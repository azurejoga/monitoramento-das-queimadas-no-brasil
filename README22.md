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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f0adc9a-9801-3ead-99c8-13a8bd0fce98 | -8.52471 | -54.76981 | 2026-07-01 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b66679a-a1a2-35ba-b77e-a65f47e3a15c | -8.35557 | -46.81118 | 2026-07-01 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ce4e0a8-ff50-35d8-bf66-938bfa4e3283 | -7.00164 | -42.77102 | 2026-07-01 04:55:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8cc980ed-69a9-3cb5-b614-7d6cbea4cdb7 | -9.02823 | -59.53974 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 978622fb-e320-305e-9e22-c0986409f71b | -10.43798 | -49.5804 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f6efd73-64cf-390a-9f0e-6dbdabac39c9 | -9.11231 | -58.26503 | 2026-07-01 04:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa625b45-f387-3a77-bad4-b895326c651c | -5.81183 | -43.80022 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bef25dfe-8bf1-30ac-ae83-e589d9e7325f | -5.35121 | -45.18664 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9aab7478-50bb-3658-bd7e-85da3af28845 | -9.8912 | -50.39632 | 2026-07-01 04:55:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f5cf6b1a-1c82-378d-bb2d-5e7d7b7946e8 | -5.79655 | -45.0524 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59f095b2-5594-3049-a920-1e1f8b10e620 | -7.75404 | -44.19312 | 2026-07-01 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff185476-a42d-3474-bdc3-1e0fa873b744 | -9.69919 | -56.09954 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fec021-1f2d-37ad-a08c-b141ec16a9e1 | -11.54938 | -47.45484 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8dd3b2bc-8b40-307e-a0b8-749779859e39 | -5.86221 | -46.25677 | 2026-07-01 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 766f6241-3802-33e7-88e8-122b3d61529e | -3.98123 | -48.42865 | 2026-07-01 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ab374b5-b36f-3f95-913e-008304c38567 | -8.60132 | -48.00802 | 2026-07-01 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d845a47-95cb-3a9b-9a90-52765ba32ca5 | -9.17453 | -58.06989 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e5adfcf-f111-3f26-a1c7-99d304cb3a19 | -8.13354 | -47.88135 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b5a04e3-decf-3545-b3a6-55943eb3a81f | -9.2796 | -48.76424 | 2026-07-01 04:55:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7794f77-7545-3ebb-b7a4-c0ef5a1edbfb | -9.11291 | -58.26155 | 2026-07-01 04:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97bd5a30-2c17-36b6-80ad-e4e1c579d848 | -8.98985 | -45.71663 | 2026-07-01 04:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2535e76c-529f-3b12-a74d-fa433cfecbaa | -9.97979 | -48.23991 | 2026-07-01 04:55:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9b467ef-1d2b-36e1-bcf2-9219ead391ac | -5.79501 | -45.06298 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e5be856-b0e8-3a9b-a11e-0c8e1c833246 | -10.13257 | -52.10205 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec681a6-99d8-3f27-8263-50f9e4a2114b | -8.63609 | -47.52969 | 2026-07-01 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3730d490-3b61-3aba-91e8-9f8ba6b55013 | -8.50757 | -50.15411 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d1c04a3-638e-3e95-bbcc-630fca6bf41d | -9.17846 | -58.07058 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41bd6b69-fab4-3eab-9032-271757da2862 | -6.42438 | -55.79838 | 2026-07-01 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae19562e-2c70-3119-9be2-2ace93325190 | -5.55696 | -48.70584 | 2026-07-01 04:55:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 268b387b-89bc-3035-9f1f-fabda0dea264 | -6.84141 | -47.94007 | 2026-07-01 04:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feafafe3-3020-3c56-8dfc-250210476705 | -7.47679 | -44.74961 | 2026-07-01 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 993ffccf-6881-3749-af49-c63260f421a0 | -10.92211 | -43.05697 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ece8252c-fe76-3610-8795-f68f371b0eb0 | -9.02029 | -59.53404 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a77fe9f-8a3e-37de-a424-8971b4a32e8c | -9.01595 | -59.53326 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d688c62b-4494-391f-9f41-ab91e9ff581a | -9.69634 | -56.09496 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28af256a-a486-30bc-a7dc-6610f43d8529 | -3.91903 | -47.81691 | 2026-07-01 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b419a28-aa55-3bea-a442-969b78eedd2c | -8.69315 | -50.69704 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4ceb2cb-9b04-3c01-bf4a-af11492fffb1 | -10.92264 | -43.04306 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 26f5a72a-3af9-3747-900d-29c2a8dbb92e | -10.92648 | -43.06082 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| a8994ad5-e1c7-33d8-a288-a9a85ef1c77c | -5.28309 | -56.01747 | 2026-07-01 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3509d7fd-a900-33e0-8ea8-6e61b1671ba6 | -10.91573 | -43.05082 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.8 |
| ff76f8d2-2624-3605-971f-f05e03b1cbb7 | -6.91628 | -42.84605 | 2026-07-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 11bc153d-1ea6-3b56-ad00-e7e0b4ae2506 | -9.08709 | -59.49352 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86578308-cfcd-3117-8309-c78904ef35c4 | -5.80133 | -45.05308 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd97b4c0-8e70-3fd2-8eb1-a1654b9b56d0 | -9.02463 | -59.53479 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50a3c3b1-c63e-3848-b5f0-e1830780218f | -7.74923 | -44.18942 | 2026-07-01 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af413dfb-5611-37b7-aa47-db27b1795e6e | -5.80056 | -45.05836 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46520a3d-6fa8-3398-914b-847797419304 | -8.98507 | -45.71595 | 2026-07-01 04:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c1dbc4d-9a66-3081-9817-bdff3a3f5b19 | -8.13302 | -47.885 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be24bdae-db41-3451-86c2-015dbaeb2a92 | -4.58069 | -48.02462 | 2026-07-01 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34d33fe0-91f7-327c-b294-a4bbd5224637 | -10.92963 | -43.04492 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6b7185c-3f97-3750-b9fa-6527c8956ec5 | -4.57997 | -48.02935 | 2026-07-01 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0a95bbd-4a17-3744-927d-8a95e1a25f2d | -6.83449 | -49.27625 | 2026-07-01 04:55:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a427e7db-f2a5-3bc9-af0b-975bc4eb8488 | -10.80932 | -49.34108 | 2026-07-01 04:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f75c67b9-1ea2-3e64-90be-5d7dbcb1b622 | -9.60569 | -56.92272 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b4bb0e1-59be-365e-bc35-3b847e5c6c16 | -11.91931 | -43.3895 | 2026-07-01 04:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fecd61e8-b3e8-3569-91c9-67b0fede4bd9 | -10.44177 | -49.58094 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a9c8efe-dd4c-36cd-9480-79b36df52b5e | -9.18891 | -58.05679 | 2026-07-01 04:55:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0189e835-8af5-3dda-a56f-8d78ee4d9644 | -10.92956 | -43.03525 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb383496-fad4-32e7-935a-fbd15fb9efbe | -9.69568 | -56.09895 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8780bc2-df1c-3b36-a197-ceaa0d670cf8 | -7.71322 | -45.93522 | 2026-07-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f74ba6b3-fb52-3416-b7a4-b466f3153385 | -9.60789 | -56.93206 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 20da131f-beb1-3cdd-be6c-58b397d2b6c6 | -9.08598 | -59.48992 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca5eca2-6fbb-3f27-8230-288178a4c54e | -6.95865 | -44.54961 | 2026-07-01 04:55:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ac350da-17c4-3794-824e-05a47fc96d43 | -7.83356 | -55.38826 | 2026-07-01 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72745530-5b9a-35c8-a493-6f91c92ab54a | -8.80668 | -47.48172 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ee56ab1-e3c8-31c5-b817-788352f5b8f8 | -5.79478 | -45.03107 | 2026-07-01 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 975f012b-07d9-3dab-b01a-3aa7a3a49219 | -11.54498 | -47.45414 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3cfa7266-99f8-3da4-87cb-93883622584c | -8.59593 | -50.97639 | 2026-07-01 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c382f4d-7e90-3b38-a08a-77a4d932a823 | -6.90588 | -48.04386 | 2026-07-01 04:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9b51331-9ff6-3f26-9653-fc6529ef65a6 | -7.28786 | -46.25055 | 2026-07-01 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e39e7daf-9474-3924-a635-5cf80d79b3a1 | -8.72594 | -47.83419 | 2026-07-01 04:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90545fd9-ce23-3aa9-b356-aaf2c83454e3 | -8.50646 | -50.42423 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5988b754-14cf-3fb6-a1a9-70e5e833bff9 | -11.49562 | -47.42387 | 2026-07-01 04:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4693b250-ab2f-338a-83ba-b2771e06dfb9 | -10.1292 | -52.10152 | 2026-07-01 04:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c56b17f-2afa-31e9-9f9c-d8cb7f0bea98 | -9.20928 | -45.33179 | 2026-07-01 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9d0cc76-ec7b-3506-b6b5-18561fa39d0b | -8.12539 | -47.88008 | 2026-07-01 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54aa7988-e18a-3fa3-95d9-255dffb37c52 | -10.92315 | -43.03883 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 066045f8-7629-324d-8db5-773b08b51cfd | -10.7641 | -48.35402 | 2026-07-01 04:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c7a9a0f-17c0-3490-8be2-d149443110ca | -9.08526 | -59.49409 | 2026-07-01 04:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec371625-b763-39c7-ba85-e50de8bf44b8 | -8.34499 | -46.82242 | 2026-07-01 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5408f398-a4cf-3a6d-bd03-566da1975568 | -10.37922 | -49.58587 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2317dcaf-bf55-3d1b-9d37-c8abd13bdf31 | -8.50293 | -50.42369 | 2026-07-01 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff279105-5627-3b81-a9ea-365acc0a0069 | -9.74821 | -49.03959 | 2026-07-01 04:55:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96298f38-9c71-3de3-ac45-98558c43fd1b | -6.91248 | -42.84928 | 2026-07-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1bb3eb93-dbeb-3981-ad60-1af76eb9907d | -10.97346 | -49.67141 | 2026-07-01 04:55:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d334a76-9df9-3555-93e2-8714e2d127e9 | -5.80604 | -43.79874 | 2026-07-01 04:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0af6235-7c77-3037-a32c-ea9d6f38524a | -10.9232 | -43.04846 | 2026-07-01 04:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 737f4886-14a6-3a26-b9bd-d237e98e5fe5 | -4.94569 | -48.24327 | 2026-07-01 04:55:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89b64b14-d750-33a4-827d-f1f5f2ae2acb | -11.54058 | -47.45348 | 2026-07-01 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4d462fa8-d1cd-3983-9926-802dd0e60f12 | -9.59691 | -56.93016 | 2026-07-01 04:55:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09023eaf-fafd-377d-8707-afa9d3a26452 | -8.60026 | -48.01529 | 2026-07-01 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a633efa2-21b9-370f-9003-0ebe83c8b363 | -7.7086 | -45.93452 | 2026-07-01 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 67ab2d1d-a2ea-3fe2-8b82-9be8a413005d | -10.38678 | -49.58701 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71ceb143-fcdc-3e75-aae0-7b738523b783 | -9.69216 | -56.09836 | 2026-07-01 04:55:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 154be52f-bccf-3a61-9a46-e0208de8ba35 | -8.58901 | -50.97535 | 2026-07-01 04:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e21c410c-17a5-3c41-831f-711585cce42d | -8.34996 | -46.81899 | 2026-07-01 04:55:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70401f5a-7f78-3ca6-aa32-20a6460f8cfd | -8.59724 | -48.0075 | 2026-07-01 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| e45ddb65-cfb0-3f70-b89b-8b7ffd8cc1da | -6.91301 | -42.84559 | 2026-07-01 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 77034997-d713-3111-a21c-38dc07c87211 | -10.43662 | -49.58971 | 2026-07-01 04:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README23.md)
