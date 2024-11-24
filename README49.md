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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c522fd5c-55c4-3899-b762-c7a563f2f655 | -3.68648 | -50.64627 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 400313d7-5296-3c2c-a241-a7c3d1690360 | -1.13643 | -51.67786 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 920a2b9c-1fce-3bf6-b123-3fc9c9da04f3 | -3.33106 | -53.79961 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69ff4ef3-9965-3ef6-ac77-955ae35458dc | -2.88169 | -53.95493 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e651f6b3-f1b1-3533-97be-60a15050bdf7 | -2.707 | -46.27074 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1beaf3f5-6753-30cd-807c-55a7f4184a2e | -3.68168 | -50.21811 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8050ede4-ff13-3582-bffb-a19f83b935a5 | -0.09736 | -51.75057 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e17e38a-466b-3fcd-9e51-4d761cf8f889 | -3.53092 | -50.75958 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e1206cb-b19f-38f2-8747-518819581b45 | -2.23617 | -53.66415 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e7d7196-1539-398e-92d0-5836fbe90236 | -0.81526 | -51.59953 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c9fe20a-f0b0-334a-a24e-86c66fb0b56d | -3.04209 | -49.45184 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 63f8fb76-74b5-39e2-9d5f-1edf24ada4f0 | -1.95058 | -49.5262 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8301f98c-5a30-3346-8138-cdad2fb15d62 | -1.02375 | -47.12152 | 2024-11-24 04:53:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 686d41c6-c8f4-3de3-8311-49f996250597 | -3.83894 | -44.04967 | 2024-11-24 04:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4417eb37-231e-3faf-b221-6565ed3ddd91 | 0.09738 | -51.03527 | 2024-11-24 04:53:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 059e4df3-f063-3e4c-9951-ee2fa86cd7be | -2.69372 | -46.27271 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c468d7c-c3fb-3372-ac6f-1bc6ef17c7ef | -3.18446 | -54.32971 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 673b4cce-f4b0-3d1a-b078-8b60c08736c8 | -2.45137 | -49.21741 | 2024-11-24 04:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cc9293b-b75f-3d8c-b09b-4eed74397c09 | -1.99296 | -53.2901 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48af3508-a1c0-305a-af54-b9d32839cd55 | -1.19643 | -51.96876 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4482cedf-9e1c-3739-a46e-00ca3b6b7a31 | -1.44673 | -52.45633 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 168fab8a-afd4-3c77-89bf-17f39640982a | -2.84676 | -53.99871 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9fb63a7-3db9-39d8-9e5a-ac4720cd1121 | -2.87813 | -53.99976 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e63dd84c-de89-31e8-9e8d-4ae32d50d3e0 | -2.80754 | -46.80495 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f626a048-fefb-36bc-aa0c-d3aac4dcb7f9 | -2.69312 | -46.27662 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2fdf2dee-3a84-306f-86d3-fe4ea22ad5df | -2.70474 | -46.28598 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1d69a50-3c0f-37b9-8bd1-1dc09fb4558a | -1.514 | -54.19006 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 2744dd1d-0cb0-38c0-8a6c-3a05baab68e1 | -3.95656 | -47.05688 | 2024-11-24 04:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea68ec6b-9a78-3ff5-a7c3-df3008348668 | -3.06112 | -53.22347 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af04d13c-27c8-3f86-ab19-8ad649aaed73 | -0.39587 | -51.45337 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca2ac91-d181-3a16-813f-419740755c0f | -1.43158 | -51.11511 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a78ee23f-01d1-37a2-8c1c-028645501488 | -2.22746 | -50.84979 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1d9bdd0-2fc9-3e12-ba40-92dae5741cd5 | -2.83355 | -54.01565 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7507aae-8e64-376e-9667-2a147a56ed01 | -2.04587 | -49.72617 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1e22d58-009a-30ed-8458-01cbf2ece170 | -2.2558 | -50.84336 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d14afba-73e0-3836-bb45-dcc4a0e48914 | -2.02291 | -51.1825 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1d6f235-5c89-3a5d-8d63-fb8c8a98f9aa | -3.07704 | -49.20048 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d390024c-75d9-3d0f-83dc-1daa3a00fd08 | -2.70518 | -46.28249 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73e39242-f08f-3f5a-b55f-a2e3d66970fa | -2.29071 | -49.20217 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b403bd6b-675b-3982-b832-bbfb16b41cd5 | -1.51112 | -54.18567 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3b1bae3e-b824-3ec6-b3cd-ba3d3c7d00b6 | -3.0678 | -53.22451 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51ba52dd-d42c-37f3-bd31-c2a8d083de46 | -3.21952 | -53.92749 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60b8a8d6-0a71-3963-a7ac-8fff96792ec5 | -2.20654 | -53.67028 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b6ae4f74-1d23-3fec-8755-623d723f9230 | -1.68463 | -48.46046 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78783004-d2fb-36fa-942e-a27aed65868b | -1.42373 | -53.38218 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cf77ff2-e27a-338f-867e-71c63d160329 | -2.97675 | -51.36979 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76074e5b-98a2-31ba-b2c0-fd9d5805da45 | -3.98453 | -44.79456 | 2024-11-24 04:53:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99aa4031-7da1-3671-b9ee-8a7d92d3afd0 | -1.29772 | -51.73147 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 8a1e3e66-f8cf-3d43-89c1-34a6d0f661f0 | -1.36774 | -52.15718 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d372498a-3f1c-3690-96a1-68eb10cc6cc1 | -3.25503 | -54.21365 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7486784-747c-3312-9b9c-8aee96ba22bd | -1.05378 | -53.65892 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef2a118a-c037-38b0-b053-447a6138822e | -2.07593 | -50.32086 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 024ac597-6980-3100-9d80-6908a6a28719 | -2.2838 | -53.62678 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9ec6bb7-ec98-38be-a687-d89f9e563850 | -1.194 | -51.76392 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 903e1d8d-2039-3607-8f42-6a2e16c9eb00 | -2.11346 | -45.89663 | 2024-11-24 04:53:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358c54d5-ebfa-3940-a7ba-a20de422a0cd | -3.25326 | -46.26167 | 2024-11-24 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7d23e18-ce29-3198-b407-7e68ff3f936a | -2.85076 | -53.99554 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9a95c67-4263-3372-8520-193b6cef359d | -3.15892 | -49.89873 | 2024-11-24 04:53:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9c4fba6-e342-3f0f-a32f-d93e6034e8d1 | -1.39461 | -51.59192 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 258f6fa2-0363-35b2-8463-fca856ec096e | -2.57568 | -54.04868 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5fee124d-d4e4-36c1-870c-f7662614b000 | -4.97793 | -49.81929 | 2024-11-24 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11356b4d-f367-3617-aa86-a962dd1d8a63 | -1.5829 | -53.82055 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 558c8a79-74a1-3698-af53-7be164b94efb | -0.28656 | -51.60833 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2414b5eb-d0a2-339a-bab6-e9594694dadd | -3.54199 | -50.53225 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dabda32-7318-3193-bcf3-7e3dc53e2483 | -2.22232 | -50.77707 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1715e659-066b-3940-9422-e8761279d951 | -3.33446 | -53.32709 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b8100f0-a902-3d23-abd1-eb392a410d21 | -2.21282 | -46.3879 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d6699f7-d695-3f39-9881-7ec45e0a3b13 | -2.13781 | -50.48855 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8706a959-acbc-3fcb-9bc8-22c8876ba7d1 | -3.96433 | -49.95513 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19ade50a-cc06-31cb-a774-cd282982a62b | -3.73459 | -51.08572 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 137947db-3ca4-30b2-bef6-0c2a622f1435 | -1.56384 | -51.29096 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 643780bb-9cf9-37f1-a77f-0e634bbae211 | -5.08878 | -49.63826 | 2024-11-24 04:53:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8df520e-ff80-3755-b471-70d733f5718b | -3.02313 | -54.05975 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96bacdfb-dbd1-3f81-a956-c57f8512ad58 | -2.59543 | -54.05533 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 70a7b409-e0f7-326f-8b60-3b759df14416 | -1.11852 | -53.40216 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af89f3bc-9d48-3114-b4a4-20781929a00f | -2.69532 | -51.36494 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35167ee0-4f83-31f7-9a58-ec3a0cd7c10e | -1.61939 | -55.13393 | 2024-11-24 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a699ba7-23d2-382d-a61b-6f5f53b248b5 | -0.19973 | -51.64001 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f12528-e62c-3092-a99d-7f644eb8c59e | -2.62299 | -51.80893 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4745bea-443a-3a77-a616-5462531dc14c | -3.83677 | -51.17344 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91cc8744-c316-3300-b78c-b035e19d5ca7 | -2.1992 | -49.55485 | 2024-11-24 04:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8fa5d35-4210-3183-97bc-4c3b0bfca977 | -1.95693 | -49.53107 | 2024-11-24 04:53:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3451cf76-e697-3faf-be8c-53e1fbd1d2fb | -4.2005 | -45.35841 | 2024-11-24 04:53:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc11b449-55d1-3674-9b8d-ed25707cf275 | -3.87693 | -52.36078 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fb4f639-7b6c-337c-b2c3-c5326aff2853 | -2.6259 | -54.93291 | 2024-11-24 04:53:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fd399fde-bab5-3797-b084-756a39ac61ee | -0.95487 | -52.27283 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 112c2fac-82e9-3dfa-9c48-cd5c1edb8171 | -2.31371 | -52.1751 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22782ef1-1394-32c0-8c59-6ec7949b1eb3 | -3.22818 | -53.00542 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 032cb535-a634-3edd-9092-b3b4c9698f65 | -5.22655 | -44.90601 | 2024-11-24 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53c588ab-a226-3ad6-a29d-c8ffa3c0a562 | -3.94716 | -46.89451 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d945b578-2d40-310b-b45f-9f0a02b11401 | -2.99143 | -46.91099 | 2024-11-24 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bd0be40-226d-35c5-b99d-ce436d913d47 | -1.30709 | -51.73642 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30c5439b-8175-3946-8176-5383eed26793 | -5.94985 | -48.05209 | 2024-11-24 04:53:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ebc0d6e2-3e70-3dad-a2bf-7d8d0fcdc035 | -1.61186 | -52.57425 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20b1be5d-ae7f-3dcf-802e-43712fc19aa6 | -2.80787 | -54.02267 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbee6d43-cf3c-3a24-9c96-758b9fadf129 | -2.73587 | -46.08425 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa5047d0-9be3-37f0-b8aa-cb03d6362c54 | -1.24287 | -53.39121 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af8041f6-94e9-3211-ad2c-6ea3d0ae6d69 | -2.69121 | -51.80536 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad3ec5dd-5588-3c5b-8f71-64faee57c43d | -2.85886 | -53.96651 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ced0b24-232a-3307-ad0f-b869a06413e5 | -3.95348 | -45.99568 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README50.md)
