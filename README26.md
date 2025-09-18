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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf5ee738-6fd5-381e-955d-3ddbc013d7dd | -17.17588 | -45.91809 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05f918f2-61a8-3daa-b600-448bb9aa0872 | -20.58808 | -45.74197 | 2025-09-18 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75cb5b94-8389-3aeb-ad26-dea99eb92066 | -15.96942 | -38.94708 | 2025-09-18 04:17:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 464461fb-260e-3881-935f-1b27fd58d074 | -20.66883 | -48.75059 | 2025-09-18 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1209360a-3d2b-36ae-b095-9a3d207c033d | -21.18933 | -50.14933 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b788cc42-ba3c-3b7f-9c66-dd3d34745f4a | -15.57205 | -44.41224 | 2025-09-18 04:17:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 22239ffe-4291-3790-99c7-7eddd639e0f6 | -18.07558 | -49.5023 | 2025-09-18 04:17:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97f7d287-2d7e-3115-b53d-d941c7e64468 | -18.11899 | -44.65495 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79a4bba6-f0af-3049-adf6-38919af86130 | -18.69183 | -43.74113 | 2025-09-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 898e26a0-50b7-3a42-92ca-097bbc479e9b | -20.3439 | -48.79072 | 2025-09-18 04:17:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31eddc57-1558-39ce-aa1c-40062bcd4a2a | -17.72542 | -46.7911 | 2025-09-18 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a093624c-dc27-37c0-a12f-686601947ca5 | -20.79876 | -48.99257 | 2025-09-18 04:17:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4ee17ecb-efd4-325a-9436-91a5830e160f | -18.69467 | -43.74582 | 2025-09-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a7fed56-d7bf-3b11-90c7-391237280359 | -20.0611 | -50.36943 | 2025-09-18 04:17:00 | NOAA-20 | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a8991cef-7f04-369b-8836-b2e12ce7c9f8 | -18.34097 | -43.29715 | 2025-09-18 04:17:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 19326e03-63d4-31d0-a828-bfff11af6975 | -19.58733 | -57.78035 | 2025-09-18 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 70d9c594-9279-30f4-9fd5-2e0b94c8337a | -15.96996 | -38.94274 | 2025-09-18 04:17:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bd53d519-3952-3f9d-ac19-1f9d2a30080b | -17.20239 | -45.92268 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 944602ad-3130-366b-85d6-8e45bfa7d32c | -19.25986 | -46.67377 | 2025-09-18 04:17:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8e01547-5477-3784-89d5-bc3953569b4b | -16.18253 | -46.47096 | 2025-09-18 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f40ff95-2553-3962-944d-aafcac9ccb30 | -15.96615 | -38.93779 | 2025-09-18 04:17:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 09db6bff-00b3-3682-98f4-b31fba178510 | -18.69527 | -43.74173 | 2025-09-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44131750-6d08-382a-aa37-02c60679c0c3 | -19.69595 | -43.63219 | 2025-09-18 04:17:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42b09ddb-9ab4-37d8-8d20-18e95105680c | -21.04903 | -48.84567 | 2025-09-18 04:17:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.5 |
| 2536be4b-e60c-3c53-92b7-78b803c31b1f | -18.53394 | -46.04947 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64714cdb-e4e7-3917-8b29-fd94355b47db | -17.77318 | -44.43665 | 2025-09-18 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa9d0fd9-b3d4-3c24-b975-112c7b13919e | -16.62383 | -43.42889 | 2025-09-18 04:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f88833b-fb42-3507-9f76-8f5e438c68c8 | -17.76679 | -40.19164 | 2025-09-18 04:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| 7768b1cc-39ae-39ec-8960-84e7f6c68db8 | -21.11679 | -49.12797 | 2025-09-18 04:17:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c313e528-a351-38c1-b1a7-42bea25f2ea6 | -21.06871 | -45.61737 | 2025-09-18 04:17:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04d8592c-99fe-38b7-8c24-d013beb8e913 | -17.17429 | -45.90671 | 2025-09-18 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2311ee74-459f-35ff-aa7d-cd32235b9d5f | -17.76267 | -40.19107 | 2025-09-18 04:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 37.7 |
| 347b7340-4ef4-3735-856b-7c36c7d22fd4 | -15.41267 | -46.17139 | 2025-09-18 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f14f1ac-d525-3000-97b3-0f2b371a5490 | -16.22812 | -40.1215 | 2025-09-18 04:17:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c0b71e2-5e4b-313b-9b9d-0c7d49ff64f9 | -18.33108 | -43.29136 | 2025-09-18 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dc238168-7617-3415-80cd-ff91730448ea | -18.38163 | -46.47121 | 2025-09-18 04:17:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9ac581d9-64ac-3134-809b-97aabfda23cb | -16.62325 | -43.43277 | 2025-09-18 04:17:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bc1e988-548b-3941-94a6-63ef5d51a159 | -14.61659 | -46.38611 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f5e676d-5357-3dd1-93ba-482722cfe268 | -20.05732 | -50.37085 | 2025-09-18 04:17:00 | NOAA-20 | GUARANI D'OESTE | SÃO PAULO | Brasil | 3518008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 6064b5fc-cb84-3b69-a4fc-fe34d64e279f | -21.15864 | -46.99358 | 2025-09-18 04:17:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a587f689-ea71-39bd-9540-bc715f909637 | -14.59987 | -46.31902 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ec7cad4-9449-3adf-8c85-56aa7e0db753 | -18.33049 | -43.29541 | 2025-09-18 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be482c96-2f0d-3740-8ee2-ce97dfa0d3f4 | -14.64472 | -46.3834 | 2025-09-18 04:17:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce35592f-87c3-3657-aac3-7353a8998502 | -20.90114 | -51.61362 | 2025-09-18 04:17:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 77b6cd07-ae08-32b9-b457-67b61c656441 | -18.67306 | -47.87878 | 2025-09-18 04:17:00 | NOAA-20 | CASCALHO RICO | MINAS GERAIS | Brasil | 3115003 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b859df9-1817-3954-8bdf-78162f81ce29 | -21.30515 | -48.55851 | 2025-09-18 04:17:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cff5faf-98be-3e73-b1b5-4f2699506f13 | -17.04908 | -45.90395 | 2025-09-18 04:17:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6abc15e9-038c-3afd-9b52-fce2c8635416 | -19.65498 | -46.19756 | 2025-09-18 04:17:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37e33a0a-9bd7-3cb4-8e4b-df46f3131bc0 | -18.36837 | -43.30543 | 2025-09-18 04:17:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 831cbc72-7db2-3762-863b-e93c98936fef | -18.12233 | -44.65554 | 2025-09-18 04:17:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8c2801a-3e65-3d03-9575-a639ac90b7d7 | -21.18851 | -50.15382 | 2025-09-18 04:17:00 | NOAA-20 | GLICÉRIO | SÃO PAULO | Brasil | 3517109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 813c1331-fe3b-3a5f-8ad2-bf7fc831cb2f | -22.04661 | -44.74055 | 2025-09-18 04:17:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6531d77a-22a1-362c-926d-82b2e32f3cab | -20.66815 | -48.75465 | 2025-09-18 04:17:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6b4ed97c-0610-30fd-873e-b10618ba9fea | -20.04309 | -44.17648 | 2025-09-18 04:17:00 | NOAA-20 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0a308af4-accb-330c-95bd-cba9dbfff62d | -18.53452 | -46.04584 | 2025-09-18 04:17:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42d29845-1e62-3079-8828-850eca37a51f | -21.10983 | -49.12656 | 2025-09-18 04:17:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3922e33f-0ddc-3983-87cb-550d4c12fa0f | -22.01336 | -46.95879 | 2025-09-18 04:17:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b879517e-17c3-3742-8c76-5e4c82a594c4 | -22.33451 | -46.75251 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d288c2b7-f420-39cf-8693-ecfbff324018 | -23.13472 | -49.64013 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30e75178-10cf-3658-80f0-eb1c0c377bf3 | -23.47174 | -47.27045 | 2025-09-18 04:19:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb3b8b4e-0215-3d3d-8aae-1cde91f45c2f | -22.34776 | -46.75491 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d9f06b9b-8c18-3824-bb21-14ae8604ad74 | -23.09398 | -49.85493 | 2025-09-18 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7430fe22-0e46-357d-a528-bc9d0a80d65a | -22.35166 | -46.75179 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e475fb3b-a624-3286-912a-db4fe0e71b48 | -22.84963 | -46.03434 | 2025-09-18 04:19:00 | NOAA-20 | CAMANDUCAIA | MINAS GERAIS | Brasil | 3110509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7ab8e067-cd20-332a-ad88-879102fe4fd4 | -23.63412 | -51.54339 | 2025-09-18 04:19:00 | NOAA-20 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 63b9525e-0b4f-3170-94c3-f115b98eecde | -22.34055 | -46.75743 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 68690cdc-63a8-3ddd-9b42-49e0312f50ee | -23.1323 | -49.63861 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 391a8ef1-2159-390b-977a-a64086abf912 | -22.65723 | -46.02384 | 2025-09-18 04:19:00 | NOAA-20 | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 575edfc4-8fb0-310a-b0dd-8121e0a0a1ed | -22.33119 | -46.7519 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| db6c7331-0212-38f0-885b-de7e5e2e4ce8 | -22.70024 | -47.52888 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4588eae-674d-361e-93a4-a74cc5ad5730 | -22.97031 | -51.59104 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7b97b3b5-4f03-364f-b39d-1ccdf3a6db4f | -22.96077 | -51.59957 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| ee825b49-2ca0-37f3-b280-acbc021006f9 | -23.13156 | -49.64282 | 2025-09-18 04:19:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6d4c874e-1754-3609-8938-f820dd303502 | -22.67669 | -47.50514 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eaaf4b20-73c1-3c18-9807-bea824cc2be6 | -22.88448 | -49.96985 | 2025-09-18 04:19:00 | NOAA-20 | SALTO GRANDE | SÃO PAULO | Brasil | 3545407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3a366d55-43e3-377a-93f5-1cb172836106 | -23.0975 | -49.85563 | 2025-09-18 04:19:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b4ae4bb1-0d50-3c1b-ac1b-91f6f7a7169d | -22.6936 | -47.52763 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 80e0dff3-9802-3f55-80cb-513348f3693a | -22.69631 | -47.53201 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f6a0e701-2a0c-3779-9fb9-41f359345b8c | -22.78722 | -47.21656 | 2025-09-18 04:19:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f89a43e2-9b26-3e68-84f0-4f852af526b7 | -22.66673 | -47.50325 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b2c06c83-c2b0-3d29-8303-344e776d5a01 | -22.69692 | -47.52825 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 792dbb93-d877-37b4-b7bc-17af654112f2 | -22.74335 | -47.44744 | 2025-09-18 04:19:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a5a6b167-0e19-3816-9763-431e2c371da1 | -23.02699 | -47.03231 | 2025-09-18 04:19:00 | NOAA-20 | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f741ac2b-c8f8-377b-9a16-c25154988a53 | -22.13211 | -51.18864 | 2025-09-18 04:19:00 | NOAA-20 | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 787fa176-12b6-3f8d-a4d8-4d6f43f640bb | -23.34715 | -45.47295 | 2025-09-18 04:19:00 | NOAA-20 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b42033cd-b7b5-36cb-aa8b-4e20f92712a9 | -22.66987 | -46.73478 | 2025-09-18 04:19:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40c0e1ba-9f91-3244-992c-56a6e22c05ef | -22.6539 | -46.02322 | 2025-09-18 04:19:00 | NOAA-20 | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3a752948-4a6b-392e-ab57-d0008db89431 | -22.66056 | -46.02446 | 2025-09-18 04:19:00 | NOAA-20 | CÓRREGO DO BOM JESUS | MINAS GERAIS | Brasil | 3119906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 21156ea4-eace-3244-9429-516d53ebf873 | -22.94358 | -48.18631 | 2025-09-18 04:19:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b82e51-4bc5-3c25-bcc1-b282be3b4dc1 | -22.24635 | -52.44729 | 2025-09-18 04:19:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 120470a9-1340-37ae-b4ff-718d499992c7 | -22.34496 | -48.34842 | 2025-09-18 04:19:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0eaa8f1-012e-34ee-9b7b-b8ba9b66c862 | -22.9646 | -51.60033 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| a73c7d0b-4793-32f0-ba0c-5b8fbfe06c6e | -22.96555 | -51.59527 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 52.9 |
| 07f9a15a-2ff9-3c71-bd2f-8e83efcaf10a | -22.34444 | -46.7543 | 2025-09-18 04:19:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ebb8bb82-9add-38eb-9690-0955bcf055ea | -22.68788 | -47.45697 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c85397e5-c402-352f-83ee-eb85fc941e03 | -23.45988 | -47.68681 | 2025-09-18 04:19:00 | NOAA-20 | CAPELA DO ALTO | SÃO PAULO | Brasil | 3510302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b5b92af2-4dad-3213-b5a7-9c54de86d905 | -22.96938 | -51.59601 | 2025-09-18 04:19:00 | NOAA-20 | GUARACI | PARANÁ | Brasil | 4109203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 2a85d196-d798-3248-a832-8c24e06aa256 | -22.68001 | -47.50576 | 2025-09-18 04:19:00 | NOAA-20 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14438e3f-6f39-3cbf-894b-be90bdb0b7c2 | -22.66796 | -47.45321 | 2025-09-18 04:19:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3264b7ee-736b-3f36-bfcc-9e0b7cf2ae36 | -24.05038 | -49.09141 | 2025-09-18 04:19:00 | NOAA-20 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README27.md)
