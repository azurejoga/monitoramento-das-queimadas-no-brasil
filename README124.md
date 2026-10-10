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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 751760a0-50d6-3dde-b2c4-47fea2fb31b9 | -2.40158 | -51.30143 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62911101-30c4-3785-a240-a471a9343855 | -7.24085 | -55.21387 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39cce095-db23-3814-b9fb-b13b0332b18c | -6.42832 | -55.25972 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a13ff6cc-3904-38a8-a905-ce559f4dd364 | -5.08014 | -60.22176 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43e0f895-5dbe-32b5-bb7b-44e141f9ff81 | -3.24957 | -54.03082 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4010fa5-c2da-3cfa-a6d9-8f378d4e4624 | -2.74817 | -54.10729 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c251c373-7a4f-3f1a-a98c-8febbb58c996 | -6.48743 | -55.96759 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 021fb5e8-182f-3e83-b66c-ab341f78a727 | -5.99114 | -55.3595 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5b0efc7-1655-3486-af9f-3127546ec975 | -3.30326 | -54.01495 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7b2f89b-cca0-3924-a8cc-0a9b5c40eaff | -2.45155 | -57.89207 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8f481275-127a-3a74-9eb6-6d1efc327fbe | -4.09781 | -53.99624 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27ddf39a-75d3-39a1-8f00-9ff37dfcc469 | -3.984 | -54.45572 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 086bc293-3e50-3c7b-9dbe-282eb460c76b | -6.45363 | -55.50238 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4271e163-062e-3b89-ad57-d840b75f4991 | -3.5669 | -54.68569 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8f0641b-fb4f-3d42-a32f-8241cb0cd320 | -1.95246 | -54.41005 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 675b6191-5cf5-39e6-842c-f8cc9e30f44f | -3.31652 | -54.03821 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86eed3da-4944-3575-9a96-855003134641 | -3.18158 | -50.57546 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de540496-e829-31d0-b117-eef266e80b1c | -3.90029 | -55.89255 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f8d0a77-9e39-37f6-a57a-c146a6326888 | -6.42589 | -54.95497 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20faf4d2-9518-3787-8677-7d6e03f44a69 | -2.93925 | -54.08108 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c936871c-d496-3816-93ad-92266e81b47c | -3.10268 | -53.93002 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 585f206c-e5d6-358a-bfdf-232f9aebfc3b | -2.98741 | -54.78207 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22fa9899-cd73-3899-9479-0fa06e9706e1 | -1.20572 | -55.68309 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 218f36dc-5e18-3ea4-9386-59f89a2a0483 | -3.20414 | -53.86852 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd36ba3-4b46-38d7-b5a6-c2b0785ec8a7 | -3.54739 | -54.74376 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b3fa741d-8276-3916-a29a-4f67975daca0 | -6.46177 | -55.04995 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d1d1e58-665b-396d-984d-42c5109515a4 | -1.63577 | -54.41439 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09de7576-31e6-35ba-a865-7f6ace793521 | -6.218 | -52.64206 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 717102a0-8094-3558-b1f7-b62497b402e9 | -6.49151 | -55.28778 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03a2be48-e833-3a44-bb3a-aa5c1cfe5359 | -2.73327 | -54.13684 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cab403a-ac85-3fda-b6fa-660f04961a83 | -3.32786 | -50.78009 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5371c4f4-bbf7-3cf1-8233-eac9b03e98ea | -2.99867 | -53.92096 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58572459-586e-3dea-9d42-7a16962c5677 | -1.95804 | -54.39654 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0afd1f58-d91c-3723-8c9e-0a796722b557 | -5.18524 | -60.1877 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 246a42bf-64b6-3a5a-b302-b4738e199368 | -3.58189 | -54.69886 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3ebc462-b304-3b07-a902-3ac01ed4cb35 | -3.76332 | -58.84253 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24011ed2-d9f0-39e4-9b07-680384a138b4 | -1.62405 | -54.42337 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ac2e32a8-45c0-3dc6-8ed7-d9f07379782f | -7.00004 | -47.71129 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9510474d-51b6-38ba-94a1-93204cd67f5d | -2.5726 | -48.25157 | 2026-10-10 05:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60e29822-c805-3a96-a2e0-7d657a1b1db5 | -2.40101 | -57.90208 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3061ad8-7fbb-3354-8bae-04e9620d390b | -3.00985 | -54.04275 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1eee65e-fcb0-3735-95a1-042be6f45296 | -2.43522 | -55.99226 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e49fcd1a-6dc8-38cf-a749-f8491f92b9c5 | -3.30767 | -54.00858 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 056c9072-5b9f-394b-a34b-f5c1d5526044 | -1.53689 | -51.60518 | 2026-10-10 05:04:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 871336d7-497f-3329-9aa4-3bee4ba4df20 | -7.23265 | -55.15891 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd598dc2-c1e9-3105-b0e7-489c5855e467 | -1.18659 | -54.18166 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6c950e2-3e2e-313d-8dee-e1fb90559e0d | -1.28837 | -55.71186 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adb71308-8626-3002-ba1b-cb6ea5c88fb2 | -7.56511 | -45.64426 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b21c8272-3a45-37e7-b33b-0cf3e3dcc407 | -6.1651 | -52.75356 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ebeb56d-352f-3152-9e5e-f7ab0887e49a | -7.03943 | -47.66394 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6502e312-9ae3-34ea-8c01-5477d5492913 | -2.49228 | -58.08522 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 166dd88e-4e05-3567-9ce7-737bbb78bf6e | -2.94551 | -50.49651 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6310a730-97ac-331e-b620-e90c48db8f28 | -2.51569 | -56.14488 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7126fd07-cbe6-3991-809b-1c4870b12ff5 | -2.94031 | -54.05295 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ee53a87-d52b-359a-b501-b3c6c6d5bc0e | -6.07206 | -44.66642 | 2026-10-10 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7707548-c0b5-3854-994a-562e4150b64b | -2.5148 | -57.23906 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7722f27-d8d0-33cd-b414-e2277f1071c3 | -7.10188 | -46.71706 | 2026-10-10 05:04:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 29b9a7be-fbef-36a0-a905-fa3ddd81bde2 | -3.27741 | -54.07091 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31c3af63-89ca-38b2-851e-6a81887011ad | -3.80608 | -49.93213 | 2026-10-10 05:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| de103e41-f7b7-39c7-965d-b96e3c5487ce | -3.26727 | -54.06891 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cfabd9b-35be-3fc6-a77f-eb68f3c8fe4e | -3.07872 | -54.27298 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a62f7242-7e5a-3ea8-88ef-9aa124ede0e2 | -4.11063 | -54.62154 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feefe5d3-775e-3076-bed4-720a00bf9aa7 | -3.77979 | -59.24979 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 12ea70c9-6f9a-3e83-a8a3-231d79101c51 | -4.34842 | -59.95482 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c5e793f-41a1-30a9-9eb9-727845fc10dc | -3.06096 | -53.93426 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e12d4e7e-3893-382d-899f-a05900a60173 | -5.47921 | -60.26693 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 012a1632-6c37-3043-ab83-1183c7304f92 | -5.60193 | -47.27969 | 2026-10-10 05:04:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 543ba298-66f6-381a-975c-33cbb255708c | -3.87658 | -55.84282 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18dd3c22-0671-3da8-accb-eb41c3116099 | -5.79053 | -53.79778 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64d7d9f5-300f-3488-985e-a7fa17609f1d | -3.11841 | -54.17282 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e53961b-d47b-373b-9094-17727fd90cbd | -1.10948 | -54.15532 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba99b802-1b1a-3fbc-b133-0f3d9fda0600 | -8.3606 | -48.14616 | 2026-10-10 05:04:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00607be6-d245-3dcd-8e4b-4992fd4c24b9 | -4.11285 | -54.62903 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb5217cb-ada3-3d0f-9964-5b178a98c735 | -5.086 | -60.22189 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e15dd76-76a2-3ecb-bb4f-8d288a4e6298 | -6.04922 | -59.92075 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f8f06a0-1e04-3b30-8021-caf076d5b728 | -3.22451 | -54.29601 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76c5b5fd-21f2-3004-a8a5-abaaa0cfecea | -3.07472 | -50.96318 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a346a95-719f-3d9a-8f0d-06fb7d8276b8 | -2.79145 | -51.40576 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d1a6a85-e2c2-35b4-bd35-4c1230f9fbd9 | -3.59079 | -54.55692 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73f2840f-dfa3-3a99-8630-3d8103eae9cf | -1.02323 | -52.42791 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4ba440d-37db-3513-98e6-f40f596cf540 | -4.72616 | -55.66225 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b858eeac-fead-3dc3-a1b2-dddb2d754360 | -3.90448 | -58.94899 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 029be382-59d4-3e8a-9884-f0586c0a137b | -6.53042 | -55.25803 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a4ee2c4-f71e-316e-9397-f7bf7992ee74 | -3.90201 | -55.8162 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92de838a-a3ec-30d9-b487-81468255aac5 | -5.9356 | -57.73738 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3303a497-9458-3ef7-9485-1229192e6ca2 | -3.84783 | -55.9112 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 655b793b-67bc-33d7-98ea-59b42dc1ef9a | -3.94195 | -55.33102 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e99efdf7-e20e-3390-ab72-f46779518073 | -3.65609 | -55.46828 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c00d8772-3a50-3e26-ad96-116f0fdcb5b3 | -6.99939 | -47.71586 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 83d32392-0068-3f7d-86b9-9c1b60c0c3f3 | -2.88571 | -54.0762 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b6162a5-33cd-39fd-b49e-2558c8fba81b | -3.27818 | -53.99999 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5706f220-e98e-371a-964e-af7b924c9fe1 | -5.221 | -60.05123 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99795b81-b436-31ce-87e2-2eeba7f6b4ca | -3.31376 | -54.03425 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5de642e6-36e4-33b7-b37e-435bffda97b3 | -1.89394 | -53.98693 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c32597d0-57c3-3954-ab28-08aba750fde5 | -3.29838 | -54.08835 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4cd443e4-fabc-3aba-b9ae-257dd30133f7 | -3.65034 | -59.17088 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8538fb01-8f8d-3b11-ba9a-334e784879ea | -3.93405 | -55.72618 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a58ed74-ab48-37d0-8714-f41477137144 | -3.10435 | -53.94086 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d031865-94bf-3eac-8dce-aedaa97deb2f | -3.63927 | -59.57557 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44c7058e-1ca1-3d64-92fa-ab573a81c7ba | -5.69664 | -53.4659 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README125.md)
