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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e452f203-d786-3fe5-81e4-c21560e8624f | -20.86451 | -56.90045 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c17e9d0f-e66f-3dc5-9d54-3dfc7900164b | -20.88004 | -54.97816 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f8def691-3141-3941-9ab0-91f258ad35a3 | -20.85579 | -56.93751 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e02ba0a8-8086-3ec3-92b3-34127766b347 | -20.83157 | -57.73463 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 536a2943-28ac-3819-b115-4f7c5460588d | -20.86562 | -54.98094 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8da9ae05-02c8-312e-ace8-cebeff16b3ff | -20.8708 | -56.91701 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4cebe5e-ade1-3d31-b9a5-802957b01510 | -20.54983 | -54.5815 | 2025-08-19 05:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4ba6198-a221-3cfb-aa29-7d36b3010075 | -23.99228 | -48.56738 | 2025-08-19 05:21:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4e4b0f85-27fb-3bd1-ba46-b04466337d02 | -20.86266 | -56.91543 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e1a60c4-ef3a-37e0-8774-af33c2ec6c49 | -20.86963 | -54.98718 | 2025-08-19 05:21:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 846b3526-a00d-3043-8eca-47038a4c8d07 | -20.84175 | -56.9163 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6092c77a-cc89-32ca-ad74-4e4694765718 | -20.84221 | -56.91248 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c89df509-6581-317b-bc4c-85f5027c9a88 | -20.29391 | -50.96 | 2025-08-19 05:21:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c709a950-897d-3b2c-b1d0-68ccfd832026 | -23.57922 | -51.63219 | 2025-08-19 05:21:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 8c722a4c-55e0-3110-94be-ccd79b6d8cba | -20.85532 | -56.94131 | 2025-08-19 05:21:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc5524ea-b3c8-380b-a45f-5b5b3c7783fc | -6.95097 | -43.57829 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 638a74a4-d2dd-3536-8ccb-81f0ff8d5ee2 | -6.93769 | -43.58405 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1323dd53-fbc6-3a37-b1a6-2b9ec3e9ea69 | -6.94648 | -43.60014 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| d2f227d1-3fde-38db-9105-993c94ca3569 | -6.93995 | -43.57662 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| f922b15f-6dc4-3fd5-8ec8-7300f96691e0 | -6.92666 | -43.58232 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3c3126a9-ca41-33a0-8693-68e444ec3fc1 | -6.93525 | -43.60517 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0f42e753-27db-31f2-a4ff-e14895c6b078 | -6.92441 | -43.59656 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 22871b52-115e-33ee-9e29-88969dcc9420 | -6.93761 | -43.5908 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| d343093a-ab5a-3c9e-973a-6274261bac61 | -3.98011 | -42.52162 | 2025-08-19 05:23:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 027ff53f-e1c7-30ca-ae58-c5f0cf6054d0 | -5.78026 | -43.61165 | 2025-08-19 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 89a0209f-7631-3426-b9f0-60a2983bea77 | -6.94629 | -43.60695 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2c8955a5-af59-34dd-9257-fd0b58b08dab | -6.94873 | -43.58574 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 58dd01d1-4c74-3fe8-8acc-d4a362a8540b | -6.94424 | -43.61452 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| b5401f06-1d53-3899-a820-31fb05f0ce6e | -4.59412 | -43.30841 | 2025-08-19 05:23:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7a3cfa2e-a4eb-3fcb-8da1-d33f83064cac | -3.97734 | -42.51419 | 2025-08-19 05:23:00 | AQUA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 76f8182f-3473-3d33-8a4f-ab3957b48724 | -6.74331 | -41.5419 | 2025-08-19 05:23:00 | AQUA_M-M | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 9b7d9f1d-d8f4-3aae-8464-7adf7fb28dab | -7.58049 | -45.42454 | 2025-08-19 05:23:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| dbba4f7c-f262-3147-8e9e-8db65af3ce12 | -6.93287 | -43.61964 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cdc66094-cecf-3f9a-a41d-fe431a19afe2 | -5.78261 | -43.5969 | 2025-08-19 05:23:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| b169e322-9d4f-33bc-bc24-ac1cc11a5b4c | -6.94864 | -43.59254 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0f66b9f8-faae-34e2-b7a2-028d4f1ca900 | -6.95967 | -43.59428 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a325fc8a-fff3-3876-b1d0-048488771d84 | -6.93318 | -43.61283 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 07107fb1-b799-3a26-9cac-cb8e3e4e4397 | -7.29145 | -43.68732 | 2025-08-19 05:23:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| fe176a42-d32a-3d05-b088-5d624a0d243d | -6.96199 | -43.58003 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.2 |
| c9ddef0d-3423-3377-8706-a398dad57396 | -6.93545 | -43.59832 | 2025-08-19 05:23:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| ff090614-6446-328a-bfa0-cb7897b5b1e4 | -12.99164 | -45.18945 | 2025-08-19 05:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 0fcb1a38-ce28-3720-82e1-353136b4ac9e | -21.39768 | -45.0097 | 2025-08-19 05:25:00 | AQUA_M-M | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.8 |
| 67bb8a52-0b65-3ac1-a5d4-7cffcb31b732 | -12.04235 | -44.00555 | 2025-08-19 05:25:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ab13680-7674-30b5-bb01-e246edaf7df1 | -21.39955 | -44.99843 | 2025-08-19 05:25:00 | AQUA_M-M | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| eb87431f-e609-3e9e-80cc-337164fc1c93 | -14.86764 | -48.04498 | 2025-08-19 05:25:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| f3866c0c-d7c1-3f78-87cc-078012f454d7 | -12.98907 | -45.20449 | 2025-08-19 05:25:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 89df7c06-7487-310d-a7bf-03afa80d07e3 | -23.57527 | -51.62422 | 2025-08-19 05:27:00 | AQUA_M-M | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| b95d573d-6d74-38f4-8118-5e21a77f634b | -6.9524 | -43.6083 | 2025-08-19 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 3a5a6e16-6572-370b-a073-76d5c3dea8bd | -6.9527 | -43.585 | 2025-08-19 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d1d8d356-247f-3532-ab79-7e93b955ca4c | -6.9339 | -43.5868 | 2025-08-19 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 15d812ab-2681-3ae2-8411-028f746247a5 | -6.9712 | -43.6066 | 2025-08-19 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| f3df838a-88ce-38ef-a8bf-1f515ec9675f | -6.9336 | -43.6101 | 2025-08-19 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| eb331ce0-7b9f-30be-a9de-be3efbf203fb | -6.9715 | -43.5833 | 2025-08-19 05:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 3218e190-cc60-349c-b72c-44d60adffa2f | -6.9524 | -43.6083 | 2025-08-19 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e62f5709-690b-3aa9-8048-27f972d1e13e | -13.1555 | -54.9357 | 2025-08-19 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| b07288c1-13c0-30e3-a59d-a11e2ec3da16 | -6.9339 | -43.5868 | 2025-08-19 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| d67b6a2b-154c-3d3f-8bd7-c63aace4cd88 | -5.7887 | -43.6134 | 2025-08-19 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 38e8a00f-47d5-32bb-beb0-365d9f8a80b2 | -6.9336 | -43.6101 | 2025-08-19 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| da9edb10-1f90-3541-938f-c9f096dd4f7c | -6.9527 | -43.585 | 2025-08-19 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d1710750-e898-3ef9-bbd7-78086b6133f8 | -6.9712 | -43.6066 | 2025-08-19 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7b741629-d2f0-3944-9d8e-c5a2fcb7c95b | -6.9715 | -43.5833 | 2025-08-19 05:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| d0f00038-e154-3aa5-830f-4ac7ae8cbc09 | -13.3537 | -54.4213 | 2025-08-19 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7f2cbc8f-00d9-35c7-b390-2647152d4520 | -13.3346 | -54.4233 | 2025-08-19 05:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 563483c4-787e-39bd-b1c4-7de438b00758 | -6.9339 | -43.5868 | 2025-08-19 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 5f51dbca-d71b-3812-850e-ed40cc3ba8eb | -6.9527 | -43.585 | 2025-08-19 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| f1249c61-fc00-39e7-b2be-514d4eac451f | -6.9715 | -43.5833 | 2025-08-19 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 98ed13af-e37f-3cf2-b11d-bddaa980f727 | -6.9336 | -43.6101 | 2025-08-19 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4fc7ff1a-b80f-3119-93a2-68eda53a7843 | -6.9524 | -43.6083 | 2025-08-19 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 9ba27623-2249-3a2d-9b46-f88e17e02b30 | -6.9712 | -43.6066 | 2025-08-19 05:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| c51c173b-ed36-3240-88e6-f286283bdcfa | -13.3537 | -54.4213 | 2025-08-19 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 054b9dc5-6a7b-33c2-96dc-52afa4d1dec3 | -6.9527 | -43.585 | 2025-08-19 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 34c5726d-224e-3089-96ed-f5705614d26e | -6.9339 | -43.5868 | 2025-08-19 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 996b1c86-f721-3f80-b628-116fecb8f52a | -13.354 | -54.4006 | 2025-08-19 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 8175386c-3db7-33d6-af91-0164803885e5 | -13.3346 | -54.4233 | 2025-08-19 06:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a19931bb-4e23-3a77-8542-b72bca162d68 | -13.1555 | -54.9357 | 2025-08-19 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5288f8da-62f8-3015-8560-ff415abda99d | -6.9524 | -43.6083 | 2025-08-19 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f7b07cf7-bf58-39ba-9091-7605a96b51b8 | -6.9712 | -43.6066 | 2025-08-19 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a8df72fd-76e4-3095-bda7-4ab915522852 | -6.9336 | -43.6101 | 2025-08-19 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| fc2f7033-022e-3259-88c0-d7e1147a9bca | -6.9715 | -43.5833 | 2025-08-19 06:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| d4d8b2bb-115a-3704-b86d-0bf56ddf50b7 | -10.04097 | -59.35652 | 2025-08-19 06:08:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6fa691bd-b350-3444-bf8c-85bb93851068 | -9.202 | -59.63358 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f52d6abc-4131-3e54-b205-54c1b656a36c | -9.48293 | -63.5145 | 2025-08-19 06:08:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b557932d-555b-3f1b-8f9e-fec3032f3d60 | -8.6235 | -62.62719 | 2025-08-19 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cac826c-9d53-3e20-8ec4-fa78a5e3df48 | -8.37302 | -70.13978 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afa13574-5e75-3d8c-98b7-0854cb3b056b | -11.08817 | -58.94386 | 2025-08-19 06:08:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea0d0ae1-be3c-3aa0-9694-87a9c0c1d90e | -7.79395 | -66.96156 | 2025-08-19 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba4dd664-6f61-3595-b475-9654482b7f71 | -8.88325 | -62.397 | 2025-08-19 06:08:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b880ae4-50a2-3967-bc54-ca2c41de432e | -9.18987 | -59.64989 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb22310a-e79c-36dc-8b58-6a2eeb6836cf | -8.73816 | -69.70982 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e77a47e4-f109-3e1f-9bf6-5f4042c1e903 | -8.64096 | -67.2656 | 2025-08-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e572726f-0334-3ea7-ae6e-be3dbab2939f | -8.6324 | -67.26797 | 2025-08-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be47a3a-30db-3181-8934-bb901304b1e4 | -9.89208 | -64.26337 | 2025-08-19 06:08:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9211ddb0-7cac-31ee-9cd0-5c0981a355c0 | -9.53888 | -63.57848 | 2025-08-19 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3d4ce5f-466d-31f4-b0a0-03f74773991b | -8.97388 | -69.3836 | 2025-08-19 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a394d74-22ae-3f6a-b28b-cabf5168e0e2 | -8.63644 | -67.26855 | 2025-08-19 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd2ac50e-2724-3d9e-9d34-26df677e3158 | -8.61797 | -62.62645 | 2025-08-19 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7b972cd-85b6-35d8-9009-4a5eed00414b | -9.1981 | -59.63858 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 992799c1-d097-3558-ab23-9eac3a9b9174 | -7.40024 | -70.08382 | 2025-08-19 06:08:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 937c9741-3b3a-3424-9504-2a5f0c938196 | -8.36958 | -70.13925 | 2025-08-19 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c30dd0a-e5af-340a-84fa-7379b9866590 | -9.19528 | -59.63267 | 2025-08-19 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README54.md)
