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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11a56142-848c-3ce1-a7d9-f7dab9a990e5 | -16.88256 | -54.5268 | 2024-10-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40a7c8c4-6f59-38bb-9c3a-c3001ad4a7d9 | -18.19839 | -54.45665 | 2024-10-07 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 929d6272-1f7e-39d5-b3f8-3c97b54b9b2d | -18.9025 | -54.53839 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a30ef70-c1dc-3609-bd75-ed0b7fd55fd2 | -18.89973 | -54.53411 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c607d1c-8e57-3a2e-b2a5-db72afb1a9a1 | -18.89917 | -54.53781 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 978714c6-26ad-3792-8105-a08a6cd35eca | -18.89751 | -54.54881 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 293fd3fc-68e3-3903-bcf8-be3dca356f38 | -18.89696 | -54.55243 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79892479-cd0a-3e52-8e4e-857ae3bdd7bf | -18.89641 | -54.55605 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d98d88ed-6b5f-35fb-b17d-8b2fead28d80 | -18.8964 | -54.53353 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 583df11e-2cbe-3909-875d-93be145e4a47 | -18.89585 | -54.55973 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1cba5ab3-38ca-3aa5-b409-61e45f0606c3 | -18.89584 | -54.53723 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3da2c2d8-4269-30b7-bf4a-1ab1172bdcb5 | -18.89529 | -54.56343 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c8815b27-4a58-3f1b-b584-5e88e52990e2 | -18.89494 | -54.48048 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7bd21927-4a9d-36c2-b99f-9d0788ebd5f0 | -18.89473 | -54.54457 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2035008-8b35-3166-b866-7211c8ce1d28 | -18.89437 | -54.48421 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 886d272c-dc1f-3330-b394-517fd3315b19 | -18.89418 | -54.5482 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82ec07f0-78ee-3c31-88fb-80b5c6675c40 | -18.89381 | -54.48793 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 517f14e1-4f65-30cc-9f81-fc2bbada9331 | -18.89363 | -54.55182 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cf408640-2719-3c05-8566-d113f0fcfcc5 | -18.89308 | -54.55547 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7dca92ba-d91a-3523-aa74-56edf7126d4e | -18.89259 | -54.54082 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dafd3204-c9f3-38a7-a19a-d61e036d0ab4 | -18.89218 | -54.47617 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d215853c-c9ac-356f-84cc-aab3bd8f8506 | -18.89203 | -54.54446 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b06a2beb-f021-3cd8-bf68-a05de2a71728 | -18.89196 | -54.56287 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4ff56bf-1d58-31c6-9213-4f0bdf7990cf | -18.89161 | -54.47989 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d67b1cbf-6e71-3838-b75f-18f675029e29 | -18.89104 | -54.48363 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1352ce93-627c-3301-b908-54d7e809d606 | -18.88924 | -54.56281 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9bb1cf78-642d-389f-8e60-ca0e488ae751 | -18.88885 | -54.47558 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52047abf-5419-341c-abf0-ac4aca595c7b | -18.88867 | -54.56654 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e9e052bd-e435-376d-adf3-0c5788f6993b | -18.88828 | -54.47931 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 825423c9-05a6-3739-8391-17b78d6482a3 | -18.88809 | -54.57029 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e238831f-7309-3216-8f67-12c19782111f | -18.88608 | -54.47128 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc7d2e4a-cdb7-333b-b7d5-39b549b668b5 | -18.88534 | -54.56598 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a1281cc-d94c-3d77-8325-eda4e64f297c | -18.88477 | -54.5697 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6573f536-1f82-3a46-9852-089d1ecea62d | -18.88421 | -54.57339 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4af75cb-8688-3eed-9a99-e38034e4f71c | -18.88201 | -54.56543 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07ea00ca-23a3-311c-9330-a3ae083fecf2 | -18.88088 | -54.57283 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 042c1fa6-57e0-3951-8d71-54350d8ecd9c | -18.87868 | -54.56487 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b28420d8-c144-3657-abc6-9432b4d63b28 | -18.87811 | -54.56857 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2bd985a-07c1-366a-8a80-a1d62bbab058 | -18.87755 | -54.57225 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3ce6873-2b97-3a5a-8548-9f8c41e6ec2f | -18.87591 | -54.56061 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d538648-9c02-38ac-9489-06fd45490e69 | -18.87534 | -54.56432 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5b4afca8-6410-3d77-b508-9880d62062bb | -18.87478 | -54.56799 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 948455ec-31a5-3e25-8858-f9009addd71b | -18.87423 | -54.57166 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9ba20191-0cfc-358e-b2c8-a04c2fc4fd42 | -18.87315 | -54.5563 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 966f3342-e0e0-3d39-aa94-153686316ec8 | -18.87258 | -54.56005 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c16fbdda-6f5d-324f-9dd1-5442f7bf2bb2 | -18.87201 | -54.56377 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e26ac79a-6a78-39b7-8606-c2e3096cae04 | -18.87146 | -54.56742 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8a492ada-7af9-3ff5-a6d7-e5619f5cdd06 | -18.86982 | -54.55573 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b080089-b44f-35ef-b165-7619e7ecdaa3 | -18.86925 | -54.55947 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef90ae1e-04c9-30f8-b67c-2fa2cf67ba16 | -18.86868 | -54.56319 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6ffef1b-6b9e-3f3c-bca8-b117ab61e8bc | -18.86813 | -54.56683 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 664b6625-9dc3-32c5-aac4-dd6d4d7a508e | -18.86649 | -54.55515 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 308a8212-b4d7-3511-b406-c67ee8dcaea7 | -18.86593 | -54.55886 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0193a393-5850-3445-a579-a7f899185bcf | -18.86536 | -54.56256 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23bb2558-00ea-3efb-9a01-aea63604f2de | -18.86316 | -54.55458 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 546c0d6a-be8d-3f05-8202-828a6db1ce78 | -18.86204 | -54.56195 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a5a601f-a166-3f37-a0d0-649209f9d1f5 | -18.8616 | -54.4748 | 2024-10-07 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a452f214-bec0-30fc-8242-a0b684111b5f | -18.86148 | -54.56563 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37b80f83-d893-3fea-b4c9-4413ee98fa43 | -18.85993 | -54.46321 | 2024-10-07 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52b3e4b6-74cd-37c2-bfd2-4cd213cea1d8 | -18.85927 | -54.5577 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a3a9535-ab57-327b-8411-94c9bedfc1ec | -18.85815 | -54.56507 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12bcb577-d151-333f-9727-9564f96f6ba3 | -18.85715 | -54.45896 | 2024-10-07 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5da114bf-e552-3e0b-8a5c-6bc574005347 | -18.85538 | -54.56083 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 166c5d69-6230-3e4a-9d5d-a62d9b9902bc | -18.85482 | -54.56451 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b94c6a6a-efbe-39cc-a918-a75a6ed92c34 | -18.85382 | -54.4584 | 2024-10-07 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b86f31f4-eb26-33b5-a304-b0a9a4f83629 | -18.85149 | -54.56396 | 2024-10-07 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c01d3cd-8eee-3d8c-92e7-82d3bd73e7c1 | -20.87128 | -55.19952 | 2024-10-07 04:55:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c15a5f9-ec3c-3df9-a9fb-d34ac2a7b534 | -20.58349 | -55.74534 | 2024-10-07 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f453ef7c-5064-3e1f-9245-75473c56a8ce | -20.47328 | -55.79744 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4cc06329-84d2-39cc-a656-c3dad5611d2f | -20.02605 | -55.50277 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10c77287-5da0-3480-b9e1-fed451fc38c7 | -19.98042 | -55.46851 | 2024-10-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 17d26a80-2eac-35c2-b867-22192e55e715 | -19.55909 | -55.07002 | 2024-10-07 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66cb9aaf-8bd2-3786-9ef2-a6849b46a828 | -19.55578 | -55.06945 | 2024-10-07 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0010e45-107e-3804-b180-1796fb180cb3 | -19.55246 | -55.06888 | 2024-10-07 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3feb3914-4228-3276-bf93-8298745aabda | -20.78278 | -54.82154 | 2024-10-07 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15ed7a78-aa06-3a4a-abd0-133f5d0dadef | -20.78222 | -54.82527 | 2024-10-07 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d86f90b-4727-39e6-9c59-76db90093541 | -20.77944 | -54.82096 | 2024-10-07 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d04a5ee-d3f8-3b07-89b0-cf909e182d33 | -20.77609 | -54.82039 | 2024-10-07 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e543826-37e4-3fdd-9267-c31488f152a3 | -20.77155 | -54.87331 | 2024-10-07 04:55:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 48c5847e-455f-3397-ab08-c941416edcd2 | -20.25464 | -54.78777 | 2024-10-07 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6a08647b-48e5-3843-bf28-6702321a24f3 | -20.25408 | -54.7915 | 2024-10-07 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 22efa385-98c7-3d2f-9c1d-f248ec2f1698 | -20.07536 | -54.53539 | 2024-10-07 04:55:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62a22bf4-2a31-3b31-bb0a-2665820fcac7 | -20.07201 | -54.5348 | 2024-10-07 04:55:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 434cb381-bcbc-33f5-a5a6-5f70451f8bc1 | -20.07144 | -54.53858 | 2024-10-07 04:55:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7e1db17-ed32-389e-9126-feadeb53c159 | -20.06923 | -54.53041 | 2024-10-07 04:55:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2eed8784-5da2-36b8-bddf-7d9308ab4f95 | -20.06866 | -54.53421 | 2024-10-07 04:55:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8e535db-a697-37b9-bf0d-59e5757a6683 | -21.36313 | -55.69484 | 2024-10-07 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96591891-8ed8-30d5-8388-090653abf0b3 | -21.36256 | -55.69852 | 2024-10-07 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6a29c248-5730-3148-8913-88aa8074882a | -21.34046 | -54.65569 | 2024-10-07 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47fa253d-9258-3822-8f43-f0b583982005 | -21.33766 | -54.65131 | 2024-10-07 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87e44c7c-9de2-38d3-99bc-43f841cdc540 | -21.33709 | -54.65512 | 2024-10-07 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 735dee8b-3b3b-3342-830e-5ef33b3cd06e | -21.33618 | -55.67113 | 2024-10-07 04:55:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afefa67a-60d1-3ac8-8cd1-0ba402fec802 | -21.33494 | -55.70126 | 2024-10-07 04:55:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2526ed24-cecc-3954-8a2e-1e171ae6f371 | -21.33429 | -54.65074 | 2024-10-07 04:55:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6c91c393-264a-30ca-af98-ac9325fcecf3 | -21.33163 | -55.70069 | 2024-10-07 04:55:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66d9bbd4-f9d4-3253-bf0b-b9dbd8200557 | -22.16565 | -54.85764 | 2024-10-07 04:55:00 | NOAA-21 | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99633c33-a9e8-37ed-909e-232eb1a99360 | -21.05639 | -54.68798 | 2024-10-07 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40c588e5-a064-3614-b621-e837c313ef4d | -21.05527 | -54.69556 | 2024-10-07 04:55:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3270c27e-b798-313e-ac7d-4de8b160794d | -16.64344 | -55.22985 | 2024-10-07 04:55:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d5ea365d-2d70-3e17-a6e8-0ea017c202f2 | -16.64168 | -55.56162 | 2024-10-07 04:55:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |


[Clique aqui para ver as próximas entradas](README96.md)
