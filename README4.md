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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 105ec602-c593-3e7a-ad1e-783deb45f220 | -20.0168 | -44.501598 | 2024-10-03 00:07:53 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 450f44f0-3418-35d3-9acf-db34e24589b8 | -20.018801 | -44.512699 | 2024-10-03 00:07:53 | METOP-B | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8028cf94-d08d-3bad-a64c-ff6330d51df3 | -20.004999 | -44.4925 | 2024-10-03 00:07:53 | METOP-B | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2b117e1a-993b-3b4d-be72-a40630fc9cbc | -20.007099 | -44.5037 | 2024-10-03 00:07:53 | METOP-B | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c668f66a-028f-37ee-9c20-f7d820fb96ad | -19.499001 | -42.312401 | 2024-10-03 00:07:54 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b0e0be7d-2493-3484-8d26-fc26407ad4f4 | -19.5007 | -42.320801 | 2024-10-03 00:07:54 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b04704a-5c10-3941-964f-ba6a1be9f08d | -19.756001 | -43.508499 | 2024-10-03 00:07:54 | METOP-B | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0920f255-4efc-31eb-9c3b-938ed14054fb | -19.7579 | -43.518299 | 2024-10-03 00:07:54 | METOP-B | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc9c4dff-2240-3757-b65e-e428076e1b20 | -19.7924 | -43.6437 | 2024-10-03 00:07:54 | METOP-B | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5594cf1f-bb7d-3572-b9e1-a83695da0f7e | -19.8153 | -43.815701 | 2024-10-03 00:07:54 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9746ed-f0cc-38be-a9c9-dae3fe672afd | -19.817301 | -43.825802 | 2024-10-03 00:07:54 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 570198ad-b1e1-3680-87c5-61e173092398 | -19.768999 | -43.628101 | 2024-10-03 00:07:54 | METOP-B | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| add49a7a-e8f3-3517-afd2-5791570af12f | -19.807501 | -43.8279 | 2024-10-03 00:07:54 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 493a9472-5f42-3e04-8d2f-49ef6a0a287d | -19.507099 | -42.863602 | 2024-10-03 00:07:56 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77b51b84-8784-38a8-be1f-9dbb786e874d | -19.497299 | -42.8657 | 2024-10-03 00:07:56 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ed5480a-8714-37e1-8223-3257e1636618 | -19.4991 | -42.874599 | 2024-10-03 00:07:56 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03d2b967-041d-38ed-8e80-1b724d8baab3 | -19.744101 | -44.2411 | 2024-10-03 00:07:57 | METOP-B | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a18400a4-825e-3d85-a0d8-fd558e96fee6 | -19.746201 | -44.251701 | 2024-10-03 00:07:57 | METOP-B | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a326cdbb-41f0-3f99-9105-cb696e2ab0d8 | -19.7955 | -45.0005 | 2024-10-03 00:07:58 | METOP-B | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 18b45b62-ca5f-3bb3-a3ab-b9cc51c03fa3 | -19.7857 | -45.002499 | 2024-10-03 00:07:58 | METOP-B | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d3fce6eb-93f4-39b7-aae6-6f500a784ac5 | -19.452999 | -43.054199 | 2024-10-03 00:07:58 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 283512ba-3d26-30d5-b213-ddeabdc04cce | -19.4548 | -43.0634 | 2024-10-03 00:07:58 | METOP-B | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8e29ab18-49e9-347b-9506-b80d528b0541 | -18.902399 | -41.201302 | 2024-10-03 00:08:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 61f0fa55-809f-341a-9a9c-04de44f3b3e2 | -18.903999 | -41.2089 | 2024-10-03 00:08:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0dc30e63-9def-3b24-bb14-fcb334814686 | -18.9056 | -41.216499 | 2024-10-03 00:08:00 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 855ae94c-7afc-3805-a302-f30a9ef04516 | -18.891001 | -41.1959 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a87bd03-3c6a-37d2-9608-74c8766b2ce0 | -18.892599 | -41.203499 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a2b4f28-8567-37ae-8358-e4c323e91f95 | -18.894199 | -41.211102 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 801cbe1d-06eb-3fd2-b342-98103fbb384d | -18.8958 | -41.2188 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 19ead75e-784e-3752-9147-6de09df0a54b | -18.905399 | -41.264599 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 496690a4-1144-3ec8-8c08-bec5dd921416 | -18.907 | -41.272202 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1409a27e-cd0f-30f0-bd10-4f8565715c25 | -18.881201 | -41.198101 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| faf833c5-2073-37a4-ab4a-1b7a89645db7 | -18.882799 | -41.205799 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1091fc4-359c-3f9c-b402-f5fe66de31f7 | -18.884399 | -41.213402 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85b36cac-5a5f-30af-b7c4-a82c4ca91506 | -18.8794 | -41.238499 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4f0f894-068b-3db5-9d65-54b59090e022 | -18.881001 | -41.246101 | 2024-10-03 00:08:01 | METOP-B | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 49d84a36-a95e-396a-bcc4-f8a2f0682fc6 | -19.249701 | -43.368198 | 2024-10-03 00:08:02 | METOP-B | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82029ae2-dbb7-32cb-8d53-213ced729850 | -19.2381 | -43.361 | 2024-10-03 00:08:02 | METOP-B | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e39126a5-5670-333c-96b5-fd8fe02bdcad | -19.24 | -43.3703 | 2024-10-03 00:08:02 | METOP-B | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78bea49d-7a82-33ec-a5c3-696c0bbac2e3 | -19.274099 | -43.753799 | 2024-10-03 00:08:03 | METOP-B | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3707595-94ef-3181-b7ec-19a289477860 | -19.275999 | -43.763699 | 2024-10-03 00:08:03 | METOP-B | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 683d405f-b546-363a-9bd7-91dacc6ce9a3 | -19.277901 | -43.773602 | 2024-10-03 00:08:03 | METOP-B | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 84306887-7892-3efe-89f2-850305c2c03a | -19.264299 | -43.755901 | 2024-10-03 00:08:03 | METOP-B | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b80c2f7-e1a0-377e-a77f-d2fcafa68e3c | -19.266199 | -43.7658 | 2024-10-03 00:08:03 | METOP-B | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ee8513cf-0c33-3712-9997-378a26990820 | -19.268101 | -43.7757 | 2024-10-03 00:08:03 | METOP-B | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63129347-856e-388a-b08b-254c02a60c97 | -18.3519 | -39.778099 | 2024-10-03 00:08:04 | METOP-B | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 553157a7-3753-305e-8af3-db168fa8fbc8 | -18.778799 | -41.889801 | 2024-10-03 00:08:05 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ce99c3e-9860-3686-924e-803970446cec | -18.780399 | -41.8978 | 2024-10-03 00:08:05 | METOP-B | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42612078-65fc-3464-a221-46e661de7c09 | -19.031601 | -43.1931 | 2024-10-03 00:08:05 | METOP-B | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 207c5508-a68f-337d-8cd6-0e49235791e9 | -19.0334 | -43.202202 | 2024-10-03 00:08:05 | METOP-B | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 519426d2-e0a0-3b75-9099-3c6ca0719965 | -19.02 | -43.186001 | 2024-10-03 00:08:05 | METOP-B | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e0fa8ff-00be-337e-b6c9-8c6f82e33247 | -19.021799 | -43.195202 | 2024-10-03 00:08:05 | METOP-B | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f080ba92-a5c3-3ad9-b807-ecf1480b90b0 | -19.0236 | -43.2043 | 2024-10-03 00:08:05 | METOP-B | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a86045ca-2ba2-3d88-8f31-fb96b5547b39 | -18.992399 | -43.2015 | 2024-10-03 00:08:06 | METOP-B | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ac12e21-9cc2-3090-bfdf-7929350ec12c | -18.974701 | -43.214901 | 2024-10-03 00:08:06 | METOP-B | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 888b09da-fba1-36cc-8491-acbfe86bb702 | -18.843599 | -42.9156 | 2024-10-03 00:08:07 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12d2be2d-db70-3b1e-9e71-a769ab5c35ab | -18.8454 | -42.9244 | 2024-10-03 00:08:07 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca9a6077-3609-39ac-ad2a-9836c4afddf5 | -18.8339 | -42.917702 | 2024-10-03 00:08:07 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a97111a8-95fc-37a5-951d-1ceeb99ff40f | -18.835699 | -42.926498 | 2024-10-03 00:08:07 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83738b8c-3958-35ac-a44c-764235a65f2f | -18.8374 | -42.935299 | 2024-10-03 00:08:07 | METOP-B | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f75c7d55-f018-3f57-ba68-cf95cf8a672c | -18.870501 | -43.617401 | 2024-10-03 00:08:09 | METOP-B | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20177320-67ab-3a36-9441-507f37944cbb | -18.8724 | -43.626999 | 2024-10-03 00:08:09 | METOP-B | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 473f427c-91e3-3f4b-b5b3-4115c092450e | -18.541401 | -42.229801 | 2024-10-03 00:08:10 | METOP-B | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bce8df9a-bea9-3de9-9372-58bca4ab0966 | -18.542999 | -42.237999 | 2024-10-03 00:08:10 | METOP-B | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a3d68631-0cd3-39bf-8b1c-3ec3d493daa2 | -18.530001 | -42.2239 | 2024-10-03 00:08:10 | METOP-B | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aa1ed40d-ba44-3c1e-9cc5-891cbe008a12 | -18.531601 | -42.231998 | 2024-10-03 00:08:10 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e3926f1-f8ef-388e-b253-46fc2c2a537b | -18.5333 | -42.2402 | 2024-10-03 00:08:10 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 501f6b49-702c-3be7-a5de-e5a1870f9f5a | -18.521799 | -42.2342 | 2024-10-03 00:08:10 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48ae23fb-0e2b-301e-9e27-e800be511fc5 | -18.5235 | -42.242401 | 2024-10-03 00:08:10 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1fa0a85-d7f1-35ca-be8f-3e537e4a6cd2 | -18.511999 | -42.236401 | 2024-10-03 00:08:10 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1317018-0924-376c-86a8-9b36fa838ddd | -18.5137 | -42.244598 | 2024-10-03 00:08:10 | METOP-B | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c283bcc0-be01-3346-9b5f-23fa545a6eaa | -17.882299 | -40.0783 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4f03e6e-f38b-3893-9c3b-db1b94d5eaa1 | -17.883801 | -40.085499 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17c0c8da-d83d-3c13-a80a-02f9d34e7b8c | -17.885401 | -40.092701 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8d337b77-225a-37ee-b0c7-f6289974b2f2 | -17.886999 | -40.099899 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 108ab75f-7838-30f4-a8fe-3a29b5ac4791 | -17.872601 | -40.080601 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ed35b8ab-ac0f-3735-9229-1fdf734fc6be | -17.8741 | -40.087799 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5458d294-dd89-3eb3-adde-a82fb492d01d | -17.8757 | -40.095001 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 32e906dc-0191-3676-92e4-ec346e44b7bf | -17.877199 | -40.1022 | 2024-10-03 00:08:13 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07c575d5-f167-3955-981d-0b047d96ef30 | -18.292999 | -42.166401 | 2024-10-03 00:08:14 | METOP-B | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3b49f46-862d-3901-a499-6086761bef88 | -18.5933 | -43.9188 | 2024-10-03 00:08:14 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3492668c-900b-33be-a4b1-016452cb88a6 | -18.595301 | -43.928699 | 2024-10-03 00:08:14 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7b1c4516-838a-3f92-a74e-6ca24cfff339 | -18.5972 | -43.938499 | 2024-10-03 00:08:14 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9544d15-54db-3692-9efb-5411da338539 | -18.326 | -42.982601 | 2024-10-03 00:08:16 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff4af038-ca2f-303d-84e2-581902451a9f | -18.3232 | -43.223499 | 2024-10-03 00:08:17 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5b5bbe1-4e1a-3c01-bce7-7ec886d46e6d | -18.325001 | -43.232498 | 2024-10-03 00:08:17 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45081a4a-b223-334a-ad5c-afb3bb1ac968 | -18.3134 | -43.225601 | 2024-10-03 00:08:17 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc17fadb-cb6c-3960-883b-7c3050109d31 | -18.315201 | -43.2346 | 2024-10-03 00:08:17 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 214ac4d7-d930-35d2-831d-3ebd0aef2a2c | -17.8487 | -41.409901 | 2024-10-03 00:08:18 | METOP-B | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2375c940-a3c4-3621-8355-6d2ae9aac4d8 | -17.8503 | -41.4174 | 2024-10-03 00:08:18 | METOP-B | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3ac9732d-1cb8-3655-9bc3-f8a0fc8ee12e | -17.8519 | -41.424999 | 2024-10-03 00:08:18 | METOP-B | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce474612-7540-3d1f-88c3-3659efa0cae0 | -18.3682 | -44.017899 | 2024-10-03 00:08:18 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99dccce5-01e2-3c2c-8813-e31d08097509 | -18.3701 | -44.027802 | 2024-10-03 00:08:18 | METOP-B | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac9a0cac-9564-3529-aa33-40218d4b6999 | -18.8174 | -46.618801 | 2024-10-03 00:08:19 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ff0a560c-15ad-3a9d-9469-d7a61f0757ce | -18.0749 | -42.600601 | 2024-10-03 00:08:19 | METOP-B | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e052453f-10c5-3c12-89c3-80a9303603e3 | -18.066799 | -42.611198 | 2024-10-03 00:08:19 | METOP-B | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb2592f1-aff9-394f-b833-db8989af3f9d | -18.068501 | -42.619499 | 2024-10-03 00:08:19 | METOP-B | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e7d6e7d9-2d1c-3036-8710-62240b2a3a27 | -17.918301 | -42.3853 | 2024-10-03 00:08:20 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 173f796c-360d-35d3-8d37-375c269e6b0d | -17.92 | -42.393501 | 2024-10-03 00:08:20 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92820e12-bf22-352d-ae2a-a4eea7709b1a | -17.849199 | -42.248402 | 2024-10-03 00:08:21 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README5.md)
