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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c6eb13-9586-3ef8-bccb-792b3dc66959 | -1.5494 | -54.2957 | 2024-11-21 14:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 46bb2188-9e36-3716-98d3-a6cf6182f959 | -5.2538 | -42.6472 | 2024-11-21 14:00:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 13d099ba-e974-3e33-a84b-ffc567ba07d7 | -5.2351 | -42.6486 | 2024-11-21 14:00:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 12afe319-ceea-3541-895b-3d523d7092b9 | -2.0075 | -54.5292 | 2024-11-21 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| cadba17f-770f-3571-ae81-9e01278521a7 | -2.0259 | -54.5289 | 2024-11-21 14:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| ed417942-aa27-39b4-ae82-0b264f3d2ea1 | -3.5202 | -44.9186 | 2024-11-21 14:00:00 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 6b9795c6-e6f6-39e8-8b8f-5403511ea1d3 | -4.2219 | -42.9958 | 2024-11-21 14:00:00 | GOES-16 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 54f1397c-689d-3097-8863-fb8bc6c3bd00 | -2.4101 | -48.6123 | 2024-11-21 14:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 27246e68-d2c6-38e9-9147-912d2d28f105 | -5.2464 | -43.5369 | 2024-11-21 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d0d166b2-043e-338a-a4f1-3451adf3ea98 | -4.3692 | -43.314 | 2024-11-21 14:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 0cd17350-c510-3698-be7a-b9619810ec2b | -3.7858 | -44.0622 | 2024-11-21 14:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 1deac322-f233-3c05-b76b-fb9f814db38a | -5.2538 | -42.6472 | 2024-11-21 14:10:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 9bf3d487-a958-352e-b71b-d6ad41571069 | -5.4363 | -43.2206 | 2024-11-21 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fb96382a-d8bb-34ce-ba69-f9b61d21bf94 | -4.5881 | -49.7055 | 2024-11-21 14:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 4213413d-4465-3637-9fe7-859cbdb63f20 | -2.0259 | -54.5289 | 2024-11-21 14:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| e73758ed-ec3b-3ea5-b9c5-6e85c4cdfd63 | -5.5113 | -43.2151 | 2024-11-21 14:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| e6ab4a1c-2f98-3dbc-b41f-962d656b7d01 | -5.6217 | -43.44 | 2024-11-21 14:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 04fa84fc-9474-3c45-90e1-837866074195 | -1.5494 | -54.2957 | 2024-11-21 14:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 00bf8b31-4094-35b3-b7bc-84250e514a3d | -2.0075 | -54.5292 | 2024-11-21 14:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 9f45cfb8-a33b-3bac-bfc2-474d9128dc60 | -3.6018 | -43.6331 | 2024-11-21 14:10:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 491d7267-57fb-30d4-8da1-d78f4a883615 | -10.42 | -44.4705 | 2024-11-21 14:10:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2734cff8-1bf2-3604-8834-bc9ff775cee4 | -2.0259 | -54.5289 | 2024-11-21 14:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 15d041b1-a2c8-311c-9292-44a8b179985b | -5.4546 | -43.2659 | 2024-11-21 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 69418a6b-1c40-38a7-a0e4-d62a894fd885 | -5.4363 | -43.2206 | 2024-11-21 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 6408a76e-ab0e-3763-a3ca-73e19b2d4a18 | -4.0148 | -43.2408 | 2024-11-21 14:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f93f0db7-dd55-3204-8f05-e89c1fba2e33 | -5.529 | -43.3304 | 2024-11-21 14:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| fab24e64-177d-3de9-97cf-2941bf64ad3a | -5.2538 | -42.6472 | 2024-11-21 14:20:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 29c3ca82-8d81-37e2-b1b8-bb52dd007b2f | -5.2351 | -42.6486 | 2024-11-21 14:20:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3f178c14-f64a-3b94-972e-ced950bdba29 | -3.3924 | -44.4467 | 2024-11-21 14:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 827a7be1-4cff-3120-84c5-ce2027828a6b | -3.7858 | -44.0622 | 2024-11-21 14:20:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 3eb002d6-8f76-3d69-9831-30d2371c9e77 | -2.0933 | -49.557 | 2024-11-21 14:20:00 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e9afa754-d248-3969-8b01-3caa7c886517 | -3.9537 | -44.0538 | 2024-11-21 14:20:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 12c4342b-62ab-370e-b9e3-6e979965ea41 | -10.4196 | -44.4937 | 2024-11-21 14:20:00 | GOES-16 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 12577ddf-627c-39c0-aadd-df1141d83c08 | -2.0075 | -54.5292 | 2024-11-21 14:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c9dcffa9-fe99-3e5a-8d92-d3d65c4f5a85 | -4.3692 | -43.314 | 2024-11-21 14:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 16480152-3d5c-3ae2-ac5e-d4c30872785d | -7.6802 | -38.2568 | 2024-11-21 14:20:00 | GOES-16 | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 124.7 |
| 6ff6a4d5-7251-3a3d-aa0c-67f090cc4ac1 | -1.5494 | -54.2957 | 2024-11-21 14:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ff254655-a692-3544-a5b1-8e381bed81a8 | -1.5494 | -54.2957 | 2024-11-21 14:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 25377b0f-308a-3df2-a159-6248b5e1f304 | -2.0259 | -54.5289 | 2024-11-21 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 7f35c3fa-23c7-3118-9a8f-99af78b5ae32 | -5.2353 | -42.625 | 2024-11-21 14:30:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 50dd4370-228b-3a30-bd26-64b6c72b2e27 | -5.529 | -43.3304 | 2024-11-21 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| eb625d5f-70db-313f-9fe8-0282679ebfef | -5.2351 | -42.6486 | 2024-11-21 14:30:00 | GOES-16 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cd958a71-e3b1-347b-a3ee-74e43929edf0 | -4.3692 | -43.314 | 2024-11-21 14:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 746df01e-f92f-3fed-bd45-649d949c85d6 | -3.237 | -42.0802 | 2024-11-21 14:30:00 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 51ea1704-110c-318b-a559-d99d1ccf4c6a | -2.0075 | -54.5292 | 2024-11-21 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| b4d28dc4-7e54-37d3-9a91-22ba0233f0af | -5.2464 | -43.5369 | 2024-11-21 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 3e2f9eba-b4db-3933-a437-e180ee60b7f0 | -4.0148 | -43.2408 | 2024-11-21 14:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 93.1 |
| c214a429-6789-3190-8e41-45e0ded28efb | -0.046 | -51.2325 | 2024-11-21 14:30:00 | GOES-16 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7a17c41c-84e7-3299-ba3a-0ac115ca94f3 | -5.6217 | -43.44 | 2024-11-21 14:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| d948d9d1-1aac-3afe-bb9a-05627e3e4985 | -3.39 | -44.9016 | 2024-11-21 14:30:00 | GOES-16 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| abf05f66-d12e-3117-9fa8-48139c218ee1 | -9.6609 | -44.4061 | 2024-11-21 14:30:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 88067d51-1328-3ea2-9676-cc6e9efcce89 | -3.2471 | -43.7184 | 2024-11-21 14:30:00 | GOES-16 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4950277f-4003-3294-9088-f754a5fd7549 | -5.5113 | -43.2151 | 2024-11-21 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3e63636a-e166-3c75-a2d3-f808ffd75e9d | -3.9539 | -44.0078 | 2024-11-21 14:30:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |


