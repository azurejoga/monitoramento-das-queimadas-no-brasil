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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02734bf2-a13d-389e-8ef3-a135268e85e6 | -9.65497 | -46.23389 | 2026-01-17 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 852333c8-852e-3a2a-b8cd-1011f41b07f0 | -8.10293 | -45.68413 | 2026-01-17 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06c9f7ee-9f5c-3be1-a673-fb1139209637 | -6.70475 | -43.06372 | 2026-01-17 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ba9082e-5abb-3fa8-857c-059725ef5628 | -7.25675 | -43.06214 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 956d7d93-a697-3994-b87f-44c3d67f2c25 | -8.42526 | -44.01753 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22feacdb-148c-3f22-9bb4-5017a9751b7e | -6.94635 | -45.85179 | 2026-01-17 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 824d235c-4913-3a4f-ae21-f9639a732197 | -4.73585 | -44.4453 | 2026-01-17 03:55:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1d3c131-23f0-3ad8-96a3-97cf0148f439 | -6.22376 | -44.16091 | 2026-01-17 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f76be8d3-2ce9-3351-a78e-ea4af98c5ae4 | -9.65862 | -46.23693 | 2026-01-17 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40eaed47-2dc3-35aa-a853-5f114987f73d | -5.82001 | -37.9198 | 2026-01-17 03:55:00 | NOAA-21 | ITAÚ | RIO GRANDE DO NORTE | Brasil | 2404903 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 399579a5-9e6f-3b2d-848e-b7fe050dcce9 | -5.5668 | -45.45376 | 2026-01-17 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80d17485-68c1-3511-953b-6754ae7a3f8b | -5.37915 | -43.19344 | 2026-01-17 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7388376-d714-3c08-a63b-4abbef0ca931 | -10.41428 | -44.88643 | 2026-01-17 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 173abbd9-df69-34cc-8006-3e0dcdb7b8fd | -5.87038 | -43.58798 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f9b6037-10c4-3e7c-a73a-39f44be0565b | -10.41363 | -44.89017 | 2026-01-17 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e097c9ad-751b-3965-8605-81ab53c772ab | -10.55941 | -44.31921 | 2026-01-17 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e6a132f-975f-31b5-bfd9-5c92a2f1c59f | -5.21357 | -37.29023 | 2026-01-17 03:55:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03d6bd54-5d1a-335e-a842-f97a867a0409 | -6.16656 | -40.55369 | 2026-01-17 03:55:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fe6b3132-b9d3-3c30-bb63-16977a9c124b | -8.43731 | -44.01954 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa5a120-4132-3604-814f-d195a8952dae | -8.43367 | -40.39467 | 2026-01-17 03:55:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 25a8ccb5-7d0b-376c-9c85-5e0f2dd11910 | -6.22377 | -44.16445 | 2026-01-17 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72847e7e-205b-370b-a299-cba09538e0b7 | -8.43269 | -44.02235 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f272596-fa1d-31e9-92f5-42bb07cc3869 | -9.65413 | -46.23853 | 2026-01-17 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3aa9dcd5-2096-390d-9546-b57f0ab5fe1d | -9.65406 | -46.23607 | 2026-01-17 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59941305-def5-32d4-b9d4-e38211e22ab8 | -6.04959 | -44.11347 | 2026-01-17 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3a013ef-b0a7-3876-986d-d39754381cd0 | -6.90351 | -42.84317 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 659327d1-7de4-3749-980c-e8fb5a8f0db8 | -6.9606 | -46.22116 | 2026-01-17 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6006094-5f4a-324e-bcb2-b3e7d60930fb | -8.09843 | -45.6833 | 2026-01-17 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a57d755-40f5-38d9-acb6-e9fb8e911717 | -6.08337 | -37.31763 | 2026-01-17 03:55:00 | NOAA-21 | BELÉM DO BREJO DO CRUZ | PARAÍBA | Brasil | 2502003 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c41dccff-3c2f-3a9f-933b-506a5ebf6978 | -5.92721 | -43.40022 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e44ee9f6-1349-3d81-b265-dea37f34cbdb | -5.37573 | -43.18927 | 2026-01-17 03:55:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 895225d8-dd41-34a9-8ec9-407657d9c4c0 | -5.30973 | -45.16747 | 2026-01-17 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0283859f-d5c8-38d6-9e8c-fa0d86f1f54b | -7.82261 | -40.6139 | 2026-01-17 03:55:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b4fbfa1-152f-34eb-a88f-1a5e555aced5 | -10.33863 | -36.71283 | 2026-01-17 03:55:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| daf95d6d-4223-3e7b-b9be-351ea4188421 | -5.9278 | -43.39669 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b3031a11-ec25-3f25-8c53-33f473fad762 | -9.50519 | -36.89195 | 2026-01-17 03:55:00 | NOAA-21 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b8ab4f7-dc9c-3525-8b64-72e8a2ad63ac | -6.89808 | -42.85216 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 47905c97-5b30-361a-b881-1d0fb53c1e82 | -9.64949 | -46.23532 | 2026-01-17 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0908c97f-5ede-3d50-b4b6-0d84a8992735 | -3.32762 | -42.86329 | 2026-01-17 03:55:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| deec15d2-85a4-301b-8815-b2a368031515 | -5.81947 | -37.92326 | 2026-01-17 03:55:00 | NOAA-21 | ITAÚ | RIO GRANDE DO NORTE | Brasil | 2404903 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 91986b92-51f5-300b-aa02-92f1607fe37b | -4.2572 | -48.8429 | 2026-01-17 03:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f57a256-699d-3c1c-b805-45759921dd5b | -6.3441 | -39.62365 | 2026-01-17 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 185d4c79-6722-3c0e-b4d5-d9314fdf98a2 | -5.56785 | -45.45522 | 2026-01-17 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b5aaac9-3173-3cdc-86cd-7c7ec999d19b | -9.85327 | -44.71447 | 2026-01-17 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecc9c700-903b-3591-a1bf-09a75b9bd9e1 | -5.93644 | -43.39439 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| decf405b-d514-39e8-919a-4c7edacface9 | -6.54627 | -40.50963 | 2026-01-17 03:55:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57a6e8e6-3ee3-32fd-8c92-244500df29b5 | -8.88365 | -44.78194 | 2026-01-17 03:55:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a894c80-94e8-3882-9e69-815b08dc1b6a | -9.85739 | -44.71515 | 2026-01-17 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c73596c-1ace-3948-9e5d-77376b9da509 | -8.98662 | -48.07997 | 2026-01-17 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b996ee1-c6b1-304c-b83a-0d72ef778fb9 | -5.93123 | -43.40084 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c175541-0b10-3681-b7af-319054c9c10a | -8.43671 | -44.02301 | 2026-01-17 03:55:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5b06570-5c56-3f06-9fa1-30166a95db93 | -5.93584 | -43.39792 | 2026-01-17 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0d92f21-c536-34d4-a3ea-4fe405174394 | -5.44442 | -37.64395 | 2026-01-17 03:55:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 742e1f6c-0996-386c-af08-9539637abaf7 | -5.30892 | -45.17222 | 2026-01-17 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a8110df-f384-3f6d-8832-4aee210ca738 | -5.45717 | -44.70243 | 2026-01-17 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1b4b039-5c8f-39fb-8902-185455ddfadf | -6.90431 | -42.83841 | 2026-01-17 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 666e8b73-46ba-3a46-9adc-da435ed47951 | -8.23648 | -46.24963 | 2026-01-17 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c28997da-5cd7-3968-ae9a-70871a8c3d32 | -17.14477 | -42.83225 | 2026-01-17 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf55c62b-937a-31e8-b588-216f8a771b46 | -16.41002 | -39.75218 | 2026-01-17 03:57:00 | NOAA-21 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e88e0ae1-5ade-3adf-8667-a236ac77a271 | -11.40467 | -41.41087 | 2026-01-17 03:57:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d9711aa-ad74-3da1-84b5-5eede5dee888 | -13.52886 | -43.52454 | 2026-01-17 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fe3014f-81d9-3e80-9421-e2e7ec1f047f | -10.61147 | -44.64304 | 2026-01-17 03:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f32bd6b-eec9-3d5c-9927-abde3f39bceb | -13.2308 | -39.60404 | 2026-01-17 03:57:00 | NOAA-21 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74b9e0c3-de60-3dd1-89b7-f824b72f4bec | -13.70326 | -45.47509 | 2026-01-17 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 092ae186-c8e9-3b79-aa33-91f40bd75510 | -13.50164 | -46.70546 | 2026-01-17 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e665584e-bfa4-3d9d-8a40-d344049fe307 | -12.50171 | -46.34362 | 2026-01-17 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d79ca4e-7c6d-3423-a2b7-a3083dcdbcea | -15.89078 | -43.45126 | 2026-01-17 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| be5f03fc-85cd-30c4-9566-e7086864e7ed | -17.76465 | -47.06062 | 2026-01-17 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15affc14-ef45-3f0b-922f-a5fac5f1f837 | -11.53428 | -47.6974 | 2026-01-17 03:57:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b137a8d1-84a8-3bee-8463-80ab342fad55 | -12.08446 | -43.76736 | 2026-01-17 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4c3d21d6-43b5-35c5-bb08-29d689a4c9fc | -12.49113 | -43.804 | 2026-01-17 03:57:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d13dc060-fdc8-3bde-8b57-3e729fa864f6 | -15.05447 | -46.85259 | 2026-01-17 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51f87c28-a22a-3faa-adfc-b688676327cc | -11.80342 | -45.36438 | 2026-01-17 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0078a8d9-db92-3af8-9523-9617a28684dd | -12.09267 | -42.80826 | 2026-01-17 03:57:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| be6a608e-8a53-3caa-9f51-4c4edeba44e5 | -17.28093 | -42.64907 | 2026-01-17 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 601a1105-da43-38c5-aa80-c3950e181eb8 | -12.62458 | -43.24876 | 2026-01-17 03:57:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d6e3e96-77e1-3cfd-8018-9fd7526a09a8 | -14.78413 | -45.94744 | 2026-01-17 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f3bac222-2e08-3f64-b186-410d3dbdde56 | -11.8041 | -45.36055 | 2026-01-17 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b83f340-2cf8-331b-81fd-14a08b49a04c | -15.71324 | -46.51836 | 2026-01-17 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94c9d2ea-59b0-3bee-b27e-b285e26aaa97 | -14.7705 | -45.92924 | 2026-01-17 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba02388f-f4e6-3432-be1a-3cc87905957b | -15.8936 | -43.45598 | 2026-01-17 03:57:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 80dde232-752a-317f-baf4-27112eddac27 | -11.83888 | -49.20262 | 2026-01-17 03:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b81cd983-2a46-3510-a0d3-afadc8dcd24d | -11.81654 | -45.36278 | 2026-01-17 03:57:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31172583-595e-35d4-8972-4d7e429b3021 | -13.74567 | -43.66262 | 2026-01-17 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d3d55be-f0ad-3f64-a3ef-6c5ee16aafbe | -16.05598 | -39.12842 | 2026-01-17 03:57:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9e645862-a6aa-3a82-89bf-f3e4377d3395 | -15.92955 | -41.89971 | 2026-01-17 03:57:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91ad2936-7ffe-3cbd-900d-a28cd82174b5 | -10.77917 | -44.42534 | 2026-01-17 03:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b254c87-5704-378c-9ccd-fe945af9b9eb | -12.82776 | -38.43511 | 2026-01-17 03:57:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8328385f-a1fe-311c-9a8a-31bba7ac5ad5 | -14.48272 | -44.33287 | 2026-01-17 03:57:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f9f5eac-6b26-3c6d-a831-2b94274bcd27 | -11.52941 | -47.69653 | 2026-01-17 03:57:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56d67261-9673-3da9-995f-866d2d94300b | -11.01608 | -45.25497 | 2026-01-17 03:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c03f2a3-6799-3e58-ae94-19d91d5bcbdb | -13.50603 | -46.70634 | 2026-01-17 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 31e654da-9d3d-37c3-b59f-b53667cdbc68 | -14.78072 | -45.94288 | 2026-01-17 03:57:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 25c123b7-c289-3f47-802c-3e5ea2675e93 | -11.83673 | -49.20068 | 2026-01-17 03:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6993f857-17d0-3583-b0b1-7d78603640d1 | -17.61239 | -46.65809 | 2026-01-17 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4267c14e-49d4-3a0d-886d-899cc8b59877 | -11.28763 | -48.73078 | 2026-01-17 03:57:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92cdeeba-6313-3c56-b4cd-f55b5c670a53 | -11.32452 | -44.49276 | 2026-01-17 03:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b661600c-f5c5-351c-a089-5af97ac8a8d1 | -11.83952 | -49.19922 | 2026-01-17 03:57:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 786a0aa6-c2a4-3da6-b7f8-c65842c13aa0 | -12.49652 | -46.34724 | 2026-01-17 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46f54bad-5bc6-38c6-85a4-6e4cc423faa6 | -13.69921 | -45.47435 | 2026-01-17 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
