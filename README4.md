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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5791faac-8ee8-3c56-a853-3b6aa67a7393 | -13.38004 | -61.29504 | 2025-11-05 01:11:00 | TERRA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0bc2a94a-518e-32c4-97d1-7395ee1b13c7 | -11.54087 | -50.19761 | 2025-11-05 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 77a3c949-f131-3f5e-a7c3-fabceda7032c | -8.23344 | -49.98393 | 2025-11-05 01:11:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 5fd30f0d-5981-32ad-a1d1-a36f4cdb010d | -11.73736 | -59.31484 | 2025-11-05 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd2f1ec6-b93c-37e8-b8d6-603166b452b3 | -11.53837 | -50.17323 | 2025-11-05 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| e0c66906-f042-3020-b305-5be0981e00db | -11.53565 | -50.16823 | 2025-11-05 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 81b9e04c-cb3d-3e38-b46a-d9b4d77a86da | -8.05086 | -49.64907 | 2025-11-05 01:11:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b2760466-6878-3d3e-8bb7-2ff0ae2047c8 | -3.8394 | -55.97519 | 2025-11-05 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e6823bc4-4d04-3747-b601-a2043faf15e6 | -3.50461 | -55.50061 | 2025-11-05 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d547d451-fb3c-3589-b87d-bda45a55e959 | -2.79149 | -50.30607 | 2025-11-05 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b9a75064-7d34-33aa-be13-c207b7cf5109 | -3.51606 | -55.49874 | 2025-11-05 01:13:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 733b3fcc-f978-3162-beb8-726d3454f463 | 1.84443 | -60.83119 | 2025-11-05 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8104670f-533d-3804-91a7-bf87c1ef40b1 | 1.48276 | -56.04211 | 2025-11-05 01:15:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| eec33f22-5252-3627-a8fd-2e9c0c7a8186 | 1.99226 | -61.42363 | 2025-11-05 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1e41d71e-1e78-3aad-a8c4-701f68b67709 | 0.84434 | -59.33912 | 2025-11-05 01:15:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27a7843e-ee20-345f-950c-70362bf411f3 | 0.84575 | -59.32906 | 2025-11-05 01:15:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e9033bb5-55f6-3349-9796-12edf0d08a2b | 3.14767 | -60.73005 | 2025-11-05 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3f6103e0-7263-3817-94e9-8812c2329172 | 3.14891 | -60.7209 | 2025-11-05 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c29b9f42-6f19-3117-93b1-7dcae684e2c9 | 4.44128 | -60.49633 | 2025-11-05 01:17:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f68057bb-d5dc-3187-8207-d51901391c37 | 3.24591 | -60.68436 | 2025-11-05 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4135668f-ac02-3a3c-9866-9abcb856cf16 | 4.02017 | -60.81285 | 2025-11-05 01:17:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b8927809-221a-31cf-9dc5-38520987a3c8 | 3.30252 | -60.67338 | 2025-11-05 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15b2a3cb-29ca-38c6-a6a0-8d2e9e7a17a7 | 4.8617 | -60.25497 | 2025-11-05 01:17:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8f71f8b9-07c6-33a1-b55f-285ba23d3151 | 3.30915 | -60.09253 | 2025-11-05 01:17:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3080c92d-b814-319b-89d4-8d876d7b3981 | 4.38881 | -61.01121 | 2025-11-05 01:17:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 77aa8c32-e4df-319b-a997-fd8f00a25e8c | 3.90442 | -59.64223 | 2025-11-05 01:17:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f60a453-e8a3-3f5b-b86a-6eca671211d6 | 4.38755 | -61.02033 | 2025-11-05 01:17:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f160fdc0-2500-396d-aa82-d19bf36952a1 | 3.30125 | -60.68256 | 2025-11-05 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 942052a7-fceb-36d0-bc87-8c1fd33470b7 | -4.4819 | -43.2374 | 2025-11-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.7 |
| f0ab4b9a-8b38-355d-8895-c8295baaa196 | -5.4553 | -45.3988 | 2025-11-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 39263827-f1c5-3bdf-bf9f-f3d6fcb64684 | -4.4258 | -48.9679 | 2025-11-05 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 3e105922-4525-31e4-aa8b-0e341bb4e47a | -1.3006 | -49.1677 | 2025-11-05 01:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3d924dbd-5ad4-38de-8ed2-2facea758e09 | -3.2503 | -46.8709 | 2025-11-05 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ecfb03df-df64-3c95-84b7-cc9ef91bfb89 | -3.2317 | -46.8716 | 2025-11-05 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 3502b4f0-4a85-3466-8ad2-a27073d3a36d | -3.4899 | -43.6383 | 2025-11-05 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| ed397ad1-2627-3f49-88bd-072cf1401ec0 | -11.8473 | -43.7256 | 2025-11-05 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 4e360b39-d80a-34f9-b0fd-c97eb30e50e8 | -2.6508 | -48.52 | 2025-11-05 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| fe106c7e-19a7-3911-b3b3-21003a6611d3 | -2.6509 | -48.4985 | 2025-11-05 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 01c81ca8-1e2b-3dd9-a890-3f80c8c6d74a | -5.0399 | -43.6205 | 2025-11-05 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 24c38982-f716-3154-9a3f-55beba82998f | -4.4635 | -43.1919 | 2025-11-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 01136b87-d238-32ee-a77e-1a8ccd851457 | -4.4259 | -48.9465 | 2025-11-05 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 4e60bc3c-bac5-3962-a461-791d98ad61f8 | -4.4446 | -43.2164 | 2025-11-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 12546d8d-af2c-3803-b6aa-89376b0de334 | -4.426 | -48.9251 | 2025-11-05 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3c5770c1-1353-3ef9-9b19-f76e2d93b3ef | -4.4632 | -43.2386 | 2025-11-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 252.0 |
| 91302fe8-8ca8-39f5-a34f-29801fc89c61 | -4.4633 | -43.2152 | 2025-11-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 395.0 |
| 56b3c9fb-1148-3de5-8667-8cfd3a77033a | -1.2822 | -49.168 | 2025-11-05 01:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0a02145a-2134-3afd-820a-ac8d8af8d81a | -4.4073 | -48.9474 | 2025-11-05 01:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 3d8ffdd2-87f1-3231-b6f8-615e286b02e5 | -3.4714 | -43.616 | 2025-11-05 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 3d12927f-d120-35d7-a4df-c29f6b04eef4 | -3.4712 | -43.6392 | 2025-11-05 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 947e37cb-e60e-38fb-b2cd-557b99497190 | -3.49 | -43.6152 | 2025-11-05 01:20:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 22e6c4b8-7f4c-3690-8547-8cd4e17092aa | -1.2453 | -49.1472 | 2025-11-05 01:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 3823c47f-bfc4-3d16-a94e-e62e8c6b7208 | -4.482 | -43.2141 | 2025-11-05 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 208.9 |
| be251725-c669-3751-893a-7e09dfad98e0 | -5.4551 | -45.4214 | 2025-11-05 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 809af3cb-bc11-3c10-ba30-c70b401b722f | -4.2789 | -45.6709 | 2025-11-05 01:20:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| a1f8a129-e903-3156-a4a8-7d9e65cc7f54 | -2.7921 | -50.3196 | 2025-11-05 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 7a3399e7-d7aa-349f-becb-4aec6bd2fbf2 | -1.2638 | -49.1469 | 2025-11-05 01:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d83d5293-f442-364c-bf87-ab22fb1945c3 | -5.2453 | -48.4966 | 2025-11-05 01:30:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b5720551-aa99-38d8-9d73-e60c6cd038cc | -2.7921 | -50.3196 | 2025-11-05 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ba81b344-e9d2-3c13-8ae6-c81fe1260368 | -5.0399 | -43.6205 | 2025-11-05 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8909eca6-ee25-3f28-930f-8ba28c3356c2 | -4.4259 | -48.9465 | 2025-11-05 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 272d5b10-aaed-3cd5-869a-2ba70f577726 | -3.8166 | -52.3608 | 2025-11-05 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 0ca727da-821c-3f46-b44c-0dc70474f7b8 | -5.2268 | -48.4976 | 2025-11-05 01:30:00 | GOES-19 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 6f7f5dd0-3640-3889-88bb-f46eb4a3414a | -3.2503 | -46.8709 | 2025-11-05 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 170017f7-6e6b-30cd-8395-899418bda22f | -5.4553 | -45.3988 | 2025-11-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 207.2 |
| 5f6cdb34-f10c-3ce8-a9ab-cc094bb53fee | -4.482 | -43.2141 | 2025-11-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 0c9c0c42-cb90-3148-ab0d-671355f2d80f | -3.4714 | -43.616 | 2025-11-05 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ece64e9f-1df5-3fc2-9a94-4e7932981415 | -1.3006 | -49.1677 | 2025-11-05 01:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c16a7b14-9e3a-3ee4-b1c0-7463e33bd18c | -11.8473 | -43.7256 | 2025-11-05 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6e899fc1-3f04-31f0-9fe1-79170b380a0b | -4.4073 | -48.9474 | 2025-11-05 01:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| b5c659d9-901d-3671-b789-ce4e6b9710d2 | -2.6508 | -48.52 | 2025-11-05 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| ebe3aa3a-5caa-3df2-866a-28e42c01e554 | -4.4446 | -43.2164 | 2025-11-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| fc01d754-08e3-34f7-9476-c7c4c3c9a9a3 | -5.4551 | -45.4214 | 2025-11-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bdb4d0b9-eb65-3d98-b9a1-57f9f32f12ca | -1.2822 | -49.168 | 2025-11-05 01:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 23d8bfae-7af2-32aa-9fd0-c9e6d6dee2ac | -4.4819 | -43.2374 | 2025-11-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 4913b7d1-cd34-3c3e-921f-9a378cddcfa8 | -3.2316 | -46.8936 | 2025-11-05 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9610f206-71dd-3689-93ed-259aa960858f | -4.4635 | -43.1919 | 2025-11-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| fb018019-8ea6-3083-92e7-bc5a0b8214dd | -3.49 | -43.6152 | 2025-11-05 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 4b6c6b3d-1173-382a-a12d-be7f8d947633 | -4.4632 | -43.2386 | 2025-11-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 233.3 |
| a16e4ddd-3e37-34a3-a748-95a9eead61f5 | -4.4633 | -43.2152 | 2025-11-05 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 356.4 |
| 9e968227-544a-3084-9d14-9d6077fc1b09 | -3.4712 | -43.6392 | 2025-11-05 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d6dcca56-1f8a-35fd-aea4-882a17110b67 | -3.2317 | -46.8716 | 2025-11-05 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 2cafc469-2ddd-3f6f-8082-4ba9b590687b | -1.2822 | -49.1467 | 2025-11-05 01:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 30a69410-7ceb-3787-bc45-9aa6d08978a6 | -2.6509 | -48.4985 | 2025-11-05 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e8096e96-b1f8-3b55-b7cb-b3046e75ef87 | -3.4899 | -43.6383 | 2025-11-05 01:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 44a61fe0-9956-3b66-88ac-5ea58a3e520d | -1.2638 | -49.1469 | 2025-11-05 01:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| bcf2a636-c818-37bd-bf68-fd2a70c68d49 | -3.4712 | -43.6392 | 2025-11-05 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 2bc765d0-79c1-3e6c-b2e8-5c252f5b5bc7 | -5.0399 | -43.6205 | 2025-11-05 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e14e24d2-65e7-3344-90d2-cd348148a3ad | -1.2638 | -49.1469 | 2025-11-05 01:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fef23fa7-5641-3905-aab1-1ae51e8cce4b | -4.482 | -43.2141 | 2025-11-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 702c6065-8231-3248-bc57-4d140bc817f5 | -5.4551 | -45.4214 | 2025-11-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a9e51442-1ec2-3cc8-94f5-d859ecd26851 | -3.2317 | -46.8716 | 2025-11-05 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| da10841a-d698-3db1-a0b1-da4b7783fb63 | -8.05 | -49.6325 | 2025-11-05 01:40:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 0d45247e-fc0a-3be5-b514-e40de94c6e93 | -4.4632 | -43.2386 | 2025-11-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 271.8 |
| 2a39ca28-db99-3a0b-a732-0cb24e9d0f5a | -4.4445 | -43.2397 | 2025-11-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 3b6083cf-25ae-3279-8c04-39770112f3c7 | -1.3006 | -49.1677 | 2025-11-05 01:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| a3a20469-3c13-353d-afc3-5a769c5f2d78 | -4.4633 | -43.2152 | 2025-11-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 307af73f-9148-310a-ac51-b11ff403ef14 | -3.49 | -43.6152 | 2025-11-05 01:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| d1380137-899f-32fe-b96e-a1a2b7f6e65b | -4.4819 | -43.2374 | 2025-11-05 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 65eb3f80-47f1-3b51-83c6-d53afee75b2c | -6.0552 | -47.2935 | 2025-11-05 01:40:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| eba7a686-0d78-3642-93e5-ae71e681242d | -5.4553 | -45.3988 | 2025-11-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.8 |


[Clique aqui para ver as próximas entradas](README5.md)
