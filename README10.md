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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfdc6dbe-55a6-33e2-8634-df6c2c426e10 | -10.2979 | -50.2372 | 2026-09-20 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| fcb771c2-e229-37f5-9ff3-04659aa66475 | -2.6125 | -54.7577 | 2026-09-20 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| bc1c6f3b-6fde-37cf-931c-50101c6762a3 | -11.8547 | -47.6596 | 2026-09-20 03:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5fea85a2-a81b-331c-b426-6e9d17981312 | -2.8791 | -57.799 | 2026-09-20 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 916eaf00-c668-32a3-8eaf-0e99d1d885e6 | -14.6856 | -46.6886 | 2026-09-20 03:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 6d9170f8-b7fe-3f53-a7c6-208659cae278 | -10.3171 | -50.2138 | 2026-09-20 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| e8f8e12f-32c1-3961-8714-6d01c05e5d35 | -12.152 | -47.0383 | 2026-09-20 03:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b2627f06-48a9-37e9-ab8d-c16685760777 | -2.8791 | -57.8184 | 2026-09-20 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3cfa0899-e923-361d-a613-9d7a5e14c0de | -8.7911 | -60.7935 | 2026-09-20 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| baa13af4-76a7-3575-8065-6ef98862eacc | -6.3321 | -47.6248 | 2026-09-20 03:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d502348d-1d03-3839-b8ff-3b9e79164fe4 | -6.3136 | -47.6042 | 2026-09-20 03:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 9bd01cc6-c1e7-35b4-a0ee-1d88b45fa70e | -11.0991 | -54.0285 | 2026-09-20 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 6f3e7d21-f848-3b9d-9af0-588423738c37 | -9.131 | -45.7273 | 2026-09-20 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 96038027-fd4d-3c3c-a967-0f9e651b204d | -2.8974 | -57.8181 | 2026-09-20 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a158d8b7-70de-3b47-a8b5-a03ede028f41 | -11.2307 | -54.078 | 2026-09-20 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f8440ed1-2f84-3ef3-bb18-826874153823 | -7.3259 | -55.6153 | 2026-09-20 03:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 32e952de-2134-3a4b-9484-a3bea15ab6fc | -6.3133 | -47.648 | 2026-09-20 03:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 126.3 |
| e117933e-ea8f-323d-8bff-6e62b012479b | -6.2948 | -47.6274 | 2026-09-20 03:20:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 3016ed01-7158-37bb-a172-7571562d1d7a | -10.2976 | -50.2585 | 2026-09-20 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| a3ed760c-0a96-39c9-84ae-3c83959ef036 | -6.295 | -47.6055 | 2026-09-20 03:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 78e1eed4-cef4-3771-8256-2d546e74c6a4 | -6.3133 | -47.648 | 2026-09-20 03:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 71633b6f-8cd4-3844-97da-3b9cbf334e4a | -8.8097 | -60.7926 | 2026-09-20 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c3783096-1c28-36ea-9d30-98d8f13b2f45 | -13.0177 | -46.9125 | 2026-09-20 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| abb00993-17d3-30f5-a155-12ffb3d844c8 | -7.5522 | -45.435 | 2026-09-20 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 8fc7fa67-e51d-3c65-b006-768fcf8b1e66 | -5.8408 | -53.5408 | 2026-09-20 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bd3245c1-2553-3b83-9aa5-bb587cb6522d | -6.3134 | -47.6261 | 2026-09-20 03:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 6076fd53-9277-3095-99e6-ac6ad93d62d8 | -6.3136 | -47.6042 | 2026-09-20 03:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7e1cbc59-39bd-355c-afb6-b1cb30c720be | -14.6856 | -46.6886 | 2026-09-20 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| b0147a07-3e16-385c-96a5-fd2957a8b7c8 | -3.7453 | -51.8288 | 2026-09-20 03:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 75e41efd-df92-303a-9bd5-d0cdb14df111 | -8.7911 | -60.7935 | 2026-09-20 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f452291e-9ad7-3f25-9554-cc31d846ba6a | -13.0366 | -46.9322 | 2026-09-20 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 19bf4262-b68b-3ccf-8313-60bdd4ef2d5b | -11.2118 | -54.0797 | 2026-09-20 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e0173b16-9a5c-3f1c-b58b-02c1253ff812 | -11.118 | -54.0268 | 2026-09-20 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 750efb5b-f886-3e3e-b4d4-0cb22d660bc1 | -6.2948 | -47.6274 | 2026-09-20 03:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| fe2cabfd-4c12-3edf-a5e3-d7d2d5b8f5e2 | -7.5334 | -45.4367 | 2026-09-20 03:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 699cd934-c064-395d-902a-f8baf4b0c89f | -13.037 | -46.9096 | 2026-09-20 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 22303ae5-4200-3859-84ba-692a5e959754 | -11.0989 | -54.049 | 2026-09-20 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 95a51760-0954-318a-9fc6-10fcc8439030 | -7.8025 | -44.9337 | 2026-09-20 03:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1b4830e7-a6bc-3fa3-a45b-bd50e4f8cfb8 | -11.0991 | -54.0285 | 2026-09-20 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.9 |
| ab94e622-7b82-3762-ac5e-fa81bd1bcb55 | -2.6125 | -54.7577 | 2026-09-20 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| a2bb2f95-0a55-33cb-ac6c-7c0a091b8d71 | -11.2307 | -54.078 | 2026-09-20 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 06706129-d2f6-360d-8fbc-7756342fbc7a | -9.131 | -45.7273 | 2026-09-20 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b25409f6-8bb8-319d-9b0f-53fd5bf2df84 | -7.0286 | -45.2554 | 2026-09-20 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d8ef4e31-f49b-314c-8e09-4b4cd986bc7a | -11.2307 | -54.078 | 2026-09-20 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| dda15a55-3a3f-3f8d-aa0b-7b6648f82324 | -11.0802 | -54.0302 | 2026-09-20 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 147d268b-4e24-32f4-ac9e-ce311c59cea1 | -11.8547 | -47.6596 | 2026-09-20 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2cc334b3-f309-3996-a30c-e3d9a6f6a08b | -6.3321 | -47.6248 | 2026-09-20 03:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e49cb38b-3d98-360f-a182-28fc8f5d8b21 | -2.6125 | -54.7577 | 2026-09-20 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| bc0c9893-8df7-3fe4-a002-31b699154fca | -6.3134 | -47.6261 | 2026-09-20 03:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 92afaa28-ca28-3193-b1ac-45c04e8eeefb | -7.0098 | -45.257 | 2026-09-20 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2316f7ec-850e-3bfe-8d85-d693847f1c75 | -11.8544 | -47.6819 | 2026-09-20 03:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 03f2a45c-e159-3212-ae60-ab4187467adc | -11.118 | -54.0268 | 2026-09-20 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 86eaf8a7-293e-35a1-8533-bdc4a652082b | -6.3133 | -47.648 | 2026-09-20 03:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 94f2fa32-dcbc-3791-879c-aa030bc11f3a | -7.5334 | -45.4367 | 2026-09-20 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 4c38a30b-5e25-3933-b028-2056176258b5 | -3.7453 | -51.8288 | 2026-09-20 03:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 669d80a5-6044-3a43-bc17-92cc8b8f8965 | -14.6856 | -46.6886 | 2026-09-20 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 4b6aed19-511a-3d8a-bb5e-977db9369eeb | -7.5522 | -45.435 | 2026-09-20 03:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 4dce8e95-9f40-34ce-85e3-45b519b5d401 | -11.0991 | -54.0285 | 2026-09-20 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 303f09c3-e057-3449-aaee-d02e69216714 | -5.6576 | -43.37407 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ab8166b-a79a-3e7f-bdab-3577d597d622 | -3.50143 | -43.35423 | 2026-09-20 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cdfcf258-9eae-35f0-b5dc-90153f4aa453 | -5.40871 | -44.27591 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60273509-f56c-3132-8311-79ba202ce046 | -6.54566 | -35.50335 | 2026-09-20 03:42:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0e4d289-90f9-3e64-a089-50acd6140552 | -3.84657 | -45.42636 | 2026-09-20 03:42:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 427e2454-67b1-3bc2-9e67-4c7d86f5546b | -5.10827 | -37.69021 | 2026-09-20 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea4204fc-4f49-3d1d-9983-b9bf5d623138 | -3.8252 | -40.68509 | 2026-09-20 03:42:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b9890add-b67e-3dc7-9848-39c02084f7c5 | -5.65807 | -43.37127 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8fdfc4f-01f9-34d7-b40b-29d616716b4f | -5.40815 | -44.27924 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 425b1612-853c-39b6-919c-470a2dc1b854 | -6.36155 | -43.35911 | 2026-09-20 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| badd0f82-7e1d-32ee-ba92-2e0c1758066c | -4.57265 | -42.97375 | 2026-09-20 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93f90c90-1ed1-39e6-ab8a-e4fef146dc34 | -5.69825 | -35.46143 | 2026-09-20 03:42:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eecc37d1-1a14-390e-ae21-6a1f490bbf14 | -6.41549 | -43.8815 | 2026-09-20 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ede7f4e-3b52-3f62-82ce-1e3192796c4f | -2.8232 | -46.71009 | 2026-09-20 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07748139-4328-325f-9075-76875651ee9d | -5.09602 | -47.5104 | 2026-09-20 03:42:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 197823c2-8dfb-38bd-a715-c38be9f134d4 | -4.98726 | -45.15143 | 2026-09-20 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8d8a048-6b05-343d-9151-4e3146ac81d7 | -6.26336 | -42.72872 | 2026-09-20 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 55cdde30-9ebe-3a07-80bd-c73c500e4b3c | -3.56636 | -43.4871 | 2026-09-20 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aa08832-bfbb-3f0b-ba0b-4d4d2c501cd9 | -5.80272 | -45.21783 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b14e38b-ae25-3ebd-816d-82a3836aca79 | -5.66724 | -43.40837 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbc7ef98-2418-371f-a192-ecaca3030d1c | -5.67382 | -45.30324 | 2026-09-20 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d95030-ad05-37b0-8f59-a8722a0cf879 | -5.22273 | -37.65533 | 2026-09-20 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 700359d1-37c8-385f-88ab-1ffa24fd0cd5 | -4.95108 | -45.39459 | 2026-09-20 03:42:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ba90ecc-0ab8-37c3-b23f-c93c748068f5 | -4.68187 | -46.39946 | 2026-09-20 03:42:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f1ef95c-afba-31e5-9706-b060c2441fab | -4.98792 | -45.14764 | 2026-09-20 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4885a604-d2c4-3714-b8c7-b778aa1ec7ec | -6.21979 | -43.76173 | 2026-09-20 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3cae6eb-b97b-3a62-a25d-2958a0237570 | -5.89241 | -46.58781 | 2026-09-20 03:42:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3988dd2-f542-370c-a311-d65e11369619 | -5.40338 | -44.27512 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e452a00e-dde5-3810-a607-540f49430fc4 | -5.65308 | -43.37049 | 2026-09-20 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1402d06-606b-3336-ac25-e6342624a8e8 | -6.29522 | -41.76995 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 86ed7488-ddaf-33c2-8fb0-e900e59327d6 | -3.50607 | -43.35822 | 2026-09-20 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5aa5d57-0d0b-3361-a3e8-4fd8403e657e | -5.23707 | -47.5856 | 2026-09-20 03:42:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e04f5d42-4e5c-3212-989f-7c0314181310 | -5.7972 | -47.36943 | 2026-09-20 03:42:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 185fdefb-3c86-3186-bf8e-91f14af12ef6 | -6.30038 | -41.7663 | 2026-09-20 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cef0ce57-812a-3a0e-bed7-026be02add01 | -5.34923 | -44.82872 | 2026-09-20 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc43771b-579b-377e-81f8-1cc7785ce635 | -5.83204 | -44.1333 | 2026-09-20 03:42:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5d552f1f-6511-3823-9f98-69fc5383552c | -3.54841 | -39.01858 | 2026-09-20 03:42:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cd2652dd-14cc-34a6-9e1e-2a363b8f7a79 | -5.55353 | -45.54098 | 2026-09-20 03:42:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17d30a1c-45ca-3392-b068-d6150b84f793 | -5.36237 | -44.32301 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2efa959-b550-3c0d-9d37-885bb4ec1f56 | -6.54896 | -35.50386 | 2026-09-20 03:42:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fd7766b3-cbbf-356e-b310-6dbf260bbc00 | -6.02436 | -45.41397 | 2026-09-20 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c54c6da4-5b47-30a7-b8f4-85f4f807f298 | -5.40825 | -44.26968 | 2026-09-20 03:42:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README11.md)
