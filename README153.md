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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e623d29-837e-32a7-914b-0b9be543915a | -9.01353 | -67.74865 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1c0cde72-1816-36c0-b50b-3cf0fcf3fdc5 | -9.12115 | -67.94479 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2d91e256-6c45-3cb6-a392-b4fcc5b57474 | -1.80592 | -53.75475 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a22ecf0c-65d9-366c-967e-a4fa0e9cfc33 | -4.05944 | -69.56358 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 266db15e-df4a-3f19-9060-232311ef855f | -10.61547 | -68.67802 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 29d6f430-867d-372c-a5d8-93f485b6cf5a | -9.2316 | -65.84687 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c61d6da-4ae8-3fec-b717-e905c40b0278 | -3.03677 | -59.20837 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9a57142f-c360-3d1d-84e4-da405134b94b | -10.12674 | -69.30244 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7b7cec8c-180b-385b-84be-86f5808554bc | -9.11071 | -68.25667 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cc62e552-9726-3dd6-b4f7-1e14db10ed26 | -9.17202 | -68.27058 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e94de7ea-897f-3ea2-9e39-975bb4a9cb43 | 1.16046 | -50.73325 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7f2cf47f-6f55-364b-8a22-acfa83782de7 | -6.64902 | -55.32525 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c3d5e7eb-04b7-36d1-98d8-daa037a9d33d | -9.62835 | -68.65944 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 36d4001b-fadf-3760-b92a-b91f4a7d5072 | -1.61674 | -55.11268 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 741dc244-36d0-30e4-b1ef-6827d3bfe092 | -1.22845 | -56.2055 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4fab2446-a1f3-3226-b6c0-35f94c682532 | -3.10453 | -59.73598 | 2026-10-05 17:37:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 33b5cf49-acc8-30c0-be6d-0faf7f7f56b8 | -9.10677 | -64.37777 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 31.2 |
| d7ce47aa-b8f9-31f8-8bf8-d9829f6735c5 | 1.57464 | -55.99582 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bfb80778-2521-3a30-8bc0-67af37fb09b3 | -9.48107 | -66.78802 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 85287cfc-2215-3b20-9705-01676745f3bd | -8.5395 | -54.59654 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0fc2d388-c9b5-3bc6-a91f-0386ad74c16d | -8.97325 | -71.40679 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 39.2 |
| f9b77d3e-b2ae-30bf-aa07-e1337671e35a | -8.43529 | -55.01688 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af6839ce-44f0-34a4-9987-7daefdea43fd | -8.96571 | -69.30564 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 25.6 |
| fbb1ba38-b18d-354f-b34d-c25436900a8e | 0.30001 | -51.0907 | 2026-10-05 17:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2bdaf420-f1dc-346c-ae64-4d04fb07bf4b | -10.48417 | -68.63063 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0d34bd7-5842-37ca-8d0f-48eda354451d | -2.77194 | -57.67658 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 9e8d11c0-46c1-3254-8170-58171987605c | -8.58747 | -69.98276 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e38bab93-4ab6-3b3a-83db-56d59d81a713 | 3.95264 | -59.85523 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0cf268b0-dbb1-39a1-a64e-b097a037605f | -7.90286 | -54.75791 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 92ddaec0-55e8-3539-a6f8-82e44420f281 | -9.47787 | -64.33875 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ea34a162-12ea-379b-866f-87d948971309 | 1.79509 | -55.54516 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2c3eedc0-5723-3b5c-a94a-2e202dfcd7d9 | 2.08753 | -50.90604 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 76fc5968-ec13-3e29-ae7e-fd7f8802af31 | -2.19701 | -54.48448 | 2026-10-05 17:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| feaf80fd-214f-3fef-9078-311a2cc51d23 | -8.77061 | -70.77816 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0722f923-09b6-3f9f-a518-5f28536318ba | -9.01368 | -68.37391 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95e4c7d6-2bc2-3e83-bb6e-125c7fc2ece6 | -9.1252 | -68.20749 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9f9e5d0e-c1aa-333e-8ec7-4a86a56cd306 | -2.95208 | -65.19962 | 2026-10-05 17:37:00 | NOAA-20 | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2319c03c-080b-3a85-ad85-93f5bfe089b8 | -8.89047 | -68.53384 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ce46d37a-3b80-3fb4-be76-e3d5412e322b | -3.54224 | -69.37191 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fd6051d8-4d79-33df-8f99-9afea2bb0cfd | -9.39941 | -65.8945 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 118ea0b5-03d2-38fc-8558-1d9a2400eae3 | 2.28531 | -55.84979 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c201530e-e5f1-3559-b7d9-71538187b77f | -6.46064 | -55.44997 | 2026-10-05 17:37:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 3cbb1309-d4b5-3b6e-a46e-d3130012447d | -9.15833 | -68.25948 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 459d870b-7b32-3434-a4e9-f62c37ffb588 | -10.73207 | -69.59952 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2d8479c8-48d0-375d-a157-1f4a76382d16 | -1.73759 | -56.07747 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9390467e-f403-3e0d-bfff-df471851e696 | 1.59135 | -55.97317 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ea1f9e7a-8198-3035-b1b5-e9c09104fa65 | -9.13199 | -64.38464 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 248c197b-a7df-3d3e-ac73-24128e44e4fe | -8.86065 | -66.79167 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2b03884b-b010-3cfa-a3ba-c5e4939e8ace | -6.81388 | -55.29535 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4bd46afa-9cfa-3714-8f9f-30830162a9c0 | -9.10997 | -67.82459 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 344dddc1-6c3d-3b63-9503-36b9d31a09e8 | -8.84834 | -70.60076 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4a293742-3495-31db-96ec-e698272c5337 | -9.08066 | -66.08508 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 83ca296f-ee71-3d4f-b0f4-436e8ff8454f | -1.0041 | -57.50157 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 77927384-d3ba-3680-9428-de16832d6bfa | -9.40786 | -65.88969 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b87b9965-5817-3da2-8e09-01f7078ddf38 | -10.15237 | -69.01954 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 32.8 |
| cfa9d585-8ca7-332f-b5b7-f21f8d5b2e6c | -8.60089 | -67.13777 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3fd670de-4a9e-3a76-8fa1-90f6e706ef75 | -1.26382 | -54.55364 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| dafb4180-e1e0-352e-8c84-54ecc7217410 | -1.66755 | -55.06607 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 49744a24-393d-374e-b912-3b7beef6bcbc | 3.07912 | -60.60146 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a647944a-3d6d-323c-8b4f-dbc94597c38c | 1.87214 | -55.75541 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 049c4d15-4942-38a6-bc21-dfeb78c1a2a6 | -9.91825 | -65.01775 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6be70c96-b438-3689-a0b7-93ff0589bd0f | -8.60093 | -67.13017 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8953a959-e27b-329f-9b6e-92b21c33ae2d | -9.02844 | -68.36565 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4778a4e0-56d1-35c7-89f6-4246973bf916 | -9.16058 | -68.23714 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c4589ae2-d265-388e-b47b-94b0a58b260e | -9.41543 | -68.54872 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0acd2e16-7e39-32e1-b471-8df55d73f199 | -8.43583 | -54.99597 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 1c5423b1-83ed-37b7-9d4a-5e2e9b1e78fd | -8.8517 | -67.00447 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 14d5aed1-eb78-32f3-8c6e-22bd2e3e7c98 | -1.73351 | -56.0781 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1258591d-5901-390c-97ee-5d52250c38df | 4.05677 | -60.2481 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0dfe4f7c-0842-30b8-9090-f34caf843dac | 3.39936 | -51.53528 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 206aa7b7-7a04-3c46-8410-4f2123d38d4e | -8.62669 | -69.50397 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 25a4d85b-49c7-34bc-a5d2-dbed9806f907 | -2.18133 | -56.22771 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59bf0a84-655a-3f42-afdb-a36c59e40ce0 | -9.40001 | -65.8988 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5fec65ee-9237-3863-bd28-837f39fc9a4a | -8.702 | -66.76181 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 014345f2-8111-370e-985b-c6dbaac66d7c | -9.47938 | -68.75527 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 300b36a8-48d8-3162-a7d3-93441eb4cd0d | 4.28512 | -60.33787 | 2026-10-05 17:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ec25b2fd-a921-3b15-a53a-458260aed2c0 | -1.97032 | -55.676 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d102753f-5dba-3c14-ae6c-f474d7fa101b | -4.06035 | -69.56985 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 76b38b1d-6fe4-35bb-8ac1-6afc315e079c | -8.64438 | -69.59693 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f0f2e54d-de4c-315e-b2ee-89ffc2a16612 | -10.14373 | -68.39356 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 298e4293-2951-3c18-b823-cd9ae790947d | 3.58019 | -61.36517 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c720f79d-68d8-3342-86a3-d0d47f633b6b | -8.77336 | -66.56551 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 16459cd1-cb59-3f70-bc6f-531fa8c7fe95 | -10.41843 | -68.95108 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6a650b18-d88d-3c3a-a5b2-35198740fbc1 | -6.67402 | -55.07507 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fda60ab9-ce4c-397b-848d-9ef71b4d6ede | -9.13668 | -64.38921 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 24891413-31d9-3b49-bc59-c46b225fd2ce | -9.1799 | -65.79375 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| aff7d539-c6c0-31fb-a470-63189e4bf5fa | -1.90271 | -56.32965 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f857617b-a46d-3829-b11c-5be7145aa7da | -2.77357 | -57.66326 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 93e806db-f6d4-3e4a-b540-7b45f01f406d | -8.42226 | -54.98769 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| fadd5789-882e-3c8d-85cf-66f9ae83c4ce | -1.46408 | -53.60461 | 2026-10-05 17:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 283cb7a7-7d6e-302e-a06f-addb6b3bb08f | -3.17389 | -60.05322 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9d69f9e3-23c2-3dd6-844f-6d187cd7a2ea | -2.93148 | -58.39149 | 2026-10-05 17:37:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 751107bb-7c5c-3ff2-9f4a-ac8d2453d538 | 1.54046 | -60.38161 | 2026-10-05 17:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 74e8e7e4-8c3f-3dd4-801c-4f559ee9beb2 | -8.65251 | -67.44727 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4874dfa-3402-3369-b86a-bd6649a48973 | -9.17548 | -68.26977 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 1333260d-28d1-3020-9ee3-be8cac8450d5 | -9.09996 | -65.48493 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b561ecc5-f497-3384-9f72-3d65aa1a20cc | -9.33595 | -68.79129 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 036ca12f-ba91-3ac5-a61c-b9c5eb7c741b | 4.31927 | -60.20562 | 2026-10-05 17:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9973e7a-f4d3-33d5-9790-a1c25f67bf25 | -9.40521 | -68.88031 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.3 |
| adabf4ab-1b95-3153-9f96-feb5388e3819 | -10.41686 | -67.97472 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 18.2 |


[Clique aqui para ver as próximas entradas](README154.md)
