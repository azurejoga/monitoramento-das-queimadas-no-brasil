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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c99b4e3-12f5-3506-8986-8d0a4bd39091 | -17.3158 | -43.6674 | 2025-10-26 00:50:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 38f33780-0068-3832-9ebb-21845afcf70e | -6.725 | -42.0499 | 2025-10-26 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 95.1 |
| c9d8e07d-8367-3b68-b7ba-a4dee09aa22f | -9.4382 | -56.6409 | 2025-10-26 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| abc31833-970f-33c7-a7a0-30171c8b84f9 | -2.7755 | -45.0835 | 2025-10-26 00:50:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 08e0368c-f642-355b-bd7c-45ba3670c746 | -5.6916 | -48.4921 | 2025-10-26 00:50:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 042e49ac-41e6-34c6-943a-1bb166640a93 | -4.8933 | -43.2349 | 2025-10-26 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 34504d30-cf54-3e0f-9556-cc1aa094547f | -4.7018 | -46.4508 | 2025-10-26 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ae7cc329-3063-36b9-b39b-b7307171c616 | -6.7252 | -42.026 | 2025-10-26 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| f2d3c970-234c-39f4-a0fd-ecb025db4f2e | -6.7064 | -42.0278 | 2025-10-26 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 182a0b95-5671-39eb-aee1-4764e5d84ec8 | -9.4568 | -56.6396 | 2025-10-26 01:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1588c1c2-0206-3718-bc55-c03c4710785d | -2.7754 | -45.1061 | 2025-10-26 01:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 386ddf15-9fd4-3265-ad69-c6371d85c380 | -4.7206 | -46.4276 | 2025-10-26 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 56cf2af2-7780-3746-8bd2-04c28a9164ff | -4.8931 | -43.2582 | 2025-10-26 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 83a4c02e-a1d6-31c7-979d-df1ef15b898c | -17.3365 | -43.6383 | 2025-10-26 01:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 0fe62b5c-8f13-3840-bb93-ce8c1122348f | -14.4461 | -49.9606 | 2025-10-26 01:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| fe3529cf-e82f-34c6-8eaa-ae3bef0a6345 | -4.0346 | -46.063 | 2025-10-26 01:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 3cec857e-2069-3d58-8bbb-0563b10878e2 | -17.3158 | -43.6674 | 2025-10-26 01:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 77c836e3-383b-334a-8ca8-77c164785280 | -5.6916 | -48.4921 | 2025-10-26 01:00:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3570e9f9-259c-3ab3-b050-ca526a5c41dc | -2.7568 | -45.1067 | 2025-10-26 01:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 43b8336f-cf39-371d-8e30-569b967f3e68 | -6.7061 | -42.0517 | 2025-10-26 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 3f6626cd-c953-3553-81e4-d7aafd0f40ff | -6.725 | -42.0499 | 2025-10-26 01:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.0 |
| 7339cb8a-cf40-30cb-9f58-34b23b0c3227 | -17.3165 | -43.643 | 2025-10-26 01:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 37a8198e-d13e-3d51-9491-a14759e3b065 | -4.702 | -46.4286 | 2025-10-26 01:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 278bd5c9-c08e-375c-ac49-a5132ec98712 | -2.7755 | -45.0835 | 2025-10-26 01:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 254dab10-2978-3911-8e1d-740c38b0e4a6 | -4.0345 | -46.0852 | 2025-10-26 01:00:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 5dfcd3ad-a811-3ce0-8a4c-96298db689b2 | -2.7569 | -45.0842 | 2025-10-26 01:00:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 66e6792d-30cf-38b2-9155-a4abdd6134e8 | -9.4382 | -56.6409 | 2025-10-26 01:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7d8e3aa7-37e4-3267-94a6-4503ee1fc7a4 | -4.9118 | -43.257 | 2025-10-26 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9a5de69e-fe73-37be-bea2-b0abc7dffd31 | -4.912 | -43.2337 | 2025-10-26 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 02faa286-5221-3d65-acb5-c17c29f2a03e | -4.8933 | -43.2349 | 2025-10-26 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d02e6524-deb9-3d81-b3cb-89a11a908ab6 | -20.48371 | -54.72259 | 2025-10-26 01:09:00 | TERRA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| dd9ee4d1-6ebc-332b-bbb7-87d6caac816f | -17.05503 | -51.53212 | 2025-10-26 01:09:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0d7d213f-97c6-384b-a465-3b259bb8c48b | -17.81283 | -57.63458 | 2025-10-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3f137381-d97d-3cd1-99e3-43def728f19a | -15.85936 | -53.58745 | 2025-10-26 01:09:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47acc1b6-fee8-3cb8-9888-264b5187695b | -17.81157 | -57.62535 | 2025-10-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f4ad4e17-4ba4-3c8c-a753-7fe1109b1433 | -17.01535 | -55.91024 | 2025-10-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 043f1673-e129-391e-98da-c07e4711a555 | -17.3365 | -43.6383 | 2025-10-26 01:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 203ac044-f661-36c2-85ba-34affc1f40d7 | -4.8933 | -43.2349 | 2025-10-26 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 23ce703e-aa70-31bd-8d0d-b3ff231c3ef9 | -4.8931 | -43.2582 | 2025-10-26 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 18b83235-3d00-3ac1-ae9a-e253ca874c5a | -6.725 | -42.0499 | 2025-10-26 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| d659239b-5ed5-37d9-b39d-0dbd18077471 | -2.7569 | -45.0842 | 2025-10-26 01:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 160a7eef-45ce-33b3-91f0-ebe78348bd75 | -9.4568 | -56.6396 | 2025-10-26 01:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| dcecb59f-b077-31b6-8343-f29c8843dae0 | -9.4382 | -56.6409 | 2025-10-26 01:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 18cf5ba3-9925-3460-a4fe-df70323a3979 | -2.7754 | -45.1061 | 2025-10-26 01:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 2d5a110d-1abf-3ec3-81ca-e3767a356275 | -4.912 | -43.2337 | 2025-10-26 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b9210964-8a25-3bfb-99ae-50b1b027345c | -17.3165 | -43.643 | 2025-10-26 01:10:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 107.7 |
| d18ff0ba-7508-378e-8057-fcbd252dcd54 | -6.7064 | -42.0278 | 2025-10-26 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| e7261387-41e6-33aa-932f-408213cad640 | -6.7061 | -42.0517 | 2025-10-26 01:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 155.3 |
| baa865b9-a2b5-3ed8-99a3-f80cb4d9563b | -4.0346 | -46.063 | 2025-10-26 01:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1d6f4bba-44c9-3270-8431-49b3de6e9dfb | -2.7755 | -45.0835 | 2025-10-26 01:10:00 | GOES-19 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 82edebe7-2898-3e98-b91f-fff3935a98a9 | -4.702 | -46.4286 | 2025-10-26 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 54d189f1-4387-3a8d-8a7c-978498506588 | -4.7206 | -46.4276 | 2025-10-26 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 56eb2a6c-0c06-3691-9333-f8054b8714ca | -12.04326 | -54.23875 | 2025-10-26 01:11:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2270c51e-2985-349f-b56b-db0608b4a0d6 | -10.20724 | -52.66186 | 2025-10-26 01:11:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ec6341a2-4e31-3608-a235-6594c0d5c0b9 | -11.09875 | -55.55555 | 2025-10-26 01:11:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8f97eebe-bacc-37a3-8972-d35ff4dee073 | -14.9164 | -52.46322 | 2025-10-26 01:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b939208b-7b5e-3ee3-80a3-7ce395fd404a | -10.20804 | -52.65601 | 2025-10-26 01:11:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 086a0f44-5887-382b-8a5a-47aaabe484b1 | -9.44992 | -56.65075 | 2025-10-26 01:11:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 324f9b01-c5b7-3487-aca2-2f7fc909a27c | -14.43963 | -49.96476 | 2025-10-26 01:11:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 892c1b88-25e4-34c9-9d65-eaaeb4215593 | -14.89758 | -52.47335 | 2025-10-26 01:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b434092b-24fe-3d62-bfd7-95c917515c25 | -11.95669 | -55.26371 | 2025-10-26 01:11:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 05d5c3f5-eb9e-38ae-976e-4e8bce01029a | -9.44838 | -56.64041 | 2025-10-26 01:11:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| e07f5ca3-ed1d-3fff-a942-164877d7066e | -11.36139 | -54.31454 | 2025-10-26 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 94e0f762-e056-3b3d-a832-c966e86160c8 | -12.5564 | -56.32092 | 2025-10-26 01:11:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 47860848-0dad-38e6-9bb3-a2c65fcb9d7c | -9.15412 | -51.30158 | 2025-10-26 01:11:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 7aacc43a-acdc-3b30-b9c4-32982a3368ca | -14.91928 | -52.4806 | 2025-10-26 01:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 44f0487a-96ab-3a95-8064-97b1be0140d4 | -14.90761 | -52.48243 | 2025-10-26 01:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 9b92a780-e6f3-3bd0-b9c9-a66ba0c01774 | -10.21121 | -52.67524 | 2025-10-26 01:11:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 50e4c897-0500-3337-859e-06e8c77bb500 | -12.89134 | -54.7389 | 2025-10-26 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 3b506657-aedf-3715-b128-a71c8f1a5746 | -14.9003 | -52.49042 | 2025-10-26 01:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c22cb943-6319-3d35-962f-6600717fef40 | -14.43508 | -49.93863 | 2025-10-26 01:11:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| ba1a194f-b940-345c-81d7-10513540b25b | -14.83395 | -52.45082 | 2025-10-26 01:11:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5313b5c0-7913-361b-801d-634cb1b3b9be | -14.89596 | -52.48441 | 2025-10-26 01:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 28aae58b-b263-3347-918b-07c9b80c2575 | -9.44446 | -56.64743 | 2025-10-26 01:11:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| b7c74e6f-e731-3454-81b5-cd70ab38e5b3 | -11.97787 | -58.065 | 2025-10-26 01:11:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0253cfa4-4f06-34db-9941-e0945833eb80 | -11.55569 | -54.52032 | 2025-10-26 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 76a43e2b-762e-30ec-b4fb-1bd16ee001d4 | -11.21473 | -54.83905 | 2025-10-26 01:11:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| d692b488-06e4-3af0-862b-2be2d270afb9 | -14.97539 | -54.83133 | 2025-10-26 01:11:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| ec6d17f4-5d76-3995-a958-450dd9df9517 | -15.27035 | -56.65422 | 2025-10-26 01:11:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6bae6aa8-8663-38d4-aca9-3eb8e3dcfd1b | -9.44296 | -56.63699 | 2025-10-26 01:11:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5f1ea70f-354d-3209-8083-845e898d20c2 | -10.9526 | -48.07587 | 2025-10-26 01:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 79d6b1e4-53da-3bd5-8a51-936280ad0041 | -11.31167 | -61.88612 | 2025-10-26 01:11:00 | TERRA_M-M | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d13226d8-b04c-320d-a62b-d9b34003fdf3 | -11.74668 | -50.24964 | 2025-10-26 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 950ddb02-a0dd-3b03-8ba4-0ae3e7a5cf2c | -12.88945 | -54.72659 | 2025-10-26 01:11:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 59554285-2827-36f8-bd33-ccbffd4f3a13 | -12.4198 | -57.80204 | 2025-10-26 01:11:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 57448266-2a3b-3ef8-9211-c9b4e7df3143 | -14.44211 | -49.95757 | 2025-10-26 01:11:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 02a79580-5733-3574-8508-3659af91d618 | -13.48643 | -56.5561 | 2025-10-26 01:11:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c0c31eb0-b7a4-31f9-95a0-fab25fb9690c | -10.63067 | -52.18628 | 2025-10-26 01:11:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| dfd5a632-cbd7-34e0-a45b-ca08188f55e7 | -2.92561 | -52.72732 | 2025-10-26 01:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 8a0bd951-f957-3fc9-9cc0-4473d0442052 | -3.78808 | -51.34639 | 2025-10-26 01:13:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| bba7d5e6-3982-3c6e-ad26-38f249567ac1 | -2.06924 | -56.87603 | 2025-10-26 01:13:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d49824b2-9183-3992-99b4-230fb5f64a4f | -3.86822 | -52.19751 | 2025-10-26 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 5e7d8c41-0efd-34a3-af6c-44dc12b046f9 | -2.33124 | -60.06553 | 2025-10-26 01:13:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 99532e3e-4fde-3b8e-943a-6d434ad08237 | -6.56835 | -51.11701 | 2025-10-26 01:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 3196e609-5315-32a6-9ba2-73c3d880d904 | -3.79545 | -52.01817 | 2025-10-26 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 22ee9578-ecf0-3569-86cc-88e38a11a3d1 | -4.19541 | -54.94474 | 2025-10-26 01:13:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b458f84c-8b38-3206-a66d-24ca70e468df | -2.68773 | -54.76803 | 2025-10-26 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 295e55de-58a3-3716-900c-2cc9262ef3ef | -6.57115 | -51.12346 | 2025-10-26 01:13:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a307bf9e-d484-3ff7-b454-99b6b7e257f0 | -3.79462 | -52.01175 | 2025-10-26 01:13:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8d049c35-d702-3dea-91fb-b3d8141f857e | -4.9667 | -56.26594 | 2025-10-26 01:13:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |


[Clique aqui para ver as próximas entradas](README4.md)
