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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3aa27fb9-d9ed-3d88-8c06-fbfaf5fd7ca9 | -10.8755 | -63.8979 | 2024-10-07 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 0c097b9c-acd3-3311-88a0-9478390a8d77 | -10.8754 | -63.9169 | 2024-10-07 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1cbaa041-6ee7-3836-9504-bd5db6e607ac | -3.94855 | -41.49598 | 2024-10-07 04:49:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 982530eb-0212-3934-b90b-2e5c6796512b | -4.28761 | -43.7267 | 2024-10-07 04:49:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0119305b-eb43-354a-b201-b154bc49f65e | -4.28513 | -43.74238 | 2024-10-07 04:49:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5a2391da-0e70-3f5c-8105-08bbb1760593 | -4.28259 | -43.75843 | 2024-10-07 04:49:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 987f6c9e-6a98-39c9-91d0-7e3ed6d4c026 | -4.276 | -43.72506 | 2024-10-07 04:49:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 027cd12e-6130-38e6-bb19-b3e96e4e1849 | -4.27351 | -43.74068 | 2024-10-07 04:49:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| b887cd23-4a54-38f0-9342-e157f3be6f96 | -4.05476 | -43.237 | 2024-10-07 04:49:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 74a70a7e-7e8d-31c4-9722-c4da2ca00a23 | -4.05203 | -43.24588 | 2024-10-07 04:49:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ff9c6a0e-9d6f-3b2a-b734-7984967dd35e | -0.03587 | -51.66207 | 2024-10-07 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed424104-a920-3a6c-ae3a-8f3ebf633fda | -1.0313 | -53.73694 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a47b4712-bdb8-340c-9abf-592a9840a721 | -1.02956 | -53.72538 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7ebb10e-b91e-3616-88b3-db2381eceacc | -1.02897 | -53.72915 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebd5af66-4ebf-38a5-ae0e-83b3c8eab55e | -1.0284 | -53.7328 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ec62f310-2f70-31b0-994e-64aa56dfe175 | -1.02783 | -53.73643 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 4e3f72bc-bb93-347e-a648-b5f8179c86cf | -1.02611 | -53.72475 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 797dce00-97b0-33b6-8a01-cfd6c957cdbb | -1.02552 | -53.72851 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 142d222f-1749-3ad0-a6db-4aef0d11af92 | -1.02494 | -53.73221 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 684d25b3-e195-3115-aa4e-23cbce59b02f | -0.94246 | -53.72308 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6bf3097a-1c5c-3562-9487-d2c6b3d2b484 | -3.38181 | -43.21727 | 2024-10-07 04:49:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 265f9ca6-bd54-3e76-98d8-e20b9d22478c | -0.69654 | -48.5178 | 2024-10-07 04:49:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00e0ce85-7520-3e62-abb1-2b8b6491a84b | -0.2699 | -48.74042 | 2024-10-07 04:49:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e746e668-860d-39fb-94d1-3211c4e5cf62 | -0.16929 | -51.70032 | 2024-10-07 04:49:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 629bdd74-670a-37fe-8d53-1949a9a18c4e | -1.20135 | -46.5869 | 2024-10-07 04:49:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c15536a7-783f-3eae-a0ac-5ee79c8004ed | -2.74046 | -46.77041 | 2024-10-07 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142492fe-be19-3762-9f01-01a9243f444c | -2.72148 | -46.81427 | 2024-10-07 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71266f2b-f1fe-35fd-97f5-3ca18d093424 | -2.71799 | -46.8102 | 2024-10-07 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a099e7fb-8639-346e-939d-2f09786891ed | -2.34711 | -46.85191 | 2024-10-07 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c40ac272-785a-3a9a-810e-9338feba7f93 | -2.3458 | -46.85216 | 2024-10-07 04:49:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71cd16ac-456d-3c72-921a-5308917a023d | -2.26602 | -46.5719 | 2024-10-07 04:49:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa41ca86-fb4c-3cb1-8f03-8633aee33fe1 | -2.46444 | -48.85288 | 2024-10-07 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84536133-e057-3cf8-9ee3-ad6cfaf29aab | -2.44223 | -48.66703 | 2024-10-07 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1885394b-93e9-36de-b4d5-3efb8b01fc62 | -2.43865 | -48.66647 | 2024-10-07 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bb33990-a15b-33d5-87a9-5230701f23f4 | -2.39062 | -48.63038 | 2024-10-07 04:49:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5468321-2abe-3522-bc29-de95c2be687e | -2.59338 | -48.95609 | 2024-10-07 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7166f76-17b9-3793-8ac9-c7d6131a4782 | -2.53604 | -49.02145 | 2024-10-07 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd6119a0-5297-3d12-9430-feae394fbeda | -2.53252 | -49.02092 | 2024-10-07 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22bb2579-cb90-313d-88f5-30b2b909244b | -2.38037 | -49.09127 | 2024-10-07 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c33d4605-37a7-321b-8494-ae6a40ea7f8a | -2.33181 | -49.10375 | 2024-10-07 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fd20f38-b40d-33f4-b1c7-229a83f4eadf | 2.17752 | -50.68831 | 2024-10-07 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9e625d8-cbeb-3bc1-b363-e9aeb648c1d4 | 1.80809 | -50.81011 | 2024-10-07 04:49:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 091f1331-66d9-3367-91f9-8e8427d5b90a | -2.12076 | -50.80423 | 2024-10-07 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da1f7b62-bd9e-391e-8ea4-92f388f98b10 | -2.12021 | -50.80771 | 2024-10-07 04:49:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f11977de-1355-3673-8be0-a9243a5aa556 | -1.62488 | -50.53763 | 2024-10-07 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8765a2e4-f83f-3d19-bbb8-846106543f1b | -1.52802 | -52.8202 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 426af4c2-b216-3d33-925e-914982605077 | -1.16397 | -53.78082 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2e16802-6ca1-3e55-9cfb-1713d4cd3839 | -1.13121 | -53.63627 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2621eef3-79fd-32a3-8184-889c6671eafd | -1.12836 | -53.63195 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 027d064c-3620-3e47-b4ae-b5a70ee6a51c | -1.12552 | -53.62759 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4fd1117-9eb0-3e13-80a7-33811a79804f | -1.12266 | -53.6233 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de470b3-5849-36e1-b19f-9b5176d6557a | -1.12209 | -53.62696 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7febdba8-1d2f-39ac-8e86-f51d3e8b1142 | -1.04123 | -53.5384 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 63ba703e-b9cb-3a17-8fd8-a2ec7ced5b99 | -1.04064 | -53.54214 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b2e053f0-664f-3827-aff1-98c51039b74a | -1.03779 | -53.53788 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7f4af68-7111-33e1-bc03-3f0b2f033be4 | -1.0372 | -53.54161 | 2024-10-07 04:49:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4bc3d6c-5a5b-3ed6-9f63-e336e30d294d | -1.03187 | -53.73326 | 2024-10-07 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| da8e4823-2592-3bc5-8a66-bec338bde36e | -6.88773 | -39.20402 | 2024-10-07 04:51:00 | AQUA_M-M | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 694b8965-00f5-3bea-a8a1-e41f64a3476a | -12.7277 | -40.21592 | 2024-10-07 04:51:00 | AQUA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ac7db0fd-9db8-3712-9dc4-3c90c5bc6fd2 | -12.71884 | -40.21458 | 2024-10-07 04:51:00 | AQUA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8b94066a-c277-3cfe-8639-17fd8acbbcf1 | -12.7175 | -40.2236 | 2024-10-07 04:51:00 | AQUA_M-M | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 17c04e28-9392-394d-bbb2-a84c9159d787 | -9.57896 | -40.34472 | 2024-10-07 04:51:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| ce7adb44-fa83-3fe3-974f-aaba81b8f46d | -7.84779 | -42.2193 | 2024-10-07 04:51:00 | AQUA_M-M | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 88995b4e-7ba2-3b5c-a502-36ac042fc7e7 | -7.73747 | -43.04842 | 2024-10-07 04:51:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 83bcec6b-79dd-3223-9d7f-3c331978850c | -7.73548 | -43.06099 | 2024-10-07 04:51:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e538e6bc-1b0e-3bfd-9ea6-938db830f9c2 | -7.64984 | -42.49749 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| acf279b7-139d-3928-b45d-401b75b2ecd7 | -7.64805 | -42.50902 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| eb9cfa23-d425-3f11-8480-2b112caa02ce | -7.64624 | -42.52058 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 55788951-33fd-3cbd-a45a-d1edc9c59a14 | -7.63806 | -42.50746 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 0a15c2a8-4cc3-3401-9473-161bf0a36a56 | -7.63624 | -42.51904 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 3ed60ece-263c-3ca2-9362-475220f0374a | -7.30973 | -42.24569 | 2024-10-07 04:51:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| d433d09b-7044-3cde-9a79-1e4fd2d57358 | -7.15007 | -42.61471 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 2ff4cddb-c583-3792-b4c4-071f149aa75f | -6.47916 | -43.21761 | 2024-10-07 04:51:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1fe13abe-148c-3166-908f-b81f935bf197 | -6.46846 | -43.21589 | 2024-10-07 04:51:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 488820ff-2d17-359c-becb-b8e4f9ddf2a8 | -11.76154 | -44.49991 | 2024-10-07 04:51:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b16e3d8c-7ed9-3553-921a-9d529ce3b8d5 | -11.75079 | -44.49809 | 2024-10-07 04:51:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b9e89ac0-790f-369c-8638-ba27e6909cc0 | -8.15435 | -44.4134 | 2024-10-07 04:51:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bca63141-2122-334c-805a-4b3311712012 | -10.27032 | -45.48568 | 2024-10-07 04:51:00 | AQUA_M-M | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 7b8283ea-05cb-3b83-a656-0fcedea5ab22 | -9.31412 | -46.72177 | 2024-10-07 04:51:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e2735010-519f-3388-b301-d245acfb2f43 | -3.5455 | -65.02657 | 2024-10-07 04:51:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3729c70a-0ad9-31b3-b3ed-a99bddaa3378 | -3.5387 | -65.02541 | 2024-10-07 04:51:00 | NOAA-21 | ALVARÃES | AMAZONAS | Brasil | 1300029 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65cbb720-8fc8-3aff-b0da-694a6d39e994 | -6.87597 | -39.20434 | 2024-10-07 04:51:00 | NOAA-21 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7c6e6db9-76ce-347c-8e17-43b072908437 | -9.57957 | -40.34475 | 2024-10-07 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4999a192-9fa6-3b4e-ba83-87178abb8c7b | -9.57501 | -40.34294 | 2024-10-07 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 53d71d27-ce56-354f-afa6-ab2af4b4153f | -9.57429 | -40.34908 | 2024-10-07 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3076db84-a29b-3253-b90a-813f59ca6d25 | -9.5728 | -40.34383 | 2024-10-07 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 062c1fcb-1027-3676-8a1b-b54b504bc725 | -6.28693 | -41.85976 | 2024-10-07 04:51:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e2b24dd4-5bc0-305b-b368-e8b9c9543498 | -7.84255 | -42.22941 | 2024-10-07 04:51:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 13587782-6882-3b48-aa27-1b8c2dbc90b0 | -7.83911 | -42.22324 | 2024-10-07 04:51:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5f27a9f7-30c7-3224-8ee8-2c96040d3000 | -7.83854 | -42.22748 | 2024-10-07 04:51:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8fb2d60c-d563-319e-a7a4-95a6f4024f2c | -7.83773 | -42.22 | 2024-10-07 04:51:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6b07e9fb-2f0a-3ab2-9712-4e2ed14f7514 | -7.83719 | -42.22424 | 2024-10-07 04:51:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 83e12caa-fdaa-3933-8154-b1720c2918de | -6.85678 | -41.69739 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 09195e76-8b61-3fbe-9924-13a026d8e167 | -6.85617 | -41.70184 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2ad0c4bb-5ecf-3d56-a400-92030046c0e3 | -6.85556 | -41.70628 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5b4e692c-4de1-399f-a17b-fb50a6e43bb9 | -6.85375 | -41.68896 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a6a0aa4-1d76-3c3c-a4d5-27906c2f2de2 | -6.85316 | -41.69346 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4aaae469-e213-34ad-85f7-a2a1ef44cf89 | -6.85258 | -41.69794 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74cbe11f-37ac-3832-9127-74535119b2c3 | -6.852 | -41.7024 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 72d2a8f2-535d-399b-81bc-9bebd25df4a2 | -6.85197 | -41.6877 | 2024-10-07 04:51:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README78.md)
