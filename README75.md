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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0c2d823-99de-3b50-9f06-6116dfd125ed | -1.92312 | -52.12445 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa7fe71e-e75b-3eff-bf03-ea50a1a7a211 | -1.92235 | -52.12949 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c101d404-8689-375a-939e-87eb822cf1ac | -1.92158 | -52.13448 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ec16181-6a83-3fce-b637-e3fff098928e | -1.91972 | -52.05143 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 951aac81-1a80-3a30-912a-df691c82ef4f | -1.91893 | -52.05657 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ba9af0e7-de18-3248-9aa8-82025bd7b740 | -1.90607 | -52.32863 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55589e27-c6c1-3f57-acbd-183102b73cfa | -1.90141 | -52.3279 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b3b47a4-e744-3ac9-9358-8f601634a026 | -1.89598 | -52.33208 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33b6611d-60be-36b5-99ad-a15f71c4ef08 | -1.81954 | -52.2536 | 2024-10-28 05:21:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b4e7aff-a0c9-3ce6-aa33-86619347f22c | -1.55029 | -52.10685 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e18e7a05-d331-3292-91fa-260a8fcb3c0c | -1.54804 | -52.08477 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f809dc4-dc28-3725-af94-63371d089bb5 | -1.54726 | -52.08974 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62985f64-e078-30e5-a478-b1915c390cd3 | -1.54507 | -52.14156 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a17dd0ff-a001-3dcf-8906-99e5a2fb0ff2 | -1.54413 | -52.14003 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c6f5478-c67a-335f-bbc0-1b4283155e81 | -1.54385 | -52.08547 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be7a63fb-cac7-3a6a-b372-50795d4d06d7 | -1.54334 | -52.14497 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d127816-e2a7-3ce5-b1bb-5e064b773eb9 | -1.54332 | -52.08405 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 848a5748-6a91-3731-b738-8a3d37ae95a4 | -1.5431 | -52.09045 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c82b0138-ee74-3caf-976c-1f187a2c56fd | -1.54254 | -52.08902 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 419ceb46-680a-3603-805e-1e780fa0c683 | -1.53987 | -52.07975 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8bfe4ce8-54b5-31c8-a552-ebb1de65796d | -1.53962 | -52.14577 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e855e4f-736b-3907-8317-423f65326338 | -1.53938 | -52.07835 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32b8dc16-c2e7-3de1-bed4-c3217ac0b2ea | -1.53912 | -52.08474 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c80f209c-1f73-3422-87aa-9b6f78328da4 | -1.5386 | -52.08332 | 2024-10-28 05:21:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af9a35ed-331c-3f50-b436-0ee2800a2382 | -1.51223 | -52.57608 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb5e9061-e67c-35a9-b3fd-5ce0c12b1204 | -1.34343 | -52.51853 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2c3da24b-d122-3bbd-a99d-31d949266788 | -1.34271 | -52.52317 | 2024-10-28 05:21:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0436a49-375a-39a2-8951-4f75c12542c4 | -2.85653 | -53.33516 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 87b7ff02-0be2-3bb7-b95a-b7c658257376 | -2.85439 | -53.32821 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91c8c7cc-9093-30e4-830d-9008abc7feef | -2.85372 | -53.33252 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22b5fcdc-969d-30ab-b897-e237ad672cea | -2.85338 | -53.32588 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc6b41e4-3fc5-388e-b9a9-ae473a55c0b7 | -2.85274 | -53.33018 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d461a4d-de0b-32e6-bd6b-6325664ff57c | -2.85063 | -53.32324 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16a9f9da-4f5a-3c29-a896-e3865324ab88 | -2.84997 | -53.32754 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d31de953-bc9f-3dfc-8cf7-9ee165b9f2c6 | -2.8493 | -53.33184 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 608d2a78-c28d-3a32-a9c8-5e547efe94b6 | -2.84732 | -53.34462 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3032c874-15da-3470-8d15-422875bab76c | -2.84555 | -53.32686 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bbbdd767-f38d-32b5-9af9-5424e87908a7 | -2.84488 | -53.33116 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4ed12250-0f81-30ae-ab56-445255b632fa | -2.84356 | -53.33972 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9930d22-e998-3300-9f88-c8e928c89308 | -2.84291 | -53.34396 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d789890f-e545-3e2d-b63a-e5965ea16f59 | -2.84113 | -53.32619 | 2024-10-28 05:23:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32883f47-5f0c-3f54-8f1e-3b7f7972938a | -2.78475 | -52.90159 | 2024-10-28 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08a7d55d-23fd-3f8d-ac42-a0ccdabf898b | -2.84335 | -52.54951 | 2024-10-28 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb511cab-9cc0-3ab7-8ca1-6b03b4e62e4e | -3.88782 | -52.38263 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aab27a5-320a-3058-bf49-33cd298ecacd | -4.21385 | -53.45836 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f61aeefc-75f5-362d-b3ac-51ba11f238d8 | -4.20938 | -53.45771 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b330e813-3d44-3e33-a2a4-cf011bece902 | -4.20871 | -53.46213 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e42a852-b57b-3e38-af82-0b615ad2ed7c | -4.20805 | -53.46651 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc87ad3d-e826-3947-9ea7-d089b8a20b78 | -4.20491 | -53.45702 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10e3b01e-9045-3ae6-b073-e08bb16d5c5f | -4.20424 | -53.46148 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ef43b9-90fe-32e8-9768-6d91cf224761 | -4.20358 | -53.46587 | 2024-10-28 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| afd3543b-ffa1-38f9-bf57-568c858fd376 | -3.75467 | -53.4109 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9173ff1-4af1-3a4c-8458-6b4a69862601 | -3.75023 | -53.41015 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fb37f9f-671f-31ca-a16c-2dd9dc25d79a | -3.74196 | -53.40446 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92af37a1-33c1-3ce2-ac91-444c27bf8b0b | -3.68256 | -53.83385 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f11b131-da2e-376c-a705-196cefebfead | -3.66781 | -54.078 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f08956ad-165a-35d7-93a8-68630419bf32 | -3.63568 | -53.97182 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a751501e-7816-3a2a-a8c5-cb215e1c6322 | -3.60095 | -53.95546 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eabf3548-a0bc-3c06-b6a7-3284c14b3350 | -3.59652 | -53.78124 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1c453ee9-b996-3917-84ef-d46ecbd74b11 | -3.5922 | -53.78047 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f29bf3e-eb4f-307b-9377-b74f89555e0c | -3.5916 | -53.78449 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2e1549b9-09f5-343a-a815-c40bf304962c | -3.50746 | -54.03174 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d597a063-cd66-3cd9-b3e9-85e28c2a7152 | -3.50677 | -54.03035 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a71962b8-63f7-33d6-9bd3-b2062896f9ae | -3.45937 | -54.20329 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2b47bf7-4dfd-35ae-9d79-22c8af7a54e3 | -3.27477 | -54.14505 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4099987b-655a-3ec4-8768-3693c19b1de0 | -3.27444 | -54.14497 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9477a88b-c82d-3280-930d-a3de25921011 | -3.27058 | -54.14428 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ded704f9-be0a-3dda-922a-156dd89e004b | -3.27025 | -54.1442 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6883758-4653-3b11-9d95-74098e949e11 | -3.16796 | -53.914 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e0ef03a-03a6-3357-b6fa-472f82abebfe | -3.16736 | -53.91793 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 918d1365-05c3-39f6-9f35-4bca90598334 | -3.16371 | -53.91328 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c55936d5-0f79-35c3-bb04-ca12b917f796 | -3.1631 | -53.91726 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e0cbc3e-322a-3466-b85d-e19fb0314dce | -3.15945 | -53.91259 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be4d1308-12f7-30ab-9a5a-56c72c59e6df | -3.15885 | -53.91654 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3800db0c-9e46-30f0-9bfd-ca2aead2040c | -3.15518 | -53.91193 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aa57c31-9c46-3537-9b16-6c9311d2632c | -3.15459 | -53.91583 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6524eb99-e031-32ad-8fb8-2923254a1b4a | -3.15093 | -53.91117 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef35ccb2-75b3-39f4-9ca7-03844f4e2742 | -3.13489 | -54.26906 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce544dd2-f0b0-3d60-b8b3-a2b0e1a544f6 | -3.13429 | -54.27288 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5362e144-0ad0-32c7-8635-51b820a33352 | -3.1337 | -54.27669 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e1a2e09-b6b9-3a36-ab98-94e2181de59e | -3.13071 | -54.26848 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b2d183c-5f1b-3294-90b1-4c66edee5304 | -3.13012 | -54.27231 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0542e08b-d30b-379d-b43c-629601afbd74 | -3.12953 | -54.2761 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f660dab9-a69c-3c33-a5d8-7ced8bda2ced | -3.12895 | -54.27988 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f249f01d-954c-3635-8f5d-a3d5d03bfaf9 | -3.12654 | -54.2679 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f7cb70-84f4-34ec-b511-d6836f98cc3b | -3.12595 | -54.27172 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c2c1a4d-c149-3e7a-ba6c-860ac79586b1 | -3.12537 | -54.2755 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6fa2544b-a329-3c5c-8bea-f82e9b037423 | -3.12479 | -54.27926 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d72be51-f43b-3f87-9107-2f2b3dc8a369 | -3.11647 | -54.27802 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a4366d1-4f43-3918-a218-00ad1ddd5c3c | -3.11589 | -54.28176 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e483208a-3ecd-3df5-94ca-1fe08fca21c8 | -3.11532 | -54.28551 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 970c1277-dfe4-3c6b-b60b-df649e6293f0 | -3.11231 | -54.27739 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b84620e-a9f0-335e-927e-d12a0f7fc2f2 | -3.11173 | -54.28113 | 2024-10-28 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2664a8b5-2e22-3320-b741-9c4193f75df8 | -3.1034 | -53.7172 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5384bf1-7529-35a7-9bff-68c5616e704f | -3.10278 | -53.72127 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5a373f7-3d14-3f19-b553-bf8cffdcd557 | -3.09908 | -53.71656 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d0cad84-ae76-365f-8fef-61c98a11481f | -3.09846 | -53.72063 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab10646c-6bab-37d4-a572-02a70f64f337 | -3.09414 | -53.71998 | 2024-10-28 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ecf20b7-9b42-39b1-bc13-a371d2a519a9 | -3.07772 | -54.16747 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9395e7b7-07e0-3a9f-a25b-29c1d6abf42a | -3.07714 | -54.17135 | 2024-10-28 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README76.md)
