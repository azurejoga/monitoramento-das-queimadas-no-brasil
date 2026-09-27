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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 121ae360-69c9-325e-bbae-968be7cba22b | -8.33888 | -44.18068 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b48b121-743f-3ee1-9e58-7e0127db70ec | -8.35178 | -44.17463 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 26f28eeb-9c39-3009-9b59-05cc2d7ae7a6 | -7.33525 | -42.08749 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b78e2a8b-fdb3-38d2-9b73-42aa3aade765 | -5.50199 | -45.51636 | 2026-09-27 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa9e035e-9b43-3617-9690-4a3a6067dcea | -7.33578 | -42.08454 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b35aa27-0a90-34ac-acd6-8b8bcdebef77 | -8.35963 | -44.16409 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 07a43417-79a5-302c-b163-a80ed63ce12e | -6.83628 | -43.51674 | 2026-09-27 03:47:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df356544-ef72-3b1a-9957-f49e5d40907d | -5.73718 | -43.27848 | 2026-09-27 03:47:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83307861-79f7-3307-9b06-6a74f9b86f4e | -8.35674 | -44.17954 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 8f99b91d-e71d-3223-b928-f61d239f94b3 | -7.36539 | -42.12295 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6649a989-cf29-3b8f-a4b3-cc843fc83401 | -8.34828 | -44.16193 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a36d9cd1-4ca5-312d-bd96-18a6314f32f1 | -8.34333 | -44.15701 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13428100-23d3-3401-88d9-8e6e06fd7545 | -7.36485 | -42.12597 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7bcf2fbe-86bd-3697-8835-e65ece460039 | -8.3446 | -44.18154 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4ea2b778-5298-3561-b381-ba5f3af13ffb | -6.31372 | -43.34171 | 2026-09-27 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89b1fdc1-00f1-3f7d-a49f-b1385f9847e1 | -8.35819 | -44.1718 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| c9f157d9-7473-312f-80d0-3f47ebee8f68 | -6.92727 | -41.61237 | 2026-09-27 03:47:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71bafc5f-4c16-3532-8fad-4cc5894f2cf4 | -5.42737 | -43.44357 | 2026-09-27 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5792e4ac-ea2e-34e8-9d7c-15ba85b3c766 | -5.74426 | -45.06135 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fb055c5-b54d-371d-9343-83d8b9609158 | -5.75464 | -45.29391 | 2026-09-27 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6669287e-4926-3a61-a42a-cc036923346c | -7.29105 | -43.30506 | 2026-09-27 03:47:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a05a039-1507-3b47-9414-7c9ab4c4b57e | -7.37405 | -42.10332 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 385da9b3-16c8-3358-9c68-aa723ba0dfac | -7.34134 | -42.0825 | 2026-09-27 03:47:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7febe3ce-c20f-35df-bf99-8f1bd9ae2e6f | -8.34973 | -44.15417 | 2026-09-27 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8531c1e-846c-322b-92d8-4afe1ca829fe | -14.11982 | -46.33983 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1268c65-5f3c-36a7-a24e-9e67c3f4ae6d | -14.12228 | -46.33977 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 399d7631-0ab2-3b0f-a4de-16e759cd6f86 | -12.56813 | -44.13952 | 2026-09-27 03:49:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0275f32-9867-329f-b0af-c893b3172e43 | -5.10157 | -38.10239 | 2026-09-27 03:49:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d7cb75e6-9a47-3590-afbb-6e0849d3b5eb | -15.60475 | -41.35435 | 2026-09-27 03:49:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1b167d01-c824-3360-9600-fc2fa412382f | -12.70701 | -47.32027 | 2026-09-27 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cd7195b-e5fc-3e5b-86b2-1410b1e6dc0c | -3.90851 | -43.01984 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4106fbc-ff8f-3120-bc61-01a692b7a3b5 | -3.91811 | -43.02337 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4f5e0881-c5f1-3bf6-9d28-a6bb08b74000 | -14.39796 | -43.78026 | 2026-09-27 03:49:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44b00208-413e-30d0-86f6-caf92a0c381e | -14.79939 | -45.95641 | 2026-09-27 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abbeaa56-f7a2-3706-97c7-85be63838133 | -12.70065 | -47.31876 | 2026-09-27 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5623fbc3-f86b-3d85-ae5a-00d1a524e647 | -12.66124 | -47.31583 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ab36e5e-80e7-3405-87ae-7fd4b0d6a5fe | -12.96778 | -42.41486 | 2026-09-27 03:49:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb666731-4efd-348d-9dbe-579d23a37785 | -14.80422 | -45.96165 | 2026-09-27 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9721ac4b-c18e-3d26-a5a1-d4ba38ce6672 | -12.17717 | -47.38652 | 2026-09-27 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d852d1ca-fc6f-3b5c-ab90-b46366a272a2 | -14.11671 | -46.32555 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d8b6b4e-d8f0-3fe1-9c25-d8920911be14 | -12.56875 | -44.13632 | 2026-09-27 03:49:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44655833-b935-3903-911a-2ddb23b2499d | -15.33712 | -42.90888 | 2026-09-27 03:49:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a0f6e9f-9878-3d51-80a9-6e914e73377b | -16.79811 | -39.4156 | 2026-09-27 03:49:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbd263f3-a206-3f5c-b17e-a473f8a3d536 | -13.4387 | -43.82246 | 2026-09-27 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0413a264-b178-37d2-9af5-aef27744d355 | -12.1775 | -47.38251 | 2026-09-27 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75cb6747-a365-3760-a46c-3364be2c4535 | -13.21558 | -42.22571 | 2026-09-27 03:49:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| c4aaac9d-9e65-3a42-a1d5-d5f868840684 | -5.65035 | -35.34938 | 2026-09-27 03:49:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1dff8666-e4bc-35c1-9c9b-9a5fc3b3c1ad | -2.91321 | -45.42604 | 2026-09-27 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7cb9edf-8897-3731-a16d-a6536d74f438 | -12.66078 | -47.31384 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7b14e007-ea2b-35ff-babd-e3b637ca07c8 | -3.91876 | -43.01947 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab3fe427-f2e5-34a4-8b9b-6485ee34bd03 | -4.56248 | -44.08105 | 2026-09-27 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ce361bc-41fe-3723-ab3a-6e74cefba94a | -12.18396 | -47.38393 | 2026-09-27 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97b2acd2-8b56-3306-9d2d-6be173114d58 | -14.72416 | -45.58108 | 2026-09-27 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c68242c-c923-375e-920a-4073c518ba6d | -14.79856 | -45.96041 | 2026-09-27 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0825dfc8-6e0f-33c6-99a9-c1546db65cba | -14.11646 | -46.33823 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b62ef1db-c345-3d8a-b03f-5df104cf7622 | -14.79372 | -45.95521 | 2026-09-27 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28f31300-2f51-3c43-b290-a8f14a7a24eb | -12.7145 | -47.31627 | 2026-09-27 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 70ed828c-13ea-30a9-9432-729c6a491318 | -14.78889 | -45.94997 | 2026-09-27 03:49:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8843fde2-dd7b-37b8-9a46-60529d59ab4a | -14.11821 | -46.32965 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28e11c0c-8627-303d-a9a6-7db919c3896f | -10.9332 | -43.75315 | 2026-09-27 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2da9ffc-407e-345a-be02-0ee17b9d0d4a | -15.47812 | -46.15025 | 2026-09-27 03:49:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a393c9a-9601-303c-b81b-aad747c24a52 | -13.85333 | -43.99542 | 2026-09-27 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbc3f262-1cc6-3f43-9aad-2d8ef96ea2f1 | -13.21106 | -42.22448 | 2026-09-27 03:49:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 8871ee10-4172-303c-9e52-8815f98e9824 | -12.68052 | -47.31937 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b10daed5-2731-33f1-8349-34885eabfe51 | -3.9135 | -43.02471 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ed15be6d-c99d-3cef-b6e6-99d0f58126f7 | -13.8552 | -43.9959 | 2026-09-27 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37934454-cb99-350e-85a3-30d3f35b5cc7 | -12.71336 | -47.32176 | 2026-09-27 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 400eef9d-d8a2-3481-91d1-4ba6d447bd37 | -4.27928 | -44.59424 | 2026-09-27 03:49:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe061c2e-87c9-3129-be84-1b624b1dd741 | -12.97021 | -42.41706 | 2026-09-27 03:49:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 756e0780-449b-340b-904d-2a4a46f554a1 | -15.33251 | -42.90792 | 2026-09-27 03:49:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33b130a1-d78a-3d50-9b49-babd82545ce4 | -12.47102 | -47.48338 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| adfb97f4-529a-382e-9503-6b1d1742d64b | -2.90652 | -45.42485 | 2026-09-27 03:49:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36ffb820-72dd-3a05-a110-645d2a3f7c9a | -16.49758 | -43.53305 | 2026-09-27 03:49:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f618e1f-8592-3693-bfc4-ee8a7940babc | -16.59006 | -41.84193 | 2026-09-27 03:49:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 65decfa0-d4a6-3b55-ac42-de9dd1c723ed | -3.91418 | -43.02084 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0c35270-4f25-3efe-a406-7dea31b2f5ea | -13.0933 | -47.39848 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df5fa517-3b8a-30b2-b320-af040a6686eb | -5.50993 | -38.00508 | 2026-09-27 03:49:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d986eb5c-6769-333d-8255-66d2862e25a8 | -14.06557 | -41.93643 | 2026-09-27 03:49:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d997e075-5aa5-32f3-bc90-15c2365bdb67 | -3.91243 | -43.02235 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd43ef80-b827-3964-9458-aea3f44e0724 | -13.21229 | -42.22224 | 2026-09-27 03:49:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 20.2 |
| e1331f07-129a-3e1a-9061-c5709bbea384 | -15.60546 | -41.35047 | 2026-09-27 03:49:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c6d1220f-5cdf-3de9-b6f4-e4398179d5bb | -15.45757 | -39.54665 | 2026-09-27 03:49:00 | NPP-375D | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a7058601-9802-3160-a441-46f6c3b4bc11 | -14.95612 | -47.53812 | 2026-09-27 03:49:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74f0159c-2553-3382-98bc-a9a1d09044f5 | -12.66237 | -47.31042 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8eadab20-baca-322e-8890-3fb82612bcf2 | -14.11907 | -46.32543 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e02155b-408d-3259-8844-3206d95469a3 | -13.09106 | -47.40913 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85b95320-687d-3a57-8e73-1b3f34378c90 | -12.68797 | -47.3156 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a14427d-66a5-3709-b3d3-4e87fe952d95 | -5.27621 | -40.59335 | 2026-09-27 03:49:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 74e19e78-97dc-3c26-832f-3c03bcd54186 | -12.17831 | -47.38094 | 2026-09-27 03:49:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 483e82a9-10b0-3742-a2ec-a9e010f17fcd | -14.12072 | -46.33561 | 2026-09-27 03:49:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 299adfaa-ee42-32f8-a4a0-3b4cc64bedc7 | -3.91308 | -43.01847 | 2026-09-27 03:49:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9f42fd0-3252-3164-bd86-55bdf9a77046 | -15.42387 | -47.90969 | 2026-09-27 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 543b6690-d2c3-38ea-8f2d-7077505e8f51 | -12.47269 | -47.48046 | 2026-09-27 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 599f3294-d883-3b98-8f9f-c77ec1c6d1aa | -16.78038 | -39.43048 | 2026-09-27 03:49:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cae8acb4-a7df-3227-9ae7-1c8d95b4845c | -5.50751 | -38.00264 | 2026-09-27 03:49:00 | NPP-375D | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b52e3607-95f6-35c8-adc3-11cd192d33fe | -13.43929 | -43.81937 | 2026-09-27 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 978c715a-cae0-383e-b934-986317aeedc8 | -15.47726 | -46.1545 | 2026-09-27 03:49:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d92e899-522a-3834-9746-edce3f6bb734 | -9.31408 | -47.63355 | 2026-09-27 03:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1c36189-aaa2-34bf-b83c-4b7482640107 | -13.70552 | -43.66441 | 2026-09-27 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e906157-c76a-3f2d-b54b-718581d3e9b4 | -15.4176 | -47.90817 | 2026-09-27 03:49:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README12.md)
