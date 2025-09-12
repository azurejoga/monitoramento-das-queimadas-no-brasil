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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74297c78-4a97-3b7a-a1d6-fcbc39330f89 | -11.9713 | -51.164 | 2025-09-12 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 2c7932f1-695b-3d50-b2c1-dfcaad71d9ea | -12.9101 | -54.7558 | 2025-09-12 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 10a9e9b7-6c90-3c2a-990c-0a6f88592405 | -11.9713 | -51.164 | 2025-09-12 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 81cb38e7-35ad-32f5-9c31-7bc7030388dc | -14.5132 | -53.8949 | 2025-09-12 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 316c5401-2204-3bde-a502-460553c4a41f | -14.5128 | -53.9158 | 2025-09-12 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| d837125e-9586-3f5f-98f5-8d3432a20a83 | -14.4939 | -53.8973 | 2025-09-12 08:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 424177aa-931f-3077-8de0-d1420a21c566 | -12.9292 | -54.7538 | 2025-09-12 08:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 567c8033-3552-3bb6-9267-a96c657925a9 | -14.394 | -52.9245 | 2025-09-12 08:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b284b6a7-d26d-31f5-97a6-bb23ef3d292e | -14.4133 | -52.9221 | 2025-09-12 08:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 49b99c9b-c40b-3585-b23d-5e015b47bca6 | -14.394 | -52.9245 | 2025-09-12 08:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 44.8 |
| b602fd80-e655-3e35-ac1e-a6b49cd7542c | -14.4133 | -52.9221 | 2025-09-12 08:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c0853dcc-33a8-325a-8721-e5571b6b2737 | -14.5132 | -53.8949 | 2025-09-12 08:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 12993fea-d14d-3aa4-8a62-514a8587a6cd | -12.9292 | -54.7538 | 2025-09-12 08:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| ecd53687-2703-3b9c-9de4-a4e515928083 | -11.7192 | -46.6257 | 2025-09-12 09:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 235d83ae-1c06-34e0-8804-b648e2c2cd7d | -11.7001 | -46.6284 | 2025-09-12 09:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e54efc62-5c82-3e8a-b893-0fe29b430a03 | -11.7005 | -46.6058 | 2025-09-12 09:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 47a00a2d-7b47-384b-afcd-a1d300964903 | -11.7196 | -46.6031 | 2025-09-12 09:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 70d7bd13-8814-305d-b1a7-55314800de5c | -16.3127 | -50.0868 | 2025-09-12 09:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 131.4 |
| b1f31986-f924-3896-8efc-6760a790a743 | -11.7005 | -46.6058 | 2025-09-12 09:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 27f193ec-6dcb-3267-873c-70b3462cc2f5 | -11.7196 | -46.6031 | 2025-09-12 09:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| b673b777-a997-33e8-ad2f-6e16066cb23f | -11.7001 | -46.6284 | 2025-09-12 09:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 364dd39c-e4a4-3cf0-b510-3979033e4d79 | -11.7001 | -46.6284 | 2025-09-12 09:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 160.0 |
| b6bca95e-e25e-3c54-b56f-af382094398a | -11.6997 | -46.651 | 2025-09-12 09:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 1720a139-ef39-31c7-85a3-844cfabb2571 | -11.7005 | -46.6058 | 2025-09-12 09:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 28d79dcb-66fa-3e27-9a4d-3935bb0da0e0 | -11.7005 | -46.6058 | 2025-09-12 09:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| d947a6a7-dbe6-31c5-bea4-326d5a52ecf4 | -11.7188 | -46.6483 | 2025-09-12 09:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 71002ccc-6610-3bca-82f1-8e3194df7cc1 | -11.7196 | -46.6031 | 2025-09-12 09:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 15c78348-00b1-3ee1-b0ee-4904dbec27c6 | -11.7192 | -46.6257 | 2025-09-12 09:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 166.6 |
| c9467d04-6517-3188-948c-fbf908b1c23b | -11.7001 | -46.6284 | 2025-09-12 09:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 6b2d78d0-9418-3153-8d3a-19f4f76ed9c0 | -11.6997 | -46.651 | 2025-09-12 09:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 1fbc2bea-5491-321c-9fa4-182cf1b5bafa | -11.7005 | -46.6058 | 2025-09-12 09:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 902b0b70-0249-33f3-80f9-86727c82f8e2 | -11.7001 | -46.6284 | 2025-09-12 09:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| fd26debf-d0b4-3dfd-940e-e589a9186824 | -11.7188 | -46.6483 | 2025-09-12 09:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| e28b9b76-22ee-337d-9f48-d2e8d62013aa | -11.7196 | -46.6031 | 2025-09-12 09:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 1186d2e4-59b4-3871-a190-8727cdae63c8 | -11.7192 | -46.6257 | 2025-09-12 09:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 6f603a51-6d6b-3c53-b5a9-c72f94a9f79b | -11.7001 | -46.6284 | 2025-09-12 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 148.0 |
| aa18f498-c812-3a3e-80a6-35098b287596 | -11.7188 | -46.6483 | 2025-09-12 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 256.9 |
| 635390d0-112e-3bef-bf9d-b5ca9ecddac5 | -11.7192 | -46.6257 | 2025-09-12 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 254.7 |
| a118e29c-9047-3439-9bb0-611c9ec0f446 | -11.7196 | -46.6031 | 2025-09-12 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 3fe5c46f-36c9-3c03-94af-9960e9993cb4 | -11.6997 | -46.651 | 2025-09-12 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 8b76dc1b-8f46-34ac-80dd-6cfd51dc7722 | -11.7005 | -46.6058 | 2025-09-12 10:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| df46171d-677b-3818-9db7-078f0d31dfb7 | -11.7192 | -46.6257 | 2025-09-12 10:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 262.9 |
| 4d8d0790-c85b-30ba-8ce3-9034fff55ee6 | -11.7001 | -46.6284 | 2025-09-12 10:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 313b4be2-92ac-3172-8b4f-544a4b515d26 | -16.3127 | -50.0868 | 2025-09-12 10:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 6c8070f4-bea4-3137-81dd-1bc4c8759be8 | -16.3623 | -51.4969 | 2025-09-12 10:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 2e59bfc2-6adf-3953-8e79-b9c3cd6a9205 | -11.7188 | -46.6483 | 2025-09-12 10:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 845e40f4-04e5-317b-a74b-b92b93b12ab0 | -11.7196 | -46.6031 | 2025-09-12 10:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 859097b0-43d9-3d59-a84b-c902e388c4eb | -11.7008 | -46.5832 | 2025-09-12 10:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f1b0a23d-f34a-3f73-9dfd-23ae77d54ca0 | -11.7192 | -46.6257 | 2025-09-12 10:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| d4aa229c-e9ad-3984-8d54-e7b96a17fc8e | -11.7005 | -46.6058 | 2025-09-12 10:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 9f5259b4-3ce4-3547-ac03-df37af996e24 | -16.3619 | -51.5186 | 2025-09-12 10:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 84d1410c-3be7-3292-9cb4-6c41fd7c5d32 | -16.3623 | -51.4969 | 2025-09-12 10:20:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 416.5 |
| 35cd0dfa-a71b-3d51-9893-9a8566af52d6 | -11.7188 | -46.6483 | 2025-09-12 10:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 216.7 |
| a5fcfe20-d06c-31b6-aec4-269123c16e3b | -16.3619 | -51.5186 | 2025-09-12 10:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 185.1 |
| f61cce04-a2de-3bfe-bfe3-d8245ab395fd | -11.7188 | -46.6483 | 2025-09-12 10:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 1806d1bc-623a-3beb-b4ea-fa8b084e2024 | -11.7192 | -46.6257 | 2025-09-12 10:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d0bf2cc5-9801-3865-8952-6b8f9ce9f282 | -16.3127 | -50.0868 | 2025-09-12 10:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b746eff0-37dd-3c91-8001-d974650cc305 | -16.3427 | -51.5 | 2025-09-12 10:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 8824769d-56cc-34d6-984d-01c005882138 | -16.3623 | -51.4969 | 2025-09-12 10:30:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 358.2 |
| a3dfce16-db23-3a9d-8348-4f0d1a059209 | -11.7188 | -46.6483 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 51577c8a-d540-3284-aaee-eaf88cc5794b | -11.7005 | -46.6058 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 6709df5b-b47c-3041-b197-0629d2cf6c4c | -10.679 | -48.6633 | 2025-09-12 10:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| fd50ef05-48eb-3c9f-a141-1f509a520d6d | -11.7196 | -46.6031 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0e5ae6b3-3e5a-3549-a08e-7951c9e58a3c | -11.72 | -46.5805 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| ef63264f-4474-3d02-87e1-c99942f62358 | -11.7012 | -46.5605 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 872f7f19-c870-3272-ab1e-7c5da7e0f742 | -16.3427 | -51.5 | 2025-09-12 10:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| ea38f620-684c-366b-9c6a-478562ff3116 | -11.7008 | -46.5832 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 83d066f2-2273-3103-b52e-42fb6cc2aaf8 | -16.3623 | -51.4969 | 2025-09-12 10:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 526.6 |
| d467223c-1520-30ae-bf52-9b70a156b0bc | -11.7192 | -46.6257 | 2025-09-12 10:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| a13377b5-5a51-38e3-a79d-056c9444e61b | -16.3619 | -51.5186 | 2025-09-12 10:40:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 289.5 |
| 8c45065d-f1fc-3e43-bd8d-8a4948e2b542 | -16.3619 | -51.5186 | 2025-09-12 10:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 257.6 |
| c5c76fc7-dbe4-3055-81d0-2e482961db9e | -10.0884 | -50.3862 | 2025-09-12 10:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 91d12ac0-1cb1-389e-a94b-eed76b300479 | -16.3623 | -51.4969 | 2025-09-12 10:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 459.3 |
| 79afe035-afc6-3bd7-8e7d-91e7dd07677f | -9.7197 | -46.8972 | 2025-09-12 10:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 72ce932f-1f1f-362d-88ae-5a82370b6b12 | -10.679 | -48.6633 | 2025-09-12 10:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 34cae530-dfc8-3ca6-856e-6962207294f3 | -10.679 | -48.6633 | 2025-09-12 11:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 4c535532-de23-3da0-9520-433c23966083 | -10.8785 | -45.5597 | 2025-09-12 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c7c67e55-bd3c-3c20-8647-a9ab5381e106 | -10.6979 | -48.6612 | 2025-09-12 11:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c40d78cd-80c9-3b88-9081-3fdc671defa8 | -11.7005 | -46.6058 | 2025-09-12 11:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 210.0 |
| ccff7ef5-2b2e-3cb7-8f6f-0431abeef30e | -11.7008 | -46.5832 | 2025-09-12 11:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f4d8c73f-b204-36c8-8abf-1004e73ecf81 | -15.9268 | -51.7785 | 2025-09-12 11:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6eb7b6c6-322b-3329-b3e2-75a71e2d3a28 | -9.057 | -47.0355 | 2025-09-12 11:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| c2fb6603-d794-3f4f-9c78-36374a33bddb | -15.1058 | -47.9983 | 2025-09-12 11:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a2f3e93e-42ef-3de6-97b8-2b82d2f6c67b | -15.9264 | -51.8001 | 2025-09-12 11:10:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 8fdf5965-bb1a-389d-8ebb-c8c265de085e | -10.679 | -48.6633 | 2025-09-12 11:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 387b6f02-9615-3ede-ab31-aba6effd5630 | -14.1907 | -46.2012 | 2025-09-12 11:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c296b475-e81b-3426-a231-3fd0f7d54dd2 | -15.2276 | -49.6672 | 2025-09-12 11:10:00 | GOES-19 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9bea3206-3d90-3556-95e6-29e316d26f1d | -16.3127 | -50.0868 | 2025-09-12 11:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e05689a9-36ea-3ff3-9a43-ddc3f0096157 | -16.293 | -50.0901 | 2025-09-12 11:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c3795d1a-d53a-3445-9e2a-cd145a6c79cf | -11.5422 | -50.6161 | 2025-09-12 11:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2a3dc402-cbac-3383-9f1e-4c184edd807b | -10.679 | -48.6633 | 2025-09-12 11:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| a2a97f57-5e1e-3300-9e10-753b243eff1d | -10.8785 | -45.5597 | 2025-09-12 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| cfa38503-46b0-31a5-b74e-9a1be42b0fad | -10.6979 | -48.6612 | 2025-09-12 11:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 1efe714b-d37d-3bde-82c5-de08316d6dd7 | -6.2123 | -42.5006 | 2025-09-12 11:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 7e069404-3266-3cdc-8913-359df575e385 | -10.679 | -48.6633 | 2025-09-12 11:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 1d5b7077-013d-3d2b-9c5f-d83c5cf9e1ed | -10.6979 | -48.6612 | 2025-09-12 11:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 995a6812-0390-3878-86dd-662b13abde05 | -9.057 | -47.0355 | 2025-09-12 11:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 4370c156-592b-39a8-a158-16d42f1bbcda | -15.9268 | -51.7785 | 2025-09-12 11:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| d256944e-85f5-36a0-85f9-dbae34142729 | -10.679 | -48.6633 | 2025-09-12 11:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| df5b65f3-3317-3936-aba7-deb94fe021bf | -6.2123 | -42.5006 | 2025-09-12 11:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 166.5 |


[Clique aqui para ver as próximas entradas](README121.md)
