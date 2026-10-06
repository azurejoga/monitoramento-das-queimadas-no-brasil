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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97da4be8-0f16-3565-ae3a-e7af040cfe12 | -3.1432 | -42.39384 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50534073-9121-3f9e-8ab2-02ce1668b957 | -2.94909 | -42.85812 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ecf8cbfd-066f-32c9-b9d2-f5037c05597f | -3.10153 | -42.9029 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffe48b95-a1c0-35aa-aca9-adff705285ce | -3.18285 | -43.88575 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e6371ad8-766b-3856-981b-2463cf2f851a | -3.30998 | -43.27816 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 52635a5d-3821-3e6a-a7a6-1068a01ac325 | -3.39053 | -44.47763 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e2f8066b-5007-3786-aa4e-2c4d55c8530d | -2.94542 | -41.4113 | 2026-10-06 15:37:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 65d4fb6f-b6cb-39ab-8f04-200be1ae957e | -3.29724 | -43.19295 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1a965a31-364b-3769-8071-ae902c432653 | -3.13781 | -42.96918 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ee54b0c8-fece-381e-884a-2562b19e7f01 | -2.99679 | -41.43414 | 2026-10-06 15:37:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| ac0db8ce-09a6-36c9-a964-9c8978c444f7 | -3.42057 | -44.32639 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2921e992-0d44-3a8c-a5f2-393a1e656081 | -2.9494 | -42.8152 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| dd89789d-9c9e-31f7-bc5c-3cc07c8e4c27 | -3.22167 | -42.81174 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1542e14d-cbc9-3e0b-b30a-d5896927ebe5 | -3.2143 | -42.77046 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f01e1a0e-b1a5-3bf9-905d-b40f9b0fdf73 | -2.99635 | -42.85835 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82c24d3e-ed4b-3438-8972-9eaf1c54cf6b | -3.13932 | -42.39579 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 34fc96c8-5cee-3294-802c-0ec1927daefc | -3.30913 | -43.27246 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f4ccfb25-d5f1-3e23-b214-f71c5f72be75 | -3.01745 | -44.01069 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 15298879-93e9-34ed-9838-d9c046985afe | -3.20236 | -43.4491 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1313f5a7-ff66-36cb-9904-125ad0a7bb62 | -3.17061 | -43.9039 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 770bcbfe-ef8f-3f1d-ab57-31811bb31845 | -2.99571 | -43.13327 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7d753179-92db-32c5-848c-87a35220c760 | -2.98765 | -42.85238 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 88b2eed9-fcd0-3009-8c9a-22439ca6290b | -3.11321 | -42.70483 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91432a78-4aa8-3825-b91e-cad2e64c6fc7 | -3.02762 | -43.30629 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a305dd4e-c4a6-348f-ade0-fb1f8191b4fb | -3.13742 | -42.96704 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 81309bee-5933-3365-87cf-ab9264185fe9 | -3.19351 | -42.94258 | 2026-10-06 15:37:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0c03d0e5-eb9d-342c-a277-a9ca6838eb4f | -3.1468 | -42.85279 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ebcf2854-0509-3393-9ad3-e0f02f7eb0a9 | -3.14716 | -42.8503 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6559dd58-2575-3e64-8c5f-35413603c9ec | -3.21524 | -42.81269 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b4d4930c-97f6-3d06-8957-1a1efcf6c93d | -3.17048 | -43.05429 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00d642e1-8bba-3acb-9495-d983ba5c017f | -3.20789 | -42.77142 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e69a9d1d-5948-39ee-b9e8-4f3bbb6788d8 | -2.9956 | -42.85304 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bfcaa06a-076c-3bb8-afa9-77146490d5fd | -3.26082 | -42.99399 | 2026-10-06 15:37:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 9a7db941-f85b-321e-aac6-cb361061188e | -3.39156 | -44.4845 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| be52497b-3020-3382-a66c-5187d9f93d16 | -2.99616 | -41.42986 | 2026-10-06 15:37:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 310d3794-60d6-3c82-aeb5-17f9f59dbb48 | -3.40006 | -44.46843 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 308.1 |
| a834a2d3-7784-34f9-b962-5af39998ea8e | -3.3326 | -44.57909 | 2026-10-06 15:37:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| d1cd8940-de35-32f2-a988-5600de192692 | -3.00204 | -41.42902 | 2026-10-06 15:37:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 569a9721-55b9-3f95-93eb-5c5f03d94614 | -3.27477 | -43.08747 | 2026-10-06 15:37:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b653f32-4835-322f-8a6b-4873a3232b1c | -3.00145 | -43.12683 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4622182a-e765-349c-a632-6d35f89f846a | -3.42276 | -44.32521 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 591ac4d9-d786-3e85-bd3b-7d768e1f09c4 | -3.39393 | -44.47635 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| afe5a970-c83a-3758-856c-ea81a0491ee6 | -3.20923 | -42.77017 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b2adbb47-46d8-3729-98b2-a4cfb3537439 | -3.40106 | -44.47537 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 308.1 |
| 47ddfc29-b95d-3cba-8758-37bfbaae0b2b | -3.17746 | -43.90283 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 922e57b3-10b9-3bc7-8253-7692d8a42d40 | -3.00286 | -43.27513 | 2026-10-06 15:37:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1fca47fc-fe73-3801-a6a0-cdb4cf50bf3e | -3.22062 | -42.81299 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55bd3fac-42d7-398a-9fff-2c363296a03c | -2.99487 | -42.85675 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fe047e88-bab0-39b0-a4ac-fe384ef4e37a | -3.07874 | -42.59962 | 2026-10-06 15:37:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db42367a-704b-3de4-a9b8-d9d3be8dce8a | 1.9864 | -55.8789 | 2026-10-06 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 15b7c781-784a-3917-9f66-9339fc7bbc4f | -8.9257 | -66.8549 | 2026-10-06 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9ce56bba-ddf5-3f94-9b0c-a4f0c4856fd4 | -9.0399 | -66.1079 | 2026-10-06 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 3cc3e01c-c55d-37c7-b216-df6e57c7feef | 1.8951 | -55.7224 | 2026-10-06 15:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 6cb41752-6cc7-3dab-8fd5-6fa8c10eed45 | -9.8244 | -65.0535 | 2026-10-06 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3f46e7d5-c200-3b6b-a8cd-d33f115d5abd | -8.6034 | -69.3374 | 2026-10-06 15:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 4e9e0a18-0de1-3fd3-b39f-c8afac82161a | -9.0097 | -69.4036 | 2026-10-06 15:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 742cedae-5e51-3a0d-afdc-5252d61ce08c | -7.8973 | -72.349 | 2026-10-06 15:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 92dab381-b5cc-3ff2-bf0d-a62e8242cbd6 | 0.3221 | -51.0038 | 2026-10-06 15:40:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 140.2 |
| 2feb1d15-5899-3e3d-8373-0383c0f2215d | -9.1072 | -67.8326 | 2026-10-06 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 692c4c0a-0773-39a8-9eb8-6237698d2f11 | -11.8814 | -64.9323 | 2026-10-06 15:40:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e0600b3f-4fa5-3703-a7b5-b15c5755b007 | -8.5733 | -67.1422 | 2026-10-06 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 809fbdae-8e0e-31d4-bfbe-9f9f1de0c466 | -9.4819 | -66.7836 | 2026-10-06 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1aa8d532-b8eb-335a-ba40-8fd83c94ae9b | 1.5649 | -55.9829 | 2026-10-06 15:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| ce9fad48-0957-351c-9a65-5b6ac210153e | -11.21 | -46.2655 | 2026-10-06 15:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 419.1 |
| a36f41ce-d02d-3180-b127-aef1787147db | -9.8844 | -64.2802 | 2026-10-06 15:40:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 79.6 |
| f1d0a9f3-4fb7-3574-b9d6-b239c3fbaed0 | -9.077 | -66.0881 | 2026-10-06 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| aeff2bda-b72a-3903-b804-6aad378b5354 | -11.4503 | -43.4091 | 2026-10-06 15:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.0 |
| c650e8ba-7b08-382a-8c65-d9cc5c104204 | -9.0098 | -69.3852 | 2026-10-06 15:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 92.8 |
| ba95116d-1b27-3fff-99a1-1c8b1ac25018 | -9.8619 | -64.9958 | 2026-10-06 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 6adc250d-5135-3db8-9ebf-01ff0e634bb8 | -9.1334 | -65.9 | 2026-10-06 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 38002f26-da3b-32a9-bc99-30632187b320 | -9.0584 | -66.1073 | 2026-10-06 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| c916f7b7-b1fd-3c62-9c35-d4d7d3f97dd4 | -9.0347 | -67.39 | 2026-10-06 15:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 2bb55bfb-54d1-325f-ac35-3eb6545830ef | -11.8814 | -64.9323 | 2026-10-06 15:50:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| d2a96c16-e8ab-3609-9617-b171a9676521 | -9.8844 | -64.2802 | 2026-10-06 15:50:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 88.3 |
| b4a7fdbe-c929-3f94-9a53-7ee9af26a7a7 | -9.1221 | -64.4031 | 2026-10-06 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| a135da88-5a4d-32d4-852c-812345d9d418 | -9.1076 | -67.703 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fca45d12-fe67-39a7-946d-32c5746b760f | -9.1511 | -66.0859 | 2026-10-06 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b196c95e-6668-3515-b255-68c028448509 | -9.1072 | -67.8326 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c463dacd-9f13-3905-8341-d9a8dd958005 | -10.9758 | -45.4324 | 2026-10-06 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 87d1dd7a-f6bd-38fe-878d-1417823d0ebe | -9.1241 | -68.2946 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| b488adad-f179-33fb-b642-de8d6a749597 | -8.5733 | -67.1422 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 509e0e9b-2007-3b30-8076-6ff426c5d9a0 | -9.4819 | -66.7836 | 2026-10-06 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3607a988-9108-3cd5-8154-0f97ba8c1b95 | -11.657 | -43.6373 | 2026-10-06 15:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 303.4 |
| c2d075f8-13b6-32cc-ad35-9eed1f2f1945 | -8.6034 | -69.3374 | 2026-10-06 15:50:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e89bbc13-b181-39df-8398-2c33c9894c1f | 1.8951 | -55.7224 | 2026-10-06 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9395a9ed-1ce9-3020-a385-435347c65e57 | -9.8059 | -65.0354 | 2026-10-06 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| a79a27ed-9853-3761-a239-8842fe7a05ba | -9.0401 | -66.052 | 2026-10-06 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| d03f5e87-6894-31c9-a91a-f38711807563 | -11.6763 | -43.6343 | 2026-10-06 15:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| d8d66ce7-29e8-3a95-9b6b-7fc57702e96e | -9.5175 | -67.1359 | 2026-10-06 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 41079eb1-142b-3a3c-bf52-885857abd05f | -8.5183 | -67.0139 | 2026-10-06 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| fb4a68ad-c801-3f0a-a659-8435ca4311b3 | -9.0098 | -69.3852 | 2026-10-06 15:50:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 43.5 |
| e027ab34-bef2-3ca3-bdc2-b20eee3d851d | 1.8038 | -55.5458 | 2026-10-06 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 07cac101-b151-3def-801b-88ce10730d12 | -9.8244 | -65.0535 | 2026-10-06 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8e050e0d-742b-359c-a783-05ff312b3193 | -8.5368 | -67.0135 | 2026-10-06 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 6d0d6909-64de-3e6e-a6aa-18820abf82c2 | -9.1257 | -67.8322 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 63648b67-6dab-3a00-b159-9909b6c40c2e | 1.8767 | -55.7424 | 2026-10-06 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 6c23ceab-10ee-3e5f-a3a4-7807e9251bf4 | -10.7767 | -68.6252 | 2026-10-06 15:50:00 | GOES-19 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 6753c513-2988-3d10-89de-64c626411053 | -9.1426 | -68.2941 | 2026-10-06 15:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 5664bff7-4565-3112-bdae-fb22465f1f21 | 1.7855 | -55.5461 | 2026-10-06 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 64d66394-0eab-37a2-9d94-132201632760 | -9.885 | -64.167 | 2026-10-06 15:50:00 | GOES-19 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 83.4 |


[Clique aqui para ver as próximas entradas](README93.md)
