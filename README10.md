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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef2ac43c-2e98-325f-92de-e0e28d6530f6 | -10.805 | -44.2319 | 2025-06-30 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 241.4 |
| 472ab188-4e9f-3191-9f17-0578551dfa0a | -10.7859 | -44.2346 | 2025-06-30 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 1c1b9021-23a5-3d07-acf2-38f8509414ae | -10.805 | -44.2319 | 2025-06-30 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| bc9a054a-72be-314a-8b0b-4078b9eba642 | -10.8046 | -44.2553 | 2025-06-30 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| c73f9fa4-d3fd-3548-a6d0-694667c2600f | -12.6319 | -54.2087 | 2025-06-30 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| c7135f10-8a43-3def-9d0b-a72fda3b381b | -10.7855 | -44.2579 | 2025-06-30 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| a35405c5-eed9-36c9-8f61-0a063d5371ba | -10.8046 | -44.2553 | 2025-06-30 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| dcacad93-5606-3b6f-b5dd-9e27b8daf907 | -10.805 | -44.2319 | 2025-06-30 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 207.8 |
| 9b41ef6b-b51f-35a6-9437-8ca5da2b3443 | -10.7855 | -44.2579 | 2025-06-30 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0cb55ecc-3aa4-39e9-8390-a193764ae954 | -10.7859 | -44.2346 | 2025-06-30 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 0d3d4ef4-c8bb-3d6b-ae55-a6ae3f628555 | -10.8046 | -44.2553 | 2025-06-30 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 8adeb773-9220-3637-bd4c-1f14310e3c7a | -10.805 | -44.2319 | 2025-06-30 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 210.5 |
| bffdd0a8-f4de-32bc-82ab-fdd33988a8f3 | -10.7859 | -44.2346 | 2025-06-30 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| dcdf8193-ea0f-3e07-851d-0695f950720b | -10.8046 | -44.2553 | 2025-06-30 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 07b589b7-e4db-3ba7-94b9-50d376de776e | -10.805 | -44.2319 | 2025-06-30 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 96b6863d-cbc3-385d-a61e-b60293468af1 | 2.7507 | -60.36786 | 2025-06-30 05:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 40923352-47e2-307b-8103-955f648e94d7 | -4.10709 | -47.93858 | 2025-06-30 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c39a1dc-e9fa-3087-ba5b-63507d2ebbbf | -4.3167 | -48.07687 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6e9db56-e944-3a0b-89a8-636fbf065b29 | -4.31879 | -48.07378 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c3f4e2a5-c887-3e1e-9d88-414a390ac73d | -4.81448 | -47.31955 | 2025-06-30 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be00bf00-8a12-3a96-9e73-a91d854863c8 | -3.62582 | -47.54314 | 2025-06-30 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4401a417-e126-364d-b523-41e3e3a62320 | -4.32278 | -48.07964 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abf1566c-ef71-3347-91cf-a76e50d04905 | -7.25395 | -43.17502 | 2025-06-30 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 104efd40-e729-374c-91d0-9a2dfb110f9a | -3.62661 | -47.54776 | 2025-06-30 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2f7cfcf-7a5a-37ef-9e77-fb1ac523d7ce | -7.86282 | -47.12866 | 2025-06-30 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10a900e0-b9d8-30b7-90fa-bd73c7941c15 | -7.29832 | -55.3159 | 2025-06-30 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71d28ec6-24ba-3a7e-81cc-a7f8eb26078d | -9.09674 | -47.9614 | 2025-06-30 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cd7cc1b-8a84-31c2-8605-e7a8e28de9cd | -8.86288 | -47.95193 | 2025-06-30 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bd5f531-daa3-30ac-a3d6-50a83d762ef8 | -4.32066 | -48.08266 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b748c530-162e-3a6d-9033-3df1b1acfc91 | -8.65434 | -47.80698 | 2025-06-30 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7db670e9-db9d-387d-b8e3-14d2169c03dc | -4.47821 | -48.3115 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9cde5e9-ae1d-35b7-aef9-743e5e734340 | -9.44196 | -47.93879 | 2025-06-30 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfb42c5d-f622-3c03-9706-b1bf8b5c9d97 | -8.12229 | -55.08921 | 2025-06-30 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b8db52a-e9ea-32df-a42e-45a66227a20d | -7.26231 | -43.16407 | 2025-06-30 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 01a140d4-11a5-32df-9a15-5df4df437663 | -7.38452 | -43.88193 | 2025-06-30 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4636dae8-3b4f-383d-813a-6743bf13b361 | -9.14642 | -46.36567 | 2025-06-30 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e7b9627-4aff-326d-8552-c9b7863ce2db | -4.10792 | -47.93965 | 2025-06-30 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1452750-e3c7-392c-b238-953c2e6da36c | -8.0129 | -47.40424 | 2025-06-30 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ebcc52c-28bc-355b-b23a-a565259f91a5 | -4.31804 | -48.07905 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3af71d95-ccdf-34ee-bf15-7930b7d6eaf4 | -3.328 | -52.55775 | 2025-06-30 05:04:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e7dc738-33ac-3cf2-a1ad-fe22ae26fe44 | -3.62505 | -47.54858 | 2025-06-30 05:04:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76edc157-989e-3245-8098-ff2a1ba6b8c0 | -9.14072 | -46.36497 | 2025-06-30 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53c0cf45-a756-3680-8754-7d2273329bea | -9.4368 | -47.93815 | 2025-06-30 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f74a4bd-0a91-331c-9b10-57db9917786b | -7.39169 | -43.87773 | 2025-06-30 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 358f3e66-7bde-35b2-a936-b0373c88fc6b | -8.65391 | -47.81006 | 2025-06-30 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df15db47-758b-312c-af77-1d01ec3122b0 | -8.54549 | -48.26591 | 2025-06-30 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b6e593a-ed9c-3250-9b1b-df485828c3be | -5.41857 | -47.57037 | 2025-06-30 05:04:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f726a93-6dfa-3d6a-991f-207b3d5bd2e6 | -7.25642 | -43.17157 | 2025-06-30 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1cc486a7-512a-3f80-a1fd-eefb3a15121e | -4.32144 | -48.07748 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d10a7f1-69c4-3533-bf7e-0e5b975ce7a9 | -2.58772 | -51.92445 | 2025-06-30 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4eb64a8-5cc5-3473-80e7-89ebd6f35730 | -9.44155 | -47.94195 | 2025-06-30 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b48ae48f-7ec4-3719-aefd-84238bb6778b | -4.4895 | -48.8692 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45a20259-cf9d-3b86-99be-63332fbb6c0a | -8.54626 | -48.26024 | 2025-06-30 05:04:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6b99e90-2fbd-32b8-8d74-1b6c7967a3d6 | -4.32353 | -48.07433 | 2025-06-30 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6847b2f5-5746-3a4f-876f-047bd0268fd6 | -8.0125 | -47.40728 | 2025-06-30 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47e7f08f-cf40-3e3f-8971-6ac6ed874dd6 | -7.25566 | -43.17755 | 2025-06-30 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e3ca6d8e-25fb-36a3-ab1a-a2550fdcc54f | -4.81988 | -47.31768 | 2025-06-30 05:04:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfcbab1f-4668-3c2d-8d85-97c67ad8a781 | -8.71307 | -47.85719 | 2025-06-30 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7981f0c1-6a3f-3f30-ab3c-362998073dfc | -7.38519 | -43.87671 | 2025-06-30 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40b64aa4-5ace-3b63-9a1d-d4ce24b64c4c | -7.85756 | -47.12754 | 2025-06-30 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57fa3efd-2cf5-3e7c-8c53-aa1c61c7f9ff | -9.09122 | -47.96384 | 2025-06-30 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41f22fa9-e797-3ac9-96f9-da59bc8f69ed | -5.41171 | -49.08159 | 2025-06-30 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b67729c-6365-30b4-8485-f39f291d94b6 | -7.63004 | -44.6493 | 2025-06-30 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 44852572-afbf-3622-8b3d-9e2999b0a354 | -5.31839 | -50.57219 | 2025-06-30 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a3d6f85-9b27-338a-8aa4-9e00b64d0a4d | -7.26395 | -43.16658 | 2025-06-30 05:04:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9fc052a3-5d98-35ab-9811-375a2e903238 | -9.09716 | -47.95823 | 2025-06-30 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9b8e1f0-e9a6-395c-95ee-5e1c10863a3e | -9.09633 | -47.96453 | 2025-06-30 05:04:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 618b353d-901c-38ac-a7c5-489af716e15a | -9.35849 | -58.8535 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68678406-7c9f-3d1e-9f05-ffe90157b17d | -9.24323 | -58.74049 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5b5500bf-96b9-3b58-a742-71c611093761 | -12.09818 | -54.67039 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 182ecad0-e57f-3c4d-8882-275ba47facd9 | -9.24261 | -58.74428 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f085dc3-d4ae-3397-abba-0e2e54f274bb | -10.87582 | -53.77939 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d60d0847-2fe5-3c7a-9e72-16b69645ae8a | -9.11238 | -59.04872 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbcefbea-27e8-3fda-9ca5-fee318e688e6 | -9.25046 | -58.7612 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60686588-e947-367c-bc97-3d75ab542720 | -12.60967 | -57.87754 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1130d99e-e440-3615-9374-84ed15da916a | -10.87524 | -53.75792 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6b37531-b6bf-3f1b-ac2c-55577bb08b45 | -9.11759 | -61.48932 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 169973db-887a-3149-852b-0205d07eea16 | -10.54924 | -52.0398 | 2025-06-30 05:06:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1127ae15-747a-3bc0-a2a0-807b71fbb351 | -10.80397 | -44.24517 | 2025-06-30 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2e66d09f-1482-3bb7-bd9b-69c9759ca0bb | -9.23228 | -58.7426 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb65ba23-6a7b-3019-bfee-4c18583bba71 | -9.23667 | -58.75899 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cda09be-3ef4-3b85-88ed-42755cee5719 | -11.19313 | -55.9194 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01f35ec7-c6ee-3f88-b467-0a11b30e4fde | -10.21611 | -54.30359 | 2025-06-30 05:06:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb5f6c06-405c-3f36-9f57-7c58fe2b5e0e | -12.62517 | -54.21206 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 541d831b-17b6-38a7-bc6e-bb26cbf24cf2 | -9.9486 | -52.17513 | 2025-06-30 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9cfb3d1b-ad11-3de7-8c62-b5d22a7e7ba0 | -11.20648 | -55.92152 | 2025-06-30 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d5d6806-5b9a-3d67-9c69-7cbe33219570 | -11.1173 | -53.98787 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 759d9af0-9149-3282-a664-7525b8b0b055 | -10.86862 | -53.77833 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1bea683b-0df3-3c5f-98c2-65474375a535 | -10.85361 | -53.75475 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f99b390a-4fda-3c06-a187-05539d911e48 | -12.63198 | -54.22915 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3a3717d-fb09-3856-b2a2-9ac2c46ee2b4 | -12.62753 | -54.22096 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 071cb772-26c1-3285-8943-a77a508bfcf3 | -9.25514 | -58.75415 | 2025-06-30 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2eaff20e-06b4-3860-92ed-cd917521c398 | -9.91648 | -53.3526 | 2025-06-30 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f496c15-0ed2-30d0-b9ca-50caa259167a | -9.1727 | -61.40553 | 2025-06-30 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ed67dd3-d431-3430-ab8d-1be3d2a3527b | -14.02943 | -54.48941 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44254449-5870-3cc7-a3fc-3fcf464487a6 | -12.50072 | -58.34874 | 2025-06-30 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 702811de-482c-3efc-8892-d391a1ee000f | -10.8535 | -53.74372 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7b48c89-435c-361a-a562-99728aa5d1c2 | -12.62658 | -54.21553 | 2025-06-30 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e58241cc-ce84-3439-a571-1f5a6187b39a | -12.09527 | -54.6659 | 2025-06-30 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc981e94-98fb-349a-8ccd-28595c7b9eae | -10.8499 | -53.74316 | 2025-06-30 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README11.md)
