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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04f023ad-f97d-31d4-a8b1-049a2eae8053 | -8.67429 | -40.40724 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9edc817a-bec0-3fa0-aefd-44f31a624fb0 | -8.67415 | -40.4064 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2a0cf31-ad9f-32b0-b5ad-15eb9f082c57 | -8.66947 | -40.40262 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| e37841b4-a9bd-353b-ab67-f3c351012c9e | -8.66882 | -40.40617 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 0093acf8-1feb-3676-8c77-7f996d5f0eee | -8.66869 | -40.40534 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| dc19a657-8eaa-3c6f-a6c2-5b15030cd294 | -8.66819 | -40.40968 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 469661bd-9efa-3d7a-a9c1-a45679126c2f | -8.66803 | -40.40884 | 2024-10-13 03:21:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 0f70029f-e289-3dd3-a2eb-80c6503f9b21 | -8.07847 | -40.80169 | 2024-10-13 03:21:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb230c58-a3ca-353a-9f8a-4e5f6b281bd9 | -8.07523 | -40.79812 | 2024-10-13 03:21:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4c4ad09c-7c91-3236-84eb-0a2586565586 | -8.0745 | -40.80206 | 2024-10-13 03:21:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2ba7f5b4-ea25-3fda-a501-38c143ba2158 | -8.07278 | -40.80072 | 2024-10-13 03:21:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d3963e6-89f5-38a7-8f9c-58527a9ea546 | -3.72383 | -40.71582 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e482706-aa84-3022-877a-b7be2743ec41 | -3.72303 | -40.72042 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0ed2c559-5ede-3a43-8451-26208a335583 | -3.72225 | -40.72495 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d9b6a727-e73a-34b6-b089-f2aaab708bc8 | -3.71776 | -40.71483 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 16d0ea23-8c7c-32d0-89ea-f74b7eaa37b1 | -3.71695 | -40.71947 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 417f7b18-b880-3d16-98c4-0f303a1c76ba | -3.71616 | -40.72407 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 64e8bf94-904f-3f1e-8a2c-586398446ae4 | -3.71169 | -40.71382 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2e08bc33-2ef7-3b42-9ba6-3d8d27d17c9b | -3.71162 | -40.71236 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2493ebd1-2cce-3cb9-b53a-ead5f6e86fff | -3.71087 | -40.71854 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9bc68342-8110-3360-b9a5-b41767463aba | -3.71084 | -40.71705 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30837689-af62-38e4-9f82-2a9f19544787 | -3.71007 | -40.72314 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 1c45f79c-c2d5-3b90-a577-c7ba6f269c14 | -3.71007 | -40.72173 | 2024-10-13 03:21:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7695df4d-220a-3764-8690-40600dfe2458 | -6.38908 | -41.59587 | 2024-10-13 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 57b3adac-7689-3b74-a117-e11cf687afd0 | -6.38823 | -41.60064 | 2024-10-13 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 741d23fa-59c4-3683-ae06-2b8da925c88d | -6.38737 | -41.60542 | 2024-10-13 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| cd2352f3-73aa-3b2a-99a8-bb8bad0c8d20 | -6.38295 | -41.59473 | 2024-10-13 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9166c576-fa31-34b5-9564-605f47539f3f | -6.02338 | -40.44656 | 2024-10-13 03:21:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| acbb4b48-7d6e-3dff-a3d3-f47336560727 | -5.63899 | -40.69733 | 2024-10-13 03:21:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ac632ff-06dd-3cd4-ac92-c65a056659e8 | -5.63826 | -40.70143 | 2024-10-13 03:21:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 27c3e9a5-c340-3f1a-a6ae-e5e212303621 | -5.12716 | -41.69289 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| fbf6e0a3-bc0e-3c93-8556-b0e9f57a7cf1 | -5.12458 | -41.69071 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| b38d5825-d278-3688-a07d-f26a7610bf3e | -5.12371 | -41.69569 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 397e0439-f798-3253-b320-9e7119e10630 | -5.12091 | -41.69146 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| f3738aaf-5eee-3913-8456-706d24c74b34 | -5.1192 | -41.68432 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab5c173f-8606-361d-ba33-6fec7eada7d0 | -5.11832 | -41.68936 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c540be90-577d-3daf-8468-9d090a06c4e2 | -5.11743 | -41.69445 | 2024-10-13 03:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 69659e07-3669-3376-9d5a-d4a1dc60ce04 | -7.34346 | -41.11648 | 2024-10-13 03:21:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 61e1e295-f1eb-3904-ae93-4d04d31b94c0 | -7.34271 | -41.12067 | 2024-10-13 03:21:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d162e9fa-94c2-3e8c-995d-f68a087e4a54 | -8.06022 | -40.94197 | 2024-10-13 03:21:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| deb041b4-ed66-386b-b144-58f4338a543c | -8.05946 | -40.94604 | 2024-10-13 03:21:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cfe81183-da96-342d-ba55-fc100665d574 | -8.05452 | -40.94078 | 2024-10-13 03:21:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| abc5c381-752d-3290-bf99-cce48380df7d | -5.13093 | -42.87915 | 2024-10-13 03:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2927f26a-b7b8-378a-81db-e2c04443e06e | -5.12982 | -42.88523 | 2024-10-13 03:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a49df10-4d7e-3762-abd2-61a05ed47234 | -5.1295 | -42.87769 | 2024-10-13 03:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e319684d-7223-3424-bb42-923e24ef4791 | -5.12842 | -42.88379 | 2024-10-13 03:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d540782-5684-305e-bd10-4c16cd9e3ec6 | -7.73459 | -43.29947 | 2024-10-13 03:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ab40899-ede2-3246-82fb-ec9c40c05480 | -7.73169 | -43.29936 | 2024-10-13 03:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d50b23a1-a16a-37d8-a5d3-3da82eef158e | -7.72793 | -43.29827 | 2024-10-13 03:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f055744-1f89-3333-88da-bf99f2d9a600 | -7.72502 | -43.29819 | 2024-10-13 03:21:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f8cfe7d-8208-39a1-abdf-4e5fa4f7da3a | -7.70833 | -43.20325 | 2024-10-13 03:21:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4f4343be-8e51-347c-996a-475cd2266daf | -7.70626 | -43.19686 | 2024-10-13 03:21:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cfaaf1b0-d5c9-385f-8c6f-d4ef7c7b2a38 | -7.70516 | -43.20253 | 2024-10-13 03:21:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1e81c9fe-3207-33f6-817e-749b5f0f9491 | -7.70277 | -43.19636 | 2024-10-13 03:21:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ed4f1bf9-6895-3767-93c1-68be3e1042c7 | -7.21843 | -42.28731 | 2024-10-13 03:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 95c4ae23-6482-3b0d-88c9-13b06295e9e8 | -7.21215 | -42.2859 | 2024-10-13 03:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6ab94b76-e90b-3309-8f1c-b56b0a198dad | -7.20672 | -42.27993 | 2024-10-13 03:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2e9d482a-6b9b-3c89-a65e-099e58d08b04 | -7.20582 | -42.28483 | 2024-10-13 03:21:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 26bb45b2-5aba-391a-b74c-51221321adaf | -8.13643 | -43.01448 | 2024-10-13 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f56b61ec-dcf2-3de6-9216-98cfa3c99bf8 | -8.13536 | -43.02006 | 2024-10-13 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 16007b40-749b-33b5-b718-f4cc8af9422a | -8.12449 | -43.00644 | 2024-10-13 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7f5919b3-7bd9-36bf-9c7f-87f2eedca81a | -8.12342 | -43.01202 | 2024-10-13 03:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4342c922-f7a2-3f88-9129-631bda4a315f | -4.82719 | -44.07634 | 2024-10-13 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36094da3-1fb6-3059-82b6-3d011a3deae1 | -4.82653 | -44.07893 | 2024-10-13 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8f2493fb-6e2d-3dd0-9b46-1f1f297d0abb | -4.81998 | -44.07473 | 2024-10-13 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10932642-7a4e-3443-b26f-6b743e0c5d9d | -4.8193 | -44.07737 | 2024-10-13 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e14e954b-b627-3614-9fdb-c57429012076 | -4.81861 | -44.08214 | 2024-10-13 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ce73961-8e05-3953-9a76-474a54419c7f | -4.09095 | -43.92803 | 2024-10-13 03:21:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c27f10b-4fe0-3b72-947b-1cd976612005 | -5.38293 | -43.51419 | 2024-10-13 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be928b6b-560e-3d65-9e41-1eaaa901c503 | -5.3759 | -43.51312 | 2024-10-13 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02f3555d-d315-3aa8-b003-40a271d16382 | -7.96933 | -44.51371 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4e6bcac6-4372-36ba-b55a-48f2463e32c0 | -7.90172 | -44.62231 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b994430-d7cf-3c3d-b02a-45a5de4d246a | -7.89821 | -44.613 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d2227f58-d50f-3470-abd0-dee5af271886 | -7.89687 | -44.61982 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 05f648d3-4c73-387d-9b3a-01c8158e722b | -7.8959 | -44.6139 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a23f1ca5-ba55-3f1a-9be0-0785c2653a74 | -7.89459 | -44.62078 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b22112d-d436-33a1-aeae-e1f2b077f7c7 | -6.5393 | -44.42977 | 2024-10-13 03:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44a2a957-5b63-3e5f-86f0-d754e8deded9 | -6.53778 | -44.42989 | 2024-10-13 03:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c29598c-c70e-3786-93a4-0d24e8a2e462 | -6.53334 | -44.42184 | 2024-10-13 03:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ba68c899-d91b-3e4e-b198-f1c3cf84d5e2 | -6.53213 | -44.42811 | 2024-10-13 03:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1e523b19-8a6c-36c7-822f-1d12c9c5390c | -6.53175 | -44.42208 | 2024-10-13 03:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7ca9d645-a703-394d-9dc6-70a0e3b1ec00 | -6.53057 | -44.42842 | 2024-10-13 03:21:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93b2417b-7531-3b8b-a060-b955cf8d4c27 | -8.06227 | -44.81455 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 722b0980-ac7a-3cb1-9c64-0a9c78057c2f | -8.06001 | -44.82624 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99d843ae-7465-3a31-abe7-3207f9143d19 | -8.05283 | -44.82467 | 2024-10-13 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 702ec803-9965-3cb2-b31b-44a59af03c3d | -10.7077 | -44.49076 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a1400796-654e-3001-bcbf-81a41802a3ac | -9.5768 | -44.38519 | 2024-10-13 03:23:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 22278f63-6465-3cb0-b312-7f32948505d2 | -9.57549 | -44.39178 | 2024-10-13 03:23:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 50f1605c-8562-3526-a4a1-01ec217bc9fc | -11.12534 | -44.95263 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| af08132b-f321-399b-b84f-74c11cbf1e68 | -10.94322 | -44.66315 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| eb016b3e-4b76-3670-9cf0-45458e6895f1 | -10.943 | -44.6629 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 23bb99e4-6e45-3c3f-ab5f-0b65dad32c91 | -10.94191 | -44.6694 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 6cf3c74d-669a-311e-83a7-d6c904cf8c8a | -10.94174 | -44.66916 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2e3f0cbc-ce9d-37df-87b6-ad84981dd85b | -10.9338 | -44.67414 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3ac1932c-74a2-3089-839d-c85e3c3b5bb8 | -10.93248 | -44.68044 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5801e8da-47d3-33f9-920a-7a1523cca8e8 | -10.93239 | -44.68018 | 2024-10-13 03:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d6b0aca3-4896-3790-a672-f4fd843d12a3 | -12.71726 | -40.21584 | 2024-10-13 03:23:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 199596cb-cb60-3e03-9d5b-3edd1d20cd97 | -12.71669 | -40.2188 | 2024-10-13 03:23:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1b57eeea-6134-330f-be1a-ca04793725a1 | -13.28279 | -41.90747 | 2024-10-13 03:23:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6fcce446-36bd-3626-9e34-43b703b44300 | -11.79616 | -38.26314 | 2024-10-13 03:23:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README35.md)
