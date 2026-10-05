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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57fb7bd3-a90f-3ced-bdea-7d7cfbdab226 | -9.48195 | -67.66756 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 491ff937-4c0b-3596-a01b-ab5911e40ddb | -1.67192 | -55.0654 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f1780011-a9fd-3cf8-820d-0c0db2da6199 | -2.75693 | -57.65272 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0ed55189-3fa5-3a31-9a0e-a2db2286b30c | -9.30715 | -68.04334 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7e9ed9c4-33e1-3f63-a48f-54ab60644312 | 4.22185 | -60.71156 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| be06d2ac-b5be-3939-8b95-af2c9fc06738 | -8.83588 | -67.38897 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 63faca2a-081d-3529-a34e-cdcd308d616b | 1.79221 | -50.62416 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 46bae110-c72a-310e-a90a-10d9697b7e8f | 1.74667 | -55.60506 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 539519e6-6bc8-350c-93a6-33b42b0823eb | -10.64395 | -68.59708 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 81c88e68-c127-324f-947b-6a7cf7b2e937 | -9.55464 | -66.04935 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 42638a1b-c595-3294-89ab-fbdc8f260529 | -9.66496 | -65.02224 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 96b6efa7-a3d5-3c02-b82e-f6b15ea705e1 | -2.77886 | -57.64936 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fe191d4a-772b-31b1-af32-75cef1aeef31 | -1.33217 | -55.27928 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1a51a26c-c755-3313-84f2-56eca146da49 | -7.21807 | -55.18802 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 99e7ade7-979a-33be-a62b-e90ab1d7e471 | -10.62868 | -69.24359 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5cc72c5c-f89e-3a22-bb8c-774b02d2552f | -8.75391 | -69.09465 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 40.9 |
| fcedb78e-9a55-38f7-b50e-ba5f141eda3f | -8.57874 | -66.82011 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d82f0be1-fd5a-3180-9280-b61dc346b204 | -9.08571 | -66.08885 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ceab41f2-2820-3a84-90fc-f9a6619003ef | -8.63177 | -69.4995 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 890587bc-b6ff-3d24-98ca-c901114ae009 | -2.7752 | -57.64992 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4327bfb2-df94-36bf-ac58-546f7ef5f55b | -1.47534 | -56.74766 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a21c85f6-8b25-3663-a31f-005118b175cb | -9.99284 | -68.55232 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d243977e-2dd9-3452-9781-fae24441a948 | -9.28793 | -68.25786 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b04c4e24-3397-392a-8ff7-a24542421bcb | -6.46003 | -55.47097 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0d280a11-79b3-3735-9273-dce2bd4ecc1d | 2.0868 | -50.91013 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 64d573a7-ebf5-37d1-b50d-c55db4084cce | -2.55045 | -57.98677 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3a142e07-f624-32c5-a411-de8185b6a7cd | 1.98023 | -60.61847 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 0f9a04bf-8a8d-3efe-97f1-b1262c78fbc8 | -8.62657 | -66.99866 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 952d4871-1035-38f5-a850-20557eb8acc9 | -1.42724 | -52.72945 | 2026-10-05 17:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35e803f3-29b3-359f-ace4-089ed2fe5b25 | -9.38718 | -68.331 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 20776a59-0557-3cf0-ad09-a479ee58ff35 | -6.46086 | -55.47604 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| aa0959cf-3cc2-3b63-91ef-1dd3e7e7b048 | -2.77588 | -57.65418 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 02018d3b-ec70-3e98-bf39-4679c6dffb28 | -8.93695 | -68.77109 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| caf72571-cbe0-3876-b144-acf5240d1cde | -8.44513 | -54.97872 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d3b34554-c24d-3579-8bea-e855b15d5f6a | -9.94823 | -69.00172 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| acf28113-0cb9-3ff1-a6e3-66eae729cd76 | 4.2857 | -60.33406 | 2026-10-05 17:37:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2f52d2cf-c2ee-3339-a8f6-7a0315b33f5c | -10.67358 | -69.10294 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 99fc6534-8e70-3da2-8dda-b4a6ce020d95 | 4.21788 | -60.71475 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 79488c17-a8fc-363c-b9eb-6dc938674177 | -9.29315 | -67.63187 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b85d26d4-2f78-3120-9b85-866f26b349ce | -9.15584 | -68.24089 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| e70fa2e4-d352-3d9d-979e-eed68fc43c49 | -10.42108 | -67.9816 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 7100696d-a953-364a-a65b-228491c1e74f | -1.26455 | -54.55832 | 2026-10-05 17:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| df0e0080-1033-3958-a176-5cd61fc71b96 | 4.21049 | -60.71743 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ebda04c0-e612-3106-b94e-0c0946e029ab | -1.3312 | -56.41126 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d21f99d6-aba6-3fcc-9a71-0d67f77bcda2 | -9.07904 | -70.03758 | 2026-10-05 17:37:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 4750ef2d-57eb-304c-af7e-c21dbbdf7884 | 4.20874 | -60.70584 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7fc32324-90d8-3198-bfaf-9c5348529480 | -9.34886 | -65.32192 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| caf37b5d-f0b0-33b0-9527-b7cd72095a9d | -8.64294 | -70.04901 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.5 |
| d4a6ca6e-dc3e-3bc3-97eb-64d80d2ededc | -9.4788 | -68.0373 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 864c7e50-db4b-354b-87ba-ccfcdc9f7af8 | -9.12103 | -67.83163 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 35f087ea-b977-3e17-83eb-280571031134 | 1.79243 | -55.54443 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 160e90f9-a483-3d44-a527-a616fac44384 | -8.87997 | -67.00055 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.8 |
| aa0c5e02-edc7-374a-aef2-96b71748532a | 4.22241 | -60.70787 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ab1da43f-8c6c-36d7-8037-8a7bbfaf42b7 | -1.70272 | -55.05735 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f5ceb1fa-e68b-35bb-9b88-37397848ae40 | -10.12159 | -69.30676 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c0c7cf7f-3510-3aa8-85b6-ac8b1a8f22ca | -10.49104 | -69.43109 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df6c0b16-0d66-3175-bc1e-f4737bcc41fe | -10.55308 | -69.26043 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6625f0e-e5ef-3b72-978c-ac85f717a936 | -2.2683 | -57.091 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a506391-2302-344b-8fa3-6ba9715185e1 | -9.41155 | -68.84432 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a91c5445-b86a-3bdb-a98a-eee5ca296e7b | -8.66414 | -54.54139 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 067519b7-7693-3ae5-8955-6dea7b4c3aae | -9.23113 | -67.89099 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 917b8771-e018-3c79-a1b0-b5341016c63c | -8.69476 | -69.42018 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2bbb7663-4e3c-3402-b163-723735d46a95 | 0.43909 | -60.52937 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 88c76313-07c5-3a5a-89e5-2beac1b8c9a4 | -9.56948 | -66.02473 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 19a348a7-a56b-394f-ac43-01b290e4c7e2 | 4.0528 | -59.98628 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1df904d3-d68f-3a18-a2f0-80aeeab9bf77 | -7.23003 | -55.18626 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b51038a7-1cfe-30ee-ac15-17ceb4678719 | -9.40178 | -68.56157 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47c0e978-2507-3265-aa79-0fb2cc69dbb8 | -2.7729 | -57.659 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| fbb9f043-42e2-32a3-8850-0476962815dd | -6.45836 | -55.4608 | 2026-10-05 17:37:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 302024a7-1b12-3407-be5c-67f75a253979 | -9.12492 | -67.82228 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8ee50229-86a8-3bf9-aeaf-20d7817594b0 | -9.97988 | -65.05316 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 20545a72-e46a-3fdb-9804-9c125ed3ffff | -2.87862 | -59.20673 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0b117eea-63e9-3029-abf4-782695af3b77 | 3.57778 | -61.33594 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20326c9d-d82e-3493-b8e0-ea8c70287f9f | 4.05807 | -59.99922 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| efd5088d-89bb-3799-a4d8-1b2c3bf8f56e | -9.33842 | -65.8419 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b4f45f4f-1021-314a-befb-642f72dfd156 | -10.27572 | -68.75497 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c6a195d-dca8-351f-8d3f-5cf0b61ef2d5 | -8.71384 | -61.39333 | 2026-10-05 17:37:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| d48f5162-8254-3937-b8a9-7f940b988ff3 | -9.28481 | -65.64366 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb0d6192-b9cd-3344-a904-61c8a02c6a32 | 0.87888 | -59.5944 | 2026-10-05 17:37:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 18c2729d-6299-3082-97fa-a0d889c4a476 | -9.04479 | -66.05429 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 77e7a437-a52b-32b6-b20e-1f33bd77d0f7 | -9.13524 | -68.24376 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 29b784bf-a30a-3ad4-921a-12dad3c0823e | -2.76261 | -57.66493 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 67f6be50-5d62-307e-baee-f9190e41ad30 | 1.28085 | -51.12643 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9036f5ba-5163-34fe-aa04-ce5577d6049d | -10.42067 | -67.97852 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 60c16ed3-8085-3cc9-b8dc-9f47298eeb69 | 0.44136 | -60.53694 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e9f36df4-f494-3231-bede-53887f0e9930 | -9.13686 | -67.75772 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1daaa956-c1f6-3d68-8e6f-86a742436655 | -6.64419 | -55.3207 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 24f19a92-5f04-3c69-8b74-d14d2cadc13d | -10.64438 | -68.60052 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b1135a46-a307-32b1-82e6-8a03db0b82b1 | -10.35945 | -68.4166 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 318063cc-6f3b-3d42-881a-fba1ad7687dc | -3.61743 | -69.43877 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a5f3230-ddd1-3ea3-a9ee-4bbc01850020 | -3.08166 | -59.16025 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d282641-18f8-3916-81fc-dc2def9e4f46 | -2.59883 | -57.47595 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c57dfeff-91fd-37ac-a00f-0abefc3472c2 | -9.47878 | -70.45142 | 2026-10-05 17:37:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 91ae5178-5e2e-3a59-b05e-9443875470b2 | -2.19151 | -56.84072 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f05bd5f6-c2b9-3198-9f12-653c87a865d5 | -1.43053 | -52.72808 | 2026-10-05 17:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 193e3170-cba5-3562-a615-d4e338414f31 | -1.9745 | -55.67538 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2c565e31-1600-31f8-805f-cbf608fc2389 | -1.42355 | -55.08899 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| fcaa8d91-83d7-324c-aee5-98ec6a827d9c | -0.33292 | -52.02519 | 2026-10-05 17:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 22f46987-271b-3a60-85f7-6765525c8d5f | 3.56174 | -61.35159 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 529fea46-089b-32ea-a5b8-20c56a5c4d0e | -9.53874 | -68.66784 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |


[Clique aqui para ver as próximas entradas](README149.md)
