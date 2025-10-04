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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1cfb18f-72cc-3b97-8900-750150ede399 | -11.31505 | -47.83503 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8a1d86a-855d-3b96-9a6e-4bf748b50f54 | -13.74831 | -48.07768 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87812244-7bcd-39d2-ae48-9eb314fb1555 | -13.3412 | -48.07452 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d45fef8-2fe6-381a-8440-4865beb51e3e | -13.98338 | -48.19596 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3a2e4f4b-5283-3c5f-9620-f05bdf837b41 | -13.52167 | -47.27871 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a0042e26-29da-391e-afcd-4319bd132cd9 | -11.11414 | -47.90097 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15b89f5b-58fb-352c-b9a0-82c5e4e4eeb0 | -12.79228 | -56.9632 | 2025-10-04 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6151062d-f64f-3b32-860c-5707ef5f4363 | -14.93581 | -49.97005 | 2025-10-04 05:06:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3785a1d3-d475-3a5d-a017-7a31fd01a3bb | -12.92063 | -54.73394 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 505eca81-5165-337e-acb9-f4e8513e4259 | -13.74088 | -48.09402 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8fd106f6-8afd-3268-9f68-61aee569f959 | -12.38971 | -54.45689 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| abef4184-89c6-3916-a035-823ffe116f68 | -10.57654 | -48.69427 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3467327e-fd5e-3c37-8a87-9db2495b0ab0 | -11.92199 | -46.3854 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 99a02e1e-504b-3cfe-867e-a99c1df274ba | -15.58035 | -52.47293 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d0a0a90-e4b6-32d0-89d2-0700b921f63e | -15.7341 | -46.27968 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 007a2523-95b9-3ba9-aa53-3ad33cbaa56c | -14.75271 | -48.13939 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| faad99f1-e2a0-33f5-a54b-1ac66bbc9430 | -14.87117 | -48.13057 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc59076c-85c7-3def-98d0-b1484429ad0a | -13.75252 | -48.06458 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 469022f3-d6d0-3557-8c33-0f8529d9eae0 | -16.75675 | -43.96207 | 2025-10-04 05:06:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 544f3728-42bf-3825-8978-553369d0f445 | -12.30174 | -55.13185 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5429219e-db7f-3919-afe7-7536004fb488 | -12.70912 | -48.57285 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 87d38106-c036-3902-95a6-94116034c18b | -14.45639 | -48.40192 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ab72080-40b7-37e4-bf36-59667ad9f0cd | -16.02164 | -50.94506 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3ae095c6-d879-3576-b663-ec78a7b004db | -13.50825 | -47.2678 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28b4f181-f0b3-3659-b4a6-036772590584 | -13.13572 | -47.93732 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f9ba933-1909-393c-aa9c-dc3960767e8f | -15.36733 | -47.95534 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cda1fdc-1413-3158-8e49-c462c341e35d | -11.25032 | -47.7931 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dad415d-6a3a-3885-aaba-a9bb5b733ebe | -12.94281 | -54.72913 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 63e1453d-43c2-31ec-85bf-1c62e87ca109 | -12.28692 | -55.13726 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c38a46-22f0-3455-ac3d-e75f811f90c9 | -12.5826 | -48.12758 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85671102-8340-3951-b737-2f3eb8a0258b | -11.54481 | -47.66703 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b05c3485-b4ee-3c9b-90a3-d36b3376934f | -10.59629 | -54.34717 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6f57ffe2-6db3-376a-a3c4-d1c47cf3ea1a | -15.22232 | -56.81313 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 438aa585-a001-36af-88d7-108319ee8661 | -14.8923 | -48.2801 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a86ccc8-9169-33f0-b9ef-c6d4b5656723 | -14.66659 | -48.24597 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cc0f91e-84a9-3f63-a365-557696163236 | -13.51313 | -47.27504 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c64c247-9068-3cb1-911b-a518482aa1a7 | -12.83339 | -43.80529 | 2025-10-04 05:06:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7bf63cbe-be4b-36e9-ba2b-b86bf472bbac | -14.87074 | -48.13433 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c39d4e1-8089-393a-a87b-f4f98e094ae0 | -15.59882 | -52.4919 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76a0a67a-ad39-3b5b-a7a8-4efdde8d0cf3 | -13.31639 | -48.11703 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f544b623-3e59-3379-990e-7206a11f0f55 | -11.17048 | -47.74987 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ba4cd75-b63d-32b9-9bc6-4197a004131d | -9.99881 | -60.01539 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 73b12dfb-4a35-3d9b-a680-e009d5fecf18 | -11.49469 | -46.75277 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af5eed3e-48d1-33f7-bf11-c96d4ba3ac7a | -12.94719 | -50.98866 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1cf02d09-5376-3bed-a69d-ed7bae874313 | -14.89934 | -48.38966 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9668435a-5145-3035-96e6-bf4e8fff4eb1 | -15.00783 | -56.02322 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdc1c148-132b-3988-aae2-002cb563e37c | -11.07809 | -54.78328 | 2025-10-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7d794d4-ae50-3279-9dc5-0c33df1390c8 | -13.29577 | -47.59532 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 459ba149-f23f-3e4e-915d-2451f5ef55cd | -11.91665 | -46.38 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e8f90e2-55ad-3da6-84e8-7e69dc367013 | -14.16446 | -49.21069 | 2025-10-04 05:06:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02ffaa2b-4d16-3efa-82eb-803b6d613bb2 | -14.88872 | -48.28918 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9304c00b-07cb-3e78-9771-b8026bd54b5b | -13.70555 | -47.35182 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fa715956-d3da-31cb-b13b-d2f91c4b57ba | -11.17088 | -47.74668 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 186a91d0-27d7-3d6c-b5da-5dd9d3e0c1ca | -10.99965 | -46.68089 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7de5d5b-2436-3afe-ab18-84a81ed0f1f8 | -12.30237 | -55.15132 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2ee0ecc-6f27-3b78-9a6c-5401575c3adc | -9.47394 | -60.3724 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e682af07-8c44-3f82-a3b6-7e1e865b7568 | -15.74201 | -46.26398 | 2025-10-04 05:06:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 695995e0-cb51-3abc-b5dc-f99e784d5fae | -9.14514 | -62.36884 | 2025-10-04 05:06:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92b89086-6542-3f53-9963-775cfbd6afa4 | -13.22671 | -47.84105 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7053f8d3-1752-389f-9ffb-f5cb53899dfb | -11.7949 | -45.02738 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 637c4091-99d9-30bd-814b-facdbe8f17e5 | -11.55739 | -47.68063 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ff45c2c5-e8b6-3096-befa-1f30fb249488 | -13.3382 | -47.61574 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1f2df2f-3826-3ab2-a967-cec09a5b6fd8 | -14.88768 | -48.27289 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbc0acc4-3ef5-3a6d-8335-9f03b6fc046b | -15.5813 | -52.46559 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5dff2aac-64ab-3fdb-b31d-a9f030989520 | -10.99916 | -46.68483 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c44304d5-0542-3c1d-87dd-828fd039b959 | -12.52998 | -45.96818 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8380492b-087b-32f1-a643-eba588dcc85b | -11.12628 | -55.45929 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08d82b80-6e6b-3066-ac97-1efdac4fc387 | -11.96188 | -51.48049 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7741ad4-0e04-3236-bbe7-aa0be32651ec | -11.1412 | -47.85524 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dee00db-e470-3ba4-8ecf-4bca4c9177bf | -12.92939 | -54.72299 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e553d01c-acd8-385e-b627-5e158dc8b619 | -11.21624 | -54.98547 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b7f4437-ecb9-3c24-b750-0f64b491dc5d | -11.79224 | -46.83871 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e5d1967-a541-3deb-af82-8bb407acad5d | -13.28789 | -47.18481 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5b712c-e29a-39af-bf0c-5d36811efce8 | -11.00484 | -46.68562 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ca00a58-bd66-3f17-848a-cc87bbf16d5a | -11.92465 | -46.36199 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a921aec-c21c-3fed-b9ff-02c6ffd4b79f | -11.48484 | -45.02278 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20a6d791-6aac-3571-b7de-cd9ac81001af | -13.98835 | -48.19992 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fbe4ad2-b4cb-3384-adc9-1ca8153a7a8a | -11.97077 | -51.47753 | 2025-10-04 05:06:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 951eda87-679e-3e5a-8639-7cc5f169494c | -9.92719 | -60.19573 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 655b7064-ccd4-3b05-bfcb-3ae41ac79665 | -12.29888 | -55.12751 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bde981f-7a1c-30aa-825c-15205e180e55 | -11.4842 | -45.02843 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b775759e-48e6-3b4b-bcb2-0820b1b7120c | -11.91715 | -46.37553 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 236dd29d-d967-3b34-8680-7e0876ff84e3 | -14.66645 | -48.2938 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c8d5830-09d7-382b-a634-0e75272c081c | -13.32083 | -48.1098 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d407dd40-f8f2-3ada-a8cf-a8e00ec1cafc | -9.98567 | -57.81942 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 228e0302-3118-31ff-adff-e5e9d25b674d | -14.75783 | -54.62767 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f352ef8a-baeb-3ec9-a0b2-8f5b3cd2bed3 | -13.32086 | -48.12475 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e20132c7-a8a6-37d7-8741-8d96709bed5a | -14.68321 | -48.27005 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 849ecfd8-da0d-3fc2-90b4-83f377872b95 | -13.7441 | -47.92988 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff74cbf4-cc45-3eb6-864d-f84953d43979 | -13.74398 | -48.09167 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a78f4fe-c1f1-3ab3-a2af-2ef65ce3846b | -12.48982 | -50.24183 | 2025-10-04 05:06:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ae2307d-ce53-34db-8021-861fd8ab5e98 | -13.14374 | -47.93888 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c07fadae-3af3-3d9e-987c-fbc11c707588 | -15.71589 | -46.27416 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af840ebc-4720-33ac-a171-5b0cacd73317 | -13.3228 | -47.25863 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15259234-cd50-35dd-97a1-3f5c79c35a5d | -11.06777 | -49.53732 | 2025-10-04 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6bf9fb8-b573-3fae-be79-54be45a63197 | -13.31837 | -47.24713 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 310274f2-ef8a-3d9b-8850-a9eb4c1b4c94 | -15.74697 | -46.26885 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df7f424e-19aa-3746-a87c-f253c0f595c4 | -15.72128 | -46.2825 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1a80941-42d0-36c3-8b42-692d6e4cc57e | -12.71551 | -48.56343 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c43b88d-1dd1-3dd1-a395-5527562d3bcf | -13.31239 | -48.13597 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README113.md)
