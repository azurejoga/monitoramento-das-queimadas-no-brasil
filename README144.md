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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbb41c9f-ca1b-32bc-b46c-4913ee84eef3 | -15.67767 | -45.95114 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 309f8a10-1fc4-38f8-a681-c49c05e0023a | -15.40718 | -52.71131 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 72292974-00c0-353a-82c3-200a87d4b843 | -15.04946 | -41.22239 | 2026-08-31 16:48:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| e77c4898-8d85-382f-b204-1d6d28021b8e | -19.22153 | -57.33681 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 6511d15f-0e2e-3d54-b5bf-e10c3ad76bfe | -19.12202 | -57.37414 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.1 |
| 66748113-2533-31db-a930-8605534c3a87 | -19.19553 | -57.35469 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| d5bc479a-e87d-3687-8101-38f4d098f817 | -15.16506 | -44.00119 | 2026-08-31 16:48:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| deef582e-9fd9-300b-ac36-efb45ddb183b | -17.23193 | -53.26829 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dd08574e-8535-343f-aa13-7e2ea2201e92 | -17.30271 | -46.95937 | 2026-08-31 16:48:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eb2f350d-c3ce-3171-b57a-ce3f9e820bad | -19.18364 | -57.35589 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| c8f7e3fd-c814-3b5c-ad1e-41c310334517 | -17.53531 | -52.54846 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3d3dedd6-08de-353a-a017-f825efbd93e6 | -15.45669 | -53.96786 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b535aa59-4a78-30b5-b72e-c585324c8bb8 | -19.15219 | -57.40496 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.6 |
| e6dfde6e-8ba0-31e5-b60c-0a3059211c65 | -13.43427 | -43.8512 | 2026-08-31 16:48:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 449d1397-1610-304e-93da-6a1a0162ecd7 | -15.05928 | -48.00412 | 2026-08-31 16:48:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e74982c4-8731-3f86-8a93-cd54ae1d19ac | -14.56766 | -53.5896 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c85e65b0-c596-3645-915e-2d95e400554a | -15.63942 | -56.38318 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ed16fb8d-a6ac-3cc4-8643-fd45cb2d84f9 | -15.02573 | -48.16888 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5018904c-31fe-3d55-846e-4ded215dc268 | -18.26133 | -52.73001 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5e8ca061-d74e-323e-93cd-8bd8d6d39580 | -14.96754 | -54.56339 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a5511ab0-52a0-37a3-8bd2-76f21bfa08ce | -17.13812 | -55.95226 | 2026-08-31 16:48:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 440f7218-e0a9-37fd-a6c9-f3d325188cc9 | -16.28709 | -42.58095 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 46cc1a96-8909-3ab1-a8ae-bbe4cf29f8e1 | -15.62996 | -56.41574 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7d8b65c2-af37-38a8-8af1-6a08bdd806b9 | -17.8943 | -52.09268 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 7de59571-5dd9-30c8-8af8-dac2b630c772 | -14.79174 | -48.26104 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1fdb4fbb-5bc0-303e-b851-6c8607cd6e95 | -19.2312 | -57.35109 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 51af1d34-330b-3440-bae9-d283ae53b5f7 | -15.21967 | -56.35638 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 73f703cd-932e-33d8-b36b-8a17a86cf84d | -15.78116 | -47.79875 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 5c537b76-d9c8-315e-9c6f-1aaa08631d65 | -19.17389 | -57.3798 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 4700d722-2743-3c6d-9771-cef59b32edb1 | -16.68963 | -49.89359 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 657c15b6-4b95-3d04-b644-28b5167421c9 | -14.59481 | -54.12041 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4dc94ca5-91d5-3ca7-89a2-966b68f096fe | -17.53007 | -41.31792 | 2026-08-31 16:48:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| f8008e93-1dae-3446-86b3-ed3edf33df57 | -16.17546 | -47.94738 | 2026-08-31 16:48:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39e4cbe2-1f07-34c7-b509-16c04473bae2 | -15.5006 | -56.0111 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d61e14c4-5c75-3109-b9bf-b3e6eac1042b | -14.96345 | -54.56887 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 92bfdcdc-9b0f-3866-b548-37a6e7b1fe93 | -14.97004 | -54.58358 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 241.9 |
| 5cbf770f-3dec-3179-a073-3d29b8a8f54e | -16.7192 | -52.28561 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8c4c996d-a856-3767-9e08-edb514f3b393 | -18.17017 | -48.62491 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| bff7d32e-310f-3bbe-bccb-156f475f76a1 | -15.21549 | -56.36718 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| bfe5c927-b93d-3474-a237-96e5a2597001 | -15.97348 | -55.95871 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 5050a8d3-983a-3a03-bd65-2a790af8d8b5 | -14.47852 | -49.04046 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e3cbdd36-8e86-38c9-8e89-c78285efaec0 | -19.12627 | -57.38467 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 6b4d963f-791d-394b-965a-985be6fab799 | -19.17475 | -57.38887 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| e910f753-f63b-3faf-b9cb-600d06054c2d | -15.61132 | -41.51817 | 2026-08-31 16:48:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 02ceb774-a631-3f6f-85c6-57a04520f8b7 | -16.9971 | -51.84269 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 53d0a913-bc28-3469-8bd9-949c5309157e | -14.49967 | -40.33547 | 2026-08-31 16:48:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| 9f1838e1-f3f7-3044-82af-79f06050f142 | -15.02961 | -48.17199 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 728eb3e0-3dc1-3d9c-abca-db5833111cb6 | -14.56198 | -52.07519 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 28eabf3b-eabe-3a37-98d1-9c613e408e81 | -16.97573 | -53.28776 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ddc19c93-c425-3ced-b9ad-c89879c3923b | -15.643 | -56.38602 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 24aa951f-b2f2-3f5a-a170-e2639fb9cac5 | -19.18113 | -57.3928 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.5 |
| 65de875a-3b64-345c-a69e-c58cf23e9e03 | -12.61975 | -40.31223 | 2026-08-31 16:48:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2597d292-c8e5-374f-9529-e6fb0f07342b | -15.45779 | -53.96563 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7e151b51-0676-3254-b203-a1eba4f6123f | -16.4448 | -51.40474 | 2026-08-31 16:48:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a34de925-76fc-31d2-b20e-4a93125860bb | -18.2734 | -52.68464 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d2cea29e-3460-3b3b-8d48-a0ea574de86a | -17.95368 | -44.57415 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 5a82d9e2-320f-331f-bbf9-94587974c144 | -17.85883 | -50.50307 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9794813a-0633-3040-a37d-7c69afc6e7f5 | -15.24391 | -56.3804 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 47a922d4-94cb-352b-82f6-5a8f0ebe1fb4 | -19.20191 | -57.35862 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 2bddf4d7-dc03-3113-a6b1-18d2d53346b2 | -15.20818 | -46.22528 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 21d93c45-5a1d-31eb-ba4a-d40a7d5eb06b | -15.40583 | -52.71211 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 442bfa19-1481-35f2-bd38-beadc18ac7df | -17.86676 | -52.10811 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 164.1 |
| fe1630db-e4e3-3148-a0f9-c343eca7b108 | -19.2367 | -57.34597 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 77df6474-195c-34f8-aab7-3423398b7e03 | -12.75551 | -41.17101 | 2026-08-31 16:48:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fbf6b823-cd3b-33c6-948f-e76a0920d11b | -17.89479 | -52.09653 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 599e8aba-9c61-3b9c-a450-84116106eb5c | -19.20104 | -57.34958 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| c81c7dbe-8e83-318e-ae61-eebedbcd54ba | -14.41878 | -41.46598 | 2026-08-31 16:48:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 37c0763d-614c-3832-9f91-548e4cb48e41 | -16.89779 | -40.21696 | 2026-08-31 16:48:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 28a30821-e6b1-3cb6-85ba-c9a21b5bc2fd | -15.99398 | -55.95288 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 497c1d01-a8d5-3d7f-a6b1-0e513119a69b | -17.13775 | -55.94886 | 2026-08-31 16:48:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| bda30b35-4bc4-3209-9460-72e6ca308f7b | -19.21046 | -57.34709 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 1ce4b8ec-ec58-34c2-bf3f-e1c32395f309 | -16.14241 | -52.37263 | 2026-08-31 16:48:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27144336-3709-33f0-a0fa-c0d5004cb588 | -17.38602 | -44.85991 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| de8d90a8-676b-366c-b2c9-97d6d7b8cef2 | -14.95857 | -41.39615 | 2026-08-31 16:48:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c565a3af-83ac-362e-b4da-ea836d0bf145 | -19.1013 | -57.40827 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 2ea89579-39e1-31da-9fa8-ae4d6478db6e | -16.07803 | -48.02255 | 2026-08-31 16:48:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9a3fd166-710c-3b04-bb50-71d11d4073b6 | -14.81808 | -55.72263 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dc1c941-d3f1-35ec-b032-80ebc7d95169 | -17.87456 | -52.10315 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 309.5 |
| 7cee10e8-b280-3c3b-ae18-d27f2273138e | -17.88237 | -52.09829 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 36c2ff60-3d15-3098-961a-274eaca1f163 | -17.7901 | -44.15343 | 2026-08-31 16:48:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6f0c13b-6b97-3342-a40b-71a94218ffb2 | -16.29006 | -42.57556 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5cf60fd7-a676-3a07-aba1-51191aed9d7d | -17.87674 | -52.08709 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| c5f3e997-47db-3a23-961c-c41e451ec69b | -19.10506 | -57.38496 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| e6091270-9060-38c1-82fd-b8f6d05c30aa | -15.62164 | -56.41705 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 966c7038-603f-3137-b7bf-8fef8505696a | -19.10969 | -57.3708 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| a407523f-e8a9-3538-846b-38b62a842aee | -19.13181 | -57.37954 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 3b64fbf1-14bd-3a6d-a926-9938d86f0eac | -14.4809 | -53.33766 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2ee3a9ee-1fe4-3bbd-b7ff-7595006d63a7 | -14.21428 | -48.64141 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8669f1db-95dc-34bf-ba29-a0c64123170b | -19.16411 | -57.40372 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9898946c-ad6c-3c7b-8329-5e9115105385 | -17.7564 | -45.39598 | 2026-08-31 16:48:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7f2375a-90a1-34cc-bfb5-a10dc9a5ba6e | -19.12669 | -57.38921 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 1aa0a1ed-42a4-3cea-87dc-9dee37493aef | -17.85194 | -50.50891 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f6ef2da4-87b9-3218-b232-a502689a8a02 | -19.13514 | -57.41592 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3cc66527-b79e-348c-bc7e-59cc6267dc7b | -19.83852 | -49.36056 | 2026-08-31 16:48:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 8c558e97-7883-316a-80cd-50b93079aa97 | -16.98013 | -53.28702 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 36411c06-f62b-3ebe-95c9-67d41c654198 | -18.21035 | -43.97691 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 005850e6-c707-313e-a70a-604fce787aaa | -14.50054 | -40.34019 | 2026-08-31 16:48:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 1ce48463-84cc-32c6-8ad6-19079bf52612 | -15.42611 | -52.69345 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0c8e2f1d-5f48-3bc2-95a1-69f4a5d1d707 | -18.26685 | -52.70298 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 5a8cf193-0bf8-3518-ba72-a2232b447bdc | -16.35898 | -51.01183 | 2026-08-31 16:48:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README145.md)
