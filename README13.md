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
| 917b0895-2861-338f-a555-80e8d7a3f204 | -17.55349 | -54.03877 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c482dead-412f-391a-9a27-bd81ebb95269 | -19.21896 | -57.33168 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e85b3b4a-2d6b-3f11-a45f-c20929d88aca | -19.1847 | -57.33317 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4a141b75-9b19-333e-ad14-fe4f2f802759 | -19.18585 | -57.32588 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 02cfb7c0-8295-32ae-895d-bcf1ad402ee5 | -17.05225 | -52.75285 | 2025-11-24 05:01:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de296491-0ad3-3b5c-9299-36d78e5c37d2 | -19.19363 | -57.31975 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 61a89b53-06cf-326d-b730-748f5b2bb479 | -21.70465 | -57.65768 | 2025-11-24 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a62c08e-bed8-3e1e-81bf-7ecac30acd47 | -17.05289 | -52.74821 | 2025-11-24 05:01:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f77ed51-ee99-344c-b42f-494b3cf3af4f | -17.55409 | -54.03466 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7198481b-5739-310a-86b0-4f4505509f8c | -17.55055 | -54.03411 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97ec43e9-a3d9-3b0d-aef4-2f52a12ff621 | -17.54996 | -54.03822 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0517e84-d1ee-381b-9177-d8340a333c41 | -17.54583 | -54.04178 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02a824cd-6cd5-3470-8c6f-a72538f10bd8 | -17.54289 | -54.03712 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d8e0edc-271c-33c6-9f55-582ec53bc081 | -17.55703 | -54.03931 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d494979f-6b95-3801-bec3-b2aa486b841f | -20.50006 | -55.82734 | 2025-11-24 05:01:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dc7e431-9a27-39c2-96c2-d45aabc55592 | -19.21954 | -57.32804 | 2025-11-24 05:01:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a2ffe2c5-f35f-377e-8b44-20892e0e6019 | -21.70797 | -57.65827 | 2025-11-24 05:01:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71c9159a-07ff-3f03-979e-ac0c20987128 | -17.54642 | -54.03767 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e875d66e-f4dd-3c67-94fa-83ef5a79409c | -17.55762 | -54.0352 | 2025-11-24 05:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 319a8935-a830-301f-abbb-df3e6946738f | -4.26366 | -40.85159 | 2025-11-24 05:31:00 | AQUA_M-M | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 7827c24f-5a90-3e7b-9f09-47cc478fee14 | -4.2621 | -40.86173 | 2025-11-24 05:31:00 | AQUA_M-M | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 4d5e23fb-d350-3cca-9b2b-b97604fef322 | -4.39372 | -40.67392 | 2025-11-24 05:31:00 | AQUA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 738a7d53-e0f4-3423-a20c-a80a67409492 | -4.69996 | -46.46267 | 2025-11-24 05:33:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 5ee7e02b-6af6-31bf-812c-6880e9a15d27 | -4.44694 | -44.31747 | 2025-11-24 05:33:00 | AQUA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 764def45-50ca-3ab3-bb70-ae7b5566c702 | -4.71062 | -46.4592 | 2025-11-24 05:33:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 729f715f-fd45-35a3-bf9f-4c4cea9a1529 | -6.39171 | -38.90932 | 2025-11-24 05:33:00 | AQUA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| ea861bd0-f061-3fad-9b43-372e8cb9b9af | -4.81477 | -43.82825 | 2025-11-24 05:33:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ee44d5c3-9773-3834-9311-e43678ce7222 | -2.23307 | -53.64937 | 2025-11-24 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a56f9df-2f2e-3190-84c8-d1422018302d | 4.21767 | -60.05103 | 2025-11-24 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69d386bd-4fcc-379d-9897-25161df79061 | -2.22654 | -53.64844 | 2025-11-24 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7f32f9b-fc5f-3ab0-b56f-441138b372ca | -2.23392 | -53.64383 | 2025-11-24 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b602bfa-c1e4-34b3-8b70-f00f897d5aba | -2.23312 | -53.64611 | 2025-11-24 05:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ec4fc7b-7da0-3073-b93e-e3b021d5612f | -3.1461 | -45.3404 | 2025-11-24 06:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 671a7ed6-771e-3d11-befc-b90c0835e7e5 | -3.146 | -45.3629 | 2025-11-24 06:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bb081490-b559-3950-87ab-177108fb3b82 | -3.2017 | -45.3608 | 2025-11-24 07:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 06d4ef33-c6ff-316f-a57e-535115f29dc7 | -4.0198 | -42.4667 | 2025-11-24 11:10:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| d29e5ff2-8c57-3b5b-a101-1be3747612c3 | -5.34776 | -38.3578 | 2025-11-24 11:17:00 | TERRA_M-M | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 1a2b5337-ac78-3849-ad77-7ba8fe2c1a41 | -5.70492 | -38.64441 | 2025-11-24 11:17:00 | TERRA_M-M | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| aedd15ed-776b-30d4-8e1a-192be5ea7b07 | -5.34617 | -38.3472 | 2025-11-24 11:17:00 | TERRA_M-M | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 30.6 |
| 760fdafd-e620-3038-a330-1d5c3ea9aecc | -7.81841 | -38.67986 | 2025-11-24 11:19:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| fe7b640e-36ca-34e9-a29c-d293b1f58f69 | -9.33527 | -36.94994 | 2025-11-24 11:19:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 97ab4cc2-3edd-3a67-8d2e-db5fd295b85e | -8.24071 | -37.81142 | 2025-11-24 11:19:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 68983c6b-13fe-305e-92f1-dc827cc07fa9 | -7.39817 | -39.0882 | 2025-11-24 11:19:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 307d20f1-1447-3ef6-bcf4-5b817c950899 | -6.99868 | -38.16827 | 2025-11-24 11:19:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 54135a6e-0e08-374f-9a4b-2b3a46852f05 | -6.35926 | -38.36509 | 2025-11-24 11:19:00 | TERRA_M-M | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 15.6 |
| b5e8f56d-1156-332c-93af-81c76651d4e6 | -9.32544 | -36.94846 | 2025-11-24 11:19:00 | TERRA_M-M | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 076f2b86-b383-3f4f-9dd4-5e75cf98ee47 | -9.36242 | -36.9155 | 2025-11-24 11:19:00 | TERRA_M-M | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 35.8 |
| 3021b814-d7b9-3f1e-93e7-a75b2b26f697 | -7.28966 | -40.76864 | 2025-11-24 11:19:00 | TERRA_M-M | FRANCISCO MACEDO | PIAUÍ | Brasil | 2204154 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 581d2169-574a-33a0-a626-56d4a20d47fe | -6.948 | -38.50075 | 2025-11-24 11:19:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 01290d98-bcaa-37f8-8a53-2f06576522e2 | -8.4358 | -39.36454 | 2025-11-24 11:19:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 26.6 |
| c63ac5a8-9fdc-3821-b503-d2737938b8b3 | -7.75807 | -37.48751 | 2025-11-24 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 22.9 |
| b5a5b898-b9eb-37f2-9c47-75736e9eb2a4 | -0.2673 | -48.79485 | 2025-11-24 12:55:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 072cb38a-76de-3136-b7d0-93846e0a0468 | -0.26536 | -48.78793 | 2025-11-24 12:55:00 | TERRA_M-T | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 413a18d6-9b2d-3f59-862a-f1a73e523d18 | 2.00052 | -55.78421 | 2025-11-24 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 86b5a344-cae3-3a2c-9c34-62ac7160bb84 | 1.99927 | -55.77545 | 2025-11-24 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 770ffa4c-6c5f-3225-ac4c-052f273fae3e | 1.53732 | -55.63142 | 2025-11-24 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f574a33e-1cba-3008-9801-9574e6bd35ea | -0.20867 | -49.90719 | 2025-11-24 12:55:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e9900350-0e5c-30e3-a534-0f513b403296 | 1.52721 | -55.62383 | 2025-11-24 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 565307c8-bfac-320b-8ceb-0546d5a172ef | -19.2151 | -57.3275 | 2025-11-24 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| eb24f0b2-e41d-3b42-9108-76c6bdb7b497 | -8.4443 | -39.354 | 2025-11-24 13:20:00 | GOES-19 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 94.4 |
| 076669d3-c943-38b8-9704-378db90550ba | -8.4443 | -39.354 | 2025-11-24 13:40:00 | GOES-19 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 4122808b-cd2c-33e8-9abe-c390c20931fe | -4.0198 | -42.4667 | 2025-11-24 13:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 89.9 |


