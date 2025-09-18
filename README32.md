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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1265b350-a509-3621-bd09-2c7bbf57818c | -10.4085 | -61.1915 | 2025-09-18 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f36fd7ca-97fb-314d-be9b-3f144c83823a | -12.9068 | -44.658 | 2025-09-18 08:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9d2dd77d-d098-3ab7-af82-9e82328e37ac | -12.9068 | -44.658 | 2025-09-18 08:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 309c45c0-6e03-3e6b-afaf-cb0cfa65f655 | -10.4085 | -61.1915 | 2025-09-18 08:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b70d4011-a98a-352a-b6b7-5bd0e1bfe7ae | -10.4084 | -61.2108 | 2025-09-18 08:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 37a9c9cc-3024-3274-aed8-b7663cc190f9 | -18.4408 | -52.1583 | 2025-09-18 08:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 200.9 |
| 9ba39373-bd97-3245-afc8-6f2fec6eca3e | -18.4213 | -52.1398 | 2025-09-18 08:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| ac358b10-797c-365c-90d9-4e1690692833 | -10.4085 | -61.1915 | 2025-09-18 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 44fee20e-0543-3b3e-867b-156097cc024b | -18.4208 | -52.1617 | 2025-09-18 08:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 125.6 |
| fcb45aa2-67c2-3b3e-998e-e54881f46495 | -18.4413 | -52.1365 | 2025-09-18 08:30:00 | GOES-19 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 159.5 |
| f7b1720e-9c96-39fc-9ff3-0f168de8c4c7 | -10.4084 | -61.2108 | 2025-09-18 08:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f2f4484f-0398-36ed-9a76-9a4348208e8d | -10.4085 | -61.1915 | 2025-09-18 08:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 5eb3d539-cd70-3ee1-9059-2129bbe6d702 | -10.4085 | -61.1915 | 2025-09-18 09:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b54aad38-76bd-3b45-8199-ca37e3425538 | -7.5818 | -44.4971 | 2025-09-18 09:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 284.4 |
| d364bd87-0118-3471-8dfb-129abe3f0bd8 | -7.5816 | -44.5201 | 2025-09-18 09:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 6551f8b7-a574-3989-8f2e-78a790738468 | -7.5818 | -44.4971 | 2025-09-18 10:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 0aee3091-a7c9-3ebb-a731-8bdd75b6f992 | -7.5816 | -44.5201 | 2025-09-18 10:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6175de4b-6867-38e2-8bfb-a15e85fbd30c | -7.5993 | -44.6102 | 2025-09-18 10:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 72505cea-706d-3e8b-97b6-b7cbe2358b78 | -8.6887 | -46.3599 | 2025-09-18 10:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 97fbb7ff-5502-36a6-9595-dae49168c455 | -8.7073 | -46.3804 | 2025-09-18 10:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 1ffb0c3f-c729-33a2-ac7d-569ec340bfec | -8.7076 | -46.3579 | 2025-09-18 10:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 9f181546-69a2-39b7-9b03-9c33cb52ba8a | -8.7076 | -46.3579 | 2025-09-18 10:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0e257a03-2eb6-3096-8b7e-0eb5358ccb3d | -8.7073 | -46.3804 | 2025-09-18 10:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 6165ae88-e73d-31aa-b1ea-16856187447d | -7.5993 | -44.6102 | 2025-09-18 10:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 8dca2850-847a-3bac-a339-d38ed6386c76 | -8.7073 | -46.3804 | 2025-09-18 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 349.5 |
| f315085a-7563-3ab8-b1cc-921503f98619 | -8.7076 | -46.3579 | 2025-09-18 10:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 290.6 |
| 85d29785-b4d5-377f-b224-90c9d93d9842 | -9.01 | -46.3039 | 2025-09-18 10:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| cf41e4ab-c2a3-3e19-be0f-bd9ce632a33e | -9.1898 | -46.9772 | 2025-09-18 10:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 8c15c175-c9ec-3e57-91bd-0335134d06f4 | -8.669 | -46.4291 | 2025-09-18 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| fc7c63a6-d87b-3f26-86e1-555768f32d90 | -9.2087 | -46.9752 | 2025-09-18 10:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 30a719cd-6cad-3a58-81be-0cdfe5d985d7 | -8.6502 | -46.431 | 2025-09-18 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 06fb190b-a48a-379a-a307-a6b434b6ba01 | -9.1898 | -46.9772 | 2025-09-18 10:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 329.7 |
| dfdf6e00-e278-320a-bdaa-312915482761 | -8.7076 | -46.3579 | 2025-09-18 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 485c62be-a5d6-3ba0-8eff-3f91f126c100 | -8.7073 | -46.3804 | 2025-09-18 10:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 291.3 |
| 011e8c4d-b3db-3cb9-a6de-2c220209a432 | -9.01 | -46.3039 | 2025-09-18 10:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a170291d-c172-3b6e-a31b-d451507c605c | -8.6887 | -46.3599 | 2025-09-18 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2727c3f9-52e3-3778-967f-0676b78cfd32 | -8.7076 | -46.3579 | 2025-09-18 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 51c27aef-f2b7-39f3-9109-16c79df91050 | -9.01 | -46.3039 | 2025-09-18 11:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c5402790-6531-3627-bb66-e852f3fb25fa | -8.6502 | -46.431 | 2025-09-18 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 7e9a7624-c771-37c2-9440-c45e0141328e | -8.7073 | -46.3804 | 2025-09-18 11:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 241.7 |
| d89a3c8f-b2fb-37a4-9dc4-05af9c173689 | -8.7073 | -46.3804 | 2025-09-18 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 230.2 |
| bb8c71a0-f7a9-3363-879b-e27db956d296 | -8.9911 | -46.3059 | 2025-09-18 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 55656b9a-296f-3a7e-8a18-e1d6a7907356 | -9.01 | -46.3039 | 2025-09-18 11:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 0219a1bb-8e66-31dc-a347-0e1749a06497 | -7.5598 | -44.7743 | 2025-09-18 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 6da4c22c-f584-3b96-b853-41af77b88165 | -8.7076 | -46.3579 | 2025-09-18 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6450ce38-d45d-304d-a041-d79fceb2f850 | -8.6502 | -46.431 | 2025-09-18 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| c5e3c5aa-6d1c-39eb-9d17-9d4e2576bf93 | -8.6504 | -46.4086 | 2025-09-18 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ea40c3a4-0fc4-32a2-bf4d-48d81771dccc | -8.7073 | -46.3804 | 2025-09-18 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 6dd368f3-a1df-358c-beb1-bf05cc3a8be3 | -9.01 | -46.3039 | 2025-09-18 11:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 70eae2c5-4857-3f72-b312-cde68ccf2717 | -8.6502 | -46.431 | 2025-09-18 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1d7b1407-44d4-3621-8ec4-5b41cd7ba0fc | -8.7076 | -46.3579 | 2025-09-18 11:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8a3e6f4d-72c9-3a31-8235-677d2da50155 | -8.9911 | -46.3059 | 2025-09-18 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 27f89e46-dd62-33ee-b966-b61e451d765e | -9.01 | -46.3039 | 2025-09-18 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 274.0 |
| f62e9b4b-f94a-3400-baf8-92d0fb05f455 | -8.7073 | -46.3804 | 2025-09-18 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 280.9 |
| fd4ba100-9d39-3be4-a6bc-e13c78edb494 | -8.7076 | -46.3579 | 2025-09-18 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.6 |
| a0247be9-10e0-3689-a126-54e72dd5c3bd | -8.34545 | -44.63168 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 27dca9d6-0619-30c6-aff2-17938be794c2 | -6.22284 | -36.70201 | 2025-09-18 11:36:00 | TERRA_M-M | SÃO VICENTE | RIO GRANDE DO NORTE | Brasil | 2413003 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| fc5aaec6-8b58-3bcf-8a7b-9124dd12d549 | -4.94163 | -37.71241 | 2025-09-18 11:36:00 | TERRA_M-M | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5d512197-079f-3740-b203-ece8a430a2a2 | -8.35544 | -44.65924 | 2025-09-18 11:36:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 4de98301-9e89-3fda-981f-334c559792cb | -8.54782 | -42.26932 | 2025-09-18 11:36:00 | TERRA_M-M | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| f11a14cf-1d62-3dac-a1f6-3305c551739b | -5.08628 | -37.60683 | 2025-09-18 11:36:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a8f82152-a3f1-345d-8148-ccb2b0c1af97 | -7.70896 | -37.08063 | 2025-09-18 11:36:00 | TERRA_M-M | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 1aeb94d2-1f77-3189-ab9b-14e01dc394e8 | -8.34152 | -44.65603 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 42e8a110-a5fc-3dc9-b081-362d60f1ccf7 | -8.1146 | -37.58764 | 2025-09-18 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 38b7d2dc-e92b-3663-94e3-d53e9686ef41 | -8.1835 | -37.68594 | 2025-09-18 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b13d471b-d259-3b83-a8a7-89655ea7f166 | -8.34983 | -44.63879 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 18b30660-f5f3-3abf-80e2-8590f9d96c3f | -4.58478 | -38.01291 | 2025-09-18 11:36:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| bd76dfd1-d5d2-3542-8990-ee04bfe67968 | -7.57469 | -44.76806 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 49325f98-71ac-371c-bc79-f6cf698b23be | -7.61281 | -45.19303 | 2025-09-18 11:36:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 41935e6a-d5ac-38f5-91ce-272d3eac3c4e | -7.00539 | -44.61082 | 2025-09-18 11:36:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 79009520-d25f-3559-8eef-52e9ac1234f2 | -4.33934 | -40.73211 | 2025-09-18 11:36:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 88.8 |
| d4b25f71-e89d-3ef1-8f4b-0393d9d706a9 | -6.52334 | -38.063 | 2025-09-18 11:36:00 | TERRA_M-M | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 98b54ac4-6774-342d-92b0-2f509cd62bc7 | -7.51944 | -45.29433 | 2025-09-18 11:36:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d0f17972-185a-31d4-b395-e7b86eab3710 | -6.08251 | -37.73295 | 2025-09-18 11:36:00 | TERRA_M-M | RAFAEL GODEIRO | RIO GRANDE DO NORTE | Brasil | 2410603 | 24 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3f2c3ddd-a424-3ed4-a78a-2e34eceaeccf | -7.56033 | -44.76553 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 66af5f1f-fec5-30d7-8b72-e16920ffd3f6 | -5.63879 | -45.41392 | 2025-09-18 11:36:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 629ebedc-9b95-395b-8a4e-0f57bb50828a | -7.70028 | -37.51525 | 2025-09-18 11:36:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 9100b4c8-84eb-398d-a35f-1d773b9eda8c | -4.45484 | -38.44551 | 2025-09-18 11:36:00 | TERRA_M-M | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5bb938ee-4119-3eb1-bdf6-b92fc7dd1cb1 | -8.34573 | -44.66311 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 48701e44-3394-3700-9126-f9df23e62b80 | -3.2714 | -43.04685 | 2025-09-18 11:36:00 | TERRA_M-M | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| b3821511-eb80-38a3-84ad-b34a191c1a95 | -8.9532 | -37.20282 | 2025-09-18 11:36:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 8814c9c1-04e7-33c7-a0c1-7a9ea4967fb4 | -5.82981 | -39.18713 | 2025-09-18 11:36:00 | TERRA_M-M | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 95.1 |
| 468a2957-45dd-3f02-b938-f02f5a64bb8d | -6.94612 | -41.30346 | 2025-09-18 11:36:00 | TERRA_M-M | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| eda5c8b5-8ff7-3645-a028-368138e88421 | -5.97688 | -35.45521 | 2025-09-18 11:36:00 | TERRA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 43e7332b-8873-3a31-985d-db75c8b6c44b | -3.79604 | -44.12152 | 2025-09-18 11:36:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 7a723a72-e0a7-3deb-8828-81e72b7a08be | -6.58057 | -37.86034 | 2025-09-18 11:36:00 | TERRA_M-M | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 18.0 |
| ebea922b-de8d-3ee4-b1fb-46fb5d9ee6b8 | -8.95448 | -37.19394 | 2025-09-18 11:36:00 | TERRA_M-M | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 27.5 |
| 3135d524-e9c4-305e-8753-b40a396fb5e4 | -7.52103 | -45.28879 | 2025-09-18 11:36:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| dec8fba0-9e75-37d7-9ae4-0ebb1d3d4682 | -4.14174 | -41.43891 | 2025-09-18 11:36:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| a0a32f07-8b66-3cdb-b332-37ae9a4ea54b | -7.59962 | -44.61367 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 540c229d-c796-3eec-a3ef-b8e6b266d908 | -8.18219 | -37.69491 | 2025-09-18 11:36:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 4.8 |
| abe5298f-b297-301a-93aa-24a622358134 | -4.33743 | -40.74485 | 2025-09-18 11:36:00 | TERRA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 58.4 |
| c346cf3c-8628-3783-af1a-c45c37e903c7 | -7.58382 | -44.50172 | 2025-09-18 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 897b0145-6851-34e3-9677-a90a02700dd5 | -7.00337 | -44.60393 | 2025-09-18 11:36:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a295404a-011d-3678-835a-0259d7c0967a | -4.13003 | -41.43714 | 2025-09-18 11:36:00 | TERRA_M-M | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 7ce289ea-5abe-38cf-933b-43a611e31891 | -9.20227 | -47.0007 | 2025-09-18 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 271.9 |
| 00be01d5-c9e1-333a-834a-58f1ffc74ca2 | -8.95818 | -45.01764 | 2025-09-18 11:38:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 6833c1f1-bbb6-3ee5-8b45-1f0db320ee0e | -12.96088 | -42.49482 | 2025-09-18 11:38:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| e3628757-f97e-3606-914d-eefaf5511857 | -9.1921 | -46.96125 | 2025-09-18 11:38:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 051def60-0809-371b-9c24-a8147b2ffa23 | -14.16333 | -42.04713 | 2025-09-18 11:38:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 34.0 |


[Clique aqui para ver as próximas entradas](README33.md)
