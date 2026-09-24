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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bab2436-c095-3962-8c77-7688ec6dfafc | -11.40543 | -47.39639 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 577e5118-af8b-3f27-a78d-459b3cf21750 | -11.12564 | -48.30037 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 946e4403-4cae-3a60-94ab-1512836f98b1 | -12.11143 | -45.61172 | 2026-09-24 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99d02fb6-31b4-3697-91ad-a700404c66b6 | -12.13918 | -45.62382 | 2026-09-24 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ab4b5d3-01ca-315b-9bc6-7080696c1b3a | -16.39504 | -43.34332 | 2026-09-24 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc810cfe-162f-3934-8cb8-6acce0d7bd7b | -14.56635 | -54.11576 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42e4d3ff-2b4e-3e04-97fc-1a83d6548e77 | -13.38457 | -41.32231 | 2026-09-24 04:10:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d4f1a0d2-c5be-3d9d-9dd3-a8a6713c4046 | -14.71593 | -45.58614 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a33e4db7-8af7-3794-ac1d-2a3ae8bef3c1 | -14.75051 | -45.61118 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6355a957-06e8-3cc9-b307-432710ae32f8 | -10.1297 | -46.06511 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 630e3abd-96fc-3233-8c41-7aab1649782c | -11.49475 | -42.33991 | 2026-09-24 04:10:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8ad3a915-f7bd-3da8-8497-6db3c6a9128b | -11.6989 | -43.47256 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95a973e0-0292-34cc-9bf5-9e421293c600 | -10.27824 | -49.97009 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 573b07a7-074c-38bd-95ff-f39b1abe3646 | -10.27064 | -49.95842 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6429304-64f9-3724-8b91-1d5c770e3b39 | -11.95512 | -50.74829 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a3c618-2f95-3bdc-b237-9c040f1729ce | -11.46674 | -47.38787 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f69d9ad-b29d-33ba-8011-7735828ad742 | -11.39337 | -47.37386 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 192d56b0-f71f-3401-90eb-a4461d565846 | -14.72493 | -45.59556 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36064435-3616-3d4c-8940-533a8bf8bf27 | -10.24663 | -49.98507 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17ea6f54-f2e5-3fa9-88d0-0c221a6dd174 | -11.79239 | -50.99026 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 315b8a1a-d64d-383b-a40e-b726e50b59e7 | -10.09099 | -46.02707 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c138ed0d-b64d-34f7-a491-efa0545cf744 | -12.81199 | -44.84941 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dc98d57-e150-3a90-854c-b984a604ef5c | -12.41303 | -46.96602 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6fbe03e-c0ac-3877-a71e-23a17d8cbb6e | -16.41492 | -43.34666 | 2026-09-24 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 174ffdad-5538-3318-a6d5-fc4d9bb17d8a | -11.3996 | -47.36095 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a0d6b1d-613d-3437-9fe4-4c17c45a5cab | -10.10769 | -50.1869 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20967103-c567-3321-8c37-34cef37e9e02 | -10.09536 | -46.0457 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4235e6e1-3730-3e11-a3b4-986aa22fd566 | -9.85748 | -48.506 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fdb9db11-2630-3509-bced-b4e4eaec9826 | -15.16365 | -43.57062 | 2026-09-24 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e35f80e3-67cd-3351-91fe-a67e5de799f0 | -10.08265 | -46.00956 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| c8533fc9-da59-33a1-bea6-b5b79b3e9c23 | -11.69671 | -43.46498 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 164ab7cb-8d5b-3186-9b5b-c056967d4075 | -10.08731 | -46.00449 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1b0d42e-62cc-3361-b4a4-25cad9c1cedc | -10.07925 | -46.0077 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fff9ac40-f308-3faf-9dc2-3a1782c799b4 | -9.96613 | -50.25898 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ee47fe6-7663-3f98-9628-983a3d5b12e2 | -9.84039 | -48.50311 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97730bff-460e-31d4-9ffd-84980153ad83 | -10.0815 | -46.01661 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 3ff25180-0667-350d-afb5-bce390c555d3 | -11.93649 | -38.29122 | 2026-09-24 04:10:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3a50ece4-4a1c-3973-b66a-3f4655ba2b5e | -10.08865 | -46.06308 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7c623b59-4d06-3a05-a494-d8130748f77c | -12.16733 | -47.37925 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2b3ac78-9cf0-3671-819d-886f56e788c9 | -10.21351 | -44.1401 | 2026-09-24 04:10:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b8a2320-589e-3b6c-aa0a-df1a3b509134 | -10.09026 | -46.03142 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d17d0bc9-e51e-3e02-a3d8-9c23bcd8e891 | -13.65225 | -43.35888 | 2026-09-24 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8e407a9a-7502-3c03-9d69-7dff5265a286 | -13.46103 | -46.25743 | 2026-09-24 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 4334dd5f-ff5c-3080-bb87-7a964c86219e | -14.75014 | -45.63465 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66f56b5a-994a-3af7-9dc3-e560b94065f5 | -11.22718 | -51.36331 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| aa249047-4389-352d-93bf-6539c820d6ef | -13.09408 | -43.51299 | 2026-09-24 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f7b8e06-d1d5-3e05-97bd-4396deaabf50 | -10.09603 | -46.06398 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d889baa-b5e2-3792-8b5c-24a86be9ee98 | -11.44031 | -47.40252 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59b8400c-0d88-3424-a75a-a14e37f86113 | -11.25408 | -51.35908 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e0b48af-db0c-38a5-98d3-4b2b9504a1e7 | -14.07689 | -44.01302 | 2026-09-24 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10875052-b7e3-36dc-b441-9638b8c58944 | -11.13204 | -48.31227 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 219e54a5-c23c-3ba1-a3c8-c96306e00427 | -10.92986 | -43.85612 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9948456-6461-360e-b85e-a578b796e0e3 | -11.39725 | -47.37451 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d53878b-3d89-3f3d-873a-114ab7817222 | -11.64836 | -43.48968 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c2c5850-30c1-38a5-a42f-f66a2482d49d | -10.11449 | -50.20105 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6612b83b-329f-367d-840e-bd2b8a5955d8 | -10.08655 | -46.05329 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2ac22f9a-e299-33f5-a10a-b093f02bd68f | -10.10576 | -50.19736 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4f06dfa9-03ee-3e8b-abf8-470046e9ecc1 | -12.29077 | -46.39525 | 2026-09-24 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec135aec-c62a-3dc5-aae0-d585d6a5e2e5 | -16.4 | -43.33303 | 2026-09-24 04:10:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bec5478f-f76b-3ce6-8dc5-d9238b897694 | -10.2707 | -49.97106 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aec70491-cadd-378b-84fb-ecd7977bfee9 | -11.66436 | -43.49589 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b5923d19-5daa-31b2-ae43-13e056c2c552 | -14.70289 | -45.58006 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c91e357c-5bb0-32eb-a030-fcc2cf597f98 | -10.10112 | -50.19324 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8f9bd97b-b824-34bd-9065-e59335d10f93 | -11.66492 | -43.49237 | 2026-09-24 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9763cec8-5cfc-34ea-b91e-e678453bd273 | -12.15539 | -47.35719 | 2026-09-24 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50c885b0-a137-3903-8dfa-182463c2c15e | -13.84538 | -48.58273 | 2026-09-24 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 370b5a43-51b7-31ae-82a7-7f17582e2316 | -11.45312 | -47.63291 | 2026-09-24 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dda72db-35bc-369b-94cb-05138920032e | -11.79929 | -50.98012 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8dc4e5a-cf9f-3d69-a89f-f0387598c5d0 | -10.26889 | -49.96838 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1094947a-62f7-31e1-923d-63813f677657 | -12.04875 | -50.28496 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c780084-9667-3c80-a1b9-a22bed56b26b | -11.1101 | -48.3011 | 2026-09-24 04:10:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aea9e1a8-7406-3931-ae00-b5c236f8ea45 | -11.63114 | -50.60356 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a2a71b61-30b4-327e-afa4-c31396a346cd | -11.45222 | -47.63806 | 2026-09-24 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 779d55dd-4e50-3e9c-b43b-051eaede9d2e | -12.04323 | -50.28902 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90d5a142-b537-3877-aff9-873843bddf85 | -11.48091 | -47.38316 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b705d318-bdd5-30ad-a855-88046c4151f2 | -12.9245 | -50.9304 | 2026-09-24 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e689b179-9d97-3774-8236-a699246cf7f1 | -11.94174 | -50.74029 | 2026-09-24 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1862df3-d37a-3ef3-b913-447abeb1d054 | -13.29692 | -47.89097 | 2026-09-24 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06a22374-ccea-3032-9557-69d7d8a3d694 | -10.0835 | -46.02731 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8915387-adec-35ae-aa21-6074b9d9d050 | -14.56961 | -54.1289 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d6b7060c-9184-380e-8e51-64e7ce5334c0 | -10.0769 | -46.02174 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1fe0ae59-50b1-31d6-82e6-a3571c7ae06b | -14.63516 | -50.602 | 2026-09-24 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1253f98d-f88d-3ac3-a413-65e85302d822 | -12.42203 | -46.95818 | 2026-09-24 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a8b13725-05a0-39da-baed-d1731b01082b | -11.2311 | -51.37025 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f3c1573-f6fb-3dfb-aae3-2247ac7a4cf3 | -13.78806 | -54.06644 | 2026-09-24 04:10:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8ed40ed0-a61c-3f24-bed5-d3546fd744c0 | -11.39495 | -47.36476 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8225d7d-131a-3c33-8f3c-e6e14bc7427a | -14.62165 | -50.5992 | 2026-09-24 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52b892d1-dd73-35ce-b8ac-09dff9d944a7 | -11.4063 | -47.39136 | 2026-09-24 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3cae6a03-827a-3b28-b6cc-3ec98c9ac479 | -9.83963 | -48.48206 | 2026-09-24 04:10:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0f1fd32-a4f1-3070-890b-4fa64d502ff2 | -10.90404 | -53.9464 | 2026-09-24 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32263f29-32d1-3dfa-8b0b-3193b74218dc | -10.1246 | -46.05064 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93fee104-5d81-3a37-95a4-d44e3259f33d | -13.81821 | -51.83029 | 2026-09-24 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcb80141-291f-38f4-b471-d6d07e2f1bcf | -14.57673 | -54.13348 | 2026-09-24 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46ac3311-78fe-3ebd-8c0f-f8f989dfa2b4 | -11.23614 | -51.3712 | 2026-09-24 04:10:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22633337-d984-3800-8be6-2cf930f1f8de | -15.24405 | -43.26974 | 2026-09-24 04:10:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4570210d-746b-31d4-9229-df0e1324470f | -14.74495 | -45.60241 | 2026-09-24 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48d7eb34-51b5-30a4-a505-d20d35b57e0a | -10.4169 | -49.37256 | 2026-09-24 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 51e5e3a2-ea6a-3997-aaf1-52dc0ff60065 | -12.46338 | -43.41321 | 2026-09-24 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec05952b-6826-3969-bdd0-243a9a7628d6 | -12.01469 | -50.3143 | 2026-09-24 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b216d40c-da8d-3d2a-a37f-da685b963a14 | -10.07988 | -46.04945 | 2026-09-24 04:10:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README38.md)
