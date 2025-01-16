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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7d0b13e-0068-3b69-8399-d1d3de681cd8 | -16.1118 | -58.1666 | 2025-01-16 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 5f8e55c2-956a-3e4b-8bb4-77e3bb45c8c6 | -16.1115 | -58.1868 | 2025-01-16 04:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 3a2276c0-2faf-363b-b9ce-bf9cebfeaeab | 2.5437 | -60.584 | 2025-01-16 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 94e05d0a-1e97-3899-9ff7-e0728907db01 | 2.1767 | -61.8534 | 2025-01-16 04:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| d3dcfc0c-0efa-39e5-9544-a48b5dcb1bb8 | 2.1767 | -61.8534 | 2025-01-16 04:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 7b4381f9-2519-3b22-8d63-5bd5fc74552a | 2.18457 | -61.85677 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77f4993d-3aa0-349a-80d1-24fc543fd3d6 | 2.17958 | -61.861 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d03e58f-fc30-3158-a1c1-e8f70caab6db | -0.84419 | -53.08163 | 2025-01-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f4d96e9-2006-3b62-81bb-8a958fc97487 | 3.14163 | -60.70297 | 2025-01-16 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0d7ff6b3-7406-35b2-a5c1-b01fc83becc8 | 4.00604 | -60.14128 | 2025-01-16 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b70548ef-3837-3ad5-8c6a-1aadd0e91e6c | -1.38694 | -55.41809 | 2025-01-16 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85636c91-173d-3837-97cb-c61a08894821 | 2.17832 | -61.85733 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 335a7655-78c3-37d5-9d62-95048bb57756 | 4.26936 | -60.29261 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0f2bf34e-2d79-33f5-885f-07c368510fe5 | -0.98531 | -53.13495 | 2025-01-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 605d2f67-2a67-3b02-aba0-0ab1b689b7d4 | 0.67833 | -59.98282 | 2025-01-16 04:55:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b60ad4ca-89f9-3a7b-b61b-9f7cb3cc0016 | 2.53951 | -60.58925 | 2025-01-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7b73362-de4c-3e12-93d4-2f48c6faa286 | 2.16183 | -61.85969 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c207a865-3ae4-3214-8708-ecbcd3b8dbb5 | 0.84412 | -59.54338 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| dd043d7e-7d00-3fa7-8a82-94f713e76f96 | 0.84832 | -59.54026 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| aca790af-d30e-305c-ad92-8c51c7a1fa0e | 2.17887 | -61.86087 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a085d23-d90c-3a39-82dc-24cc2fabb8a1 | 2.16678 | -61.85535 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e7f616f-8ca3-3006-90bd-b02d8fc43ec4 | 2.16256 | -61.85984 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b36ed04-609d-38fd-b5cf-6ce0d8e91a5d | 4.26482 | -60.2971 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed3d4529-05cf-34a2-9f59-5cd0bba2de97 | 2.11144 | -61.8235 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d7e1f9a0-ee32-33c2-ba46-c3c166c71735 | 0.72455 | -60.11777 | 2025-01-16 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 024be27f-4893-35fd-b161-0e0c16aefa2b | -1.71529 | -52.40507 | 2025-01-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bfbef10-e5f1-31c0-8475-0d8a65011e18 | 0.7134 | -60.2993 | 2025-01-16 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2156c4f-24b0-3045-82d9-325c17a19d06 | 0.84872 | -59.54276 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1cae8ac-8463-322c-8a33-91fd5aa983bf | 0.72853 | -60.11545 | 2025-01-16 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c8c65c9-68ec-3412-a30e-bba694b2cf5c | -1.70588 | -52.40007 | 2025-01-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a14f1f37-8b00-3b27-b37d-e44927590e53 | 4.26977 | -60.29543 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f15b4627-5c00-3816-beb1-0b6879082792 | 0.72934 | -60.12055 | 2025-01-16 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c58daefe-8fc2-33b6-b194-f506ed2dcaa8 | 3.73405 | -59.72197 | 2025-01-16 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 862e1690-8281-32ef-b7d1-dd5500a97d1c | 0.72458 | -60.12131 | 2025-01-16 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7fb43a7-0d81-3bc3-85ea-9f64608597f9 | 4.26436 | -60.29399 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ce3dfb1-9254-331a-ae4c-e1c952356a0e | 0.71257 | -60.29403 | 2025-01-16 04:55:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1acd91a6-be34-3f41-ac97-e231af059494 | 2.16805 | -61.85901 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d204ca-83d4-3003-80ac-10af1716b6d4 | 0.72532 | -60.12289 | 2025-01-16 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7cd5df9c-d0b9-3843-9df3-1ea3c7d1041a | 0.72376 | -60.1162 | 2025-01-16 04:55:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c355a054-3fc8-38bf-a7ad-86f1710bc1da | 2.11584 | -61.81558 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88816958-1dac-3182-8035-18d48813cf32 | 2.11197 | -61.82702 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 088f6621-6aaf-3dd8-b4f2-aabcd2f9bf44 | 4.41619 | -60.59539 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dfaf5ba-520d-3549-979b-87bf31c2ca03 | 0.84372 | -59.54089 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9dfaff13-7fcc-3549-b87e-2ba77921b939 | 2.53907 | -60.58628 | 2025-01-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2582b06-6588-3ab7-aca2-9f9650e77d23 | -1.38408 | -55.41374 | 2025-01-16 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3bf352f-ed0c-3eca-b73c-fd0971b8125c | 0.84338 | -59.53872 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd0c84eb-12df-3c2f-8bcf-513c1672f217 | 0.5511 | -59.80191 | 2025-01-16 04:55:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67336a36-e766-3cc3-bb6a-fcf4db3c316c | 3.92899 | -59.68345 | 2025-01-16 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28c16bd7-acfa-34f5-9ed8-d4e7d91d2b8f | 0.96538 | -59.47553 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90c9ad83-f5b3-3da0-a649-bbe10e356316 | 2.16205 | -61.85635 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd63f61b-d2ed-3bc7-a382-1ec62ef1ef1b | 3.92412 | -59.68417 | 2025-01-16 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fdca40c6-552f-30d0-9e31-be181437ad3f | 2.10434 | -61.81353 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 77aeee15-b5d1-370c-a834-117e05786153 | 0.92114 | -59.80085 | 2025-01-16 04:55:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1ae478e-9194-3f6f-ab9e-aed5591845e1 | 4.26895 | -60.28984 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c3932e8c-a617-32a3-a5ea-562e4006d594 | 2.28902 | -60.21742 | 2025-01-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0fe3a047-44a3-321e-86d3-8b4f9ff2d7e6 | 2.11037 | -61.81643 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 364b416c-4037-3e4e-863b-235f0e819bd7 | 3.14116 | -60.69985 | 2025-01-16 04:55:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 944f587f-c3f1-32bc-9e02-4d64c7b6e1cf | 4.41152 | -60.59983 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf30dff5-f0f0-39d9-b5ca-44904f0f05eb | 4.29076 | -60.126 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 672127a7-66b7-38e3-8687-894d275a7cff | 0.66829 | -59.59173 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd9f0f5c-26c5-39af-86c8-7141e20c5d84 | 2.16732 | -61.85886 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28c44bca-42d1-34d7-a6cf-12f36f6b51d8 | 4.41014 | -60.59041 | 2025-01-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb4ed50c-240c-3241-ba22-082bd8e89c43 | -0.84749 | -53.08214 | 2025-01-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a7df697-11ec-31c9-bc4d-653b7836d200 | -1.93794 | -52.06772 | 2025-01-16 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d96f0be3-16a4-3629-ac79-21ed24bc4aa2 | 0.84798 | -59.5381 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d2813f6-8c41-3524-99ab-0bd23828c68f | 4.00648 | -60.14426 | 2025-01-16 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a72d24a-2c9e-3c69-ab62-795480b9f59b | 2.53863 | -60.58332 | 2025-01-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c86536dc-5de7-37bf-b33c-7d421a359397 | 0.84443 | -59.54557 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 883a4d7c-ece5-3e65-b92e-e7f241c275a8 | 2.11091 | -61.81998 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0434c927-fd20-39c9-ad42-e85f9a4f037b | 0.66902 | -59.59647 | 2025-01-16 04:55:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f98f9870-cd1c-3a4f-8c0c-83916da8823f | 2.11689 | -61.82252 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 29c4671f-dde3-3920-8a70-7727939b605d | 2.11637 | -61.81907 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bee0491d-c873-3088-929c-09dae8bbfae1 | 2.16754 | -61.85548 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 818af0a8-63f2-349d-ac7c-047ec7f3672b | -0.92533 | -53.0591 | 2025-01-16 04:55:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b4b7d1-8d23-30af-8435-e0c13ea80884 | 2.18509 | -61.86031 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a720b5b0-56aa-3554-b34b-e134234257e8 | 2.10545 | -61.82092 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1189b140-64b8-3b5e-823c-3c221565aec2 | 2.53994 | -60.59221 | 2025-01-16 04:55:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29331997-f524-38b7-919f-5c54a028cdfd | 2.17906 | -61.85746 | 2025-01-16 04:55:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 72c37d6a-1bff-344c-8e30-f46129810132 | -2.96871 | -54.6194 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25a859a9-816d-34d7-94fa-050e3a9e5683 | -2.97084 | -54.6234 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 829cccbf-4737-3d71-82ee-ed9b8b9cb504 | -2.9714 | -54.61988 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0be0811-35aa-336b-ae00-3b5d333f5946 | -2.81298 | -54.72152 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f0dfa4d-6bd0-3a58-8933-84cdbcc7b73e | -2.68953 | -52.2415 | 2025-01-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 793c7116-64b7-31be-9298-bad22c150796 | -2.96816 | -54.62294 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73e4eae5-7d77-3723-ba5b-0ade7570e196 | -2.69287 | -52.24198 | 2025-01-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c65c6cae-8753-363f-a794-98c4316099a7 | -2.90739 | -54.48755 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcffbbfd-f001-310c-a07f-4d372ed6e7c1 | -3.0237 | -54.59191 | 2025-01-16 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a94934ff-0075-3003-b53c-aec19db05600 | 2.1767 | -61.8534 | 2025-01-16 05:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 2e8c95d4-8b5b-3723-a028-c2d5c281c151 | -16.11103 | -58.17849 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 215cedea-8a7e-3df9-9041-1fe799aaf525 | -17.3369 | -53.77621 | 2025-01-16 05:01:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c5b1fb1-5e45-35b6-ae32-9928caba0584 | -16.1178 | -58.17965 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 8e9ce650-ab9b-3898-8472-2820f2daf824 | -16.11564 | -58.17152 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 630b8770-5b79-31fb-a830-6441b21764d3 | -16.11503 | -58.1753 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| b68094b5-6b20-326a-81de-e71f72c3b857 | -17.33334 | -53.77567 | 2025-01-16 05:01:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 31a5a9a2-3d94-3661-9752-f040452c2181 | -15.5962 | -59.01088 | 2025-01-16 05:01:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb5135d9-b226-3e8d-a391-04bef1d66d10 | -19.83536 | -54.70696 | 2025-01-16 05:01:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2728634-b83b-325b-a796-82ae9ecdff6a | -19.29658 | -54.22078 | 2025-01-16 05:01:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ffc0d9e-5230-3538-b158-44c964501e46 | -16.1138 | -58.18284 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 109168be-a538-3a22-ba9d-07fa11726b51 | -16.11195 | -58.19418 | 2025-01-16 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 633ee96c-26f8-3cd6-a6ac-05d5bc542f79 | -19.51172 | -55.31251 | 2025-01-16 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
