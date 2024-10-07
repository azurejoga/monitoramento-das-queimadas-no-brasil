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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67a05b69-7fe8-3e76-b0df-e3fa97a2255b | -17.91105 | -48.614 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4845b997-5600-3b61-abc9-4d70d6e50df6 | -17.90608 | -48.61794 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72eeb853-c56f-384d-90c1-6ec3e7e5de6e | -17.90328 | -48.60382 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fd942b6-cb3b-3f50-995e-c5f3ac7714b1 | -17.90273 | -48.60837 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0f1455d-ebb1-3ee1-909e-b450a551ca7d | -17.89884 | -48.60334 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef981446-fceb-3bca-b940-3f3f6e5d8b4f | -17.88393 | -48.61522 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57898bfa-4ffe-3fe7-9092-bd8def831ca2 | -17.8795 | -48.61469 | 2024-10-07 04:55:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1f90e38-4dbd-30f3-8e13-6900f8ee7654 | -18.64263 | -48.6662 | 2024-10-07 04:55:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fb307fa-0f6c-321a-b9c1-c098a8ca63a5 | -18.90756 | -48.19299 | 2024-10-07 04:55:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9de0e0e1-4d5e-3701-92df-905bb52cf91a | -20.76104 | -49.47903 | 2024-10-07 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| def7c2b6-4f83-35a5-8fcf-bdbfc631d63e | -20.75996 | -49.4762 | 2024-10-07 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f14ebe58-36d6-3d45-8713-7c7e6ce57c5b | -20.75943 | -49.48058 | 2024-10-07 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 5a76b46e-c902-32c6-83fb-2d7a39c83447 | -20.75508 | -49.48003 | 2024-10-07 04:55:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| bbb3ec1b-5033-3ed5-b319-31df5d5c71a7 | -20.71345 | -49.64288 | 2024-10-07 04:55:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 3cada2fc-cabe-33e9-9e28-c8f8b1fad9dc | -20.71294 | -49.64714 | 2024-10-07 04:55:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8fecc30d-b37b-3285-b44f-86e3e8d12557 | -20.70864 | -49.64659 | 2024-10-07 04:55:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fb0cd824-c2d5-316c-9528-f437b024814a | -20.60133 | -48.49001 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdf615fd-c1c9-390e-b762-7ec2e91b75de | -20.60076 | -48.49506 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da6d24cd-a72d-3881-a7aa-dac799b74cd0 | -20.59209 | -48.48863 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d53326b5-716a-3533-99ee-cf4f67288434 | -20.59042 | -48.50363 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1772a350-24ab-318d-9433-c7bacddff54d | -20.58692 | -48.49289 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8b0d504-c6c5-3b15-9eb2-0afa48f6aa95 | -20.58637 | -48.49788 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cae1f47-cf99-3b1a-8edf-fcd9da632d0f | -20.5858 | -48.50295 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 86cdb2b1-aad1-32a7-bbaf-ccce2af4b944 | -20.58523 | -48.50813 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d9665b80-fd62-3276-a7e6-61439af6e3aa | -20.5806 | -48.50763 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 520b33fd-b065-3d6d-a564-3f85466da897 | -20.58003 | -48.51276 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e1c450d3-ccb8-373b-8131-0ace7d2c30a7 | -20.57598 | -48.50691 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3b572fa7-1bc8-3fdd-925a-69c2017f8996 | -20.57542 | -48.51201 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d7b1b999-d0d7-3f61-9dad-83465133ed7f | -20.57487 | -48.51699 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 944b3f77-60e5-30f8-ac15-2c22047ed692 | -20.57082 | -48.51122 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 28.7 |
| a91e38cd-c477-31be-ae19-ef52c2f5a36c | -20.57026 | -48.51624 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 28.7 |
| e5cf1875-a3b0-3e2d-a693-0b57a4b748a6 | -20.45415 | -48.64065 | 2024-10-07 04:55:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b28c0cc-88ed-3a47-b659-e34520af291e | -20.35093 | -48.80884 | 2024-10-07 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 36.4 |
| acbdfcc8-9e42-3ce1-9ce2-210d496c0394 | -20.34696 | -48.80349 | 2024-10-07 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c80409f6-c95f-3ef7-8573-e79d9f64148a | -20.34641 | -48.80829 | 2024-10-07 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 12e97049-8060-37fc-b69d-beb6235a54c6 | -20.34586 | -48.81309 | 2024-10-07 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 36.4 |
| cd1e3c65-bc5d-3bd2-aa4a-4c18bf4baa86 | -20.18714 | -48.72895 | 2024-10-07 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c0648fde-6c3e-34a0-adc2-04d17d5bf983 | -20.18262 | -48.7283 | 2024-10-07 04:55:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e649a63-69b5-3d84-9b88-a87dc95dc976 | -21.2963 | -48.81132 | 2024-10-07 04:55:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c5bdf9ce-87a6-3af6-98be-3a2044ff2922 | -21.15588 | -48.94555 | 2024-10-07 04:55:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5b30a09b-bd87-3b4f-8c9b-14d59c4f7c9f | -21.15534 | -48.95048 | 2024-10-07 04:55:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 82f4804b-f4cf-3c69-89b0-8901a3d5b02e | -21.15419 | -48.94775 | 2024-10-07 04:55:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 801283e2-06b7-3020-abe7-01b7bd6f15b8 | -22.28637 | -50.00109 | 2024-10-07 04:55:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec2060ce-3894-3b98-924d-bc681b2be2c3 | -22.00135 | -49.45408 | 2024-10-07 04:55:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 24a6e1f4-45b1-317a-9e0f-2a9ea1bbc25b | -23.77164 | -50.14931 | 2024-10-07 04:55:00 | NOAA-21 | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8232e1e8-ac7a-3c47-b98f-472791636ab0 | -22.53885 | -48.81213 | 2024-10-07 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a5ac0b7-ef63-3491-8219-b35f38eeeb05 | -23.14478 | -49.81036 | 2024-10-07 04:55:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cc3aa28f-93f8-362d-8680-0c8714ac22f1 | -23.14422 | -49.81534 | 2024-10-07 04:55:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9ba000af-c5f5-32c7-91cc-08615ec65a1d | -23.04202 | -49.84866 | 2024-10-07 04:55:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 0dc713da-4536-3cee-be98-4eed1211fbff | -23.0415 | -49.85323 | 2024-10-07 04:55:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 1d34c730-064a-311e-9ddf-2012ddec188f | -17.64285 | -53.05652 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b62b8c0e-42de-32f0-9805-ced7fe8d51f7 | -17.62432 | -50.19798 | 2024-10-07 04:55:00 | NOAA-21 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| decefa63-328c-35cf-8f0f-ab7fb2fa81b2 | -17.62361 | -50.20334 | 2024-10-07 04:55:00 | NOAA-21 | TURVELÂNDIA | GOIÁS | Brasil | 5221551 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a35d18a8-9110-3bfc-ba54-c8d28c88acf0 | -17.26437 | -49.21815 | 2024-10-07 04:55:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71bc4893-7c9a-3f01-bd55-85b5fa4281d8 | -17.26386 | -49.22221 | 2024-10-07 04:55:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8941678-18cc-3a6b-b969-3c46f65bb353 | -17.25964 | -49.22169 | 2024-10-07 04:55:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71aa1121-516a-3a3f-92a7-1f29715e5316 | -16.72818 | -49.16983 | 2024-10-07 04:55:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ca45575-336f-302a-8dc4-910a98aabde7 | -18.11618 | -50.15497 | 2024-10-07 04:55:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e1c1569-f66c-34d6-b537-71e3b82e9a97 | -18.11217 | -50.15438 | 2024-10-07 04:55:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b4afc3b-99bf-3a0b-bb30-4ab5f7e7bbeb | -18.10815 | -50.15382 | 2024-10-07 04:55:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7c128343-4f87-39a8-9436-a5e81baabacb | -19.16941 | -50.63447 | 2024-10-07 04:55:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63347f47-ca2e-3889-95a7-b305cf1427a8 | -19.16873 | -50.63976 | 2024-10-07 04:55:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37112ba3-b118-3016-8abf-068edf1c7b0f | -19.1641 | -50.64439 | 2024-10-07 04:55:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b2a6856c-3d5b-3b29-90f4-354ef02a50b0 | -19.16152 | -50.63316 | 2024-10-07 04:55:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 32f3fe0c-201c-3595-a9ef-ecd3f8736568 | -19.16016 | -50.64378 | 2024-10-07 04:55:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 56179d75-28a5-30c6-85a3-fc8a09c72c22 | -20.19313 | -50.96613 | 2024-10-07 04:55:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 42b533fe-26d1-3e62-b7b7-bcaf2905cd21 | -21.20192 | -50.97884 | 2024-10-07 04:55:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 5232e39e-6c74-369e-94ab-80645a809ef8 | -23.06132 | -51.45466 | 2024-10-07 04:55:00 | NOAA-21 | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 706e83c2-2550-3f4d-80df-56557c914725 | -23.05736 | -51.4541 | 2024-10-07 04:55:00 | NOAA-21 | PRADO FERREIRA | PARANÁ | Brasil | 4120333 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6b5f4cbd-5436-376b-9a4b-6eef5267b5f5 | -17.63429 | -53.09123 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1dd0bb50-0b73-3c22-b7d6-7d374e06f37e | -17.9952 | -51.62241 | 2024-10-07 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d3d2fed-e6cb-3d47-b062-6bd70356477d | -17.14366 | -51.70782 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3fb47785-6753-393e-a12b-23d12c7fb98b | -17.14307 | -51.71212 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b864ab70-6d68-3517-b566-fcd2fad1c024 | -17.14248 | -51.71645 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a964552b-c37a-32e1-a94d-e5fcca42c8cc | -17.13945 | -51.71154 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 9c0dbfce-1d52-3e5d-842f-eaef4c5559c5 | -17.13899 | -51.70916 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 91514319-e959-3f42-b505-4090a5afbd55 | -17.13885 | -51.71587 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d82273e7-7b3a-3f70-9cec-6f4f5992af5b | -17.13838 | -51.71347 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 70a870cd-13a0-3e8c-8cdd-eef4665f2d66 | -17.13776 | -51.71782 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 552b766b-7b72-30c4-a58f-536abec5d5e3 | -17.13582 | -51.71095 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8a4590a-e391-31ea-b31b-d7cc05165b68 | -17.13523 | -51.71531 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| de3d6bc1-d444-3b20-9790-7d048eddade4 | -17.13476 | -51.71289 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 2981474e-c4bd-39f3-ba5a-fe4dded1be15 | -17.13413 | -51.71727 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c07622dc-7edc-3760-b228-8845fce1a326 | -17.13279 | -51.70605 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a67866ed-31b6-3816-9abc-b2504b95bb95 | -17.1322 | -51.71037 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7068fb2f-d07c-312b-a366-537435e5f98a | -17.13175 | -51.708 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3b6bf1f-2892-36e0-9073-db0267f76992 | -17.1316 | -51.71473 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb2290a0-2280-3357-8eeb-5b61f674b812 | -17.13114 | -51.71232 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6439598f-8e9d-31f2-821d-ac5b8ff2cb2e | -17.12751 | -51.71175 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2c925b0-66c8-3834-9da4-6e56d4eadf97 | -17.12441 | -51.73358 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bee1b47-4029-39e5-915f-95aeee530889 | -17.12326 | -51.71558 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2cc9bc1-6e19-3294-99f9-78e09058f17d | -17.11178 | -51.71824 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 51.3 |
| c7f9454e-04cd-3a7b-a153-0b56648c22b3 | -17.11116 | -51.7226 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 79fcce9e-64cd-3323-a272-497a5c3d9510 | -16.675 | -51.7426 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71379d99-7e8c-38db-87cc-94cfcc83223d | -16.672 | -51.73779 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3979d32a-1e17-3509-9d8a-d5f851cb0f6c | -17.24326 | -50.71489 | 2024-10-07 04:55:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0b95074-3774-30e2-b9de-5c3cfb39ebcd | -17.2426 | -50.71976 | 2024-10-07 04:55:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 613d82ea-ac44-3c98-a2b2-428cef791f1a | -19.39617 | -51.68909 | 2024-10-07 04:55:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db3e0aab-938e-36f6-83fd-0d0e5c1c6457 | -20.99568 | -51.79425 | 2024-10-07 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e7d7a3fe-3033-3ef4-9d50-dfaf73b62ae8 | -22.71913 | -53.22561 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README92.md)
