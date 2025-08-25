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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e2c5fb4-1fe6-3d57-804b-eb9a84b0cba9 | -11.26861 | -44.98836 | 2025-08-25 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 03f866f3-0e54-379d-b587-f32b8b6518c7 | -6.80598 | -44.99713 | 2025-08-25 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 51cb3c02-badc-3b59-8931-67fedb34ce94 | -6.03386 | -44.20857 | 2025-08-25 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1087be3f-8ffd-3273-8f10-1b2a183fb5ed | -8.24144 | -45.08713 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c4514a6b-b20a-31e9-a558-58f44bd0551a | -6.37301 | -45.19199 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cb7d4655-5216-3c1b-a318-8c531769f6df | -5.11722 | -37.81871 | 2025-08-25 12:14:00 | TERRA_M-T | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 41d1fda1-55f0-38fa-8020-019d02369067 | -6.40984 | -44.68026 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 005629a4-d6ad-30bc-8cde-d4c590d582e7 | -6.2536 | -43.82411 | 2025-08-25 12:14:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f13c6412-7dd2-37ca-8b5c-ec456af8c972 | -8.80334 | -47.326 | 2025-08-25 12:14:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 98b764e9-fa33-344f-a182-d5711aaaee6d | -11.19831 | -48.46484 | 2025-08-25 12:14:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| da0338d8-d6a5-390e-a640-fadb3b2d1205 | -10.46561 | -48.3176 | 2025-08-25 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d9df67a4-555e-3a74-9fbc-86064846bbf2 | -5.1483 | -43.22852 | 2025-08-25 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9ede1d1c-39b1-3c28-a068-fdaa9584e943 | -8.75759 | -49.93881 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b19249a0-bd80-3bf8-be91-3f9b65bf39d4 | -6.41874 | -44.68154 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 93ffe7ce-83ea-3e6d-b12f-f3d30d7a77df | -7.23019 | -44.41716 | 2025-08-25 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a97c2950-a505-339b-a7fb-2d93609c9588 | -6.38824 | -43.26591 | 2025-08-25 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d2558c56-8a1c-3bda-b218-3bd5250a62b2 | -11.30531 | -43.27434 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 468d3e2f-14ca-3fdf-b83a-f5e509c886ad | -6.38966 | -43.25583 | 2025-08-25 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 272b5e86-e775-369d-925d-a890c0a9e627 | -6.36292 | -45.19955 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f7e92795-5843-309b-8888-64e5f83f5a79 | -7.1554 | -44.16359 | 2025-08-25 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| efc79b84-2672-318b-83c5-a826996f7beb | -7.55217 | -39.24697 | 2025-08-25 12:14:00 | TERRA_M-T | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 53.2 |
| 9b0a5c0f-95c3-379f-9165-5477b9b973f4 | -7.86862 | -46.27305 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d98d77a1-998e-3fb4-9e83-7a3f80254b64 | -11.14868 | -44.79308 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 108df3f5-67ba-3dde-8436-950b90a4e430 | -6.91655 | -44.4206 | 2025-08-25 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0ef02660-e3ed-3b0f-8073-d0e79303a18d | -6.45438 | -44.62234 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 8bd527bb-25b9-308e-b179-00ad2991d118 | -7.64124 | -46.31903 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 94df9043-fec5-3d30-8ede-66e28fe760c4 | -3.97811 | -42.51108 | 2025-08-25 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 0ae303c5-e5c0-3cb5-b99c-b60fc17a32fa | -7.12214 | -43.67447 | 2025-08-25 12:14:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 60da5947-8cda-3017-9055-704267e8e1b0 | -8.70391 | -47.8661 | 2025-08-25 12:14:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 4ffa912e-87ed-39cc-8aa5-7a94b4aa3f34 | -9.38707 | -40.63104 | 2025-08-25 12:14:00 | TERRA_M-T | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ebad3acf-9abd-3398-8197-399c58acc835 | -11.27123 | -44.96938 | 2025-08-25 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b1f75028-7eac-35ee-b5ee-2e84eda6fbdf | -6.36419 | -45.19073 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7f35b624-cc9a-33d1-a11c-63635059d796 | -7.31576 | -44.5288 | 2025-08-25 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 27461cfb-d972-3bdc-9530-f936094264e9 | -6.8956 | -47.93382 | 2025-08-25 12:14:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 238c2786-089a-3d47-9b3f-d53d10dc52af | -7.54513 | -46.02089 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 44ff775d-b668-388a-ac07-0b79e21f41d7 | -4.78485 | -45.33051 | 2025-08-25 12:14:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9090ee83-372c-3cbd-aa31-581b740e8206 | -8.3231 | -47.26624 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| bf7de34c-32db-3e40-ba36-c7bcccfd1e5f | -8.04466 | -47.33768 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9100744e-b63e-32d1-8196-c372026e0896 | -5.11592 | -43.20782 | 2025-08-25 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a8eb7a05-2d5c-3fde-9c53-58d06c257378 | -5.6414 | -45.14781 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 58a0b90c-0371-3da9-afdf-1344d45045a5 | -6.80725 | -44.98822 | 2025-08-25 12:14:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e058e429-c96c-3bc0-a7dc-2b639e970555 | -10.78025 | -46.42637 | 2025-08-25 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e780fbf7-7ffb-3e06-a182-6fd3a30b11b1 | -10.8225 | -48.33598 | 2025-08-25 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1cb81cfc-2ba9-3642-9bce-dc3d10253d50 | -7.61282 | -45.2356 | 2025-08-25 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 5a6920de-91bb-3bb9-bde0-ba59006d38c3 | -4.78612 | -45.32173 | 2025-08-25 12:14:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| c852c1c4-6d97-3362-9a68-46bbfbbbee1a | -8.59014 | -44.05401 | 2025-08-25 12:14:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8fb4cba0-41e9-3e57-ac0f-29cc663215eb | -6.45567 | -44.61329 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 354cb715-7829-3f5b-80d5-76356d405ec4 | -10.74768 | -47.02528 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 8d0cb6ef-d534-3d15-aae8-c78e8e240b94 | -7.59102 | -47.47331 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1dae55d7-53a1-32de-9ef6-5ca38813ec37 | -8.32447 | -47.25689 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1cb3d4f0-f4e0-3156-aa34-bea2452b41ea | -11.28681 | -44.99088 | 2025-08-25 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 00484a1b-13dc-3065-968a-fac5eee6bc95 | -8.17105 | -45.06165 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9bc5aab0-88f5-3d31-af98-cb8d4ec1034c | -10.7503 | -47.00727 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 3a577672-c40a-3888-88a7-883268fc6d38 | -6.5007 | -44.88131 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab78f7ac-1489-3741-82bd-b866e132430a | -7.76377 | -47.36482 | 2025-08-25 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 32e92bf8-c43d-35b4-8335-580568b2a446 | -8.23889 | -45.10509 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| dae2a719-71a3-33da-9d37-f84922c4c137 | -5.68945 | -45.14256 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| e7a1bfa1-8e06-3153-94bc-b79a6500c584 | -6.43659 | -44.55548 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47fc4d49-3990-32ea-b987-804b484fd0cd | -6.2479 | -43.73974 | 2025-08-25 12:14:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 11d584ff-63d9-38fd-882c-cd62e4dfc3fb | -6.96765 | -42.86303 | 2025-08-25 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6b71c4ae-f11e-3798-a8ab-797acd996c5c | -8.05771 | -49.68951 | 2025-08-25 12:14:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| b5ce87e0-9714-3e2c-84ee-763dd089e9b4 | -7.28761 | -44.46869 | 2025-08-25 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 67555242-65c6-360e-b2fd-e1ea7dec3b59 | -7.85977 | -46.27179 | 2025-08-25 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6aadf998-34c4-3cb5-9f79-1bb9ccaa11f5 | -4.77603 | -45.32928 | 2025-08-25 12:14:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| ffe0ef84-c3fd-31fa-8b32-690d603133e9 | -5.86529 | -43.89955 | 2025-08-25 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| a3c3379b-23fd-3eb4-8fc8-6d61ebc4b871 | -6.9149 | -43.77258 | 2025-08-25 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 2753e4ca-bcec-34bf-9bcb-a9b6ed21bd2a | -8.0596 | -49.67686 | 2025-08-25 12:14:00 | TERRA_M-T | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2379ec35-1b0b-3ea7-8865-6a09a8e9650a | -11.8065 | -44.27568 | 2025-08-25 12:14:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| be154bc2-659b-3b3d-a07d-f041853ce05b | -8.17866 | -45.0719 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e2902f64-a890-3c77-91a0-60f3a9329473 | -7.6822 | -45.39637 | 2025-08-25 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 16f6f221-83e7-389b-a987-04a415e08ba4 | -7.46792 | -45.02102 | 2025-08-25 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe1c2c3b-449d-3c16-bdeb-ad7d7ae638bc | -10.71057 | -50.53632 | 2025-08-25 12:14:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b7518cdb-a754-37fe-b6a5-0e5d6af7722d | -10.58523 | -47.13355 | 2025-08-25 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 62f31496-1060-3680-bf05-c6bc02141b6f | -8.07004 | -44.99561 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d3ac2bcf-591a-36b1-b493-0c313bee8c89 | -7.33241 | -44.54049 | 2025-08-25 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b346a3f2-71f5-3845-bebd-562476ed3f32 | -5.11401 | -37.84249 | 2025-08-25 12:14:00 | TERRA_M-T | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 7e7b0a21-aaf8-31a7-b29e-a11a52e5de58 | -6.40857 | -44.68927 | 2025-08-25 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f61f24b0-d843-38ad-91e2-f2e92038c3c9 | -8.22043 | -40.35341 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 25.5 |
| ccfb309b-7522-3cf7-b5ff-a4e1934ffb47 | -5.63132 | -45.15538 | 2025-08-25 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 3116bf0d-21bf-3585-9232-df11bd7e6f10 | -8.02678 | -44.98039 | 2025-08-25 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2ab30e77-d872-3ac9-8f4c-0616b40172b8 | -6.70637 | -44.0135 | 2025-08-25 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ba1b39cf-d908-3197-8e35-1075dab0f105 | -10.89499 | -49.49224 | 2025-08-25 12:14:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fcbee755-5c68-31f6-b307-ea0936f5468a | -14.26066 | -48.04956 | 2025-08-25 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ec327e97-0c50-3bee-969e-e0d3385763a5 | -15.14292 | -48.69476 | 2025-08-25 12:17:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a8cb4a90-efbe-388b-a6c5-62229b981c5a | -13.46366 | -47.00328 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9dd78bfc-9428-37a1-aecc-5aad40a54ebc | -11.60381 | -46.34519 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b559ead8-3681-370a-bbcf-cec75b0427a9 | -11.60509 | -46.33625 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 13bc5506-a13c-3bc3-9a02-77e1594f3dba | -18.33599 | -43.8429 | 2025-08-25 12:17:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf73d2b1-03f0-3fa3-bc3d-1ae136b0df4b | -13.40168 | -51.80328 | 2025-08-25 12:17:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 626da5ec-e002-30a9-9a5d-d255fa0012b8 | -11.61915 | -46.23758 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| dbb63f8e-3025-3b4a-9bd8-ac0b9eb44430 | -14.78627 | -47.93082 | 2025-08-25 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 70405a34-a030-3a03-96e6-9ea1646029de | -17.57329 | -44.25038 | 2025-08-25 12:17:00 | TERRA_M-T | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 28.2 |
| cbea80ec-7c18-39f8-97e7-abf23ea71485 | -13.45301 | -46.87546 | 2025-08-25 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 2fff9411-b6b7-3ec5-82e8-0c6c261a41fe | -11.64195 | -46.20417 | 2025-08-25 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d5c8c632-2981-3737-af80-9eca917dbb58 | -14.79515 | -47.93213 | 2025-08-25 12:17:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 9208a0db-72d0-39b3-8c03-0399fe838236 | -12.6971 | -47.83015 | 2025-08-25 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 3f46a022-49fe-35f2-b932-5ff68f179318 | -11.91368 | -47.12955 | 2025-08-25 12:17:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 54b5bc2a-3888-3808-ab68-76e2b846dc9e | -14.50221 | -51.91595 | 2025-08-25 12:17:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 0729c49b-cdfc-3d4e-9cfd-22c10c956570 | -13.61346 | -48.18277 | 2025-08-25 12:17:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0a659dcb-64c9-3a32-b85c-56a953227713 | -13.21294 | -46.04357 | 2025-08-25 12:17:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README94.md)
