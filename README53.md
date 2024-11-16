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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5a321ea-42c9-389a-b474-0ea037c09f9b | -9.91767 | -59.91034 | 2024-11-16 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a027c953-ed26-3086-b216-78099b083db3 | -17.64074 | -57.55526 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.2 |
| 1e321540-a872-3c2f-97d4-725c12017897 | -21.21872 | -56.35768 | 2024-11-16 04:53:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ab26b6f-c256-3a9f-a1dc-79fd2315af0c | -17.81202 | -57.5559 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4319a99f-4607-34ec-b2e3-8ff0e0269c3f | -17.56983 | -57.46852 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 87dfc517-c3a3-3d1d-88c7-b1d0f2214771 | -17.24922 | -57.45266 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4923548e-fd54-3581-9a29-f7f851f0dc20 | -17.57185 | -57.45667 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4e8c52fc-df2a-307a-979e-be38872ae418 | -17.62187 | -57.41303 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 938c1751-2c5f-3081-87dd-adfb7ef3cea9 | -16.04361 | -60.11354 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c41f5008-f96a-3892-899f-912131446b8d | -15.90512 | -59.11093 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd834592-942e-3ec1-b1bb-cce9743d89bf | -17.21386 | -57.22813 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ceb623f7-397f-3d34-bd49-b2a7538c3906 | -17.58441 | -57.48754 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cf33e7bc-3091-3e6a-888c-10c431a5878e | -16.01735 | -59.36862 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 30139b4d-35fd-3514-a8ad-25721b225242 | -17.64408 | -57.54598 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9fdb22c4-2b3a-3487-8a25-3a6b438877e6 | -17.24576 | -57.45202 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6eaabac2-66e9-3105-a90b-293a7e608315 | -17.62836 | -57.56528 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.2 |
| 80dad56f-5c16-3e13-8b5f-da6fc2198c13 | -15.90151 | -59.26542 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9085818f-d417-39ba-8ced-10c9fcb58a3e | -17.04528 | -57.43398 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8e1e0695-900a-3569-9b98-37f55cb31b4b | -17.56705 | -57.46393 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| ec765fe6-116f-30fd-8c7b-4005332a33a0 | -22.13523 | -56.57767 | 2024-11-16 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4f3b2fa6-ecf9-3e56-8fbc-3ba4ac562868 | -16.00793 | -59.37007 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b4a792-23f7-3e3e-addf-d943fe9e2a71 | -17.55903 | -57.53193 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 45fad126-2aba-3c87-bee5-5185e308d6cf | -16.9565 | -57.63381 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ee8bba89-5217-3ddb-96cc-522b3d336a56 | -17.59248 | -57.58741 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| 02dd8236-5a54-3916-a307-4ffea8e676d2 | -17.65859 | -57.54456 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 70233f8c-0e1b-3c21-9666-cd828f265f93 | -17.56638 | -57.46788 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| d92c9591-e8c2-323d-9f96-fe6907db0614 | -23.65198 | -52.94059 | 2024-11-16 04:53:00 | NOAA-20 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 32.4 |
| ae3ec45c-8b4c-37b9-8d9c-9fc959c10c1d | -17.58343 | -57.5775 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7de4e14d-b761-3a6a-8679-2cb49f2ed4fc | -17.71036 | -57.53366 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a14bd969-4c86-3a15-a3c6-2f5fc894a73f | -17.57673 | -57.4698 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 9487478f-c2a4-33dd-9555-745894b0fd09 | -17.57606 | -57.47375 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 390dca00-9dde-3e86-9402-bc9ed8b7075a | -17.71081 | -57.48882 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| acd4b310-69b6-31cf-81a6-b8471deb0345 | -17.64204 | -57.5579 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.1 |
| ea90cfd1-c57f-3b48-86a0-48dff5e83551 | -17.63872 | -57.46086 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 21f3c778-d69e-3abd-9b19-402c9679556b | -17.57718 | -57.57223 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 28c8de9f-1fa4-36b2-b26c-154deac6153c | -17.58689 | -57.57815 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| e847d4e8-09cf-32bf-84b4-21714e8b8fb9 | -17.58757 | -57.57416 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 888a7419-cf01-386d-8abb-d714b2449dbb | -16.16514 | -58.35732 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 79d40435-067c-3a64-90e7-a1a1a6abd7aa | -17.64907 | -57.46277 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ad8dbd6a-ddde-3e75-8c64-bee7f0617db8 | -17.68213 | -57.55301 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 4a4ca4fa-b386-3763-969f-c2db978c4890 | -17.29396 | -57.31445 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0202c757-8949-3c9d-88f5-2de271fcd5fb | -17.09123 | -57.47937 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7b9da249-b8ea-33b8-9ad6-4dd3f181b8bf | -17.70802 | -57.48423 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 91ab0a9e-52ff-3e15-b4c7-cc1c5ff59412 | -17.58009 | -57.45004 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fb86547a-2b60-3415-875a-327e524fc7a3 | -17.69366 | -57.50606 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| afd73678-e8b8-3389-ab62-eaba499ab4e8 | -16.91852 | -57.5395 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 935b03ae-a2ad-3ad2-9763-05e0961517c2 | -17.68626 | -57.54968 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 19b93a34-8442-3a47-a69b-417d3cb41e00 | -17.69462 | -57.56353 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bbea5050-04ca-3d99-a7f2-5d2368a3e685 | -17.56189 | -57.55708 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0ae679f9-83a5-3047-9abc-3fc6f2217fb8 | -17.68904 | -57.55429 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f37c3297-3d28-35a6-9472-e1807711aa67 | -17.56418 | -57.43898 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7c462fee-6c46-346d-9e55-80e31942698d | -17.58076 | -57.44609 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 476aea3f-8032-3541-a0c7-ab6fbf2da62b | -17.58208 | -57.58549 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 64ead26f-6152-3dca-83af-d489d7d108c7 | -17.58508 | -57.48357 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b4cb9ecc-7c27-3b28-98e1-38c70b98c5e6 | -17.64415 | -57.44965 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 07903334-3ce3-3aa0-8018-f6d8e7ed317d | -16.95999 | -57.63446 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 94b41668-9452-31de-87c5-e1d1254bb19e | -17.56671 | -57.54976 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d6ef9dc4-71cf-371a-8b03-b54b6604eb10 | -15.89293 | -59.26899 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e46a3296-a410-3956-9eca-6b580dedfba4 | -17.57932 | -57.43363 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 52b3e2bb-3f26-3c73-ae9e-bddae474a07b | -17.56317 | -57.52861 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5cd06acd-d5ad-304c-8c0c-d80e37f2ced3 | -15.90534 | -59.2662 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ac547651-5daa-3609-b733-5595bdcb9c09 | -17.67656 | -57.5438 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 50165dbb-d716-330b-8b64-f60495ae534a | -17.56486 | -57.43504 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| a8b1d386-6706-32e8-9d09-46b3ff9257df | -17.82558 | -54.54099 | 2024-11-16 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f430d67a-091d-34b3-acae-b3f10946288c | -17.59054 | -57.47235 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 31608786-4146-3276-a7ca-9a87732af4b2 | -10.12539 | -65.02899 | 2024-11-16 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7948157-4ba0-315b-8445-87e4255e53c7 | -23.70497 | -55.16018 | 2024-11-16 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01f724dd-108e-331d-949a-8ba1c131a750 | -17.59103 | -57.57481 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 46d931f3-551a-303c-827d-c6f57867e248 | -17.69183 | -57.55891 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb85de99-d591-30b5-b8f6-92e01c7a922f | -15.69598 | -59.28661 | 2024-11-16 04:53:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7bb5bf3-4a05-3a86-b21a-93c1fba99009 | -17.5841 | -57.57352 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 92a02910-1b1f-3f89-85bb-270d3c3b4617 | -17.69192 | -57.57944 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |
| f8715a68-39d3-3fd8-87e2-5335b6c4ea69 | -17.24508 | -57.45599 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a37ad0af-b44c-3619-bb62-27b4c824d3aa | -17.57929 | -57.58085 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 46b113f4-a595-32f0-b839-5e4ba879dc3e | -17.6877 | -57.56224 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d1c8d3d4-ccdf-3cc5-b3ed-0c604d511264 | -16.95931 | -57.63851 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4d09df9c-e32d-341c-8ffa-a45805a0d322 | -17.68559 | -57.55365 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7b25d169-6285-3c6b-87e2-b5c132f675a3 | -21.21931 | -56.35398 | 2024-11-16 04:53:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 704bf7eb-4609-3c4e-8220-4bf183fad0e0 | -16.93135 | -57.63335 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3cb050ea-2f30-36bf-8c5d-7b44c3d65636 | -15.97149 | -57.2808 | 2024-11-16 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c71bdd62-613c-332d-909b-449a26f46288 | -17.64628 | -57.45818 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 86f550ef-b711-362d-a219-7923e5a6c73f | -17.63528 | -57.56656 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.7 |
| 629341cf-06a0-3198-b27d-b2028db9da7a | -17.59315 | -57.58342 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.0 |
| cf87d2b2-d1c9-3d86-b07d-6869ab11c557 | -17.6476 | -57.45029 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cff1e5b5-ad3b-3854-a944-dfe3d0fb0d21 | -16.0416 | -60.12457 | 2024-11-16 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d420dee-7e46-3a10-a3d4-121e2e06a4a2 | -17.63248 | -57.56193 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 435ee6a1-a498-3e18-bea6-e569524df4d3 | -17.70129 | -54.08849 | 2024-11-16 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f52e97f4-e4d3-3df1-80d1-63b5c0c03f5c | -17.57463 | -57.46125 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 408004ab-4272-380b-b0d0-3e498db7f2c0 | -17.58297 | -57.47503 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 40f65947-f3d3-324b-866d-649e58589499 | -17.21973 | -57.19305 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0496da8a-274d-3084-b733-a02d5496a7d6 | -17.58969 | -57.58278 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 96a808a1-1615-3e6d-b3cf-6a44c074a6bb | -17.57798 | -57.44152 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 402607bc-bd96-31fa-8f6f-dddc886196ba | -17.81269 | -57.55193 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 58d264f3-f2ce-3e2c-a633-e2420311b013 | -17.2341 | -57.19165 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b170a8eb-6375-3ea0-9c13-84ca4cbd36c3 | -17.62355 | -57.57261 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 190757fd-3620-3c50-9e53-8690de8dac28 | -9.25123 | -63.6264 | 2024-11-16 04:53:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61b9a88b-3365-3a74-a3c8-09035867f050 | -17.65039 | -57.45487 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b4dcb987-335b-3f8a-a709-4e788c1d9cc5 | -17.55347 | -57.52271 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.2 |
| ca1528ad-0550-3f76-b4d4-6eb741504f58 | -15.89684 | -59.26935 | 2024-11-16 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1682b349-969e-367e-a163-d2cf5f254a5e | -17.6926 | -57.57545 | 2024-11-16 04:53:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.5 |


[Clique aqui para ver as próximas entradas](README54.md)
