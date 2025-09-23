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
| 65093604-3d82-3dd8-a756-b062307871b2 | -15.35823 | -59.17755 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb525cf9-4ffe-3296-a62a-628c2f1d72cd | -15.78352 | -59.48204 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5402eef4-62d7-3aa4-a09e-b6e2054d7eff | -14.77147 | -60.22338 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc38664a-57bc-3239-b62d-6b041f7d3053 | -15.36043 | -59.18522 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e19c08c-5bc5-3740-b010-d983b6fbe832 | -15.28596 | -59.42134 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1363c01-1071-3369-97e3-72755848219b | -15.34226 | -59.19318 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22e3bb2d-aa78-3455-b6f2-16c007bc17dd | -15.35602 | -59.1918 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237c0960-26dc-36ab-874c-483ca40d2650 | -14.76815 | -60.2228 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 960c72f7-5fe6-3878-85f2-4f242a7126ba | -15.83164 | -59.58855 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 41a90a0b-ce33-375c-af0d-c8ffb34ef22a | -15.9463 | -59.48658 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c6a63cd-3f8c-301e-9362-0aa70d42799d | -15.35217 | -59.19482 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c76b8df-0793-33a9-b1bb-4658b845f51c | -15.31737 | -59.41897 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c41483c-b8b1-393e-bf05-9620001f575e | -14.40515 | -60.2985 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 910e9590-d3ca-3775-9a9d-a05467fbdeb8 | -15.96062 | -59.48166 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9f611c9-847b-3a0a-9772-094933fd428f | -15.95071 | -59.48002 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abc2eec4-ba55-378d-a111-3ac00f42881e | -15.82334 | -56.12362 | 2025-09-23 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7076b451-798d-36d4-9a23-91bf309df35a | -15.28652 | -59.41778 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54b7fe36-af85-3b61-a198-90442b034be1 | -15.96006 | -59.48521 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14323a1c-fe2d-3c21-8e5f-287fb6f400de | -15.35658 | -59.18824 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a4dc8e1-7be6-32c9-9e2b-369858b940ba | -15.35382 | -59.18414 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60e804ec-d297-394c-a62b-c22400ec3c8d | -15.14681 | -59.46404 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 453b8d29-8cc2-325c-8640-e337cf04ae04 | -15.35988 | -59.18879 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13318191-113e-3ed6-ab65-dbe80142543b | -15.78626 | -59.48615 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7176b10e-6bc5-38ad-84a4-70f7df4b40a9 | -15.8388 | -59.58609 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 819ddf4a-3a6a-3c3c-868d-03cea202d55a | -15.34886 | -59.19428 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd51d543-c08e-3f23-916e-3383588c15cb | -15.78679 | -56.17232 | 2025-09-23 05:14:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 280ff472-4792-35bd-ba8b-16550f33941d | -15.4087 | -58.78232 | 2025-09-23 05:14:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cff28b55-7f9d-3d46-b3b7-7bf28d0cbdb2 | -15.36153 | -59.1781 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ca748d6-359b-3dee-96d5-0c4c9b98e911 | -15.95565 | -59.49179 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecbe9bb9-a812-33e0-bef9-6d9a1ebb62b8 | -15.84266 | -59.58308 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99cc0657-3db3-3596-9783-d3455744ccc2 | -15.95731 | -59.48111 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94a1950b-4185-39b9-b8d2-88f8399e02b4 | -15.96336 | -59.48576 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb8a396-9bff-3b13-b3ae-590661524e9d | -15.34501 | -59.1973 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 175beb95-2890-3025-88c4-3f047d673417 | -15.96392 | -59.4822 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4caab08b-ab73-389c-a1bd-87f0f0aab20a | -15.95235 | -59.49123 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cf7de72-69f5-376e-8c51-1c968275c354 | -15.8421 | -59.58664 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64f3cdb7-591b-3167-9735-a1d5d5fcb922 | -15.9475 | -59.36647 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b45c1c2a-76d8-362f-8dee-6ec83af4d9fb | -15.83494 | -59.5891 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2385e3d0-5826-395c-b899-1b1924663567 | -15.79044 | -56.17287 | 2025-09-23 05:14:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6e736836-d35c-37be-8d1c-ff62a34b6ac5 | -15.92272 | -59.3734 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 793d1e0c-c867-38a9-aa17-8f9163319504 | -14.76757 | -60.22644 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4151904-59c2-36ae-b613-79155334e0d1 | -16.46194 | -55.13094 | 2025-09-23 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5b28c136-0d88-38c1-af45-db169585a93f | -15.94467 | -59.47537 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 144f15ee-52d4-32f3-9b9c-3ff1cdc6d883 | -15.41534 | -58.78339 | 2025-09-23 05:14:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ab4483-466a-341e-9007-8b4a155da925 | -15.35768 | -59.18112 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81e90837-1a5a-37dd-9070-2f13dde7deca | -16.463 | -55.1274 | 2025-09-23 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6e20377b-df5b-321f-970d-eb970ac3d6da | -15.73349 | -59.45554 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8648ac0-b9bb-373b-9681-f8eb584ecfe7 | -16.46584 | -55.13152 | 2025-09-23 05:14:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a866de4f-5d21-3433-973e-c17d16ef709f | -14.42399 | -60.30889 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8c0a845-2f23-3b40-8030-50a90880aeb9 | -19.88522 | -52.96056 | 2025-09-23 05:14:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 62ef1665-f814-329e-ab7f-e74152ce9f87 | -15.9562 | -59.48822 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6fa3979-431d-3c69-be67-60b3008bb818 | -15.36484 | -59.17864 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e92a1dd-b096-32f1-8bad-691d71733951 | -15.83439 | -59.59266 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4658ec5b-89c6-3bee-9f9a-6c6c232ada45 | -19.87992 | -52.96538 | 2025-09-23 05:14:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d50cba42-61f4-3f4b-9215-5a1ca3eb1403 | -19.73816 | -54.41956 | 2025-09-23 05:14:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab03e196-0b65-3183-9e8e-cd9f4026f6da | -15.94685 | -59.48302 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03590525-43c2-3878-ba55-76134c8ff639 | -15.31351 | -59.42198 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37bcd2fb-8759-3762-82dc-7a9bc555a7b7 | -15.95346 | -59.48412 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c55bd23e-0d92-31cd-917e-64ab207e3284 | -15.83109 | -59.59212 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 696f9315-dbb6-339f-9483-07be7f05a789 | -15.78682 | -59.48259 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9c94d46-a14d-3792-b179-7e193f9bc211 | -15.94741 | -59.47947 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 765df795-559a-364f-8196-655d38751c2a | -15.36209 | -59.17454 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef44825b-bb6e-30d2-98b2-8f731feeda5f | -15.84168 | -59.5025 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbd1fbe-fe13-3349-8ccd-f24a4ef90a34 | -15.35713 | -59.18467 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73237a17-e7b8-3257-85a6-5b1828461ea5 | -19.88463 | -52.96585 | 2025-09-23 05:14:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b220c903-f2bb-3fb3-9897-5370b39623f1 | -15.74505 | -59.4465 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82750c26-5904-35c6-9f7e-90597da6c078 | -15.95676 | -59.48467 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9d5a916-bc42-3224-9264-c615d009017f | -15.34556 | -59.19374 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b9304f3-8151-3568-b48d-581648654965 | -15.36098 | -59.18166 | 2025-09-23 05:14:00 | NOAA-21 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1adb4a3-4c51-3d0c-be12-f47665e83901 | -14.77088 | -60.22702 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d912be9-ddbe-3a7d-a615-00dc5da20ee0 | -15.94355 | -59.48248 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e71d1800-070c-30f7-8e11-966be0cc3bc3 | -15.41202 | -58.78285 | 2025-09-23 05:14:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd71de87-1482-3baa-b6a1-fafbd02a53bf | -16.00739 | -59.48582 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eec24322-4577-3806-9c79-d7091cecb9ca | -15.83825 | -59.58965 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69f2a098-deed-3da6-812f-2a46265cd37f | -15.943 | -59.48604 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13a84576-987e-3e35-bb2a-70551647fe75 | -15.96667 | -59.48631 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd663d9d-debd-36d8-8868-d4a3270a1fb9 | -15.28322 | -59.41724 | 2025-09-23 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 753cd174-c4ef-32e2-ba16-008ad6e9821d | -14.7068 | -59.8391 | 2025-09-23 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fde25623-dbe7-31d5-89ed-8569499a1936 | -24.20876 | -50.42284 | 2025-09-23 05:16:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 829101aa-7b21-32de-81cf-75b9baad846a | -24.20913 | -50.41836 | 2025-09-23 05:16:00 | NOAA-21 | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2130d47f-b8cf-31d6-83f0-dcffb3ae5a59 | 4.3339 | -60.71085 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 251cae3c-434b-3649-a490-b95aa0ab04f9 | 4.25888 | -60.87899 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6256bc31-7721-34da-a6d4-5b75b63bf36d | 4.31729 | -60.73125 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a01f6458-ba82-3de4-982c-166a16fe6593 | 4.30786 | -60.73635 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09a9ab03-5cf3-3cda-88e2-fda9aeff4b9f | 1.12257 | -59.59294 | 2025-09-23 05:36:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a8100d-5ea0-39e5-a323-5cd49c7c56d6 | 4.30728 | -60.75422 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26358d04-7eb1-309d-88e1-c7fb9d3a4e71 | 2.41144 | -60.70719 | 2025-09-23 05:36:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 691ac239-5770-3523-978a-ba8c24657b38 | 4.31119 | -60.73582 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97d3bc9d-826c-35f6-926d-5139f75fd3f0 | 4.30673 | -60.75076 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98bb5fc5-c066-34e1-9660-7241fb8ba6a8 | 2.40809 | -60.70771 | 2025-09-23 05:36:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 901da05f-f899-3d8b-ad5b-84fec2e432dd | 4.31784 | -60.73475 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f971992-0881-3cda-8972-75ae3e3a1c50 | 1.12319 | -59.5968 | 2025-09-23 05:36:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb310004-e50f-36cd-af0c-9371ea6110a4 | 4.34111 | -60.71329 | 2025-09-23 05:36:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5650878e-4cc9-3564-acab-fb8e9ccd3869 | -3.64407 | -51.9099 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b14ec9eb-f712-39b5-b025-3dd3768e11a4 | -6.52074 | -54.87386 | 2025-09-23 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf8154b6-3f46-3e25-9dba-f05eb382b147 | -3.35657 | -59.43597 | 2025-09-23 05:38:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f34486b-7e05-3dd8-b2fc-1638580fcc8d | -3.63235 | -51.91191 | 2025-09-23 05:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4a35cd40-7ddc-35bb-8b55-350617c23041 | -3.19424 | -54.97867 | 2025-09-23 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82a4d9ca-6174-3f54-926c-442a1aa2f30a | -2.36578 | -67.21555 | 2025-09-23 05:38:00 | NPP-375D | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c393b4c-4ffb-39e2-b73a-b4d096a79571 | -6.33579 | -56.19259 | 2025-09-23 05:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README22.md)
