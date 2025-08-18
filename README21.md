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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eda6b029-4b63-3027-96ee-eb45949858a6 | -14.63742 | -54.90565 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59d2d52b-bd23-36b5-9a1b-113bd76a0388 | -12.9866 | -56.84712 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 944e2745-b2df-3458-b905-a0cee7a3a441 | -13.22412 | -50.76307 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 9ab1e976-810e-3ed7-a3d8-5b89dff1255a | -15.00639 | -54.78224 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c699badf-b5f1-3e2f-a55e-f3fdb931ada5 | -14.6294 | -54.91194 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34fda5e0-0a4a-33ee-b33e-51d789976a8a | -14.18533 | -45.3341 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4933db3c-3f74-32a7-a450-4e137fb970f2 | -13.2412 | -50.74143 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8871af8e-6f90-3980-9cbd-3bc304ab903f | -15.49963 | -48.52487 | 2025-08-18 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f8aac22-38a4-3653-a3be-a147afb98ba5 | -14.98193 | -54.77507 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecba34ee-010e-3619-83b0-dd3e3a78722d | -16.8153 | -49.33652 | 2025-08-18 04:49:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42d267d3-c879-3ac7-8f8d-69f0beadf581 | -12.50627 | -57.78176 | 2025-08-18 04:49:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aad3a1f-2ed9-3555-8a19-1798e04fb5f4 | -13.17066 | -54.93348 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37030ad6-dbf3-3e8f-80a4-c82ca65001ba | -13.62357 | -46.89553 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f60cf779-dd91-390d-86c8-38947d7dfb9e | -14.37689 | -52.62883 | 2025-08-18 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a586f449-4e92-377b-a7ad-2c4f0e22b13c | -12.5378 | -48.49402 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 747b3189-43e5-3754-a12c-0a7e1358967a | -13.22126 | -50.75873 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0a45a76c-317c-39e1-b841-211cc8385871 | -13.2144 | -50.75766 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 7083e833-68dc-3429-8d09-39807b24a42f | -17.38871 | -42.62311 | 2025-08-18 04:49:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 989c4700-6fa5-3555-b238-49f687cd99f6 | -13.65134 | -53.69683 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8c0f121-8bee-3c3b-a464-ef6d809f69cb | -13.87185 | -45.54397 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87401e2f-9fb1-3dd0-8804-56ac293a1086 | -14.28572 | -53.19235 | 2025-08-18 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7adc9789-2392-3200-828f-7aba038aec11 | -18.04867 | -43.81787 | 2025-08-18 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b75e6823-b589-322f-abb4-ec4481e93100 | -13.47146 | -47.06812 | 2025-08-18 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0df51c57-b1c0-37aa-899d-a2250915b500 | -12.12383 | -47.90487 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bd67791-673b-333c-ae35-43f88947231a | -12.54407 | -48.50446 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a17c118d-3b2c-3b3e-9c74-880c5ef5f27e | -14.17464 | -45.29851 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5b69885-4316-3e2b-b37e-48dd8c1e44fe | -13.23726 | -50.74562 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 684f4f2f-eb7e-35f4-803d-8a1a53dacc4b | -11.65929 | -51.71706 | 2025-08-18 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f409e785-16ca-34bc-93c9-ad8f131be2d9 | -15.00322 | -54.80132 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 31f3d96b-9aeb-3439-b6ac-5152fa460677 | -13.13417 | -57.14095 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 11045764-7609-3274-a4f6-327280611ce6 | -13.01995 | -56.85585 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 925cd838-1879-315f-b3e1-323bc2516494 | -12.99254 | -56.85797 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f13b5c68-27e1-309b-99e2-b31ef337bbcc | -18.0427 | -43.82127 | 2025-08-18 04:49:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2dee33a-10df-30ad-be2f-fa5800ab4ea0 | -14.97794 | -54.77824 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd488f14-b23f-3429-88af-98017ca7da2d | -12.13527 | -47.90473 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3994b835-8a4e-3afa-84ed-080ce2ac756b | -14.17874 | -45.30452 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ecd6b0d-eddf-3daa-88c9-622978010556 | -13.22469 | -50.75926 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| fae25512-b2ce-3353-8e58-7d4d29397784 | -13.21727 | -50.762 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 45ebd2e9-9d1e-3081-938b-ba92e5363124 | -12.80424 | -59.77428 | 2025-08-18 04:49:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1d76de2-31a0-3e37-b47b-1cc0310d8950 | -11.31468 | -55.21869 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad943e50-f961-3032-9f3b-f64fa258dcb1 | -15.86422 | -50.2122 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07ecd08c-2dcf-31c6-89cc-16b5d979c0a9 | -13.22069 | -50.76254 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 16a5386d-cd56-3bac-b5a1-11f58cb6c564 | -11.85242 | -51.58741 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 699c7def-054d-3214-9f6c-a57a65a13271 | -13.14612 | -57.16337 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 82a82121-ad26-3c90-9fe6-27e37b7fdfc6 | -12.72912 | -45.05243 | 2025-08-18 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1642d78b-686e-358f-955f-1065e5644684 | -14.98133 | -54.77879 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 644cdc42-e95a-3294-8078-c4dee70e703a | -13.13631 | -57.15144 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 522a9a1b-eadd-321e-ad83-6f02b15da3c8 | -15.00042 | -54.78956 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55d28a77-4715-3da7-862f-2a186c137e4b | -12.72844 | -45.05168 | 2025-08-18 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45b27efe-9977-3dba-9e57-379a7f25f546 | -13.59311 | -47.74481 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93bec8d6-31d7-3623-a8e3-981e5cadf087 | -18.54469 | -43.99248 | 2025-08-18 04:49:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e08f7514-b0e5-3797-bfee-b99d7741874e | -13.01762 | -56.84797 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58f6547e-0db7-39ee-be52-529eb9573820 | -13.01464 | -56.8426 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24fe3303-8883-3bf5-a0ec-e3b9eeae8c23 | -15.00385 | -54.79755 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11481572-0c8e-3032-8cca-2b9bbabe1c5e | -13.2207 | -50.78588 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c90443e-0800-3abe-95d5-e040dd71c8fa | -14.6328 | -54.91256 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e5eee92b-3eaa-3f04-a65c-121f9fbdf39b | -15.49529 | -48.52542 | 2025-08-18 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa0a3ed5-f999-3a2e-9853-636f79ddc45c | -13.00251 | -56.84521 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc7d20ce-a715-3a64-af29-543c45298353 | -13.43122 | -45.89374 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f8ea53c-c1da-31dc-9f58-a4d52ba07134 | -17.21801 | -49.58548 | 2025-08-18 04:49:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5405d16b-b4de-3fe7-92a9-847d568a90a0 | -13.22297 | -50.7473 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d4d22aa3-47f0-3194-9176-793be10eaca9 | -13.22013 | -50.78968 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22a9ed3d-9f32-3a26-b4b8-b00361dfcb75 | -14.18495 | -45.33218 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a208f65-67aa-3b24-bda0-36bf774678b5 | -12.99335 | -56.85323 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45b00793-7a06-3b9a-8302-54ded48df84c | -11.8535 | -51.58031 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce0abd6a-1643-3ab6-9a61-ca98885f4ec4 | -13.22754 | -50.74021 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3aa68af-4d25-3af8-86ce-13437b573435 | -14.9881 | -54.77988 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5931321f-93a9-39d1-bc2c-55972c4314bc | -12.13212 | -47.8989 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aad43a2-3bf2-3b27-8346-dac13d79a082 | -13.59027 | -46.98444 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a60f59ca-fa4c-34b4-aa34-acccf9441100 | -14.63063 | -54.90442 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 428d3e1f-6840-3c88-825c-459103ed139e | -13.45392 | -45.89695 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 11499243-ba09-3f3e-8c6f-b592a83fe256 | -13.21041 | -50.76094 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 6710bc89-0cff-33b0-b7b1-e0c07e5ab352 | -11.84963 | -51.58334 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20af5caf-164a-31e3-8aba-b02ffcc04f55 | -16.79844 | -50.09817 | 2025-08-18 04:49:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ea3a28a-2b48-3935-b9ca-b7bdf2773aa1 | -13.13247 | -57.15075 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c14b0afb-bde7-34f8-b23f-38720f053162 | -13.43454 | -45.90382 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5065a92-8139-3051-97a8-062981d362ec | -13.17411 | -54.93407 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 07d556ca-6caf-3741-9508-204a360b0b89 | -11.7515 | -51.71351 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ddca9eee-b917-37b1-9255-929b8822151b | -13.00926 | -56.85131 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c121465-05eb-3e1f-8d2e-f6722593811c | -13.17539 | -54.92633 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43a49e03-9fd6-308d-b6c0-148529f4a3b9 | -13.96573 | -54.09014 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5067ddd4-d577-3d77-b12a-2c1461040e71 | -15.87265 | -50.20457 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6c9791b-f51d-3935-9b2d-5c15e2b95ea0 | -15.00915 | -54.78659 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7afc778c-d3c7-3865-b761-1c5d4f38bc79 | -12.98498 | -56.85657 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7d2fee9b-ac02-3795-bdc6-3f25401ea453 | -13.21211 | -50.74952 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e539817c-911c-3c41-8a28-09b463ef2907 | -14.99919 | -54.79719 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58e43244-e11d-31f4-b650-1539c577c196 | -17.38824 | -42.62756 | 2025-08-18 04:49:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8b9fca95-f62a-3208-a5b0-1d770eba1ce0 | -12.62796 | -46.89537 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b0f4a9c-71e4-3cb9-b568-7e2b8f4e92e6 | -15.61549 | -54.30919 | 2025-08-18 04:49:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70800e6e-24a0-37f9-98b6-8d1330dce21f | -13.5976 | -47.74199 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df454a57-d696-3efd-8e88-4f9b57f0a18a | -12.99874 | -56.8445 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9a50424c-a976-3a2a-aeb9-3655310ef8c5 | -13.17258 | -54.92188 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3822bdb2-5e5e-380c-a823-d23fab897457 | -15.25217 | -49.52374 | 2025-08-18 04:49:00 | NOAA-21 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 552929bb-b954-33da-bd8c-94dfe629cb68 | -13.00171 | -56.84993 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 404eb896-3e08-3ea4-9335-b86f814b726a | -13.22354 | -50.74349 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a7fdd9fc-6bce-3188-8aee-5a2e8a49b48a | -13.01384 | -56.8473 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9775a1e-ae37-3a77-8cb4-9379d524ea4d | -15.96746 | -43.90205 | 2025-08-18 04:49:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 71c4ba56-c45c-35cb-aa6b-0946eeafa422 | -14.95549 | -54.76678 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5eb0b2de-3369-3baa-94b2-f2b1013c90ba | -17.09334 | -49.8792 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e20f7191-6466-395b-83de-4a9f4cc56eaf | -13.47424 | -55.76915 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |


[Clique aqui para ver as próximas entradas](README22.md)
