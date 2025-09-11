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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66493f06-6637-3a3d-8f42-9f221e982c71 | -16.6052 | -49.77311 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4facd64a-f29d-3747-a9db-5bed6dbab5e8 | -17.55562 | -44.53984 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e032916-19ec-3a58-a506-50979197a457 | -16.55168 | -55.15118 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c968987f-6263-3f6c-a8cf-e7268ca9a087 | -18.01203 | -47.12814 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa752fe6-7a37-3e57-815c-40f1b24d7c5a | -16.34764 | -52.94132 | 2025-09-11 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3caac91-e788-3af6-89ae-9b38ccb2676f | -20.48646 | -54.91739 | 2025-09-11 04:49:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b747873e-5a07-323f-90a8-9224821445fa | -18.15096 | -48.0989 | 2025-09-11 04:49:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c3e986b-c85d-33c1-a25d-92ee97d23758 | -20.09141 | -44.48008 | 2025-09-11 04:49:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 50505677-9137-3bcd-8cdc-5d91870c833c | -19.99585 | -47.63783 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1225eae9-9c72-3db5-9448-5dc073a69b28 | -18.59651 | -43.87753 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee729376-073b-3565-bfca-ee2a0afedf2d | -17.79852 | -44.41 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd0a39f7-476f-3481-866a-8d1bdf916493 | -18.34655 | -44.36736 | 2025-09-11 04:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5e0aea9-9166-3584-854b-597e4bce44ca | -18.5044 | -47.30486 | 2025-09-11 04:49:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fbf1ef8-ad35-315d-ac5b-90c4d5aba22d | -22.9959 | -43.5006 | 2025-09-11 04:49:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b13afe8f-daba-3713-86bc-0c28f8ce7cf9 | -18.76467 | -48.54042 | 2025-09-11 04:49:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbf77d2d-1784-3216-9dce-3bd1af3011c4 | -20.15571 | -41.03046 | 2025-09-11 04:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fd2c9d6f-0e87-350f-a475-898ef0133473 | -21.43793 | -48.91358 | 2025-09-11 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c48c36ae-0a6e-30e1-afaf-b39ef5426834 | -19.95314 | -49.27203 | 2025-09-11 04:49:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| cf082f31-9d4b-3297-8478-04a089748fd2 | -20.48295 | -49.73109 | 2025-09-11 04:49:00 | NOAA-20 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54543f8c-f23b-33bc-8d7e-19e0933dabc0 | -18.01658 | -47.13061 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 115de583-60e8-31d0-bdc1-f51ae5dec997 | -17.7466 | -44.49908 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 503c2707-70bd-3d4f-bd66-654b863dee9b | -19.18623 | -48.79836 | 2025-09-11 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5d7530a-fd19-3333-a1f4-ace7905c4d64 | -16.50988 | -55.14866 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 408cccbe-2f3a-3559-9bf0-76036ae645f6 | -17.82889 | -46.73533 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15239d03-2c36-3b75-ad14-7db4820dde66 | -16.61924 | -49.78041 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89115213-ceec-3ef8-8b9b-74154afb3c8f | -19.99663 | -47.6318 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25bb39af-0d78-3a7f-ac85-3b61ce97c863 | -16.49166 | -51.9743 | 2025-09-11 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd09b651-a9a6-326d-a9a8-92918e70c5e1 | -17.27131 | -46.08236 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| bd7a347a-50b6-341d-8412-83f2f6abcd0d | -20.15771 | -41.03931 | 2025-09-11 04:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 22750eff-ca18-3909-8efa-b0138c59bbe0 | -17.93949 | -44.48588 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 783e718c-dbd4-3a0f-a075-f6354cc1bce5 | -20.53887 | -47.61716 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e02e471f-6f05-3655-b21d-f4925856544b | -17.94469 | -44.48703 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f58ef524-115d-3fa1-9b0b-d6feb1834ee1 | -16.6299 | -51.81997 | 2025-09-11 04:49:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80a0f3a3-f7ec-34ac-b86d-da0eb953e56b | -22.32144 | -48.82688 | 2025-09-11 04:49:00 | NOAA-20 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c51e28c2-e4fb-33f9-85ca-e36e99ea4f43 | -19.23229 | -48.00517 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 4d5758b3-cb52-3e43-9dac-253963451676 | -17.49827 | -43.75414 | 2025-09-11 04:49:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65279367-f7fd-3de4-b0af-42040fcf0b2b | -19.1867 | -48.79472 | 2025-09-11 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fe15454-3a2e-3e77-aa7e-a7b93555c727 | -22.31839 | -50.86399 | 2025-09-11 04:49:00 | NOAA-20 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6662f38-a587-3c0d-b83d-5a65d939e03a | -18.34942 | -49.32942 | 2025-09-11 04:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 12de9374-670c-37b6-814d-3d0c62acd42f | -15.87847 | -54.93435 | 2025-09-11 04:49:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 739a1c75-665b-3a1a-80b2-3cdd46c74202 | -19.97884 | -47.63114 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| aa6133e7-d5ca-3183-b7cd-30a7b0525274 | -18.34488 | -49.33391 | 2025-09-11 04:49:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67b805d0-5e8f-3b66-b4ef-2a11d73db371 | -19.2328 | -48.00106 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f552881-910c-385d-9a48-01c1ad4ec2f2 | -19.9931 | -47.62404 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ae7a7df-1438-34e1-8141-0e7584cb4a66 | -19.25875 | -48.00044 | 2025-09-11 04:49:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66849f54-f59c-3b74-b39e-937ab9b9900b | -17.84318 | -46.74442 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eb7074b-696b-3a22-adf6-4fb3da60c501 | -17.9499 | -44.48812 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ae043b6-bc6d-3419-b2a2-1b35cd0f8ef5 | -19.22806 | -48.00455 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5d8021ee-3260-3441-bc4c-d16106903989 | -19.99278 | -47.62655 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f99deee-a951-3805-9c60-9bcec34e2956 | -20.23506 | -43.58167 | 2025-09-11 04:49:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 935aa85d-dd77-3355-a427-37210d576841 | -20.05692 | -47.53759 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d37166e2-8c72-3ff0-ab66-b81ce04cd210 | -19.99927 | -47.61022 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 610628d9-d7d7-3304-99f8-374e48523367 | -19.03449 | -42.1493 | 2025-09-11 04:49:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f9db1eb-b514-3a45-bd6e-368b17af4d85 | -18.15978 | -48.09607 | 2025-09-11 04:49:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82c62cbc-0a0c-3157-8aa6-af807e3f0427 | -16.5139 | -55.14555 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 70e87583-9138-3ed8-a263-7f4a1ec18a1a | -17.37757 | -52.92996 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6a5cc19-a49c-3175-81d3-4efad22c1b2f | -21.77519 | -50.83666 | 2025-09-11 04:49:00 | NOAA-20 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8407e95e-697e-32ee-83ca-6441fae6f37d | -20.16146 | -41.0424 | 2025-09-11 04:49:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 75c9e2b5-5591-3320-bc40-3b0ff597768d | -20.08057 | -45.9881 | 2025-09-11 04:49:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 676c2d68-2551-3699-97fb-ac7bd294af65 | -17.27078 | -46.08667 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2a8ab18d-e40a-3e69-8b9f-882300ff77f1 | -20.91625 | -49.46936 | 2025-09-11 04:49:00 | NOAA-20 | BADY BASSITT | SÃO PAULO | Brasil | 3504602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 76250e4e-1086-3ff1-ba07-7b78d252b313 | -16.5445 | -55.17315 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 14614fb6-d6c8-399c-a407-3abe64af2fa1 | -19.65963 | -44.90132 | 2025-09-11 04:49:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cf3ce82c-8ce6-3de4-90df-a3a4bf11f455 | -21.12745 | -47.7313 | 2025-09-11 04:49:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c437f120-b81e-3721-b700-c74d03c3bdfc | -22.69127 | -47.31485 | 2025-09-11 04:49:00 | NOAA-20 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab4b963f-59ff-36d3-933f-3a9f99b9671e | -19.54954 | -46.94444 | 2025-09-11 04:49:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35a793da-5808-3ded-9efd-067827bee823 | -20.93517 | -45.79184 | 2025-09-11 04:49:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117db601-0048-37ff-a5df-88d4b183e60c | -20.53742 | -47.62427 | 2025-09-11 04:49:00 | NOAA-20 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 096a822d-93fa-39f9-87a5-d0b4faaed232 | -19.18719 | -48.79103 | 2025-09-11 04:49:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f83bb3e-54dc-3180-9cca-8c7d9e056c24 | -20.89314 | -48.46473 | 2025-09-11 04:49:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05f9f429-0067-39d9-b530-0044a6293bef | -19.70914 | -44.23312 | 2025-09-11 04:49:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f220c1ff-fc60-333a-9441-930ea9720072 | -21.43381 | -48.91303 | 2025-09-11 04:49:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c8c65732-612c-303e-a67b-14faa1b885ab | -20.93525 | -45.79221 | 2025-09-11 04:49:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b8cffd5-9ca5-37b2-be78-7578d886b99b | -17.84556 | -44.22076 | 2025-09-11 04:49:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ceea6d4-cfb3-3239-8b09-7cfc350bb957 | -17.25152 | -46.0886 | 2025-09-11 04:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9479f322-2814-3f17-891b-88061b8149ac | -19.79362 | -47.1655 | 2025-09-11 04:49:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b0029d-4cf8-3592-8697-1caae3d2d8c1 | -21.91387 | -47.90712 | 2025-09-11 04:49:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54e6c8df-4c05-3501-bf70-0ec1d09027df | -17.54972 | -44.54522 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ee4f9d5-ad71-3fd9-bdb9-4cc1920107a7 | -18.342 | -44.35973 | 2025-09-11 04:49:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5372dd58-85cb-3b9c-9531-194ca7262981 | -17.55904 | -44.5562 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfaa2e04-bc13-36a2-8233-6f4285389ecd | -19.98901 | -47.62054 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05313a21-680e-3e11-8b9d-805ae93c99f0 | -16.51266 | -55.15306 | 2025-09-11 04:49:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7cb45165-140c-3da0-a1b8-2075cf6bdb69 | -17.95584 | -44.48252 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a92721f-8a3f-3c3c-81f1-088dde32f647 | -20.12839 | -47.68856 | 2025-09-11 04:49:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03427c1a-961a-3812-9c8f-e4c2a88e65a7 | -17.2444 | -46.76024 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a978d51a-4496-3c1b-8c90-7f0bee9adc2f | -19.20464 | -47.98443 | 2025-09-11 04:49:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13fecd76-4356-3e0e-93c0-5009fe995794 | -18.59141 | -43.87271 | 2025-09-11 04:49:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e644362b-88f6-3471-8e46-d8d7a2e8712f | -19.03403 | -42.15422 | 2025-09-11 04:49:00 | NOAA-20 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 707d5deb-53ba-3f3a-b71f-1d085a3ec68a | -16.62979 | -49.7585 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 706be3df-fa5b-3e50-8643-7ad709779c37 | -17.24888 | -46.76083 | 2025-09-11 04:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 33a963c9-f867-3aaf-a684-af69cb047f23 | -18.00829 | -47.9974 | 2025-09-11 04:49:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e04efa1d-1b24-3ef0-8037-b10a8f0049df | -17.75219 | -44.49657 | 2025-09-11 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f674e16a-7794-381a-af1a-8011bbad791c | -17.38851 | -44.93035 | 2025-09-11 04:49:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ef85c28f-60a9-366b-a0e6-79dabe8130cf | -17.37701 | -52.93359 | 2025-09-11 04:49:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 32.1 |
| b5dcb17c-cdcc-30b1-8faa-b51870fca359 | -16.6186 | -49.78501 | 2025-09-11 04:49:00 | NOAA-20 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb174863-a734-3153-87a6-b3256b60773e | -17.5542 | -44.55232 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 754a8c39-d143-3a91-bf77-506e56b20dc6 | -17.556 | -44.53656 | 2025-09-11 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51fed87b-d02c-3e1c-a0a0-50001a5a6a40 | -20.44326 | -49.99705 | 2025-09-11 04:49:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5271f97-fd37-367a-bcec-ae8a53c388b5 | -17.84713 | -46.74984 | 2025-09-11 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 934e8154-0868-3260-be68-ecf78d7c0d6d | -19.9977 | -47.62255 | 2025-09-11 04:49:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README121.md)
