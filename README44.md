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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23019908-7235-38a9-aab4-6e07479c0b7d | -5.2613 | -46.21027 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de0cc9d8-e2c8-3084-8153-9c42aae2160e | -5.22772 | -46.02228 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d4ad5c9f-802e-3512-a789-2b6a6f73d3b1 | -5.22715 | -46.02589 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d5bea80-691d-3cf4-b60b-752b6be544b0 | -5.22492 | -46.01817 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee8b54ef-859b-33ef-842d-1be6edd8b6c9 | -5.22434 | -46.02176 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e945ead9-951e-3023-aad6-14273041bf1c | -5.22377 | -46.02534 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a491eb-22f8-3448-877a-5f21437a58e8 | -5.2232 | -46.02894 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b9dd28f-2a42-3b7f-96a9-afa28091ae39 | -5.22096 | -46.02123 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34fd3a72-88d2-3b7b-9d28-1399d393bc13 | -5.22039 | -46.02481 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e42553f7-8e5d-3ca5-a475-c354c47616d3 | -5.19316 | -46.06504 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 224bc064-7aa4-3a68-834e-486eb2b6e35a | -5.18977 | -46.06454 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32b76209-84d4-3f8b-ad35-019bb0286331 | -5.18695 | -46.16872 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14bbd951-47ea-31a6-8217-6a1b4b9f44d4 | -5.18159 | -46.11546 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ceac0100-1309-333d-bf35-55328bfd795d | -5.181 | -46.1191 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 445a44c4-5030-3059-8b14-efdf659f80bc | -5.1782 | -46.11495 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41f7604b-c461-3b0c-9a8f-8b2e6994aba5 | -5.17484 | -46.20072 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bfe43c1-ff90-3269-8f10-e3333c486607 | -5.1692 | -46.10608 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da37ee63-0d38-3fbd-8a11-54585d9c7e58 | -5.149 | -46.16662 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6a9461d-b22a-3e73-8361-6f76a5fabe9c | -5.14787 | -46.16681 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a6327b5-d0d1-3e8e-9cd9-18a995f5c3f3 | -5.14522 | -46.1176 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14c6e72c-92f7-30a3-97c6-983e9d667a43 | -5.14487 | -46.19219 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d28b25fd-ffcf-313e-b1f6-ed51f4037fa0 | -5.14464 | -46.12125 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4676c771-0f9f-3c4e-9523-b328ad759b1e | -5.1444 | -46.18872 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c8a3ca0-787e-3c4e-9db1-b72ec89a4f98 | -5.14382 | -46.1924 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81728d41-0389-3b4d-ac69-666315740e32 | -5.14182 | -46.11711 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d32fb8f-5727-3d4c-a95d-8a9a229758e0 | -5.13695 | -46.06026 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| eeea34e0-9231-36df-ad99-7057fbb23728 | -5.13414 | -46.05612 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4804923f-491b-3625-82c5-3e2ef725ddd5 | -5.07425 | -46.06179 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49fc014-394b-3d9f-8b04-8083bad3fe44 | -5.06456 | -46.07884 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63ea762e-4adc-3f8d-a1e3-72f40c144a8b | -5.06397 | -46.08252 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbc8f594-aa0a-351a-a8e3-5a71afd4a113 | -5.06118 | -46.07826 | 2024-10-14 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 440f9e74-9b40-391f-b60a-492c8996fb6d | -6.08916 | -45.46383 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cc4e7d9-e13a-32a8-9f91-8a4c5927d35b | -6.07539 | -45.99829 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49e919a9-d9dc-3cfd-a3db-72e2c074814c | -6.07203 | -45.99776 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1b0f93a-5e17-30ed-bac1-81bd4d674e80 | -6.00237 | -45.41066 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95688b2c-a796-3d43-94f3-1ac67a56b895 | -5.99905 | -45.41014 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 40caa77e-14ea-3cad-a7c6-7e1b068fd8d1 | -5.88053 | -45.5566 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e061ab9-2621-3767-9389-06204803f4f7 | -5.87997 | -45.56014 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c705180d-5d64-3dfd-88e6-8ff9a035d0ee | -5.83899 | -45.94214 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f538e70-6cfe-33a4-afa8-8aea01fb3009 | -5.83673 | -45.94196 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d76ebbf0-af33-37f0-a4d8-1c5e522a8cfb | -5.78308 | -46.5046 | 2024-10-14 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a710416f-819c-3e19-ba86-2d1770681129 | -5.70538 | -45.67291 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 328d03f3-69e0-3f9c-a783-a476b502f38b | -5.70482 | -45.67644 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38e8bb16-62bc-3553-9dc6-ffb7e88c3555 | -5.61795 | -46.37223 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2b351fd-d552-3609-81a3-5331f1f503b0 | -5.61736 | -46.37597 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f98c3d09-a55f-3ef8-b983-b45b06f689d6 | -5.61396 | -46.37538 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44db1b8a-3c62-3ae2-aa72-2d3d5a61ce20 | -5.61236 | -46.45105 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e6b4667-2bf5-36d8-99a4-f12993ebcd06 | -5.60894 | -46.4505 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a58daa8-2756-37b4-a266-9f01e63cde3d | -5.60715 | -46.37429 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e6780a3-65f1-3206-9470-53de546396e6 | -5.55647 | -45.75126 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec54144e-68e4-3c69-9f14-0bcc1fc7899e | -5.5485 | -46.36552 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e3b6694-fbd1-3fb6-9d14-6791be452c36 | -5.5266 | -45.95896 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe169ff7-8f6d-3814-8801-9da7065713b8 | -5.52382 | -45.95482 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53539a0e-ba9e-3f3c-ab93-a6c6bf1c8453 | -5.52324 | -45.95843 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1916bd7c-ab30-393f-9bed-0138ba1511bb | -5.52045 | -45.9543 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69a8bff5-5ac0-3108-ad96-f9d1c83b73c5 | -5.51987 | -45.9579 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dcce060-a207-31da-8e9d-7db82f4291ef | -5.49782 | -46.28948 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec3a5c6-6ecc-3640-b700-ee7b8486405e | -5.49588 | -46.23649 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0906bfc-9fd4-3154-b1b5-c7876585c0bd | -5.49414 | -45.84726 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fca995cc-0a4d-30ee-84c2-0db7f6d4857e | -5.49307 | -46.23233 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7676e2b9-0c8b-3e29-989c-967da90c76be | -5.49191 | -45.83964 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adcc4fbc-6315-3b31-8c64-2932b70f283a | -5.49134 | -45.84318 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17a3d13a-be18-3822-b947-92c2e2a8a14f | -5.49078 | -45.84673 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ead1238-7cb3-367e-89e0-5c023323e3b3 | -5.47627 | -45.82983 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3aac3331-55cb-3426-a535-dc0e230358bb | -5.47292 | -45.82927 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e7568a5-181d-3f9e-9e99-b5db1f74a267 | -5.45443 | -45.83734 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d1c3fdd-a8ec-33fc-943e-ad510cd5cf13 | -5.45273 | -46.30515 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a9a7f47-115a-3e2b-ad50-995e3a345f32 | -5.43832 | -46.42001 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1406b4c-115f-35f6-bea7-2216662c0530 | -5.43711 | -46.42748 | 2024-10-14 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3123cf8e-43fc-3b78-842e-744966b5a86f | -5.43576 | -45.88945 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d45ff1f1-7326-345f-8f14-c4ada510db7b | -5.4324 | -45.88894 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 006a9616-15fa-30b3-b0a6-96cfe54788e1 | -5.42409 | -46.24413 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e572cd9f-5b73-3652-805e-5a5e02e8a2d3 | -5.41502 | -45.88985 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45400ba0-b00a-3ad4-b4c2-8bb016d3eca4 | -5.41166 | -45.88932 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2abbc847-3195-33b9-a2bc-60ff8e301f6a | -5.4096 | -45.88851 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 727474ad-6462-3635-80eb-e7e70d0fb025 | -5.40903 | -45.89214 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a32e1dd2-8b50-373a-9615-833d8055d134 | -5.40396 | -45.9024 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ebf7fb9-6dfb-3d38-8796-92b9b48632a5 | -5.4034 | -45.90598 | 2024-10-14 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a914f5e2-aad1-36a0-80e8-6f0f20677be5 | -6.44106 | -45.8839 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bc87b11-0cbc-3e40-be99-31c6ff3b42ea | -6.39353 | -45.92382 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76008710-cbb1-37f0-9936-e7c5c4870ce8 | -6.39019 | -45.92329 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3511fab7-3769-35d7-8ebf-dfe7b293881a | -6.37461 | -45.72485 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 895c73b6-0dc6-3294-abbb-c7298d875af4 | -6.33707 | -45.8748 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| febf05ec-11ee-3f73-a3a1-3483acc89b09 | -6.27987 | -45.74276 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c1afe67a-b883-393b-9304-ab33545cbaa2 | -6.23391 | -46.45425 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66cd644f-e003-36f9-a644-2b8636f4653d | -6.23332 | -46.45793 | 2024-10-14 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42b2b0ad-a174-3b83-a7bd-30d2ea592263 | -6.00292 | -45.40718 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0890fe72-2905-3280-9157-372d1b3b1344 | -5.9996 | -45.40666 | 2024-10-14 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec5fac81-d538-3612-b9af-e1cb5b849f91 | -6.80326 | -46.47318 | 2024-10-14 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0586327c-16ab-3339-a3e6-43805b32a5bc | -6.67235 | -46.16639 | 2024-10-14 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c94460e9-ae6b-3772-a284-29ed5da39629 | -7.4244 | -46.69663 | 2024-10-14 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c34aed52-e9d2-3bd0-b40f-a8e4e46e7fa5 | -7.42208 | -45.58062 | 2024-10-14 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61166ef2-b34d-3ae7-9ede-145841413c5c | -7.41907 | -46.5568 | 2024-10-14 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 567162c7-72dc-36d4-adae-cb24fb073a6b | -7.41124 | -46.71347 | 2024-10-14 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba50f6b6-aab0-31e5-88ef-39d491ca245f | -7.3705 | -46.1169 | 2024-10-14 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb2a2c06-1ce7-3a9b-9d28-2e71c73d5bb4 | -7.36993 | -46.12045 | 2024-10-14 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c8d4107-94cb-3713-ac77-a5c2b0ea3e5f | -7.27973 | -45.70482 | 2024-10-14 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d3ce1a6-b95a-358b-add6-f217fbc43032 | -7.26006 | -46.31947 | 2024-10-14 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d998cc4-e46d-3e56-a0e4-14651dd90633 | -7.04174 | -46.08595 | 2024-10-14 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f39cfef-5543-38e1-8d56-e2219dc4fa83 | -6.97375 | -45.55178 | 2024-10-14 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README45.md)
