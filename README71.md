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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8772e760-6cc8-3cdc-96d2-7fa604eb2303 | -8.50171 | -41.40499 | 2024-10-14 04:44:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eda88415-78ef-33e8-86e2-1e998b978acc | -8.14344 | -42.3282 | 2024-10-14 04:44:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1c6b1a0-accf-392d-a5b7-23545e6780a5 | -8.14301 | -42.33139 | 2024-10-14 04:44:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a0e20211-9d6e-33c1-9310-793b54eb3be6 | -8.14259 | -42.33455 | 2024-10-14 04:44:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cdecbb1a-c3a5-3cc8-a2e9-d08f6bd2a2c3 | -10.49083 | -42.44062 | 2024-10-14 04:44:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2af52902-ff4d-3335-9ec5-b63b875f6d43 | -10.49037 | -42.44418 | 2024-10-14 04:44:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 8b0c5ae7-3545-32f6-a6f5-2169632d9a95 | -10.48587 | -42.43626 | 2024-10-14 04:44:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 96c31fdc-c468-326a-91ff-bb34ce0ede01 | -10.48541 | -42.4398 | 2024-10-14 04:44:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| d8ebf2e5-8fb0-3869-a74a-98562584cd62 | -10.48496 | -42.44335 | 2024-10-14 04:44:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 14.5 |
| bec39877-c3d7-36ca-a370-88d03eb68891 | -3.30952 | -42.84134 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 89fbc483-9cff-363a-8cf4-81320d04aaf9 | -3.30875 | -42.8464 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 01a40ca4-69ab-333b-b834-e627f5bd1f17 | -3.30631 | -42.83053 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c08864a9-5653-3d03-a070-a5d7859d12e3 | -3.30554 | -42.83557 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ddd72f4b-ab10-3d0f-b743-148d43116856 | -3.30477 | -42.84063 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 36dee78f-76dc-32c9-aac5-3d1d3b02403a | -3.304 | -42.8457 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 799033cf-e83c-3dea-9a86-0b943db449f6 | -3.30323 | -42.85075 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 653d1c5b-2426-3ee3-b4e9-a1f21b8bb97f | -3.30155 | -42.82983 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe3d45dd-f6d3-3dc9-9cd9-96705fc29ad6 | -3.30078 | -42.83488 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| ff307644-36f7-3a4b-b0dc-75792602d69c | -3.30001 | -42.83994 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d1592ad1-3b6f-3c99-a0dd-5e750a804bee | -3.29924 | -42.84501 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 8397876d-f2e8-36a6-8123-f8dd2e0679b6 | -3.29848 | -42.85006 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| df2d4629-67b1-3e1a-8cae-1e11273bca26 | -3.29603 | -42.8342 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 7bfaa4b9-635d-39f5-98e5-f21fa890d33c | -3.29526 | -42.83926 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 38ed0827-c11e-323d-a97d-970ecc00c4d6 | -3.29449 | -42.84432 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 29e9702a-db32-3e0a-b575-2c87dbb7a6c5 | -3.29373 | -42.84936 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| fcb3afc2-ee13-375f-8ea9-43cca9db5f5a | -3.2905 | -42.83858 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb43b8f4-2b53-3e06-aae9-952313dc0c29 | -3.28974 | -42.84362 | 2024-10-14 04:44:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 309b8e95-60b8-38fb-a8e6-46f7c3c05529 | -4.03596 | -43.03376 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98d22e30-3fb6-386b-a18c-a17aa30bb248 | -4.0352 | -43.03873 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e96ba61-6e59-3c06-b7fd-51a066e2166a | -4.03501 | -43.04674 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f73b06d-638c-3fdb-93d9-c80f35b587fc | -4.03444 | -43.04381 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e49c5e25-5343-33fd-8889-8460605b06bd | -4.03367 | -43.04885 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c35557d7-b3d4-3d4c-8848-91ec0ba368d9 | -4.0312 | -43.03313 | 2024-10-14 04:44:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00c0c621-656a-3157-9d6f-c9bb03ddc37b | -6.2572 | -42.4984 | 2024-10-14 04:44:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d84494e-7d45-332a-a41f-fba6bbbefe18 | -6.25677 | -42.50137 | 2024-10-14 04:44:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a7d0aacb-7f43-3c22-a6be-d0d2cc1f82fb | -6.13504 | -42.77943 | 2024-10-14 04:44:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 39293bf7-c7ad-339d-b44b-69354d048202 | -6.13448 | -42.78445 | 2024-10-14 04:44:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 31f898ff-1ddc-3804-a39f-4d6e19757923 | -6.13425 | -42.78503 | 2024-10-14 04:44:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f9b5cfc2-1731-3670-8260-1b4b644d2408 | -6.08589 | -42.40532 | 2024-10-14 04:44:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1313d96a-785f-3df5-800a-0280bd5f3837 | -6.08078 | -42.40456 | 2024-10-14 04:44:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| becb123c-b181-3837-afbd-db41b40fb9d8 | -5.95577 | -43.19241 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1fa8f952-a45b-3165-ac6f-00c1607a7454 | -5.95235 | -43.18927 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a37dc8d5-a4bd-3abc-a5a4-53938b5900a5 | -5.76218 | -42.78479 | 2024-10-14 04:44:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7559c21-31ee-3995-a3da-540d95b967da | -5.76137 | -42.79039 | 2024-10-14 04:44:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37d06022-13f1-314b-bfd3-c15149c26a42 | -5.53096 | -42.93767 | 2024-10-14 04:44:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1f30725b-c046-3487-92b5-54cfdf33d610 | -5.53019 | -42.94299 | 2024-10-14 04:44:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3494de0e-f13c-3bf5-a098-c2cd46005373 | -5.33535 | -43.01463 | 2024-10-14 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f79e61f7-0f55-34e7-a106-a89620d475c8 | -5.2914 | -43.07832 | 2024-10-14 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c35b455d-7b42-3bf7-9361-1bbf6cb3158e | -6.04129 | -43.34842 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52591961-c022-31e5-a98d-936b15fe949d | -6.04121 | -43.34427 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d473bbaf-cd02-3dbb-b279-1ae059b5ee29 | -6.0365 | -43.34773 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d87450fd-a2b1-3664-916a-d40ce2d7c362 | -6.03643 | -43.34356 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 497b9194-2e2a-39ea-a985-cf1f4ca96f71 | -6.03586 | -43.38511 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 69f74a8f-36ed-310a-a7bd-ba4863cc9acb | -6.03535 | -43.38624 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7183ad35-074a-36f0-afad-ca3414f2fa7b | -6.03104 | -43.38479 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5af7f5f0-dc15-3009-94af-de50c89db2b9 | -6.03053 | -43.38592 | 2024-10-14 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1c6fdeb0-091a-351c-a46e-680d094de557 | -7.72752 | -43.22007 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 471b24fb-932f-31c2-969c-612c1702b3c7 | -7.72491 | -43.20257 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 45c714f8-6a07-3edb-af89-13c1c9a52f03 | -7.72414 | -43.2081 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e0df5ac2-b2fa-3b87-a323-60b6e209fd79 | -7.72338 | -43.21356 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| df8da8ad-793e-3a4a-ab01-6838b15fa388 | -7.7226 | -43.21912 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 640b0cb3-1826-3690-bafe-843f343fa183 | -7.72182 | -43.22475 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a233b111-3e81-3333-9f97-c1f6f0b2d457 | -7.72075 | -43.19609 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 64f2ea2c-4080-3670-99a9-35e40945c568 | -7.71996 | -43.2018 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| db148ea6-6302-347b-aa2a-949e2dbf5b73 | -7.70628 | -43.22767 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 22020acd-9586-33a4-9976-ef478c60957f | -7.70329 | -43.17604 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 11064d7b-cb7c-391a-b125-a728c805d696 | -7.70134 | -43.22692 | 2024-10-14 04:44:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16dba52a-d96e-3ed3-8330-1b12b90ed3b0 | -7.4371 | -43.00205 | 2024-10-14 04:44:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a81323e-9568-3911-9246-f6b76513f6cf | -7.43286 | -42.99586 | 2024-10-14 04:44:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2709ba3f-5596-397a-b5d0-9b768654c46d | -7.42707 | -43.00079 | 2024-10-14 04:44:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dd12a8a8-8845-34dc-9b7f-75e122afaf50 | -7.4263 | -43.00633 | 2024-10-14 04:44:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 39b4c478-5e50-36d6-8808-730c6491d582 | -7.42207 | -43.00005 | 2024-10-14 04:44:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d82ec54f-dda5-3818-8571-9140610fbd1e | -7.20598 | -42.28978 | 2024-10-14 04:44:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc0a755a-48a1-32c4-89e3-f85ed2bb6cd5 | -7.20211 | -42.27916 | 2024-10-14 04:44:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cc524cba-b932-3c57-a42b-b4d2e791d3f2 | -7.20166 | -42.2824 | 2024-10-14 04:44:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a827b78-5cef-35b7-8ae2-cad776d63de3 | -7.20121 | -42.28563 | 2024-10-14 04:44:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0af114af-10d4-3f6c-a859-9d2983bad2c1 | -7.20078 | -42.28879 | 2024-10-14 04:44:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3b7c6dc3-e57b-33ae-868b-52ea871e8d0e | -7.17457 | -42.62853 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 57151ef3-a33f-3f9f-a83f-a88a0ccd4cd6 | -7.17415 | -42.63152 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 715ec0b8-3cea-3f8a-9433-7648d2f8792b | -7.17373 | -42.63454 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1b9d4493-4bcc-307e-ab47-eee6697a2906 | -7.17325 | -42.60073 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0178da7a-bab2-3b75-a25c-84918b4b39f6 | -7.17282 | -42.60381 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3aa86e9d-218a-3009-a90b-701099e3fd7f | -7.17239 | -42.60685 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72bfb290-8038-3aaa-817a-354ffca273fa | -7.16946 | -42.62777 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2523f8e4-ad36-3dcc-98a1-2d863793479f | -7.16856 | -42.59691 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b188bc95-765a-3122-8415-28da941c7dbb | -7.16386 | -42.59309 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d4efcb1-41e1-3346-97d7-732d9f6128a2 | -7.15875 | -42.59229 | 2024-10-14 04:44:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9479332b-e8a0-38da-a034-05eadc213e52 | -7.0901 | -43.01209 | 2024-10-14 04:44:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e00dba08-408b-3944-8637-b82bd2d815e6 | -7.08969 | -42.65548 | 2024-10-14 04:44:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dbabfbe7-fbf2-3e8c-8eae-6441ed1b2798 | -8.44945 | -42.51092 | 2024-10-14 04:44:00 | NPP-375D | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 900d2051-0855-32ce-b362-4090f3d55b47 | -8.44902 | -42.51414 | 2024-10-14 04:44:00 | NPP-375D | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 573a50ca-0d2f-33e6-b83b-a06e91c84583 | -8.33308 | -42.73672 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f56d65c-7f06-34ae-9bed-8b4493c0d8de | -8.33265 | -42.73983 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c4fdfec2-8d01-3e70-affe-5b02221576be | -8.33223 | -42.7429 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35dc3ad1-4d31-32aa-b092-32d1ab1fab4c | -8.33181 | -42.74598 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4561f325-2274-3cfb-800a-b1b88d73a21e | -8.33139 | -42.74903 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a59e78e-ef84-3583-b163-83324e0bdc56 | -8.33097 | -42.75209 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47a09b31-2505-35cd-b115-899a0076da34 | -8.33055 | -42.75514 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee4c0364-98ec-3bf4-a8ab-e1a0bf8f32b2 | -8.32793 | -42.73593 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 86e9c9c2-4b60-3e55-8d29-daaeaca7d7b2 | -8.3275 | -42.73903 | 2024-10-14 04:44:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README72.md)
