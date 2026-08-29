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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b7c2a8f-2e2e-3a92-8376-b7fa9111a549 | -9.9708 | -53.9419 | 2026-08-29 15:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| c094352e-d329-334a-bda1-02a90831f7bd | -11.7167 | -54.5244 | 2026-08-29 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| e63e4372-c805-3b32-82f9-d2e59084f29c | -11.2446 | -45.3267 | 2026-08-29 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 866fa16d-d934-3d4e-b3e5-d8b3d832fe1c | -6.9303 | -45.6931 | 2026-08-29 15:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| debd08c5-4c2c-39c2-a97a-b53b33b93283 | -11.2877 | -54.0522 | 2026-08-29 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 34f1b51f-85fd-3e13-9cd9-ff1efaed2f83 | -9.6022 | -55.128 | 2026-08-29 15:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| dc8a117c-0208-3818-8790-e16a1b89e3ca | -17.5992 | -51.6247 | 2026-08-29 15:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 72ff60ac-b195-3791-bc75-60787b0e88a6 | -12.2093 | -50.5386 | 2026-08-29 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b0f44fcc-9b3d-3193-b76d-16c5d746d7bf | -11.1913 | -51.292 | 2026-08-29 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| fdec530a-c107-328a-849a-c5ee542c308e | -14.4 | -52.565 | 2026-08-29 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 947c251b-7674-3fd3-ba09-72530369ac07 | -14.3863 | -50.0565 | 2026-08-29 15:10:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 97131a73-ff0e-3ef1-917e-06c66dbcf27b | 0.1367 | -60.412 | 2026-08-29 15:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8da1e58c-0e1c-3f2f-b428-312726acb1ea | -10.8215 | -50.6519 | 2026-08-29 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 5d8b0c08-34bf-33fd-ac2d-bc2357d0cc80 | -7.9169 | -61.3671 | 2026-08-29 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c25af6d2-6247-3793-8730-dee61b22a122 | -11.0254 | -57.2237 | 2026-08-29 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9766a885-c65a-300f-99df-bf69b379c0aa | -10.8653 | -50.2203 | 2026-08-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| caccfce2-3776-33a4-bef3-5a62cfa8659b | -10.3391 | -49.9762 | 2026-08-29 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 464ef778-c48e-3144-9398-3e10225c0ca3 | -8.7767 | -49.9977 | 2026-08-29 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 04366738-a34c-3774-b7ee-9f34be3dd45b | -6.6315 | -43.7533 | 2026-08-29 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 670e59c6-ccab-375e-ae12-36eeb7dccaf8 | -11.0057 | -49.6677 | 2026-08-29 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 00894430-27d6-3380-8367-6234ccc3f746 | -11.269 | -54.0334 | 2026-08-29 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| b8de55f4-6525-307b-8e4a-213070471a22 | -13.4128 | -51.7997 | 2026-08-29 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 31a748dd-7e2b-3a06-890f-d5944d18f8f2 | -11.1726 | -51.2728 | 2026-08-29 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 1740fcca-c85a-34a2-8d74-994a34fb16cd | -11.2687 | -54.054 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 030b9fd5-8689-33a2-9ddb-1a4f9a70dd7e | -10.8996 | -46.6216 | 2026-08-29 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 7c01e747-bfbc-31cf-bad2-0e3b63ba33df | -1.2541 | -55.7101 | 2026-08-29 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 709d8398-4640-324c-9b94-648cee310546 | -8.7582 | -49.978 | 2026-08-29 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 37f2cbd7-6c49-3b1c-a72f-17e09ec3875a | -11.0247 | -49.6656 | 2026-08-29 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 02a2eeb2-f0bc-340c-87f0-d3c3130b6f81 | -13.8752 | -54.1153 | 2026-08-29 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1823157b-141f-3773-8564-2ced2fb746df | -11.7165 | -54.5449 | 2026-08-29 15:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 26060b52-7bd1-32a2-a624-a2badbd7f49c | -7.0057 | -59.2575 | 2026-08-29 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4ce76849-f46b-3a1c-b9a0-1cc9b2ec8218 | -11.2506 | -53.9941 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| dbb74dd8-caf5-3ed7-ae73-60b4ea5c655d | -12.9027 | -45.8612 | 2026-08-29 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 2ea73624-6142-3864-a098-d664ce5589a9 | -14.4649 | -52.1538 | 2026-08-29 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| df2449cb-3eca-312f-9081-21c8eacef4de | -11.2125 | -54.0181 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 8e3287bc-8fda-318a-846a-49985ff919a5 | -10.9402 | -50.2764 | 2026-08-29 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 14ffc7a7-cc5d-3cef-ae88-e1b2a4120fa9 | -8.8184 | -49.6308 | 2026-08-29 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f15f7c47-02a0-36cd-9b29-feb8452ca944 | -3.6216 | -60.547 | 2026-08-29 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| db4997c0-c0b5-3515-bc3c-4597b8adf98e | -6.6129 | -43.7317 | 2026-08-29 15:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f090f4c1-531d-36d5-b89b-c7c5a1c06362 | -7.5478 | -61.3056 | 2026-08-29 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| f9a6b9e8-156f-37f7-ab5e-e54dbc1a4a06 | -10.5404 | -50.4683 | 2026-08-29 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 491d4cbd-db85-344c-8e61-60906b3fc681 | -10.8164 | -54.0129 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d755c9c6-e4fb-3421-8df5-ad3fcdf1615e | -8.7584 | -49.9566 | 2026-08-29 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| af9b7e2d-a955-37ce-b26c-b66e3a25a63a | -7.2995 | -49.9464 | 2026-08-29 15:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 464f1b6f-32fa-3a81-850e-5a6b1536f414 | -7.1001 | -42.2044 | 2026-08-29 15:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 26b402f5-eccc-3cb5-a20d-7530472a3fb8 | -3.9363 | -59.3381 | 2026-08-29 15:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 13ed5990-fc5f-30ca-a08a-1e449f767f30 | -11.2317 | -53.9958 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 125.0 |
| f8d0313e-0e81-34f9-830b-5b6420eceb1f | -10.7596 | -54.0384 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 67e16cc9-e695-3fba-898f-d197416978fe | -8.795 | -50.0387 | 2026-08-29 15:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| af6293b8-0ef2-32f6-8587-1ab3a91783be | -13.8756 | -54.0945 | 2026-08-29 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| abfa1a93-0e51-3547-a625-27c4364442f9 | -11.2128 | -53.9976 | 2026-08-29 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 5e52a030-b600-33ea-80a8-120bf05eada1 | -4.1516 | -60.6878 | 2026-08-29 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 672e43dd-cfc6-33b2-9cab-63d3391193e5 | -9.6024 | -55.1078 | 2026-08-29 15:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fbcc465e-822d-3d50-b9ee-0de7bc00ef9b | -11.0443 | -57.2222 | 2026-08-29 15:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c4b21206-2961-3680-93a1-4dbeebf84367 | -20.8979 | -57.7014 | 2026-08-29 15:10:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 6f79438e-0967-3e91-9660-45138550be55 | -6.9872 | -59.2582 | 2026-08-29 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| fb71f33c-d9e9-3b4b-9cfb-15c7d9e1b800 | -8.6694 | -49.5369 | 2026-08-29 15:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| b2016ae0-72f3-352e-bdb6-5d0ca82820a9 | -11.2128 | -53.9976 | 2026-08-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 58bde609-249e-32aa-8833-8a8d6bed1b48 | -11.2314 | -54.0164 | 2026-08-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 78781847-930c-322f-8113-1f2bff4d6e76 | -10.9859 | -51.0807 | 2026-08-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| a887fdac-2024-3c32-94b7-57ce9203d040 | -20.9406 | -57.5905 | 2026-08-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| c023f467-351c-3805-ad8e-e73e6742bcfa | -10.5601 | -50.4022 | 2026-08-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| fa7954a6-4766-3577-9534-c9e1802b08a3 | -9.9708 | -53.9419 | 2026-08-29 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 5f3bf73c-9c17-35fd-879c-8a25209d82d2 | -11.0244 | -49.6872 | 2026-08-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 475f309d-4a15-30fa-84a4-b866b09df4c4 | -3.9363 | -59.3381 | 2026-08-29 15:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d584db74-0494-3d0f-8fe3-27f835440189 | -10.7407 | -54.0401 | 2026-08-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e00940b0-9932-3b17-9a6b-eaee7e9408f4 | -10.5598 | -50.4236 | 2026-08-29 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2a78812b-d8b5-32a1-8935-94ef7d18a528 | -10.9592 | -50.2744 | 2026-08-29 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 55de0cb7-8bc4-3a30-bc3f-2fd3b05086bf | -11.0054 | -49.6893 | 2026-08-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 489a0b9b-0256-36af-9ce7-537bf3b1a9f1 | -11.1723 | -51.294 | 2026-08-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 60b79b0c-e7f7-32d7-9e8a-1d251a466a1b | -11.006 | -49.6461 | 2026-08-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d9a5cb08-ff64-3058-a316-625be9c215c9 | -9.6024 | -55.1078 | 2026-08-29 15:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 667e3010-602f-35bb-a7cf-0660e9f63095 | -6.6129 | -43.7317 | 2026-08-29 15:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 326a2c9b-6d4a-3b5b-8932-8e8a3633bcda | -6.9872 | -59.2582 | 2026-08-29 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| a908ce71-7b32-3a21-a21f-0de4dd4b8751 | -11.0057 | -49.6677 | 2026-08-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| abb695e2-ff47-35de-b227-e8f742acd9a7 | 0.1367 | -60.393 | 2026-08-29 15:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 4e48c69c-c273-333c-92b2-16ca9824d142 | -10.9673 | -51.0614 | 2026-08-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 93856d37-6344-35ba-a98a-17fcffda9c7e | -8.7947 | -50.06 | 2026-08-29 15:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 343c66c2-f9b0-325c-9bc7-0e6158a9d444 | -7.9169 | -61.3671 | 2026-08-29 15:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 78346efc-c0de-310d-92ea-cc7f7968608f | -8.631 | -66.5473 | 2026-08-29 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dbe9a304-2178-3958-99ff-40c70d97e742 | -8.9481 | -62.3704 | 2026-08-29 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2a330c49-defc-3ed3-97b0-f42ba7aba8ef | -1.2541 | -55.7101 | 2026-08-29 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b84d232b-62b3-3074-a116-8a2d614fc011 | -14.3182 | -51.7046 | 2026-08-29 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 636a0374-64e9-34d5-831d-582df1b65398 | 2.256 | -50.7511 | 2026-08-29 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.6 |
| f1d5c647-09e4-3a07-b70c-a5ae8e46e43d | -14.2989 | -51.7072 | 2026-08-29 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 271b62e3-7c42-32d8-b8df-0c9a361bcb0f | -9.006 | -65.4 | 2026-08-29 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 95510f06-329a-35e0-81bb-2b72b445f86e | -7.1001 | -42.2044 | 2026-08-29 15:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| de708a8a-0f61-38a5-8bc8-0a51372ceec4 | -11.1729 | -51.2516 | 2026-08-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| eef841e3-f2ba-3338-a40b-e6c666d38f23 | -11.0247 | -49.6656 | 2026-08-29 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 83f99e44-2d93-3812-8158-ea4923d86275 | -10.7596 | -54.0384 | 2026-08-29 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| ec71f89e-8cee-321e-9626-b7f365b2258c | -8.5216 | -54.8612 | 2026-08-29 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d47f52b8-76c2-3e39-8578-a626ac2813ef | -7.0034 | -59.643 | 2026-08-29 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 54aed7aa-08e9-38f0-8257-d0dfd6895c50 | -7.2066 | -42.7634 | 2026-08-29 15:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 2d904d99-1ed5-3f10-8e19-3684e64cd89d | -20.8979 | -57.7014 | 2026-08-29 15:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 1ac09b40-50a6-36ad-ad95-d50bc7ae7eb9 | -9.971 | -53.9214 | 2026-08-29 15:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 170.7 |
| cbcf326c-7d56-3560-aa16-31a87eb02837 | -8.9478 | -62.4084 | 2026-08-29 15:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 16717eb0-7b28-3f2f-82e7-ec81e6ef48fd | -11.1916 | -51.2708 | 2026-08-29 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| be76efe8-96f6-3dea-b603-99061c378e32 | -11.7165 | -54.5449 | 2026-08-29 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 584fab3b-0be3-31d9-a0f5-1d874bd84d37 | 2.2375 | -50.7515 | 2026-08-29 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 1c5edede-dc5c-3d02-89f5-98d90b16060c | -7.0057 | -59.2575 | 2026-08-29 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |


[Clique aqui para ver as próximas entradas](README85.md)
