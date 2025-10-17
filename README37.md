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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff3b1ab7-d50c-3c16-b9fb-94fc9491ae4c | -7.47307 | -42.13899 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8516bd09-542c-39df-9cec-94a14c8c84ca | -9.24892 | -44.37724 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 275ea41b-702f-3fb5-a763-7b855dfee491 | -6.402 | -46.87819 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4af897f0-2044-363c-b93c-4139a99845ff | -8.23107 | -44.00929 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a748f96a-61ef-341c-9f55-a5062a838718 | -10.50903 | -43.42769 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 503d4863-33da-3c55-bc0a-fe7f20628d10 | -10.15855 | -44.54148 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b50866d7-55dd-3968-9ea5-228f34dabe41 | -9.9678 | -45.52877 | 2025-10-17 04:19:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d205e54-d2c0-3c75-8259-0b102d025158 | -11.39586 | -44.20168 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9caa5ffa-8957-3fc9-99d7-dfed9807fa4c | -5.45954 | -42.95138 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a0497405-a134-3554-923c-1bb1340ad3cb | -7.47596 | -42.754 | 2025-10-17 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ee4fcdb-cd73-371b-ba76-a51cbdc69249 | -6.42553 | -46.88579 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1dc41f8-4a3f-3623-953d-fb75fa7758d1 | -6.07329 | -41.9077 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4cc5c1dd-8f32-3115-8028-1adcd907cd93 | -6.39232 | -41.47301 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 84dd8c33-3521-3942-bcaf-d61c227419d6 | -10.05547 | -43.83303 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| bba6db73-4d9e-30bb-8ad5-2b61c4f4ad3f | -8.60819 | -47.12443 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc7d7839-985c-3284-87b0-0bffbff34992 | -4.58814 | -46.27124 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6eb4a82-db3a-38dd-813b-a7b1015bef57 | -5.71242 | -44.52036 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d113e853-d980-3e46-bc29-8afbe897b3e4 | -8.19759 | -43.31534 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 6be3cda6-93c7-3b12-a5e2-99696ab03e0f | -11.39649 | -44.22054 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fcd42eb-f6ac-3a6b-b7f3-5d024c766bf3 | -6.28628 | -44.02415 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3fe76c5-63ac-37f2-90cd-00fe3a6b792b | -11.48475 | -44.1854 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffc12200-e1c3-38b6-89de-5421a0495ea8 | -6.22942 | -44.15014 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa96b195-650e-3fff-aee0-e935028b98d2 | -4.1055 | -48.02239 | 2025-10-17 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd25e641-4469-3fc4-b1ef-39b9d27bf822 | -9.93234 | -45.34503 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d5da46f-7f06-3548-9fbd-7b3baee540e5 | -5.43222 | -43.30122 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6002ae4-deab-3e87-82b1-4efe64794ed3 | -8.2433 | -44.01842 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0edcf3a2-379f-3731-81f1-b8bb15fbc334 | -5.71526 | -46.45192 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f29ac6a-a2e6-365b-966b-4a3dbfca24e6 | -4.86406 | -44.43876 | 2025-10-17 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d8f9c96-615f-3b57-af6c-820178db99ed | -9.05031 | -46.0818 | 2025-10-17 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| edb38765-4a48-307a-8f7b-39d47601fa3a | -5.8735 | -43.85662 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a2d542d-899c-3af3-a6ec-87c6fa513af8 | -10.50379 | -43.39244 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ad2ce84-6983-38f2-91f4-d9fe27d00e60 | -5.12731 | -42.65287 | 2025-10-17 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52c7f9f4-6e7d-32de-ae70-38316cf64942 | -5.32739 | -45.688 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6328ec2-621f-3236-a2b4-6164e3f1484a | -6.31837 | -45.51335 | 2025-10-17 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bbabd1f-b0bc-3c14-baf1-01784cfc241f | -4.26031 | -48.54841 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f5db60f-4593-391a-a898-dbd7f44f914e | -5.32911 | -42.93556 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93870e85-61ab-36c4-ba5e-5a52390b8779 | -7.29614 | -42.32442 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 326b2ba6-2b20-3e67-baf1-6aaaf20bb9c7 | -8.70145 | -46.98294 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7705ca4b-0701-3898-ba84-508f7e4963eb | -7.7477 | -42.50784 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 45b9d354-cc04-313c-87da-a6d3098383fa | -8.48234 | -40.60677 | 2025-10-17 04:19:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44a8cfef-ab50-3a64-bbaf-796e1031559e | -8.55757 | -45.49414 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b33bdfa-7f20-3f48-b877-a2a88e1cf7d4 | -7.29674 | -42.32053 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f87cc15-2c6f-37eb-bc39-f12b54fcd1e2 | -10.94908 | -43.08172 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba29a193-4766-3399-904e-46598494c678 | -11.40999 | -44.22264 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 232ebc6d-9c26-34cc-94d8-e492345e9772 | -4.82918 | -41.46661 | 2025-10-17 04:19:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e35e501-da0e-3a74-af6a-3a1dcfce400b | -4.82469 | -47.08463 | 2025-10-17 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83361ef4-efc7-3767-b5d2-a0844fcb5644 | -10.58023 | -47.428 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67598b47-7f72-34c1-ab24-66e2d9f5c63d | -5.04201 | -42.85849 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9003aab1-e11b-3c05-b637-6c8dda08afd9 | -8.82822 | -47.30592 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d33ea176-c9a6-3e86-bc04-d12db59428fb | -11.47631 | -44.19539 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c25b9ae-5070-3707-99af-a3fe915ba5c9 | -2.96104 | -52.50607 | 2025-10-17 04:19:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 140aad3e-f7ca-3655-b6b7-ecfd6fe0bdcd | -10.28358 | -44.03616 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7c73558-6628-3526-8a4c-93768f17be37 | -6.59289 | -44.37416 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffe11ddb-dd36-30f6-8dd8-315fc385992f | -4.83628 | -41.46754 | 2025-10-17 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5df7aae7-42db-3e38-96df-0246c6566f04 | -8.40912 | -46.28252 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23d7c4cf-30f0-397c-b105-8ce7a7242edf | -5.52041 | -43.52347 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4f82d6e-559c-3d4e-9939-8b14f7b30a02 | -5.0621 | -45.472 | 2025-10-17 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1666a2e8-84b9-3373-b178-28e852bfd9ea | -7.27986 | -42.31393 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2a28c516-2f75-3aa6-885b-8fafb0b50c0b | -5.60578 | -49.03164 | 2025-10-17 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c2c534ce-fb39-3067-8792-4c094c79dcc2 | -7.5293 | -46.84137 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43312d66-75b1-35e9-83a6-535723a50e4c | -8.25275 | -44.02349 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06584d30-f487-312d-ba81-844dc95095ce | -5.16718 | -45.21629 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc66826f-ac55-327d-a35f-8c516f3bb22c | -7.97351 | -44.13535 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1646980e-50ee-377a-b06b-ec163f04e814 | -10.6506 | -45.25298 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a4fbe9b-bb1c-33dc-a601-727af22a9191 | -7.24684 | -40.7475 | 2025-10-17 04:19:00 | NOAA-21 | FRANCISCO MACEDO | PIAUÍ | Brasil | 2204154 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 092bb6b4-c7cc-30e7-8f9e-124dea740f52 | -3.76382 | -48.92564 | 2025-10-17 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15c23e1e-e725-357d-98af-c523546f5fb8 | -11.39821 | -44.23207 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e2e770f-338a-30c5-827c-57580a957327 | -10.29258 | -44.04491 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 03a8eb48-9887-384a-98b4-d73608808acc | -5.28364 | -47.92661 | 2025-10-17 04:19:00 | NOAA-21 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21a589a8-4f37-3b85-b5b0-9b9e59a1d864 | -5.3502 | -45.73901 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 915ffd5b-3f69-32c5-8c4b-074e41eb6a51 | -5.91557 | -44.74317 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8e684260-8745-3262-9f74-2c507892ba30 | -2.88219 | -50.73515 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0fc023cc-9097-31dc-8ab9-2d30ad98744b | -8.0865 | -45.43946 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 587c2f2d-909b-32d5-8a6c-5b615168659d | -9.36872 | -46.98518 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce66e7ce-39ee-3700-ae08-ef046d9cd43d | -8.45663 | -46.23901 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f34f49e5-3eb5-33a6-8038-ef9bd3e20902 | -6.53704 | -55.05137 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1731883f-cee6-3cde-8fb8-51553a4474b2 | -9.38417 | -46.95385 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d8da054-d667-3b27-9b0e-c289a326189d | -8.24787 | -47.87162 | 2025-10-17 04:19:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ba0a1d8-5281-36dc-8b80-ee3e204b8a26 | -6.38872 | -41.47246 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6ae92af4-f28e-30c8-81e6-16bb4117bde3 | -6.5313 | -55.05038 | 2025-10-17 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c54c6f3-a1af-312a-b724-13d26cc308c4 | -10.50215 | -43.42665 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 50697972-8001-3951-b4be-02a503d6985d | -8.45323 | -44.17764 | 2025-10-17 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df7af7ca-9065-3fec-a623-f78263a103e9 | -6.8237 | -41.68931 | 2025-10-17 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c898e57f-8628-3855-a115-88b2b9430441 | -7.17879 | -42.35843 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 88287be5-566f-3d28-9fe0-58448f7fa3ad | -10.59188 | -47.39933 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 607f1d24-c989-303c-8f6e-eac9f97287c0 | -10.28248 | -44.04336 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8469f817-0efd-3ab1-89bc-dd61550cb093 | -5.19871 | -47.48516 | 2025-10-17 04:19:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b201888f-c7a2-3188-84a1-09b42bddc624 | -9.27039 | -45.27083 | 2025-10-17 04:19:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 609bd96c-21a5-3a61-b8e2-b3ffa51d69e8 | -9.09796 | -46.67977 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67e6e950-a1b4-3f88-86f6-2e8501cf261c | -5.34573 | -45.74559 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9178035-d8ee-3d4a-a5e1-97b0677d0d40 | -7.17336 | -42.18148 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5f71c0fd-21df-3520-80ce-f00181b1a33b | -10.10622 | -44.57327 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 61f007fa-6e8a-3b64-99c7-67d9a3eb7970 | -7.18398 | -42.37117 | 2025-10-17 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6cf36b0a-93f9-3222-8244-98c870a87e6b | -10.52594 | -49.55035 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| ed5c8bbc-54cb-3e24-b822-40233a7aaaba | -6.07665 | -41.91488 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| de8e11b6-9796-3062-badf-78a44bfea604 | -5.96673 | -42.87689 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3731a5b6-5583-3fb6-8b96-b082d2d8d05f | -5.88659 | -43.88363 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40b410ff-3ccc-3f48-8091-5ab53eeb89af | -7.71815 | -47.84652 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32c2760b-2e2a-331c-ae4b-55cc8712fa9c | -10.11189 | -44.62468 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ef208f3-a6bc-347a-8b09-638f907b12a7 | -10.29535 | -44.02675 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
