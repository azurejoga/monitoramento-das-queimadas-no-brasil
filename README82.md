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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3eacab75-538a-3060-ad78-e6745d47c405 | -2.87648 | -53.32149 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c4e3e66-0b8c-354e-bda5-2195d51f4fee | -3.69743 | -50.22332 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc4e3c50-b14b-3294-864a-49bfdd229816 | -3.68642 | -50.2279 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b61a64d-35e7-366a-a47c-8ecc1f76ce91 | -2.80519 | -54.06536 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03770fa8-e714-3038-801a-84e8b0f63078 | -4.22552 | -50.89287 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e688d5c-40ac-33e7-b960-3d94349e9bd5 | -3.70206 | -50.22713 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d519db1c-eeec-33ad-a0cb-3caa0d7ca8b7 | -3.22677 | -54.17218 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 998c9e58-4f50-3993-a81d-b2738c247a61 | -2.18294 | -53.77355 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc3a409b-639e-33d9-9616-4fbc806b4b98 | -3.79222 | -50.13098 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bdc1ed3-8c7e-3f8a-9bb3-d855c6aca981 | -2.99192 | -51.45019 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d01c26b2-cd93-3776-b35d-c6307b488b5a | -3.43455 | -54.5406 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c4465d7-6b96-3c49-b0c9-2a26bcd641ae | -2.60649 | -53.9715 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a858c08-6157-3edd-bf16-f7001e329029 | -3.24305 | -50.14167 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69a32465-679a-31e3-b4b7-482240104742 | -3.66271 | -54.33918 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd19b506-3e6f-3dc8-b9b0-6a692fce30cd | -3.1072 | -53.82146 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 47802d63-30b3-3468-a05d-e076d250c461 | -4.31429 | -48.08537 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47a15b47-d743-35ba-a5d2-249d62f181ab | -2.87549 | -54.00392 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fcbb4108-153c-3bb6-b2c5-71a63102c497 | -2.25749 | -53.75533 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 728206b0-3dbd-35a7-86ca-400de24f40dd | -3.5741 | -53.02203 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16d5aee0-28cd-3047-b2fb-09add06573bf | -3.50264 | -50.49928 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8b63170b-357a-379e-b530-02e741b30014 | -2.41618 | -53.82304 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a424757-6b10-3aa7-8e71-8edd2a7b568f | -2.87476 | -53.94741 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08b7fef4-2bc3-3c4e-8dd0-4650cd9aed3c | -3.76903 | -51.65085 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c84c93b-f0cc-334b-a6c6-fd51d9bc10dd | -6.088 | -48.03798 | 2024-11-28 05:18:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbdb57fe-e6a2-313e-8804-eb20e7e292b2 | -2.90492 | -54.1749 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ac4a499-cdd7-3354-b432-6913d812697b | -3.05763 | -53.27893 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa2eeb1f-f5ca-3476-bd5d-0d3b1d8cd7ea | -3.07283 | -49.20259 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d7c1a23-e25a-31b6-89c4-55a072c3339a | -2.34577 | -53.92148 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc07a67a-cd1f-3430-96ab-631a66e553c9 | -3.09798 | -50.35992 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fcecee73-34c6-31eb-8d26-25c7e368b011 | -3.46619 | -50.53989 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cddda308-1057-3b63-a1f8-e5c13a269687 | -3.61868 | -51.36433 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 382aa155-f7c8-3e54-b1db-be0e71b736cb | -3.52678 | -53.78259 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e605178-8666-3b61-9cb3-3e50bab42e5a | -3.13378 | -50.25923 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16ebafdf-2993-3edc-8373-fa55f579ad0a | -2.60081 | -54.21314 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67c53bc0-4788-3a25-bb3f-189b26f6ff03 | -3.58347 | -50.3364 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bc891de-2e3f-3fbf-957f-c15ec386a6ae | -2.31201 | -51.95808 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e5b36e8e-95da-3f83-be19-4dde444505ae | -3.4436 | -54.11997 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c06a7fd-c7f9-304a-8565-70f5f715a7ae | -3.49295 | -53.81892 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1e964cf-7a58-3f5e-ab0f-af00c5f30dd0 | -1.76237 | -55.65296 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88a94684-998a-35d1-b42c-6a74d9c8e667 | -2.83125 | -54.0497 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 536e58e1-28bd-3fb9-bb97-e4006f9935e9 | -6.09558 | -48.03928 | 2024-11-28 05:18:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a63ee9e-3303-3057-b0eb-6fe78b7988a2 | -3.24806 | -53.63873 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8245426e-4d04-34fc-8153-edfdb80d63f4 | -2.72779 | -51.74 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8263894-35aa-3ece-8359-eebb1a5d5b2d | -3.27174 | -50.61694 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bad42919-dc3b-3949-9d96-36fc8b671e45 | -4.30839 | -48.08448 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74bc06cb-97fd-3677-87a2-69bce0dff635 | -3.24593 | -50.77087 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| a4ceedf4-f9b4-39bb-868a-9d62a031ab9a | -3.05375 | -48.51692 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc60a3d5-682b-3d86-9a57-b977bd57cdc0 | -2.34649 | -53.91666 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f2b8da3-7b35-3f5c-8be8-ed048fa63793 | -4.24219 | -54.73207 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4753cd14-1c31-31bf-add1-5c68c24cb47b | -3.31513 | -50.27964 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f63ccb9-d953-3d9e-b58b-5364b61f3668 | -2.17182 | -52.1362 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 013fea26-2901-3a64-9d58-f58bbeb8057c | -3.4984 | -53.80959 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 540b14f8-5255-3b8d-b945-6ec97cbe3467 | -3.08869 | -53.2942 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34e57dec-d84e-3251-832a-06b57f5b3800 | -3.4995 | -50.49364 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1435b6a-adba-3b5b-9516-ac7222201dc8 | -3.0392 | -54.03085 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d97f363c-ccb0-3dba-a093-007a322d9858 | -3.24408 | -53.63811 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8eced5e4-8a95-3fb3-a96a-54507e515869 | -4.09074 | -54.76203 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3636f40f-4dbf-3bc4-98e3-b43e95df3b67 | -2.2501 | -53.62223 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c589d1d7-48f1-302a-8ee7-858d4921c466 | -3.91218 | -47.20417 | 2024-11-28 05:18:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d3d01821-9e48-32b5-85bd-275109c20a60 | -3.37967 | -50.11869 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9072425-6e8d-3223-bd6a-fba240318e82 | -3.29268 | -51.15145 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17c252f9-f631-3306-8a97-6692c0bb2e2e | -3.24517 | -53.63108 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1130b4c9-865e-3523-93bf-5a484d2add63 | -3.29448 | -50.31624 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f294230-c4ca-3446-9d1c-7a12c44ab6ce | -3.38352 | -45.83739 | 2024-11-28 05:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 29.9 |
| afb282a3-a629-3d21-8e1b-10eeb7c0871a | -3.79136 | -50.13693 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 009baa91-463b-36df-9981-abf66aa8b66b | -2.87118 | -54.03291 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19fb47b8-10cd-3e01-a8b4-4152176cf9ae | -2.25403 | -53.62287 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90d6a7d6-bda0-3502-8404-0e623e40b13a | -2.53583 | -53.98299 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30b8b812-dc2c-3262-9b51-551a0eeec737 | -2.60462 | -54.21368 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d54ea965-6c27-3ee9-a665-7b20bf133131 | -3.39524 | -54.28466 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d018a90b-77ce-3553-a789-b8bff16bf6ec | -3.19955 | -46.59889 | 2024-11-28 05:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5024cae-aa61-3ae1-8caa-f48f87806143 | -3.12591 | -53.09843 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f721e1b5-8234-3135-8927-13cfc604c15f | -3.10109 | -53.26656 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a2a2e12-ca65-3ddf-92f5-0dbcdccb4a7f | -3.23298 | -54.26039 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 207217d3-fc48-33e6-b0d3-6f72215b73f0 | -2.25881 | -53.75202 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fff1841e-aea4-389e-857e-99fd4a2862d7 | -3.37502 | -50.11504 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 062234f7-352b-371d-9336-31a61cd55177 | -2.58109 | -54.36562 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9eb14e34-b22d-33dc-9cec-13ac06e323e4 | -2.97721 | -54.66195 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3792feb-c9eb-3c74-abc2-2fd58676bc48 | -2.07529 | -53.40203 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6aeb7dc1-2886-3652-bfc2-b0a0fd1657da | -2.99264 | -51.44539 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07978071-c0fa-3951-9651-68f486a4c4b9 | -3.31062 | -50.27713 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0fad5ac5-5b74-3f6e-809d-767c2bad8905 | -4.48272 | -48.1184 | 2024-11-28 05:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e980727-444f-3f9e-9287-2b189920234e | -3.1151 | -54.47334 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2779447f-4d3e-3019-ad17-a57f7a8b4420 | -3.49276 | -50.08103 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fd1c320-a0db-3007-8f04-f25edb5a91d1 | -3.2936 | -53.67676 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c88d1fbf-f834-3877-af43-cdba274db937 | -3.11201 | -54.00453 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d9ead2-4c4d-3a51-a332-eeb492ae5779 | -3.43966 | -50.02988 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81ae8ad5-fdae-3719-a4d2-425a083c844a | -3.31012 | -50.27882 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 565d0823-94c1-3758-9a44-70f6b085e18d | -3.24592 | -53.64159 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| facb2e77-81c6-3a07-a363-73a47e060d68 | -2.62259 | -54.19389 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 80fa3840-a2b9-388c-b279-89212997b3f1 | -2.91123 | -51.57959 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb16f375-24e1-3b75-914d-1d0fb991cc85 | -3.55689 | -53.53063 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26735261-d61c-346a-9860-9a3f52d0292d | -3.71157 | -51.81624 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59a43290-cdbd-3fd6-9d3f-6cc1e3625efc | -3.08339 | -50.25404 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4522edfa-8ab8-3d9a-8dbb-cd79b5554ba7 | -2.82648 | -54.02927 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6a1f0dd-1ac0-3140-b8aa-21d7494f2184 | -3.40362 | -54.28103 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5944d8d9-b1bf-3d3b-a080-98902c8da5b0 | -3.39155 | -50.10848 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 690eeaac-0bd4-37a8-8925-709d3eb88da2 | -3.29118 | -53.66578 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09d51787-71fb-329f-b426-68e09796fb25 | -3.05652 | -53.28623 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7d68554-aaa9-3675-aa9d-64dcf4868256 | -3.56802 | -53.12103 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README83.md)
