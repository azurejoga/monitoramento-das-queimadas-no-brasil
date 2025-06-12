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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f550080-15d7-33c0-bccd-16d22398a6cb | -7.4575 | -45.5116 | 2025-06-12 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 6d9be61f-3e86-3097-8451-f150fc3d0dc3 | -7.4763 | -45.5099 | 2025-06-12 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 869f9137-2c85-3d50-a575-3010b103675d | -7.4575 | -45.5116 | 2025-06-12 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| cdf633a6-1ec8-32cb-b2c4-0aecca4c3279 | -11.9874 | -57.2076 | 2025-06-12 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1601e540-6140-33f0-bc6f-ffdb0c5df8a6 | -13.8864 | -54.6519 | 2025-06-12 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4fa9fe10-f5dd-326c-a2dd-5721373c1d2a | -13.9056 | -54.6498 | 2025-06-12 01:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 9149add4-ccf1-35bc-8ba7-9bc9a2ce22c2 | -13.2798 | -57.0751 | 2025-06-12 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 28fd62b6-16ce-3fd8-9f50-e12abeb607f5 | -10.8832 | -54.742 | 2025-06-12 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b940695f-bee8-3dbb-bad8-4c0a5087240a | -12.0063 | -57.2061 | 2025-06-12 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| a7559e79-286c-3af7-864f-da566fc0306e | -12.7169 | -58.0242 | 2025-06-12 01:30:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 2c3534b0-a2b0-3895-9cf0-e238f89c0f38 | -13.2986 | -57.0935 | 2025-06-12 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 396fe7f9-0898-398d-9166-ef56067ce71f | -13.2989 | -57.0734 | 2025-06-12 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| eb9eb7dc-efdf-37f2-a730-1a3eb7a15c0a | -7.4572 | -45.5342 | 2025-06-12 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b51709f5-94ca-3a74-99ab-87c3f358c314 | -12.6268 | -58.049 | 2025-06-12 01:31:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d25e32f8-8cb1-30bf-932c-598db20811d0 | -13.8224 | -54.658901 | 2025-06-12 01:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4529d91c-a26f-3c53-9679-35a4615c8b82 | -13.8051 | -54.6334 | 2025-06-12 01:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e4d5201-3cda-3e40-9eba-4fc191ae4305 | -13.205 | -57.0919 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8d8034d8-d126-37d9-84b9-58a0a8f85f42 | -11.9133 | -57.205399 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01729385-9572-3c48-8d86-12a92037c7fd | -13.8033 | -54.664501 | 2025-06-12 01:31:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 810b48e2-22dd-30ed-8290-6488c0ee64e9 | -10.8094 | -54.781898 | 2025-06-12 01:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98c7eba5-4e85-3f2c-aef8-ad71cb383338 | -11.9186 | -57.226002 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c03299b5-0e71-3a8a-9f48-3b202036d3c3 | -10.7914 | -54.753201 | 2025-06-12 01:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f3961ddd-e8c3-3ffc-82c0-336db9a7fd34 | -10.801 | -54.750599 | 2025-06-12 01:31:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61b4b5d5-b5a9-3108-9f72-5221c3c6685a | -12.6223 | -58.031399 | 2025-06-12 01:31:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 88b044ad-a7a3-3e9b-8249-d433574aae88 | -11.9037 | -57.208 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06dd4a43-8f05-3461-98a3-47e032c29a7b | -13.8128 | -54.661701 | 2025-06-12 01:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85b06692-5456-3db9-a6ac-390dfac7b8da | -13.2102 | -57.111698 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8cac04b-3abb-33d5-b000-03be2d446de4 | -11.8411 | -57.483601 | 2025-06-12 01:31:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 857d5bb9-8057-3de6-9bae-1853fc185ac8 | -13.2094 | -57.069199 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80baf1c5-4269-3537-ac72-c61242fd8d64 | -11.8315 | -57.486198 | 2025-06-12 01:31:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05dbb6e6-d2dc-31d0-9cdd-509236de88df | -13.2198 | -57.109001 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 505dde11-71b7-37bc-972d-0cbb36718f0c | -13.8206 | -54.689899 | 2025-06-12 01:31:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e1f80c6-32a1-3893-b434-200dba90302c | -11.909 | -57.2286 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 356f8aeb-94a4-37f1-a66c-89749a084741 | -10.7999 | -54.7845 | 2025-06-12 01:31:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c66a328-8bd5-3ffb-817a-024bfa34eaec | -13.2146 | -57.089199 | 2025-06-12 01:31:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7b2dd08-1dae-3471-a1a0-734849a2d53b | -9.17 | -57.548801 | 2025-06-12 01:32:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1082dc47-81e8-3abc-805f-94f18aae3806 | -13.2989 | -57.0734 | 2025-06-12 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3b99a72a-7e7e-3e79-84a8-91bd86e775c6 | -10.8832 | -54.742 | 2025-06-12 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b752bebd-7ed7-384d-889b-cd1bb3229806 | -13.9056 | -54.6498 | 2025-06-12 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0cb66e6e-78ff-3229-a2e2-df41b4e31516 | -13.8864 | -54.6519 | 2025-06-12 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| fc96ebf9-41b6-3a59-aec1-7128cbb65292 | -12.0063 | -57.2061 | 2025-06-12 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d33c0a3d-4ca3-3d0e-968e-79d4d60ddb81 | -7.4575 | -45.5116 | 2025-06-12 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 9c97ae54-b172-3e32-9f17-c842d0876925 | -11.9874 | -57.2076 | 2025-06-12 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a732d5dc-bc73-3f3b-8932-f79343a35a7d | -13.2798 | -57.0751 | 2025-06-12 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1e133034-9ac2-333f-9a88-ae083113f119 | -13.2986 | -57.0935 | 2025-06-12 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| cd388bfc-f57b-3382-ae78-90dfccb453cb | -13.8864 | -54.6519 | 2025-06-12 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7de4899a-8e4d-302d-94e4-165f97a41cf2 | -13.2798 | -57.0751 | 2025-06-12 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2e79d187-7004-3aa7-a8ba-ce0426ae428f | -7.4572 | -45.5342 | 2025-06-12 01:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 8650f0ed-fda3-372a-9149-cc05ad3983d1 | -13.9056 | -54.6498 | 2025-06-12 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 18576f2b-53a6-394b-b151-f595e628faa0 | -13.2989 | -57.0734 | 2025-06-12 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 90c1838b-64b2-39dc-80b7-fe2f28195367 | -7.476 | -45.5325 | 2025-06-12 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 95883b9a-cbad-38f7-a02d-d8bc4e430c08 | -7.4763 | -45.5099 | 2025-06-12 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 19fb9caf-1115-39b9-8f83-82a5acb79c3e | -13.2986 | -57.0935 | 2025-06-12 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 09332fab-a10b-3de4-9848-dcf23c929946 | -7.4575 | -45.5116 | 2025-06-12 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 2be21f19-6fde-3ff4-b7ee-08a958e8b276 | -11.9874 | -57.2076 | 2025-06-12 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 5c16ec02-5b29-3c50-be73-d181c5852f21 | -12.0063 | -57.2061 | 2025-06-12 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 9e598b77-7f02-3484-b1af-cf75c73f5fef | -12.70386 | -58.04625 | 2025-06-12 01:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 317414d5-ec7f-3163-a3b6-3a951e77b180 | -13.29391 | -57.07432 | 2025-06-12 01:56:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 169.1 |
| 6cced126-c2cf-337e-8e5a-eb808e2ca99b | -13.28842 | -57.08236 | 2025-06-12 01:56:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 202.1 |
| fe4f0ed5-d8f5-3ed0-9046-9c6c9b6175f5 | -12.70904 | -58.0521 | 2025-06-12 01:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1452e798-56ae-3b4f-bfc9-d4db9a19f921 | -12.70343 | -58.02002 | 2025-06-12 01:56:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 7a7ee4f3-c24a-3f67-998c-93a423f4b8bd | -11.92549 | -57.47938 | 2025-06-12 01:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 04253733-2d5a-394c-8e68-b11c0b64a83c | -11.91482 | -57.47463 | 2025-06-12 01:56:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| bb8abb42-837b-3e46-aa17-4c85be6426de | -13.30054 | -57.11013 | 2025-06-12 01:56:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 10f599ed-48e5-36c1-a10e-780689fea4e8 | -9.25409 | -57.55789 | 2025-06-12 01:58:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| d3e2b29a-a2d8-35bc-8d77-86e977691d6c | -8.75383 | -64.80372 | 2025-06-12 01:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1988d01d-8046-3f48-ad55-0242fd42cae7 | -13.2798 | -57.0751 | 2025-06-12 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 0c5873f6-df75-3a4a-94f1-6f07a464bac3 | -13.8864 | -54.6519 | 2025-06-12 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a42a7d0a-34e1-3983-a246-71d73a531e6d | -13.9059 | -54.6291 | 2025-06-12 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| c3624c32-84ad-3840-a09a-9673cabdcb3e | -13.2986 | -57.0935 | 2025-06-12 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e37085ce-1a5e-3bc9-9d60-7f56192eac65 | -13.9056 | -54.6498 | 2025-06-12 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 5ad6c0a4-3a63-3aca-9c88-77cf29cc9c41 | -13.2989 | -57.0734 | 2025-06-12 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 90f19c5d-4f57-323a-8d79-55fb4d2a057b | -13.2986 | -57.0935 | 2025-06-12 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 1996afed-53a3-3038-98f1-4872039dbbe9 | -13.2798 | -57.0751 | 2025-06-12 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1b28025c-4d41-30d2-b5cd-824ec8264f08 | -13.8864 | -54.6519 | 2025-06-12 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 80d52dae-55fe-3588-852c-b8423fcc57fe | -10.8832 | -54.742 | 2025-06-12 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4f7da513-99eb-3c69-bfd4-29b180e447ca | -13.9056 | -54.6498 | 2025-06-12 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 358cd5e1-9e99-341a-b457-41e192b8b957 | -13.2989 | -57.0734 | 2025-06-12 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8310247f-12ce-3d23-8e1a-6df42e775f6f | -13.9056 | -54.6498 | 2025-06-12 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 7eed1c47-be26-3617-99d0-dffa12718536 | -13.8864 | -54.6519 | 2025-06-12 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| bbd2f6cc-891f-3d59-ba93-358c859ad0ba | -13.2989 | -57.0734 | 2025-06-12 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 87a9e334-ef07-3170-9be0-ff514e8a0206 | -13.2986 | -57.0935 | 2025-06-12 02:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 0acc5c6d-6e13-3ffd-87a2-8d44bf04d860 | -13.8864 | -54.6519 | 2025-06-12 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 023902a1-5d4e-370e-81f3-c8ed2314fe5c | -10.8832 | -54.742 | 2025-06-12 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| b20aa26f-8dbe-3683-9c5c-cd42eca590a1 | -11.9874 | -57.2076 | 2025-06-12 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| c7c584bf-b895-35ba-bade-d8976d6c815d | -13.9056 | -54.6498 | 2025-06-12 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| d32df8c6-a631-3860-96e5-a17fbf1dc47d | -13.2989 | -57.0734 | 2025-06-12 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6a0f805a-5240-3412-b6fd-98661ba5527a | -13.2798 | -57.0751 | 2025-06-12 02:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 769fdfc7-5818-30e4-85a4-b93a1c19a19f | -7.4575 | -45.5116 | 2025-06-12 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 1f3414d4-a0a0-3694-9384-185bcf42210f | -13.2798 | -57.0751 | 2025-06-12 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 281a3d01-fdc2-3d3b-85d2-262009e6f203 | -10.8832 | -54.742 | 2025-06-12 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 39e10e6b-5444-31f0-a578-ef128428f760 | -13.8864 | -54.6519 | 2025-06-12 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b0e0bf73-127a-361c-9431-1214883ff442 | -13.9056 | -54.6498 | 2025-06-12 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| de23293d-824e-3d36-ae0a-1e3515ff52d0 | -13.2989 | -57.0734 | 2025-06-12 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 7a83923d-ec4f-3992-b9b3-f90eb8169b3d | -13.8864 | -54.6519 | 2025-06-12 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b78d13fd-484b-309f-b21d-45faf3f3355f | -13.9056 | -54.6498 | 2025-06-12 02:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| bb17562b-0f1f-3517-9943-81538d54611d | -13.2989 | -57.0734 | 2025-06-12 02:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f0ced59a-006f-3ac1-a161-26a7c6b18d87 | -7.4575 | -45.5116 | 2025-06-12 03:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| e7122430-743f-37af-87c4-103a7d7a62b8 | -13.9056 | -54.6498 | 2025-06-12 03:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.9 |
| bd0053d7-061f-3b17-af73-722d19894f4c | -13.2989 | -57.0734 | 2025-06-12 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |


[Clique aqui para ver as próximas entradas](README6.md)
