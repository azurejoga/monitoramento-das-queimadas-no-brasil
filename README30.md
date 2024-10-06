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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d65a4d5-59bb-3b8b-bd2a-a14d30dc4c2f | -16.546101 | -57.2108 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38d4bd22-9693-3e9b-b0a2-cd26f4dab3e8 | -16.548 | -57.219101 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c928df91-e713-32ca-b4bd-adc90ca83563 | -16.549999 | -57.227299 | 2024-10-06 01:41:03 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 32012932-347d-3523-86fc-ac394e5a1cba | -16.534401 | -57.205101 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 269b4ad2-b497-33f7-907a-a11263eca4b9 | -16.5364 | -57.213299 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2190d77f-549b-3a52-99d6-850de494e8d6 | -16.5383 | -57.2216 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9fee00f7-45f6-3ece-9093-9dbbdf248b6c | -16.5403 | -57.229801 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76a274a2-bbb9-3fc2-b0a0-ce3f5fe05425 | -16.542299 | -57.238098 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2f24a24f-ad6c-3318-b7d8-0e0aba00b0c6 | -16.5266 | -57.215801 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa293afc-7ce8-3099-9e9d-b2894d4f64e2 | -16.5285 | -57.224098 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3feb3fe-8b68-354b-bec9-baab8d0e2038 | -16.5305 | -57.2323 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10d088ca-53e4-34d1-a9fd-63197f4005d8 | -16.518801 | -57.226501 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b3c6696-d020-37cd-9aed-e16bec3d875f | -16.5208 | -57.234699 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd4a9b9d-199e-30c3-8e76-900bdd24ff28 | -16.5228 | -57.243 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 087bc19b-ab28-3d91-8fc1-beebb8fdc219 | -16.507099 | -57.220699 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6cfdaaee-c7bb-3f51-bbcf-dd37bdb012eb | -16.509001 | -57.229 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a22e090-c4ed-38f1-aebf-2534b75f328e | -16.511 | -57.237202 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59c06044-d98e-326d-8447-03b5ec61f122 | -16.513 | -57.245499 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2b6bd08-b35e-365f-b856-7291a730f78d | -16.497299 | -57.223202 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41945284-ccd5-3f7a-be54-5bb28baea5c9 | -16.499201 | -57.231499 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66681b09-db51-3f0c-9d36-c40c14a7f056 | -16.5012 | -57.2397 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e421b957-346d-389d-9ed1-89cf1dd75e4c | -16.503201 | -57.248001 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 111ce2d5-c723-321e-93ac-6fa99576c77b | -16.5051 | -57.256199 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 814a6656-bcb7-3954-83d1-5c17b035f6ba | -16.507099 | -57.2644 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 90865737-ebd6-3483-87cb-e4b15440a56a | -16.4895 | -57.234001 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1ea64982-a31e-330b-bb44-84e9a32481bb | -16.491501 | -57.242199 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c70fef29-1ef6-3c36-93b7-225f9fc49590 | -16.4935 | -57.2505 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b2b44d44-0c44-387e-a34d-cd76525e9dc7 | -16.495399 | -57.258701 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33413c11-e001-3b8b-bcad-cd4ef3242470 | -16.4974 | -57.266899 | 2024-10-06 01:41:04 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15a4520c-36ce-3846-945b-43441ed498a6 | -16.481701 | -57.244598 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ac551a9-2659-3d77-a377-7212b550dbd6 | -16.4837 | -57.252899 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ba009fa-1a2f-3c07-8c89-13eef3d9e9f9 | -16.4856 | -57.261101 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6c73055-6b1e-3d76-be25-4f73e75b06f6 | -16.138201 | -55.910599 | 2024-10-06 01:41:05 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d512275-d696-3aae-adb2-95a10206dd8a | -16.1406 | -55.9203 | 2024-10-06 01:41:05 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8fcafff0-2623-3439-875e-cf6612e8a4b3 | -16.4681 | -57.2743 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6aece176-dc4f-3dcd-8755-3fbdf6260004 | -16.4701 | -57.2826 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0b2255b-b329-3eef-bc3d-71f574f85cfd | -16.472 | -57.290798 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b396e0a3-4232-35e1-82ea-76e65d6d269c | -16.4564 | -57.268501 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0b26c25-1e46-3efe-8acb-2f51f38de950 | -16.458401 | -57.276699 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c7638f2c-5bfd-3472-b6d8-706e1c048d8a | -16.4604 | -57.285 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b6875c4b-7ab5-3ad8-a776-4fbcbd5fb73f | -16.4466 | -57.271 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5ddb9e12-900b-3325-909c-a3cd6132f7f4 | -16.448601 | -57.279202 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a3fd1a4b-b8b8-34d4-bc8a-851b9ecb9e89 | -16.434999 | -57.265301 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ac6dfdd-809a-390c-8e3e-e18e7dab3e8f | -16.436899 | -57.273499 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 59395704-de39-30f1-9fb2-10b78bb9ed14 | -16.4389 | -57.2817 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1de2ddd-c1fe-3193-8fc9-49ef16a77da2 | -16.440901 | -57.290001 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2db7bb37-c4d8-3a8b-b1f8-abc3c5d03345 | -16.442801 | -57.298199 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5fb0d1a-b274-3c8a-93d2-9f627490b37e | -16.444799 | -57.3064 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5eac4f3-54e6-38b6-8098-bcf8261df857 | -16.446699 | -57.314602 | 2024-10-06 01:41:05 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e5b633e5-a732-3a13-9478-95440fbdcfda | -16.4252 | -57.267799 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5788d0a-768f-3d63-bc87-9c7c1a06f7b3 | -16.427099 | -57.276001 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3e8f1263-e8d4-3516-903e-ac0d4ef201b5 | -16.4291 | -57.284199 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 48e3b8ec-e355-3804-9ccb-30666315c200 | -16.431101 | -57.2925 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7f814c9-6c83-33ab-8818-466a276ec0ea | -16.433001 | -57.300701 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 64ae5ef6-a417-361b-a140-80a13dc490ec | -16.431 | -57.3358 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16fc40ea-6636-3b7c-979c-d5a18a2a3550 | -16.433001 | -57.344002 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4a4bfd3-1e0f-3d63-9923-642282f4c558 | -16.4349 | -57.3522 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43da459c-3abf-3dc8-a1ba-609de3b1bd2b | -16.421301 | -57.338299 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2d59e54-9556-3a65-9d75-9f31a2e3f093 | -16.423201 | -57.3465 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed18c231-8726-3ba2-9ca8-383d1f4bd8a9 | -16.409599 | -57.3326 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84fc2c6e-7afa-3644-a135-1b1747c5e6f0 | -16.411501 | -57.340801 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b528fa01-5aea-348a-9242-f6fd1f72abc3 | -16.502899 | -57.7262 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9cab5b36-f9d6-3711-8163-1ef1829ee851 | -16.5047 | -57.7341 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ff7be52-1a42-36a9-a1cd-0a2dc9c9ab22 | -16.3999 | -57.334999 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c87ede7d-310f-35a2-b133-73cd63f56b73 | -16.4018 | -57.343201 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00651f86-af76-3648-aaed-b3a6dd3f9fc3 | -16.4076 | -57.367699 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c1fb3a9-70e5-379b-bd96-1639d747de2c | -16.409599 | -57.3759 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2b051405-6ed5-3615-96d8-4d661151ad72 | -16.392 | -57.345699 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e6d79f3-2e33-32b0-b02a-6526a0888967 | -16.3939 | -57.353901 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 364913f4-1582-396e-ac24-636bd5f5084c | -16.395901 | -57.362 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| edc247cd-87f7-330c-aa8e-3602b1f15608 | -16.3978 | -57.370201 | 2024-10-06 01:41:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7ba9a5a-6af0-35e9-910b-b5526071ab42 | -16.382299 | -57.348202 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6eb12c0-112f-33dc-aba0-0ded537efe3f | -16.384199 | -57.3564 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5afcd45b-4f68-305d-84a8-2653a15f442d | -16.3862 | -57.364498 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a486012c-7bed-3192-8ea1-51e81da33fa0 | -16.3881 | -57.3727 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 663c6611-c7ca-34ca-9904-9037fdef7445 | -16.374399 | -57.358799 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9190fef-c41e-376c-a809-524c4548128f | -16.3764 | -57.366901 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 124888ff-ec1d-3856-a149-4a0be04970c2 | -16.5436 | -58.207901 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79ee428e-4f21-353a-a31a-58bfe10fd793 | -16.5338 | -58.2103 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f2023d0d-f1b6-3daf-9dce-eda58a039cf1 | -16.5355 | -58.217899 | 2024-10-06 01:41:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aab4b360-0323-3f76-9f43-d67ba156ff47 | -16.3741 | -57.750099 | 2024-10-06 01:41:08 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 409224be-d894-3512-9452-b7d1765f00f6 | -13.6722 | -51.168598 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bbedc1fd-3ec1-3e17-8e7e-3421573428b8 | -13.6778 | -51.189499 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 35e7d8c8-554a-3d75-a748-e78aeaaecab1 | -13.6626 | -51.171299 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 135a2c4d-a2e0-3958-af7f-36af7b71a40c | -13.6682 | -51.1922 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecff623d-9393-30b7-8eb1-1b330aa2751f | -13.6474 | -51.153 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0bc57e43-9379-3b84-b3dd-13e850febf65 | -13.653 | -51.174 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9bb698-8341-399d-937c-e308397e5233 | -13.6586 | -51.194901 | 2024-10-06 01:41:25 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4a4a4a9c-f8ee-33bc-8d8c-1c054d5d9c5d | -12.7601 | -50.509201 | 2024-10-06 01:41:37 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a23f02a-95a0-3d63-b4e9-6cc381c277a3 | -12.7505 | -50.511902 | 2024-10-06 01:41:37 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9397a295-3154-31e7-87d3-e2ed88935acb | -12.757 | -50.5359 | 2024-10-06 01:41:37 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0ba580-50fa-3d56-8126-ff0e3b6465df | -12.7409 | -50.514599 | 2024-10-06 01:41:37 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3c5b637-0701-3c69-ad6a-cf74f1d6ee97 | -12.7474 | -50.538601 | 2024-10-06 01:41:37 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6835d672-af54-3cc1-858d-92c92743ae58 | -12.6196 | -53.094799 | 2024-10-06 01:41:50 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 88e221df-f9b8-3b27-b0c9-30b00685b091 | -12.6238 | -53.111 | 2024-10-06 01:41:50 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 715ada1a-e4fa-3856-9633-9493eff1e452 | -12.6099 | -53.097401 | 2024-10-06 01:41:50 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2892ccb-911f-34d4-aa59-53744df4f3c0 | -12.6141 | -53.113602 | 2024-10-06 01:41:50 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e237ece0-3ea4-31f4-8705-a15706e7856f | -12.6044 | -53.116199 | 2024-10-06 01:41:50 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 840d35ea-d87b-35cc-a3f7-d3793016dc1b | -12.5948 | -53.118698 | 2024-10-06 01:41:51 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa0d2355-49eb-3004-837f-62f0c408ab52 | -12.6609 | -54.019001 | 2024-10-06 01:41:53 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README31.md)
