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

## Dados Diários - Página 193

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c12f3ba-72b1-362a-bd40-67c98febd011 | -4.42827 | -55.16275 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 737f2127-9355-37cc-a745-108ac4c07b1f | -3.5949 | -54.58134 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0a350598-c891-3b28-a2a8-1a8aed39664b | -3.67659 | -54.50222 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 593dc6e3-0cbc-34f8-80eb-2c3d7e92e1e7 | -3.26689 | -54.0528 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c069f8ad-4f71-34bb-bdeb-4de113b9c614 | -3.17353 | -50.59684 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4bd5443c-5996-37c6-9aed-7be70f85ae52 | -2.78319 | -51.6841 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58dc946f-df1c-32e7-9d89-b3b385fdefd7 | -2.78478 | -51.68222 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52ee68b9-1cf6-30f7-af82-eebfab457285 | -3.47461 | -54.63147 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a179e5b1-1b4e-3317-8913-b677f1e2f755 | -5.29611 | -60.08728 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ade14a39-2ae2-38f8-b548-8bb7636b9b4b | -3.32731 | -58.15255 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ebee0b9-1d66-3920-a39e-41fd9aa1d99e | -3.17819 | -58.63746 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 83a04e26-cebb-3f54-8f6c-0f5e33d3450d | -3.53888 | -59.4938 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c86ff76d-a192-3d41-9b2a-14f21918d961 | -2.78899 | -54.088 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3787a887-7854-3a91-8e9f-44999886eb3e | -4.06443 | -51.04182 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ddc6984-2831-35e4-b6b5-39ebda0854a4 | -3.16831 | -54.73432 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07d041fe-16ff-337d-81ef-9a97282a4a71 | -3.07749 | -53.9598 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ead9e523-d73d-3cec-8cb4-604dafd87bf6 | -3.86456 | -56.00367 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 024931c7-dfda-3f48-b4c1-3021b221467f | -3.39958 | -59.60764 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21a81d09-704a-3141-90e1-1aa14e6d8604 | -4.52188 | -54.9843 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e65d9e3-c47d-39d2-a0a1-641817911489 | -3.02307 | -53.92045 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 948e415b-cc4f-3a8d-aeaf-73da69cb2b91 | -3.289 | -54.08672 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3c1330e-3808-3124-85f4-90c0333e744e | -3.54015 | -54.6299 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a8f1c49-ceee-38ed-a82f-58f2faf6b5af | -3.2706 | -51.06977 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f286fc7e-3d47-3658-b471-ba3ded8ee75e | -3.5877 | -54.30485 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bab771b2-d940-3121-a566-8ed0730cfe98 | -3.02422 | -54.09469 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c3ab43c5-fc6e-320c-8043-776c9838cdbe | -3.85455 | -55.98352 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5524a796-7880-3bb1-9357-067a27800e03 | -3.02661 | -53.89673 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a165545-27f5-3f54-b9fb-f95c076692f9 | -3.29725 | -54.05423 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7abbc7d-3e83-3016-9f83-069f40e2efb0 | -2.50635 | -59.52876 | 2026-10-08 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a645f17-4f6c-39b1-b477-f60efe803ba5 | -3.17113 | -58.63135 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b72af8e-966e-3bb4-adca-4ea63bee0a36 | -3.54635 | -54.65939 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 162d00f2-28ca-3ce6-a135-52184f44189d | -3.03998 | -53.95406 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7d6e9ec8-5a45-3459-8caf-57831ba5a0b6 | -3.01757 | -54.06675 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b4dd35d-d69c-3f14-bb73-177a52249672 | -6.62719 | -55.29857 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4a5b042-eb9b-30bd-8b1a-bf9e8b4c8a4d | -5.23644 | -50.90878 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9016cf30-1980-31d5-906d-6cdc891ff872 | -2.46694 | -56.09319 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bd4322a-9a8c-318b-b2ea-f3cad9428891 | -3.69615 | -59.64741 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b88f8b0-bcf7-3d1c-b281-2f816259f780 | -3.67041 | -60.62651 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2427af50-b74f-3894-bd92-50653272e7b6 | -3.02339 | -54.06424 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9caec870-9b4a-3b6e-a67c-44cac6c072e8 | -2.98687 | -54.77631 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7317282-68bd-38ce-8238-fa742c2e6ac3 | -3.28707 | -54.01145 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ea5f411-9fbd-37cc-b1f0-159be138e4ac | -3.2463 | -57.86756 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e69a91ab-6c0c-3127-baaf-6b820cc54ee0 | -3.30221 | -54.02036 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30813e13-b0f9-3a45-8288-b5a7e1f6e711 | -2.98837 | -59.04095 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b9dc3fe-99d0-30b6-9b94-24f934c5e696 | -3.3646 | -50.48392 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 755967fd-885f-312d-8015-fdf2eac27511 | -7.22682 | -55.11111 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7173c10e-6336-3b81-b013-6333ee77de84 | -3.58595 | -54.57032 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79f02ffa-88cc-37fa-81a9-ddfb3b031eb5 | -3.47789 | -59.45915 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eeeb692-62ca-3be6-9aa6-cd169a8260d1 | -2.48558 | -56.12473 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0d7f5f6-671a-3650-8f65-368d690edd90 | -3.08391 | -53.95367 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1278dbe5-a2ef-34eb-a41d-efa8ba0a881d | -2.50412 | -56.15633 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbdb9a4d-5471-3bd9-ad90-937af660b4f1 | -5.22745 | -60.23999 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66750fed-e75d-3485-ac55-e6d4fe3deb85 | -2.64243 | -59.7862 | 2026-10-08 05:42:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1e60352-eca8-3472-8b16-7f9e4c175294 | -6.80458 | -55.29888 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dd12f70-090f-3ad0-89e1-4cc66cb23658 | -4.06629 | -59.83946 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f6262f11-5d5d-36ee-8729-5422207f7658 | -3.04762 | -53.90334 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 988ebb19-6013-3772-ac46-d2a79417b7ee | -7.89903 | -54.71547 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0f884edd-697e-38fa-a136-bc1136385228 | -2.86909 | -54.47882 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 055cbbaf-8524-3ea4-8e9d-8c278851afbf | -3.03948 | -54.52839 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed5d3fc9-2fa1-3c34-a075-9fe15704e918 | -3.04754 | -54.15507 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0b32797-93d8-30b0-8cb5-5ec769d0bc3e | -3.59621 | -61.6361 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac371ac8-0664-30c9-83e8-0a7c56df5a3c | -3.1861 | -50.55719 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eeed8fb3-3f1a-3ed7-8162-6ed402e88051 | -5.68217 | -53.48194 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f660e2b-cb80-3dbd-83fa-752760d5b450 | -4.30542 | -60.946 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b958613e-e01f-32ec-8cad-db800bd8fbf0 | -3.66689 | -60.62597 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ca31587-6867-38dd-a9e6-94033c47af2f | -3.55532 | -54.66992 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3408edc2-3296-3f78-b339-f58d1a028bc1 | -3.2972 | -54.03342 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d61225e-458a-30db-955a-f54fee8789b2 | -3.54836 | -59.48155 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de28743a-dc49-3568-ac0a-cf08213e8e31 | -4.09841 | -52.06857 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 996ba6f9-528f-3474-9fd1-f8e029aec9a0 | -3.57966 | -54.68303 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1b475fbb-a155-3458-842f-c8ec8af182ac | -2.88623 | -59.20244 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ec5dda2-8751-3364-9b89-9ffc594a08e7 | -3.70444 | -58.29564 | 2026-10-08 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21ea77f6-bd63-3146-a9ac-250a0209512f | -3.11631 | -57.59741 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72a2ef7f-d811-3970-bc78-ea120422f878 | -3.53847 | -54.67726 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00fcce6c-6266-3582-afd1-d7e56b84e4db | -3.30336 | -54.67389 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dbd4f5e-4d8a-32de-b1da-7ba6a99b8acf | -3.63624 | -58.93926 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b92335a1-9228-3002-98b7-6726049ff1d3 | -7.21449 | -55.16218 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00bd5865-400b-3507-8482-02f9ea0ab8b7 | -3.50037 | -59.28705 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8c59be2-17df-35bf-a109-27cc8fff1684 | -3.2851 | -54.06269 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f763034-dc27-37f0-a5ee-6bf4da93b210 | -4.5373 | -54.98598 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70356aa2-6ebe-34bf-b26d-77857fc3536f | -3.08197 | -54.24364 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3af10033-ab4e-34ca-a9f2-baf340228e42 | -2.9452 | -54.15289 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46d3cff2-c927-3289-9054-8211e9607636 | -4.92348 | -55.86406 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb28a5bf-eb9f-356e-b7b2-0ed061cb89f0 | -3.70364 | -61.32943 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 840015bd-e628-36ab-87f8-498d5d5787e6 | -3.46025 | -59.47465 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f53304c-ed1b-3f08-b53a-6da33ce23109 | -3.50283 | -51.69436 | 2026-10-08 05:42:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac9da39a-defd-3eac-9083-8554354c6c9f | -4.53498 | -55.61718 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4895d3cc-cfa5-3482-8543-4542ebee47ce | -3.35151 | -59.50131 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26111c21-3872-3960-a709-c74809dcaa16 | -3.30129 | -61.3484 | 2026-10-08 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 699eddc6-374a-3b69-97e9-41fcbc060a52 | -3.6333 | -59.54913 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d9e49fb-2281-3e5f-a8e8-c4103861fec9 | -3.53343 | -59.49496 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 525440d1-ec0f-341d-94ff-41adf0684d20 | -3.77742 | -58.52299 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe085f8d-9a37-329f-87e8-788ea5530f98 | -3.71253 | -60.54256 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ff145d3-0512-3fbf-85fb-21120952c947 | -3.5459 | -54.66245 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c43a6b3b-d50d-3ee6-bf52-cf5b4ddeb808 | -3.01115 | -54.10942 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2c08882-a0df-3e5f-ad78-539e85fd8e11 | -3.29338 | -54.04336 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c70cd77a-03aa-3527-a593-83a45dae9f68 | -3.29732 | -54.01629 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f28367fc-1a87-38ad-982b-eacd372b11b3 | -2.49813 | -56.16489 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d02ea47-a2c5-313c-9bf7-970dc2db0793 | -3.01361 | -54.09307 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ac494221-2798-3b9a-90e8-6a9a7635a34a | -3.61343 | -55.4712 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README194.md)
