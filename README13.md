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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2737edb2-33ae-32a1-b053-0a5c257a8a71 | -17.61085 | -46.60118 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 749276f1-8b18-3e66-bb3a-81fb96daa91a | -21.02476 | -48.41687 | 2025-10-23 04:10:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd2832c-5e39-3be0-8421-677e09b671e3 | -18.23293 | -47.42179 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 731da700-c2c8-3652-b562-28b5044c5a14 | -20.76349 | -43.21627 | 2025-10-23 04:10:00 | NOAA-21 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 659c25cd-c9aa-3e33-9be0-da526b95c234 | -17.59973 | -46.60328 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536683be-6781-3bba-a4de-3bcfbe740dac | -17.55158 | -51.03954 | 2025-10-23 04:10:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e299898d-67cf-3864-a4b0-9f74382b806d | -19.95939 | -45.60222 | 2025-10-23 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2618eaa2-139a-34d8-9a2c-ebc8b9189607 | -15.59724 | -45.90241 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d71641e7-1e35-33d9-a6d3-59157e7462ea | -19.78988 | -50.97979 | 2025-10-23 04:10:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da67c335-4b58-3b35-8e94-99c267914026 | -17.60183 | -46.61194 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82be743d-2769-3f11-9c2c-1301b3e348fa | -17.86488 | -54.49974 | 2025-10-23 04:10:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5303bd60-e038-3054-937c-2cc81a606591 | -17.62203 | -46.61985 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27f6e316-d7e2-3b7c-b722-0d2dd2641264 | -17.59627 | -46.6234 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74df6955-7650-36a6-ac09-9418dda036ea | -13.90835 | -48.3633 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fb1d83c6-e104-3c03-af1f-74ee1b8a0d79 | -21.95351 | -42.9257 | 2025-10-23 04:10:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4add5dfb-6d86-3ae2-a348-85b2ac8c59a5 | -13.89282 | -48.37394 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cbe5f32a-dbb1-3b3b-a84b-401dcbd34ff6 | -21.95407 | -42.92184 | 2025-10-23 04:10:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 5ad9a867-f6d3-302e-a697-573c5903633b | -17.55511 | -51.04528 | 2025-10-23 04:10:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d57143b3-21bc-37f3-894d-31a3b0d9ab4e | -17.62409 | -46.60777 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0553b0ea-40cf-3b18-821f-ce7bbb53ced0 | -14.84203 | -54.22381 | 2025-10-23 04:10:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 93397f75-61e5-36ef-8e49-e0a06b61ccc9 | -13.89345 | -48.37037 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 611bc399-428d-3fa2-86de-42ec69a72166 | -18.18685 | -46.1935 | 2025-10-23 04:10:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 175254e0-1b6e-3ea3-9eed-bf7734b17f94 | -15.52046 | -50.13377 | 2025-10-23 04:10:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0f965f5c-0b08-3eb1-b2db-2922c07f56d6 | -20.63669 | -42.71432 | 2025-10-23 04:10:00 | NOAA-21 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d1debf78-34b3-3334-9064-9bd2c04eba65 | -15.59526 | -45.9143 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e6b30683-daac-3b61-ad79-8e5c33d11f35 | -17.40208 | -47.52074 | 2025-10-23 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9675bcf-2284-3712-a87b-ac0b8fd0fcbf | -17.61648 | -46.63128 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d992074-740d-3bb9-8424-2a11f4045f52 | -17.55399 | -45.76944 | 2025-10-23 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 68d4358b-e269-3918-90ea-8f87b1e699f6 | -16.30488 | -45.87628 | 2025-10-23 04:10:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b01327a7-e895-3c83-b8ce-515b9e11c33f | -17.61713 | -46.60649 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7793c72f-c527-350f-a48f-bfe3fc4ba23c | -18.69427 | -47.04803 | 2025-10-23 04:10:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe8b10b3-15b7-3c81-ac39-1aae98186bb4 | -14.69313 | -52.8137 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4de183e-33c0-3cc9-8a31-7c3ffa31bfa2 | -13.89787 | -48.37529 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9326fb3d-fbe3-3354-9501-fb4465f29f10 | -19.96332 | -45.59912 | 2025-10-23 04:10:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfbb746c-4210-37f6-a4e3-1d408cc87003 | -17.60603 | -46.62935 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 44a35310-4023-3a48-964f-e9bc5c1f102e | -15.51548 | -45.96484 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0fedae8f-2e90-338f-bc71-a43486b41e9f | -15.59789 | -45.89845 | 2025-10-23 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2eb035c4-77a0-3ad7-a0de-03adf2a88e5d | -18.14072 | -44.45982 | 2025-10-23 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09fb9d7f-e89f-3054-ad42-00265b2c4183 | -15.92006 | -48.32558 | 2025-10-23 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7d19113-77f8-38ed-b4f4-b2ca79801038 | -16.05222 | -45.12674 | 2025-10-23 04:10:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2571e851-5f34-37a6-b91b-da0146b0992f | -18.71706 | -46.82881 | 2025-10-23 04:10:00 | NOAA-21 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce613de7-332d-380c-ab8b-7b50d3a8f9ad | -14.69313 | -52.81371 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 735d1976-f805-3a1b-920f-7832f1e58ea6 | -17.60813 | -46.6381 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5739bad-51c4-3fd3-b4f2-a1518f48a16a | -17.21328 | -47.65231 | 2025-10-23 04:10:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89dd2f23-ce4b-3fa3-8da9-5edcbbed0a89 | -14.28053 | -48.07215 | 2025-10-23 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b30914f2-4e08-39ab-aeaf-16c7381eecc2 | -14.26584 | -46.296 | 2025-10-23 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61548dc8-40c4-34a2-be10-f4a9987b9955 | -20.98051 | -47.36179 | 2025-10-23 04:10:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8d34a04-5288-3e3a-af63-9618a3110422 | -17.6262 | -46.61647 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 313cb897-812e-30cd-bf9e-91c963ddbbd3 | -18.13878 | -52.97336 | 2025-10-23 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79f1d902-bd15-312b-a0cc-b41683bbd21e | -21.95695 | -42.92623 | 2025-10-23 04:10:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 364f1d6c-0e4d-3a5a-b29b-87e403fdf398 | -19.26521 | -51.97854 | 2025-10-23 04:10:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b3fd68f-0c1d-3c4b-b511-0250da251eb6 | -17.62757 | -46.60841 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6827d1b6-3234-3e11-9208-fc01679747ba | -19.38411 | -48.32047 | 2025-10-23 04:10:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa1b1c91-95dc-3f32-9f23-af9725b22cd6 | -16.47573 | -46.4735 | 2025-10-23 04:10:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f40bd95-d4a3-3745-ba7c-cbeca0b95f74 | -17.59976 | -46.62403 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d83559fe-4564-393b-92b4-8569af21acd4 | -19.05073 | -44.92319 | 2025-10-23 04:10:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d393b08-3266-349a-b3a5-7a3c8f147fd0 | -17.61021 | -46.62596 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f412c955-31fd-3409-803b-7343b373f1b1 | -18.17611 | -46.69654 | 2025-10-23 04:10:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5c046e7-f542-30c5-bc73-fe1f854c2c32 | -18.14377 | -52.97449 | 2025-10-23 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b164f35c-afe7-3e1d-a5a1-f2da1cb18865 | -21.41388 | -44.27437 | 2025-10-23 04:10:00 | NOAA-21 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 620ec0cb-d08e-3029-a6b8-c01ef72b1a7f | -18.22576 | -47.4205 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f40927-97fe-340a-bae9-57272cc9776f | -14.90004 | -46.2454 | 2025-10-23 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bcb78dd1-a20f-3808-a8e0-b74547f7a302 | -17.62477 | -46.60374 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f8a4ce1-2988-3e55-8c71-aaa07911d210 | -17.21328 | -47.65232 | 2025-10-23 04:10:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b61e9b11-57a6-39d0-8270-abf50c1c7bdf | -17.62134 | -46.62386 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2f5f2be-0780-36ca-8fee-ba7e655a2bfa | -20.98052 | -47.36179 | 2025-10-23 04:10:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9b9cfb0-a2bf-3506-b586-3e64095dbc0e | -17.62831 | -46.62515 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f826456e-7ca2-3021-81c8-b93104ccba6d | -14.26511 | -46.30024 | 2025-10-23 04:10:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba235155-3f55-3db5-a70a-7fc1b08aa30e | -17.59835 | -46.6113 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e088fb-ee53-383d-b6d2-c566131e4673 | -17.62688 | -46.61244 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14b595c0-d43f-324b-97f6-3219a2560d54 | -19.26408 | -49.3522 | 2025-10-23 04:10:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a55910e8-2865-3cb2-82a3-133b242a1ded | -17.61717 | -46.62725 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b9429cc-3a38-37db-82ba-eb2aa803a6b7 | -17.65276 | -46.65044 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 805ad560-f675-3e3c-b614-e0ca67838c75 | -20.21779 | -46.33543 | 2025-10-23 04:10:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10779104-c471-3629-91f7-d09c6c2ad836 | -13.90774 | -48.36667 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 764b8353-f8f6-39ed-94b6-2c4141e1659c | -21.84547 | -43.71007 | 2025-10-23 04:10:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 23a78734-4984-38fb-be08-de7e4cd5d691 | -13.8969 | -48.37433 | 2025-10-23 04:10:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8b1a7d3-5300-38bf-bdaa-e37887d312f4 | -16.08305 | -51.41315 | 2025-10-23 04:10:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be77584c-194e-37f8-9355-63ed2ff97e83 | -19.76696 | -41.29701 | 2025-10-23 04:10:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0045c72d-4008-3aea-8083-c143c507dc54 | -17.61231 | -46.63469 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80abc24c-80b4-399d-a443-3cef8c54e8a8 | -18.22934 | -47.42113 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c558e824-49ca-3843-ae77-1a81e79abf98 | -17.62899 | -46.62114 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03a2b013-4504-3027-90bb-a1c8344a2f0c | -17.61992 | -46.61116 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e76eb5d-307c-3195-a4b6-7fa8535f95a6 | -18.58304 | -44.50283 | 2025-10-23 04:10:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2df100d5-3f5b-346d-8e76-df17d9b72a60 | -17.55341 | -51.04233 | 2025-10-23 04:10:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 56c9de27-e6de-3173-9b17-73ac4749b03f | -13.47853 | -47.94713 | 2025-10-23 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b783762c-1d5b-3813-acca-90ba20594b29 | -20.97705 | -47.36114 | 2025-10-23 04:10:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76849aa5-1278-30e9-bf9e-ab57e6047010 | -17.60047 | -46.64085 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b56ff033-1adb-3aa8-8bc9-1578a7309274 | -17.59768 | -46.63617 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e828a411-2ddd-33c5-8bde-0b7986b14b13 | -18.22934 | -47.42112 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5a302b0-93b7-33e1-9457-48d00242ca66 | -15.91617 | -48.32494 | 2025-10-23 04:10:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| feed7142-dd25-3082-9ba7-fec36b6f254e | -21.95639 | -42.93014 | 2025-10-23 04:10:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0d780cdf-c991-30bc-9450-bff7d6fc5c77 | -17.60185 | -46.63276 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dbdf1d7-7c32-3c30-9ba2-6b84b82af397 | -18.58087 | -44.92381 | 2025-10-23 04:10:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfb28348-fa83-3ed4-9785-aab62cd860c8 | -17.60673 | -46.62531 | 2025-10-23 04:10:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc4dc980-4fa2-3b83-9ceb-bb0a88bda1e5 | -18.23084 | -47.41257 | 2025-10-23 04:10:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 669218ff-54ef-36e4-a686-4c429714e4a3 | -15.6051 | -48.05564 | 2025-10-23 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1bebfa4-6863-336e-97e9-567ff2226a7c | -18.69287 | -47.05629 | 2025-10-23 04:10:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10c4dc83-733c-3a0a-a2e7-49eb76ef657c | -19.79667 | -50.96772 | 2025-10-23 04:10:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4f719a81-6866-3e66-bc59-a60071904048 | -19.52664 | -44.73323 | 2025-10-23 04:10:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README14.md)
