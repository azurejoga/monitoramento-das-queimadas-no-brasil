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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc0d7d9d-06c2-3f32-afb5-aacecf05c5a5 | -3.41513 | -50.16859 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fc4f24f-ee3d-342f-8ccd-53a199448fb1 | -3.80577 | -52.10012 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f060b36-b66d-3987-8061-91b3292c99be | -2.76273 | -55.32851 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5453e136-1e90-3902-9f4f-a40580d32e81 | -3.60975 | -49.98149 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5de078b-8718-3361-a4bd-f666d22d84d1 | -2.2656 | -53.47306 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c00e994-62b4-30e1-8511-8cbbaf6f2f75 | -2.02113 | -50.77153 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 227b1e0b-bebd-30da-bafc-70466f6148a1 | -2.46481 | -49.04492 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7df59f56-b872-3029-bbcb-aead1350bf16 | -2.8788 | -53.98839 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d2d7babd-47b1-3645-8df0-e20b1dca26b0 | -3.78576 | -46.69524 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11563acf-22e3-3351-a534-dca2dc0a6af6 | -3.70827 | -45.68351 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 834bf33d-c1d5-3786-bf89-66bbc92ff5f6 | -2.04581 | -54.67864 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ebcd766-70a8-39d5-a1d1-0c9dbed5e452 | -2.33057 | -54.50451 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ace406f-722b-3779-b007-3cf81a20b062 | -3.26905 | -50.55544 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 058351ba-9a6f-360b-b76d-1bf42d190fb5 | -3.02554 | -54.01797 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0214d13b-5d35-371c-84fd-7abc23dd57a4 | -1.33396 | -55.84393 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93507781-30b9-33e5-a8ee-b2d056bcdfe5 | -3.39773 | -54.27639 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be55c567-d163-3c42-bf00-4db82ee63842 | -3.08365 | -50.25193 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9375af81-0aa5-33c9-8225-6545afcc8952 | -3.68175 | -49.57167 | 2024-11-30 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a166999-1df6-382c-9dde-2beb016a3882 | -2.23452 | -53.69366 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25ab0353-6610-386b-8a93-c294aaba7e71 | -1.44661 | -55.19682 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a3b28088-228c-3b92-8d07-e483e17c871d | -2.80647 | -53.05046 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ca6875bd-adf7-36c6-8c8e-b60fdce1f1d6 | -1.19848 | -53.87083 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daa06c76-1306-30d4-a8ac-ed9be2fa27c6 | -3.59211 | -50.36988 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03dcaa0c-6895-3e47-a6aa-289d24d26dcc | -2.66794 | -48.79244 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be142930-7852-3de1-aa9a-3cd8493141e3 | -3.11787 | -53.75739 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67845c5b-34dc-396a-9891-2eef656b727a | -1.52775 | -52.05635 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7076c9d2-9526-36d9-84b2-ad165d89a4bb | -3.84154 | -50.08904 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c27e6438-fa5f-3d18-b671-d290bf3e69cf | -3.10429 | -53.11047 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41e36a01-b81b-3d74-b4b5-bcbf1141a437 | -1.3167 | -51.67139 | 2024-11-30 05:01:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c734f91-c964-3515-8705-d07ccd1a3853 | -3.04143 | -50.97948 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 889e41be-1609-3595-ab24-db4cd7078bcc | -3.74718 | -50.05693 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeab8671-6b45-34eb-816b-5c26bbad6148 | -3.29235 | -50.35028 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aeb6512-21eb-3eec-8d42-f96ab92a1066 | -3.08637 | -49.2053 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1268669e-6cf8-3e21-b57a-3495ad41ccb1 | -2.69646 | -48.66403 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0629b2c-fbbc-32f9-9e5a-e13ff0688acc | -1.9896 | -53.29585 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a2f91ce-6ee1-3564-82e8-b1ba3020e272 | -2.44571 | -53.96772 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae50609b-627f-33d9-a79d-32774fa0c882 | -3.24781 | -53.64269 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfc743ab-68c8-35b2-949d-85fcbd5ffa9e | -1.45559 | -54.495 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00f7a8a9-d4f0-3097-a4b0-b5127cca06be | -3.21629 | -53.62304 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9998050c-a70b-3b8c-9237-03a3bea8a118 | -4.05081 | -46.82612 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa5a8194-06a0-31f5-8aec-89e86998fce6 | -3.69476 | -51.80706 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba6a2dab-badc-3f3e-a7d3-bab6ff191e71 | -2.86541 | -53.98631 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3045bd8c-7af4-37ef-841e-8660c8f85403 | -3.2174 | -53.61587 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48465772-642a-31ef-aff4-14ea42847c24 | -3.41824 | -53.22217 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5a0ac72-4f00-3353-bb49-b821ae2d945a | -2.03163 | -52.08168 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f527ed1-ecf4-3f9b-b24e-a0d9f7095d8a | -1.40034 | -53.40292 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b661d99d-57a4-39f9-9760-c5477496a461 | -3.33627 | -53.36702 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96b0fcb9-e049-37a7-ab1f-c70559e2edbd | -1.78906 | -52.7457 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14a976bc-d5ec-3437-bf8e-c178623b6991 | -2.90332 | -54.17484 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c3223e6-0279-387a-bc4c-10a0d0b5465a | -1.49322 | -52.96505 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40b1a093-a271-332b-a660-f96001f9671a | -2.29246 | -50.69043 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33064319-c410-37c0-81a8-5d9b8ccf1bdb | -1.71953 | -51.18093 | 2024-11-30 05:01:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d0929d-59e4-39e6-bdb3-db9e2d1b4785 | -0.94754 | -53.21371 | 2024-11-30 05:01:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ded86ac5-2493-3f74-8077-f211de858fda | 1.18697 | -55.97019 | 2024-11-30 05:01:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c9bba0d-5651-367f-9ba9-406337cf6b00 | -1.59568 | -52.28883 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4110359-111c-34d3-b011-4b7565015dd9 | -1.72334 | -52.48351 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 524f0e53-7f30-3088-9931-f47b574e4d9b | -1.08734 | -54.16908 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8554d53-fc7b-38d1-9786-08860a130a37 | -2.89056 | -55.22449 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e1332d6-184c-3919-8f3d-6ddf609644a0 | -1.47533 | -55.38293 | 2024-11-30 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 309c8a0f-5890-3d5d-98f3-d1f4021e72fd | -3.025 | -54.02148 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1747c75-0d21-3024-802a-3feaf30aaea4 | -3.02834 | -54.022 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e7c4a0b-666d-3019-bd73-47e0fde7b19a | -3.11677 | -49.49094 | 2024-11-30 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72c19fe9-2d93-3ec0-8536-7cb9d3dd29ff | -1.56431 | -53.51852 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 768c1acd-95e9-3cc3-be58-4a369e887c6c | -2.77161 | -55.33698 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35a2a4fe-fc55-36c4-82e2-14c4c2a653cf | -1.39293 | -55.19553 | 2024-11-30 05:01:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13a8f980-d5cd-321d-bcd4-3243081344f4 | -3.05379 | -52.76219 | 2024-11-30 05:01:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb20a910-c331-3d4b-a94c-59ba6d530e77 | -3.07605 | -50.32845 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98b38388-bacb-399c-94f3-3736e5d44a50 | -2.45137 | -54.01871 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11460213-b3e1-3627-9a09-5d6882732b37 | -1.45613 | -54.49156 | 2024-11-30 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 095dbad0-5ecc-308a-873e-076a9c80d495 | -3.70285 | -47.1412 | 2024-11-30 05:01:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4182dea-00f4-39e9-a507-bfde78f59667 | -2.98406 | -53.90009 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a40aff2e-b379-3757-8f3a-917e34853f7d | -4.46662 | -49.62079 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f5e3ded-612d-3bba-922f-c6be871a73bf | -3.98673 | -41.50592 | 2024-11-30 05:01:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3569c066-8a4f-3f1f-9699-9b3a2c8eeb5f | -3.95881 | -50.19322 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d250e742-8030-36b5-bffe-d5ce57867176 | -3.82513 | -46.54951 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6cace99-d408-30d9-bb17-c87007a26255 | -3.71322 | -45.68785 | 2024-11-30 05:01:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96e512d6-dc0e-39f2-b0d3-e91d56649dcd | -1.99676 | -52.09653 | 2024-11-30 05:01:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2f0c3760-8741-3391-9ffc-532eec336d90 | -1.62979 | -53.85935 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40dada66-42b7-3cc3-a6f6-7c3cac525f1f | -4.04554 | -46.86166 | 2024-11-30 05:01:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28d79939-a4f6-348b-a948-058c55ed27b0 | -2.74393 | -48.61904 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 153313f0-ee73-3e21-8332-a0d36187e2d0 | -1.20404 | -53.87886 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b68121-4c94-3597-bbd2-957244ca8878 | -3.34005 | -53.21079 | 2024-11-30 05:01:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 903f7dc0-cc3d-3cd3-b977-077c90572dcb | -4.17199 | -48.61398 | 2024-11-30 05:01:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc0ee904-ce6c-30d7-b86f-4358c5a1c5d7 | -2.85047 | -54.03786 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c75deacc-6eb3-3aaa-8674-33cee68d6f2f | -3.7728 | -51.61698 | 2024-11-30 05:01:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8711ce3c-1bf3-302a-b5fd-587f03a8eab6 | -4.19184 | -50.68305 | 2024-11-30 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2984b1c3-1b87-36f3-8e95-d75d461481a2 | -2.80488 | -54.06665 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb4f54a4-fc56-3cf3-9902-fca93ffd8da4 | -2.98293 | -48.72302 | 2024-11-30 05:01:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78e1a73c-1eb3-34e7-83b2-33bb72577fde | -2.01644 | -51.19613 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc6a09b3-9906-3765-b8a4-e861d84409ca | -2.61058 | -51.80951 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ed28d6dc-f222-387d-936a-84db53994811 | -4.1065 | -50.98088 | 2024-11-30 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dbeb39bb-50e6-3d6e-9ab2-f4557ae1ccff | -2.54509 | -55.22736 | 2024-11-30 05:01:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94a0f277-40ac-3b17-8516-780e9449e715 | -0.0969 | -51.75162 | 2024-11-30 05:01:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa1a5322-8ea3-3302-ba6c-82fd521c7144 | -2.32673 | -50.67174 | 2024-11-30 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65231ecd-ff96-3006-a8e7-1afe9b758838 | -2.63065 | -46.87781 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51c337c9-7bb3-3d37-a63b-d4fba7b48173 | -3.19325 | -54.33054 | 2024-11-30 05:01:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fab6ce3-facd-3917-90d6-127657dbc565 | -3.22156 | -53.83192 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31bd6f63-87b7-37ee-8e53-a29ee4ac4180 | -2.26053 | -53.46131 | 2024-11-30 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21227fd0-9c38-30eb-b597-73d110f01c3b | -2.60128 | -46.57096 | 2024-11-30 05:01:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cab76dda-c266-3edd-8892-85a525b9a2ea | -3.44388 | -54.06815 | 2024-11-30 05:01:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README114.md)
