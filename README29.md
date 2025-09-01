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
| 468b75ae-a327-3d8b-92ea-b0f44bc1ff6e | -6.33703 | -43.52523 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa98d19d-aa8d-35a6-b073-6c05d3eae780 | -6.30038 | -43.62029 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c854a49-8363-3713-bacd-d8a682b51768 | -9.67004 | -47.81772 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7bb524f-e23b-3a46-8734-83fedddc071c | -6.26619 | -42.6143 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 30e0dfd2-8dce-3bcf-b544-6d45dacd6289 | -8.84696 | -47.50244 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0606183b-316e-31e6-acaa-55b4b34acad0 | -7.09141 | -44.34492 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| d0e37919-7d2f-39f1-8cf9-ab2b3679f8e7 | -10.24196 | -51.1177 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97d5b3a1-b98a-37dd-8900-da1959c6978d | -6.83106 | -52.81821 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e43ef27-506b-3b4a-a9f4-9f3365ce1539 | -6.15877 | -43.33113 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9e832fc-d2e7-39f4-8a89-b32ca9ec7b87 | -6.44933 | -43.94898 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31c6c305-3240-3a72-bf0d-466220cc620e | -5.36092 | -41.15136 | 2025-09-01 04:10:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1528a2f9-e1b0-3720-b65a-95a64aa105c6 | -11.37198 | -43.62421 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62391e20-9f07-30e4-8b45-f1d297359285 | -5.99448 | -43.37042 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c1c6c0d7-bded-38a0-81a2-26136e003c96 | -7.10937 | -44.77404 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eae164ef-192e-392d-9137-81fba6c3dd1a | -11.03722 | -47.04034 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46d69d15-5a7b-3fc8-a806-2d8e85e3355e | -7.07202 | -44.33829 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22990de8-ec6e-3aac-9a9b-5954a7f68037 | -11.89114 | -46.748 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d837ac0-ceed-365f-98bd-a0410bb7500e | -6.30978 | -43.78675 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e335246b-229d-3646-abca-025a63d43c60 | -6.79354 | -52.81583 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35b9fec7-55ae-34aa-8f4a-17d9acd071f9 | -7.06942 | -44.35438 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 795a8161-325e-3c3e-b96e-85ddf16d5877 | -7.69726 | -46.7156 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdb3788a-f3ae-356c-9bae-f32de552fc85 | -7.6265 | -44.03312 | 2025-09-01 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a66998b-0ff1-3648-8e53-87c6c54c7fa8 | -11.90025 | -46.67845 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de6161b2-3bc9-34ac-a6e9-89a9b3dc4794 | -11.95566 | -45.83626 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4607de0c-8ba8-3af4-9d4f-82f73f0fcad6 | -8.49548 | -44.74578 | 2025-09-01 04:10:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 28e40bb2-d68a-3ff9-99d2-888a7bb92bf1 | -6.94142 | -45.56459 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc4305ba-db32-3003-a9f3-1873cf60ba08 | -6.28127 | -43.56239 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8465df1-e99a-3f80-9cdf-2595dadb1020 | -12.32524 | -45.72539 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd5d1cab-494f-381e-a925-f297def5dbc0 | -5.81857 | -43.2283 | 2025-09-01 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ec6a658-15a7-30ad-a8c5-158948e81429 | -7.4577 | -44.81316 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5c606fef-7f50-3d52-a112-7c61c174a971 | -6.29236 | -43.29846 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ace06ed-8e60-33b2-a021-4f8d51c8f19a | -7.08268 | -44.34011 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 516ddce9-a328-36f4-91ee-3e8917d37484 | -6.18119 | -43.31498 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f76f45b3-4ea5-3768-9716-f4df70a9a6e6 | -6.84947 | -52.82127 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d63e1c20-65cb-3e5d-b866-f5f7f8240a73 | -8.9197 | -45.87135 | 2025-09-01 04:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36dcdd82-401b-38d2-b778-be08c5eb3253 | -6.28326 | -43.28942 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17c8e058-9876-3f72-855a-6369f7adcfca | -5.4348 | -49.99549 | 2025-09-01 04:10:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 25a53ee3-fbf9-31bc-a478-155bdd484572 | -6.27111 | -43.53743 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f72e7a94-4616-3008-a4fe-e02d3f457ebc | -4.48232 | -48.11864 | 2025-09-01 04:10:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88a60736-9f37-3a5e-974a-2291eb2b4488 | -7.08007 | -44.35625 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef49189f-c249-3b27-a9eb-cc22ab9b3365 | -6.46987 | -42.43548 | 2025-09-01 04:10:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 93e7ad7e-6732-3e3f-b24a-8c2ea8bbc5c2 | -6.16446 | -43.33978 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3567ef4f-bcdf-3b06-9e96-a3c6ac420321 | -10.04309 | -48.10647 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 60a7da03-b5f8-37fc-aff4-e2ec62a2f8d1 | -8.17476 | -45.03852 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8229fcab-1c67-363b-b626-2b605945cc28 | -6.84418 | -52.81568 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 527be896-763e-37d3-bd13-599c96ad652f | -11.87685 | -46.74033 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffab22d6-8590-3986-ba07-6c5d656e683e | -8.08195 | -49.94328 | 2025-09-01 04:10:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76568b7c-2e1a-31e3-9ab8-0b4bed2d36b3 | -9.1525 | -45.22086 | 2025-09-01 04:10:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19970c4e-f5bd-3b91-97d5-3d4003c1e721 | -8.89994 | -45.12194 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89d61c4a-10ca-312b-bdb5-b8965e9a25c6 | -6.53891 | -42.96075 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 794e8741-1206-3aea-9aa5-f3392fa6a15b | -6.81138 | -45.69724 | 2025-09-01 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| ec46ce32-103b-3aa4-8aeb-cdb00047303a | -9.15699 | -47.93366 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2e68bb9-e085-3607-9fa8-36f8b41ecfe5 | -7.47899 | -45.99493 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab2f9902-d200-3fa1-98ca-758fac4009c4 | -6.15593 | -43.32681 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea087530-b0ec-3203-9973-1278ba7441d2 | -11.04325 | -47.00517 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79ab5cf6-a26b-3efe-8ebd-771da932dbc0 | -7.11091 | -44.31534 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 744e2116-a7e2-357d-bac5-7adf13ff64b6 | -11.89811 | -46.68587 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c6a6e848-fe42-3c05-89b6-938b1f276ea3 | -7.74326 | -50.26089 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0a7e0083-8d1a-35a3-ae03-7fb473038299 | -11.37869 | -43.62534 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea8f36db-8376-38e6-bc0e-cb29e0d77bf7 | -11.04943 | -46.8993 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9acd1bc9-4ea0-31e7-bcc6-a78f00062274 | -11.04665 | -45.14688 | 2025-09-01 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 8a6fbd49-de61-3426-8f28-a4914ee4b1d0 | -8.76756 | -46.10437 | 2025-09-01 04:10:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c32258e-2fb8-3c97-97f1-11f14158ba8b | -7.08783 | -44.35345 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 6b70e2fa-34b0-3249-bd03-3ec3a1828ce6 | -6.29114 | -43.30591 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b6fac4f-0b14-350a-9e6e-0e7e1e716111 | -7.11074 | -44.76561 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1888eb7c-b9af-3048-8480-cace6caee7ee | -6.26863 | -43.5526 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f6dabdc-1d0d-3bfe-bb1b-e8f9aa28c25f | -7.73827 | -50.25936 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f9f83ce-5b2a-3005-a649-c371fee719fc | -11.81684 | -46.41494 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 761cea62-c645-3643-a50c-04704bd7cf8d | -7.10449 | -44.31006 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8a0fa585-ddc9-3280-8b02-f1ed0d69ffca | -10.24711 | -51.1188 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d533e9b8-3bf0-397d-8e7e-e9a02be596ec | -7.58974 | -42.68641 | 2025-09-01 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 244a68d2-7362-3644-9629-bde5f4bf1857 | -6.15069 | -43.33751 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de66b3ed-3385-3811-81dc-f63ef2ce3e69 | -8.8898 | -45.11588 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21901d21-c559-367f-b505-87fa152f1d33 | -11.7996 | -46.42614 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8cf36dfa-76d6-3293-8420-e83351b31da9 | -6.28757 | -43.56739 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03806942-ee5b-3563-b460-e48848d5d7a6 | -6.29863 | -43.30322 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20d83bb8-1167-396d-b28f-2c7d5d1d2267 | -9.23476 | -47.06879 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e23b84ed-18c7-303e-a5e6-2bfc3b55e422 | -7.70143 | -50.27534 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2933da11-432e-3780-99be-ae98ab37d99e | -8.19763 | -46.7826 | 2025-09-01 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fe48e354-4e5b-3fd0-b422-07e55b339441 | -6.57135 | -43.70936 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a80d22d-09c6-3290-b042-84b30565632f | -6.15249 | -43.32624 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c8e08f7-8d7d-31a4-ac6f-4fdb2e8a3f9c | -6.11625 | -43.33205 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb5300f8-d342-3aa7-a355-3ef865cedb2e | -10.23801 | -51.11026 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e36dbd09-e617-3b69-a2c3-e2a35864ef05 | -6.24255 | -42.41701 | 2025-09-01 04:10:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 330eaf7d-bf86-3ab8-9e66-36f86fc4e557 | -7.07877 | -44.36434 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 23e6824a-8146-3f8c-b04e-44ce401ee447 | -9.66844 | -47.04174 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1068243f-4041-3b59-a3c6-e0d88dbdefb5 | -11.8883 | -46.74945 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90f375ba-c855-305b-8596-3ae19a289de1 | -5.40452 | -43.36388 | 2025-09-01 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61dfcbfc-a6c7-305e-8f9d-f8527be54853 | -7.46282 | -44.82711 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb935cc2-562b-385f-bbda-8b0bb64f7dcf | -11.91008 | -44.88361 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5838130-9540-30c8-b15f-7138d3517bb5 | -8.84562 | -47.51009 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b402ee60-6db2-3ae2-8372-81539510a48d | -7.07557 | -44.33891 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a8a1cee-af5d-3b0f-b945-d94e22bc0b04 | -6.18303 | -44.20969 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17d775f6-2438-34a3-b4bd-c22c508f319e | -11.80553 | -44.94542 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91898549-a8b5-3ba0-ba7b-e3691fd3686f | -11.33005 | -43.69134 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcd9e6c6-b9b0-32f0-ae30-6423d6f26e97 | -9.63851 | -47.80049 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5d56207-2a4a-34f7-9593-59969a2705e4 | -11.32601 | -43.47359 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aeb32a2a-99f5-3039-9d44-59ca9b35aa24 | -6.85882 | -43.49148 | 2025-09-01 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af456011-4a83-3566-afc9-fe696cac16d5 | -7.08584 | -44.35645 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| eff7edf6-f1d8-30a7-a801-22a87070de1c | -9.63715 | -46.59964 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
