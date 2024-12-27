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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2687755-a994-3370-90aa-b8643b6bd4a6 | -3.74011 | -47.3372 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9acbc82f-dacf-3eba-91d2-ff8c58a1839b | -3.98537 | -46.67958 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffe77f80-05b4-32a2-8895-2bd8070cce30 | -2.71452 | -46.16818 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b1e7675-58e6-389f-933a-b156214f0e1d | -2.636 | -45.95015 | 2024-12-27 04:31:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfdf80de-2289-3150-a8e2-10f211f059c3 | -3.7402 | -47.35831 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20315a08-d776-3b83-96f4-1580354f2554 | -3.92056 | -47.20745 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c639c4ed-d572-392e-b970-3d4099d816b3 | -3.97432 | -46.68502 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8435b4a-110f-324c-be79-c7ca9367a2de | -2.69044 | -45.44017 | 2024-12-27 04:31:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 829664ad-08ae-36dd-af89-74692b550bbd | -3.82342 | -46.05569 | 2024-12-27 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fa75bec-59bd-3c57-860a-dc094d3958b1 | -2.6403 | -46.09883 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de941b0a-a27a-3d59-93ac-967cf94af572 | -2.02288 | -45.62688 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6c696f7-a6db-33d2-8542-49096c089c8e | -0.06316 | -51.65638 | 2024-12-27 04:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2307e17-916e-38df-ba91-d34bf5069e9f | -2.283 | -45.57513 | 2024-12-27 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51601f62-473e-352a-9f85-225f6ed8d93d | -2.7418 | -46.19029 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc20c2c2-3af8-31de-9910-07ad24ada8f0 | -4.52106 | -42.07135 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b0adfb07-b8f3-3661-8381-b2e412c3aa20 | -3.73342 | -47.18487 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9972161d-070a-36ea-98a5-e5be727991d6 | -2.76104 | -46.11063 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d111514-cec0-381c-9f35-4d7e3af2ea7c | -3.91054 | -46.89881 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9849505b-eea3-3fb5-bf95-68116dd0a793 | -3.94841 | -44.98521 | 2024-12-27 04:31:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 969f015c-462e-3e12-949e-7b98602a6a96 | -3.23273 | -45.96548 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a32a4ef5-00db-3b1a-b5c2-170117a343c3 | -1.17048 | -53.73442 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 699c290d-5f19-3625-8ea8-33ad8379c24d | -3.09771 | -46.56992 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ef1ddff-dbb8-337e-9d24-3b4fc7e31e99 | -3.98482 | -46.68308 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bec1a94b-80b2-3a56-b3d0-283f4ca586eb | -3.91332 | -46.90278 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cf73186-814c-30c7-adf5-1f3309f16198 | -1.19425 | -53.58694 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d054ece-babb-34cb-8b5f-9fb5abda11b1 | -4.01197 | -46.70508 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17b0aaed-ea3f-3237-965a-fa03163171c9 | -4.51939 | -42.08276 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 25630457-af97-3779-ad5e-3843005c4006 | -2.63697 | -46.09832 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2133bc06-0d7d-3f81-8aa7-39ff941134cf | -3.70184 | -43.41889 | 2024-12-27 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 466433ac-77ea-37e9-849c-69e780be9bac | -3.23553 | -45.96957 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 59415c88-75cb-3686-9b4f-d10c019acb2a | -3.7352 | -47.34699 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1eef535e-00cb-348f-ac34-7e7a8bbe380d | -3.91886 | -46.91071 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2976c76-ca05-361e-acd8-8c01f6a89182 | -3.89882 | -46.99602 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5829a944-1e97-379e-9338-935aa40f2387 | -2.76333 | -46.13978 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f245c8-7fdf-3e2b-b6d0-479b8e078d29 | -1.64469 | -45.87312 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0c455e7-9964-3147-960d-b6ef04f22784 | -1.12591 | -54.13038 | 2024-12-27 04:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a634e60-413e-370f-88af-4825e23f4fff | -1.78374 | -47.83902 | 2024-12-27 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e320682-6862-37eb-a5fc-ce6fd8320ee0 | 0.46753 | -51.34165 | 2024-12-27 04:31:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a352ed8-b562-3118-a414-8c44c7055eb0 | -3.48459 | -44.97729 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3469c244-4d7d-3f57-9671-371e43f18adc | -3.22296 | -45.44541 | 2024-12-27 04:31:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80441b72-0c5f-3beb-8ae2-c1a026426d64 | -2.62664 | -45.3747 | 2024-12-27 04:31:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8658f658-d032-3eba-851f-cd2a23a23709 | -1.33045 | -46.64715 | 2024-12-27 04:31:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9833674e-0f90-3ca8-a1ed-1f180351bf32 | -4.00356 | -45.92876 | 2024-12-27 04:31:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6bee562-83be-34ed-8f6e-4468962096d6 | -4.77333 | -38.55497 | 2024-12-27 04:31:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2d68f809-d97c-3bea-a26f-196382692a6b | -3.73011 | -47.18436 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef8009cb-2451-36b4-aab7-f0bc387b615b | -2.72615 | -46.15921 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a28cd827-b8f1-3ae3-9072-6223e97ecebc | -4.04158 | -47.06043 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28e0b088-15aa-381f-8ce2-ffaa55788d65 | -2.71789 | -46.01384 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e1413d4-6eaf-3235-8fd3-6738a85db2e7 | -3.24111 | -46.30297 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bcaa335-7434-38fd-bd4b-0db5438a8b98 | -2.67306 | -46.63152 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4b8605a-53b2-386d-a57d-58daf29297e3 | -3.7435 | -47.35882 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de8c4388-7fc4-300e-9904-7e6b8c50843b | -3.88582 | -46.53175 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27e89a76-8f82-3986-9efb-a32d05a95f19 | -3.98705 | -46.69058 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ab21a50-27f8-3dcd-93c2-4950d763421e | -1.81242 | -45.58054 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 281aa08b-0c45-35f3-8239-7a632b500bfb | -3.98205 | -46.67908 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96df08fd-8f98-3fa5-a39d-6ce90fa6db03 | -3.89668 | -47.00977 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4861d39-f276-3ea4-9290-a04b4ef48287 | -3.82398 | -46.05211 | 2024-12-27 04:31:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c21fa5d-b222-3bd8-b2b2-2dda7cc88936 | -3.74056 | -47.18245 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61ca0795-e124-32b9-bddf-e007f111da45 | -3.00471 | -48.0583 | 2024-12-27 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 972130a2-7030-359b-9119-674ddd140f65 | -3.2361 | -45.49633 | 2024-12-27 04:31:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9104c3fd-f215-3c18-8ef5-3d14b80927bb | -4.00094 | -46.71052 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48cbf4c4-c7e2-3312-aca0-ec0dea1b2062 | -2.69892 | -46.61782 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78ccc40b-cfb9-3d0b-8957-3b892bd24bb7 | -2.73853 | -46.2113 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d2d614a-5f4b-36a4-89a6-0ecb42cce1e5 | -2.89032 | -45.36969 | 2024-12-27 04:31:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a0d4e84-aa77-3712-94c4-cf71c7bb3753 | -3.19304 | -45.97759 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d15026-a076-348f-abdb-ead4de1258da | -2.72287 | -46.00377 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 707fa731-c966-3560-9bd4-5fec45661741 | -4.03774 | -47.06336 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 259ad2bb-938a-3051-8cb8-89c14a64c504 | -3.69807 | -43.41828 | 2024-12-27 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5284453c-57bb-3658-aab5-4d6932c7a061 | -4.03658 | -47.04908 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bd0cce2-a87f-3731-b239-ab3fadde89a5 | -3.73065 | -47.18092 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51e4a407-a5a1-3b17-958d-bd4afb3676cd | -2.71119 | -46.16766 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60e5c6a3-0484-361c-84fb-7cc8a873fb0d | -3.93128 | -46.98333 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c98f2bd4-00b0-3ad6-a7f4-06962972b564 | -2.44333 | -51.79724 | 2024-12-27 04:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8db26875-c04d-32ec-9cb2-f65c235f62ce | -3.19359 | -45.97403 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08c79d15-53b5-3f09-9e16-2734ef2e747d | -1.64857 | -45.87012 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe3d403e-431c-3e60-a79a-ef3bf2cac926 | -2.76552 | -46.12572 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49a3adf0-d8b4-3b33-8b32-cc9dee6419b2 | -3.03932 | -40.11533 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 00d29a37-18aa-3cc2-9e3c-59fa415e8666 | -1.74724 | -52.60003 | 2024-12-27 04:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d279c531-dd7d-39c1-a7cb-27377770ba32 | -2.15816 | -53.73936 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2435455c-2db3-3033-8540-31cb1e8bfd73 | -1.5558 | -53.50222 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 22768d76-41f2-3b67-868d-6161d90e2ec2 | -2.79743 | -46.77427 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed44604a-433a-3067-b4ed-8fc2de1bebb5 | -2.63867 | -46.10936 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b00b746f-99cd-3c1c-b18f-be1939528497 | -3.09107 | -46.56889 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8276b41e-d744-33e1-b6bf-4ffafb61f046 | -3.41741 | -44.90385 | 2024-12-27 04:31:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 982fd9bc-b9e0-3a6c-b776-45b20ae57dde | -1.70503 | -46.2294 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02078b15-025e-31bb-beb0-fb98284a853f | -2.38017 | -45.40441 | 2024-12-27 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a5dca98-7be6-3ecb-b2ee-1ec56dd8dc81 | -3.76162 | -47.22091 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 101178c1-0008-3521-81f0-7032faca7421 | -2.15513 | -53.72961 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1ae8548a-317f-3acb-a911-b512208d32cb | -3.09385 | -46.57287 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2832ffdb-a8e7-37e2-8455-c8fdc7b6e7bb | -3.91171 | -46.91314 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93f9be83-2c3e-3c65-bac5-2a2df8677195 | -3.90266 | -46.99308 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8506f0cc-3be5-3082-b033-3f392db44d67 | -4.00641 | -46.69711 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73a5dd72-d5e7-3d73-ae09-2cb375b70ba5 | -2.73687 | -46.02399 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fdc5b19e-40a2-3179-bfa1-e61e5b4b97fc | -2.78035 | -47.14451 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5732e42-d621-32fb-80b9-c9a3b3281529 | -2.27907 | -45.57821 | 2024-12-27 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2df1ddaa-bb6e-38a5-afc5-83f7cefdd6b3 | -3.32666 | -46.71558 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa81a353-b513-3db7-9922-a61b4409a989 | -4.00426 | -46.71103 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60e71929-fec3-3b94-b30b-fa21d244050e | -3.91233 | -46.93093 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 345546c7-3a5c-3ef4-8d9e-bfde500e1963 | -3.9269 | -46.98971 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef9f0406-5623-36ea-9111-acc89a35cfc7 | -3.92109 | -47.20401 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README9.md)
