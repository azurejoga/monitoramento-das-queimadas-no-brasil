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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc60d528-aa82-3aaa-8d02-7e50c6a88e7a | -16.04343 | -43.84509 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d81e09f9-fced-30de-b5be-9f1280aac9e6 | -18.83074 | -42.13202 | 2025-09-16 12:00:00 | TERRA_M-T | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| 735834f4-66a0-39e6-b785-c4f874d451e0 | -14.35225 | -40.7071 | 2025-09-16 12:00:00 | TERRA_M-T | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| c3847521-f5b0-3705-a4fa-0e2f869180a5 | -17.81336 | -45.34469 | 2025-09-16 12:00:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 31af56c0-4f35-3e72-98f1-3b505027fea9 | -19.24965 | -44.16897 | 2025-09-16 12:00:00 | TERRA_M-T | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 54922da2-2070-3e91-8e8d-548b6641d171 | -14.09776 | -43.9073 | 2025-09-16 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 20ef117a-8698-32a0-942a-c86bd5f350db | -12.7011 | -47.98317 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 05786ef4-ae85-3b52-95f2-2b6640f6c01d | -15.69553 | -49.90743 | 2025-09-16 12:00:00 | TERRA_M-T | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 8e394729-b3a4-31ea-a5f6-71bcc1df9208 | -12.6298 | -45.74676 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f7a989a9-fa20-3cbc-b487-9f5545ad5ad4 | -14.16698 | -46.14553 | 2025-09-16 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6196aace-be9a-38f8-8d44-017f07ca7594 | -21.79501 | -45.37043 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 454c3cf5-279f-33b7-82c5-f12e5e8348d6 | -11.92157 | -46.73672 | 2025-09-16 12:00:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2fb7379f-6930-3abb-92bb-c57cc79098f1 | -13.53224 | -42.46535 | 2025-09-16 12:00:00 | TERRA_M-T | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 32.1 |
| 7fbe650b-1508-3c3a-8055-f0abf11efb0d | -18.42125 | -44.28808 | 2025-09-16 12:00:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b95439b2-ff79-32c9-83d5-157353c2e4e3 | -12.09952 | -42.81773 | 2025-09-16 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 44.0 |
| dbbfd528-a6ab-3163-8ada-217d1281eac3 | -18.89248 | -49.5961 | 2025-09-16 12:00:00 | TERRA_M-T | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 3b091642-b0ea-34e3-bb7a-030ee64a6983 | -21.74516 | -45.70628 | 2025-09-16 12:00:00 | TERRA_M-T | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 5f180fb0-c4b9-3d1d-a1d7-50b1fb419ab8 | -12.69582 | -48.01501 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 352.7 |
| b63cf3af-a98e-3b30-a65b-95c82dbca919 | -11.5967 | -46.97018 | 2025-09-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 9d1e1fb6-e41a-3409-9351-fc09e266a5fe | -20.76699 | -45.14632 | 2025-09-16 12:00:00 | TERRA_M-T | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| fc4bf886-8306-3849-a32e-defd2beafa01 | -14.66606 | -41.03976 | 2025-09-16 12:00:00 | TERRA_M-T | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| cfaba2cf-040f-39d1-a7fb-18da80f05858 | -17.81188 | -45.35439 | 2025-09-16 12:00:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3bdada01-4679-300f-a4ce-ce684292f77a | -11.72434 | -46.47857 | 2025-09-16 12:00:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| fe52d2dc-4f49-3313-b88e-0cbbfef97f77 | -15.42167 | -46.13033 | 2025-09-16 12:00:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f83f8c85-ac35-3188-a185-54ac5e2060f4 | -12.64592 | -45.77223 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 9a42cbc8-48f5-3286-9939-27d16e03f0f0 | -16.34654 | -41.46297 | 2025-09-16 12:00:00 | TERRA_M-T | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d99fd2c7-bfc5-3632-a50c-e6f71ed245ea | -12.67475 | -47.93982 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| c207e311-459d-3f80-93eb-ded1b9032238 | -14.62086 | -46.39752 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e081a15e-258e-35e5-8446-ac4390682d2a | -21.06594 | -45.68123 | 2025-09-16 12:00:00 | TERRA_M-T | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6b0a171d-bf35-3c4a-85c4-2e21561e03e2 | -19.86221 | -45.5887 | 2025-09-16 12:00:00 | TERRA_M-T | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| aaf561ed-5558-3b8c-91eb-2cef681c159a | -17.7319 | -46.77007 | 2025-09-16 12:00:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| dc649244-f773-3230-a07e-9b5c2bdba6c0 | -20.66379 | -45.4124 | 2025-09-16 12:00:00 | TERRA_M-T | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d443674-a707-32fc-9b92-7f8988e3777e | -14.6109 | -46.39627 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f666ee32-c738-38e5-a6a1-3360321a13c2 | -20.10666 | -41.38716 | 2025-09-16 12:00:00 | TERRA_M-T | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 92d4b4ae-7fe5-30af-af0b-eb236bec1352 | -14.86455 | -41.68576 | 2025-09-16 12:00:00 | TERRA_M-T | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 03d80800-be79-3bc8-b275-6978a295807a | -21.75928 | -45.35812 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 61d088c2-d3f8-3c7d-a119-b0e8928c3571 | -12.16357 | -42.9372 | 2025-09-16 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6cb86aa2-8901-348b-8c1f-78e925c22ae9 | -12.69847 | -47.99901 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 2e862cc1-f16b-3bfb-a3d4-9abda63afda6 | -18.56022 | -49.25266 | 2025-09-16 12:00:00 | TERRA_M-T | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| aac3d5a2-3435-3177-9d22-ee898889b3a1 | -18.6257 | -43.89585 | 2025-09-16 12:00:00 | TERRA_M-T | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5eb3e1d6-b98b-39a2-ad04-0a265b8dfb5f | -12.64763 | -45.76102 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 76e9c199-5797-381a-a735-82fdebd2498b | -14.32516 | -46.05767 | 2025-09-16 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7878adc6-9018-3c8d-b362-5cac81cecb99 | -13.68867 | -42.85222 | 2025-09-16 12:00:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 56aca9be-f403-36ae-adcf-472f27c896a3 | -12.68505 | -48.02276 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| c82c4b78-3ef0-38ea-97e4-187545204d22 | -20.91103 | -46.45717 | 2025-09-16 12:00:00 | TERRA_M-T | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fb45e701-65c1-37d7-b801-42b7d70e1aa9 | -14.64422 | -46.37804 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 796fd03b-b65a-3b94-a783-a5038419fe87 | -14.97581 | -46.55233 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0efb22b1-1aa6-33b7-88b5-45f8d5ef9bb9 | -12.68619 | -47.94168 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 7b4b4141-84ee-3b7b-b540-96289e63cecf | -18.55812 | -49.25906 | 2025-09-16 12:00:00 | TERRA_M-T | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.8 |
| 44af6204-70a3-3e3f-98ed-2bf5001984dc | -14.61276 | -46.38464 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fdb9676c-3608-32c9-a74b-31bd27a0e726 | -20.91032 | -46.21906 | 2025-09-16 12:00:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| fa5e65a1-f8ea-3276-81ac-b098da53c01e | -14.44126 | -43.76184 | 2025-09-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8307640-2f62-316a-be41-eedcc7674d2e | -21.49546 | -45.89388 | 2025-09-16 12:00:00 | TERRA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| d08891e2-9676-369c-8a48-14b0422d0407 | -14.32345 | -46.06863 | 2025-09-16 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 8b2cec84-67b6-374f-b65e-6cb7b720d055 | -18.57153 | -49.25478 | 2025-09-16 12:00:00 | TERRA_M-T | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 138b6540-b727-3a9d-9c8b-e92d1cdabb7f | -21.23329 | -46.9441 | 2025-09-16 12:00:00 | TERRA_M-T | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d05316cd-a2e8-3711-a105-600210351667 | -14.44259 | -43.75268 | 2025-09-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e7e78309-cce5-373f-8616-3f51d6e3fc27 | -15.83598 | -43.61747 | 2025-09-16 12:00:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 565235d5-45ef-3e05-8d90-52b02a7cadcb | -21.62822 | -46.47469 | 2025-09-16 12:00:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| da5ca4dc-0e3b-3dce-ab72-0b5c6752d53b | -21.5885 | -45.0159 | 2025-09-16 12:00:00 | TERRA_M-T | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a17df4a7-02ef-30cc-9065-fa2589d8b01a | -14.0902 | -43.89675 | 2025-09-16 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 81de1d5f-6607-3852-80f1-fd5f25ca4a6d | -12.63612 | -45.77076 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| ad44b3fb-9b25-3b22-b7e4-5a99d55227a2 | -18.41373 | -44.27742 | 2025-09-16 12:00:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f0c6e77b-ddb2-3423-a10d-25785432cdfe | -12.81097 | -44.74598 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 8691baec-e7e2-3f5e-802f-d7711d6f89fa | -21.30786 | -45.73037 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| a542c64a-4c91-3b5b-87cc-9bd5e3c8b889 | -14.66342 | -46.83962 | 2025-09-16 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5b276fe0-5253-3e1b-bbe2-b7a97b82dd25 | -12.67739 | -45.31028 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 31fe6255-49a7-350c-85c0-09ae6954ecda | -12.68867 | -47.92616 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4f34b9ae-8258-3c97-a37b-908beb43ca88 | -14.97381 | -46.56489 | 2025-09-16 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 816a4076-8708-3868-9266-a573fb84fd39 | -11.1337 | -45.33891 | 2025-09-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c6a66df7-5402-35a6-b0bd-1079b03c5762 | -21.26893 | -45.68406 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| 467089b3-65a1-366d-a449-27dd81df66f1 | -17.09114 | -45.83632 | 2025-09-16 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f580087a-b31f-33d3-a387-310af3f6f8a2 | -12.67354 | -48.02083 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 86a776f0-fd6c-38f8-adac-aec0b50cc6a5 | -13.1326 | -42.09699 | 2025-09-16 12:00:00 | TERRA_M-T | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 41823e88-7854-3f38-aa7d-2b4468166f93 | -14.33316 | -46.07034 | 2025-09-16 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 1557ec05-19dc-36ca-b598-3290cd3ed6b4 | -14.70111 | -42.66868 | 2025-09-16 12:00:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 082d7cd6-9bd0-330c-b500-e5257ebe012a | -12.67725 | -47.92426 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 87f9d2b3-1121-3c53-a280-49f6adaaf9ea | -14.52624 | -47.32077 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 99d07f7f-e76b-38cf-982e-536a8ff40484 | -19.25099 | -44.15965 | 2025-09-16 12:00:00 | TERRA_M-T | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| db6518af-ddda-3feb-8231-786025261776 | -20.90878 | -46.22897 | 2025-09-16 12:00:00 | TERRA_M-T | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 68a1ee79-a250-3068-bee7-c915ece5e593 | -21.57781 | -46.20272 | 2025-09-16 12:00:00 | TERRA_M-T | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| 9faf7d22-bea5-3640-af4f-dac9c1dc72f5 | -19.56361 | -43.77694 | 2025-09-16 12:00:00 | TERRA_M-T | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2cb8d9ac-8d58-3d35-b753-5458e9a54cb0 | -11.7249 | -46.88343 | 2025-09-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4cff0a13-183a-383c-a41a-edea6c67bf0d | -12.44204 | -44.74568 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f1cb9e34-3456-3bd8-bc1e-bb84d547b71e | -14.15727 | -46.14332 | 2025-09-16 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 8e0f0add-2121-3321-928b-3ee7f588116a | -12.69266 | -47.97486 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f6e7240f-821b-3af9-bde7-c431cb9035da | -20.55108 | -47.1106 | 2025-09-16 12:00:00 | TERRA_M-T | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28d8dda6-8582-3ae0-85a1-8592b416d3b7 | -13.68737 | -42.86127 | 2025-09-16 12:00:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| cdcb764e-42a3-3d1b-afdb-090dd6bb0900 | -13.02684 | -47.97095 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c5865d5c-d795-39f1-b745-4dc81bf889e6 | -16.93246 | -44.07143 | 2025-09-16 12:00:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c98760de-a060-35aa-a627-30d0b0504d9f | -11.48664 | -43.59838 | 2025-09-16 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7e8f61eb-ed45-3531-a18f-e9e25be78646 | -13.43703 | -45.89711 | 2025-09-16 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| ce9e8dea-2fb4-3fc1-a649-85acbe7e5c1a | -12.68432 | -48.01314 | 2025-09-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3ae65d41-1cc9-3b46-935c-43322ef24c80 | -16.43399 | -45.67895 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4525c483-3ede-30e0-b3b0-2b8854670c98 | -12.68063 | -45.28923 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| f4df2ef6-3757-33b8-b42d-accec7bbac4c | -16.15421 | -40.34085 | 2025-09-16 12:00:00 | TERRA_M-T | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 16205b8c-d82e-3416-9c52-f1b75a476cd0 | -21.30931 | -45.72066 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 23ba10f6-6781-3eb1-b138-8f336ffff098 | -21.18554 | -45.62456 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a399954c-3e0b-3421-9d61-5d88bdb2d15b | -17.33757 | -41.75492 | 2025-09-16 12:00:00 | TERRA_M-T | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a6946349-e7cc-35e7-b301-6c2935f8e505 | -17.08579 | -45.8288 | 2025-09-16 12:00:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |


[Clique aqui para ver as próximas entradas](README90.md)
