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
| dfd688a3-96a9-3a11-9822-d4670e5ab660 | -3.92598 | -46.98855 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2cb114-24cd-30dc-a0bf-a4cabf5d6845 | -2.86956 | -51.80447 | 2024-12-28 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48c11017-3d1c-36cd-a757-1112104bccfc | -4.09802 | -46.80587 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f10b020c-30d3-3027-babc-f7f79d1d621f | -4.00744 | -46.71408 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1353a647-5b44-39ee-bb65-e74be5798509 | -4.01794 | -46.55334 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ff6c5b2-2c22-3efa-89f6-520ca6e4bdf1 | -2.12174 | -45.51544 | 2024-12-28 04:38:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6e35688-8adf-365f-b1bc-d35332e2cc55 | -2.57272 | -53.99158 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca0c199c-b8e4-31a5-b774-6a47ace36074 | -3.00311 | -51.73603 | 2024-12-28 04:38:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c37a7726-c9d4-3a3c-a077-aec086d82d29 | -3.89868 | -46.99297 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65e98003-cb62-3284-be41-f1aba4a73cea | -5.24518 | -41.39002 | 2024-12-28 04:38:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a15c9fe-6752-39d8-b594-21370b2c0bbb | -4.05759 | -47.112 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c450a68-14b1-3b8b-a843-e896d5b5dd28 | -4.72798 | -45.61805 | 2024-12-28 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a3a1fd9-3320-3984-b3cd-28a331eaa7b4 | -3.99987 | -46.71685 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89556fed-fe0c-3e7d-96f9-217f6689d630 | -3.96501 | -47.97878 | 2024-12-28 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 906cc317-a9bf-3574-b886-c9dd8cbfe8bf | -3.75727 | -47.22575 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dda0f265-6129-38a7-8ab0-f5d3f63acdaa | -3.72482 | -47.18685 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66c2ca40-40cf-3606-a4e1-31cda68a0500 | -2.77723 | -47.28916 | 2024-12-28 04:38:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dcfd7dd-7261-332e-bf44-c803df08e4a8 | -3.98821 | -46.72292 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d98edf1-1de8-3a5b-9d5c-94cf83b0eeb2 | -4.01502 | -46.71131 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97fb4a1e-4a57-3711-9c94-41cbd2290e7e | -2.62702 | -48.08756 | 2024-12-28 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6bb450c0-ec70-368c-959b-85002053cc6f | -3.74763 | -47.19791 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14a90500-7d93-376e-8cb4-c95712eb2bc3 | -3.91158 | -46.93337 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b05930-12b7-35b7-bdb4-c3a2bb0a3f6e | -6.00599 | -39.27443 | 2024-12-28 04:38:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 49fa2f1c-fa63-32c3-9aee-020e0f1c03e0 | -3.89121 | -46.99559 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5edcbd24-050a-3bff-9e41-bb1a53df750e | -3.81521 | -46.69811 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef461971-fd51-3300-9ca8-964547e7a996 | -2.57684 | -53.99224 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb00d115-22eb-3833-b0ef-47ca0a44f842 | -3.97681 | -46.88871 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce07ae26-85d8-3fc8-ad7e-8c66df95e137 | -2.07723 | -52.04643 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1a43d32-5bf0-3da5-8bde-fa30b680e6d2 | -3.8886 | -46.69287 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fefd2cb6-0544-39a3-bb44-ef42608c8829 | -4.12155 | -46.7232 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0ddd57f-3d6f-3ac5-8c9e-ec5141f82fbf | -1.45862 | -53.55515 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c1d7e5d-4e9e-3d2a-b5a7-1ccf6bbf2dec | -1.37128 | -46.61387 | 2024-12-28 04:38:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 657092bc-0a6d-306b-a805-cd8ee79e1ffd | -6.00546 | -39.2784 | 2024-12-28 04:38:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 557c1f1e-300a-3d88-8c97-78f4cd860302 | -3.81691 | -46.7101 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84525d5f-2d02-3b9f-8177-4f8f22e2de80 | -3.81333 | -46.73302 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71af23bd-d8e3-33b8-8448-6f23119194d8 | -4.08457 | -47.09719 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b5326da9-3ee5-3f99-8fdd-48ffe18e2d7b | -1.59238 | -54.13645 | 2024-12-28 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5e26d72-65b8-30ac-89b0-80fe4aec3e38 | -3.9093 | -46.92538 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2835361b-980b-3247-b882-6dc881c05769 | -6.44887 | -44.38387 | 2024-12-28 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5e47b9d-0d6d-3da0-af6d-e676bbe54048 | -2.84391 | -48.10673 | 2024-12-28 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06afeec8-166d-38c6-88a6-ea12e5bb0446 | -3.99107 | -46.75061 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4261657e-5033-3f45-ad8e-23d190ef260d | -6.01176 | -39.27523 | 2024-12-28 04:38:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| beeffa55-061b-3bd2-aa85-62251406ec8c | -3.84264 | -46.68261 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b322240-4041-323e-b7ea-18ef0bd7e6c0 | -3.75711 | -47.22529 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8a73be0-bccf-3d93-9fab-8eb386bfd89b | -3.78055 | -46.85196 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea4d9f7c-d69f-3919-b58a-050284b33367 | -4.09395 | -46.80912 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1884ae6f-f315-345b-a067-5a67ffb5d0f4 | -2.38596 | -51.91222 | 2024-12-28 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb4b716e-fea2-3e7f-b972-68d747505fbb | -1.35136 | -53.52365 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f29342fb-a4c3-3b1f-bae9-9af5f071ccac | -3.56109 | -40.85249 | 2024-12-28 04:38:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5bfa2447-d796-3f00-a687-9df2e612a8a6 | -2.21949 | -53.65103 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4dac6d8e-e1fc-3837-8adf-007f321bca8f | -3.75768 | -47.22163 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2317fd5-1c8e-3387-9ec3-73af518b75dc | -2.33672 | -45.82952 | 2024-12-28 04:38:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2267033-4381-35bf-9907-21a118f445a3 | -2.21484 | -53.65402 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e48f44a6-3ae5-383b-97ee-7517f6a5c965 | -2.11318 | -53.66765 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9488c7c-9761-3e3e-a817-1a6a90f878a3 | -5.09045 | -40.58311 | 2024-12-28 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 550da5f9-3cda-378f-98b8-123369dbb048 | -3.92022 | -46.98006 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca6a19c2-c07f-3f8b-a3ba-47ea4ae14aa9 | -3.90988 | -46.92164 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60f3b161-66eb-3bf5-ad91-1df1336469ed | -1.77553 | -45.84267 | 2024-12-28 04:38:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a1ac4f13-b32a-3366-94ce-b564a0f563b9 | -3.88772 | -47.01785 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbc4993f-729f-36aa-9502-19ca8f77dea3 | -5.1926 | -44.77179 | 2024-12-28 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3f53634-c240-3335-8aa0-a35cb5c491ef | -4.01382 | -46.71899 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81414795-2547-328f-a2bd-867cc84327c8 | -3.78236 | -46.61021 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 753c357a-b9be-35d5-86de-5bc5aa4ca668 | -3.759 | -47.21476 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8183ae0e-44e4-318d-b458-08aebb20b801 | -4.50453 | -44.22909 | 2024-12-28 04:38:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79fc1234-46be-33ae-93c5-db7110b04fed | -3.93403 | -46.98217 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a48ecfb-50df-39c0-88e3-58664b149ff4 | -3.87463 | -46.69079 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3f0f65d-119d-32de-b7b9-4a5c188b8ada | -3.99585 | -46.6966 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6880687-3125-3975-a2fe-648c387deda5 | -4.07886 | -47.0886 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| dc26cf66-2157-33b7-b67f-7d48120a834c | -3.88666 | -47.51327 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| acc612cd-ea33-3dbb-bd9f-f31758eefeb3 | -3.75824 | -47.21796 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aca8077d-0420-3790-b399-20c29f4bcbef | -2.48841 | -45.79715 | 2024-12-28 04:38:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 799903b4-27e3-3d8e-bfe4-6dd92cdf2f05 | -3.19058 | -46.00401 | 2024-12-28 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc225a69-cb1d-3c57-9463-3e1e9d014223 | -3.03652 | -53.91247 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3358e59c-0d38-3b9a-9531-6a2cf1514970 | -2.00233 | -45.58696 | 2024-12-28 04:38:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfee2c9a-7742-38fb-abd0-7e0618ab7e42 | -1.36843 | -46.60965 | 2024-12-28 04:38:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50b5a5d-568a-3b98-b0ee-e9424596c489 | -5.64519 | -43.71637 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a33b4f71-620c-3397-bacc-685b7f38b645 | -3.73167 | -47.18791 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ca8b6f-fcf5-3325-b8f9-35560f3eeb01 | -6.00505 | -39.27589 | 2024-12-28 04:38:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e98db1f3-da03-31ad-a4ee-22b9eac8b1b0 | -3.9231 | -46.9843 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bf0e4ad-1c37-372f-abbe-889e03c2e7f2 | -3.3805 | -46.22382 | 2024-12-28 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4aa3442-207e-3ce8-bf02-77ee6ab77df2 | -3.77826 | -46.84388 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a82d73a-d77c-3a4b-bc6d-8d5f0726f4ef | -3.8883 | -47.01413 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ec4aaff-53dc-3f31-a32f-ab595cb3b7ee | -2.21657 | -53.64341 | 2024-12-28 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f52cb105-9970-3e09-ade9-0851de36c88a | -3.89292 | -47.00723 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fe7f494-5ec5-35c5-b7a9-57fe751300eb | -4.74028 | -44.64515 | 2024-12-28 04:38:00 | NPP-375D | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09ea09d0-4d3a-31dd-bee9-b769179a5aa4 | -5.64039 | -43.7196 | 2024-12-28 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b959148-26fa-37b2-b86f-beca76c6d094 | -5.93404 | -45.56739 | 2024-12-28 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aabfbba5-f18e-313d-905b-34205a76efd7 | -3.54722 | -53.75996 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f736c596-9987-354d-9e8b-69cff46e90f8 | -4.01383 | -46.55669 | 2024-12-28 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53d6e59e-2f35-3830-abab-f4fb3df43f58 | -3.58896 | -53.71587 | 2024-12-28 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aca0609d-9238-3693-ad75-5a210249a900 | -3.77426 | -46.82391 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 166acaa0-cdb1-33c2-b85d-ab9ec25af414 | -3.89524 | -46.99242 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17d60fb3-6a9b-370b-9b43-9e3ff92c4bb0 | -3.92425 | -46.97681 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72df821d-04dd-3901-8689-358c8d80a411 | -6.11772 | -43.9515 | 2024-12-28 04:38:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| edd54218-52db-36ca-8629-25852ada1384 | -3.92943 | -46.98907 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8705d83d-fda6-3c65-8542-a785dd370996 | -4.08114 | -47.09661 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a534a8b-4cb5-3217-a31b-4a7159e116c5 | -3.73566 | -47.18476 | 2024-12-28 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b18a16a-e391-3719-885d-3c1eca918f65 | -3.88732 | -46.95269 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f633478-2ac3-30ae-8fb1-a210e1d660e9 | -3.84232 | -47.03751 | 2024-12-28 04:38:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b310e034-02d2-33e4-b116-0d5589aee804 | -3.91274 | -46.93649 | 2024-12-28 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
