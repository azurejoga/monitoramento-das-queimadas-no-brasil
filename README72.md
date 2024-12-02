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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fef8c9a-7c49-3bdc-b465-e74fdff2966d | -5.5882 | -45.1412 | 2024-12-02 05:40:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 55504e81-5eb1-3390-8cbc-3ff49dc2c666 | 3.18377 | -60.18803 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 668cd704-b565-3772-9f52-604f1ef77f1e | 3.18849 | -60.18476 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78b80ed3-62ae-3100-8c26-4aa4c3b465bb | 3.18738 | -60.18746 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 291ae885-673c-3237-b1ae-17653baa4c13 | 3.19034 | -60.18272 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e0069e9-2dd7-391d-bac8-99e70e6e8897 | 3.15197 | -60.29064 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c804c428-c64f-3131-b13c-e3760b55fd19 | 3.18673 | -60.18328 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ba42dfac-b977-39ad-83ff-5c1581d2abde | 3.18782 | -60.18059 | 2024-12-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aff7e5af-2313-3217-9802-24fcd1970f51 | -2.64053 | -53.36613 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9df86dfc-b9d2-3e2f-b1eb-9ecb19ae7feb | -3.12178 | -53.80968 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99c358f3-37d4-32e2-a31e-1430405a2b7d | -1.25267 | -54.53955 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e2b614e-fa2e-3dbd-85c4-f4ac8f56c605 | -1.27755 | -54.55291 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5096fd14-7b77-374f-992a-c4b80e5c71bd | 1.09182 | -56.01267 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de82ce75-2af0-3c38-9651-fd580fb20cc9 | -2.26411 | -53.6128 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 102a76fa-8724-3215-af06-8a3225ad0335 | -2.45813 | -53.63066 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ec248a-0f57-3b64-b677-d0bdffff2b70 | 1.00423 | -59.46716 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e61326d-4caa-3278-a39e-b5c364726b37 | -3.26131 | -53.6262 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3d801e4e-4574-3cc9-ab01-204726fe680d | -3.74984 | -54.51656 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1890ada-7cc1-3209-b589-b1f3b9e81fcf | -2.91161 | -54.11821 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34aa394a-8b00-3008-8226-a628c68b7482 | 0.90875 | -59.44888 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 738ad634-88fb-3f92-84fb-c1474c7e67f4 | -1.44198 | -55.42682 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d15acb9f-2525-3b55-bb8e-ec71c739d7dc | -1.37731 | -55.88161 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42f2b983-c094-3175-a488-670a339c31fc | -3.29258 | -52.07458 | 2024-12-02 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f8a098b-5e25-3782-a2ef-003894fae112 | 1.10561 | -56.0048 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db33d51d-9635-3a63-8079-71cc4798e065 | -3.62467 | -51.53573 | 2024-12-02 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23922c99-6e61-319e-88f7-8ff423236a5e | 0.8628 | -59.68654 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7c565ad-cf5f-3fa7-bf56-775f47001198 | -2.2716 | -53.60422 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21bbe1a4-376b-37d9-a810-cfee3c041d67 | -2.7135 | -54.95651 | 2024-12-02 05:42:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b30a7e6b-b0e4-3159-bb35-6f326c39b04e | -2.26341 | -53.6174 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fab33c11-33b1-37b8-ad16-c52d42691e74 | -2.19665 | -53.77462 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6ed3e5fe-6cdb-3b36-8065-782b0c71cc0f | -1.73367 | -52.64159 | 2024-12-02 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 703b7f75-2735-3db5-80f0-3460bb86865b | -1.44252 | -55.42793 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a623e5a3-a848-3424-a252-1877b9273030 | -3.24935 | -53.92075 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42b184c6-8527-3a1f-b00a-58f9f18c51ee | -1.46242 | -54.5335 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 500146f7-88ec-309b-ab75-2777c8d47beb | 1.12345 | -55.99064 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d863134-0a52-32f6-91ad-d0da0d66b49c | -2.64192 | -53.35657 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 91baa029-de25-35cd-873a-88ed91622730 | 1.21192 | -56.00728 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6210b248-3a36-3d00-ab3d-74f829373644 | -2.44116 | -54.00056 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75dd969e-82fb-3ee9-a872-a54b704c28de | -2.78348 | -55.35945 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 859f4622-47f4-3b56-af5b-9ea5eb453def | 1.12078 | -55.98903 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6907a1b-c9c6-3085-a444-9cb9259a5550 | -3.50053 | -53.84147 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61018537-ea6f-3734-810f-ec334516db4f | -3.96186 | -52.1784 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 721fb531-1c6f-315e-9f5b-1c64ef4acf8d | -1.69553 | -52.63544 | 2024-12-02 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f39e81a-a45d-3024-b327-b2cdc7f8c971 | -2.45881 | -53.6259 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53ec5118-47a9-34b2-9681-707c15111465 | -1.24957 | -54.54863 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1d4ec63-001c-3893-8161-ba22fb189da8 | -1.45132 | -55.1938 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bdf0520d-0949-39f2-a0a6-c1965ad44984 | 1.0967 | -56.01188 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b2a2c24-cb96-30f5-b29e-2aeb8c630223 | 1.11368 | -55.99224 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a8a9c420-9e77-3880-b130-6647320c7ebd | -1.27698 | -54.55674 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c479edb8-0da3-3f1e-8571-ead8dbc69eb9 | -2.62855 | -53.36391 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e6717e92-8ac9-3b0b-bffa-9c71277ca35e | -3.63768 | -54.67695 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf66fc50-4b21-32bc-99b2-fd9435d84563 | -2.98036 | -53.88089 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| da79e472-498a-310d-8920-fb901cff5b3b | -1.0762 | -53.44872 | 2024-12-02 05:42:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 84e9f349-350d-3bc2-91f8-abe6a3d52935 | -3.05586 | -51.06385 | 2024-12-02 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42a5c33b-bf30-37a6-86a8-376853143bd8 | -3.42998 | -53.89295 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3316744e-ebbe-3d2c-a4de-1cd922b76ab5 | -1.40219 | -53.65403 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 61d68c1c-730c-36e8-be42-2d6da7f607ec | -3.77704 | -52.03959 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e893e32a-efac-3246-ad7d-d38b5781dbab | 1.20659 | -56.02542 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e356575-7dbe-3682-a4b6-463455746a39 | -3.77979 | -52.03269 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bfec747f-afe8-340a-979d-aea6ac86a8e3 | 0.90587 | -59.44783 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 951dff4e-f2ff-3915-b187-196c51c120d0 | -1.07247 | -62.64493 | 2024-12-02 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15d9a2e2-e821-36b6-a10d-a680428a949c | 1.12479 | -55.98281 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e65902f-dd48-3061-989a-eb8a17a682a0 | -3.25414 | -53.92987 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fed758f0-3dc3-39a8-befb-8ef07f0767b2 | -3.26675 | -53.63177 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 784b8d3c-0245-3a6c-b26f-451cb80668c8 | -1.34435 | -62.27443 | 2024-12-02 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d7ea51b-545b-35d5-b946-20429d2d71c0 | -3.50114 | -53.83715 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2394796-9e20-309e-9802-275ec1efc81a | -1.40541 | -53.65509 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cabdf90d-cf48-37d2-ae48-0e7a1414a363 | -3.96679 | -54.66021 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b18a057e-443a-3e65-ace1-a73a1172498c | -2.26707 | -53.6047 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97f6a824-a5ff-3122-988f-c7ddd0122f82 | -2.63858 | -54.19437 | 2024-12-02 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f743700a-ef1d-3146-9119-05dbfd44aac6 | -2.97776 | -53.8796 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bc00f55-66b8-3d72-afad-30683e4b54bf | -3.75569 | -54.51722 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a578bce5-0828-3eb1-b739-38bc264a3e56 | -2.73822 | -51.75282 | 2024-12-02 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8648b981-e223-3524-b04a-88b97d98d3d3 | 1.00035 | -59.46775 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86c96d69-9a17-33c7-8a63-e4828e48ed61 | 1.10701 | -55.99683 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 971944bd-f6f6-3e38-b972-0d4ed5c1975b | -3.74682 | -52.26881 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2de73fbd-a5b6-3c30-9044-0a3722c3b540 | 1.10476 | -55.99931 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46a4cb0f-a064-38b9-86b2-9f936b8ecb8b | -2.62893 | -53.35922 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4855bcbe-f076-3b88-a621-f0aabe016040 | -3.26743 | -53.62708 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0eaa090-94b6-3f85-af13-92137ed2d6d6 | 1.14031 | -59.52996 | 2024-12-02 05:42:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d69c9501-98e3-3697-8025-93ae20715d40 | 1.12968 | -55.98206 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6032b4e8-e4bc-3f9e-8b44-43ef631468e0 | -1.37501 | -55.88077 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 113bd106-e80d-38ce-9930-ff1f92043a63 | -2.40257 | -56.41694 | 2024-12-02 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e8109985-91aa-3de3-bb38-3e7fe5a85cd8 | 1.20892 | -56.00832 | 2024-12-02 05:42:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55c94174-adc9-32b9-a7b1-c90e114cc8a2 | -1.33259 | -54.97725 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b4dc1ea-9216-3765-b2a8-1dd603b96ef7 | -1.34493 | -62.27066 | 2024-12-02 05:42:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72575318-0cbb-3916-a112-a3b90c54cb1d | -1.27331 | -54.55414 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98bbc163-0cc0-3ffa-9e7a-555e8ec71121 | -1.57339 | -55.33664 | 2024-12-02 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4849173e-4026-349e-853e-dce746b3b109 | -3.77892 | -52.03888 | 2024-12-02 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 776e54b5-6409-35ae-b57b-28fb51718aeb | -2.75181 | -51.75498 | 2024-12-02 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8fc8868-95a6-38db-a692-393fa96e8977 | -1.25092 | -54.55082 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0f1a098-e85d-31e9-9cda-f9cce0f93a94 | -1.94745 | -53.34167 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c25a65db-4ae2-3ffb-b0b4-262adc978226 | -1.45901 | -54.96096 | 2024-12-02 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc0b3aa4-7cba-3f41-a314-ef82346ab55b | -3.96101 | -54.65931 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b8dc71-caa0-34fb-a143-c41b383b6c95 | -3.1158 | -53.80836 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 28f501fc-b76e-30bc-b5a1-ef806e874b59 | -1.27195 | -54.55207 | 2024-12-02 05:42:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b21e4687-c248-3608-8116-f1b95397293f | -3.64398 | -54.67396 | 2024-12-02 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce0a8c4b-c5c0-3278-996b-b0d3794d7655 | -3.25475 | -53.92572 | 2024-12-02 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 593b0dc8-2cab-37de-98a9-50654df325c0 | -1.72731 | -52.64057 | 2024-12-02 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac2c4f4-633d-35a4-bcad-105bfebaee30 | -2.26504 | -53.61868 | 2024-12-02 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README73.md)
