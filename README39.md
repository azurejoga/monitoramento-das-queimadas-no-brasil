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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 206aa79a-b706-38ec-965d-fa2e48440ba6 | -20.6124 | -56.7335 | 2025-09-26 04:46:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2d05e919-f540-32d0-be10-c77dae25050b | -23.76862 | -51.62484 | 2025-09-26 04:46:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| cc9a9975-f2ba-3080-aa4b-d08153981aec | -18.47398 | -50.38379 | 2025-09-26 04:46:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b7f24272-d59c-362e-a200-8168806788b3 | -21.03929 | -51.11446 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| b7eedfb3-b778-3164-b8d3-be2a5302935d | -18.69731 | -52.0154 | 2025-09-26 04:46:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61503ebd-cd17-3cf6-8edb-2169f0c7b293 | -21.03472 | -51.12171 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 7f4b9163-44b2-3a34-abb4-b2af852c3628 | -21.84617 | -50.57806 | 2025-09-26 04:46:00 | NPP-375D | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a1e86e5-ea75-3d60-b5a0-d4529aa4c219 | -22.60979 | -49.02609 | 2025-09-26 04:46:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f237a3fe-a208-34d9-b1f7-870a8f9b0bd5 | -22.24607 | -56.04855 | 2025-09-26 04:46:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f525e88d-e57c-373b-ac58-cb7a2ceb3499 | -20.56974 | -47.17966 | 2025-09-26 04:46:00 | NPP-375D | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62df1a36-bfb3-3ca3-acca-5b1ff6ae51f6 | -18.31088 | -57.10686 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a35eb6a-b12b-3df1-9e58-56b45b79f600 | -22.37988 | -49.48425 | 2025-09-26 04:46:00 | NPP-375D | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7223f076-58c3-31c4-8ff6-e837eff3ac48 | -21.0159 | -51.10651 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8794b7c7-92c3-3825-acfb-6de81d347f32 | -18.30695 | -57.10606 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2cd74c1c-55cd-39bb-86f5-5206125cb0dd | -21.00011 | -50.01658 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8f5493fb-3f14-3327-9b29-4edb14db9d08 | -21.83856 | -50.58107 | 2025-09-26 04:46:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d4c211c6-7008-3a8f-bf87-dfac742dc0ed | -18.18875 | -53.33253 | 2025-09-26 04:46:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31a4a37f-d944-3fa4-bb7d-8dc024039dc1 | -21.00488 | -50.0087 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1b1654d4-39d9-3616-a499-ac8a48407ed2 | -20.5568 | -57.07792 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 381ea0de-0cae-3e23-9318-dd40fdb5a936 | -18.51486 | -46.9636 | 2025-09-26 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77cb0bd7-3163-3dc9-91cc-c0da71c57356 | -20.53704 | -57.0994 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7eb912f6-3810-3195-a523-be9443dba8dc | -30.39237 | -54.25146 | 2025-09-26 04:46:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 62ec796f-df7b-367d-965e-ee99ceb68dfd | -23.76517 | -51.62428 | 2025-09-26 04:46:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| dbd2eda8-c887-3617-9583-9fa23d5d4dd6 | -19.9248 | -43.62127 | 2025-09-26 04:46:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ddf19c7e-7175-3965-928d-72e67b2cfda7 | -20.53845 | -57.10294 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03135311-d0d8-35fc-974a-6b9ae814d044 | -20.01566 | -44.23918 | 2025-09-26 04:46:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 165fc3d2-456b-390b-b140-fbb93b060bc7 | -21.03529 | -51.1178 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 835402c9-a07b-3484-9ef4-8a31ce4868e5 | -21.03129 | -51.12114 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 27280d76-a9ae-3ee8-b2e0-2c9b5f45c93e | -17.92725 | -55.85472 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9af8b3bc-2c11-3d36-b676-3deaec0b7f39 | -18.51439 | -46.96718 | 2025-09-26 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a18f91a-037a-3fa4-b921-219ba0b7a3d1 | -17.9289 | -55.85251 | 2025-09-26 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c8b6a717-4821-3564-a12c-18daf1e78e1a | -22.60534 | -49.03046 | 2025-09-26 04:46:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4f8e1b7-2827-3305-a00a-fb1a72e60970 | -20.56059 | -57.07871 | 2025-09-26 04:46:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e1dd2cd-d380-3074-8f93-7d0b4cc8621f | -17.17874 | -56.36642 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 59d8517b-6ab5-3807-a803-4d1161f3531b | -18.55102 | -46.96795 | 2025-09-26 04:46:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd5f53d9-1225-3124-963e-632f436bdd43 | -20.99418 | -50.00703 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 250ca73d-7dad-3880-b4ee-a7a69d72e84d | -17.18484 | -56.36006 | 2025-09-26 04:46:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 20afef97-a858-315d-889d-52a7bcd6a7aa | -21.03072 | -51.12504 | 2025-09-26 04:46:00 | NPP-375D | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 20e3ae0f-7b27-3036-80d9-dd11d434fb1f | -21.00368 | -50.01713 | 2025-09-26 04:46:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 803cfe17-77dd-3fdb-b79e-472f1287ecc1 | -25.88369 | -53.28096 | 2025-09-26 04:49:00 | NPP-375D | NOVA ESPERANÇA DO SUDOESTE | PARANÁ | Brasil | 4116950 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 610b2f34-8db9-3b7b-aca6-9c243a83d38f | -27.48702 | -52.67881 | 2025-09-26 04:49:00 | NPP-375D | BENJAMIN CONSTANT DO SUL | RIO GRANDE DO SUL | Brasil | 4302055 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c5d402ed-5374-3c15-bee6-1ef48d6b1ab1 | -27.49046 | -52.67935 | 2025-09-26 04:49:00 | NPP-375D | BENJAMIN CONSTANT DO SUL | RIO GRANDE DO SUL | Brasil | 4302055 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6531c11c-0094-3d28-83fc-590a76447b40 | -26.88032 | -48.72009 | 2025-09-26 04:49:00 | NPP-375D | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a82c281-b8b6-34ee-9272-a9f7fd20b71a | -26.8828 | -48.72309 | 2025-09-26 04:49:00 | NPP-375D | ITAJAÍ | SANTA CATARINA | Brasil | 4208203 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eb5fa3da-832a-3846-89b0-ca45089aead8 | 3.90985 | -60.23672 | 2025-09-26 04:59:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8027ffa2-fbfd-3ba2-8ed3-4f576a2b8845 | 2.64822 | -51.01061 | 2025-09-26 04:59:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 215ca89c-59cc-3c27-ad55-4552837e717a | -2.96257 | -48.59443 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d026f184-35bd-3800-aa09-b7a171628299 | -4.78683 | -42.82054 | 2025-09-26 05:01:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0ed598ef-2b69-3abd-bef3-a8a9d1d5fbbc | -3.80572 | -41.57455 | 2025-09-26 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 954d9f23-4b8b-3204-bbf9-e7131ef3d4e6 | -2.9199 | -48.30537 | 2025-09-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8f1e6c5-f813-3ac6-9076-50039aa571b5 | -6.85516 | -43.18595 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f97998b0-baf2-37e8-8e68-7ab5bb7e2e57 | -1.15004 | -54.22069 | 2025-09-26 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ecdbeed-e9f0-332c-b353-8a0baa8c5361 | -3.77911 | -48.63554 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39713a18-718a-396a-a8ed-579037969e86 | -6.85268 | -43.18029 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7d7bba82-007b-335c-93a0-7f39be858aa1 | -5.6343 | -43.92552 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7607fcdc-f446-3d75-a34b-a5e2becbbd3e | 0.247 | -51.30277 | 2025-09-26 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b80e908-2e69-38e4-80a3-7f58dc42c5a2 | -2.69637 | -54.94934 | 2025-09-26 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4b80c1bf-9995-38d3-8d47-4ea4b315266b | 1.00841 | -59.50737 | 2025-09-26 05:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 233b2145-e3d6-369f-a9b0-a233112c0ebb | -2.4475 | -49.01435 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f7c1574-1a19-392e-aa89-b4c9670fbccb | -4.75427 | -43.61491 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a84d07c8-1c17-3b12-a00c-d070f22262ea | -7.10937 | -43.74455 | 2025-09-26 05:01:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21110c1f-5336-32e9-aac2-f6c563020fe2 | -3.05751 | -48.71049 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a3f411d-7f04-39e0-a7fb-f0662ddd2680 | -3.05764 | -48.70783 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b297da4-81fb-350f-9079-b2a67c51ddee | -5.74906 | -44.96094 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 63c39c87-f219-3479-8f95-b0b0e81eca0c | -3.32816 | -48.70385 | 2025-09-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c077bb4-ac5b-34d0-aed7-bf838003a830 | 1.00667 | -59.51226 | 2025-09-26 05:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 187522ab-66f8-3d72-9866-60fb52c5a1ca | -3.44067 | -44.12825 | 2025-09-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1183767-b00e-3865-862a-d43aed1d34ef | -3.17284 | -49.47755 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a13b6d4-079e-365a-9d00-86291bc89a35 | -6.26084 | -42.48854 | 2025-09-26 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0bb364d-a46f-350f-9287-ad590c716ae6 | -5.58299 | -48.95588 | 2025-09-26 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67828c68-0f60-30ef-bd20-f75cd78bdacc | -5.74223 | -44.97895 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| ab6874a1-81a9-33e9-a971-cb0f671fa140 | -4.48038 | -47.67684 | 2025-09-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df8b2c2a-ddf8-3551-b889-7a470e5e433d | 0.71354 | -51.37044 | 2025-09-26 05:01:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7aebf2c7-ef20-322b-a51b-c201a5fd99ba | -4.74871 | -43.60872 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c127e9e-97f0-310f-9e51-6389326b08f7 | -5.73317 | -44.91581 | 2025-09-26 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bf22c80-878b-3de4-9edd-dadecec0def5 | -4.17121 | -44.27503 | 2025-09-26 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e85a9f9e-6721-3eac-ae19-1d7a2a5afcd1 | -6.54681 | -43.93253 | 2025-09-26 05:01:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 36090dda-2499-3bfe-bd43-164c44a5e83c | -4.81058 | -43.5392 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c773fdf-68af-3100-be2a-f82c3ab142ca | -3.69113 | -49.04367 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cee9483f-e22f-3f71-a557-1e9523b72926 | -5.63361 | -43.93051 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2305e56f-a22a-3b31-8d7f-0a559bfe18d5 | -6.71166 | -42.74748 | 2025-09-26 05:01:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2a6105d2-8d34-3e0c-8333-858662116c1a | -5.7555 | -44.91343 | 2025-09-26 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ce8eabc-c526-3059-8488-66fda37a69ce | -6.8791 | -44.50668 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 522f7180-8998-3b0d-b5db-661674a3a251 | -5.46737 | -43.0765 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2112ed01-710f-3b41-95e4-2ae1744077ab | -5.742 | -44.96878 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 670c8106-8534-3d7c-b379-ecb71c8ca63b | -1.37149 | -47.16583 | 2025-09-26 05:01:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ba9af7d-e563-36f6-a141-12b033a4137d | -5.73872 | -44.96142 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b7ff9d62-54c8-39ef-92e6-188b2948c6ef | -3.79016 | -51.82893 | 2025-09-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68876481-5038-3ce9-83ec-6928db3c3892 | -4.16969 | -44.27232 | 2025-09-26 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1c22283-b81f-3c3d-8514-82db4af66588 | -5.46901 | -43.06487 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5683d2f7-d375-3c2c-a2bb-dc781550c293 | -4.74446 | -43.26707 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c54ddec-b46e-312b-853b-5989ee681294 | -3.32376 | -48.70324 | 2025-09-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a77e0bc-6dae-3a0c-b990-5926a8e1733a | -2.35851 | -48.89187 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63db17d3-181f-35e5-a283-1db60a1867fd | -5.74144 | -44.97297 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| bed6a740-cbdf-32c6-a651-c1ae6ca5d2bc | -6.71812 | -42.74438 | 2025-09-26 05:01:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ea21515f-90ac-3290-a3b5-9cf1509bf25e | -2.69361 | -54.94538 | 2025-09-26 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96378990-610c-343a-badb-a19a4db62c98 | -3.80389 | -47.58743 | 2025-09-26 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4c4bca1-0fa2-3bdb-8c48-a863521696b7 | -3.44387 | -44.13205 | 2025-09-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 808fb7b4-1299-3535-a475-126a5565ff8d | -1.0862 | -54.1085 | 2025-09-26 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1b3b636-2c0e-3d37-9aed-5a2ddda5ee43 | -5.73692 | -44.97408 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |


[Clique aqui para ver as próximas entradas](README40.md)
