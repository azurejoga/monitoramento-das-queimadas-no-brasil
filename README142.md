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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe3e7474-61a3-3ac7-a29b-cd51fec7a1cf | -9.88689 | -64.80782 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a2461e7-41a0-3d7e-acfb-9000d263f6a5 | -9.88675 | -65.0048 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0b865a9-bd37-310d-bacc-21a029f5ba30 | -9.8863 | -64.81189 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96b10956-2135-3a3b-a0f8-7fb2899af4ad | -9.88616 | -65.00877 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d9923dc-6299-3b3a-a9f0-4ea65c2807ee | -9.8857 | -64.81594 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c42b82d1-a1fd-3222-8c39-12a6a6301e4d | -9.88511 | -64.81999 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb827df5-34e8-39eb-b505-3cabd19e4b03 | -9.88334 | -64.80728 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 041b0101-8819-3f4b-b640-b3ecaa8a0a9b | -9.88275 | -64.81134 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62ad17e4-2ba0-36cc-a6f7-585dfdde3780 | -9.88216 | -64.81538 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d5e5915-4faa-37f5-9381-0da53e6d2b36 | -9.88157 | -64.81943 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c60615b8-3be8-3653-8da4-216aa2006265 | -9.8792 | -64.81078 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57968084-88a8-34be-8885-399be2ee1939 | -9.87861 | -64.81483 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbec22e7-b5e1-3ae5-8391-dd39ae2f6021 | -9.87802 | -64.81889 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3171bcc2-774c-3d65-845c-a21ebff4f9cb | -9.79217 | -65.05592 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e6d6f79-c0cd-3019-b1ba-5a39a73e487d | -9.77463 | -65.0533 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 384ab614-00cd-3d41-9256-66a0c067e161 | -9.74225 | -64.88275 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75882848-2f6f-30f8-812a-6ffa7403b33a | -9.73872 | -64.88222 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecc9327f-bb9d-3beb-9787-d44682d915f7 | -10.8014 | -65.17077 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23723dbd-d939-381f-a5fb-b381dfb6725a | -7.78795 | -66.92849 | 2024-10-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fe25f31-3607-37d5-9230-25f513a25a1c | -9.30273 | -65.84257 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d54fad-2cc5-308d-9ea0-64d50c61a3c4 | -9.19717 | -66.09473 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a1a3cf5-4a02-3a59-88a8-15c830c7e58e | -9.19381 | -66.0942 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73ab37a2-3a36-3fed-a9bf-da4f3b07dd8e | -8.70715 | -67.00259 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12a1451b-6a2e-3ea2-9049-8af052e2dde7 | -8.70438 | -66.99859 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fac78349-4cfc-3b04-af91-f4ab6efee40c | -8.70384 | -67.00207 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75460eb5-ebc1-31af-b904-6f0529ad5882 | -8.70053 | -67.00155 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be29c181-efa7-35c1-b173-b80fe268c316 | -8.70047 | -66.98014 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ab7acab1-8254-3d6f-92c2-becf205349aa | -8.69668 | -67.0045 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39e3d0c-5dfc-3932-aec0-16426f3286da | -8.56645 | -67.07685 | 2024-10-12 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03adc0cb-7bd0-3aa3-b396-0d9d08d410dc | -8.49967 | -67.09126 | 2024-10-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 851bbc94-4f7e-3005-a238-4e68ab6a2002 | -8.47843 | -66.9668 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 00cd481f-ed7c-30b2-befe-cdcc121ed500 | -8.45619 | -66.97723 | 2024-10-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7e5713d-c35b-3396-b394-a1fdada1e2d6 | -8.45289 | -66.97671 | 2024-10-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 002d1835-779f-3b47-83cf-529a52e394dc | -10.09107 | -67.14265 | 2024-10-12 05:48:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce34e0d-b82c-33ca-a288-d2473b3fa718 | -10.0883 | -67.13862 | 2024-10-12 05:48:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| affc8735-3125-36da-a49b-ac4caf8e6b5c | -10.08775 | -67.14213 | 2024-10-12 05:48:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b0edc3e-23c7-3bb8-8aa0-d560a94f98ca | -9.88414 | -66.79268 | 2024-10-12 05:48:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe9e36fa-2c40-3e36-a43b-db26174c9832 | -9.65343 | -66.43695 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f8c9ae8-ac7b-3af8-a687-04b13eaaaa75 | -9.61131 | -67.14944 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b327cc19-5ef8-36a9-9dc3-c5f8fbb48f7a | -9.61076 | -67.15293 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd4c270-1e65-33a3-9059-50754169b4dc | -9.44511 | -67.14796 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ff74f1-f9f0-3b6f-a63c-749a87c8e3cb | -8.3939 | -67.24493 | 2024-10-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aecfbcbe-4505-3d2e-a0de-7d8f649f4f89 | -12.61561 | -55.21066 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b30a3d6-ac9b-3517-91e1-2c4fc01014e2 | -12.61492 | -55.21683 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4931a121-a8f0-34d9-a7e9-02260dc8fb82 | -12.61153 | -55.20588 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0e6b6eae-002b-3d8c-bd2f-bf5cdafe2041 | -12.61086 | -55.21216 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1bb3ba34-47dc-3540-a64a-01d251402ddd | -12.61021 | -55.21831 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8fbf2c37-0aae-334f-8a21-5b2379ecdf33 | -12.60957 | -55.22438 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6f3d8cb2-f881-32a1-8faf-eda52c10782e | -12.60954 | -55.20361 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cfcd8638-ebeb-3a96-a70b-b72478cf6e6f | -12.60893 | -55.23045 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f40ddc51-f327-386c-be1f-bbe9b2cac5b3 | -12.60883 | -55.2099 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5901345c-0e1a-31b9-95c6-d068de26ce9f | -12.60814 | -55.21606 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5495de81-b970-36f0-8f38-ef41462aeefe | -12.60746 | -55.22209 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9d4de7a5-d306-3232-ad34-81cf33a231b3 | -12.60678 | -55.22821 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5ecd1a35-fda8-3d82-8263-fcf01a93e179 | -12.60281 | -55.22346 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eb14ce62-c177-3f6a-a64d-de3ce9ad9bf4 | -12.60216 | -55.22964 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92bfe497-4b4f-3ec1-867e-c379c7d8faee | -12.60001 | -55.22737 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cc52318c-20e0-3967-a8ef-2eeddd43c744 | -12.44916 | -54.56628 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a11eced5-f76d-3b9e-a6d9-1cf4bdef957e | -12.4484 | -54.57319 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df9e0b4c-46fc-3380-badf-625be48a5ba3 | -12.44807 | -54.56048 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a784d031-45a9-39b6-ab41-ad9ffa250cc4 | -12.44735 | -54.56752 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 06950054-da5c-39c8-b7a7-dca83127b9b4 | -12.44288 | -54.55857 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32c9ac3a-3dcc-3ef2-8df1-999c2a6cbce5 | -12.44211 | -54.56564 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51d9adf1-5b7f-3310-b778-2b10fce725d2 | -12.44135 | -54.57269 | 2024-10-12 05:48:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bb210ce-486e-3a4b-941e-dd2025ab0966 | -9.57637 | -55.80491 | 2024-10-12 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d175780-4d05-3164-ae17-097c5c6c5527 | -9.57574 | -55.80993 | 2024-10-12 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b18cc10-36ad-3bba-9a47-92f8af79813b | -9.57373 | -55.80208 | 2024-10-12 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 99e89de0-24b0-3907-a4a1-db0961e19acb | -9.57313 | -55.80714 | 2024-10-12 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 03743720-5fb3-30a5-b8fc-916434b0b38b | -9.57006 | -55.80412 | 2024-10-12 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f52cfa92-7ef8-3e41-a282-9a6810061800 | -9.5694 | -55.8093 | 2024-10-12 05:48:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a1ed8461-5d39-335b-9897-137413727c8f | -11.9262 | -56.91984 | 2024-10-12 05:48:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 682d7426-b43e-31d5-9342-98f7a6b76cd0 | -11.92067 | -56.91445 | 2024-10-12 05:48:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5208a57b-3140-3973-b044-f2f330173279 | -11.92012 | -56.91924 | 2024-10-12 05:48:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beb87675-1b82-365c-b298-37dcf1043c82 | -11.91406 | -56.91843 | 2024-10-12 05:48:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54c08877-fae3-3759-a980-4ea6be00a479 | -14.32692 | -57.59963 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2f6ac6d-5e8a-367e-8880-8ce2e78fa28f | -14.32095 | -57.59888 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50342f09-d26a-31ea-ad43-144e7bff8a6e | -14.31594 | -57.58943 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf0b4bb7-e494-37c5-803f-941934e6649b | -14.31546 | -57.59377 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6751b501-321e-336a-8cfd-f3894be2b9f5 | -10.42182 | -57.2288 | 2024-10-12 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ba5a779-c5d6-376d-82b4-37fb1e1027f3 | -10.4213 | -57.23298 | 2024-10-12 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57f4d4a1-87a0-330c-ad03-78010874a0b9 | -10.28917 | -57.71378 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1629ef31-8aff-38e6-a3c7-72d1b6e896f0 | -10.28868 | -57.71757 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fdf9ba1-420f-38f0-8fa9-1cb265102628 | -10.27173 | -57.71567 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 424ce870-e6b3-3c3e-89c9-bed67ca4cc2f | -10.27127 | -57.71926 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95c56c9b-68f5-34e3-89d7-eeb54bb34f18 | -10.12447 | -57.76535 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e2a00d0-92f2-3501-a231-b785991bae15 | -10.124 | -57.7691 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71cdbf5c-7b37-3652-86db-0a349ee222e9 | -10.12352 | -57.77289 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa4fe91c-b96d-3452-ad10-24c43a14a2eb | -10.11935 | -57.76074 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dd0e02b-021e-3fb4-b4cd-96aa0bad6694 | -10.11887 | -57.76454 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a3f7f00-8e54-3b9f-acc7-a2a64aafa72e | -10.1184 | -57.76832 | 2024-10-12 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef7361b2-9edf-311d-8618-a39ef9a994e2 | -9.31779 | -59.28422 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 33be6ddd-4b0c-3ed4-9911-d6b67e3a8ea1 | -9.31278 | -59.28359 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 200184dc-c716-321e-95b1-5a1ba37bb6d6 | -9.30777 | -59.28289 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2977fa44-7ac0-35a1-9221-4ab1adf1e9d3 | -9.30738 | -59.28579 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9ecca9e-4509-369b-af1f-d4fbedf1f7e9 | -9.78161 | -59.01912 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc5ce431-d9e3-310a-b937-8c22fea97d86 | -9.78121 | -59.02213 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ad207ec-acb3-3d43-a118-b6f3c7e1a8b7 | -9.39273 | -59.33567 | 2024-10-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07332e37-8e54-3bd1-9327-1c6eec7c3e76 | -10.2932 | -58.99738 | 2024-10-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 45d7002c-ccce-3dd2-9812-81a7421a2a6b | -10.65401 | -58.40512 | 2024-10-12 05:48:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aad29847-a7a4-3adc-af3e-28a99da4a7c1 | -10.65355 | -58.40862 | 2024-10-12 05:48:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README143.md)
