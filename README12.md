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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0460aff4-58b9-3afe-9438-4bbceae58459 | -8.24113 | -46.80534 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 480a59fd-527d-3974-8708-f4e7ba4085ef | -6.88206 | -47.23939 | 2025-10-05 00:35:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4c65d33e-8c76-39bf-af8c-ed66fbc184d2 | -7.75434 | -46.32259 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b8cada16-8619-3e3d-9deb-e2aeb0785e5a | -2.10708 | -47.50969 | 2025-10-05 00:35:00 | TERRA_M-M | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e802fd7d-90ba-3828-ad4c-4cc983408da3 | -8.70036 | -49.36425 | 2025-10-05 00:35:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1eaabb37-17ef-3f3e-9891-5539f26c7af5 | -6.21718 | -42.93427 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ff30bc13-519a-3a78-9389-f8513fb1ba51 | -4.8814 | -45.85909 | 2025-10-05 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 38a2fc21-64e4-3c25-b63d-15bd7cd7d201 | -8.52493 | -50.02761 | 2025-10-05 00:35:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2308f311-b41b-3a4c-ae26-b81810db5c4a | -7.73513 | -46.32576 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| d2b53e78-7329-3bb1-ada2-34790c017d27 | -7.52398 | -43.85506 | 2025-10-05 00:35:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d6250715-72a3-33ff-9511-ad17adf07322 | -6.14396 | -44.63492 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| b5ab491f-c74f-38a1-9f03-5f6d7a37a110 | -4.628 | -43.18789 | 2025-10-05 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| be586c60-68be-3cd4-862a-5362004dfd86 | -2.57101 | -48.96446 | 2025-10-05 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bb7ec60c-b348-389d-96eb-3d3bcdd6ac24 | -4.31091 | -48.0939 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0a55c9ba-3fe9-3315-b080-9144ce155d09 | -7.77179 | -42.62419 | 2025-10-05 00:35:00 | TERRA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 42048cde-83f0-32f0-8185-695b912e0e66 | -6.60393 | -44.31982 | 2025-10-05 00:35:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 41e937c4-a595-3ae8-ad86-6b37ca9cea44 | -7.74356 | -42.52719 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| ebb86fcb-cfef-3f1b-9e14-8a2d6bd7ace8 | -3.85008 | -41.58027 | 2025-10-05 00:35:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 53.6 |
| 249728ac-4ab7-3441-94bc-47c87984c71d | -4.76319 | -46.90625 | 2025-10-05 00:35:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 00b73b3f-4e80-3a8f-82d8-f4288f17f3e1 | -6.61695 | -43.73241 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1a3d2c16-db65-3469-aa9f-fccfe41d6518 | -2.2511 | -47.87412 | 2025-10-05 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 708e1770-867e-31d4-9eea-59bd80b4ac88 | -6.15944 | -44.66257 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 303.7 |
| cdff4158-90fd-398e-9ed0-a8fe1df6e035 | -4.87965 | -45.84672 | 2025-10-05 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| bfc069bf-031c-3cbf-aac2-60069b3b9494 | -4.6379 | -43.16585 | 2025-10-05 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1f48248f-9a20-3f9b-aad2-0771d5845466 | -3.61396 | -51.03803 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 3706ab76-6134-30a6-a4a4-f3e5b4fb5808 | -5.12902 | -46.23447 | 2025-10-05 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d954ad4a-743e-3b1b-8d30-349ad5b5441d | -8.23323 | -46.81661 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 42fcd926-60af-3e6c-943c-849d737fc9ad | -4.25761 | -48.56853 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| f294ea1b-3cd5-3504-b9d7-dc5887f4f07d | -5.84328 | -42.89482 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| b5011a43-e243-3757-bb09-2ff4836b9ee3 | -6.40913 | -43.07854 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| c435d702-e73e-3436-9e02-ecdf0f4fa364 | -3.81336 | -51.08167 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c7e8c915-a3b8-33da-8eae-1ade6c51c144 | -7.71598 | -46.26298 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ecd10467-0387-307e-9930-310d3b961cbe | -6.22903 | -46.91591 | 2025-10-05 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 390277bb-21a0-3929-a539-c089a6f0d163 | -8.35069 | -49.5019 | 2025-10-05 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 3ab0b737-97b0-3693-bad5-247a4ce2fad8 | -7.69921 | -46.23832 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 14a24322-e621-305d-8ae6-b7792459fa85 | -7.43476 | -46.96964 | 2025-10-05 00:35:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1d43c20a-228a-332b-960e-ae227d86ee82 | -8.23182 | -46.80674 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f7aeddae-1cf7-3667-8e54-2e900a86cee7 | -7.72551 | -46.32731 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 4d76250a-a1bc-34c2-8184-98b53be1f013 | -5.29484 | -44.33424 | 2025-10-05 00:35:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4be0e2dd-9ae9-3030-80eb-7f9b3e4d91ab | -7.72394 | -46.31666 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 48ef41ca-188f-313b-9e77-c7028c781dc7 | -6.02212 | -45.42253 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d2cf20bd-088c-3627-aac7-2abe629f1380 | -4.64388 | -43.20592 | 2025-10-05 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 842ac4be-50e7-3620-863c-4726400a4373 | -6.43079 | -47.17424 | 2025-10-05 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 29eb47b7-aeb8-3cce-82ad-e44e724fd53d | -6.29056 | -43.92719 | 2025-10-05 00:35:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| b0a35652-d886-3162-98f1-0a87323a5160 | -8.34946 | -49.49297 | 2025-10-05 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 7deec1c4-4d57-36ce-b76c-eab988e21980 | -6.60226 | -44.31433 | 2025-10-05 00:35:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e7da627f-346b-3aa2-a016-b94ebe7e1705 | -4.25634 | -48.55942 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 563bb6ec-dd12-3bf4-bbd3-8d37a2d0dc7e | -2.90708 | -48.08231 | 2025-10-05 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8d824925-5dad-334d-b63c-379742789c1e | -7.0206 | -42.78 | 2025-10-05 00:35:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 263d3c6f-1431-3bfc-a453-83a170cc94c8 | -5.92193 | -43.32092 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 9bf0126a-8f33-305f-9bec-66a714b8e0db | -3.3909 | -50.15119 | 2025-10-05 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 03ef6310-b842-3efa-b66b-e2c80d450e36 | -8.25045 | -46.80393 | 2025-10-05 00:35:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0e115fee-b178-3ef8-a2cd-7d0b7fbcb53b | -2.90569 | -48.07258 | 2025-10-05 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a95867f1-1903-307b-be8a-99d4a6cef554 | -6.91022 | -45.05428 | 2025-10-05 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7ddfc09e-ac81-3197-a5ba-02f679366940 | -7.16833 | -45.07554 | 2025-10-05 00:35:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 89299cb4-8a77-3742-a3ab-d6cb91545c4d | -5.93723 | -43.33765 | 2025-10-05 00:35:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 0641158e-1220-3dd3-b4ad-941b30725d3b | -6.39419 | -43.05535 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 42c7f7ba-5518-3248-8ed6-1f844b5dc977 | -7.16526 | -46.21488 | 2025-10-05 00:35:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| d9e63120-bfe4-364b-88d4-95fde99eab07 | -5.06608 | -40.49286 | 2025-10-05 00:35:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 941178b3-12c5-3847-8bb2-d7b067a5e964 | -6.66907 | -42.38379 | 2025-10-05 00:35:00 | TERRA_M-M | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| c7efbbe1-f5b6-38ab-8ec9-632c99f08f4b | -6.35601 | -43.91136 | 2025-10-05 00:35:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 614834af-6b7e-35ce-8a6f-ade7d99b4c94 | -5.25184 | -42.63603 | 2025-10-05 00:35:00 | TERRA_M-M | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c6ee4909-10b7-38bd-8bfd-0cbbba02d419 | -5.64184 | -43.89747 | 2025-10-05 00:35:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 05f5c6e9-9938-3891-9727-be15e5250308 | -4.0673 | -45.21808 | 2025-10-05 00:35:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0c899d35-9586-36cf-8236-c47b3d5da410 | -7.80204 | -46.01964 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cc61c8a9-5e8a-32d7-ac07-417a7db5bf7f | -3.44415 | -43.34216 | 2025-10-05 00:35:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ef63aaa2-aa3c-3d18-bdf6-d3cb98eea589 | -5.00431 | -47.20672 | 2025-10-05 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 33f8f0cd-c057-35a7-9a00-0e6caec73083 | -7.44106 | -47.86215 | 2025-10-05 00:35:00 | TERRA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c3f64504-1d6f-384c-8818-44459c149212 | -7.80016 | -44.5489 | 2025-10-05 00:35:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1f7ef799-5a23-382c-b56a-911574a518a8 | -5.62625 | -44.40456 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7ed8c763-e18b-3201-8b88-14442e4d3054 | -6.70518 | -42.17651 | 2025-10-05 00:35:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 30.5 |
| fcb9bfee-0818-351c-a605-945876fdb827 | -7.72124 | -46.32347 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| ce0db450-2a0c-3ccf-8b6a-f8c49ce31153 | -5.00581 | -47.21708 | 2025-10-05 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| a0796950-bc1a-334b-b8e7-29d4b80b8737 | -3.67892 | -41.7595 | 2025-10-05 00:35:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 71de05cf-e254-3b43-9746-8133da31f77f | -0.91472 | -47.54921 | 2025-10-05 00:35:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 5ffcb027-70d4-3a87-b23c-4ad288aa763d | -6.63366 | -47.75995 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 130df7c4-ecc1-3d99-915f-1d52e53073d6 | -6.0863 | -46.19674 | 2025-10-05 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 584f0e73-92a7-3a1d-927c-71fcffa161c0 | -8.34184 | -49.50315 | 2025-10-05 00:35:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2503a84a-f4dd-3554-ac56-2f608bf45416 | -7.20637 | -46.86216 | 2025-10-05 00:35:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| db9ff88c-8219-3c6e-8708-3c17543185b0 | -6.2339 | -44.38528 | 2025-10-05 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ed3a7fe8-d9b3-3dd9-b525-ed244fd2b081 | -6.63498 | -47.76935 | 2025-10-05 00:35:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ad7a327e-5b5e-3ca8-afc8-3b4815a8b773 | -5.97499 | -44.11694 | 2025-10-05 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d7df03a5-19b4-384d-a139-e1138d83bc49 | -8.54226 | -50.15685 | 2025-10-05 00:35:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f07d3748-1418-3d9d-8fc7-dbbac5fcd752 | -7.31571 | -45.98554 | 2025-10-05 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 9b978847-4043-34ec-b1fd-9b921d272b6e | -5.23027 | -49.06437 | 2025-10-05 00:35:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e25b90a9-c31f-38bc-b35f-d887e108c0dd | 1.00183 | -51.26824 | 2025-10-05 00:35:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca6cffe1-23ed-3bb4-9a54-703a59305d58 | -3.84574 | -44.56655 | 2025-10-05 00:35:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 83f7808e-7c93-3f2d-9dba-f262a3571515 | -6.0151 | -45.41597 | 2025-10-05 00:35:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9527ca7a-1608-3e31-a9fa-a2f3b01190c8 | -8.72746 | -49.48172 | 2025-10-05 00:35:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 23ea2a91-097e-3b5c-9fed-03cbd7db575c | -6.39987 | -47.2899 | 2025-10-05 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 9342252b-ac35-3797-b6ab-011ffe0985be | -5.97739 | -44.13306 | 2025-10-05 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| fffbaba7-634a-31a0-90bb-5c1a12d9199f | -5.98863 | -51.89904 | 2025-10-05 00:35:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9a80dc45-4df0-3de3-ae95-1d020f0b7420 | -6.34486 | -41.62284 | 2025-10-05 00:35:00 | TERRA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 8370f2bb-764b-36b1-b1c3-bb0e63d0d06e | -4.56719 | -48.6024 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 849bb2c9-21a3-3473-937e-f0b8f22a8c70 | -2.69424 | -49.52205 | 2025-10-05 00:35:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1cc2ec3-13f0-3a5f-b677-593e59867afe | -3.08835 | -47.79243 | 2025-10-05 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f1e2a72e-d95a-3b27-98fd-3f54615d4df9 | -4.13786 | -47.6604 | 2025-10-05 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 9e00fa79-9fd5-3555-bc50-34e4d0f7f769 | -4.90938 | -48.01947 | 2025-10-05 00:35:00 | TERRA_M-M | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7912122e-fac8-3ab2-9f2d-865a96e363a4 | -4.65379 | -43.18394 | 2025-10-05 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6b71bbc0-2298-39ea-a973-05022e008779 | -4.24864 | -48.56984 | 2025-10-05 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |


[Clique aqui para ver as próximas entradas](README13.md)
