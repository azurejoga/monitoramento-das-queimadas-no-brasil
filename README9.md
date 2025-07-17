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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f3cc5cb-affa-3e54-8d58-60b3fe54abe6 | -5.6754 | -43.7147 | 2025-07-17 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 242.4 |
| daed393c-18a7-342c-a863-e2aac113931c | -3.3958 | -47.4785 | 2025-07-17 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 80e0cfe5-a7c8-358d-802b-b294af0e2ed4 | -5.6567 | -43.7161 | 2025-07-17 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 310.8 |
| 4f22c542-fa04-3b3d-8f2d-8a00d5197aaa | -9.2449 | -48.5546 | 2025-07-17 03:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 8868c91f-670a-373c-861e-1aac22980898 | -5.6752 | -43.7379 | 2025-07-17 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 91690d72-1836-38d4-b069-cfe9f21c272a | -5.6565 | -43.7393 | 2025-07-17 03:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 44bbfb58-c34a-3271-8cea-471b3d9fee44 | -3.80958 | -38.6837 | 2025-07-17 03:30:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7560dc6c-ed0e-35bb-b1d5-0f6a415ebfdd | -4.97673 | -37.16106 | 2025-07-17 03:30:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| df0dfa51-e4b7-3073-981f-5a3c320a100b | -4.97687 | -37.16391 | 2025-07-17 03:30:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 038b2c83-ceb9-3ec4-babf-764812aba04d | -4.97612 | -37.16485 | 2025-07-17 03:30:00 | NPP-375D | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 585cfe96-0dbc-3af7-a72e-e77a2dbb10ec | -4.91234 | -37.34379 | 2025-07-17 03:30:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bbed7025-e0f8-3bb6-98fd-929a7c874723 | -3.80285 | -43.22346 | 2025-07-17 03:30:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45e1b255-6fc3-3834-beab-bf3db10cd0d6 | -5.015 | -38.53312 | 2025-07-17 03:30:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2484cbae-288d-33a4-8d2f-dbaa53a89f92 | -4.58815 | -37.80933 | 2025-07-17 03:30:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dfeafcbb-5f8d-3cc8-a40f-40ccdfe95ac9 | -4.44862 | -38.44782 | 2025-07-17 03:30:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 842b4bdd-7c85-309e-8a26-cf19eff8b5fc | -5.01579 | -38.52847 | 2025-07-17 03:30:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 00b72bf2-9dc6-385d-a922-e7e9e34c5ea7 | -6.71601 | -44.32935 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9526c4ab-202e-3528-a662-f4fe3ab4799f | -7.15684 | -46.09554 | 2025-07-17 03:32:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5fb0a1d8-ec39-307c-9d29-adec29c24d91 | -9.35364 | -38.30144 | 2025-07-17 03:32:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e4f97342-a078-3148-b7c0-060b1c4c6a8c | -5.79682 | -45.08926 | 2025-07-17 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65eead74-c5a4-36ee-970f-30db74cf14e6 | -7.23702 | -43.5015 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a18d0e66-d905-3cf7-8eab-e833bfe1619d | -11.66389 | -43.76952 | 2025-07-17 03:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8ba4033-9f32-3f5d-bea9-c33e6846a0dd | -4.8025 | -43.23103 | 2025-07-17 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98a86faa-84ba-31df-b3eb-5c08d81b5e36 | -6.72674 | -44.33764 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 20852a4d-91ed-3a79-b293-bb713e1ee90d | -6.97954 | -42.80806 | 2025-07-17 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b3cd96b6-6107-3905-99e0-2340eab2fd07 | -5.66072 | -43.71384 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| d20d7b48-70cd-3a53-a8a9-c2d343c0a004 | -6.84891 | -44.76592 | 2025-07-17 03:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3868286f-ba06-39af-a760-92d26df6aa7f | -9.58288 | -40.34943 | 2025-07-17 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fcf2e41c-fadf-30a2-896b-dc8ef6990ac0 | -6.45805 | -45.34363 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| ee2f942c-6183-3442-9457-1aa15b1f247c | -6.57104 | -36.5587 | 2025-07-17 03:32:00 | NPP-375D | CARNAÚBA DOS DANTAS | RIO GRANDE DO NORTE | Brasil | 2402402 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 468957c9-d12d-3f58-b46e-95d4dcd6100a | -5.78998 | -45.08776 | 2025-07-17 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3bc5ca10-dca3-320e-81bd-a1022e66e5b5 | -7.18868 | -43.11737 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1a9ce67d-3e23-3364-aebb-cbb772ecd9dc | -6.87326 | -41.73011 | 2025-07-17 03:32:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5845f1bd-fea4-30ef-81f6-4eef802487c5 | -6.72149 | -44.33611 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a4a7c718-a0b8-3c83-9d58-35c325792afe | -6.45681 | -45.3502 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e1243293-7119-3b51-a7c0-d2c210e54e67 | -6.7225 | -44.33062 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| aa43d2e2-6c85-358a-b5d2-15745ffd8043 | -5.52937 | -43.89156 | 2025-07-17 03:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 136c83eb-2abd-335f-a69a-23284f27427f | -11.66964 | -43.77083 | 2025-07-17 03:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06022175-4997-3512-8bd1-eb82723049bc | -4.8043 | -43.22104 | 2025-07-17 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3df5bbaf-a22f-3da3-8f2b-587379391078 | -5.65635 | -43.71204 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5dcbfad5-f7bb-3df6-93ba-9c9c5fe8d3c0 | -9.58767 | -40.35031 | 2025-07-17 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8a1e2af-96e8-3811-a9a8-30e5a8c1f602 | -5.66905 | -43.71444 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 2fd2f935-cb2b-3a22-a0f8-2802217be561 | -7.18702 | -43.11788 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1570ec89-c92f-3b67-b300-41b9d14f9f3c | -6.46589 | -45.34488 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 634ca653-e861-3a96-bcd3-dc612ed1e55c | -5.65443 | -43.72239 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| bc919544-ff19-39c3-bf70-a4b0ebca2d63 | -5.53037 | -43.88615 | 2025-07-17 03:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1d8c0b82-3b7e-3a53-9cd9-6a55e0e34485 | -11.66979 | -43.76943 | 2025-07-17 03:32:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f78019ce-261e-3999-8e9a-d1c00b2e3e04 | -7.18622 | -43.12239 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 72b1e156-1a14-3f1a-a9e1-e9b750ba2b90 | -4.8034 | -43.22603 | 2025-07-17 03:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c10d1949-c4e3-3553-bdf0-b5ca44365c6a | -4.5932 | -43.31697 | 2025-07-17 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10114155-9cf3-3df8-b0bd-57e49a780a01 | -9.3146 | -44.84607 | 2025-07-17 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67db74a7-e118-361c-b6ec-6e92ad260438 | -6.67514 | -43.03411 | 2025-07-17 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bac29ea-bbb6-39c9-b339-7bfa99bffcfb | -8.88349 | -44.79301 | 2025-07-17 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3071890-e8e3-3adc-b30e-afaf8b9d30fe | -6.72127 | -44.33099 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0d48de84-61fc-32a7-85e7-0063105e85c4 | -7.21149 | -45.33354 | 2025-07-17 03:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95fc7715-7be6-301f-ac1a-db80e289be80 | -6.81772 | -43.78605 | 2025-07-17 03:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02fd8081-ee49-3744-a758-496c26690d1f | -6.71029 | -44.31808 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8d231aca-cbd4-3397-9f79-58194f7cdc36 | -6.87373 | -41.72613 | 2025-07-17 03:32:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f93dd772-10fa-31cb-bf60-5ef3c4ad9bf0 | -7.19466 | -43.11853 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7473b311-8885-37f5-93db-0eec5a10dd29 | -8.10163 | -43.14852 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 0af57d90-1534-3e8b-95bf-7b7934ddb6f3 | -5.66084 | -43.72332 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 90fc0111-3a89-3470-8dba-b40f87d7e66d | -6.71143 | -44.31768 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 333f7a0b-0981-3877-8342-cb26709fc6b6 | -6.71579 | -44.32449 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 744af2a4-7efc-39a1-874b-efe3419ca4fa | -6.97366 | -42.80692 | 2025-07-17 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4d4fc6b1-6c62-3ca2-9a8f-64d7e74b328c | -10.96478 | -46.4843 | 2025-07-17 03:32:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82175a36-65fc-3a9a-9f8a-49faac0bd0fd | -5.6662 | -43.71996 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 52083e7a-47ec-3ad1-879a-bae21efc861a | -9.49074 | -40.3925 | 2025-07-17 03:32:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d7276f5-0515-3c1f-8759-f594f3b4aa8b | -5.53061 | -43.88589 | 2025-07-17 03:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f1762c58-c41c-3f8b-b680-28ff74801d0b | -4.59229 | -43.32207 | 2025-07-17 03:32:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5a1a79-2400-3adb-bec4-fe3bb8ea9469 | -7.34653 | -44.20032 | 2025-07-17 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fbf7546-3259-3280-9295-40fe44966725 | -5.65889 | -43.72415 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 82259b52-b3ff-3da5-9e65-1303795682d0 | -7.35292 | -44.20148 | 2025-07-17 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 08e6e036-3bab-3602-b6fa-940ef09bca0d | -7.2309 | -43.50037 | 2025-07-17 03:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2a484f73-40d9-3b4d-a439-ab3d57aedef2 | -5.65343 | -43.71787 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f66d7d8b-2516-3a08-9b1b-690ceb42ebf6 | -5.79562 | -45.09584 | 2025-07-17 03:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7544a458-5ea5-316b-b1b3-ecdb4a7af924 | -8.11173 | -43.14649 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 37513368-a4a2-39a6-bbec-13af35398e6b | -6.82159 | -43.78559 | 2025-07-17 03:32:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39c10105-7bed-3b05-ae7c-81c1d20a590e | -8.10753 | -43.14965 | 2025-07-17 03:32:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c47950bf-2e36-38d5-9252-1e9cbc44eb50 | -9.34947 | -38.30059 | 2025-07-17 03:32:00 | NPP-375D | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 354967b5-574e-3605-99bd-4a5d91faa9ac | -6.7105 | -44.32276 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e39ddf2e-be6e-34bd-ad12-e1c2270c2c7d | -5.93373 | -43.36697 | 2025-07-17 03:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c8664240-8204-3853-b61c-d35b5e08450d | -11.40018 | -42.29497 | 2025-07-17 03:32:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 99ae2ce7-54c0-33ed-9551-5940a6db95f1 | -10.10209 | -40.9208 | 2025-07-17 03:32:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5308d8f4-67db-3fe3-ba28-904218edd20b | -7.34556 | -44.20551 | 2025-07-17 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 041bfe76-b555-3557-94a7-17516903c37b | -6.71479 | -44.32974 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 423b2b89-5ae4-38a8-af47-335bc45d0fab | -9.31354 | -44.85141 | 2025-07-17 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8da68365-9271-3b46-8d47-2a28873ac413 | -7.18782 | -43.11343 | 2025-07-17 03:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 265bb261-45c3-37c6-b805-3be52bc35c6d | -6.67432 | -43.0386 | 2025-07-17 03:32:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b939b9b-f326-3892-ade5-6ed03f8ca7ec | -7.20472 | -45.33191 | 2025-07-17 03:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94a37ffa-79ad-3185-a25e-78306d5eb29e | -6.97877 | -42.81231 | 2025-07-17 03:32:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| afbfa060-1b17-3a57-bbc7-3de866ee9d8a | -9.38553 | -40.62238 | 2025-07-17 03:32:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca6b2bfc-a8f3-36ad-a7f7-0078dbeee78e | -7.33917 | -44.20438 | 2025-07-17 03:32:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ea88dda-f820-35e2-aea4-5d1982db567d | -9.31316 | -44.84977 | 2025-07-17 03:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c4b1bb3-35b6-3527-9cba-187aa357a4c8 | -6.56923 | -43.47821 | 2025-07-17 03:32:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9f4c795-2fb1-31d2-a9cd-ec53a74d9888 | -6.46352 | -45.35257 | 2025-07-17 03:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38ad2c19-ffde-3dc7-b868-0ddc70f9087a | -6.72877 | -44.3269 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b86fc5e7-77a5-3505-8e8e-066f7b47108f | -5.6554 | -43.71714 | 2025-07-17 03:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 039af1b0-96e6-33a8-8249-a1be93a06adb | -6.70952 | -44.32814 | 2025-07-17 03:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dac0f222-a7e1-3ddc-8f00-3e73b910ac27 | -11.39825 | -42.29464 | 2025-07-17 03:32:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d311669-3412-36b8-9451-a08109298a9e | -8.88246 | -44.79773 | 2025-07-17 03:32:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README10.md)
