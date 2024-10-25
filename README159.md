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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d9abdda-f5fa-38ca-90d3-3d959acc9a32 | -5.84425 | -38.41972 | 2024-10-25 16:52:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 451f9eae-abf9-3edb-9e64-860cb2eff82c | -5.84352 | -38.41988 | 2024-10-25 16:52:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 33449e8d-bb73-3274-a250-40b305a588e7 | -6.42026 | -38.41999 | 2024-10-25 16:52:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 33.9 |
| 3189c377-b826-379b-8ad4-695c7656dfc0 | -6.36579 | -38.63725 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 26.0 |
| b083117c-24c4-39a0-b0fc-5872ea115fa4 | -6.36486 | -38.63214 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 26.0 |
| a791a992-a299-3e0a-a7c5-e4ed471b8337 | -6.36403 | -38.5916 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 88f9c545-7535-34a2-9f64-a874e4cbc14e | -6.34846 | -38.57787 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 996030d0-bbf5-3c7e-8f71-a05bebb35a50 | -6.333 | -37.72057 | 2024-10-25 16:52:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3b17fa46-c4d8-3579-a1cb-4d874414eabe | -6.32335 | -38.54788 | 2024-10-25 16:52:00 | NOAA-21 | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 75c5c4c7-4140-3112-bc1f-ed57927becda | -6.32146 | -38.55111 | 2024-10-25 16:52:00 | NOAA-21 | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 34e9b839-4cb2-3158-8d24-e3b030f4a172 | -6.31555 | -38.62857 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 34d85bdd-7201-388d-93f7-28009e756087 | -6.31461 | -38.62327 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 20.2 |
| c5e97241-f8ee-388d-be24-35af28320497 | -6.31167 | -38.62653 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| f7976a4e-cb33-3dcd-b651-d5cb31af6e32 | -6.28003 | -38.46562 | 2024-10-25 16:52:00 | NOAA-21 | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6c38ca89-01cd-36dc-b3dd-530d38724b88 | -6.27578 | -38.46818 | 2024-10-25 16:52:00 | NOAA-21 | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 24ab75bf-445b-3078-8417-a70d62e3a67e | -6.24749 | -38.46791 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 13.2 |
| a98a0c9a-9796-3908-8e55-a99b0d95d38d | -6.15152 | -37.74714 | 2024-10-25 16:52:00 | NOAA-21 | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 7ee59a82-c60b-36b7-a4f6-3a4b3fd36374 | -6.15046 | -37.74125 | 2024-10-25 16:52:00 | NOAA-21 | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e93ccfee-6dd8-3806-bad2-baaf645bc23d | -6.14789 | -37.74508 | 2024-10-25 16:52:00 | NOAA-21 | ALMINO AFONSO | RIO GRANDE DO NORTE | Brasil | 2400604 | 24 | 33 | nan | nan | nan | Caatinga | 15.7 |
| a1f96b28-4f76-3628-b6d0-da137c54b7bb | -6.08808 | -38.36184 | 2024-10-25 16:52:00 | NOAA-21 | DOUTOR SEVERIANO | RIO GRANDE DO NORTE | Brasil | 2403202 | 24 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b5863e35-d226-36cf-af2d-5a9be2d47608 | -7.86286 | -38.46318 | 2024-10-25 16:52:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 99839f10-1c32-3034-8681-8386786be350 | -7.8166 | -38.76158 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| fc13ae35-cad1-3097-ab09-85b673cc4617 | -7.77234 | -38.39349 | 2024-10-25 16:52:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 043d8992-7bba-3f4c-b029-d6a19f277d70 | -7.77136 | -38.38836 | 2024-10-25 16:52:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 38.8 |
| d6871bc7-c035-33bc-b650-136b0a40924d | -7.76824 | -38.39266 | 2024-10-25 16:52:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 4e5d363d-9e37-3410-9de8-0e6bada0fc1c | -7.76595 | -38.5901 | 2024-10-25 16:52:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a8280b5e-c61b-35b3-868c-565c8f87eb38 | -7.76507 | -38.38936 | 2024-10-25 16:52:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 2b3ece6a-5c36-3f42-bbe6-1110add91e07 | -7.72335 | -37.85533 | 2024-10-25 16:52:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 19.0 |
| afe692f1-f2fb-3910-9f82-aadba3bdc762 | -7.66435 | -37.8269 | 2024-10-25 16:52:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 2bfc1337-c210-34f4-8836-c9dc4503929a | -7.6637 | -37.82363 | 2024-10-25 16:52:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 31.2 |
| e0b0717a-8b79-31a2-995a-e3ddbbe50402 | -7.66332 | -37.82132 | 2024-10-25 16:52:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 23.2 |
| b634c8e8-afd9-32d4-8b30-f0342265fd78 | -7.62273 | -38.77335 | 2024-10-25 16:52:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 13.9 |
| f0432933-75bc-3c58-a033-3bb6cb2b6cdd | -7.6224 | -38.77233 | 2024-10-25 16:52:00 | NOAA-21 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| ae3f5582-01d4-3acb-bac7-c8baab3eb71c | -7.49484 | -38.4612 | 2024-10-25 16:52:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 963767ab-d9e8-39d8-bfbd-b32e22f665e9 | -7.41914 | -37.62209 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 3c3cc7b4-807b-377e-a1ec-f8caf227a941 | -7.4174 | -37.62272 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA BRANCA | PARAÍBA | Brasil | 2500106 | 25 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 7e02417d-5337-38ec-99f4-d67ba46f96de | -7.18084 | -38.56302 | 2024-10-25 16:52:00 | NOAA-21 | MONTE HOREBE | PARAÍBA | Brasil | 2509602 | 25 | 33 | nan | nan | nan | Caatinga | 15.0 |
| cfe04f8b-db1e-32d6-bee0-9a474947f21a | -7.17884 | -38.56508 | 2024-10-25 16:52:00 | NOAA-21 | MONTE HOREBE | PARAÍBA | Brasil | 2509602 | 25 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 58e9713a-e0a3-3b92-95d7-7767bf7746a6 | -7.17607 | -38.37493 | 2024-10-25 16:52:00 | NOAA-21 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 2d3ec1ee-8b84-34d9-b202-1784a8871660 | -7.17504 | -38.36932 | 2024-10-25 16:52:00 | NOAA-21 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 36.5 |
| f878adc9-1eef-3914-9070-14ac97fcf63b | -7.17397 | -38.36352 | 2024-10-25 16:52:00 | NOAA-21 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 36.5 |
| e63eee64-184b-3b42-bcd2-e754badef1e1 | -7.07394 | -38.07868 | 2024-10-25 16:52:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 78fa0c27-9a29-3227-823f-611b9f38c2fc | -7.07297 | -38.07334 | 2024-10-25 16:52:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 678b944d-df16-3250-b8cb-5872a8c5462b | -7.04163 | -38.0113 | 2024-10-25 16:52:00 | NOAA-21 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 3.5 |
| aa37d387-e7c6-3dac-9ea8-d13dd8078906 | -7.00242 | -38.41956 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 014f9d3b-fb2c-3204-8a71-bbe38f6cf7f4 | -7.00151 | -38.41452 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1dbba046-0c36-358a-86e4-59d94a72344b | -6.9688 | -38.30717 | 2024-10-25 16:52:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 3400dae5-a08d-331d-875d-5da8c6a0e04c | -6.86371 | -38.74234 | 2024-10-25 16:52:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e0eb868b-85da-3895-b92b-79e59361fd41 | -6.74745 | -38.89595 | 2024-10-25 16:52:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 268014b5-b0a8-3109-b166-3ec4002b5f35 | -6.68975 | -37.59644 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 0396fb23-5c4a-3c6e-bb53-f0e77d50e4f7 | -6.68692 | -37.59914 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 271040f6-9848-3038-95eb-94d1b036468b | -6.68587 | -37.59332 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 8317afe2-5892-3e87-a19e-1b192e8a9e16 | -6.68308 | -37.59768 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 99916d5f-2786-329c-bac7-7e4eec7b92df | -6.68197 | -37.59178 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 79573865-001f-3dd2-8f72-d27a062b9409 | -6.67919 | -37.59456 | 2024-10-25 16:52:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 0f405a3d-43d1-3a6c-a36d-a39541009eb9 | -6.51937 | -38.56913 | 2024-10-25 16:52:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 17.3 |
| 5f1acc87-3356-39e9-8c7c-65038ded3074 | -6.51567 | -38.56895 | 2024-10-25 16:52:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 6af71e60-5b2b-31e9-ab9f-ba0544d2451b | -6.51304 | -38.57019 | 2024-10-25 16:52:00 | NOAA-21 | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f891a963-902f-370e-8702-79adeb116dc6 | -6.47642 | -38.65607 | 2024-10-25 16:52:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d735b25f-f403-3567-822d-abba6d060a1b | -6.47326 | -38.56685 | 2024-10-25 16:52:00 | NOAA-21 | BERNARDINO BATISTA | PARAÍBA | Brasil | 2502052 | 25 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 744b579a-4d5c-3090-98f6-1c3b33be7249 | -4.9894 | -39.84957 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4f291437-e82c-363e-985d-11eb7471ffbb | -4.92575 | -39.92519 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| c99a8fcb-3b27-383c-8049-501e751506d1 | -4.92501 | -39.92087 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| ce1d5f3a-62f8-3747-965d-1c5b08238cf5 | -4.92289 | -39.92626 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 17.9 |
| d4494768-28fb-3701-a2f6-d1290a8f7796 | -4.92212 | -39.92197 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ed6bd9d0-934b-372c-8afb-cf53ceb44791 | -4.91242 | -39.83296 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 667a6659-d7bf-38d9-b2e2-c39b13cb5ac6 | -4.9116 | -39.82834 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 50e0ea61-459f-3ea3-aaf1-f64379783a05 | -4.90995 | -39.83273 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 39.2 |
| d848c80e-3cc8-31b6-864a-2b19ea7e5cf5 | -4.90645 | -39.83413 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| f101cca3-b282-3e5c-a43c-591fed496ce5 | -4.89776 | -39.64547 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 72a61015-2823-3f10-b5e9-8254ca4f564d | -4.89736 | -39.64941 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 6f31811a-5682-37b3-b5c8-eadb416eb814 | -4.89655 | -39.64465 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 9c05caa1-5187-33c1-8a71-75a8a6135107 | -4.87026 | -39.52594 | 2024-10-25 16:52:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 35489f47-e1c9-396d-a122-2181531492a4 | -4.86986 | -39.52474 | 2024-10-25 16:52:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 26.7 |
| 4bfec2d2-a40a-3b1a-ae6a-920202a94afa | -4.78574 | -39.91469 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 0d637842-004a-34bd-bc7f-87dee8f4f9e7 | -4.78463 | -39.83644 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 931adffe-4ee9-3715-a7ea-92babac5a0e9 | -4.78416 | -39.90553 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f6309631-06b5-318e-bdaf-d10c5db1a78c | -4.78336 | -39.90085 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 346b80a2-2e0a-30fd-a2a4-72293d5fb241 | -4.77945 | -39.84228 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 8be1082b-c8d9-3178-86aa-f98e9f8f6df9 | -4.77864 | -39.83759 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 46.2 |
| b23ef03e-41a8-31a4-99e0-cce1ada23d93 | -4.77287 | -39.43944 | 2024-10-25 16:52:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 26ce8fd4-25bc-3aec-ae7d-280e68efbc96 | -4.76674 | -39.44065 | 2024-10-25 16:52:00 | NOAA-21 | MADALENA | CEARÁ | Brasil | 2307635 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f162da2b-f0d7-3842-9750-975e5411d8e3 | -4.74709 | -39.83414 | 2024-10-25 16:52:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 6a61acd0-7f18-3a9d-9459-ba521bc0b07c | -4.74245 | -39.91368 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 88dc626d-a835-3569-a182-a2765260d3b8 | -4.74162 | -39.90894 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 11.7 |
| e702de1d-a359-3b76-9a07-ebfce10d9d3f | -4.72268 | -39.8714 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 44.6 |
| 9522a630-cc7a-3da3-89d4-f9f12264c8a8 | -4.72109 | -39.87497 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 5bee1dbd-7e87-331d-a275-07e6700da28f | -4.72032 | -39.87043 | 2024-10-25 16:52:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 11a1e7bb-e480-3911-907d-09e1c66e5fbf | -4.65306 | -38.83537 | 2024-10-25 16:52:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| a17dadd4-8d71-3323-928b-bc3c387dc3ef | -4.60411 | -39.66499 | 2024-10-25 16:52:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 17.7 |
| 9c82fb6e-9a46-306b-8ed7-d78bc79dbf90 | -4.58338 | -39.58245 | 2024-10-25 16:52:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| e1fcbb13-d657-31cc-8a8a-ede4afb9c094 | -4.57818 | -39.48026 | 2024-10-25 16:52:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 2870c4d2-34db-3d13-a42a-36b2f2dddfe5 | -4.54017 | -39.47718 | 2024-10-25 16:52:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 29.5 |
| 91298924-3493-3312-b5d3-2d8d569c20a8 | -4.53971 | -39.47825 | 2024-10-25 16:52:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 3653550a-cf0e-370f-b2ce-6395b02e4480 | -4.48676 | -38.7296 | 2024-10-25 16:52:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 3c1950b5-b943-3645-adb6-50c5033a54a5 | -4.48669 | -38.7272 | 2024-10-25 16:52:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 21.4 |
| 3026c1ba-bfa7-3781-bfb1-60f2ec97a895 | -4.45059 | -39.47377 | 2024-10-25 16:52:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 4881a227-535f-3974-9929-19aa6d48c507 | -4.44971 | -39.46873 | 2024-10-25 16:52:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 47ef5a40-6fa5-32de-87cc-b5a5311dc6b9 | -4.15339 | -38.81142 | 2024-10-25 16:52:00 | NOAA-21 | PALMÁCIA | CEARÁ | Brasil | 2310100 | 23 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 875bc9de-019a-3ac3-8827-f4471648f3eb | -4.11581 | -39.79928 | 2024-10-25 16:52:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 65.9 |


[Clique aqui para ver as próximas entradas](README160.md)
