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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c331ec4-16d4-3714-b0cf-af2d2f050b01 | -20.08301 | -46.89737 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e221b3b8-6baa-37bc-9b3e-bc28cf8069e6 | -15.78736 | -52.27457 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42c006ea-303f-3285-82db-1d327f0212be | -15.12529 | -52.48315 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45f43a77-cc2f-33fd-99f1-78217a2500c2 | -15.76101 | -52.24734 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7e74cc77-72b6-3f47-9702-a6664e4c19d2 | -15.76822 | -52.22437 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bbfe35a-63c8-3e91-a1c4-2fe03236e2ab | -15.29352 | -53.78596 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| deadb14a-206c-322a-9ba2-d1c7844c0e0c | -14.7525 | -55.61875 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5a1bb0d-692c-36e1-828a-c258281e8563 | -15.19951 | -52.48192 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5b73872-1fca-39ce-ac12-d131652f35ac | -16.58236 | -55.1676 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 561ddcca-c741-3c64-a4d8-3eb6271b2be0 | -18.14033 | -49.19176 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3c00bd81-c20b-31be-aa2b-730c692a57f9 | -15.69703 | -54.36367 | 2025-09-14 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd08d7cb-abb1-3ff1-b77e-3684138997ba | -18.25955 | -49.4627 | 2025-09-14 05:10:00 | NPP-375D | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c392338-d9bf-32cc-aaa5-66121ca0eb12 | -20.6204 | -50.36942 | 2025-09-14 05:10:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f9ecf12-ec33-30b8-bbcb-925719c72bcb | -14.91199 | -55.95249 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d73fac33-8ee4-3827-bd2c-d04a29aac2ec | -17.83321 | -50.42839 | 2025-09-14 05:10:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b127585d-772b-339a-bb65-a9026c640b79 | -20.25212 | -47.79411 | 2025-09-14 05:10:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4570c4b-edb8-3453-971e-f438fd2c5624 | -18.62975 | -47.18037 | 2025-09-14 05:10:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e18c985d-82cf-3d1b-aa2a-dd16e0a8a3e7 | -18.06329 | -50.73991 | 2025-09-14 05:10:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04f21790-50c3-3421-8d69-14fa8fd66164 | -14.95477 | -55.9478 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70a94ac9-c149-38d7-9fbf-4a50a6965d5e | -22.17776 | -49.61535 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fa39035-dbc0-34fa-805e-f7970467983c | -15.19849 | -52.48969 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a9b9468-f42e-376c-b921-d188995430ec | -17.31977 | -46.0869 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b9131e7-d346-3736-a580-b4f6574c77ed | -15.85956 | -51.85092 | 2025-09-14 05:10:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18841639-cfad-3d5d-bd89-08c06883f2da | -15.59354 | -54.78252 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bccf497d-57ef-353e-acaf-c95f1d12765d | -16.28597 | -45.68628 | 2025-09-14 05:10:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795a6948-fa5f-323e-98d6-2e469c40d63e | -15.43454 | -47.35841 | 2025-09-14 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abe70f76-b2d4-390e-a826-cb64a420613e | -20.08685 | -46.89905 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b441d84c-bb2e-3d8d-8a81-0aca904447e1 | -20.90564 | -55.18309 | 2025-09-14 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf39528e-e748-354b-a039-595203b4f8fe | -21.65674 | -50.12234 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 76a2f71f-b464-3599-9a8f-8da935b04161 | -18.4593 | -49.57414 | 2025-09-14 05:10:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ba7e7748-9de1-3e81-934a-55531872bcdb | -18.14748 | -49.1878 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6770914b-9b75-3662-b5c9-427193e29465 | -17.14697 | -53.89026 | 2025-09-14 05:10:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59d266a0-a1b2-32f9-888c-4f662e75ae8d | -20.905 | -55.18786 | 2025-09-14 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dedde63-ca48-3340-892c-f7e6d3def332 | -16.49563 | -55.12171 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 00b46830-bc67-35ba-8504-cf6c1689f4a9 | -15.76351 | -52.2278 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ea26493-1c4e-318d-a633-212163cc43d9 | -15.58399 | -54.74635 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0eb989cf-f0a5-339c-a2b3-a1a5956f1b66 | -16.49203 | -55.1212 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c6b62a0d-5edd-36c2-928a-f5cdc63ffa70 | -18.46416 | -49.57794 | 2025-09-14 05:10:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| efcc1e58-cbfd-3076-b5b0-c296fe6bc4fe | -15.52037 | -48.52413 | 2025-09-14 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f8e4aac-70da-3689-a5f9-0332681d3141 | -15.28346 | -53.77489 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b54389c-7e44-3c5e-8bf5-701df92bafca | -16.28631 | -45.68716 | 2025-09-14 05:10:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 314ec3a2-8596-3afb-91f2-646cee4d8529 | -21.65639 | -50.1257 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fd68025a-e52d-3396-ad12-1d6ad63d62a2 | -15.16061 | -52.46881 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fbb96fb-028c-3ff8-a826-55babad1fea5 | -18.15703 | -49.19852 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 22e113eb-08d6-395f-a220-a1ac3dd9dc76 | -20.09977 | -54.61244 | 2025-09-14 05:10:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4028af20-a657-3d0d-beb3-66acf2502239 | -20.2645 | -57.16171 | 2025-09-14 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80487191-e60e-3f60-a1b5-57a0f95501f8 | -16.56804 | -55.11363 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d3245065-7ec7-32ab-ade9-e347c5e9b0b3 | -15.71551 | -54.36628 | 2025-09-14 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7e4d3b9-b517-3d0e-a62b-b527addf594b | -15.62185 | -52.78237 | 2025-09-14 05:10:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f313fdf-613a-36f9-abf6-7a3ce58a2420 | -21.30158 | -48.55462 | 2025-09-14 05:10:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a63246be-585f-3011-9b30-40d14c3d8dda | -15.58693 | -54.77718 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87afb8de-3050-32c2-8859-4bafc16b4899 | -15.59251 | -54.73849 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fceb6f56-a362-3512-9062-85e1eab415bc | -18.01418 | -46.96957 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a5f5a3f-2785-3e10-b3e1-0eed83650eb3 | -15.29105 | -53.77601 | 2025-09-14 05:10:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64b1327f-f5ed-3118-9485-8cd9d98e0d33 | -20.12704 | -46.87447 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96724dac-24ba-3751-8819-03664ca2bf1d | -16.36438 | -51.77563 | 2025-09-14 05:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8addc47-1f45-35f0-a481-f0dc145fa047 | -20.76516 | -56.95159 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 05b09359-cef0-3a69-b6dd-f6e0dd3d6b2e | -17.40722 | -49.26502 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee4f28c2-1f85-3c49-bc24-7d6693a2effc | -17.25902 | -49.26325 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b732ee3d-2bc2-35b0-ad27-fc8d6b6aa993 | -15.15146 | -52.47475 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0d88515-9235-3810-bb96-0dd31a3bbce1 | -18.97955 | -48.59602 | 2025-09-14 05:10:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b14b8106-2be0-3075-bb75-5bbbf2021035 | -14.47526 | -55.96403 | 2025-09-14 05:10:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddd56208-03a7-3e89-a255-2c58986821fd | -20.08771 | -46.8893 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b69a226-5933-3f02-817f-3a7c60ce7005 | -15.76051 | -52.25125 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 24544007-3b1d-3785-8f79-592a22255f97 | -20.90318 | -55.17284 | 2025-09-14 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e272561e-01c3-362a-b80b-f6d02ff65169 | -17.29773 | -46.11352 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c58c57c-22fa-3b11-af51-1aac9245ca73 | -20.76575 | -56.94758 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0859caf-ae66-316f-9f47-4f7cf11c189f | -15.12067 | -52.48651 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd7d44f0-eb2b-318d-bf4d-51fa09bc81e0 | -21.65685 | -50.12568 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1803498-a818-3f27-aa33-fa45a6d71626 | -17.99073 | -46.95689 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04347dc3-a9a9-3c07-b4b9-fdf5bb2b7173 | -17.433 | -49.22372 | 2025-09-14 05:10:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 051c4b48-f55a-3475-8d88-9cf333208225 | -15.59416 | -54.77824 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59a9f9bd-d4d8-342d-9695-8842204c3cdf | -17.31984 | -46.09644 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e7233488-27a5-3a64-9efc-fbf39d68b545 | -14.75725 | -60.23781 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4554088-9bc0-3205-aa6f-c4ee712f6a6a | -15.67174 | -52.24336 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96087e86-3cf0-3a48-bfbb-ecfa2a756400 | -15.42692 | -58.77865 | 2025-09-14 05:10:00 | NPP-375D | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2ef6faa-1d52-3416-a23e-c2ff20436920 | -14.75435 | -60.21189 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f21879f-25da-35fa-86b2-24be508cf3e7 | -21.64902 | -50.2047 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b8a8bff1-074d-3dde-89c3-00a90d38472e | -21.64801 | -50.20457 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f8e44e6-8542-3f2f-b772-a1f8a72192fb | -15.69011 | -54.34676 | 2025-09-14 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cf61189-5b48-330e-89d6-268ea19d563e | -20.90876 | -55.18841 | 2025-09-14 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8029311-2b62-30e2-ab77-52792596ba2f | -17.25794 | -49.27275 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 197695e5-89f4-3311-9c7f-13fa1e36a67e | -14.93825 | -55.96453 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e9b20c9-d62e-3962-bf9c-477e550568c7 | -20.62106 | -50.3632 | 2025-09-14 05:10:00 | NPP-375D | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6d415481-6c50-3202-85a4-186a7c2cb94b | -17.60825 | -51.83233 | 2025-09-14 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4270db1c-c2fd-3c1b-aab5-2f5bf2d488cc | -15.80575 | -52.19901 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d439d4b-e2f0-3fe0-9e34-7ec5859107c0 | -15.43058 | -52.91268 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77dcd46a-4988-39f2-9692-f8d26d2970f5 | -17.99768 | -46.94902 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb1553c0-7e30-302c-856e-a7439dd148dd | -15.77428 | -53.47887 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a654290c-fd3e-3ca4-9ef6-5f428c6b9b2b | -16.48423 | -55.12446 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3b41844f-c299-362c-888d-8c3646d5b386 | -15.80378 | -52.21419 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 94140795-e035-36cc-97a6-13b7da70c0a5 | -17.32026 | -46.09202 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0a68da1-4e08-3cb6-8e9b-d3f741f80cfa | -15.8601 | -51.84675 | 2025-09-14 05:10:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f49fa908-8d69-34ff-b42f-26d4c2a5741b | -22.18926 | -49.61001 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a766f88-c6ea-3d08-8afa-82c61b57d641 | -17.29814 | -46.10935 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5a1dd19-1206-3c05-8f12-6c3550c5b03f | -18.26478 | -49.46328 | 2025-09-14 05:10:00 | NPP-375D | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc099a83-de65-3cde-821b-c336a5540ee3 | -15.12882 | -52.48792 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 060801c5-4008-39de-8d67-6fe0a11b802d | -21.75374 | -53.31211 | 2025-09-14 05:10:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b19be30a-59d5-3975-8de6-700194d2c752 | -21.64836 | -50.20134 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 505d606b-b86a-375e-8657-ab90794cc04e | -17.2622 | -47.24211 | 2025-09-14 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README64.md)
