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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68b76730-363c-3005-95f6-085c8c9950a4 | -3.0827 | -47.0088 | 2025-10-01 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 956bff24-c205-3fce-b315-2cc8e83ef306 | -3.0826 | -47.0308 | 2025-10-01 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5645a9ee-903b-3c40-baea-01fe1e767d51 | -15.1615 | -49.082 | 2025-10-01 02:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 784d4cbf-7b3e-30eb-a2a2-7bdb3a0bbedf | -11.6476 | -47.4867 | 2025-10-01 02:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e65aadb4-14a4-3d7f-9510-6f189e1abccb | -23.1394 | -50.0891 | 2025-10-01 03:00:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| 8983861f-c6bd-3f3f-9255-cd81d7390599 | -16.2562 | -50.9275 | 2025-10-01 03:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| fe9fcbe7-2b35-3d32-97ca-e30e20471322 | -14.3519 | -45.9206 | 2025-10-01 03:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 86e9997a-0d1a-3ce0-aecb-0d34ccdaa2d4 | -16.3792 | -47.068 | 2025-10-01 03:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0635f5a0-2382-310a-813e-e9e7b13b2d71 | -22.5735 | -46.7755 | 2025-10-01 03:00:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| 1817be00-1277-3160-a773-bee6a7889509 | -23.1611 | -50.0608 | 2025-10-01 03:00:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.0 |
| 97d398be-0bcb-36d8-8e47-1b7b70edebf4 | -13.9396 | -48.1182 | 2025-10-01 03:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 34cf54f5-bad1-31b7-8740-e3c6523d2ccd | -9.2902 | -54.5242 | 2025-10-01 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| ce5b36ba-bc68-362e-9908-5e1ea2755ad3 | -14.8021 | -45.7946 | 2025-10-01 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 40461998-d875-36c2-b6fb-7d980d426e4e | -5.6361 | -43.9258 | 2025-10-01 03:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 05f1fc75-2f25-3f17-974f-74ecbaa7bc44 | -9.3089 | -54.5229 | 2025-10-01 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a15b647b-2321-3be8-92fe-2a24662a6d86 | -5.338 | -43.7623 | 2025-10-01 03:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| b6145312-1b21-3b85-bb74-e6c657a09ecf | -23.1604 | -50.0841 | 2025-10-01 03:00:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 197.7 |
| dcf34aaa-91dc-31a5-a201-4bf1ae056ca9 | -14.1926 | -46.1091 | 2025-10-01 03:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| c76f7c90-03b1-30f1-a79c-9035aa53d731 | -5.3382 | -43.7391 | 2025-10-01 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 7a103194-bfd5-3971-a8fb-b6807b1ef9fe | -12.2536 | -47.806 | 2025-10-01 03:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 57ee33c7-3e66-3008-afde-8fe4e9c1d145 | -3.1013 | -47.0082 | 2025-10-01 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 178.4 |
| 2ca5343c-1ea7-3c53-b1b5-9d170207f609 | -20.6309 | -46.2046 | 2025-10-01 03:00:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| c5ce0193-18ac-35a7-b3f9-82d87e43918d | -11.478 | -45.0868 | 2025-10-01 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| aada37b3-ecf2-361a-9203-2551ff75a292 | -23.1815 | -50.079 | 2025-10-01 03:00:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 101.1 |
| 8f5c29aa-0603-3695-a2ff-e6dba86b48ca | -20.0287 | -44.5283 | 2025-10-01 03:00:00 | GOES-19 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| e1a4b559-3c95-3f96-9374-878f1319c490 | -6.1674 | -47.2638 | 2025-10-01 03:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c3b38d0e-8cbc-33d9-937b-0a7f53b891de | -14.7831 | -45.7749 | 2025-10-01 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 82d5b24a-cac2-3045-a8f9-f6a3a6dbf770 | -14.7826 | -45.7981 | 2025-10-01 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| b5a0bdf3-2870-3189-83b8-42c86df43c79 | -16.2558 | -50.9494 | 2025-10-01 03:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 9fedc1c3-c3b2-3472-a5d2-9beef16a1e93 | -3.1012 | -47.0301 | 2025-10-01 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8e63fbe5-b186-391e-b6e8-9dc79f1190da | -5.357 | -43.7378 | 2025-10-01 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 85b1ad40-7ed6-337b-88e2-3b545108809d | -5.3195 | -43.7405 | 2025-10-01 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 28789629-e3db-3686-956f-c9e4a2c3ec59 | -3.0827 | -47.0088 | 2025-10-01 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 7ac3483b-7c42-3852-9e57-a96ef1b6669f | -23.1597 | -50.1073 | 2025-10-01 03:00:00 | GOES-19 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 555de26a-1dc8-3758-8c69-342fef147e92 | -14.8026 | -45.7713 | 2025-10-01 03:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| a49258e7-6588-387c-bc2b-963396328c3c | -11.4588 | -45.0895 | 2025-10-01 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 18f0e5c1-4913-33c2-84e3-a6834b27b83e | -14.8026 | -45.7713 | 2025-10-01 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 330f56c2-d67a-3e46-b82a-e51fcfb9b04c | -16.2562 | -50.9275 | 2025-10-01 03:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3d31e2bc-d7a7-3edf-8e59-bbb11eb98f73 | -13.3278 | -47.8313 | 2025-10-01 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 68e07aa7-14de-34e2-b53d-e6c8bbada547 | -11.8246 | -44.9669 | 2025-10-01 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| d714473b-fc02-334f-b80f-55a3d8837500 | -11.383 | -45.0543 | 2025-10-01 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 10270df5-16b8-39f4-b0c3-897798a2157d | -9.4394 | -54.5739 | 2025-10-01 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3fb9a83a-788b-3359-9831-b1c52a748f32 | -5.6361 | -43.9258 | 2025-10-01 03:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 1aa5e64f-2a09-376a-a623-0f40dbf1739f | -13.3471 | -47.8284 | 2025-10-01 03:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4451bbaf-51cd-3526-b09a-ea8086b16906 | -14.3519 | -45.9206 | 2025-10-01 03:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 868d1591-3958-37c6-a2ff-2bf8562ccec5 | -14.1926 | -46.1091 | 2025-10-01 03:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 28a2846e-0d84-34a2-bcd2-26cd26e7dbdd | -3.1013 | -47.0082 | 2025-10-01 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 3a83e2d8-3371-3e84-a0de-7d162a9703d6 | -5.6236 | -43.23 | 2025-10-01 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8c61ea36-eb5f-3bbb-acb7-d9b3e173f28f | -11.8438 | -44.964 | 2025-10-01 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| cd02c00f-c93d-3e6a-a4b9-a4abcd67b638 | -14.3514 | -45.9437 | 2025-10-01 03:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a0b50efc-b23e-313e-9798-bf297ff42d64 | -6.153 | -44.736 | 2025-10-01 03:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 981314cf-e762-3609-83be-616755930c31 | -12.2536 | -47.806 | 2025-10-01 03:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 223e373f-4fee-39b4-9a83-365487ec1278 | -11.8434 | -44.9872 | 2025-10-01 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 3ec1a5af-6fce-3075-afd5-5e4163101d63 | -20.6309 | -46.2046 | 2025-10-01 03:10:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 43.8 |
| e3eda40e-db94-3ff4-a163-6b8e81e536c8 | -11.8242 | -44.9901 | 2025-10-01 03:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 1c6e954e-8753-303a-9b3e-0a8e5620128f | -14.8021 | -45.7946 | 2025-10-01 03:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| f5b0841c-994d-3c8d-bb7c-2a3cfa61d2d7 | -3.0827 | -47.0088 | 2025-10-01 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8f3ef009-4721-3c53-88c3-14e912aa6282 | -3.1012 | -47.0301 | 2025-10-01 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 299e7033-565f-3c1b-bc7e-07b61ebd3a95 | -20.0287 | -44.5283 | 2025-10-01 03:10:00 | GOES-19 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| ea8ae57e-4136-32c0-8781-70abdf11cf7d | -14.70311 | -42.32336 | 2025-10-01 03:10:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 82f93d15-b326-3a45-9b4f-18c6d892cf00 | -12.58848 | -41.28836 | 2025-10-01 03:10:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27329b2c-9397-36f9-96ba-10be69d7a0fc | -18.3315 | -41.81248 | 2025-10-01 03:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| faa091bf-ed77-316c-99cb-c57b87e397e7 | -22.24932 | -43.42619 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 72447bf8-4d4e-304c-9d23-5a68a88f97e0 | -22.25612 | -43.42738 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0aa0a212-ae63-3c6e-9550-52ce484c02b0 | -18.60469 | -43.27549 | 2025-10-01 03:10:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 2eb22333-3c79-308b-be7b-df2f836da82b | -22.23735 | -43.41724 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a99871ff-27dd-3a7d-8dc6-2496a90fae60 | -18.60741 | -43.27341 | 2025-10-01 03:10:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| eba2532e-f406-3248-99c8-f3f97d73bfdc | -22.25496 | -43.43826 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| b712cca5-65f7-372b-9b13-33bbf229203d | -18.61181 | -43.27711 | 2025-10-01 03:10:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 380f38e9-ac0c-3cee-bbd7-7e5c5a1a0579 | -22.06853 | -43.08155 | 2025-10-01 03:10:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe5ab4aa-378f-3ed0-a9b2-ad1d5ccdb481 | -23.21034 | -45.12157 | 2025-10-01 03:10:00 | NPP-375D | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 95545af1-b3d5-3a0a-8000-2224eda452ee | -18.3382 | -41.81359 | 2025-10-01 03:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5500e657-a8b0-33a8-b308-2778469ab95c | -22.11449 | -44.69405 | 2025-10-01 03:10:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| e54d0944-245a-37ec-b0e5-7c01e170e7e8 | -22.11194 | -44.70388 | 2025-10-01 03:10:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 26d5f414-2324-3a57-8af1-c1e224ae78a5 | -12.58143 | -41.28665 | 2025-10-01 03:10:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 75767beb-111c-3edf-a164-dc350f33625c | -12.57834 | -41.28655 | 2025-10-01 03:10:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 30790074-e5ee-3599-b2fe-0b723b235242 | -15.53429 | -42.66837 | 2025-10-01 03:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 26af7e22-6cac-38b3-9c54-7badb84efdd9 | -16.42874 | -42.41204 | 2025-10-01 03:10:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a10639f-e17b-3474-ae16-2b93e84641c5 | -22.23908 | -43.41027 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d8889de7-5f1b-3bb2-890d-7400c2405d6c | -22.062 | -43.07967 | 2025-10-01 03:10:00 | NPP-375D | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9124d60c-b4c9-30c4-86de-4e0ef8ff9c6f | -22.25686 | -43.43077 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 43817b55-e828-330f-a942-67b9dbf6c7c0 | -15.81656 | -41.89176 | 2025-10-01 03:10:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d762f3b9-46cc-3f16-b300-645c3ce5ac6f | -18.33568 | -41.80832 | 2025-10-01 03:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a640722e-7bb5-38a0-8cc3-c5f21f6e5bb4 | -15.53597 | -42.66125 | 2025-10-01 03:10:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fa5c160c-f5bc-3a3e-bbb1-7a4a7745e41e | -18.32889 | -41.80756 | 2025-10-01 03:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1543a470-2d18-36d7-a97b-1e8d27eba52a | -17.00337 | -40.0266 | 2025-10-01 03:10:00 | NPP-375D | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 22ecfccf-d874-3ef9-bd27-4d0d69bc5de0 | -22.25015 | -43.4292 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 82d5072d-dde2-37ea-a4ed-55864692ef0b | -18.60558 | -43.28079 | 2025-10-01 03:10:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d50ce0ea-f0bb-352d-85a3-0b3ec6953ef9 | -15.81481 | -41.89932 | 2025-10-01 03:10:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 407957ae-48ce-3078-b836-a093cd36516d | -15.81804 | -41.89195 | 2025-10-01 03:10:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 245d5ad7-5fdb-3f8e-802b-47e7801ec44e | -18.33398 | -41.81551 | 2025-10-01 03:10:00 | NPP-375D | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 269b60fb-f8dc-3212-8876-0a62edc5c64c | -15.81634 | -41.89951 | 2025-10-01 03:10:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 60e04d35-48d4-3a4c-8903-3587acf58ae6 | -22.1192 | -44.70531 | 2025-10-01 03:10:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| b14b6472-9954-3d8b-a2ac-a82028fe167d | -22.25428 | -43.43479 | 2025-10-01 03:10:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 67ff071d-164f-3c2c-b873-1c8f1830ca18 | -20.34953 | -43.33944 | 2025-10-01 03:13:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 21192efa-8535-3f96-a5a1-8d934b1450ea | -20.69851 | -41.57264 | 2025-10-01 03:13:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bd61eaba-2767-3268-8376-07093e2233e5 | -20.83322 | -43.02276 | 2025-10-01 03:13:00 | NPP-375D | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 436ebfdd-8b3f-30b7-a6be-1b39eae762a2 | -18.95863 | -43.71637 | 2025-10-01 03:13:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16259319-45df-3ec1-ba72-b734bfc158bc | -19.93176 | -43.89358 | 2025-10-01 03:13:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0ba65185-b80b-36c4-bfa9-e6d4ac81eda7 | -19.85584 | -42.58735 | 2025-10-01 03:13:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
