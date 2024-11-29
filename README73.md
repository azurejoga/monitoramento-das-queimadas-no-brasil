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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01a6dc8b-9721-3902-9db1-220946a7eb22 | -3.49675 | -53.7993 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 56b6676e-e1bc-3505-9498-222407f7def0 | -2.5901 | -54.09359 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b7c928c-bb6f-31b6-aa90-28d7fd30a7fe | -1.26609 | -51.59118 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db40d1b2-1d94-31c3-bf87-f5859cc41e18 | -2.93168 | -53.88984 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d92188aa-17af-3a3e-8b72-f8c51f8d479b | -2.36763 | -50.42186 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e616fd2-8687-3e05-b2e2-77cc2c1183aa | -2.69615 | -51.98941 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d22feeea-56cb-3601-98b6-e0ab08511889 | -1.70443 | -52.64077 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5d5e9b75-f726-3385-9980-d440be2ace2e | -2.38535 | -48.60316 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 835914c4-728d-3a64-afa3-31a6fd0f841d | -2.87692 | -46.86688 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 987bfeb3-07f9-3afb-8e04-8d60c0d5d159 | -3.677 | -52.11196 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ee45813-b772-395f-955d-2059965e831a | -3.10881 | -53.75549 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c57810b-be0a-338f-99f9-5abe68dc4683 | -2.96249 | -53.88755 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25e97668-b4fd-3d89-b18d-7856a89d3d97 | -2.05698 | -56.07586 | 2024-11-29 04:57:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cbabf6d6-dcf5-3ca8-b853-d651ce8b05b0 | -1.70068 | -52.44719 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d1d57d6b-d512-32ad-a0ed-8b72e6ada6b1 | -2.84686 | -46.81973 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3481aa95-6cf6-3325-9665-6ad646ff491d | -2.53485 | -53.98959 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e78abf8e-28e4-35ef-95b2-07ce4475195f | -3.96393 | -46.91244 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 001b7bf4-351b-30a8-8b35-fb9e1068d666 | -1.0376 | -53.18531 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f64290fe-0bf6-3b7e-a3b2-3f36185e1022 | -2.83714 | -54.07946 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cc11c12-2382-31a2-bb14-c2dea74def40 | -2.10527 | -50.34344 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c33fb41b-16c5-3225-ade1-5468778a6112 | -3.23005 | -53.41597 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8d7137e-18e7-3f12-86e9-cb543d173696 | -2.64124 | -54.28907 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad38e000-4f86-32d5-ba89-678d4e239b80 | -3.10247 | -53.8178 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8dea8b2e-d3ad-37c3-88ed-9a599c08a966 | -2.29169 | -50.59086 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4437f67-3ab3-3d22-b8e6-ba2fd1b6eec5 | -3.02953 | -54.02471 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67bf0320-8069-3b3b-9118-22e48a809e8f | 0.97777 | -50.12907 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bc6fdd7-3bd8-347e-8b71-49d8aa3939cf | -2.72182 | -48.67517 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe8c2ea-7622-3251-8ae7-aec832475eda | -2.5693 | -51.83651 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 282e4aa8-270a-3333-9524-4391522775d8 | -1.23345 | -51.8004 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99ebdcbf-85b7-30c8-b1bd-b216f6e6f8db | -3.91928 | -53.66478 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baf5ce7b-f751-399a-9c63-b9938e0be8d9 | -5.2274 | -44.91333 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c9a1339-6ef1-3bb6-afa0-b570bbba8f34 | -2.91324 | -54.11596 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 595241f5-2da4-3517-8b34-304408bc1e7e | -1.42454 | -55.25666 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78e0a90d-a8f8-3e4f-952d-f11ad793ab4e | -1.72312 | -52.01754 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1f2a18f-6ab6-3fb1-b0bc-75d868de57c2 | -4.14036 | -50.65276 | 2024-11-29 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cc5cb6b-f058-3cb6-a53a-8370c57e2c4f | -1.24917 | -51.78816 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7761489-551c-3c6d-a62b-23362494a1d6 | -1.79178 | -52.73575 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e61720ee-38a5-34c6-8d45-5b14177dad93 | -1.58658 | -52.23966 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61b64e87-5360-3763-a5f1-fdfc9a6618af | -4.47982 | -48.18999 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 2100b17d-fde7-30a7-ab0d-5c8ea1c31177 | -2.76713 | -54.0722 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e92109f-8a3f-307f-af8f-0312a0021a57 | -3.09234 | -54.03441 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aefc4d1f-cc0e-3bb7-b512-d902113b3e97 | -2.97517 | -53.89303 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdcdeca1-95ff-32e6-b13c-b867b4271571 | -1.24631 | -51.629 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02ce6627-752c-3770-bde2-ce50bc7d2604 | -2.45828 | -53.69567 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9834441a-aa68-3ef4-be37-64298c6047e2 | -4.17273 | -48.63153 | 2024-11-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ebab60f0-dc7d-302f-9592-99c1a29b384b | -1.48358 | -51.9593 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d371070-39fc-3cf5-8535-de9a77c0eda9 | -0.98334 | -47.88292 | 2024-11-29 04:57:00 | NOAA-21 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64f09ec6-f767-3f8e-87fa-9a703a475cd2 | -2.57564 | -51.88596 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0546ecf-e96a-3cb4-b1ca-4201825bbb9c | -3.50165 | -50.4956 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69c463d4-4531-3c5e-81e0-0f6a7cb7f9ef | -3.27088 | -53.30596 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e02fd47-c373-3c53-909b-ade21c4f70ab | -2.10103 | -50.34702 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aa697f6-dc6e-36d1-8d3d-1639d430fb59 | -3.49653 | -50.45615 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8df55a64-fe63-30a1-a7e9-d1711fdab08d | -3.07263 | -51.25665 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1155094d-f9a6-30d8-b664-ef07ebcf5a51 | -3.07712 | -54.56789 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60431f3b-3282-3b57-b0c4-03bb782e64c0 | -2.3908 | -55.29602 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ae04868-c3e1-3638-a0df-bca66dac41b7 | -3.09719 | -54.02872 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1831cc45-2bed-397c-a4ac-3164ddc93ff7 | -2.76081 | -54.06691 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dbd4544b-dc28-301d-a2c3-c70d0d3ee149 | -2.77354 | -54.00975 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54b7b2f1-d8c6-3f67-853a-a9c5eb906902 | -2.57813 | -53.66902 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87a44113-4497-3744-97fd-eb437e6805d1 | -2.53671 | -54.04282 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17a8582a-69e6-3622-a0e7-614ea634e75e | -5.71804 | -43.84055 | 2024-11-29 04:57:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 762f04e2-2ba0-3dd7-ba42-57cdefbdd27b | -3.14727 | -46.59549 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 859417ce-2412-3299-9658-d55a10fa056c | -2.98509 | -53.89455 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 028f1c64-b94c-3049-9abc-d0b221fdece9 | -2.87841 | -46.86504 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e66fd61b-3545-334a-9e2f-3b87149e7248 | -3.283 | -48.76373 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21e53d8c-a1ec-3828-8b3c-3e1660639920 | -3.48999 | -54.66822 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fcb3a6c-e91d-343b-be40-73a789424b72 | -1.62875 | -52.49328 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a1deb3a-bf06-3ed4-9ba3-57f7b45b6df7 | -3.35357 | -52.07057 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e699c5-18a5-3bb1-94be-33dd40e37e60 | -1.53299 | -51.61655 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5b37f358-c620-3e04-8a3d-b5e635c8f29d | -2.44513 | -50.42113 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d4d2d42-816c-33cc-af2a-f1755ef1a26a | -2.61515 | -51.80991 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b4f568f-029d-3df8-98b1-a1231fa80768 | -2.41378 | -53.8506 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d70e157b-2c1b-3aeb-a588-98a17f8a0a67 | -1.45464 | -54.37136 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e572110e-634c-3725-9584-d473f7598007 | -2.44469 | -48.40935 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 048251e4-a8f5-3de8-8ea4-251d812d3e2a | -3.04283 | -54.0479 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6b3dd66-31ec-3223-90ed-005bea60f231 | -3.30324 | -50.49379 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51a2a548-8a8c-3525-b36e-4089b27de41a | -3.53017 | -50.38285 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2a8d8e0-bb30-3cef-be7a-3c070bda5f2d | -3.07434 | -54.56388 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 702fc08b-65fb-31ad-a67a-71ad9028b9f3 | -2.66823 | -49.86895 | 2024-11-29 04:57:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6823052-bb5e-33ea-8ef1-7eb29f48f038 | -2.03461 | -50.73009 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43192b32-cfaf-3fc2-a9e1-f1370f412e06 | -2.69733 | -51.68651 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9c984b3-c7c8-3692-bb57-6d064ab735f6 | -3.09605 | -53.72891 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7eabcab-fe17-3ea2-9a08-0aac66581c53 | -3.11526 | -53.99979 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b019e904-2bbd-3d7d-a866-cd0ee7172729 | -2.86396 | -45.53557 | 2024-11-29 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ca53a1fb-34d3-3e9a-9d6c-8e063c904be1 | -3.18549 | -54.33223 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94aeca4a-1330-3afd-aa61-57544262f307 | -1.96206 | -52.10174 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bc73e34-fffc-34e9-836a-a1ef5b2b0397 | -2.83911 | -46.80923 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54cf241f-e74a-3b0b-b514-4331a2f443c6 | -1.23289 | -51.80399 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbbda189-dc14-3859-a502-fbf61d89aef4 | -4.12334 | -54.20751 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e27e4a54-c66f-3c55-b3ba-bff425fe7d68 | -0.2993 | -51.74463 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e2888242-ea64-306e-a2db-6fb1c71c36b4 | -4.07764 | -54.56473 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a8470e4-f34e-3258-afbc-e69100473e07 | -1.89865 | -53.03138 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37e70ce4-5060-3a99-9602-e39506a69f00 | -0.89938 | -51.65003 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddf21a50-3e9c-37e5-8e99-08df034bfb34 | -1.68621 | -52.43067 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e46844c9-5955-32f4-bbcc-4786cce7ab58 | -3.35441 | -50.5051 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5423273-b3fa-318b-b9cc-3c69eb16e4e3 | -2.84599 | -54.08789 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41fe2ef6-ace8-3530-917e-f85aa973c074 | -3.57021 | -52.27771 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f773b12a-0b9b-3fdb-8043-b8b2c4493ee8 | -2.72734 | -54.10766 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a8fbdf2-afe1-3cb6-a27f-dc1f72030b6e | -2.60487 | -54.21607 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 028a8b8f-bfe0-3d92-adef-422408cd08aa | -1.24524 | -51.79123 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README74.md)
