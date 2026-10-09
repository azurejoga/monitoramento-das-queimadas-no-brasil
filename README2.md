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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcea91da-b1dc-3577-b6ad-6697f509fb0d | -11.8499 | -43.5835 | 2026-10-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| fb70beb4-e212-3c38-a29d-e4b69e5ace40 | -13.4922 | -44.3713 | 2026-10-09 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 32f55a12-78b2-3275-8767-cc73d3eceb86 | -6.4903 | -62.8554 | 2026-10-09 00:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 32cc317b-ae0e-3701-86cf-bdf438ca9891 | -4.6282 | -49.2147 | 2026-10-09 00:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 28fd1fb2-ccfa-3be0-9cae-985544f92ac5 | -5.6934 | -53.4667 | 2026-10-09 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 6c6e40e7-e587-3ceb-b87a-c15845da5bfa | -10.0256 | -48.014 | 2026-10-09 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 96328efe-6063-3e20-868e-a2dd027fec52 | -3.0925 | -53.9455 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 22f80fb2-a81b-3801-9bc0-b4e39ee848bf | -7.4095 | -44.7656 | 2026-10-09 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c0581d01-4ad9-34bf-9e51-c60f8f75c569 | -13.183 | -54.3365 | 2026-10-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6547271f-137c-3d0a-91a2-f95ebab52524 | -3.1786 | -50.6016 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ed3af8c8-03eb-36df-bea9-d613f3c46698 | -2.9823 | -53.908 | 2026-10-09 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6e1f6f13-e3f1-32c2-93e3-d0d19b6e6677 | -6.8907 | -45.8988 | 2026-10-09 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c4b3cbd2-2928-3583-917b-3e9bb5e6d278 | -4.6096 | -49.2156 | 2026-10-09 00:00:00 | GOES-19 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| cd15fdd4-302a-3259-9a92-0b04cbab845c | -1.5489 | -54.5556 | 2026-10-09 00:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| a9e273c8-528a-30cf-84a5-5b9db5e0aac5 | -5.9833 | -40.961 | 2026-10-09 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| dc1fea4e-d7ca-3ce9-bedb-afae49a5293c | -6.4949 | -55.2995 | 2026-10-09 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 99f117b6-3d55-3126-8246-27b88252b3ff | -4.2768 | -49.0816 | 2026-10-09 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a3fdebcc-f7f8-386f-80a6-bd777eac69d5 | -7.5834 | -61.5516 | 2026-10-09 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b31709d5-e88a-340c-90de-8be34d1374eb | -5.7679 | -43.8467 | 2026-10-09 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 338b2a18-9036-3335-b834-7a37cb4aa347 | -11.6369 | -43.6876 | 2026-10-09 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 680e4a46-96b6-3bee-a9eb-fa902fbe03a3 | -13.1636 | -54.3591 | 2026-10-09 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| be2d96e4-56a4-305b-a818-fdf6ea849f03 | -3.364 | -50.4072 | 2026-10-09 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a1da8716-d162-3567-a600-7b041b2dd610 | -3.6975 | -47.687199 | 2026-10-09 00:06:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9cbc2e8-ef24-3c37-9603-8a01064125ad | -4.1574 | -47.9855 | 2026-10-09 00:06:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35243158-1e1e-3b81-9bae-09ecf54c89d8 | -9.1288 | -45.8246 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cf0c064d-3a0d-3a74-834e-45dcc97cb202 | -3.5555 | -54.674099 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f467375e-4e2f-30f1-96e9-e2bcfe648d55 | -3.0037 | -54.036201 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd6cdc9-8b53-3648-9aa1-fb0be71d6f89 | -2.2101 | -55.449902 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ca8c7f-331b-3f50-b02f-7c3a88a1be4d | -3.3039 | -54.000801 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8589223b-064e-3959-b065-865a80fab210 | -8.3291 | -45.447899 | 2026-10-09 00:06:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 31192267-5cc3-306e-a69c-69d08be6c716 | -6.9973 | -47.685799 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ff681f8f-dcc8-3c23-8d01-9b215e57a83b | -7.2261 | -55.137001 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4808ce-7e0e-39f0-8e8c-cf91fa061ad8 | -9.2966 | -47.456699 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2386689a-47ce-313d-9107-16ccb274a759 | -8.0756 | -45.6446 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1aacff0-0802-3d20-abc7-4c7945b97cec | -8.9068 | -45.181099 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 19cc3d67-1b39-35f3-883c-bc4bad4207b2 | -3.423 | -54.538101 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0166b5dc-766e-3b6c-b1be-da1398416d7c | -3.4862 | -50.4865 | 2026-10-09 00:06:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a33088-f6dd-3f0b-97df-ff6a827ab324 | -10.2782 | -47.831902 | 2026-10-09 00:06:00 | METOP-B | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abea9cd3-c98f-3740-b459-1ce3753b5739 | -12.0362 | -43.431801 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e80bc427-8dc7-388c-a8f7-a189850c8ec4 | -2.9981 | -53.918499 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 563c17d4-b55b-3f33-a9c4-0de7992ebf5d | -3.1973 | -58.8036 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdb2b2df-16ae-3284-a4e3-adcb84c6268a | -15.9569 | -40.8447 | 2026-10-09 00:06:00 | METOP-B | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| addf8ffe-ee64-36b4-8bce-7233b5626853 | -13.4982 | -44.366402 | 2026-10-09 00:06:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db0bec96-2397-3b19-b299-4242d201d974 | -2.7358 | -54.124599 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d966e00-937f-3c40-8a93-65a1d743d095 | -2.7188 | -54.6478 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4357820-9b12-306c-9137-0a3bb46f20b7 | -12.3148 | -47.078701 | 2026-10-09 00:06:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 979bb4ff-73ff-3ade-95d4-f59f4afb0be5 | -3.026 | -54.182701 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f201a66-0b12-3637-899a-c44e4df693e0 | -3.1085 | -53.953701 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f4a6f0d-ba08-3acf-9813-b8e1a7a1295a | -2.4 | -51.292099 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c22aae2-09f5-3bd8-89f7-8d9c8a4c70ff | -3.0369 | -54.139599 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776fd899-3919-3c56-81eb-ceecaade91f3 | -4.1146 | -55.025299 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3518037-1ed2-3a0a-ab74-40b78b29e5b5 | -3.1679 | -58.623501 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 342aab97-86a2-3823-bfbc-79ca305a4307 | -15.0145 | -46.245998 | 2026-10-09 00:06:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca01f30-8dc0-389d-9e52-c3f9f8d2c0ca | -12.0235 | -43.465 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc8ce719-4667-3621-bdec-e8b0acd7b936 | -6.6757 | -55.0928 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 612226a3-dc70-3d38-aa7f-43b6021afa71 | -7.0902 | -47.731201 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c2e6927-af08-34de-b0d9-d67d5becb33f | -3.0891 | -54.282001 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 476aaef9-1f5d-3b00-8783-8a0c43ba6245 | -5.5056 | -43.049099 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d753347e-342d-3897-9a08-1a417effa10a | -3.0262 | -54.0914 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9517a7ae-4058-31a3-9a7e-cf64a5dfae09 | -12.0039 | -43.469799 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2bcf633c-78f7-36fa-a643-15f86832f7db | -14.7844 | -42.903099 | 2026-10-09 00:06:00 | METOP-B | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 0236a7ef-2863-3c00-8ff7-912a1e61bfcb | -14.2538 | -43.669498 | 2026-10-09 00:06:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bbe7213c-b765-3b84-9a00-edd553a7b7a2 | -3.1062 | -53.758499 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aabe0ea5-f60f-32e3-9d3c-1748750d67de | -4.0799 | -44.120399 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5a32a7-49de-3c83-908d-5128545df344 | -2.5477 | -58.027 | 2026-10-09 00:06:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cbc054d-2b23-31d4-bbd2-af807387e9bc | -11.6035 | -43.6973 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 105683b5-9dbd-3526-9e93-470f7b375200 | -11.7719 | -43.536999 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 224ac30d-f8fb-37ad-922d-4344401269e9 | -10.4265 | -47.300598 | 2026-10-09 00:06:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f57d95a-71eb-35d8-add6-81baab493aa0 | -12.1654 | -49.386299 | 2026-10-09 00:06:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29604a59-b109-3ef3-8642-a819996a8db7 | -11.7865 | -46.793999 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4caa6aca-15cc-39cb-9dfe-2e6616d62f2d | -7.4697 | -42.861099 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 291e77e8-3c1a-3c5f-a8cf-c46011caaa6f | -18.632799 | -41.350101 | 2026-10-09 00:06:00 | METOP-B | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0d6124e-fa33-3d7b-8116-0c4e7135ca25 | -18.791599 | -46.462399 | 2026-10-09 00:06:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c8afefe7-dec2-3a08-9b8f-3427bb980c83 | -14.4399 | -43.931599 | 2026-10-09 00:06:00 | METOP-B | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 56f89ff4-c543-338b-842c-af639d8478ce | -1.5363 | -54.549301 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b79745-9395-36b2-919b-61506c5ad225 | -1.3233 | -56.388302 | 2026-10-09 00:06:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de409a4c-8bc5-39a5-b726-fd61b73dba46 | -3.2843 | -54.0051 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05f9d4f1-68b6-364c-88d6-fb16594a3760 | -2.9939 | -53.899799 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5d9f0af-a859-3ea7-bb2b-d750d6255079 | -9.7476 | -44.803699 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 25ad2564-cb47-3c20-9bb3-ea45706e10be | -3.2021 | -50.826698 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d97158e7-c1c4-3e31-ad57-b05e7686a320 | -2.8726 | -54.1856 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef61bb15-beeb-38f8-a91a-5c49614bb10d | -12.0167 | -43.4366 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e264afe4-97cb-3b40-a602-e2218a812f49 | -8.2849 | -50.2593 | 2026-10-09 00:06:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7887ce37-3c90-30dc-9fcb-5ced59ffa7d9 | -2.9283 | -54.112801 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8087539c-0c06-339f-9536-a54f5003ac0d | -5.7134 | -53.479698 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c95e8222-4d77-3df5-aa38-285736b6f144 | -11.7789 | -45.5886 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62f90ef0-16fe-3243-bd84-610e2fe94e25 | -18.6241 | -46.4491 | 2026-10-09 00:06:00 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d0a71533-cede-3d55-a5fa-0c49fbc826dd | -5.6705 | -46.3526 | 2026-10-09 00:06:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54bc8cb4-8a81-38c8-b5c6-d395ed7c996f | -3.0346 | -54.221699 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6b92e41-c66a-3e69-913d-0af8067bfb7f | -5.6952 | -53.443401 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e406960-1899-368a-9156-2084a88db9a9 | -11.0092 | -45.430698 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3796c3fe-97ff-3db9-9059-175ea72f4c77 | -8.676 | -47.086498 | 2026-10-09 00:06:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 627076d9-4f5e-3674-8d61-3c84c4438b59 | -6.1536 | -47.9212 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1a4bd8-02c6-37ec-83d3-c356eb93602b | -2.8802 | -54.173801 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4214e6-57ff-3219-a27c-793097b60cf7 | -3.768 | -58.577702 | 2026-10-09 00:06:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4111c5e9-95b0-3c46-817e-18435b8e2976 | -2.763 | -54.1087 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4aec4763-b301-30a4-8d53-e8cf3e180e06 | -3.0706 | -54.244701 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73112073-e8bf-33d5-8f94-db96ec3d0d91 | -14.9392 | -48.098301 | 2026-10-09 00:06:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0e314520-cd21-3908-ba3b-11e17ec47411 | -13.1931 | -54.363899 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08d8087a-e56d-3abf-8b71-90178c3ef840 | -13.3652 | -43.889999 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
