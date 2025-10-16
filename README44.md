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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d668194e-704e-396d-8f6f-1918f5b9c57a | -7.64745 | -44.08926 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| b7b3cd8c-fe67-37a0-9bc4-3566a3c7b2c9 | -4.97618 | -47.10314 | 2025-10-16 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 689fd620-5e9e-35e7-a0b2-016302cc9b57 | -5.3029 | -42.67405 | 2025-10-16 04:38:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 516d2ffc-ae2e-3f1c-bb19-b5a10cde6afc | -5.87712 | -43.85118 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f12d465-32e3-3f29-af8b-de20fe0d4f13 | -5.2538 | -41.01862 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e256f2c-1790-30d2-97bc-7c37f3a91a1b | -4.67576 | -44.10966 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38d0d430-61a1-3205-b9f2-532534779ad4 | -6.37729 | -41.47778 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4e3f7d2a-e4de-38c6-9bd9-5a6c64af11e1 | -6.23174 | -55.63239 | 2025-10-16 04:38:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79cb1042-6350-3f1a-927e-b9386759ea4c | -4.66324 | -44.11142 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce36648a-0c57-3123-b0bb-8b7cf5026aae | -6.53066 | -44.24863 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb7f5aad-7b56-3aee-8800-87f89c4dc8d0 | -2.26493 | -47.84537 | 2025-10-16 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fafcac3-e047-38b5-ab5e-9bf8c284390c | -7.39521 | -46.78757 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9664fd24-d47d-301c-9549-e13ebb5f9de4 | -3.22874 | -43.45498 | 2025-10-16 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16be7f5f-fa15-325f-9223-0e23bea6074f | -5.26946 | -45.17134 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 415f9bbb-c434-3d10-97f5-4a8dec12ff3d | -7.94695 | -44.14256 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ecf3509a-5116-390c-b3e0-008e27c8083c | -4.65737 | -44.09622 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87432296-fdee-3930-a714-49a5e15f6005 | -3.38726 | -50.28086 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fba12dff-4169-3585-ad00-35478def604a | -4.91873 | -41.55346 | 2025-10-16 04:38:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 863e4e7f-6f24-34ba-9cd2-d5245ee2a433 | -6.13806 | -41.75756 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d97369fd-4da4-3145-9f1f-40d2835444cb | -4.38785 | -43.38783 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6052e23b-db88-36c4-96dc-aac491697913 | -8.07364 | -45.4264 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2c3b898-e111-33bc-8c3c-10addd93dcd9 | -6.37082 | -41.48841 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 02c24982-be01-3432-817d-bf257dbed9ee | -7.79454 | -46.01827 | 2025-10-16 04:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 691442c9-38f3-3e04-83ec-d1af965993bc | -5.60009 | -44.25854 | 2025-10-16 04:38:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed9eb2ca-a411-33f6-9032-da4c56915b86 | -8.20342 | -43.97718 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf95e800-8921-346b-9716-9206cc5c6f32 | -2.388 | -47.70848 | 2025-10-16 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a642b9fe-44d6-3096-90c5-b8bbb05dd567 | -6.17897 | -44.29302 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c70da795-9051-3da3-ade5-389cb945b263 | -7.18775 | -42.3597 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 49c8817c-234d-3692-9aff-e6b783412b72 | -6.17228 | -43.43404 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87a30545-74fc-3dbf-9d9c-4babdf282c28 | -4.38256 | -43.39481 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 22118aab-a80b-3945-bba0-a0d39002388c | -6.07077 | -41.9178 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 70e27fca-06cc-3a30-b6f9-0316272fe486 | -3.27554 | -45.84031 | 2025-10-16 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95605f25-3680-3291-870e-a7ea1f7736c1 | -5.45736 | -41.02735 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 634f0499-0040-3fe9-8050-16575a4b207c | -4.36589 | -43.39219 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 14b77378-66ae-3683-aa63-bd287fed5118 | -5.4342 | -44.23299 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3450af58-862a-3ce9-b26c-074323eab8fc | -4.95878 | -45.09865 | 2025-10-16 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c78319be-b1ae-39a5-aa94-bcf61884a468 | -4.00128 | -48.3399 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd76dd73-87a7-374d-9d80-f671f0346bab | -5.45128 | -41.02966 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b2bdeddc-738b-3fd3-8d97-ffda68052c42 | -4.01909 | -48.96532 | 2025-10-16 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6e5aea8d-7da1-31ee-96ae-f461b15f5633 | -6.19996 | -42.60582 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9189b59-cf62-3605-aff2-e6cf60da64f0 | -7.05929 | -45.05869 | 2025-10-16 04:38:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8cafa1a3-a4d9-39c1-9e71-c1cf50892077 | -7.03986 | -43.49297 | 2025-10-16 04:38:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84cb978c-bc32-360d-a4ef-4c430e59a5ac | -5.39803 | -40.902 | 2025-10-16 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a8bd1b2-7bc6-348a-8ea7-31f7aeb38523 | -4.64597 | -43.13251 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 120c6c52-2ab0-3c9e-96dd-51baf2ba1618 | -4.4089 | -50.3162 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f29f7f65-8a03-31d5-ae4b-97ab09d13f9c | -7.4929 | -44.58631 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8dfc1a16-1a8f-3dad-98d6-312399550a7f | -8.25405 | -44.10566 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af8cf2bb-4a7e-3a57-88f3-1c3a5549ef1e | -7.62662 | -44.08585 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ad88ffe-88b9-3e20-87f9-5dd0ac327a40 | -4.67838 | -44.09249 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b717d09-8338-36d0-beaa-d6f51f60b5bd | -8.29282 | -43.43382 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 88cba1b5-711c-3792-bbe7-d9968fb36601 | -5.50729 | -47.30306 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eebaf938-4e41-36b3-9820-8b5104c0e47f | -6.63971 | -43.42407 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e7354c0-fd1a-30ce-a4d3-219bf45cfc87 | -5.45157 | -41.03236 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5f93ea12-b850-3469-82f8-51f0451afab0 | -7.20801 | -43.83351 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b38de2d3-59f2-39f3-b9c1-9aca0bb62bc2 | -3.1437 | -49.03432 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 837b6943-fca8-3216-9b27-d9e30b24b88c | -5.21777 | -46.19584 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ab0d77d-9a41-3578-8783-fc7fceb83cdc | -7.0765 | -41.97407 | 2025-10-16 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 68fe9287-fb51-3b83-8246-d5ac9beec4a3 | -7.50774 | -46.64085 | 2025-10-16 04:38:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fcd688c-0210-39ed-b9ed-4592113bb097 | -5.43369 | -44.23648 | 2025-10-16 04:38:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2d0558e-57fb-3960-829f-ff65c1fbff56 | -8.20766 | -43.97782 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f32ce61e-63e2-30a7-93f2-f4e069b1c61a | -4.65633 | -44.10313 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e88d5e6-38ee-3019-9f68-c017c9d048e9 | -7.17823 | -42.18992 | 2025-10-16 04:38:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0bbb52c7-77b8-36d0-9c85-eeb9d12fa70b | -6.55237 | -43.91998 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5d09807-e657-36ed-b485-3bc61780bfcd | -6.75328 | -44.37785 | 2025-10-16 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aed83001-0139-3798-b9a2-184da532b560 | -5.93767 | -43.80096 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93a0ad53-de0e-33fe-b665-db623327546d | -6.17848 | -44.29641 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b97533d-82ac-3e6e-b42f-22a53c187b0f | -5.85778 | -43.86784 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71e23f1e-fd71-32b6-84c0-4ea18d07aee7 | -5.6594 | -45.9566 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79651fc9-ff75-3a89-8856-b9bae2db50be | -8.24406 | -43.33522 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5daf95b8-b6a7-3d2d-b2a9-e374d83cbf15 | -6.26484 | -42.89754 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a28591c2-817b-399c-9ad4-741c1b291c2b | -7.94804 | -44.1348 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e3bf82a-d121-3283-9de8-f8556b437193 | -4.17716 | -49.97531 | 2025-10-16 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef720107-773d-322e-84e5-09975d110e39 | -5.8968 | -42.82748 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a4550403-c2f3-370c-8e5f-3e79fab16721 | -4.83201 | -45.65768 | 2025-10-16 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66bbd3ed-1c1e-3727-8f85-96be5de73d1c | -3.38333 | -50.28393 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca94acbf-5128-35c5-bf61-ac714a9778e7 | -6.37649 | -41.48358 | 2025-10-16 04:38:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 03d3c1c1-08b3-3686-8eea-1ec4843a894c | -1.62553 | -47.05289 | 2025-10-16 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df98b1fb-8beb-3903-86c5-6c984f249efa | -4.66377 | -44.1079 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2234925a-a34a-3617-9e90-c25a9793937d | -7.47732 | -42.76006 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 8f332bdf-278c-313b-a99d-b1a3c11513bc | -5.32278 | -44.8355 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f66191b6-c0ba-344d-8326-8b870dd81171 | -3.26448 | -50.04148 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dd6d377-2e38-32ed-8281-0452263ba157 | -2.63945 | -48.0592 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| bddb3b5b-27f7-33ee-b28c-81682a57bd17 | -5.47293 | -51.17871 | 2025-10-16 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a87f5ab4-0d92-348d-90ea-733cc99091db | -5.91596 | -44.72615 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db5beb10-b6c0-3ea8-8341-c4823a52a4b5 | -4.10243 | -48.01861 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 350d9b8a-1fac-3792-bcbe-39bb2184362a | -6.32259 | -45.52006 | 2025-10-16 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35ab40f7-7f5a-300a-b41c-7042d42f6a15 | -3.3537 | -54.72559 | 2025-10-16 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efa5427b-35ba-3159-9ad8-13248a50e31e | -3.66755 | -50.26943 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faaff288-3e84-39a8-a665-2b9b97a0fe29 | -5.8815 | -43.87863 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e87352ff-3a23-3016-824b-f0be7e7f270b | -3.29909 | -50.17099 | 2025-10-16 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12058370-c659-3b9c-ae07-6dd13785d2ff | -6.04091 | -41.92368 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5934196f-eef1-3817-b6f1-dab7bcc8f2c8 | -5.51411 | -47.30412 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 079529db-aaa3-3839-9b5b-b32e487aa39f | -5.42777 | -40.98076 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 41e4848d-74f0-398c-b54e-e92c1953a740 | -7.35842 | -41.91103 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e29a8a2-4f2c-3892-a58e-de85fac55fc8 | -4.41898 | -42.89001 | 2025-10-16 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2c5e00a-fcdd-3146-93f2-cccb7ce8bb1f | -5.43698 | -40.98771 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d6367fb8-ce40-3074-a956-463fe64c390c | -6.91334 | -44.07771 | 2025-10-16 04:38:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b4f3ae9-44b0-36eb-b963-d7e1574c443a | -5.4033 | -41.1504 | 2025-10-16 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b587aa7-8099-35db-9e64-be9028340f29 | -7.49242 | -47.32334 | 2025-10-16 04:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fffd4b3c-e91d-302b-aaef-dc15a650b806 | -8.06599 | -45.42483 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README45.md)
