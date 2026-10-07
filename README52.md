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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17c422a8-2fe1-39df-b2c5-3838e29cfed5 | -3.61165 | -55.28849 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b828eefe-3e2b-3a77-a2c3-097d6a55bb55 | -3.28868 | -54.02937 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5e9a1414-1836-31bf-9485-c365c27ce8ea | -4.24149 | -49.98004 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef338a1e-01d1-3b9e-9eb1-e364604dfd3a | -4.84138 | -49.37061 | 2026-10-07 04:19:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93664166-aba7-36c2-b46b-99075f69f138 | -3.56987 | -54.65657 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8264585d-b183-3955-9d63-285889573dc4 | -7.83571 | -44.18636 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 379a2066-c98a-319f-ae9f-c58401fb0909 | -4.8149 | -46.82687 | 2026-10-07 04:19:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10c697ca-1fdc-3ec5-b3e4-5e88271964ac | -3.504 | -54.65568 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b97fcb6-7fd6-3073-a5ca-c1c6aee187c9 | -3.17164 | -50.43679 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1f3d96b-bc15-3a33-8eb9-5b1893df5eb3 | -2.7623 | -54.08154 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 099c99ff-3717-3df0-87a6-f63b6b2deae3 | -2.93488 | -54.1508 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 192bc5f1-bd0c-3860-8adc-14c3d4031242 | -3.51502 | -54.6681 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f3b7e374-7c14-3e2a-be6f-a2111f01620c | -4.16166 | -55.16216 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a6a669d-ecf4-3fa1-988c-f05412350409 | -3.27221 | -54.0513 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c2dfcfb5-66e8-37c7-a4df-4a8b0407b9ff | -3.28521 | -54.04194 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e1ec85d9-89ae-363c-8b2d-8a700fa274bb | -3.03848 | -53.94347 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82eb811f-9798-3b82-b6ef-90b6f23ad114 | -3.80094 | -51.03379 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 452ae135-f714-3564-a7c6-9b841d1ce5aa | -4.15505 | -55.16139 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3845ee33-6162-3e8f-8188-19c27c7c002b | -6.44128 | -55.03134 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0c6a278-21e4-3845-ad99-76ad4c14c186 | -3.53994 | -50.09058 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00956ebc-c6f4-3f4f-af38-d4dcb68a6b90 | -3.05865 | -54.22334 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6fe1c6d-166c-389c-9c1a-d38ba4092e1d | -3.27183 | -50.40827 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6a8646f-fa31-3563-bd9a-14afd6b0faba | -3.05828 | -54.15158 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca21699c-5247-3796-a8ed-01da8ce92f28 | -3.26932 | -54.03076 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 99d9a2e4-458c-3bd4-84b6-7d4ae0f56397 | -1.2907 | -54.57123 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 26817914-bcbe-326f-ac10-62edd1399c40 | -3.10902 | -51.24557 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77720ff3-41f3-397c-8926-f8431c455386 | -3.28437 | -54.04673 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b2005640-017e-3a11-9f70-157c7fc6f31b | -4.76801 | -50.8149 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ec9a722-850a-3089-8d50-b01ca206f238 | -5.67375 | -53.49426 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 992087d2-ffa4-38d2-b2b1-ee6798cd6218 | -5.04733 | -44.75333 | 2026-10-07 04:19:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c845b91e-5af7-3bf5-a98a-5dbecd33cf44 | -3.83658 | -50.3099 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74838718-7537-3869-ac6c-284908a11c18 | -2.8407 | -54.07487 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e81535b-1c85-3dee-9a01-e1ad7d4ca9cb | -3.27461 | -50.4375 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aac7d946-1b24-3869-b242-bb983a9feb78 | -3.0957 | -54.15878 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e4a0029-51a4-3666-9512-c27373cd4d7a | -3.4985 | -54.64947 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b2523ef-9261-397c-98ee-5f476017a019 | -3.26461 | -50.40778 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1ec5e05-c05e-3045-9e11-8dff18c368f8 | -6.37315 | -42.91165 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| aae63cf1-3a1d-3883-9ce4-c72ea0e349ec | -3.57985 | -54.31821 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 478aeb40-5bf0-3399-87bf-62d184c9103e | -4.13704 | -54.92544 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8799e411-e78d-3584-95a4-f4334dd3080d | -3.06107 | -54.17246 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15114f43-9daf-38a3-af6c-3867f4a93de0 | -7.76297 | -43.81074 | 2026-10-07 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d9511dd-0739-3428-b02e-e9749f6d277c | -4.23683 | -49.97927 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 165cded7-a872-3bb4-87ac-19e3f9886eea | -6.15187 | -51.74134 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a168017-8503-3e03-95cf-33cabe99fa17 | -3.73437 | -51.21354 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8fd4127-d4b8-3442-b63b-329e10075d1d | -3.10196 | -54.15984 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a566dfd9-cd29-30c8-a122-495d1cc314a5 | -3.3573 | -50.76683 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8294081e-8f08-39d5-a625-330f6f4a16f5 | -4.15191 | -55.14665 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3294323-7e7b-3db5-81dd-63885881a7e6 | -3.2776 | -54.05716 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 743a8632-e842-35a6-98e9-6dc7e955c6b4 | -2.78424 | -51.67653 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3380879c-2d9b-3875-ac2f-b5c70a20260b | -3.28352 | -54.05153 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad63e216-ab5a-3ba3-9cda-f7edf96b49e7 | -3.18976 | -50.56984 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7e6df79f-b00b-3d09-a1c2-cd72a3981f46 | -1.29379 | -54.56328 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 23563659-12e1-306a-abd5-e15899e0f0e7 | -5.01758 | -50.94498 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 501920e5-e1b0-3051-b343-58084924d9d5 | -5.24753 | -47.94017 | 2026-10-07 04:19:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b88fa02-a109-34ae-865c-ddc53137e2c4 | -6.94801 | -41.49163 | 2026-10-07 04:19:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| de08c1f7-1028-316c-99a4-53152dedd28c | -2.17453 | -48.14079 | 2026-10-07 04:19:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 92fee2bc-97d9-3716-8c58-71e220f1cd9f | -6.22853 | -46.45081 | 2026-10-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4691220b-f9d3-35b3-aaee-8e6c0ef9a161 | -3.0179 | -53.91531 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a1615680-3165-34ff-9bb0-d6b6da89995b | -5.89092 | -45.54826 | 2026-10-07 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 239def4d-5c69-3c1e-a0d8-a0cad412fdfe | -3.84945 | -55.98349 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0902a232-e015-3222-aad2-56f41473b40a | -5.97937 | -40.94138 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 1b56ac04-6707-3bb1-8bff-3901ff167381 | -3.12505 | -53.76845 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfa01e84-55c7-3b93-9c08-0dd81d6ddc3f | -7.19273 | -44.29825 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3fd9d8f-eb59-3c28-bc47-249bedd5dc11 | -3.10661 | -54.17022 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5c5262e-83a6-3665-bad2-e005a667fba1 | -4.82573 | -38.6897 | 2026-10-07 04:19:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 102c2956-fcf5-3587-bd15-306d970c29d4 | -2.94827 | -54.07141 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8003538e-4c87-3ac2-9d34-10f028ffdf92 | -4.9275 | -55.87662 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da8f043e-a75b-354c-92cc-b1fd03e839ab | -3.74409 | -51.21832 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 575fc79a-85d4-37fb-bfba-d2eae0ec9d44 | -3.84713 | -55.99656 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0d9536f2-03ea-32d2-9f67-ea99efaf4b53 | -3.10115 | -54.27746 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3f8c03d2-e27f-3b03-bf58-fa614e475178 | -3.27677 | -54.06205 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6158fbe1-a593-3c7c-887e-076a346f6c22 | -6.99524 | -45.11814 | 2026-10-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb8f71ed-c937-3b85-9e47-3667aef5b17c | -3.85521 | -55.99114 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f06f16b5-1464-37ba-a916-05d7dddedd7b | -2.99415 | -54.12686 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19cf39de-52e0-356b-92bb-9e216ed1d052 | -3.1476 | -50.44775 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06ec99ad-0e8a-393c-b11d-b9ae550dde15 | -3.22502 | -53.88602 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afd1d30b-52be-3f45-a676-41b1e090d060 | -3.27228 | -50.43645 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7211c3f-7e9c-3bff-8ba2-76a17fd582a5 | -1.1907 | -54.2144 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ce68178-904e-311d-a7b6-22a027acb22c | -3.13359 | -51.03275 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 141213aa-3521-35f9-9240-085154468454 | -1.28506 | -54.56454 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f768eecb-c480-3df7-a7d0-7188f9ef7695 | -4.31639 | -50.78136 | 2026-10-07 04:19:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ac21c2c-0084-3915-9e50-b1610e1b620e | -8.21892 | -46.8848 | 2026-10-07 04:19:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80020b16-aaac-38b0-a70d-68f54a124873 | -2.95732 | -51.05034 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d1b9fcf-2549-3741-9f83-c470ec42862f | -4.39898 | -44.25294 | 2026-10-07 04:19:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41d4c1fc-66e4-3d42-9a1f-8d99affab845 | -3.54252 | -54.656 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b0b17930-30d3-3635-aa11-550d4b4a8370 | -6.21042 | -52.83987 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eea72bbf-b47a-3883-8bb6-d2d016ec1acd | -7.19938 | -44.29935 | 2026-10-07 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62f1124a-6429-315b-a3fd-f42b2e6d6473 | -4.75315 | -55.66122 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| eeb0894b-638d-3e21-8072-8498b238aefc | -3.23888 | -53.87862 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3c9792f-59dd-3972-9468-52a9e28b219e | -6.44315 | -55.02135 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 52cdc175-a859-339f-b96c-b77158c69e5b | -3.09318 | -53.73406 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9bf96656-66a1-3918-a74e-3d365d73b9e7 | -4.13792 | -54.9203 | 2026-10-07 04:19:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e7857219-7048-335f-8172-055319e5229c | -2.76595 | -54.09772 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 23616540-086c-3e1a-a6ef-20bd746786e9 | -3.03885 | -54.26238 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 266cb79c-ad8b-3dea-98e5-367818a54866 | -3.52338 | -54.65211 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9b7f9710-fcd3-3ade-b3e2-2736138e0e1e | -3.15028 | -50.44391 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71d3bdac-52f6-3451-b15d-2c3c01a96847 | -4.11329 | -50.82503 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd83c512-ce7a-38a0-9d16-e11917bd5929 | -4.25066 | -51.0446 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bde30698-c555-3e3b-88cf-133c4f023967 | -3.67676 | -55.95782 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6ac93148-baac-3a37-bace-f5dfceee53a5 | -6.90228 | -45.02037 | 2026-10-07 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README53.md)
