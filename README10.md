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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c253c52-6339-3559-bc6e-ba1c35dd6541 | -13.03912 | -48.82656 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37138bc0-dabf-33fb-a961-5608b48a8e15 | -8.68029 | -48.30282 | 2025-06-26 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 640ca57e-73f5-34aa-9962-2178c977e498 | -10.30265 | -57.13259 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ed38df8c-32ce-381f-a20a-0e0f59ce7a15 | -10.52706 | -53.62758 | 2025-06-26 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21da6cd6-c12a-3350-8cdc-ff2ad6530c16 | -11.07904 | -48.25126 | 2025-06-26 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb21e9de-09fe-3525-bb19-71ef0c4a1a3c | -7.19743 | -43.09914 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 77692c9a-7186-33f2-9931-e1ea889f2b1b | -9.31225 | -48.74268 | 2025-06-26 04:40:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26fccd6f-5818-3d8a-81f1-5595474f6af5 | -10.71623 | -59.13725 | 2025-06-26 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c05179c6-3a19-3379-b737-5c8a4cd96967 | -7.87927 | -47.87495 | 2025-06-26 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6305018-9515-3a85-878c-7ba82a0f8b65 | -13.32077 | -43.3869 | 2025-06-26 04:40:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 811cd361-a643-3b9d-bc4c-fe5d63fac44c | -11.82337 | -47.5484 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21534cbe-5125-310e-a026-39e4bdca06ec | -8.47617 | -48.26072 | 2025-06-26 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d2e82d0-e922-3e66-99da-5089986a09e4 | -13.042 | -48.83097 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ed53e7c-0546-369d-abd7-b18bf2002436 | -9.11872 | -49.43115 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 46ade8f9-14e2-3a47-b9c0-72e48b398304 | -11.61977 | -58.28521 | 2025-06-26 04:40:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 166e6a2c-e597-35e6-9da9-3cd09dca5d89 | -8.06314 | -46.97151 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc7375a7-b743-30ec-a289-2a942f92422f | -8.58144 | -48.21562 | 2025-06-26 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b95c879c-73cd-34b4-8db9-c25c43420dde | -7.98278 | -49.65129 | 2025-06-26 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 459075a5-67a2-3a17-9e6c-907133c65fe3 | -10.87327 | -53.77757 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f66cb90b-f97d-312f-a0ea-1f82ea309ff0 | -11.83659 | -51.26416 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e99da2d5-ee4e-385b-85be-280a5bff43dc | -8.26565 | -47.02082 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20aeab65-22ec-3389-acb9-f2da25031775 | -8.06374 | -46.96746 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a9bb94e-8d2b-3257-bf45-8131834f2634 | -11.0734 | -46.63471 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8546d165-1542-33ea-bba0-53394932f9ff | -11.06832 | -46.64338 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4a18e95-6c9f-3bb7-ac42-f95f1851e1dd | -11.83826 | -51.25362 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb9aab69-8e5b-328d-bc2a-7d459a5a6ece | -8.1431 | -46.82813 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 987306e3-da23-3ca1-9379-4771ea6e343b | -11.08092 | -46.6359 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c127059-9a65-3435-ac99-5d276976a08e | -11.79444 | -47.54416 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88464490-620f-3097-8450-8c5ea0fe781d | -10.06682 | -49.65571 | 2025-06-26 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58fd68b4-206e-38bb-900e-28335a9c09bb | -7.20891 | -43.08243 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| de5b6966-bede-3b41-8ece-9f5791e502e9 | -12.03281 | -47.77497 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc724e30-24d8-3f77-b61d-a32c2283a9e0 | -8.37557 | -51.07016 | 2025-06-26 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 836c39a0-604e-34a2-8f71-6955399e5b02 | -11.8308 | -51.25608 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3323577-4859-3a7b-b9f6-a1045b505557 | -12.08387 | -49.00778 | 2025-06-26 04:40:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 88e96e65-6241-3ba2-b685-f7d50c0c809a | -10.82066 | -53.73829 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d28c8308-4860-34a4-99a8-7b0e126a34e1 | -8.44813 | -49.63287 | 2025-06-26 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83d1e6ab-374f-309e-a948-a5ddec418d5c | -13.05006 | -48.82432 | 2025-06-26 04:40:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c39e5abc-2a01-3014-90d3-25604f0dc9c1 | -7.02492 | -44.56423 | 2025-06-26 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2f9027-b005-33da-9fd6-ef13edf9c6fc | -11.11067 | -46.64799 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44acac2c-238c-3746-b3f7-a53634b4fee0 | -7.20254 | -43.09533 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6ad9f056-5774-3e06-8fa4-d73b98c6e0f2 | -11.11274 | -46.65506 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2e717b8c-c6ca-3027-a686-800319f0a3d0 | -11.8377 | -51.25714 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0834f94-9975-39c7-a19b-e1b84ce88cd8 | -12.76622 | -44.40446 | 2025-06-26 04:40:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 518fde00-b282-3264-970e-f3f05e26d64e | -10.82356 | -53.74306 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5473fb5a-e616-3f6c-8360-e21c92512238 | -9.56898 | -49.10965 | 2025-06-26 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1253274-848e-311b-bcc4-ba9a87d52260 | -8.97267 | -49.86855 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1cbadd5-4cc6-3dcb-bd84-239715f84173 | -13.10193 | -52.29132 | 2025-06-26 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af57873e-2526-3f3a-bd2b-4650b2597519 | -10.7117 | -59.13348 | 2025-06-26 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c0b86b6-b2ae-35e8-80c7-7acfcd93d43c | -11.58979 | -44.63983 | 2025-06-26 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 055f6fa5-d26b-3af2-bdbd-1ef4b19708a6 | -10.24764 | -44.63836 | 2025-06-26 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73689e4c-321e-346f-92d4-f86060b1e3a9 | -11.57116 | -52.09714 | 2025-06-26 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dfba957-df0a-39b8-b616-42dd7bfce33e | -7.97948 | -49.65078 | 2025-06-26 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40372285-5b5f-3a0b-b8fa-1acb4cd252ae | -11.83384 | -51.26012 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe33693f-47a2-3a56-90a3-1f37f20c6a91 | -11.14032 | -53.91503 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d5e7963-9b9c-30cf-a3c3-51aad7e19508 | -11.81112 | -57.35936 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| acdb59e5-e397-3144-a043-033ef6b04d7c | -11.08534 | -46.63189 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6157f027-ab34-3494-96c9-0ad1cd3218c0 | -10.79562 | -49.66874 | 2025-06-26 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 281c32df-b28f-3a8e-b279-ca78c7b6b201 | -7.20442 | -43.08179 | 2025-06-26 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0e46dd45-9a29-3305-b21d-3fbbaff76f9c | -10.06748 | -55.5541 | 2025-06-26 04:40:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce282506-2550-3d5d-8312-2dd7d6dc1045 | -8.71657 | -47.85552 | 2025-06-26 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79ead5d6-ca3a-3d54-a9d2-569deb1a4ee6 | -8.33605 | -49.23635 | 2025-06-26 04:40:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3e161d0-301b-3218-8537-a0d648bf9813 | -9.3335 | -47.82689 | 2025-06-26 04:40:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5867255-b2e0-3e25-ac9b-81d43417f925 | -9.56952 | -49.10608 | 2025-06-26 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d50d068-ac3c-3efe-80f5-b64d535a72c6 | -7.02439 | -44.56796 | 2025-06-26 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1886732-42af-377c-8d45-68b9d3f45291 | -8.97321 | -49.86508 | 2025-06-26 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41dfcc28-ca3a-370c-9aa1-fc21ea219b3b | -11.58435 | -44.64754 | 2025-06-26 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d45aa25-dcc1-32e3-bb78-a3ac0ed24f53 | -9.85398 | -44.70241 | 2025-06-26 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 72174e30-b3cc-3d75-85a0-89a63d7cd13a | -8.26267 | -47.01632 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4f6d9328-3849-3f28-9ae4-3e1d6ea0f0d6 | -11.83715 | -51.26065 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8531cc2-08cc-380b-95ed-f5f84166f7e1 | -12.04604 | -48.07757 | 2025-06-26 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dde99a4d-0755-3055-8773-8e22e35d7ce4 | -6.33114 | -47.33406 | 2025-06-26 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 395448ae-ec60-37bc-88d0-84728746d3fb | -10.86249 | -53.7757 | 2025-06-26 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7341f39f-03b2-33de-9b61-3055d6d9c769 | -12.34221 | -49.31306 | 2025-06-26 04:40:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25ac740b-49e1-3164-94bf-d1f7c98dd191 | -9.12096 | -49.43869 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 82efd7de-1cb5-3d02-b974-0503333275b2 | -8.47956 | -48.26126 | 2025-06-26 04:40:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 11bf4130-4e4e-3a08-8eb9-1e057a799470 | -9.2898 | -56.24391 | 2025-06-26 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6db5ee2-5afa-3db1-85a2-f24ee65b219b | -10.18953 | -48.76045 | 2025-06-26 04:40:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2c341ca7-bdd9-3736-a0d7-5a67bc6f5282 | -7.11164 | -47.84892 | 2025-06-26 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0bc30645-adc4-3b30-a50c-29cac96bdd1c | -11.11342 | -46.65037 | 2025-06-26 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9505a6b2-5ac1-3590-b3ee-f5115cfd2bce | -7.1088 | -47.84463 | 2025-06-26 04:40:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51f11195-1836-3d98-b621-d1bef05f69f3 | -11.83495 | -51.25309 | 2025-06-26 04:40:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64b51f47-bc52-3e81-9a53-c9f92e2542fd | -11.23578 | -49.49976 | 2025-06-26 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5a04c2f-116e-35e8-9573-399bcde16295 | -12.12959 | -50.16949 | 2025-06-26 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 452a9792-e9b5-3a0d-8f08-2df685e6bfac | -11.57537 | -47.43124 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3b77436-32d6-304c-9be7-fd32ece9b1f5 | -9.11818 | -49.43466 | 2025-06-26 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 112bd0b2-7645-31aa-917a-91901050d0b3 | -10.30187 | -57.13707 | 2025-06-26 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8d00988-df95-3e5e-b8ce-c451150a4af3 | -9.22099 | -50.67437 | 2025-06-26 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 465be0cc-c5a0-3f1a-8594-847f2e82139f | -8.07086 | -46.96867 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eeebf17-25bd-3353-854b-16e040bf6c09 | -8.23671 | -44.93661 | 2025-06-26 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e78f438-bd25-37c5-9169-20001a21d0d3 | -10.50967 | -47.20094 | 2025-06-26 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b09c0b46-7cdc-3577-8fab-3b8b5cb5a92d | -6.88086 | -46.36042 | 2025-06-26 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f8e4e0c-227f-3f48-9583-ffec814b1fe1 | -11.80949 | -47.5423 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38e87233-1cbe-35db-b5a2-9d5a3307ed60 | -11.80586 | -47.54183 | 2025-06-26 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b64e358-d2b9-300a-a807-42383fb65068 | -8.0673 | -46.96806 | 2025-06-26 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73ffcc6f-7a5f-3a37-90b8-f24d2df006fa | -9.50668 | -56.09867 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6dc3589e-a990-349e-bfc8-b4e83f0763fd | -9.51399 | -56.10743 | 2025-06-26 04:40:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0d1ece6b-8160-3e8f-a197-e565fd526a9b | -6.88448 | -46.361 | 2025-06-26 04:40:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c6b6f80-846b-3b6b-b8b8-ac21802262cb | -10.02964 | -54.31907 | 2025-06-26 04:40:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 039781dd-2209-307a-934b-84c510d1f16b | -5.00829 | -56.17576 | 2025-06-26 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b5b1dee-784f-38c9-ad49-8fae05f03b38 | -11.58548 | -44.63921 | 2025-06-26 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README11.md)
