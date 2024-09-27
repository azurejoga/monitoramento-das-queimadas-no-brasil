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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8444fcc-4ef8-399b-ac26-84f73c4dc9a5 | -19.373199 | -42.561298 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d7e51b8-f52a-3867-9b41-625debc6974f | -19.3752 | -42.569698 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbf95f57-8f18-3a19-9098-8f4d32b306b4 | -19.3771 | -42.577999 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19a4ca6a-0297-3911-94d7-3538fba5fe00 | -19.379101 | -42.586399 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69444d00-1b34-3a4e-8a1a-81285acf83ac | -19.3615 | -42.5555 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fefa80d0-79bd-3e82-8c87-34d83bc08b76 | -19.363501 | -42.563801 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b07731b4-96c9-3616-afa0-740a5ccd0474 | -19.365499 | -42.572201 | 2024-09-27 00:31:45 | METOP-B | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 224021d3-2b28-39eb-bd1f-8bc9f5611cba | -19.6399 | -44.170101 | 2024-09-27 00:31:46 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d9deca9-0910-3616-a324-7890aa8c514e | -19.6416 | -44.177601 | 2024-09-27 00:31:46 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d309502c-20ab-3216-bd71-b8807b0301a9 | -19.643299 | -44.185101 | 2024-09-27 00:31:46 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5c8267f-fbe9-33c7-b09f-2d4fa7de0ad8 | -19.630199 | -44.1726 | 2024-09-27 00:31:46 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c996dd46-31c3-3c58-828b-1bf967d28b22 | -19.631901 | -44.180099 | 2024-09-27 00:31:46 | METOP-B | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37998fa5-2592-3039-833f-b3e454905f44 | -19.924299 | -45.742401 | 2024-09-27 00:31:47 | METOP-B | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b0824266-4a43-3c1e-a18f-a5604e714723 | -19.9259 | -45.749699 | 2024-09-27 00:31:47 | METOP-B | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01540c43-a705-31ef-a0f1-06c2105408d0 | -18.898199 | -41.997299 | 2024-09-27 00:31:50 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6c0b85c-3188-30e0-a667-3ac15442ba5c | -18.900299 | -42.006199 | 2024-09-27 00:31:50 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9a3ca42-3290-3420-b872-e132c860f799 | -19.986099 | -47.152401 | 2024-09-27 00:31:51 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1522b3c9-8dbc-3abc-bef2-d5059bc25971 | -19.0931 | -43.446201 | 2024-09-27 00:31:52 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f94ce495-d5d8-36b8-b8f3-a7788fdebb6a | -19.0949 | -43.453999 | 2024-09-27 00:31:52 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9336c2b3-4909-3e02-8964-6dd9a68b5a17 | -19.6126 | -45.870499 | 2024-09-27 00:31:53 | METOP-B | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e42cdc47-17a2-3586-8cb5-4d86c7e41cdf | -19.578199 | -46.0933 | 2024-09-27 00:31:54 | METOP-B | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8d385094-6068-364b-89be-b647836a3da9 | -19.5798 | -46.100601 | 2024-09-27 00:31:54 | METOP-B | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63ad6b35-e6bb-3051-a779-21cce5410472 | -19.5814 | -46.107899 | 2024-09-27 00:31:54 | METOP-B | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 471eb94f-12d0-3687-b185-cbf518d46327 | -18.700001 | -42.077999 | 2024-09-27 00:31:54 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10f1e375-7406-3b87-afff-98f44643bdd4 | -18.702101 | -42.086899 | 2024-09-27 00:31:54 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7a582e7-b121-3b85-a004-c4d8b345f266 | -18.704201 | -42.095699 | 2024-09-27 00:31:54 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a5bec64-b708-3204-a9b5-9c5161ee8a4d | -19.7609 | -47.252602 | 2024-09-27 00:31:55 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8c504d14-1c57-38d6-ad6f-9d0f2e2c3bb1 | -18.952101 | -43.506802 | 2024-09-27 00:31:55 | METOP-B | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eb64be8a-b520-383f-b3b7-d6a9166d6210 | -19.908001 | -48.324902 | 2024-09-27 00:31:56 | METOP-B | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b6097da5-218f-3036-a6b6-e562c6590c05 | -18.872 | -43.427799 | 2024-09-27 00:31:56 | METOP-B | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 107383d7-debf-3c02-9638-89cdf7a76ea0 | -19.7537 | -47.765202 | 2024-09-27 00:31:57 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 38c28c75-2a09-3bb4-adb3-2a8e035f07e2 | -19.597799 | -46.961498 | 2024-09-27 00:31:57 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8f08096b-ff1e-3a64-835b-a13759186fa0 | -19.5994 | -46.969101 | 2024-09-27 00:31:57 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 59a7efe6-f467-32a9-ba81-b169451205f5 | -18.4886 | -42.189899 | 2024-09-27 00:31:57 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83851668-93fc-3d07-b736-b88cd917836b | -18.490801 | -42.198799 | 2024-09-27 00:31:57 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b84accc-1503-3eb3-9557-36283e955d9e | -18.492901 | -42.2076 | 2024-09-27 00:31:57 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8141fb0c-0337-37b2-9572-5d9464aa74cb | -18.478901 | -42.192402 | 2024-09-27 00:31:58 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d51fba7-6ca3-38f2-b606-a7c46e851ad4 | -18.481001 | -42.201302 | 2024-09-27 00:31:58 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4936f0d3-d058-38c9-abe7-72f9318afe64 | -18.483101 | -42.210098 | 2024-09-27 00:31:58 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40eafaca-8c9b-369b-ab31-e8ae99fdf2fa | -18.7626 | -43.896599 | 2024-09-27 00:31:59 | METOP-B | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c37f2fd5-f51f-3030-ae7e-066b98887b4f | -18.608 | -43.403301 | 2024-09-27 00:32:00 | METOP-B | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45adc719-b908-3ba7-889d-9991d90016e4 | -19.5303 | -47.8745 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e60ebc7d-2e22-378d-ad98-df648d688cc1 | -19.532 | -47.882599 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e8a3c623-8c92-3d0e-aa36-3f6bfa0e49c8 | -19.5336 | -47.890598 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5d519f62-0dad-3693-a948-d539a6420bc5 | -19.5189 | -47.868599 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03b36ef2-32cd-3121-83eb-134b87c77853 | -19.5205 | -47.876701 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 74066e7e-d7b2-34a6-b392-6495554aef5a | -19.5222 | -47.8848 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0494ab-2e74-3757-b806-ac2f76e2e36b | -19.509199 | -47.8708 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51ef0439-85da-3afa-8829-01105a399ac5 | -19.510799 | -47.878899 | 2024-09-27 00:32:01 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac5378c5-3335-3b01-a57b-6427b04dfc2b | -19.479799 | -47.877399 | 2024-09-27 00:32:02 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 86a0240f-8c66-38cd-ba1d-dc8464642cda | -19.4814 | -47.885399 | 2024-09-27 00:32:02 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37d8bc1e-70fb-3e75-87d8-ef1988f6c575 | -18.3293 | -42.608601 | 2024-09-27 00:32:02 | METOP-B | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f1c9c48-edd2-34b4-bed1-104b33c954ed | -18.933701 | -46.299099 | 2024-09-27 00:32:05 | METOP-B | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 897d4a41-0d85-3a3e-b1c5-37819d040e9e | -17.915701 | -42.130901 | 2024-09-27 00:32:06 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1530e62e-cc3a-379c-ad7b-6b43185521e9 | -18.7862 | -46.618099 | 2024-09-27 00:32:09 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4370070-15f4-32ed-ba8f-a7acebd73e47 | -19.2967 | -49.6698 | 2024-09-27 00:32:11 | METOP-B | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 25442716-a733-3e7d-b6b7-2cb8273ef7a2 | -19.2985 | -49.679401 | 2024-09-27 00:32:11 | METOP-B | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1bccafdc-1346-3a1c-b47d-e332c7a76a62 | -19.3004 | -49.689098 | 2024-09-27 00:32:11 | METOP-B | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4be41a34-5d39-3b9a-a61d-b903e3b1263c | -17.9891 | -43.855701 | 2024-09-27 00:32:12 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0a083d14-f85f-3afb-91ac-1360ab3cce57 | -18.058901 | -44.3424 | 2024-09-27 00:32:12 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c5317014-6867-320c-a112-17bcb364c917 | -18.0474 | -44.337399 | 2024-09-27 00:32:13 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63d718f7-e6f0-3a08-a15f-ac789ce035bc | -18.049101 | -44.344799 | 2024-09-27 00:32:13 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4ec3255e-3adb-3d0b-8a41-69984e54688b | -18.004999 | -44.3321 | 2024-09-27 00:32:13 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b499336-be09-33ac-9e18-f947540715f3 | -18.5238 | -47.075199 | 2024-09-27 00:32:15 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 558c687a-f802-371d-aad6-e29fd85c5b3a | -18.5058 | -47.0872 | 2024-09-27 00:32:15 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed2555c1-93ae-374f-820d-c1c96ce4d55a | -19.006201 | -49.436401 | 2024-09-27 00:32:15 | METOP-B | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 64709d8a-081d-3deb-86ed-939257b666bb | -19.007999 | -49.445702 | 2024-09-27 00:32:15 | METOP-B | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7e7d2cc-6eb7-34f2-bc27-6e72e9beb312 | -17.052799 | -41.134102 | 2024-09-27 00:32:16 | METOP-B | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b349edf1-3126-39f3-b882-dac1364841fe | -17.0553 | -41.1446 | 2024-09-27 00:32:16 | METOP-B | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a7136ea-5a77-36b5-b6ca-206b9e0110f3 | -18.6017 | -48.791 | 2024-09-27 00:32:19 | METOP-B | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df8416c7-60e7-3acd-b7f6-ddca72898806 | -18.6035 | -48.7995 | 2024-09-27 00:32:19 | METOP-B | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8655e460-8a79-3310-82b7-f96fa6e134a4 | -18.5919 | -48.793201 | 2024-09-27 00:32:19 | METOP-B | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5363c777-d33a-3e6d-a1fe-9a7d13c7387e | -18.5937 | -48.801701 | 2024-09-27 00:32:19 | METOP-B | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a575c20f-e0e9-35eb-b887-77933023f008 | -18.5954 | -48.810299 | 2024-09-27 00:32:19 | METOP-B | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b52fdcf9-5d7c-3b2d-8d5b-c3446230783a | -18.5875 | -48.974201 | 2024-09-27 00:32:20 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88d10a73-5e33-34f2-81fb-8f7f3efb8b26 | -18.096399 | -47.432999 | 2024-09-27 00:32:23 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be3cd1d2-1d73-31ff-b101-eda47ed91f40 | -16.8148 | -41.814701 | 2024-09-27 00:32:23 | METOP-B | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 492109d5-3002-3586-bc51-bea1dc5e1c5a | -18.397699 | -49.301399 | 2024-09-27 00:32:24 | METOP-B | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 830a56fe-c791-3b46-8996-fe042daac6d0 | -17.036301 | -43.2225 | 2024-09-27 00:32:25 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e6d0e511-8597-35ad-bd94-8c90ee4d3b34 | -17.0383 | -43.230701 | 2024-09-27 00:32:25 | METOP-B | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c18c39b-3495-312b-ba76-945005a10f8d | -17.503201 | -47.007999 | 2024-09-27 00:32:31 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5f7009d-c8b1-3f63-b859-c5716e4267f3 | -17.2414 | -46.271999 | 2024-09-27 00:32:33 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 90ed8653-8f8c-3b3d-bc58-a37210524693 | -17.242901 | -46.279099 | 2024-09-27 00:32:33 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4397cc95-3938-3fa0-a3d2-e1bf42758c4e | -16.8876 | -45.3232 | 2024-09-27 00:32:35 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82cb788c-d45b-3f34-bc44-7501c4185b57 | -16.886 | -45.316002 | 2024-09-27 00:32:35 | METOP-B | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af3b96df-b873-3530-bc98-2f243bade46b | -17.1534 | -47.631802 | 2024-09-27 00:32:39 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 88379b30-89cb-34f0-9dbf-d740da528b56 | -17.155001 | -47.639301 | 2024-09-27 00:32:39 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7fe9bf-ac43-3203-8d1b-c5d6d51e476b | -17.156601 | -47.646801 | 2024-09-27 00:32:39 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 36f3a3ba-7b21-3487-8223-3fa7fc4dd0c3 | -17.2237 | -48.014198 | 2024-09-27 00:32:39 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c4d77f60-b7c5-3ce1-baad-71f86e259926 | -17.2253 | -48.0219 | 2024-09-27 00:32:39 | METOP-B | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a6c985ce-9f6d-3cff-838e-ddd3f5ccd227 | -16.0399 | -43.601898 | 2024-09-27 00:32:42 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9835cef8-82e7-3222-b76b-e584a688699e | -16.0418 | -43.610001 | 2024-09-27 00:32:42 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 93fcb18c-cff9-3e50-a4a0-9e8ca9099431 | -16.840099 | -47.702801 | 2024-09-27 00:32:44 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8871ef25-81c4-3bc5-929a-f90369f30f30 | -16.8417 | -47.7103 | 2024-09-27 00:32:44 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 858e69d7-6ec7-3a95-92dd-58e4f8c7b0fb | -16.8496 | -47.747799 | 2024-09-27 00:32:44 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7c1caef9-ef92-3f36-9d07-19e9aab8e824 | -16.8512 | -47.755299 | 2024-09-27 00:32:44 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff1a68fc-0c9e-3246-9acd-f4f55fd4a948 | -16.834999 | -47.727501 | 2024-09-27 00:32:44 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bffe62ef-f08b-3524-adea-328d8ca42843 | -16.836599 | -47.735001 | 2024-09-27 00:32:44 | METOP-B | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52ce43e1-14d5-33c3-9e47-252d2fa196f0 | -16.5499 | -46.923199 | 2024-09-27 00:32:46 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4fd749e-9e5c-3bfc-b5f6-f5d0089fd9ec | -16.5303 | -46.9277 | 2024-09-27 00:32:46 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
