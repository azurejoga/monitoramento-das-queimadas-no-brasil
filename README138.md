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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76914213-298f-3070-9cad-6422854ffe55 | -3.70639 | -58.54839 | 2024-10-12 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ce74d11-bfb6-3530-ace4-1437c33bd536 | -3.66795 | -58.80862 | 2024-10-12 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a8f15b2-7b54-3502-9d14-c4c03d930757 | -3.53461 | -59.39372 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 985d00f4-b549-3e08-8b9d-ace95d8597dd | -3.53418 | -59.39076 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c14cfa13-8346-3719-b6e9-9fb0164128af | -3.47982 | -59.50431 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce36e484-77be-301b-93c4-f4a92e3ee36d | -3.4753 | -59.50367 | 2024-10-12 05:46:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec98fe7c-42a6-3b35-a37b-006f483aec37 | -3.2179 | -58.93855 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5383df6-e417-3745-aa28-889922e56e6f | -3.21248 | -58.94282 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1ea88c7-1159-37ed-a59a-7b245335472b | -3.09461 | -59.38165 | 2024-10-12 05:46:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52371653-cc1c-3d9b-b759-b50a91762025 | -3.05142 | -59.36111 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbf86342-757a-33e9-9616-4d80ce75ada4 | -3.0469 | -59.36038 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ca1ba38-466e-3c63-888b-50e265954d56 | -2.87577 | -59.18829 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bf2d41c-1e27-3b8e-ae33-e262785b54ee | -4.55756 | -59.57021 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6798cfa-ae26-337a-9ef2-aa8100c112e2 | -3.9301 | -59.12274 | 2024-10-12 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f0f3fb0b-7a4e-3139-a8b1-34432083a17e | -3.90376 | -58.63554 | 2024-10-12 05:46:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef648be8-57b7-35d0-9c73-b75f072590f2 | -3.72718 | -58.47489 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beb6953d-30ac-34c7-b858-bf877f958b47 | -3.7223 | -58.47425 | 2024-10-12 05:46:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44ec944e-b322-33ea-851c-66fcf60b92ed | -3.63525 | -59.09365 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e9f6bfe-71cc-37ec-b1dd-f067e8aa1e36 | -4.2686 | -59.99964 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee197235-5655-335b-936b-ec5816c3eee3 | -4.26483 | -59.99468 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3bb6eecc-0da2-318d-92fc-084bc94b111b | -4.26418 | -59.99902 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c61327b6-72fa-307b-b05e-2dade19c7374 | -4.25976 | -59.99838 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ec2ccba-1d15-3341-bf00-17624ca4fc16 | -4.25664 | -59.98903 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b132f58-88ac-3c7f-a9fa-b1929f632bb2 | -4.25599 | -59.9934 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83ec4b66-c011-315b-a50c-8243303ec94f | -4.23649 | -59.94167 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 705241e6-ae1b-3e63-9f92-37fe7060269e | -4.23209 | -59.85809 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e998e646-a9c3-3a96-ace8-54d2fed36ddb | -4.21738 | -59.95413 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccc13726-355e-3ac2-9646-70527d1c1be5 | -4.21672 | -59.95843 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf543f8f-bc89-3f4b-bf69-6f60eaf27292 | -4.21622 | -59.95654 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f0f79691-00fd-3ee4-b356-a3147c8c6725 | -3.89321 | -59.68576 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8527b21-dd97-3749-899e-077eb1314502 | -3.89254 | -59.69019 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc55de0e-e350-32e3-9fdc-45cab7fd1287 | -3.87174 | -59.73724 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0533a97-8fcf-34f0-ae18-e863390c7a0d | -3.86727 | -59.73658 | 2024-10-12 05:46:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81060f5d-9d25-31f3-ac17-a1efb310fd05 | -5.57362 | -60.17335 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd7d6f41-cef3-3ae8-8dab-c0ebb014f4d7 | -5.57266 | -60.17182 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1536d2a-6969-354c-bf93-b8e2d444a421 | -5.56917 | -60.1727 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 803347ee-01e7-3100-9f6a-89f2c862f867 | -5.36524 | -60.09355 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a3ec1f5-955b-3960-9cc6-0ca31f57eda7 | -5.36458 | -60.09795 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 427a356b-8ed1-3540-8028-d7637d07d9f5 | -5.33392 | -60.1205 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7223cd5a-8dbb-3475-92a8-bdf6d757b417 | -5.33327 | -60.12489 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 903f3268-c773-3dcf-820e-0639211aa898 | -5.33262 | -60.12929 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c201a8a-9511-3e73-9020-511f12776108 | -5.33197 | -60.13369 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd2da01d-e2e0-34f9-8373-5d49719c7b07 | -5.33132 | -60.13808 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fa58960-db35-31df-a7c3-bb827bf507eb | -5.33068 | -60.14244 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef19f8d4-0d53-33ed-90db-bfe1ec523c26 | -5.32882 | -60.12424 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432627ed-bc43-3ac1-8bcf-8b8af8c69316 | -5.32688 | -60.13742 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6493974e-1af6-37d4-bc0f-41ad6ccfc41b | -5.32624 | -60.14179 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe16321-0f59-3496-90d8-e5ad87e92124 | -5.29386 | -60.20822 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 66d3c0a1-4293-33d4-acf3-b03857831c94 | -5.28944 | -60.20757 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d1d8d2fe-6fde-327f-991d-56517b75da6a | -5.28882 | -60.21186 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2a822959-5995-3c85-8d4c-70df2b6f087e | -5.19646 | -60.07534 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cbb8d93-c19a-3d31-9588-347d8362c614 | -5.1831 | -60.13614 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4fd81210-96f4-37f4-b24c-e2e2ec65f256 | -5.18247 | -60.14052 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8caca89-9fce-30ba-a02d-61eb8609e298 | -5.17867 | -60.13549 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 566f90fe-a999-3ffb-80b5-a497ac1c26cd | -5.17803 | -60.13987 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f1d211-48a0-3867-be2e-4e8eee39a90c | -5.1736 | -60.13921 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5a5fdaa-07f6-3155-9cc0-cb1c57dbb521 | -6.38559 | -59.97937 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0533a757-8093-323f-9d7b-0cd2caa008af | -7.40039 | -59.71257 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f624e470-c755-34d5-b714-53aed485444a | -7.39968 | -59.71766 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cfe6f0b2-d946-3aa6-8c04-7ba446abf18e | -7.39897 | -59.72276 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd619b06-815b-3264-b4df-f38e0a4ace31 | -7.39495 | -59.71701 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b950bc1-52ec-374c-89db-420d14bb92be | -7.39425 | -59.7221 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 177800ac-99a2-328a-8ee5-b0bde4cf7f74 | -7.38953 | -59.72138 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85a4b0b5-f64e-36ab-a44b-35171de0b156 | -7.18299 | -59.76454 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c916359-84b7-317c-a7e6-0a2582a68678 | -7.11187 | -59.77655 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb67e132-7e87-3277-be0d-78ddb66ad8d7 | -7.1079 | -59.77092 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8969828b-ba82-3af9-b518-ca335d4ac37e | -6.92381 | -59.7867 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d164e7c-dc9e-38b1-85ec-23d0187b2b79 | -6.92233 | -59.78429 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55f66ac7-347d-3f45-bbd5-fa388643f55d | -6.92164 | -59.7893 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e6f07a9-4e89-308a-b228-395a92df30cb | -6.91912 | -59.7862 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1388ddf6-3222-3c59-bb6d-1c4cb55bc566 | -6.82311 | -60.12663 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d506839-b4a5-3906-a4e2-878608d4aef2 | -6.81336 | -60.12989 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 140d0e2b-9d95-35be-a333-4a27ce8c7f28 | -6.81271 | -60.13445 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3669ab35-a3be-3c3a-94d0-c4fb7080da42 | -6.80881 | -60.12924 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 09a27ed3-200d-389f-9461-e40e511cbc70 | -6.80816 | -60.13377 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 037d6ce2-a6bf-3720-a041-01ee87d0590c | -6.80237 | -60.10906 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7c1c43f-c308-3ba1-b953-e47ed5ac8d7f | -6.8017 | -60.11381 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 973c0a33-711c-331a-8247-60af2a442446 | -6.73746 | -59.77296 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6d5de8-9c56-3078-b5eb-bf8adad282ee | -6.73558 | -59.63422 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4ac6984-2780-359f-a47f-52eac02251d2 | -6.69152 | -59.86507 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df53edfd-29a0-30ec-88d2-d3812baee948 | -6.61111 | -60.00551 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66324010-34ba-36e2-8abc-bc70f57956af | -6.60653 | -60.00486 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fe83b11-adbc-36a1-a842-864968e56320 | -6.55551 | -60.03338 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e1071f6-3866-3d12-862d-fc604ebe9ff3 | -6.55094 | -60.03281 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60a8dc54-e01a-30e1-a8e5-f90cb6464329 | -6.54636 | -60.03228 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4529cb25-5892-3594-a475-a6a3161161b4 | -6.54247 | -60.02696 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec8b2854-483b-375a-979c-1b818e1b485b | -6.54181 | -59.76976 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5d423f6-468c-3ff2-a8c5-328fd00dab56 | -6.54179 | -60.03163 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc4220bc-1af2-36af-8c88-137d22fbc53c | -6.53786 | -59.76423 | 2024-10-12 05:46:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24dc414f-02aa-3cba-9822-8a364319e73c | -6.52409 | -60.05751 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91f075d5-59da-343c-8e88-5d59a484705a | -6.52345 | -60.06199 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b40516b5-5047-383f-964e-a35e7eb49bcc | -6.51956 | -60.05677 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27fe845b-8c46-3cb9-ac2a-3836409933fa | -6.51891 | -60.06126 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d428c82-59cb-3688-996b-b5c8bb3c411e | -6.51436 | -60.06059 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f2e21a9-4ef7-3516-9d95-b0df06fa505f | -6.51361 | -60.09804 | 2024-10-12 05:46:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c23a7311-49b4-3297-b74b-72faacc1595e | -6.79113 | -59.35331 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c07d1a1d-f33d-3380-97a2-3dbd68d0f899 | -6.79041 | -59.35854 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a90e767d-9804-3f24-ae80-b22c98d3e27c | -6.78734 | -59.30986 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ceb0f1e-a496-34f0-ad5d-614333d1fd10 | -6.78732 | -59.31307 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b8311a1-e330-3f87-910c-a57f67a4a3fb | -6.78661 | -59.31514 | 2024-10-12 05:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README139.md)
