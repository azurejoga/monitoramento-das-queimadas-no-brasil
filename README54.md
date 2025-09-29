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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96f8be1a-7df7-3de2-95f2-9abec08ff047 | -20.4225 | -43.35477 | 2025-09-29 04:10:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5db9f04-392e-304a-a26c-eb8777c3df56 | -17.71979 | -46.68687 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fc5a719-f2b9-3884-8962-030f2aad5aad | -16.50327 | -46.02837 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 130c6b25-633c-344e-a664-98325948d148 | -23.54441 | -47.53804 | 2025-09-29 04:10:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35de8d76-a0b1-3dd5-825f-25f8e6a39346 | -20.08045 | -41.35951 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b178e542-d8cf-384c-bd9f-a277e17fd7f4 | -21.7323 | -44.41693 | 2025-09-29 04:10:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a969cfa3-0bd3-32ea-b2dc-ec0b2e2c5618 | -17.08791 | -48.5717 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| a6230aff-6ef3-3653-9076-32ad52b9d761 | -16.52664 | -46.9505 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7741065b-9d08-3bcc-bd44-947687cacdbe | -18.11723 | -42.18768 | 2025-09-29 04:10:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 278c6c96-4105-3784-a16c-16200a73064b | -19.84855 | -42.60455 | 2025-09-29 04:10:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c121ccbd-147f-3cef-ab09-5912b308e7ff | -17.08106 | -48.56506 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f173145f-6434-34d8-ab86-2fd1962fbf22 | -16.52738 | -46.9463 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9117830d-fa16-328b-a767-c998f3e03c83 | -18.11669 | -42.19139 | 2025-09-29 04:10:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 737cf61e-0f64-3133-8d92-ca9742020002 | -17.9571 | -41.50967 | 2025-09-29 04:10:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 802782e2-5d2f-38f8-969b-f86e6cfaed21 | -16.20403 | -48.26165 | 2025-09-29 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7420a4f1-e988-3e4e-9a61-ec5348349c15 | -19.54745 | -40.62602 | 2025-09-29 04:10:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7d9befc7-3a60-300d-8fef-ed72c107d13a | -23.20608 | -49.21764 | 2025-09-29 04:10:00 | NOAA-20 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb7f743-b2d5-3372-b42a-ab823645c9fd | -16.85335 | -45.80508 | 2025-09-29 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d03c5267-76a3-3e85-ad26-5638fa4cdc2c | -16.539 | -45.28682 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9e2f0be-a6f5-395a-be01-27067b2cbfb7 | -19.94109 | -43.66854 | 2025-09-29 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e35cc871-0c36-3681-ac45-290b0752849d | -16.50193 | -46.03639 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00a8094d-3a31-3906-a63d-c9939fa7b92f | -17.71354 | -46.72356 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aa129d3-d5e5-39aa-95f9-c2c613f1cb3a | -17.74721 | -48.76526 | 2025-09-29 04:10:00 | NOAA-20 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81339e32-7b43-3277-80ad-fbbf6dcb8216 | -19.65485 | -45.97747 | 2025-09-29 04:10:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00c35d12-35d3-39a2-96be-872c7b6967eb | -19.73232 | -43.22789 | 2025-09-29 04:10:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 77701ae8-ed3f-3ebe-a1f7-0b15fb115f85 | -23.22934 | -49.40369 | 2025-09-29 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 2d7faba5-c6ba-32a3-87db-0966a5ef4d67 | -15.24342 | -56.82143 | 2025-09-29 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bd78721-4215-325f-98fa-f3d35001d713 | -20.04681 | -41.3365 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c77e2ed2-54f7-3c17-b657-f6d0973d9024 | -19.67733 | -43.77278 | 2025-09-29 04:10:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7efdbe9e-61bb-3b08-84b7-c3c2ac2fba4d | -16.60378 | -45.13295 | 2025-09-29 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d99c9f7-1a96-354c-ab44-4678d54e2209 | -20.20452 | -41.38552 | 2025-09-29 04:10:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 75f8ce69-2f98-3773-8e5b-92d74618388d | -17.90169 | -57.61234 | 2025-09-29 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 025b79bb-2afe-303f-ac2e-bb507f5dfa85 | -16.99738 | -43.50669 | 2025-09-29 04:10:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 754eab10-e295-3cb5-87f4-c6ac7c34f272 | -19.96502 | -41.73991 | 2025-09-29 04:10:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 442e7d62-def5-3d0c-a0c1-18d2549a946c | -16.29057 | -45.85115 | 2025-09-29 04:10:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3468fa7-2abc-3d1a-a8e1-d3489742b191 | -20.05454 | -41.33392 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| af463c4b-d4bc-3a00-adab-b6c563990804 | -20.53931 | -45.09726 | 2025-09-29 04:10:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 97d744cf-54d2-36dd-a566-c2893a1eac37 | -16.8452 | -53.19823 | 2025-09-29 04:10:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b083b482-3bcf-3857-b5c8-432d3b79be0f | -20.44136 | -43.2289 | 2025-09-29 04:10:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f7b3a479-0586-36a3-b991-79eed343ef0a | -19.73289 | -43.22408 | 2025-09-29 04:10:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2aa74939-d54e-30eb-999c-8fe6277cb48b | -16.48879 | -46.02989 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31746fb6-1854-3724-b4e6-cf1ee996f0dc | -19.86788 | -43.83446 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8a8daeff-1a76-34da-82aa-44e43743fbd9 | -18.41246 | -44.90578 | 2025-09-29 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdb257ab-ae93-3e0c-91e8-3203bcff8043 | -21.33125 | -44.48896 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7583d0a7-94b0-3dcc-adb9-ced03f48992c | -17.89994 | -57.61989 | 2025-09-29 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a7713643-f345-3cc6-878f-d73a25c54205 | -17.28101 | -42.70059 | 2025-09-29 04:10:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 707a99e0-74ab-369f-8145-d1aa8b43bcb7 | -19.85197 | -42.60511 | 2025-09-29 04:10:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f8baf1c0-fbcb-3560-ac8d-0a6c0eb20154 | -23.22278 | -49.39757 | 2025-09-29 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6d46540c-a0a7-3b1b-8ff8-fb8f2b92e29b | -17.71707 | -46.72412 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2b03065-3d94-3751-ad76-77be4b466918 | -22.53012 | -49.11065 | 2025-09-29 04:10:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 710c37c2-982e-3d70-8f6d-6654c1ef48d1 | -17.39484 | -47.11855 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71d3b06b-5a1e-3dc2-8ddc-991e2d993c31 | -17.08896 | -48.56847 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f671d968-b746-31ac-9b38-4ccb687bcdbf | -20.53871 | -45.10096 | 2025-09-29 04:10:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23468e16-b44d-3a4d-a622-d0533883f379 | -18.23698 | -42.44202 | 2025-09-29 04:10:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 35538dc3-132b-3ac9-828b-e79e740372c7 | -17.09177 | -48.57255 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 9b3a3d9b-fc34-3732-9480-3583aa03432b | -17.39559 | -47.11428 | 2025-09-29 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a7105e15-14a7-3591-a36a-8a1aeed02f56 | -16.54667 | -45.3036 | 2025-09-29 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 430c0398-ec07-3b33-be66-bc5d57e1222b | -17.7121 | -46.68961 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0583f4ca-baa8-3350-9703-7580a77f0f4c | -23.35803 | -46.89145 | 2025-09-29 04:10:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45a9400f-2392-31b4-9a40-318bcbe67f7b | -23.73138 | -47.32607 | 2025-09-29 04:10:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c78ae75-3392-3238-910c-c7aec887a7ff | -23.22297 | -49.41756 | 2025-09-29 04:10:00 | NOAA-20 | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| c2a0d865-0d48-3a4a-aa30-292aee98d3cf | -17.08988 | -48.5635 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8459984e-8b47-3606-8324-e61d51257a72 | -22.08908 | -46.83778 | 2025-09-29 04:10:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f767f93-cf90-31d9-9b52-86ea2758ba5c | -16.10793 | -46.67003 | 2025-09-29 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa387502-1a62-3103-8241-d603b718af44 | -18.97745 | -48.40011 | 2025-09-29 04:10:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 79839f6a-ac2c-3bca-8707-c5e90c246cf7 | -17.73029 | -46.6888 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d6b58cd-4073-3e8c-9d05-df1c20e463c8 | -17.09187 | -48.57446 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 872a1b34-2702-3f28-81b3-893b96f1fc12 | -19.85597 | -42.60175 | 2025-09-29 04:10:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4b54982e-0d9e-3488-8da8-906782835307 | -21.04333 | -43.2985 | 2025-09-29 04:10:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8c84ed4a-35b7-3011-8545-6d1927a2433f | -17.50356 | -43.483 | 2025-09-29 04:10:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c9df782-e469-39c9-a893-61b3920a246f | -19.84912 | -42.60062 | 2025-09-29 04:10:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 067cefd4-fc9c-3db0-8f7b-426cb320ad87 | -20.08348 | -41.36422 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9bdd936a-4421-3dc2-9a97-417f05d6ae8f | -19.86409 | -43.79226 | 2025-09-29 04:10:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 23ea6ced-f684-360a-b567-65cac869b383 | -23.44763 | -47.28036 | 2025-09-29 04:10:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f47ef978-aa9a-3967-958b-cfc8bfd89479 | -20.05813 | -41.33459 | 2025-09-29 04:10:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 397a3c4e-525f-3299-b663-d13cac34a12f | -21.01463 | -44.03098 | 2025-09-29 04:10:00 | NOAA-20 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9cc1d394-0198-3d3f-bd9a-9a3d86e5b86a | -16.06082 | -51.0257 | 2025-09-29 04:10:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04fdd646-5f60-37f4-b50e-1d6fc274373a | -18.54501 | -44.02916 | 2025-09-29 04:10:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58a4d823-7aca-3513-988f-587397d57855 | -17.64955 | -46.41732 | 2025-09-29 04:10:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a2f37d6-b024-3ea2-9e80-edb4908137f4 | -16.84564 | -53.19828 | 2025-09-29 04:10:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80490ddb-e16b-38f7-900b-d7a7fa5ed9cd | -17.08881 | -48.56664 | 2025-09-29 04:10:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1481d2cd-ef71-3c1e-9af7-8f4b6021e4d0 | -21.42427 | -43.76793 | 2025-09-29 04:10:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 073785ae-10c6-31f2-80cc-109e904f49f8 | -19.67457 | -43.76854 | 2025-09-29 04:10:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 254c7333-32e2-3fac-9acb-1657d1a2975e | -16.49504 | -46.03504 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfc77c2f-cd34-3ca0-afc8-0e9ae69cd7b7 | -17.7156 | -46.69026 | 2025-09-29 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e94dbea4-7cff-3b86-a298-673dbb05cae5 | -16.50673 | -46.02903 | 2025-09-29 04:10:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fa5b898-6225-3b85-8cfc-27ae331586fb | -25.06347 | -50.44787 | 2025-09-29 04:12:00 | NOAA-20 | IPIRANGA | PARANÁ | Brasil | 4110508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 91c06ae9-7f8b-3874-8537-63345c8f9cb8 | -25.05055 | -50.041 | 2025-09-29 04:12:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eafc1bd0-cb6e-3532-9624-5c86e7f1e537 | -25.06029 | -49.35422 | 2025-09-29 04:12:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0903d0e-ac59-3ea3-8cea-d6ceacb09b7a | -24.36908 | -48.9512 | 2025-09-29 04:12:00 | NOAA-20 | APIAÍ | SÃO PAULO | Brasil | 3502705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 038c8af7-f6c7-3b0f-a49a-b8a901b64a33 | -25.04684 | -50.04017 | 2025-09-29 04:12:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9f3f3a1a-da45-3ab3-a56d-50db06e352e7 | -25.06305 | -49.35957 | 2025-09-29 04:12:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 029018c1-3ece-3318-8c7c-af65d87bf650 | -25.0639 | -49.35489 | 2025-09-29 04:12:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c16d91b1-008e-31f4-bb15-5c6ecf85bbde | -25.00582 | -49.38345 | 2025-09-29 04:12:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2677b0be-92e5-33ad-8467-6273602e8117 | -23.4746 | -52.09877 | 2025-09-29 04:12:00 | NOAA-20 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c7466f9c-4cb3-3742-b018-f7cdceaff7e2 | -25.05944 | -49.35883 | 2025-09-29 04:12:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 63e558d6-6184-323f-b513-8b8f1c13b1b9 | -17.9009 | -57.6182 | 2025-09-29 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.2 |
| 71584c76-52bb-3716-a58f-38b1ff455788 | -14.553 | -48.4237 | 2025-09-29 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d389e7d6-022f-3741-a546-ad82fb38ce45 | -17.9013 | -57.5976 | 2025-09-29 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 4bbcd282-8e33-35a3-beb0-4375d1605154 | -14.5331 | -48.4491 | 2025-09-29 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 129.4 |


[Clique aqui para ver as próximas entradas](README55.md)
