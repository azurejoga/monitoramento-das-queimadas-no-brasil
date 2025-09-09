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
| af5ffa18-0ecc-341a-8ac6-d72dcadf0acb | -15.22176 | -44.03945 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89ec8680-586e-35c4-9152-fcb11c1c4273 | -17.29288 | -46.74016 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4af79579-682f-3b3f-8f65-a2c7e981b5f1 | -15.82323 | -52.25492 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99f58fd9-f565-3880-a1d0-897dde0a5ab0 | -16.35183 | -52.94324 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d50611e3-d90c-3ed6-bc1a-9840732269ba | -17.29468 | -46.75452 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99b6d1f8-4a05-344b-8a87-4be35a4ae9ee | -15.71152 | -53.54601 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 149c76f3-6072-389a-9493-5df33ebc8d14 | -19.48023 | -43.89913 | 2025-09-09 04:36:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e7cf5f4-afbe-3e50-9b1d-c3aa77931503 | -17.67278 | -52.25417 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23def381-c7bd-388e-8dfe-3f5e2962d3a5 | -12.89615 | -62.0844 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6e8e5ee-3650-3b0d-a47d-e2a0b1f84086 | -16.63123 | -51.85333 | 2025-09-09 04:36:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb18a062-d84c-3a21-85c2-302343e026bb | -15.53012 | -48.40438 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 77493149-e18e-3a2c-b23b-58fb3e7b715e | -15.04936 | -50.12716 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e12247a4-2e10-311f-b63a-890a47b69681 | -18.61044 | -48.21127 | 2025-09-09 04:36:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 430aeb51-f710-3a1b-ac1c-cf414ccdab74 | -15.25432 | -53.80181 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7a2539d-e5a8-3900-92ee-c6fac1015695 | -17.57974 | -49.81362 | 2025-09-09 04:36:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a02c3f27-2e1b-3aa8-bb43-7b05c7b1d5cb | -13.96379 | -54.01738 | 2025-09-09 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8a65152-bcc7-3b10-93b5-ca545dc38360 | -15.50583 | -52.76551 | 2025-09-09 04:36:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 995575d8-4a51-39db-9519-dec2310060fb | -14.54044 | -48.75599 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fbd5bffd-5e3d-3ec1-81be-32b59f0b5f37 | -19.83702 | -50.93863 | 2025-09-09 04:36:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1558cae0-f59f-39a8-b737-656d8f74dc80 | -20.00425 | -46.95784 | 2025-09-09 04:36:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38542f5c-a52c-326e-9637-cd6e71676800 | -15.70714 | -53.5498 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac4d6eba-c2c0-3b8f-b867-a9c5447b741c | -16.32454 | -52.93419 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d53928c8-1759-309a-99e7-15c36668a157 | -17.67428 | -52.26621 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a04f6e0c-b9cd-38ff-98ab-305b86aa7a41 | -15.74487 | -53.52536 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a799e709-623c-38ee-aa0b-37d13bda5da2 | -18.02963 | -47.13359 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8a162732-8fc6-31e5-a320-c8fb71a4a04a | -20.08337 | -47.3558 | 2025-09-09 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca2bd0af-9288-32f3-b6d1-9a9a2045fcbe | -17.72379 | -44.47282 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c98dbcd-a0cc-3b7f-af73-60869a9eea14 | -16.32594 | -52.92598 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d61ec175-77df-3c0a-a678-9da58b91a7c5 | -15.72384 | -53.53943 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 907a860c-d44f-3064-b283-10d7a22cefa1 | -21.00628 | -46.05978 | 2025-09-09 04:36:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d8937032-c767-350e-a303-eaca86aa3353 | -15.26805 | -53.80316 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b95a81-dd76-384c-a0ed-e36fa9774f16 | -14.46768 | -55.95129 | 2025-09-09 04:36:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddbab146-968d-3f58-9db7-4b8a01603453 | -14.799 | -48.18452 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c6c4357d-522e-30f5-8ffb-c098a1180898 | -18.02599 | -47.13295 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 525ffbcf-58e8-33b8-bfc3-845f315156ac | -14.54378 | -48.75654 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8b6d320-a93c-3ea1-abdc-d50e9f7547ef | -15.78009 | -53.54321 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b9450770-66e3-38f9-9348-01d8157c3e3f | -17.27434 | -46.73751 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ba7dc689-4a14-3a71-b70b-cd99398df186 | -15.81508 | -52.26158 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7183796-a6c5-3288-9a38-8a9bf9a727f6 | -16.07223 | -50.48083 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cc030a2-ad71-3bc6-a5f8-f59cbd636e77 | -14.76784 | -47.77968 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79953a87-86ab-3da9-b594-8977158e270b | -18.83515 | -49.68942 | 2025-09-09 04:36:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1c338c30-f532-332d-a671-9bbd19eafe5c | -12.88604 | -62.10117 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45fe3da2-4045-3c7a-b336-509db4d67ed1 | -20.17391 | -44.7987 | 2025-09-09 04:36:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ba41095d-ff06-3e76-8680-3517636d9bcf | -17.29224 | -46.74478 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a37706e8-db26-3e3e-b909-82ac675e48a1 | -18.12028 | -45.3236 | 2025-09-09 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a5bc183-0004-331d-ae6c-b1a5ae910982 | -16.34206 | -52.93712 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14978070-a78b-3aa1-9bfd-f2e73d56d565 | -17.73374 | -44.49715 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7ac0ebf9-521d-3c9c-aa9c-348c78e671af | -15.72966 | -53.52716 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37236ccf-892c-3373-99c9-30eb22d1a97e | -14.78888 | -48.22935 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a830259c-dcc8-35db-a631-e7d994894efc | -14.52819 | -48.74657 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccd617d2-10eb-3d20-ba54-51bdbbaa25b2 | -14.36323 | -60.30987 | 2025-09-09 04:36:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 579a8f6f-fa9b-34ff-b1aa-94e4f1e1239f | -18.06409 | -47.37098 | 2025-09-09 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d97169ea-8a19-355c-b4a7-b5581adef01e | -18.34428 | -49.38544 | 2025-09-09 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ee6f8cee-c859-33f5-a453-a6da7af0ad8a | -15.77935 | -53.5475 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02d8a978-8562-3656-821f-47eb672e113c | -17.26204 | -46.68865 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 832bff4e-de50-3d1d-8eb1-fa16c84a26ff | -15.78383 | -53.52159 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1f072cd3-abff-321e-8db8-c0eaa9a310db | -15.15376 | -44.02979 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afed05d9-3c4a-3a99-aae2-0f05ed79ba38 | -16.3435 | -52.94991 | 2025-09-09 04:36:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54ceb44f-10b6-3468-90b3-51f34e4897e4 | -16.06449 | -50.48687 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb552e4e-0ba8-3a45-8bfa-ac1017c1bbbb | -17.67765 | -52.26685 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19eeb412-7108-3226-8f67-d157481c7282 | -12.88722 | -62.09563 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 109664a8-2933-37ec-814c-6f07e018a292 | -20.44723 | -48.0609 | 2025-09-09 04:36:00 | NOAA-21 | IPUÃ | SÃO PAULO | Brasil | 3521309 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b283dad9-c816-30fb-b417-0a85851c6c29 | -15.82826 | -48.95639 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bd96c11-71d3-36ca-bcbb-fb8ca22bd4c0 | -14.53821 | -48.74819 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6707f0b8-3cb1-331d-8259-24372aae5a18 | -17.67215 | -52.25797 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b89daf6-8394-35ba-990e-4fd5dfc0dc2e | -15.82326 | -48.94419 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 7d0e725e-079b-3f90-8ca0-8662e1485781 | -17.99172 | -49.26449 | 2025-09-09 04:36:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a496f52-b0a2-37d9-a226-2a010267322e | -18.0132 | -47.11744 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e1bf460-d8d6-352c-8e60-1cf960bb8a07 | -17.6789 | -52.25925 | 2025-09-09 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75e0555a-7905-395a-b8c3-02e2be47b600 | -15.70787 | -49.8969 | 2025-09-09 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e44a6ac1-da40-33f2-bcf6-4721a6884638 | -17.16177 | -44.45749 | 2025-09-09 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bdd5164-164f-3423-804d-2738f5bb4a0b | -16.06997 | -50.49512 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bc9df50-cc7d-3da3-bd12-c42271c65fa8 | -14.5332 | -48.73615 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8397cd0e-24b6-3e26-9e38-766df719ff9c | -15.16663 | -52.39947 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59fa2e2f-65ba-3a0a-8a97-96ffc0e90dd9 | -18.04093 | -47.07943 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de9406fd-646a-3e75-ac0a-c2c4ae2e57ca | -15.11639 | -52.35887 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d82fb394-715d-39fa-b777-cb361be70d03 | -16.08102 | -50.48964 | 2025-09-09 04:36:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c2443aa-ce53-32f5-adc7-e1daa243ad16 | -15.77646 | -53.54261 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 004b7585-cf12-3fd3-9e12-8aba85707f7d | -15.24836 | -52.34886 | 2025-09-09 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e97c64b-26be-3e73-b251-e252a56572a5 | -18.1507 | -43.39403 | 2025-09-09 04:36:00 | NOAA-21 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4622d21c-f42c-3c70-9c87-15ba4ba76dd2 | -16.06731 | -50.469 | 2025-09-09 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e0214ff-6153-3bc3-b0bd-59dda3111756 | -17.56902 | -44.36234 | 2025-09-09 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3758950d-62d9-3f01-b009-8a22335145ef | -16.43967 | -49.28912 | 2025-09-09 04:36:00 | NOAA-21 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9583af21-4446-3337-aa10-f72c522bed3c | -15.53461 | -48.39753 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 60046826-895d-3950-b641-9b4ea4d31667 | -17.27248 | -46.75114 | 2025-09-09 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7aceee16-5385-3a18-af42-14153810ec17 | -15.17694 | -47.95008 | 2025-09-09 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 005999ec-c930-3ccd-963c-f34913f9b814 | -15.26725 | -53.80772 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d6cd29e-8f61-3b80-8348-b2e854c0bb8c | -16.42898 | -49.29551 | 2025-09-09 04:36:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f14e17-97cf-3663-89ce-e2ed16715dd8 | -18.03388 | -47.12994 | 2025-09-09 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 202fc2c5-b8b1-38db-a81e-c681e59d1bb1 | -15.54867 | -48.37294 | 2025-09-09 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe02b3a7-9287-304f-a1a1-7eeb12ef2ac4 | -16.89964 | -45.82811 | 2025-09-09 04:36:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2437931-fa4b-3be1-b457-a13eb34ea9f0 | -17.73084 | -44.48577 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7151a9d4-ce9e-357e-9939-123e15ec4efd | -19.65296 | -44.90205 | 2025-09-09 04:36:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 552fce25-207d-3c13-ab02-7e5d728ff591 | -17.70663 | -44.47083 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8b13fca-cef3-330d-89fa-aa985e4a23ce | -16.04942 | -48.06572 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee21c6fa-ff18-3580-bb4d-cd884312ed57 | -15.8277 | -48.96008 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b8f2b9f-cb62-36c3-ae1c-ec81964369e9 | -19.88129 | -48.18824 | 2025-09-09 04:36:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5c00e7f-ad86-30e4-aefe-e1ea8da11580 | -19.52034 | -43.98896 | 2025-09-09 04:36:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6343e544-d7fe-32a6-aefd-23da0746c7ac | -18.06047 | -47.37046 | 2025-09-09 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 112abe2a-1430-3e59-9e19-b8a2002f42ae | -15.08578 | -50.08945 | 2025-09-09 04:36:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README54.md)
