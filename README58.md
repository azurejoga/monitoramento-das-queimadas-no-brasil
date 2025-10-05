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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4aa5eac-46a1-3804-9de3-8c1348edc083 | -13.78497 | -47.8338 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec6c451a-86a0-31dd-a335-fb0fccc4bc4b | -15.26733 | -44.12976 | 2025-10-05 03:55:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e8e2a93a-a7d9-34b7-8c88-e26ebc8d1a9d | -13.3539 | -47.20536 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7e2f32f-4dfe-3cc1-98bd-659a6b9fc355 | -15.17321 | -43.63599 | 2025-10-05 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dabb9693-ebf5-3043-841d-0ac7a6d91830 | -14.66777 | -48.34159 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4362327-c1a3-310d-a6f6-a84c16dabf6d | -15.22594 | -49.29377 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2d79926c-ac82-3fae-8f9e-eda4a63b574b | -15.30396 | -46.31077 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131bad11-b506-3361-a0d8-12d5e57c57f3 | -15.38331 | -47.94268 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41518d70-53aa-3279-9db5-b9a134c86cff | -15.23533 | -49.30628 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbd92566-10a6-31cc-bf18-446a6507979e | -14.59779 | -48.35136 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 614a2aa8-6a97-351a-b9a7-7f347430abcd | -13.17755 | -50.87267 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a4cf666-45ad-310e-afeb-ef55d0d5241e | -10.56649 | -48.71888 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 737bd414-c754-385a-9bb3-a99a2c0a7dad | -11.68269 | -47.48751 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ea4cb8f3-2e6f-3adc-b6f8-e97076c8295d | -13.08032 | -47.90464 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb9ba909-20fe-345d-903c-701c859585f7 | -16.60409 | -49.38308 | 2025-10-05 03:55:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49a6f80b-0de4-3e29-a6b2-a2c6cd2ad61d | -13.14557 | -47.97121 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef67a52d-795f-37dc-a957-c3596a5fb112 | -14.87351 | -48.15435 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9824a628-47de-3830-925f-17352be83aa6 | -11.91614 | -46.24525 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3137bf77-1916-32c3-8c10-0fe655d5ac30 | -15.52357 | -46.88011 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4964ee0-173a-37c1-a41f-d82c5364ae04 | -15.28594 | -47.33476 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 553a856a-1b6e-3719-a4ac-17278ef69c30 | -15.93155 | -48.99098 | 2025-10-05 03:55:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65a6e4a4-5c8b-3c51-a820-e5e99e163523 | -11.48978 | -45.03266 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ffca86-9558-34e0-88c0-344520c3f4d7 | -13.45685 | -47.26251 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0315b22-7197-3b2d-8344-b0d033d5dd46 | -10.45904 | -47.81637 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e1ac459-8bb3-3401-87ad-e0ac93c482d7 | -11.45135 | -44.95148 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf6bcf88-76d8-3719-9739-f12c112c3b82 | -15.50674 | -46.84921 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a84a30e-5b85-3eeb-a6b2-d2af434fd463 | -15.80332 | -46.2718 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86232945-dc96-3c87-a4e0-29b1b7834978 | -13.74698 | -47.96991 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16c117d4-48e9-37c3-b455-199d0e9632f6 | -11.82819 | -45.08496 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37555878-9225-35c6-b2fd-cf096f113f05 | -11.24925 | -47.78493 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3fead40-b2a3-391e-8d04-7b756a50eb68 | -11.53719 | -47.6788 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e65fedb3-4314-3c9e-87eb-16d56f2da63b | -11.11208 | -47.14057 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f95f2cdf-1dcf-34e4-ba59-d635565bc568 | -16.37907 | -52.1668 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e7782547-c902-3f9c-a161-edffe8495a6e | -13.30751 | -48.12175 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3d4245e2-7963-36a6-9091-71abb57f14ee | -15.12476 | -45.74241 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1c0fcf9-9d4f-3162-bfb3-97acee225c85 | -15.39254 | -47.95214 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 11dcaa13-cd45-3b3b-aca9-202e33533c72 | -17.57123 | -46.08395 | 2025-10-05 03:55:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20a9634c-d84b-34fa-99aa-3a3550b0c366 | -11.90369 | -46.2258 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d36a1a3e-3ed1-356f-a2db-e6a6b4c5fd6b | -16.11577 | -53.98415 | 2025-10-05 03:55:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 079cca39-120b-3e91-8df9-f1fc6993dc6a | -16.0435 | -51.04045 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f506527-dfb9-369d-8fb0-431b42e809d3 | -14.32229 | -47.70469 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1a43560d-bcc9-3d30-a2c0-a3aa3dcb885c | -13.15142 | -50.92481 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 33883bec-802a-3ddc-8e39-ba42f03a69c8 | -13.34448 | -47.57645 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f27a012a-2d13-37de-94fb-4be017fac592 | -12.14018 | -50.93562 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 556888fa-64af-38ba-aba5-06e982ca07b1 | -15.44519 | -45.87042 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e795e5c3-8f8b-3857-8c0d-37c30a3eac1b | -16.38945 | -52.15265 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12e34ffd-8fd5-36f1-8d6d-26370faaa1fc | -13.52204 | -47.28746 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0645ed22-1615-35d4-b50b-5092b2ef409c | -17.01545 | -43.45188 | 2025-10-05 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2411e6d1-4b77-3632-9c74-eb844a8d4e3e | -11.11108 | -49.86817 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 564e1925-c098-38ab-875f-0bc878940bff | -10.75574 | -46.61803 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5a9dffa1-9df1-3fdf-8108-a5728b3f51ab | -13.62636 | -48.6873 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1ba03d7-3653-3e4b-90c1-3fd4ba2e3953 | -13.47893 | -47.28527 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88a38f5b-61f5-33dd-b819-bfbe6a04fd83 | -12.59681 | -48.13974 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39f90ddc-10ba-34d9-9eaa-ae12e007af03 | -13.27114 | -47.62608 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e92638d2-7f67-39ad-b694-f02aeef770ea | -16.33299 | -48.06818 | 2025-10-05 03:55:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3b3f7d68-74f9-35dc-a099-024246556675 | -15.54842 | -49.28187 | 2025-10-05 03:55:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cdda2b4-3360-3417-b6b5-7d560b4862e7 | -16.43497 | -43.2801 | 2025-10-05 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb6c02d2-bcbe-3389-955b-1ffc8313d518 | -13.48609 | -47.273 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 41e355e2-584a-3c29-b75e-cec7234b537e | -13.45361 | -47.29107 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 506b5f47-fe06-3acc-bccd-d8b7ee01904c | -15.75266 | -46.2639 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b1c227f-d8ec-3dfe-91c9-dffbc460eee9 | -12.91114 | -47.31121 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 02368010-e080-37e9-8d01-ddedb0af3c93 | -12.46026 | -45.51402 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d56108c-c16c-349b-b136-608a8cc7c2c9 | -14.67203 | -48.37162 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1bd6d840-8d4d-335a-98e6-cdfb18dd1602 | -14.66638 | -48.28535 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 95ed1bad-9329-376e-a4c1-94bb900a3431 | -14.27208 | -45.86305 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbac3036-f19f-398e-ba50-703c773294b0 | -11.01546 | -46.70214 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a5b423b-760d-3704-bd9c-f8a9156426b8 | -13.05534 | -44.93722 | 2025-10-05 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8123e0f-1d02-3efe-9a15-ec6599307aaf | -13.48472 | -47.28026 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1e35f84-36ee-3542-b5bc-4217e5e0a88c | -14.66261 | -48.27859 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9df7ca9-7c96-3e09-ae09-dfaf596ec5e7 | -14.49624 | -47.5126 | 2025-10-05 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 855dca94-836e-3230-ae46-04b3df124d3e | -13.38701 | -47.5604 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae3c5937-c207-3017-9344-d1ab12b6cdf6 | -13.33992 | -48.06321 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ff5b749b-22c8-3b53-8161-eb4632bc01fd | -12.82121 | -46.86596 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fba1a3d7-2484-3911-b0f1-2e84406c86d8 | -11.79615 | -46.8363 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42d01674-2f2d-360c-ad05-68c1b5e9480b | -12.77536 | -48.82016 | 2025-10-05 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8800b2a-b21e-3b50-b317-a63d850dc056 | -14.87693 | -48.26718 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7e7ecdf-5146-3718-8691-05e0bcdf483b | -14.66808 | -48.35644 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c01fa3f7-71c0-3dcc-845b-4bec0be24bb4 | -15.16958 | -43.63531 | 2025-10-05 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9d552a6b-6dca-33aa-a203-9f514c2a4006 | -13.83957 | -48.05266 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3da4f20c-cd20-31c3-8483-48e27f49801e | -11.79891 | -46.82162 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d8c593d-b93c-32e0-a1ab-faa6947f752c | -13.74299 | -48.06784 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 672c8b7b-7570-3997-8b00-128a5217227a | -15.71914 | -46.25531 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43eb2ba0-7e75-3759-b78f-f9b77aff9ee2 | -16.01878 | -50.96093 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8a5357ee-481a-3013-8cdc-c919ebef32c4 | -13.73295 | -43.49633 | 2025-10-05 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77ed900b-6964-36a1-b1ec-9502cb6899f5 | -14.95243 | -46.85836 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0442e686-a033-3039-b3f9-41912b473ac8 | -13.45876 | -47.26424 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 56ee2402-c417-3668-a7a4-1b0c91c7596e | -11.01967 | -50.70263 | 2025-10-05 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2154e694-cfe2-3b30-a818-7616dc832037 | -11.91531 | -46.24971 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f09bbdfa-181a-39cc-aa8e-78817691ef78 | -15.60652 | -52.50275 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2604ae9b-4497-34f9-aa94-a6910440cc43 | -10.93881 | -47.09361 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f749cdcb-ab47-3a48-9af5-94cbbea4a025 | -11.85133 | -45.05133 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e8ea2be-f282-3e14-89bd-7b22f3ed541a | -11.151 | -47.92873 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ef80703-1f28-35ee-965e-80fde214be72 | -12.77473 | -48.82343 | 2025-10-05 03:55:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73b40746-f3fb-3e32-ba7a-a05c96afc48c | -15.17033 | -43.63095 | 2025-10-05 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ded23eda-e62d-33a8-84b2-fdd31d252cdf | -10.72823 | -47.64703 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64605e1d-c39f-344f-b5a2-41f826eb0ca9 | -13.78978 | -47.83474 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3038bae1-faba-3248-8a69-6b54029610a0 | -14.68172 | -48.29673 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5016a78-abd8-33ed-bfc2-71a522ad98ab | -13.35787 | -47.58407 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fb44588b-1c93-3ef7-ba26-0d92b522ceec | -13.43996 | -47.27551 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d9bf401c-4cf9-38ac-b115-97cc55bde747 | -15.70214 | -46.27716 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README59.md)
