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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed0aa9b2-e178-3bd4-9e16-d7622585428c | -3.47691 | -42.10619 | 2025-11-26 12:36:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 197.5 |
| 0bc85bc1-9b2c-3bf0-bf2d-7d8e8ae74589 | -3.52249 | -42.14597 | 2025-11-26 12:36:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 938f13bb-cd9c-34aa-bb20-f1b1b492e38c | -1.31839 | -53.13612 | 2025-11-26 12:36:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cec8bcc1-e98b-3f95-b00b-c0e9e7f1f131 | -2.92013 | -51.30811 | 2025-11-26 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c0131ba7-ab7c-3339-ae0c-162433eeb7e8 | -2.87691 | -51.80013 | 2025-11-26 12:36:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0cfe9692-db18-3b22-a250-45dfad5e20a2 | -4.18226 | -43.70792 | 2025-11-26 12:36:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 9218de64-8490-399a-99bd-2c3dc3a2b464 | -3.55579 | -42.43907 | 2025-11-26 12:36:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 149.8 |
| 26f18b9e-5291-3bbe-b97c-01118282c980 | -3.28408 | -46.02286 | 2025-11-26 12:36:00 | TERRA_M-T | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 001c008a-c348-34b7-8d01-446b7bc51f43 | -4.05239 | -43.55021 | 2025-11-26 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 4da689c3-2875-3fc9-9459-53b7c5d591a4 | -2.12573 | -50.1529 | 2025-11-26 12:36:00 | TERRA_M-T | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8391691e-45b5-3d1b-a39e-7ecc9cb7cbf6 | -3.47572 | -42.09905 | 2025-11-26 12:36:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 158.3 |
| 0d7c4b23-fab5-3592-83de-2223847b57c1 | -3.52394 | -42.15312 | 2025-11-26 12:36:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 68db503a-c2fe-3553-ad73-c3ef6b12824e | -2.89266 | -48.02768 | 2025-11-26 12:36:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| b0b8b855-283d-3627-9542-05e100614127 | -4.1834 | -43.73314 | 2025-11-26 12:36:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 79f127e7-5ee8-3b28-aa27-a6bf8571ec3b | -3.54219 | -42.44235 | 2025-11-26 12:36:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 256ac3b9-f815-3d9b-a7e8-8afc17df58f7 | -4.17831 | -43.7392 | 2025-11-26 12:36:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 8b3fea4c-92a4-3760-8a14-ff71fbbeb7b5 | -2.24209 | -45.78999 | 2025-11-26 12:36:00 | TERRA_M-T | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 25.2 |
| eb5496e0-e67a-33a2-840a-b0939d174a8c | -7.47289 | -45.17338 | 2025-11-26 12:38:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4bfb29fa-0939-32ae-a373-72f53fd307c2 | -8.0614 | -43.11095 | 2025-11-26 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| aff49179-9b4d-3d22-80cd-e65d4a934f6a | -4.65583 | -45.85252 | 2025-11-26 12:38:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| f6de417a-2dd6-319e-96a4-f42e7341be56 | -7.45912 | -45.17855 | 2025-11-26 12:38:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| d184fcf2-0b53-3352-9411-ad2ae47ac44b | -4.70704 | -43.99923 | 2025-11-26 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 1a70b044-90b1-342d-9129-b178d0f21d61 | -4.65294 | -45.87362 | 2025-11-26 12:38:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9fbb3cf8-7658-3480-9c32-6d0f9ab20d48 | -4.71086 | -43.99296 | 2025-11-26 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 50a1ee3a-4243-336f-a2bb-e9b44714b50f | -8.05947 | -43.10353 | 2025-11-26 12:38:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |
| fa441586-bbee-3ead-bf5d-303d0b953c1a | -4.65206 | -45.8587 | 2025-11-26 12:38:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c7d2f2f0-fa74-38c2-b746-e1db284a4817 | -8.40399 | -44.0097 | 2025-11-26 12:38:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 988011db-ac3c-3e71-9ede-0e0ecbd283f4 | -7.95331 | -44.33876 | 2025-11-26 12:38:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b2074bd3-9617-3371-ac58-ea4f7f050293 | -7.47384 | -45.17992 | 2025-11-26 12:38:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 71fa3449-1c6d-3884-81ac-8e0e81d78261 | -5.28855 | -43.37967 | 2025-11-26 12:38:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 7a05fea6-3331-39c9-94ff-606a2c6346bd | -4.57069 | -43.31018 | 2025-11-26 12:38:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4966721d-da23-39cf-8a14-56ee9911fc37 | -4.57931 | -44.06158 | 2025-11-26 12:38:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| b4a5c9f1-037c-3d54-89dd-a77f30a684ce | -20.87122 | -55.56604 | 2025-11-26 12:40:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 00665de0-dea0-393d-9da3-1d301118c7bd | -20.40681 | -57.96716 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 7d93a8b1-d8cc-366a-b133-e1b67a65f604 | -12.18073 | -54.24158 | 2025-11-26 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c0b8e423-df1f-3a05-bcda-9832674e6b01 | -19.60994 | -55.55305 | 2025-11-26 12:40:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 81f8e131-376a-3859-a262-7300f5b44f84 | -15.63257 | -56.44262 | 2025-11-26 12:40:00 | TERRA_M-T | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ab6144f5-f6b2-3ee5-8e86-9383a47bfba4 | -12.92468 | -49.04415 | 2025-11-26 12:40:00 | TERRA_M-T | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4ea02798-a630-324d-b13a-27f772b2d8d1 | -20.07309 | -57.18849 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4a1ca0c3-0660-3498-9a9a-71ace65d5ee6 | -20.41599 | -57.96873 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.4 |
| 765cbe46-23f2-370e-9f1c-d50c4b2aee12 | -20.87254 | -55.55657 | 2025-11-26 12:40:00 | TERRA_M-T | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 47674906-d836-322b-b462-3e63cedce51b | -16.01687 | -55.21404 | 2025-11-26 12:40:00 | TERRA_M-T | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6b81b9e9-ad14-3391-b495-5fec5f40fb6a | -18.09946 | -54.16229 | 2025-11-26 12:40:00 | TERRA_M-T | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a4292984-6ff0-3cb2-b7bb-59ab97f068c6 | -13.24974 | -52.11836 | 2025-11-26 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8228345b-0fd4-3c31-b6af-5f89caf8a49c | -20.3992 | -57.9554 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| fc846531-8930-3219-9669-33a16f9c8426 | -13.17048 | -51.95204 | 2025-11-26 12:40:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 81eb3b58-18a6-315c-9e18-e099e1a3c496 | -19.51114 | -54.06719 | 2025-11-26 12:40:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 066d4aab-ad47-3415-83b6-6d4cfb70d5c9 | -15.79009 | -55.69074 | 2025-11-26 12:40:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6672e7a9-8287-3e15-99f6-f62f54e996fe | -19.61878 | -55.55441 | 2025-11-26 12:40:00 | TERRA_M-T | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 1160a67a-fb0d-328f-bb8f-ebe828accc30 | -20.00824 | -50.58498 | 2025-11-26 12:40:00 | TERRA_M-T | MESÓPOLIS | SÃO PAULO | Brasil | 3529658 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| eda3de5e-b72d-3775-bfb4-f2a3fe8408dd | -17.64699 | -55.61185 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 27da307b-7a1f-311d-91e9-4768336eecbf | -13.18383 | -51.99673 | 2025-11-26 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 04d42731-a6cb-3bac-b2f9-d63156b779d0 | -20.39762 | -57.96559 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 890315c3-2618-373b-aae2-cfe739d70e95 | -13.4038 | -52.34046 | 2025-11-26 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9be02426-2541-3647-9442-53c1108c77eb | -20.0101 | -50.56815 | 2025-11-26 12:40:00 | TERRA_M-T | MESÓPOLIS | SÃO PAULO | Brasil | 3529658 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.0 |
| 01dbe5d2-0340-30fa-9c3d-d2d3d0dc70d1 | -14.70788 | -56.98866 | 2025-11-26 12:40:00 | TERRA_M-T | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d27715b2-cf9f-3cfa-9074-ba16817db6bd | -17.592 | -53.62183 | 2025-11-26 12:40:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 05e418b0-ddcf-3743-b5f1-f2481dd6281f | -20.07163 | -57.19818 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7418c543-1427-346d-9bae-5d59a7e1c6cc | -16.55224 | -54.75647 | 2025-11-26 12:40:00 | TERRA_M-T | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f908d03c-6482-3537-ad93-67250613e579 | -13.10983 | -52.67682 | 2025-11-26 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6360c13a-01c9-31e2-8b07-3aca95cfd86b | -14.92317 | -57.29045 | 2025-11-26 12:40:00 | TERRA_M-T | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| de6a92f1-d868-3ebd-ba71-0b3bb060be52 | -20.24475 | -50.62614 | 2025-11-26 12:40:00 | TERRA_M-T | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| aca9a7d3-a47f-39c1-b36d-e8a2342a0893 | -13.16587 | -52.38807 | 2025-11-26 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a74bb9fa-1932-3a59-b0b1-de7653ce7815 | -17.64566 | -55.62106 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.9 |
| c3cb4a26-ed8f-3d21-a958-7bd4913a7cf2 | -20.40839 | -57.95697 | 2025-11-26 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 355f71ad-4eeb-3765-89d3-fcd8d7ddd728 | -22.21271 | -49.66027 | 2025-11-26 12:40:00 | TERRA_M-T | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.6 |
| 93b511e8-7926-363e-a9b1-7f8afcc07a1f | -17.59332 | -53.61183 | 2025-11-26 12:40:00 | TERRA_M-T | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a0257f92-d3c2-36f1-9fab-d4721992602e | -24.1226 | -50.7991 | 2025-11-26 12:42:00 | TERRA_M-T | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| d12627c0-f480-3101-b0e1-b3c8db548a4b | -22.83143 | -52.89162 | 2025-11-26 12:42:00 | TERRA_M-T | NOVA LONDRINA | PARANÁ | Brasil | 4117107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a1c9ebaa-8bc3-31a2-bb4a-dbe6a2f16ce0 | -29.224 | -51.33379 | 2025-11-26 12:42:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 2ed00031-d162-378b-ada8-771c19bdf043 | -24.12457 | -50.78012 | 2025-11-26 12:42:00 | TERRA_M-T | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.3 |
| edab79af-102a-31a9-8631-b690154e8c64 | -28.97587 | -51.07076 | 2025-11-26 12:42:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 4df52de3-25a8-3c42-9437-c579777f02b3 | -24.33507 | -50.6238 | 2025-11-26 12:42:00 | TERRA_M-T | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 1aadd6c3-1254-3914-8703-eb46c0412855 | -26.35342 | -52.84227 | 2025-11-26 12:42:00 | TERRA_M-T | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 6e2810a0-5d53-3125-8ceb-3dff27e9924b | -28.75218 | -51.91138 | 2025-11-26 12:42:00 | TERRA_M-T | SERAFINA CORRÊA | RIO GRANDE DO SUL | Brasil | 4320404 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 744f2602-832d-3a87-b782-4ce5a6ee2a56 | -23.77336 | -48.8712 | 2025-11-26 12:42:00 | TERRA_M-T | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 09d4bd94-2393-3f8b-8df2-d72689d8a952 | -29.19043 | -54.86458 | 2025-11-26 12:42:00 | TERRA_M-T | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 6.3 |
| 8766685b-c6cf-3495-8254-9a9f9e1d2dc7 | -21.81056 | -56.28476 | 2025-11-26 12:42:00 | TERRA_M-T | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2ef9270d-1e8e-3db0-b147-a928d1d028c2 | -22.4159 | -50.57526 | 2025-11-26 12:42:00 | TERRA_M-T | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 15.2 |
| bc5c6b2b-aaf6-3764-a2ea-c4aa9ae631f7 | -25.69688 | -49.80502 | 2025-11-26 12:42:00 | TERRA_M-T | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 842cf47e-2860-35ce-bda1-8b9164a8b04d | -29.64062 | -51.73782 | 2025-11-26 12:42:00 | TERRA_M-T | TABAÍ | RIO GRANDE DO SUL | Brasil | 4320859 | 43 | 33 | nan | nan | nan | Pampa | 12.1 |
| 0f3d8969-45d9-3f13-b101-6d656bc231aa | -29.74008 | -56.29937 | 2025-11-26 12:44:00 | TERRA_M-T | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 5.4 |


