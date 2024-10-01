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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68cbc883-aa8f-3143-bc1f-872dcf407b00 | -21.53074 | -47.89851 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64f63625-8844-3f00-9362-bef2054efefa | -21.58291 | -47.88717 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 37abea62-1a89-3066-9a63-9bfb2bd4f82b | -21.582 | -47.93184 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 748d69a0-ca1b-3158-8b01-4819f733241b | -21.58173 | -47.90484 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a7d3f1dc-1786-3b21-bdb5-3e05027aad95 | -21.58137 | -47.89344 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 39ecc317-7241-3f8c-bf05-f449e98832e7 | -21.58042 | -47.93812 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c6443de-a606-38ed-a0f5-effa34b84953 | -21.58015 | -47.91113 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e6d416c2-030e-3625-acf0-b07598b6f748 | -21.5787 | -47.93309 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5142de8d-0230-3df1-8aa8-ce942860b91a | -21.57857 | -47.91739 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b41b1908-86db-34bd-b5f9-85486dadfcbf | -21.57829 | -47.89048 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d86cd336-27d4-37f0-b1a1-6d87b2abb021 | -21.57717 | -47.93932 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c1b7009c-fa0a-3388-aa03-3b2726134f62 | -21.57672 | -47.89671 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 55d71db7-3419-3dee-b8eb-f3cb026c9ef8 | -21.57634 | -47.88524 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 00314e6c-9bb1-35fa-8fbf-9a3fdbc78b08 | -21.5748 | -47.8915 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 19.9 |
| ca6a542f-30d9-3aa7-befd-45fc9698a150 | -21.57365 | -47.92491 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 650602ec-68c8-37b7-91b1-b7a7ce2e4f45 | -21.57326 | -47.89776 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c260a6d0-bb5d-3c46-8c34-5de08f08bc23 | -21.57059 | -47.93735 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51b665cd-697e-392d-a5e7-f64ac6446613 | -21.57039 | -47.92179 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3b583cdc-612d-30ef-8c7a-66c4f562e0aa | -21.57023 | -47.91008 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f4b0aaec-0dbc-3ee3-af1c-d12f8caecefb | -21.57018 | -47.89469 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| fe4b53e0-30f9-3176-b84c-79b7f5f5bbd7 | -21.5688 | -47.92811 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 16b93303-d79f-3782-83b5-f0439c34a3e3 | -21.56867 | -47.91644 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fb32114f-0c97-3298-84a8-df3ad9a0c013 | -21.56864 | -47.90075 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.3 |
| c6bc95b6-c874-3281-98e2-2c823d691efc | -21.5671 | -47.90684 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 476a121d-913a-3789-85ad-91cb47ae6f26 | -21.56708 | -47.92291 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5132b930-e7f9-38d6-8b03-8451cffcd7a8 | -21.56679 | -47.89539 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f4176779-d84a-3314-81b3-34711f54043b | -21.56554 | -47.92915 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d4dbbd56-adb9-3ccc-9605-0f94229b2116 | -21.56551 | -47.91314 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 36e4bc22-066f-357c-baee-c9a41fa6d9c5 | -21.56331 | -47.8809 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| de9e3b96-0a02-3b0c-967a-992fd6cee2af | -21.56226 | -47.926 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0659a6a3-8b8d-3f02-8468-e87f16eb8963 | -21.56216 | -47.91418 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 05fc9da5-be92-3962-a5b7-59830b7d2ff1 | -21.56074 | -47.93202 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62260061-bb6c-3f74-b3be-315d94ff14ea | -21.56034 | -47.89293 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5a86af82-dc04-368d-bb28-d00f875931df | -21.55884 | -47.89902 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| df62a1c5-81c1-33eb-aafa-38e1c9c1f62a | -21.55754 | -47.93296 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2de9ffdf-36df-30c6-83cc-77cbf8ba8a13 | -21.55564 | -47.91198 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f797599-3fdb-36ae-8523-9d0528154242 | -21.55397 | -47.91879 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d881f803-ba57-34ba-807c-595c1f8cf14e | -21.5488 | -47.88257 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9d3bd0a3-f445-303d-8b5f-99ceae563c50 | -21.54725 | -47.88882 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8bd15e2-ffa1-3d83-a790-08c2f0dcf0c5 | -21.54566 | -47.89525 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e211df88-35ca-30b5-a5b0-3931859ea885 | -21.59213 | -47.84955 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| cddbe28d-9cdb-3bec-9cca-b0b5780d3bb9 | -21.59198 | -47.82153 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 289.6 |
| d84ffd63-8b00-34e8-91f7-e529108a6776 | -21.59178 | -47.92108 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4d20cd9-af24-33a5-8d64-28b53d91cc3a | -21.59148 | -47.90974 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7071666c-fc65-3b40-84ac-0e6da833c72a | -21.59148 | -47.89416 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d4b37e3f-239d-3ad6-8fa9-baf4a567b985 | -21.59132 | -47.79562 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c95f6201-a2d9-3557-9064-08e2120838a2 | -21.59118 | -47.86734 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 66de0dff-90ed-397e-809f-a4aa329b2dc9 | -22.3575 | -49.33741 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.2 |
| 632f968a-d110-3344-9cf9-37bc9d2963e1 | -21.59104 | -47.88274 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 64e68a33-5986-31ff-9ca3-bdc99f8754da | -21.59092 | -47.84039 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 6ce7387e-5c61-3706-9aac-9cdc9c3cfe98 | -21.59059 | -47.85582 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| fe75340d-8f66-3382-b03f-7c4f18e80634 | -21.59039 | -47.82798 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 289.6 |
| 62b7c589-af98-3be2-90fc-f4c8f37f6cdb | -21.59019 | -47.92737 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e3826da-1417-3a25-91d3-d8680654a5d7 | -21.58994 | -47.80124 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5150cd90-fe47-3cb0-8d2f-332857152339 | -21.58993 | -47.91604 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d0fb155a-eb99-3230-8430-925fe6fd279d | -21.5899 | -47.90043 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 674ecd54-9250-3c3b-b48c-89390ed1ccce | -21.5896 | -47.87359 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| fccc37bc-e6fb-3bde-82d2-6cd9f8dc8d4d | -21.5895 | -47.88902 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 65d78526-0cb9-3bc3-87e4-411f7fb69849 | -21.37592 | -48.48774 | 2024-10-01 03:28:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d610c1af-5131-3795-b4dc-efac3644ae0c | -21.58943 | -47.81843 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 366.6 |
| c0c8ff41-96a9-3bc2-9b11-26bc6057b5a4 | -21.58933 | -47.84671 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| a554eb03-3749-33db-bbb3-77918aa12a8f | -21.58905 | -47.86213 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c75f8b0d-151d-3218-90dc-d577b5ba1f00 | -21.58876 | -47.83464 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 48d02eda-57d7-332a-af38-80896c8ebe74 | -21.58861 | -47.93367 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6c51a19-39d0-350e-ad1f-a54006d5dd4b | -21.58857 | -47.80683 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 510dbb34-90ec-33b7-8297-d70cacc7f70b | -21.58839 | -47.92236 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fcae14ca-3fb3-368a-a1f2-6d19883ba7b7 | -21.58833 | -47.90668 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2ab83662-a4bc-3b78-9050-560be29ae850 | -21.58804 | -47.87981 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 45b1fe04-b091-3b90-af01-5987f799c624 | -21.58796 | -47.89531 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dd7d9cd0-20a2-389d-aa6c-6058dc44b589 | -21.58781 | -47.82483 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 366.6 |
| 7b94819c-202f-375e-a836-7281b1a63530 | -21.58775 | -47.85299 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 88ccc28c-38e9-3711-8c53-b11981ec3485 | -21.58751 | -47.8684 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b380f5d6-de44-3176-b911-790a1bd39927 | -21.58714 | -47.84124 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 40cf410e-7718-3dff-9864-5bc8c516aae1 | -21.58713 | -47.81266 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 25fac094-6198-3e0f-a43a-83571f827bae | -21.58685 | -47.92867 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 720c51cd-ac43-3e8c-96cb-3e017f0e7a46 | -21.58676 | -47.91295 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0fded9b0-ce68-3370-b622-64eabc6a6ef8 | -21.58646 | -47.88605 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4e4e6010-ee5b-34f1-9786-6adb8a60d316 | -21.58642 | -47.90159 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 79b5f6f7-8396-3076-91d2-ea8830b675db | -21.58616 | -47.85926 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a828202a-d4ff-362e-84dc-231a2c3bb0a2 | -21.58615 | -47.83143 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 3be26ae5-3a34-3f9f-96a7-c99521e71816 | -21.58598 | -47.87465 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3fd6a243-3405-3cca-bf1e-f9c0ee39c291 | -21.58559 | -47.84756 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 82ecd547-c357-33ae-bf60-f5acf5796fac | -21.58557 | -47.81904 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0202843c-5019-3f5a-9d70-064e615197a4 | -21.5853 | -47.93496 | 2024-10-01 03:28:00 | NOAA-21 | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a284e496-9c0d-3f95-8d28-9cd11f29d437 | -21.58517 | -47.91926 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| def3fe1e-e07b-3bbb-9161-b4e77019cfd7 | -21.58489 | -47.89231 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5c916bd4-fa69-3bc0-bd46-f0430c9a9fd2 | -21.37767 | -48.48083 | 2024-10-01 03:28:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c005f6c4-76ed-3e99-8687-2887bf4c1677 | -21.58488 | -47.90786 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1c1d635f-783a-37c9-a3fc-2852c6226493 | -22.35935 | -49.33032 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.2 |
| 780aa6b0-1344-38e3-9b41-40de4d7cf062 | -21.58479 | -47.79366 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b6e6716c-ee3f-3e46-a312-2756b1cbc775 | -21.58459 | -47.86553 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 08b18b3a-96de-38a8-affa-9ec8d814057b | -21.58445 | -47.8809 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6dd5eaa3-e66e-3d64-a753-f316af78771f | -22.35939 | -49.31539 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 016e2a21-545a-3086-8ce9-94d647ff3e7b | -21.58442 | -47.83826 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 55577de2-f42e-3d7c-b9ca-e71bb38b9b0f | -21.58403 | -47.85389 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 06850c36-3351-3f1f-8c52-97fec4181e16 | -22.36054 | -49.35462 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 3a267d19-db56-3bfc-8305-21ca0a1cb785 | -21.58397 | -47.82552 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 30f0dcca-c460-3cdb-b0d7-a31bc803ed95 | -22.36121 | -49.32318 | 2024-10-01 03:28:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| a1c008cd-3659-339a-968c-ff775efee325 | -21.58358 | -47.92555 | 2024-10-01 03:28:00 | NOAA-21 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54c123ef-27da-3a39-a6ab-041ff8d1df66 | -21.58334 | -47.91417 | 2024-10-01 03:28:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README41.md)
