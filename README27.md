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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47b559b6-0684-3521-8724-32ae0d2ac4ac | -2.675 | -56.4657 | 2026-09-28 04:32:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b970621-4eee-3a87-aa4d-c8771117ce7e | -4.91334 | -37.37223 | 2026-09-28 04:32:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1a880401-02a4-3d9f-8832-c69066cd1e5f | -1.80451 | -48.06151 | 2026-09-28 04:32:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aa6147c-451a-31ec-b69f-5f1cac280a60 | -2.66237 | -51.73925 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88ccd231-0907-377b-a361-44b2da1acf32 | -5.23266 | -45.82001 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8fd2bba-d393-3b00-94a7-0729b3c84166 | -0.49154 | -49.13683 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dace360-0b80-37e4-bedf-fe5f18ee4164 | -5.28819 | -48.12929 | 2026-09-28 04:32:00 | NOAA-21 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ee479be-029b-380f-a91f-4319c5a3e2a8 | -0.50379 | -49.12692 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f9b4f6d0-2f1c-34fa-a455-981b7912b2ae | -2.05318 | -56.86834 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 432ce54b-6d39-3b9a-bab1-35528ce07cd7 | 1.24782 | -51.12985 | 2026-09-28 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2147bdab-fbb7-3110-9bf1-4653afef5902 | -5.57769 | -45.30289 | 2026-09-28 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4510e1ca-5dbd-3669-8ca8-0f715cbfac0b | -2.1183 | -56.88375 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ca9d14-80fd-3dd8-b8be-e847266cf3f3 | 1.67597 | -55.95459 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c33b6018-b0bc-3fa2-896a-e6c3762d05f2 | -3.69697 | -51.37166 | 2026-09-28 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 47e0eb36-499f-3aed-9fd5-79dce7534820 | -5.7267 | -43.28173 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 981587c6-779a-39f2-a59e-a8fe97524167 | 1.26113 | -50.67558 | 2026-09-28 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 348615de-c040-3f57-a8c7-55af9e81ec72 | -3.23798 | -50.57454 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5a45b7c-d9c4-3e78-b3e9-7ce8201182e5 | -3.97685 | -44.51593 | 2026-09-28 04:32:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c6f8de4a-8ee3-3cce-84d0-38ae157a3ebe | -1.76644 | -53.76271 | 2026-09-28 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 287ede9c-eaad-3d85-8af8-1ba8662e5620 | -2.77239 | -49.48136 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9577b1c3-0542-39aa-9959-bd1aaf6015a5 | -2.99212 | -47.45054 | 2026-09-28 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b242b33-3d46-3aa2-ac16-2b71bbd6fb9a | -3.20326 | -51.03137 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba763c6e-2a4e-3b76-8243-896a624a7791 | -4.31045 | -50.39883 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1af57cd-9939-3fd5-ba59-1185711be21b | -3.42152 | -50.42825 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b280fbe4-40db-3a1d-8150-da66a1dec752 | -3.98337 | -44.52107 | 2026-09-28 04:32:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a4bf993-4df4-354f-a40a-9dc31ee662d1 | -3.0115 | -54.21609 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e12aff50-4dcd-3fda-8c76-27fffa40c566 | -3.42219 | -50.41532 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3137e29d-2715-3088-84d7-80c7b1aa4265 | -4.78611 | -49.11531 | 2026-09-28 04:32:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5663ec1-2450-3f64-a7c0-61e7d8ac8050 | -2.07686 | -49.5482 | 2026-09-28 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09c94049-ce84-3e01-bcb0-b2f0f7b82902 | -3.10271 | -50.19379 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b78595e-3a29-346f-a958-f2213d294d11 | 1.67488 | -55.94724 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d03c8f8-da78-33e0-98dc-66dec3d6e730 | -5.63707 | -43.71786 | 2026-09-28 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d9c26ac-169b-3efc-b41f-576de1e4c30c | -2.98674 | -51.05025 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35f1736f-0669-3515-9823-b29c0b4fc59c | -2.89631 | -54.17135 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04fb8416-1e7b-3494-819c-17368c96bb76 | -2.86052 | -54.13208 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3811f64-a800-3209-a507-7cab8a69e2d3 | -0.51075 | -49.12798 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8112f7d5-f3bb-3a23-9fb7-21e226e1273b | -3.82077 | -44.09119 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9c78b38-1cbc-335d-a4e6-d518782dc641 | -3.80363 | -44.1059 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6471208-15cf-3fe6-bb49-77faa79f64ea | -0.49623 | -49.12969 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb964ea-5bdb-3e72-9d43-d1b26b4af244 | -3.21068 | -51.03257 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f41908ec-42b5-3892-8057-f7bdb7063859 | 1.66565 | -55.92194 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7f03ab3-67b7-3915-bc5c-8e2609bd03cb | -0.93837 | -47.55184 | 2026-09-28 04:32:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af162a65-dd64-3b3b-9643-ee186cf996be | -0.49502 | -49.13736 | 2026-09-28 04:32:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeb1d384-c91a-3919-a81d-176c7644b330 | 1.65943 | -55.91948 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b3efeb2-21da-3370-b65a-35a167a2920d | -5.12952 | -45.75922 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddd8e6e5-9d74-3822-be3f-1ba5541a5842 | -2.7317 | -54.2004 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76b64430-ddf9-3c52-8a2f-48e9502d3d31 | -4.98422 | -47.48591 | 2026-09-28 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93e7bdd9-2043-3b0a-884c-20506907dd89 | -3.29477 | -50.30924 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67fe144c-81fa-37d5-a504-a86c0fb2dd9f | -5.12154 | -45.76553 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 38df1d20-88ff-310e-ab27-282a6dca9804 | -3.98925 | -50.52448 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eae495a-b6bf-39cd-931d-8ba45c7c2188 | -3.39366 | -44.37062 | 2026-09-28 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3af9cdd9-981c-39d9-b29f-a7eded30523f | -3.01225 | -54.2114 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bae01220-9276-3e32-b9d5-11047cd4c22c | -3.147 | -54.07421 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d23620d-8041-3c6e-961b-737ffc0fc0cb | -1.74153 | -57.18139 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39b79aad-1e9a-3d8a-aa14-bfa2939aeaea | -3.80063 | -44.1011 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3130411-6466-344f-a004-40d34b0492c6 | -3.8092 | -44.09374 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 167d44f9-0d91-33b6-81c8-221b7d26f6b0 | -2.89707 | -54.16663 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abee70a8-4dc9-37fe-9d6c-92910bba010d | 1.67694 | -55.95787 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7bf61ef-5788-3a3c-95a5-0a9df6dc0fd7 | -3.46072 | -50.61182 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 912675a5-2c87-37d5-94db-b1f48cee343f | -2.26829 | -52.01536 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a723500-2bfa-3633-bf31-f6cb6a9e161e | 1.25027 | -51.12737 | 2026-09-28 04:32:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aad24e48-684d-3f98-85d0-d0871a2b67a1 | -2.9122 | -54.13065 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30187d63-59fc-3118-90da-b3fba39fdad4 | -2.42646 | -48.39289 | 2026-09-28 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f43085b-8960-34b6-8f95-70af293d8eb9 | -2.07337 | -49.54766 | 2026-09-28 04:32:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c46c96d6-bd80-3cc7-b9a4-6ae51f4f45f9 | -3.19143 | -51.03407 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a09bb0f-191e-34f9-a457-46eaeefe79a0 | -1.04522 | -53.56222 | 2026-09-28 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8e0110b-d485-3002-b0ae-08875c59646c | -1.73581 | -57.18055 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91a3ce09-f161-3d9e-a162-9bfa8ef8f6dd | -3.01684 | -54.21205 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6d0977b-67f6-3885-ad21-d53a7a1962ed | -2.72709 | -54.19982 | 2026-09-28 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00f09e48-8ddf-3796-b41f-6db84c33199b | -3.81778 | -44.08638 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 910342f2-0a09-39f5-89a1-e2815e697525 | -3.14954 | -54.09699 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fa0aa8e-c5f7-3698-8263-ff573494cb2e | -5.72679 | -43.28321 | 2026-09-28 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 838a81c6-684b-364c-8fbc-ee9b20a231da | -1.77024 | -53.76802 | 2026-09-28 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| accec87e-943b-3c5e-9fbe-1eda87d06dda | -3.93742 | -42.5519 | 2026-09-28 04:32:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| bd9daa38-4a26-38e0-a8d0-47f40107b55f | 1.64566 | -55.90259 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8d1a079-1baa-354d-a22c-b6aec5cc6873 | -1.9312 | -52.14098 | 2026-09-28 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c7fe5861-dfd9-3cc4-b56a-915e94783b21 | -1.04972 | -53.563 | 2026-09-28 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3da3b927-aa1f-352c-973b-35ccf4cc7024 | -3.107 | -50.32263 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a193f488-7095-37c7-8ff9-f53e35dbc163 | 1.66551 | -55.92232 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78f04dc5-d873-34bf-9560-33cd94094ad7 | -3.41793 | -50.42774 | 2026-09-28 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40222687-c1ee-350d-9a2d-23b5ba93b95d | -2.77179 | -49.48515 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fe4363e3-3fb5-3c3f-9ce3-8d83de67aa3b | -3.81713 | -44.09062 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b1ac34f2-b39e-3220-bec1-4f20db0189b0 | -6.14129 | -44.13339 | 2026-09-28 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dd69636-1214-38f5-9081-0c29186643d2 | -4.04246 | -54.22127 | 2026-09-28 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f9d517-70fb-36ea-a3fc-32c6a442efd7 | 1.65389 | -55.92031 | 2026-09-28 04:32:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb47b611-75a0-3fa1-a728-261dce5138f3 | -5.42514 | -45.8907 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc0b5e69-c170-3469-aef6-c991044ab399 | -4.31399 | -50.39939 | 2026-09-28 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ea60d711-83a3-324e-aa44-b6954c3f89bb | -1.26086 | -54.68645 | 2026-09-28 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d06bfe64-a539-34ee-a52a-62782e97dc25 | -3.23436 | -50.57398 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cb0b14b-c401-32d2-b913-f90e6ed0d1e0 | -2.73618 | -49.46408 | 2026-09-28 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21d41db3-d398-3f7d-b6ab-e6c8fa36655b | -2.55309 | -58.04839 | 2026-09-28 04:32:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7d4faca-38fd-3dc6-82f5-3f2ceaedbe19 | -2.05826 | -56.86662 | 2026-09-28 04:32:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c92cf373-b7ae-3bfb-b102-20e69f1f993e | -3.95684 | -49.04782 | 2026-09-28 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f28c44c-7339-37f7-98c2-3a1379dd77d0 | -2.61275 | -51.74436 | 2026-09-28 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f441985-4566-3aba-8600-332d4c735564 | -2.99159 | -47.45398 | 2026-09-28 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a1fb90d-6384-37a7-b48a-34cc7c211479 | -3.15005 | -54.08414 | 2026-09-28 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e953cc5b-fb1f-372e-b612-526ad26a54b9 | -5.12495 | -45.76609 | 2026-09-28 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70092eab-cf01-3728-b9a8-37bf6f6fa7d6 | -3.81349 | -44.09006 | 2026-09-28 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2f8d4e4-1166-343c-962d-37c3eecea542 | -3.9934 | -49.04652 | 2026-09-28 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a87168a-a3c0-3834-90d4-f5dac8e1f3ab | -3.22551 | -54.31952 | 2026-09-28 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README28.md)
