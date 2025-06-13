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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcc063fd-0ca4-36e0-b74f-e1d75ba29dbe | -7.45615 | -45.51625 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f94af4cc-b3da-3c09-b25d-b200f924ea3b | -6.94596 | -42.89923 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5d656360-555f-335f-a076-9f7a81138d2d | -5.78189 | -43.61299 | 2025-06-13 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7f3a392-e780-33bf-8ebe-dcf3f06682c8 | -6.95163 | -42.8948 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| cfef7220-23d0-3658-8436-a8d6bb6cb4ad | -5.64125 | -43.59891 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 412bcd57-7810-3536-986a-6199919a81cf | -5.6504 | -43.60666 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 928b29bb-9775-3492-80b1-aea82e3b6e2b | -5.64339 | -43.60697 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5278f521-a79f-3837-b735-99d0edea5e29 | -7.45745 | -45.51887 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 40bbc0d6-b057-3669-a1e7-931faedfa68f | -7.45253 | -45.51407 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 450adbb3-8479-34a7-a1bd-abaa0437708c | -6.94947 | -42.9014 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 11545507-b054-3540-9315-77f52f924019 | -4.89102 | -37.52653 | 2025-06-13 03:42:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d080733c-3871-3975-b3bf-dc35e6f9b115 | -7.46238 | -45.52361 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c450f253-05b7-3802-9534-1ab97d449b87 | -6.94688 | -42.89405 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e8281edf-ae07-3a04-9c99-804e857377ff | -6.11603 | -35.91532 | 2025-06-13 03:42:00 | NOAA-21 | SÍTIO NOVO | RIO GRANDE DO NORTE | Brasil | 2413706 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d573c0b2-f76c-3685-bc19-9c1a596765fd | -7.80456 | -40.55078 | 2025-06-13 03:42:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd0de30e-8c02-3336-bc45-8822456132e2 | -7.46105 | -45.52099 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0d082468-edea-3f50-9ae1-88f7e08b2cca | -5.91652 | -43.46181 | 2025-06-13 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f42a8895-53c0-3d27-a8b0-8bc5523a74a5 | -7.45114 | -45.52187 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| babd2849-afd7-34c7-87df-980ef6a5ffe9 | -7.46307 | -45.51976 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f3acf01-6494-3b0a-a34c-c3b637eed760 | -6.95036 | -42.89617 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a3dee398-74c7-3a0a-9165-37db619211ad | -7.46176 | -45.51713 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8bfa5e7-0b15-3c43-90b6-1e846e6d75c1 | -6.95071 | -42.90001 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1be76778-db20-3390-a755-20e46625976f | -5.64445 | -43.60095 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b38f235-09f3-38d3-b3c8-ff183a4fd8e1 | -5.5012 | -35.58325 | 2025-06-13 03:42:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6bac9e44-76c4-360b-925f-8703c2ef9372 | -7.45542 | -45.52014 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c68ed5db-a4f4-3dd8-b351-8bf76a6b856b | -6.9478 | -42.88892 | 2025-06-13 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| bcb63b68-a909-3fdf-85ce-8f2f685b27ac | -7.45183 | -45.51796 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c8911ace-8541-3387-b458-c8d4b75d8441 | -5.64848 | -43.60783 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7132ca-73ba-39cd-8d5c-20dcaa40a4ff | -7.45814 | -45.51499 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 49c8ad3f-7ad5-3302-acbb-9926ee94d9d1 | -7.46247 | -45.51331 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f94c9b15-abc1-31d1-a1ca-09e0354ae9ec | -5.63883 | -43.60312 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1a50a82d-3aa6-38ed-a85f-9f002b18cc86 | -5.64074 | -43.60192 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24fda5b2-20cf-3fc0-8477-90d8badec7cb | -7.45686 | -45.51239 | 2025-06-13 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8a16ba3-6143-3763-b822-5bedc6dd992e | -5.64023 | -43.60493 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e18ecbb1-5423-3357-a57d-f8eaa100ad16 | -8.0731 | -34.97725 | 2025-06-13 03:42:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00abb39c-7c1a-3307-a7c0-2707e0025bc8 | -8.07636 | -43.11258 | 2025-06-13 03:42:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6279dc59-0df9-369d-8b28-542fedbfc38f | -8.90561 | -38.56606 | 2025-06-13 03:42:00 | NOAA-21 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6a628dad-4225-3ff1-8bce-5219882c8ef0 | -5.64481 | -43.60881 | 2025-06-13 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79ddad9a-78d6-39e1-972c-82c3878a3390 | -12.05569 | -48.07723 | 2025-06-13 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6194417-ba05-3e04-b43b-3aa1a01c1d87 | -8.58822 | -45.86438 | 2025-06-13 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e91d453-0529-3ff2-baf3-5beb92dad352 | -9.84415 | -44.69607 | 2025-06-13 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2294f11a-71cf-36bc-aace-12772e475cda | -12.00394 | -45.13706 | 2025-06-13 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0ae73977-f239-345b-a69b-9b91593eeb7e | -9.66608 | -48.76884 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 487d4fe1-2c42-3a4f-9633-aa0e8958921b | -10.64886 | -49.42326 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b5fcb759-2f02-3551-9612-2f3ad8092500 | -9.39663 | -48.42448 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 588f1460-3e6f-3ac4-a1d3-5bb8870bfe3b | -9.40961 | -48.42689 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3133bfdb-f0fe-3c13-a140-38931e8a0381 | -10.65007 | -49.41732 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f44ca3af-1bff-354a-aca1-2488a7db5040 | -9.41607 | -48.42823 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f6dc656-dbf6-3ff5-98b2-b0dfd4f4ebb3 | -10.69786 | -49.5029 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 53282d2b-51b3-3b57-b500-2b5b1880302a | -9.38969 | -48.42688 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9bced237-cc4c-344e-b2eb-38ed389b5ecb | -8.9565 | -47.27781 | 2025-06-13 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4277abf-ae1b-3f8b-a226-7783605d8ab5 | -9.35998 | -40.41865 | 2025-06-13 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce44f888-db56-36b8-a982-8968bcd1f875 | -14.44917 | -44.86842 | 2025-06-13 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72b35485-3ed6-3c24-afe3-58fe291d49f8 | -9.67171 | -48.76553 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e9941941-aa7b-3813-b4ab-bd74aa74763f | -9.88051 | -37.07801 | 2025-06-13 03:45:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2c5ca00f-7564-3106-be80-71c109412018 | -9.67374 | -48.76456 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a956e960-74c3-3a91-a466-cfa9662ee93d | -11.99948 | -45.13309 | 2025-06-13 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b17f68c7-47ae-386e-9a47-0a24506a76ab | -8.59318 | -45.86904 | 2025-06-13 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb612a48-17a8-3031-9c71-f7b7416bbdb4 | -14.84362 | -48.3116 | 2025-06-13 03:45:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d5a28ed-84e0-3301-ad70-dac587d9b0d1 | -9.84982 | -44.69379 | 2025-06-13 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e8360ff-8022-338a-8267-b5e877e0a810 | -10.70373 | -49.49902 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ca1ce9af-255f-3ab8-ac22-7444d83a3708 | -11.7825 | -47.32199 | 2025-06-13 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6073f6f1-698e-3d20-8969-d48611040bb4 | -12.29202 | -50.10675 | 2025-06-13 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| add84a02-e7b1-31bf-8135-f7e1ee43a1ef | -9.39014 | -48.42328 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 46f383cb-ba20-3b41-9729-4950fbb6b1c9 | -13.1179 | -44.07578 | 2025-06-13 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b85f71a-a93b-3548-b212-781362101d8a | -9.88056 | -46.28091 | 2025-06-13 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8ee6e785-9d16-3998-8627-7cba4a795f6d | -9.88695 | -46.27801 | 2025-06-13 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 363f37fc-58eb-3b70-b742-e1d5bc93f18e | -9.79156 | -36.99458 | 2025-06-13 03:45:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| faf4c5af-5b57-3753-8ee2-6e8f7fb3d25a | -10.6472 | -44.48422 | 2025-06-13 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 48864fc8-dc55-36e0-bb92-1a59fff4a9b0 | -10.70043 | -49.49046 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c8620680-18c7-36c4-9954-aeee184207b5 | -9.84195 | -44.70811 | 2025-06-13 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 22af3981-9c6c-339e-91e2-0a06cb7e4822 | -9.67058 | -48.77114 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fbe099c9-82fb-3589-a7cb-4905ffd4de3c | -8.59091 | -45.86827 | 2025-06-13 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7c2ef62-510b-3fe9-947c-fc05d0940a26 | -11.79947 | -43.79023 | 2025-06-13 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75bfe3a6-b6fa-3930-bba7-5d262ddcacd7 | -12.00508 | -45.13108 | 2025-06-13 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ed4c241b-dbbc-3ffc-8401-3a2ec5faecf5 | -10.64089 | -49.42802 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4cd17239-2a81-3393-9675-da1115bd9eea | -10.65561 | -49.42454 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9c2066d-6343-39e6-ab94-91c9aa6dc142 | -12.28609 | -50.10619 | 2025-06-13 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b08ff24f-2e1f-3bf2-9f37-89441bd0b310 | -15.414 | -44.28677 | 2025-06-13 03:45:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dc25a9dc-6a73-3312-ae3f-846572a1b870 | -12.00451 | -45.13407 | 2025-06-13 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d79f19a2-5ec7-3487-92fd-fc3d8cf50029 | -9.3923 | -48.41241 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 510a21b6-709f-3539-97a5-6fd433072bea | -8.96549 | -47.97194 | 2025-06-13 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 369545c5-3ac6-3e94-bab8-a0230860c9ac | -12.2907 | -50.11313 | 2025-06-13 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6948086-2f29-36b7-ba8e-642c3688846e | -12.1057 | -48.87631 | 2025-06-13 03:45:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15c6f05b-c4a5-3946-bc6f-78413ced003b | -10.6421 | -49.42208 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 34e99bf3-76da-39b0-b21b-57a065ecc3df | -9.78824 | -36.99405 | 2025-06-13 03:45:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e1eddb96-2315-3439-88d4-62658ca3f06b | -11.99891 | -45.13608 | 2025-06-13 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aed7327-ea52-3bfe-a392-1a4d38c30694 | -9.84471 | -44.69299 | 2025-06-13 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2aa1a79f-c98d-3092-aba8-8d0b3638b7bb | -9.40633 | -48.40952 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 151763c1-6327-3663-b412-ed63f5891e17 | -12.10745 | -48.87635 | 2025-06-13 03:45:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dedef741-b416-36c7-bb13-207a5f44a411 | -9.88662 | -47.81199 | 2025-06-13 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 960d3ac9-468d-3f6a-a27d-a299815c0354 | -12.05582 | -48.07975 | 2025-06-13 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ebca9b4-d314-334a-9159-cb0285bf6edb | -8.95676 | -47.27488 | 2025-06-13 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39873874-9a94-324e-82f5-a83e14a3a584 | -12.76878 | -44.41183 | 2025-06-13 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 30b269e9-55c2-3cc0-9676-35c41590e76d | -10.63966 | -49.4341 | 2025-06-13 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c25718d6-0fbc-33fd-9a35-1d44865c3b0b | -9.41669 | -48.42636 | 2025-06-13 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5f00f42-6614-37f6-acbc-c7d53721eb94 | -9.84528 | -44.68989 | 2025-06-13 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aace90c0-dc48-314d-8f54-b082e64250f0 | -8.95591 | -47.27941 | 2025-06-13 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b194c558-41ad-3d8b-b099-3c6ff9e71ec9 | -8.59154 | -45.86488 | 2025-06-13 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 14f14804-3f92-3aa9-a73b-3e7eabde383b | -10.69697 | -49.4977 | 2025-06-13 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README8.md)
