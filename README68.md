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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ce633f9-0d94-3115-a221-e149e869be8f | -11.64515 | -47.49216 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 452d1f03-9083-37a9-bcd3-1053fd0360fd | -12.46384 | -47.96134 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54441ff2-0715-3920-a752-e882eb1006c8 | -13.61869 | -48.03032 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf716f34-4941-3903-91b9-4a374ee11a4d | -13.76271 | -47.922 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9975cf12-c6ac-3158-885d-a458d7873f38 | -11.43761 | -44.95168 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a8c79c1-8ca1-3f38-8de0-0ab3e85e4f83 | -10.07559 | -45.63988 | 2025-09-30 04:40:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27e7a26a-e7bc-322f-97f7-90544ac642a6 | -9.09569 | -45.8512 | 2025-09-30 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c9ad608-f929-3ca4-81a5-441e54275dd2 | -7.11506 | -45.06409 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5ac6841-0ffc-3651-9ec3-ab8cbb189503 | -9.20317 | -45.93813 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ff99d5e-015f-3b1f-8798-66feeb5cdeb5 | -13.01366 | -49.44573 | 2025-09-30 04:40:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c7ba8f6-665a-3911-9667-7b7cdfb09f12 | -9.01004 | -51.71273 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08fa2564-71c3-333f-81b5-99dc31ac321e | -11.3033 | -47.08285 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcfd8323-f54e-37d0-a83c-85a90b48ad98 | -14.38536 | -47.13513 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73d5052d-8c01-3183-86a4-db334ae2065b | -11.25358 | -47.22277 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dc99437-0ed9-39ba-9692-a1bb1cddc113 | -10.10614 | -47.78451 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bb9c6a0-e81c-3f55-bd40-62fd8b6aa2b1 | -10.88472 | -53.75086 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d3f8748-72e7-350d-a0af-9776a8245d98 | -9.51074 | -47.6953 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a5e9fae-161a-312e-8a7b-f6d58986cd66 | -8.20327 | -48.98833 | 2025-09-30 04:40:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40b8f9b5-3840-30ec-a55a-3bb0e505d694 | -13.23225 | -47.31068 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 73bbe2df-f5c6-37c6-8a5e-2cf9ae64c9aa | -6.89635 | -46.9465 | 2025-09-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7898cd84-7e5c-34c2-a14a-7b6facf6291f | -13.3881 | -48.0741 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9d66c81-3888-32bc-bf20-2ad3f36391f6 | -11.16089 | -54.11523 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| afd8b4b0-ec48-38c4-b694-5a5156702d81 | -10.13844 | -45.30036 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75307a58-75a1-3577-b33e-7c573ff10470 | -12.2351 | -47.79679 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 08ba2360-701c-3eed-a31a-486977758516 | -11.19991 | -47.22928 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 752ac871-ccb9-35ee-bc21-49eeab134e0c | -13.21493 | -47.32626 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 269dffca-dd0e-33ff-bdaa-b483aa9f997d | -10.64087 | -53.69544 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6c8c557-f2c1-3806-9d00-1f5691f2f1b4 | -12.96098 | -46.8722 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 084aec11-0010-3266-a81f-5fca82383c7b | -11.74313 | -46.8482 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7efc8ac6-de39-323c-bbc8-8f69d2fa5eb5 | -8.98659 | -47.52005 | 2025-09-30 04:40:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8198402f-a26f-32ef-8cc4-47dcaf8fcde9 | -10.11257 | -47.78946 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24d1827d-b238-3d24-acd1-9cfee9f498ea | -7.21853 | -46.60409 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fcbb899-151c-373f-9899-50d366e0eab1 | -10.63368 | -53.69423 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ddfc3fb-58c0-3c47-9ab9-c55878409624 | -8.72295 | -47.99223 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11e6d032-8280-3cbb-8a26-d68266ab7655 | -10.09323 | -46.07293 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b9e4d13d-997c-3c90-8bd6-9537885c2d0f | -13.0408 | -47.07719 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 490a6a79-a6b0-3a66-98b4-c1d688a8301a | -12.83446 | -47.00441 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 08d06146-9d7c-3fa8-b8fb-6bd29fb52bbc | -7.02034 | -45.2199 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c290efe1-7767-324d-bf96-f5c3ec9b4914 | -13.2393 | -48.44624 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f018e18c-73ac-390b-ad6a-c3a06a1091ca | -10.63953 | -48.5843 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7227f08d-689b-3a19-a68e-7a6050f7e3b3 | -14.44806 | -46.35835 | 2025-09-30 04:40:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 865b903d-7459-3856-b969-8dd392a6d05f | -10.83721 | -45.41168 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd5e2953-e2d7-3e2b-a9b9-2053316132d5 | -7.11864 | -45.52958 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dea5b340-7a76-3de8-b73a-08891d7456da | -7.37271 | -47.05113 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8c8a802-8d2e-3187-b44b-1a9cc72171c9 | -9.29994 | -54.50403 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b01a9c6c-b458-3ae9-bb0c-10a31803a076 | -13.647 | -47.33289 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bfb4537-6195-38fd-8ace-5af38408be0b | -13.0327 | -42.80845 | 2025-09-30 04:40:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48d53677-2c7b-3247-8945-2c32caa751a2 | -8.86434 | -46.67831 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d46a70a0-589f-3828-877c-c81753c63c3a | -10.47149 | -47.95075 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8853d37-6a9c-3498-ba7d-f9d4a6fda3e3 | -11.42839 | -43.5023 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7d82f769-0427-327d-92f8-6a16da1d6a16 | -11.44559 | -43.50746 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9ebfefa-d0b2-3b08-a554-2db64630a4d3 | -9.18811 | -47.74443 | 2025-09-30 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 403f0061-2076-312c-9baa-e5dd3255c4dd | -9.04068 | -46.69888 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70b54380-fe50-3af0-a8aa-8124088665d4 | -11.10924 | -47.72723 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9b2c39d5-e921-34f3-b3ef-97ee06867386 | -7.0471 | -46.41867 | 2025-09-30 04:40:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40132843-4b6a-3062-bda5-07a6a12bb292 | -7.51855 | -45.43779 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4ff8cfa-6a1f-3c3c-9834-11bcb525048d | -13.62875 | -48.03679 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97c04711-3d96-326f-aba0-f3cf2b4523c2 | -11.19566 | -47.233 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 491f44f6-9aa4-3625-8a41-9739012a58c7 | -13.37127 | -48.16451 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36191140-0e91-3556-a64c-7e2021623f67 | -10.88648 | -53.75171 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09078034-3c4c-385e-ae7a-0a757e426cfe | -11.26086 | -47.22387 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e65b2bea-bbe8-3153-806c-9c2f8e63f0ab | -13.82975 | -47.49469 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46b7d7a8-e0a1-3ceb-98cc-3d0cc98b4969 | -7.9149 | -44.61062 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30e414e7-a7b1-336a-ab7e-5e8a35e56185 | -13.22485 | -47.30946 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03d1dae0-417f-37b7-872e-1ae500abda46 | -10.6309 | -48.5485 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27c3a5f7-1134-3c69-91c2-8a0c63e9cde8 | -13.35163 | -47.84267 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b2499a2-0709-3bed-aa63-6998abe89bbb | -12.18322 | -48.3531 | 2025-09-30 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a52f2a3e-a132-381e-8c63-f2a1f88f4eff | -13.39345 | -48.06243 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17af5428-47e0-3781-9197-f50e3c5b6f52 | -10.06662 | -48.19546 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09a7aa59-4cad-36ef-ac38-b6368b4b5d1d | -11.26147 | -47.21951 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7bcd16b-08d6-3760-8288-9faff77d8f1a | -13.81161 | -47.88976 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd8f8f38-1cd0-3f94-b3ba-bcb17672cf18 | -10.38369 | -48.15916 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7964fe54-8054-3229-b62e-a522e4f52437 | -12.22324 | -43.74934 | 2025-09-30 04:40:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e8c27d9-f1b2-3bbb-8d95-8c386702a41e | -10.39833 | -49.04036 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f93fa59-427c-3b81-8829-62b958eba590 | -7.82356 | -46.7767 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8640d3c3-ab68-33ea-859a-9efb3363f2f1 | -8.07428 | -55.21928 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c587d79-1bf3-3fcc-a4fb-6da746379c15 | -7.86729 | -47.25487 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb891b9b-5ee0-304e-a24e-70a2cfe9f0e3 | -7.47668 | -47.08256 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f821c34-346b-3442-831d-9b48a0b644f3 | -11.43081 | -45.03161 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bf84586-48f2-39a9-9b32-b0fb487d038b | -8.89921 | -50.59194 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f12d8038-bcce-316d-badc-155b18271f4b | -11.46241 | -44.98825 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9abba5ed-2901-3a26-a977-5da322de860b | -13.34921 | -47.83374 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89a170ed-6c46-3b89-8817-318e39f1b7df | -11.1594 | -54.12394 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 69dd78e3-66bb-35df-ab1f-95172f6ddc33 | -11.46023 | -45.00381 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48c189e7-cf57-32a1-a405-655dde794faa | -13.24819 | -48.44177 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38a87cd9-ed9c-3d91-84d6-4df23603f24d | -12.85197 | -47.01622 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| af6b8d00-d7d4-346d-b3bd-c79db140fe82 | -10.40841 | -49.04193 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4235cbd9-76e9-300f-9ecb-46133a0dc62d | -12.69136 | -45.28637 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06258aba-23b9-30fb-be2d-b82cbb9a6018 | -10.60243 | -49.63869 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2307a77a-0d20-35ef-a06f-04076dc76778 | -10.40037 | -48.16581 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49ffad39-b8b8-337d-bd0b-8cb311a214d6 | -10.92665 | -44.32561 | 2025-09-30 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 636388af-34a3-3a72-8498-dd2ad2fe5e69 | -10.2028 | -44.89259 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37f02a81-b675-3c0c-91b8-b02875e3fbfb | -10.32172 | -48.03635 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 563f8a87-bcde-3914-a121-1f06ad8c608e | -11.48727 | -43.51299 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7914dd0e-055b-31ec-a6f4-bbfaecbe9817 | -13.7329 | -48.65908 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ec38e2b-6e7e-3146-a8ab-357a826a20b7 | -13.73876 | -47.89875 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 824c4318-6cff-3276-ae1e-65c8359ad8d3 | -10.63835 | -48.56886 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7023fa93-78ce-385d-9942-2bf398503fdd | -13.35705 | -46.37907 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 69bffaad-5264-3706-a07a-5a023e199078 | -13.45161 | -47.23609 | 2025-09-30 04:40:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35ef684e-f457-336a-b8d1-b87467407ba1 | -8.14687 | -46.36663 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README69.md)
