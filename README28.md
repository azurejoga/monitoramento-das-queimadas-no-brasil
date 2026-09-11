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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ed81d37-ce2e-3db5-87f1-f38ff489b441 | -8.63575 | -66.51014 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21c61ccc-cf47-334e-92bc-cbafc2970ca1 | -9.28872 | -65.8071 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92953237-309e-3c28-8f29-2c0492bcd8ff | -9.31884 | -68.20229 | 2026-09-11 05:29:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ad1b7106-bbbd-3891-b3c1-b30ec1dc64c5 | -10.36046 | -48.13712 | 2026-09-11 05:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad68cdf0-5aaa-35d9-ab03-76c15fe71f35 | -10.99025 | -60.65735 | 2026-09-11 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f5adac5-e5d7-3eea-842f-8552a545eac6 | -14.60055 | -48.86241 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 815ca74a-604a-3f14-8d4d-f5cdd3e4eb99 | -9.19078 | -68.21391 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a0ef0be-af0f-3324-b214-bce62630a361 | -7.75761 | -66.90492 | 2026-09-11 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9080c43-ecef-3ca4-911c-26c7646852a9 | -11.4002 | -55.23966 | 2026-09-11 05:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3000c2f-0962-3c77-8744-d25e72d7a0f9 | -9.41247 | -67.41206 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2be92c0c-91bc-37df-b9ba-c2a644c648de | -9.18567 | -68.21297 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7eb1e42-0a56-330a-bc14-d527de6e3029 | -10.19359 | -68.76744 | 2026-09-11 05:29:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65cfd6ba-06ed-3004-a801-50190678774d | -11.80436 | -60.45733 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a5ba4eda-e24d-30d6-9aa1-159b247ea8a6 | -10.05462 | -46.28907 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 604d6408-6768-3a34-9908-4cb50b70b73f | -9.39757 | -65.85542 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9dc2cdb-ea99-37b2-8a6b-5d1e0aa2b2c6 | -9.1558 | -49.98613 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e442f16e-2504-31a4-8252-8878403c0ed3 | -9.23593 | -65.59174 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ad6f550-1e64-36ea-a80d-ed40162f9a23 | -13.50567 | -48.5598 | 2026-09-11 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be2eed1b-a860-3051-abfe-4a705b8a3381 | -9.10457 | -67.69323 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4a48cbd-d650-3ac1-ba61-960cfd70fca2 | -10.0591 | -46.27065 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f573ba1a-1b99-311a-ba86-ee7f82c890f6 | -8.65188 | -69.79477 | 2026-09-11 05:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2eab3f8-c43e-392b-8684-f794333b97c3 | -9.23091 | -65.56973 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0dab396-5e51-32db-b26e-f564d2c4465d | -9.01407 | -65.44691 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7236e1f1-c7f1-3936-9b81-484069248d74 | -11.81491 | -60.45544 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 577e473d-4daf-3f8c-bea2-5f8c3a7f7e50 | -9.15808 | -66.05984 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ac71003-4fbd-355b-a626-77c4ec7cafe6 | -9.00765 | -65.43344 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8125943d-4ada-33a4-9924-8994ccf4075e | -9.17157 | -49.95112 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4cdc384-0fc9-377c-b9ad-267d8e7d15b2 | -9.17835 | -49.94911 | 2026-09-11 05:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 374b5961-3d6d-3c77-8cb4-10d16b21a2e9 | -9.30178 | -65.88965 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4331e8f4-26ba-3e26-9ea6-13ea200aae9c | -10.35995 | -48.1413 | 2026-09-11 05:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb380d7f-3d6a-37f5-b8e1-b527fd90c911 | -9.39685 | -65.85959 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff4096de-1cdf-36c6-a477-b5d0b42826dc | -8.97998 | -65.39164 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48d48dbf-fbcc-3e7a-abd4-ad5074097af0 | -7.84652 | -56.5813 | 2026-09-11 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcfe7b47-156b-3b0d-81cc-6a1f258a5448 | -9.48982 | -68.49741 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c7c9439-9038-30be-96e9-622f89b589dd | -10.5425 | -51.35434 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dd38335-734a-3c01-beb3-9f2386745057 | -9.1506 | -64.27782 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bf67c98-0fae-3c49-a326-aae3bffd4717 | -10.66864 | -49.07946 | 2026-09-11 05:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39455494-c7c5-3779-ab85-bec7e7f05d79 | -10.54803 | -51.35217 | 2026-09-11 05:29:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c758e338-6b5a-300d-8896-75ee4809baf0 | -9.28801 | -65.81123 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d7e63b1-2cc7-3ba3-9ff6-e881c382078f | -9.0793 | -65.49004 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 069c7d8c-023b-3dad-8ab0-a0d85d51b00c | -10.05613 | -46.2761 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f58bca50-b78e-39c0-b5db-c6f042b2a608 | -10.98968 | -60.66088 | 2026-09-11 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f382d451-e742-3741-837e-e87713c93837 | -9.41478 | -65.86185 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5385e2f7-4947-3c8a-8c99-a9c07155b727 | -7.63281 | -67.25743 | 2026-09-11 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9f05c7-8cdf-334f-af54-2f8b6a0e185f | -8.50112 | -50.14913 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80fdb82e-facf-39da-9a92-33db45ae53f9 | -11.80769 | -60.45788 | 2026-09-11 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e732c43-2ec0-3f2b-abfd-5d2ac452b0bf | -10.05983 | -46.26473 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05919764-82c2-3a45-a5ae-79ae0dfd5f48 | -9.4012 | -65.86034 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad0bbd2f-0343-3cfe-9a02-707ec917fd09 | -7.75668 | -66.91012 | 2026-09-11 05:29:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b51b02b1-f33a-3232-8db1-f2062413956d | -8.93639 | -66.84389 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8679fc6c-c7cb-3a3e-b4c7-0d9f05ba0358 | -8.63868 | -66.52053 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 17d5987d-263a-343f-976f-405eec344e84 | -9.0412 | -60.44176 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 312abc1b-00b6-3467-ae4e-1a4f5effa3e9 | -9.02521 | -65.40789 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e3d235-b897-3be9-9367-295d6460088c | -7.24662 | -59.51975 | 2026-09-11 05:29:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7cca529-b2c2-3750-bf16-6ef3f68c42e0 | -8.58344 | -54.5522 | 2026-09-11 05:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c14694-54fe-3193-8de3-e43f144a9cd1 | -14.60409 | -48.8488 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b18422fb-4658-30ab-be40-04e76ac7d5e4 | -9.63171 | -49.01576 | 2026-09-11 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c9b4aac1-a916-337a-8613-2d834a3959eb | -8.71246 | -49.61614 | 2026-09-11 05:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 300c9503-7644-3e48-8df0-33341c1a9b05 | -9.41043 | -65.86111 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 336473b8-b986-3893-97f4-ffddc01d292c | -9.42363 | -65.86002 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1c570d37-a4cb-3060-b652-5068980e9608 | -8.50064 | -50.15256 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| daa6ac40-3de4-36ff-af7a-ca055c2c8480 | -10.48578 | -48.64807 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 130dc142-27af-31ce-9a26-0e7bec140b53 | -10.46678 | -48.65028 | 2026-09-11 05:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d867b53a-6f1c-3f09-a1e7-1f05b8c08de3 | -9.22314 | -65.5892 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b529b519-0978-3c84-8231-ecfd1c75c76c | -11.51284 | -61.03155 | 2026-09-11 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c525e813-7529-31b5-bbc5-4f7dbb48edb8 | -11.41134 | -62.12524 | 2026-09-11 05:29:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 505aff23-db60-3c97-b66a-ac1e1aabb3b7 | -14.58199 | -48.85511 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 792f331c-0928-3a53-a55e-a3e907d06c85 | -9.75828 | -64.94608 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43125db0-d311-391f-bde7-7a80b0526eee | -9.63764 | -49.01659 | 2026-09-11 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b3b13ff3-dfa9-3fd4-b140-8eede9b9eb4d | -9.07079 | -65.48853 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edde45c7-d0c9-3423-883d-d644ae98a752 | -9.41912 | -65.86265 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d3830c3-9505-379b-9fcc-df53ff46468e | -9.0408 | -65.41888 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 273dcd54-422f-37cc-9392-154ef0d7e553 | -10.78583 | -45.94869 | 2026-09-11 05:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eba17d1a-97cb-38ac-8f2c-40f38d08d0e3 | -9.48467 | -68.49635 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86797510-62b1-3025-9b2a-87809d2d05d4 | -9.03724 | -65.41415 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1d6f5d15-a6cf-301f-bf74-61ccbd0e9440 | -8.50817 | -50.15125 | 2026-09-11 05:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a7e3551-bc00-32ba-ab8d-b0af549fcbf7 | -8.70634 | -49.61909 | 2026-09-11 05:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| df1c5958-3f31-3262-9c55-11331bc70fe8 | -9.41986 | -65.85853 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 86bf711e-797e-3243-a482-2ef1880a3fb3 | -9.10953 | -67.69635 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 54f60502-5258-3da9-8747-762f73f570e2 | -9.10562 | -67.68983 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 86d38e85-540e-382b-8be7-745263ad3b1e | -10.06168 | -46.28978 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9efeec67-9f79-3951-8c75-8253ae6a2b3e | -14.61058 | -48.84853 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c0298da-90a6-3c5c-a828-480519b5d345 | -9.14053 | -67.80735 | 2026-09-11 05:29:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4055f2de-532e-327a-8e4e-c99cc6d3e39c | -9.48904 | -68.49667 | 2026-09-11 05:29:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b79efff8-e500-301c-92e4-7037aa559c30 | -10.10543 | -54.92778 | 2026-09-11 05:29:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4ff021e-1528-3a70-be01-91ae43ac3b7a | -9.75485 | -64.94169 | 2026-09-11 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bc4a532-610b-36dd-8f12-78db36d97adf | -9.50004 | -66.79278 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f757028-9146-35fd-b30d-216b909ade16 | -10.05754 | -46.28341 | 2026-09-11 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 772ef912-c223-35b7-a24e-ba53eb0d9d95 | -8.65264 | -69.79072 | 2026-09-11 05:29:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2776ee7b-ae5a-35eb-9e8a-f6efd0bed877 | -7.90981 | -56.63496 | 2026-09-11 05:29:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e15639-f095-3649-8d6f-ff847456403b | -8.64335 | -66.51316 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b639328b-648a-3373-9f5c-fca32f8c52db | -10.18601 | -59.63271 | 2026-09-11 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cdfc4c6-1cb9-31ae-ae95-a5450f78dae9 | -10.95886 | -49.64332 | 2026-09-11 05:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 259231b7-cca5-3ec7-b4ab-99a744655b7f | -9.22384 | -65.58516 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 176239dd-30df-3d0a-9f72-e7abdbae5eaf | -12.01374 | -61.84398 | 2026-09-11 05:29:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de274d77-341d-313e-8205-2453fc0ced45 | -9.07584 | -61.02462 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73e175b9-d56d-376e-a87d-52acc43f3a52 | -14.58399 | -48.85565 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42248cb1-4187-386a-826d-35eeacbd584e | -8.65969 | -66.5015 | 2026-09-11 05:29:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6346a9ed-195e-34db-8810-ada2fedece95 | -9.07863 | -61.0288 | 2026-09-11 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31dc290c-f3e9-3c24-a997-0ff24356c155 | -14.59034 | -48.85671 | 2026-09-11 05:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README29.md)
