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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90b05d87-9057-3e0c-a2f6-21b822cd5786 | -6.9158 | -43.5185 | 2024-12-13 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 419.8 |
| c5cbf47a-d1ab-38a5-aecb-2981a2057f3e | -1.62 | -46.6747 | 2024-12-13 01:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 80fa29c6-d0f1-3b2e-9063-919048b4aad1 | -2.8196 | -53.0832 | 2024-12-13 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ae1d3e64-810c-3ede-bdf1-b1ab5d98c848 | -1.6385 | -46.6743 | 2024-12-13 01:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| d606b679-ac3d-3f14-a092-99e71e9fff57 | -11.1959 | -53.8348 | 2024-12-13 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 12db38c5-402b-369d-9832-5e9118977754 | -13.0453 | -52.0349 | 2024-12-13 01:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ef7c0ab1-7b5c-3c4b-8f97-1182a1a2a29d | -11.2148 | -53.833 | 2024-12-13 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 4980bf42-3c68-3b23-b5c8-59bf385e67fc | -5.211 | -43.2833 | 2024-12-13 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 35252a14-b2d8-309f-bf79-93b9c0d3db7c | -3.3301 | -45.7146 | 2024-12-13 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 9ce12862-afda-364d-8e42-d6f4d02d871c | -3.2686 | -46.9142 | 2024-12-13 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 74812846-ebb1-3916-a80e-cae6e9de8994 | -6.9344 | -43.5401 | 2024-12-13 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0054fe96-8f46-39d2-bee1-f65a0a7122a4 | -3.3302 | -45.6922 | 2024-12-13 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| f8cdc60f-8e9b-3ded-8287-7d6366261d2c | -14.7655 | -52.6446 | 2024-12-13 01:20:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ad7b07e1-b035-379b-b873-8dd488dc2e8d | -3.3115 | -45.7153 | 2024-12-13 01:20:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 2295f5e2-f663-32ba-92c1-daf371209072 | -11.1962 | -53.8142 | 2024-12-13 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| d5a3c0c9-b065-3468-9692-54f117f2fbc0 | -0.7486 | -47.7569 | 2024-12-13 01:20:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1bc90cff-8248-38c9-b02e-4f3cb0c1cf6a | -11.2151 | -53.8125 | 2024-12-13 01:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 31beed93-d879-34eb-be70-13373f12b989 | -2.4923 | -51.8027 | 2024-12-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 185.9 |
| f6fc4ee3-6a8f-375c-9126-a9b00613ee16 | -2.7464 | -52.963 | 2024-12-13 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| f1ce4936-f45b-301e-a7c3-4b6c7f24098e | -1.9892 | -54.5095 | 2024-12-13 01:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3cbd88c4-1571-3ed5-ab86-390339796a56 | -3.2685 | -46.9362 | 2024-12-13 01:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| faf5972f-93b7-3c1e-a7a5-abf2f43fd33c | -2.8196 | -53.0629 | 2024-12-13 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4055d1b7-c39c-3d1d-93a2-01080bfee828 | -6.9349 | -43.4934 | 2024-12-13 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 1b191bf7-be43-3981-9fb6-a088fd88fda7 | -6.9346 | -43.5168 | 2024-12-13 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 338.3 |
| e17859a8-9780-33e2-9187-d0f0d37a3cfe | -13.0836 | -52.0304 | 2024-12-13 01:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9191b321-462b-3cb3-b871-d088c4bd83cc | -2.0076 | -54.5092 | 2024-12-13 01:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7b78906b-0c8c-3feb-b234-a29016189905 | -6.9156 | -43.5418 | 2024-12-13 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| e31ccd1b-4a73-3f1e-8c05-fb314667ebbf | -6.9161 | -43.4952 | 2024-12-13 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 0be7cf1d-9842-33b0-9c0d-e64993d87721 | -13.0641 | -52.0538 | 2024-12-13 01:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| cf8b87a3-4359-39bd-8eee-ea8c6c7af857 | -13.0644 | -52.0326 | 2024-12-13 01:20:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 125.1 |
| a6da5628-2027-32c8-ba4d-0272acbea778 | -2.5108 | -51.8023 | 2024-12-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 35d2fd9c-5730-383b-b0f6-4c179115b76a | -5.2298 | -43.282 | 2024-12-13 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 649b15e9-e650-3b8f-9f8b-073711bc2f02 | -2.4923 | -51.8233 | 2024-12-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 97aabb4c-829b-3c80-b2c4-d6aedcc3909b | -5.2108 | -43.3067 | 2024-12-13 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| bbcb4b9f-670d-3550-bfd0-ca2be23f1569 | -2.4924 | -51.7821 | 2024-12-13 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2e3b8945-85e0-3f35-9d80-c29cb4e18e06 | -3.3301 | -45.7146 | 2024-12-13 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 05ea76b9-02d5-3ba7-8462-3f1518697bbd | -3.3302 | -45.6922 | 2024-12-13 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 775e49aa-b0f2-3a69-9549-62a1034e0f19 | -2.7464 | -52.963 | 2024-12-13 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4bb5ac3a-85a6-359c-a2cf-af7d0fa00f70 | -2.5108 | -51.7817 | 2024-12-13 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 946f1676-69a0-3a58-8e7f-d2667d9a39a8 | -1.6385 | -46.6743 | 2024-12-13 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 5f37d14a-2f16-38d3-9875-143b32fc01f3 | -6.9156 | -43.5418 | 2024-12-13 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 2c908a4e-f7de-3391-8246-9cf188d47a87 | -11.2148 | -53.833 | 2024-12-13 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 714f246c-3376-3a62-bb72-d3ba065c7d6e | -2.4923 | -51.8027 | 2024-12-13 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| f22f31b8-6886-38ab-b4f4-9e5401d53ec6 | -2.8196 | -53.0629 | 2024-12-13 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 44997560-08f2-3d8b-8c0c-9433eb3fdc14 | -5.2296 | -43.3054 | 2024-12-13 01:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 2b5225dc-6385-3d6e-9fd6-e7382c29e4fc | -5.2108 | -43.3067 | 2024-12-13 01:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 2ff0ab1b-7c07-386c-ad37-54e34d1b3c48 | -0.7486 | -47.7569 | 2024-12-13 01:30:00 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c6fc5041-6aed-38fc-a73b-9c8bb117b273 | -11.2151 | -53.8125 | 2024-12-13 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 41ae3b98-3f0c-3bf3-b142-67dad8477bc7 | -5.211 | -43.2833 | 2024-12-13 01:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| e1f54b1d-1c4b-31c2-9cf9-e8323fb27c55 | -6.9161 | -43.4952 | 2024-12-13 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 124.4 |
| ac0c0c11-3ac2-334d-9ba5-667a5f28ea8e | -14.7848 | -52.642 | 2024-12-13 01:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| a2d6dbdc-7be4-3030-90cc-21ee06bc42be | -2.4923 | -51.8233 | 2024-12-13 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3d452d2b-2dd3-3897-98e9-247908064702 | -3.2872 | -46.9135 | 2024-12-13 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| d757dd55-56a0-3ee4-9e33-f4c3bfdc1616 | -6.9158 | -43.5185 | 2024-12-13 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 380.4 |
| c114f33b-9933-358e-9e06-b6a9387199ac | -2.8196 | -53.0832 | 2024-12-13 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 79200056-a738-311a-b54b-a1a190f7bbaa | -3.2686 | -46.9142 | 2024-12-13 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 0178ff9a-958c-3553-b169-cf65e66cb74c | -13.0641 | -52.0538 | 2024-12-13 01:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 286c78b4-239d-3756-a097-0989101eded6 | -13.0836 | -52.0304 | 2024-12-13 01:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c0b1a0b3-2c6f-3d61-9d60-d8ca728f478f | -3.3116 | -45.6929 | 2024-12-13 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| aab89eff-43a6-34ba-ae34-32aae26ef731 | -3.2685 | -46.9362 | 2024-12-13 01:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b43343a4-06bd-3cbe-aa31-9fd05d6460ec | -6.9346 | -43.5168 | 2024-12-13 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 354.5 |
| 4e6c87a4-1288-3093-a0a9-652f290ed50b | -6.9349 | -43.4934 | 2024-12-13 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 135.7 |
| f84c2ba1-619a-3f6d-8476-ffe0e6bdcd60 | -1.62 | -46.6747 | 2024-12-13 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 368abab3-8c0b-30b9-8534-cc4ec5330d86 | -6.9344 | -43.5401 | 2024-12-13 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 3674eb89-8396-368b-9be8-022e62c3ce6c | -11.1962 | -53.8142 | 2024-12-13 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| dd9ee4cb-41da-369b-8e5f-fde49008660f | -2.0076 | -54.5092 | 2024-12-13 01:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e8ce9bf4-0f4c-341f-ba47-c5e07d5990bf | -13.0644 | -52.0326 | 2024-12-13 01:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| dcfe66fc-dc6a-31ec-b618-13996ecfe00b | -11.1959 | -53.8348 | 2024-12-13 01:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| e03bf272-ec18-33db-9e10-220b78d4deea | -1.62 | -46.6526 | 2024-12-13 01:30:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 88fb8269-47d0-3488-ab45-1384a9df8c92 | -2.5108 | -51.8023 | 2024-12-13 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| d7450d2c-2d61-382e-9e0e-7ab7b6e31ab9 | -14.7655 | -52.6446 | 2024-12-13 01:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| f5ff52be-fb54-35fa-bac8-da36a0eed261 | -3.3115 | -45.7153 | 2024-12-13 01:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| b0eb3780-9d37-371f-8f76-f2062c659c87 | -6.9156 | -43.5418 | 2024-12-13 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 187.5 |
| d92a7792-a104-3bc6-963f-cf77cc5720b2 | -2.4923 | -51.8233 | 2024-12-13 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| d684f8dc-a6ff-3afc-ad07-70b7f4907fab | -13.0836 | -52.0304 | 2024-12-13 01:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 82537dff-36d6-31e6-a218-b98bcd0e6a12 | -6.9344 | -43.5401 | 2024-12-13 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| d453b6fa-ad10-3d86-9b41-ccd9bd9c25bf | -6.9161 | -43.4952 | 2024-12-13 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 8ae3c717-8d4b-36db-9cac-deb0e11cf4be | -11.2151 | -53.8125 | 2024-12-13 01:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0d21f8a8-84a4-3b13-aaa6-eb0aeca4f57d | -11.2148 | -53.833 | 2024-12-13 01:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a984fdd2-0077-33ed-8a5c-caa12fac4c35 | -3.2686 | -46.9142 | 2024-12-13 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b6a89514-28c0-343e-9838-5a0a2289d1a9 | -14.7848 | -52.642 | 2024-12-13 01:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 4b95a8d8-87ee-3bb9-a204-efb963439f7c | -3.3302 | -45.6922 | 2024-12-13 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 9b7f2c30-a8b4-366e-b704-35f1ce601ee9 | -3.3301 | -45.7146 | 2024-12-13 01:40:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| d2a6275d-7e53-3465-b3bf-34db5716ea21 | -11.1959 | -53.8348 | 2024-12-13 01:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 18cdec04-eef4-3d75-8188-178abb22c9af | -5.2298 | -43.282 | 2024-12-13 01:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6a34e913-5ad4-3af4-8365-f8c376fbb89b | -2.5108 | -51.8023 | 2024-12-13 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| aa51920f-a934-34f0-b345-696d3ae91530 | -1.6385 | -46.6743 | 2024-12-13 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 93df5e9d-f656-3b0e-96ae-a4cde3086554 | -14.7655 | -52.6446 | 2024-12-13 01:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 234d512b-a206-371a-a5b7-7bd84b30521a | -2.8196 | -53.0832 | 2024-12-13 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3994ac44-005f-3737-9eea-d2fe6f8c63ba | -3.2685 | -46.9362 | 2024-12-13 01:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 8ff2d6a9-c77a-3ec7-8a9e-046bfad7a6e7 | -5.2296 | -43.3054 | 2024-12-13 01:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| a83fa0b2-52a7-3c74-a87f-b09629e8d12c | -2.8196 | -53.0629 | 2024-12-13 01:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f0d56f01-c12a-3475-9a07-565b261b3dfb | -5.2108 | -43.3067 | 2024-12-13 01:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| fc30fdb6-7709-34c0-8d6f-b01dd9b7c784 | -13.0641 | -52.0538 | 2024-12-13 01:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a47b3a66-ec37-3416-8cc7-aad002d75619 | -1.62 | -46.6747 | 2024-12-13 01:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 14682215-cbf5-38e9-8d34-14b718b798f3 | -13.0644 | -52.0326 | 2024-12-13 01:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 7406c2f6-abe6-3051-a712-8d1a50ad7c6e | -5.211 | -43.2833 | 2024-12-13 01:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 40a44a03-9a5a-3d24-8bcc-548f55f86ae2 | -6.9158 | -43.5185 | 2024-12-13 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 401.8 |
| 995d9dc7-897c-326d-8992-08f3fa9b19d8 | -6.9349 | -43.4934 | 2024-12-13 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| ad86d41b-ee4e-3f71-887f-ec9d88bb2460 | -2.4923 | -51.8027 | 2024-12-13 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |


[Clique aqui para ver as próximas entradas](README7.md)
