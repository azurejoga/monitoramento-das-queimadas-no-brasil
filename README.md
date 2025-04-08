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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a90104c-c9d0-32b7-8fa8-c0a65534bc31 | -17.62354 | -46.62169 | 2025-04-08 00:05:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 604ee411-0449-3724-8f8a-24a028781cfe | -17.91988 | -45.53164 | 2025-04-08 00:05:00 | TERRA_M-M | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 6cfe30b1-211a-32da-bc7f-dc3b2ef01f97 | -14.20299 | -44.35682 | 2025-04-08 00:05:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 106c429b-83f1-37fc-914c-56ee1965a730 | -13.61241 | -43.97692 | 2025-04-08 00:07:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c1a59c9d-3434-3f68-9b2f-112c50072271 | -13.1899 | -38.90642 | 2025-04-08 00:07:00 | TERRA_M-M | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| 3bd9723d-ccd6-3e67-882f-ed271b833135 | -13.28429 | -41.43332 | 2025-04-08 00:07:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 4c7030c0-fef5-3402-b702-1daf4b0c4ad2 | -13.2859 | -41.44592 | 2025-04-08 00:07:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 6d3f3364-5d5d-3d56-a314-64effeade70c | -6.879 | -41.68606 | 2025-04-08 00:07:00 | TERRA_M-M | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 64ed2bd1-9c9d-30f7-8893-df75a640bf98 | -13.41494 | -44.17419 | 2025-04-08 00:07:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6d70bb8f-3b82-36f4-844f-df86e0e70f25 | -6.68693 | -43.56729 | 2025-04-08 00:07:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 174afb88-937a-35aa-951e-71efdb24434c | -13.27563 | -41.44733 | 2025-04-08 00:07:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| f694a0c0-db1d-3a44-8271-907d79856cdb | -11.91547 | -38.13701 | 2025-04-08 00:07:00 | TERRA_M-M | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3b278820-9d01-3a81-86ca-45731803bbed | -10.46124 | -38.20908 | 2025-04-08 00:07:00 | TERRA_M-M | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 1a74f169-2b9e-3188-a74a-b6627abd8da0 | -12.26901 | -41.30606 | 2025-04-08 00:07:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5de8ea95-5ee9-30be-81bb-adc674c2323a | -6.68481 | -43.57338 | 2025-04-08 00:07:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6731e230-e75f-33f6-819b-06d8799201cc | -13.27402 | -41.4347 | 2025-04-08 00:07:00 | TERRA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 76e11a5d-3bde-3901-8948-fae94e79ec6e | -8.57765 | -36.44149 | 2025-04-08 00:07:00 | TERRA_M-M | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1ce60ed9-1f3e-397c-87cb-2d3571ca1421 | -12.26805 | -41.3004 | 2025-04-08 00:07:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 20.3 |
| d67da6c1-e321-3391-9746-4d31b821b4d4 | -13.19116 | -38.91579 | 2025-04-08 00:07:00 | TERRA_M-M | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 83747d7c-c3dc-32ba-849c-76473e386ca6 | -12.11328 | -45.62751 | 2025-04-08 00:07:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a26cc97f-66a2-3ffa-ac25-7da558ac08cf | -12.26748 | -41.29438 | 2025-04-08 00:07:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 1a877a51-01d4-3bb6-9f84-b48aa24a5cac | -3.12055 | -40.99361 | 2025-04-08 00:09:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cf6cd4bf-592d-3b76-afaf-5154a32c7a86 | -20.5986 | -56.0369 | 2025-04-08 00:34:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ebc9e4f1-dd58-3850-b922-d054691150ca | -22.4823 | -51.700401 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a6a28ae-ff18-3eee-a498-593c4b7cb147 | -19.176701 | -47.8106 | 2025-04-08 00:34:00 | METOP-B | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 02523405-9824-3e97-a60d-9e0ac71e8be1 | -19.9482 | -47.5714 | 2025-04-08 00:34:00 | METOP-B | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df386a83-70b2-3bed-b631-01271ca61b40 | -22.4839 | -51.708599 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f47daf0-3c7e-38f2-bf83-d6a4771e90cd | -22.4725 | -51.702702 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8c04234-2b1b-37b5-8938-f241aa3ec26e | -22.479 | -51.683899 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b174e02-77a2-3a3d-a851-9bed7d35a353 | -22.4741 | -51.710899 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfd7a070-a4c7-3607-9785-9b4ce1d34fc4 | -21.781601 | -55.304001 | 2025-04-08 00:34:00 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 142c3beb-1672-3cb5-9eaa-9b7c7325a691 | -17.929501 | -45.522701 | 2025-04-08 00:34:00 | METOP-B | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa4873a1-97b3-3b47-871d-cf4d8f4f554b | -22.4904 | -51.689999 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ba64d56-d1e4-378d-9fac-02d315bbdb9c | -21.7913 | -55.301998 | 2025-04-08 00:34:00 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9614cd71-0bb8-3085-8ddc-91f1d818b875 | -19.958 | -47.568901 | 2025-04-08 00:34:00 | METOP-B | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0ba971c9-2d04-3af8-ad3a-a3cc525844dc | -21.793501 | -55.314201 | 2025-04-08 00:34:00 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f325aba0-db9a-3ab1-a7d3-0f466429de28 | -22.4921 | -51.6982 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15ba2cae-3368-313b-b343-8d49b48de188 | -17.6332 | -46.6959 | 2025-04-08 00:34:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 19dabe72-a428-3147-b4ab-3663e7ded0f6 | -13.283 | -41.410099 | 2025-04-08 00:34:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fc6c4059-3886-36e5-9f0a-c4e550cbc8a4 | -15.2726 | -47.467899 | 2025-04-08 00:34:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a6f65f0-67e0-3fc3-9be2-3667abe81e27 | -13.2889 | -41.4324 | 2025-04-08 00:34:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 09283584-d795-332f-8264-750a6a04072a | -21.596001 | -48.607498 | 2025-04-08 00:34:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef6c72e0-65f8-300f-b79c-6554236fc57e | -22.4708 | -51.6945 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23e3414a-2c12-3a94-abc6-8626b3148068 | -17.6376 | -46.627499 | 2025-04-08 00:34:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ddd9fa63-8682-3970-a8e1-95d1c58a30d4 | -15.2628 | -47.470299 | 2025-04-08 00:34:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c22b9e6b-3175-3174-8842-16988ae88a1f | -20.596201 | -56.023899 | 2025-04-08 00:34:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| deefcf04-be5d-3210-a26f-be7cd85a15a9 | -17.635401 | -46.618401 | 2025-04-08 00:34:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a98d81a6-d583-3e5f-b9aa-750d02e92366 | -19.959801 | -47.5769 | 2025-04-08 00:34:00 | METOP-B | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b449028e-708e-3ebb-b593-6ef5515ae547 | -21.7838 | -55.3162 | 2025-04-08 00:34:00 | METOP-B | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 200f5cc1-f109-3baf-9326-9a1ef16c4e95 | -21.012501 | -47.346699 | 2025-04-08 00:34:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb9b1cd-ea23-3030-882d-7e691e20fced | -20.6367 | -55.0271 | 2025-04-08 00:34:00 | METOP-B | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ac922b60-c253-37ec-a03b-7f54f0eb84e6 | -22.4806 | -51.6922 | 2025-04-08 00:34:00 | METOP-B | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61a7de1b-ca32-349b-9e8d-6cc4042f8ea4 | -22.4785 | -51.7047 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b7e5e326-4a6d-3e68-9e5b-d1bfa1960c85 | -21.793699 | -55.310501 | 2025-04-08 01:26:00 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3666210b-03d9-3419-8425-6f4c90c83f08 | -22.485399 | -51.690899 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16fbe041-2622-3f0e-8850-1cc766d38dc7 | -22.4979 | -51.6991 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b060e8d-11ad-3e45-bc71-1bb158224d84 | -22.488199 | -51.7019 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3f6fd62a-0ef3-3da8-9a4d-d0d620676dac | -21.877001 | -54.777802 | 2025-04-08 01:26:00 | METOP-C | ITAPORÃ | MATO GROSSO DO SUL | Brasil | 5004502 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c3a1214e-b649-320c-9ec5-209fcec31428 | -20.643299 | -55.035099 | 2025-04-08 01:26:00 | METOP-C | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f92afe00-d45f-321b-97f7-8a76ba2c87cb | -22.490999 | -51.712898 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e81f8c2-3bfa-3b72-a261-f64dcb6f9d28 | -21.7955 | -55.318298 | 2025-04-08 01:26:00 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c0568c62-e4bd-375e-8ef9-0f33dd44e6d6 | -22.4937 | -51.723801 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5644efa1-6ed6-3594-950c-b64df10848b4 | -22.4757 | -51.693699 | 2025-04-08 01:26:00 | METOP-C | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a5a9f47f-c9e9-3c9e-9140-8e0333d16f7c | -22.4621 | -51.70454 | 2025-04-08 01:41:00 | TERRA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 875bbe91-6a8d-31a2-8008-557efea2030a | -22.46151 | -51.71028 | 2025-04-08 01:41:00 | TERRA_M-M | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| 2a2561e8-72a5-388c-af36-d9b11749b407 | -12.26107 | -41.30515 | 2025-04-08 03:06:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9480127a-fd7c-35fb-aa86-2c7b55bc50fc | -12.26302 | -41.30515 | 2025-04-08 03:06:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 98c53983-ae2d-3802-888a-78d69151b9f8 | -12.2625 | -41.29832 | 2025-04-08 03:06:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 065c716a-e892-38d4-b6d4-8f91d04cf01a | -12.2645 | -41.29828 | 2025-04-08 03:06:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a091d095-637a-312a-bd48-b67a30313d65 | -12.11328 | -45.6355 | 2025-04-08 03:28:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06d33e2a-55fc-3150-98c6-e25d59d99976 | -6.87489 | -41.68791 | 2025-04-08 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de2e0d49-4a81-3c58-a0cf-ca33f8d62124 | -10.71501 | -42.33114 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40995ca6-70f9-3fa8-a3dc-4fee91ec86c3 | -10.71214 | -42.32778 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 269369fd-09b3-3576-ae22-f861eebd5fce | -10.71753 | -42.32885 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe8104ce-d63a-311b-b26a-c0caf2ada6de | -13.18544 | -38.902 | 2025-04-08 03:28:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2294c7e2-cdf4-36df-98f6-b13ee6584f30 | -10.72291 | -42.32992 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9cd17dd4-a44b-3340-8513-b1418c69366b | -12.94706 | -38.61466 | 2025-04-08 03:28:00 | NOAA-20 | VERA CRUZ | BAHIA | Brasil | 2933208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 05d61fb4-aadb-38a2-a053-dd0f12c14000 | -13.18477 | -38.90581 | 2025-04-08 03:28:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 23a6979b-0e94-3868-975a-7c67bbac1209 | -13.19208 | -38.90158 | 2025-04-08 03:28:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a69f0601-84a8-3ba3-b0e8-e71a5848e96a | -13.18727 | -38.90459 | 2025-04-08 03:28:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3ea88bf9-13cc-351e-a7b6-e2335eb1c1b1 | -12.76966 | -44.41375 | 2025-04-08 03:28:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 501d89a9-dd02-3058-9277-db8d637ca3f1 | -10.69598 | -37.0481 | 2025-04-08 03:28:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d03db3d7-d0a5-3db5-bbfa-84f4a1e3635a | -10.71566 | -42.32765 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 285eb165-a07f-3a06-b3eb-e79281aab16f | -13.18797 | -38.90079 | 2025-04-08 03:28:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9884897c-412e-3031-b500-f3c61c07b9ee | -10.18388 | -37.2111 | 2025-04-08 03:28:00 | NOAA-20 | GRACHO CARDOSO | SERGIPE | Brasil | 2802601 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 533392b5-efd8-3cea-b3bf-762e631caba6 | -12.26664 | -41.29595 | 2025-04-08 03:28:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f0602498-67cd-370b-a618-9061ddbfb61e | -8.07346 | -34.97707 | 2025-04-08 03:28:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8afa87c7-4f8d-39f2-a2a2-e484e26d6869 | -6.87423 | -41.6916 | 2025-04-08 03:28:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 934f49db-8008-34b8-9328-ce796cc48c8d | -10.72357 | -42.32644 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1b090c5a-caa0-3edf-a387-45633778c7f7 | -12.10785 | -41.31942 | 2025-04-08 03:28:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e4ccfe9-b96a-3ada-83a7-f389b7fe6792 | -9.63327 | -40.39965 | 2025-04-08 03:28:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64f35cb9-22ac-37d1-943f-b7896e657c25 | -11.2935 | -41.86364 | 2025-04-08 03:28:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8de48af1-b34b-3cb7-8838-48ba2956d8eb | -12.76714 | -44.41076 | 2025-04-08 03:28:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74fc4f90-ca26-3753-aca2-cced6a5482a0 | -10.71819 | -42.32536 | 2025-04-08 03:28:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 812bd6cf-3124-3f6e-8f19-80ed51ceccc6 | -12.26561 | -41.30144 | 2025-04-08 03:28:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 105d4906-7716-368b-8486-ef7eb35007e3 | -13.18316 | -38.9038 | 2025-04-08 03:28:00 | NOAA-20 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4430ff01-7540-36a4-a152-122023b3c355 | -11.28832 | -41.86268 | 2025-04-08 03:28:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b38417ac-8884-34ea-8b37-350b60c40e8d | -17.91976 | -45.53347 | 2025-04-08 03:30:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 072fef05-008e-3797-bd2d-c6b9356de4d7 | -17.61329 | -46.7023 | 2025-04-08 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01304ac6-5f11-33ba-8ab5-88864ab25e57 | -17.61704 | -46.70372 | 2025-04-08 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README2.md)
