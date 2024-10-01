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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ffcf904-5c63-39bb-8198-8467eb8cc609 | -18.87284 | -54.50827 | 2024-10-01 05:48:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f9245e65-86e0-36c8-8cb1-7806954ff197 | -18.86388 | -54.5068 | 2024-10-01 05:48:00 | AQUA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2e850eb8-e7ff-35bc-abc9-b82b11017126 | -19.98538 | -55.47767 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5276495a-5536-355d-873e-70b6102044a6 | -19.97534 | -55.47907 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 698c6824-b1b3-32a9-922c-8e7114993eca | -19.97394 | -55.48848 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fa03c59d-ff71-3998-8db1-992e66009d7d | -19.96508 | -55.487 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 44b934ec-c151-3ef1-b5b4-d20da116d048 | -19.96369 | -55.49636 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85897a8d-3afb-32bb-9918-080c87856b85 | -21.69781 | -54.78778 | 2024-10-01 05:48:00 | AQUA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6a57d2c1-7761-3376-9c80-c277b0dda767 | -21.69641 | -54.7977 | 2024-10-01 05:48:00 | AQUA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6afcbc8c-d1e5-37f1-814a-ab827f9ee7c7 | -21.68735 | -54.79628 | 2024-10-01 05:48:00 | AQUA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f48d4e8-1e6b-392e-83ae-91ef9d6dfab4 | -21.6428 | -54.84982 | 2024-10-01 05:48:00 | AQUA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1f187625-441b-3136-afea-85c4bc922413 | -16.63341 | -55.19141 | 2024-10-01 05:48:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3cd0c888-4505-3662-aaac-1de258ecc8b8 | -16.63202 | -55.20061 | 2024-10-01 05:48:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| eeac4830-da6b-3f65-8c90-d4da8324f20d | -16.62454 | -55.19 | 2024-10-01 05:48:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 08788645-0824-3681-aedc-005d931d42e3 | -17.18053 | -56.19476 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.3 |
| d0966b2c-7e7d-38c7-84be-e2b2731110ba | -17.17906 | -56.20428 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 0853cd20-91ed-323f-b4bd-94133d0c046c | -17.17759 | -56.21381 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| 326f8de6-0784-37ef-82e5-7b866663dedc | -17.17741 | -56.15522 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 568bd581-e2ec-3fde-94ca-eb591d356f9f | -17.17594 | -56.16472 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 60cf3c03-d786-3e7d-ba37-70cd0f32e25e | -17.17006 | -56.20279 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| 049d6def-9cb9-3c8f-a9a9-f495adbea195 | -17.16989 | -56.14423 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ea35bc91-125e-3e62-b03c-c033d60efb09 | -17.16858 | -56.21232 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| a743db1d-988e-3b31-935d-c0f72657e233 | -17.16842 | -56.15373 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 06f47cb1-f661-3af5-9d70-17abaef261eb | -17.1671 | -56.22186 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 014b4c10-6552-3d08-a588-e3029d74cc61 | -17.16401 | -56.18225 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| d720a226-591c-3ad0-8edb-19d82999753b | -17.16253 | -56.19178 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 15b6d9f9-d316-32fb-b4db-d3cd347c34bb | -17.16106 | -56.20129 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| bc451491-24e8-35fa-aea8-228f6fc3d5a8 | -17.1609 | -56.14274 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 75.6 |
| 41434724-8c7d-3622-8022-da14bed3614d | -17.15958 | -56.21083 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 22c26641-ec74-3c8b-bcce-cf1357eb8b1c | -17.15796 | -56.16174 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.9 |
| c496275a-208a-3e65-8554-184b030d5147 | -17.15649 | -56.17125 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.0 |
| 5a0cc678-e81a-365e-9f56-1da404eec4fb | -17.15501 | -56.18076 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 90fc9f4b-df3e-3aa8-a1fb-6cb1a848bca7 | -17.15353 | -56.19028 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| 0bb80eb0-89bd-3cb2-8ba4-388d9fbbb254 | -17.15206 | -56.1998 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 15ae965f-6742-3c2b-9abe-a1f1123677b2 | -17.15058 | -56.20934 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| e652cd8d-01b0-35a6-9066-39ada3566be9 | -17.14601 | -56.17927 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| d5fc0a54-6573-361f-9c8d-e6d789f4afbf | -17.14454 | -56.18878 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.1 |
| d27721a5-d2d5-3bd1-9dac-cf75ca557a01 | -17.14305 | -56.19831 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| bb980e06-06b1-35dc-85ca-776a820bfde0 | -17.14157 | -56.20784 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 956a3ae6-64ab-3864-9921-4c57ec7736da | -17.13702 | -56.17778 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| b233b9e3-dd60-3fe0-9553-af75c3797fe2 | -17.13554 | -56.18729 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 0b500173-ff1f-3fb9-8879-8b238516c531 | -17.11745 | -56.12582 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 444394f2-644d-36e3-bebc-547eaaf443d7 | -17.08293 | -56.11346 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 9f8a7f04-01b1-3a27-83ff-1c09d0ccf0d0 | -17.07869 | -56.20054 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c4a9919e-1059-3650-870a-18501b29356d | -17.06408 | -56.70199 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 7e40ab46-c3c6-305c-9ae1-030a140fb4f9 | -17.05745 | -56.09953 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 556b7f8d-6121-3b1a-aad2-ee11c52eabff | -17.05598 | -56.10901 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 219638a0-0662-32f9-b334-2dc5ce15e28d | -17.05492 | -56.70045 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 4f9ad84e-d543-3c56-83c3-bac03ce90fe5 | -17.01404 | -56.07682 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 79c8da13-32b2-3135-a97e-a58b88ec82b0 | -16.96647 | -56.20545 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6e479689-a340-3208-8d09-f6d5f9bb5861 | -16.94092 | -56.19143 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c716456e-73df-3b9a-ba2d-17bac8e515c9 | -16.85607 | -55.90295 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 5d353fcb-1bf5-3c34-a1fa-8cc3ed48a1a1 | -16.85463 | -55.91235 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 64c5d267-84d1-3ba3-b20a-b85e26db633c | -16.83817 | -55.90002 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 293c039a-3107-336a-8085-7dcb01687241 | -16.83673 | -55.90941 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.1 |
| 8c1d6eb5-052b-3654-bb71-e06b2a0b2769 | -16.82777 | -55.90794 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.4 |
| 5bff8974-afa3-342d-980a-484c0c6ed60e | -16.82632 | -55.91735 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 36c3cdbc-7d4e-30a6-ae69-e6b7437c2d68 | -16.80527 | -55.87536 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| dbc1d6c9-f934-3024-ab4e-cd967f749a30 | -16.80382 | -55.88475 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9069c860-6db3-3956-a8ec-cf886afeaf04 | -16.77446 | -55.7773 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4bb640d8-6977-3b22-99f9-9b8bf0da94a2 | -16.77303 | -55.78666 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 6d840cbd-4fb1-3504-8917-2738d9c55dd2 | -16.7716 | -55.79601 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 962c5dd6-ee32-357e-9d66-0848a755f8e4 | -16.76553 | -55.77584 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 29.2 |
| 58148acd-b0e8-3be0-8136-56ebd551d7fb | -16.7641 | -55.78519 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.2 |
| ea8e3eeb-1e44-371e-a227-dff13de97598 | -16.76266 | -55.79455 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 29.5 |
| 453e338f-3952-3e71-bd50-2054e8b9b435 | -16.76122 | -55.80391 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 02c7e5fe-2770-3ba0-a2e6-9ed448265c4d | -16.7566 | -55.77438 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6bdbfb58-833d-311f-9357-0b26af4e8d6a | -16.75516 | -55.78373 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 0c68b5a0-f8a8-36e5-a7cd-aae0211a781d | -16.75373 | -55.79309 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 5c46dcb1-a02a-362a-a5a6-e263185b661b | -16.75229 | -55.80246 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 54d75355-f778-3a88-bec7-e050255f31e7 | -16.74623 | -55.78228 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| dcd71708-7b00-3b9a-ba65-9476f089a56b | -16.74335 | -55.80099 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 73303fce-750b-3094-b889-0f38bd679c30 | -16.74191 | -55.81036 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| b8ee8c82-7661-3e00-bbaf-e65ca2b12651 | -16.72439 | -55.49634 | 2024-10-01 05:48:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7126d41e-b832-3f2e-b3c1-2c83098df25e | -16.65294 | -55.96345 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 074ed924-b319-31ec-a317-064fe2ff39d1 | -16.60367 | -55.98441 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 3ed997f1-cfbc-3b26-b0dd-10e57b38e8bb | -16.60221 | -55.99387 | 2024-10-01 05:48:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a46855a7-26f6-3c0d-b8a3-5cfb06365e26 | -19.65028 | -56.47065 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| c818e258-f163-333c-b796-b1b692b05e1d | -19.6488 | -56.48017 | 2024-10-01 05:48:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d168b79a-5273-3dbc-afbd-65635b78afe4 | -16.89476 | -57.69428 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| ec7d35a1-13d2-3608-b2d8-f5ce175c40df | -16.89297 | -57.70523 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 5115044c-8d2c-3718-a469-5d1f7f3314b0 | -16.89117 | -57.71619 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 378feda2-573d-381d-bb83-372cb3f88bb3 | -16.88155 | -57.71451 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| de9e43b8-8f7d-32a4-a9b0-21d1e43f3f75 | -16.86594 | -57.68927 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 13ecb28a-95ef-3738-830b-871bf7b881e4 | -16.81836 | -57.54035 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| ea4c93b7-3b92-3886-87b1-4576ed6e649c | -16.75774 | -57.7883 | 2024-10-01 05:48:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 133f4e1a-4fa9-3c89-ac95-7dd80d657932 | -16.71041 | -57.36656 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| 5fcd7290-edfd-3a4d-9b25-42e496fc1393 | -16.70872 | -57.37716 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.6 |
| a6abbb8b-ab4f-3be8-bcec-a923b87c8e41 | -16.69925 | -57.37553 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| d78ecff4-0b88-3fc7-a35b-0d1740a7ebad | -16.66305 | -57.23956 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 2a1a4c45-9a59-392e-aaef-8e0550252a5e | -17.09914 | -56.71806 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.4 |
| 3d8c1370-86d3-3dcc-a124-919420b7b8ab | -17.09759 | -56.72794 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| bb32ee02-39f4-32b4-933d-d71fe554581d | -17.08998 | -56.7165 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.4 |
| 3a8eedb9-f6d5-3296-b27e-a154bffe8785 | -17.08843 | -56.72639 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 8358c7cc-9a55-3791-b8d3-50e0e363c415 | -17.08688 | -56.73629 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 6c694442-0e50-39c0-bc1b-2bdb5b84d6a1 | -17.08083 | -56.71496 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 0b00df7d-bba6-351c-b1e2-dff6a5a34b62 | -17.07771 | -56.73473 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.1 |
| b63be410-8ed1-377a-8d5d-545c8ef49256 | -17.07167 | -56.71341 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 2f8f5d3c-9b8d-3ebc-a992-e772506f64ad | -17.06855 | -56.73318 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 6c526e9a-d29e-3e54-bc42-daadf100f654 | -17.06252 | -56.71186 | 2024-10-01 05:48:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |


[Clique aqui para ver as próximas entradas](README154.md)
