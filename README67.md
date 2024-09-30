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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c067efe4-7f11-3f73-9120-ce1201e956f5 | -16.51637 | -57.35458 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 198fc471-bd34-30d2-9c24-147b81238647 | -16.50937 | -57.3513 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b4d92d2-dc9c-3b3e-8d4d-1655d1f3c6d5 | -16.50526 | -57.35071 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6bfb52df-cff4-3c0f-8c04-52f24f80eb1e | -16.50425 | -57.35834 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 30ef115f-2610-394d-9d59-987b74042b1e | -16.13401 | -57.52341 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2f753897-01c3-37e2-8a0f-629054921f5d | -16.12997 | -57.5228 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f1de9c3f-9044-3fb2-842b-11c7191645b3 | -16.12593 | -57.52221 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c324de95-7fc4-3fb2-b362-7e0cc2a71dc3 | -16.11247 | -57.53057 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d7058f56-c463-360d-82b4-dd91e4822e28 | -16.11202 | -57.53395 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a95a7148-e3ac-3ff5-b830-59839b9709f4 | -16.10885 | -57.52675 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb0a7a50-9dc7-32bd-aafd-0bf143ff103b | -16.10841 | -57.53011 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 608a2835-4012-33e1-9365-2368a990834e | -16.10797 | -57.53345 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 931054f5-dc0b-3c40-a487-9fd668092e88 | -16.1048 | -57.52628 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bea3354-f930-3e28-bfbc-b337981cf356 | -16.10435 | -57.52966 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63a7ba97-69a6-3501-b44c-3260bb496429 | -15.92047 | -57.44374 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 373b013a-fb16-3718-a900-213f9328db70 | -15.91693 | -57.43927 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11083e46-1be2-3835-9637-4471849c84a4 | -15.91645 | -57.44296 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06f725cd-c7a8-382c-8c31-d1476625d652 | -15.91289 | -57.43857 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 944ec14b-844f-3fee-981a-fe7ea55cecba | -15.82861 | -57.38448 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ead5815-44cb-32b1-909e-a3ab9b1a0f3a | -15.82813 | -57.38812 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abe949b3-f8fb-39ce-9297-0fd6fa65af3a | -15.82458 | -57.38372 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b6e704a-ce9a-3063-a2aa-5285d9121867 | -15.82412 | -57.3872 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 604f1e8e-fe63-3d5c-8e22-93bf6da8c320 | -15.82368 | -57.39049 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62b5824e-f1c5-3991-9b52-acbb37a3d94e | -15.82325 | -57.39372 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0ea3e31-c28b-3ba6-9b62-5fac4d3c6977 | -15.82054 | -57.38296 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4efd6bc0-6616-3da1-8724-ebc1836842cc | -15.8201 | -57.38629 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7562e52e-b412-34a3-90db-f25da0decee6 | -15.81966 | -57.38953 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f49fa2e-5200-3cb0-96c9-8e9c9fcb07c0 | -15.81923 | -57.3928 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83c12d2b-e3e2-3b15-ab33-36fe274cd1fe | -15.81609 | -57.38527 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5bb5013-aa48-331e-b482-32a4c50d00ce | -15.81565 | -57.38855 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 241ca726-9915-3963-a64c-f3a53414a740 | -15.81337 | -57.37453 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05084424-7e28-3a89-b1e0-238a2d90f952 | -15.81298 | -57.34583 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9173f55d-1600-3598-8514-7b703f9a6f2c | -15.81251 | -57.38103 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83867e56-c98d-32e3-b2e7-d02dd75a7a11 | -15.81242 | -57.35008 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5795b18-7e59-32a8-8312-426dd1d9a4a3 | -15.81208 | -57.38429 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56cff01f-e238-3aea-bc5a-b387d62b4e5d | -15.80978 | -57.37035 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e31a9ad7-a962-36b6-812b-c17ff3277618 | -15.8083 | -57.34992 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54454865-4fb6-346d-99bd-240d7ac3b338 | -15.80773 | -57.35433 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f5693a1-9ad9-3ce3-b263-85a520cc3f10 | -15.8072 | -57.3584 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c792854-f516-3ab6-804a-6fbd9a854ed2 | -15.80621 | -57.36595 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba354d4b-276b-3a44-aa56-cbb208a9481f | -15.80263 | -57.36169 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc56df7a-d85b-3159-8d33-2441f5890a1b | -15.78097 | -57.80136 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa146324-bc09-34e9-a11f-a3f718bd26d9 | -15.77844 | -57.79029 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e809dc71-90b4-3659-bd05-e39f88d9ee2f | -15.77773 | -57.79554 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 278c6583-f9e5-3bb9-8d51-15cebc85086a | -15.77702 | -57.80077 | 2024-09-30 05:25:00 | NOAA-21 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb4b5f28-72b1-36be-b5af-ceeef0b62899 | -15.77448 | -57.78971 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a0ba9b2f-9db9-3872-97ac-42b0d8092877 | -15.77377 | -57.79495 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b55e1498-c42c-33cb-bcf4-4640d71a7747 | -15.77307 | -57.8002 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3427770e-64cc-3d13-b0a3-043e8abb12ca | -15.77052 | -57.78914 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e24f543b-ab6f-360f-8d84-81868c347768 | -15.6191 | -57.46084 | 2024-09-30 05:25:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e71311a3-71ad-361a-8203-1e8389e81484 | -15.61556 | -57.45661 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f554e199-4fcf-38cf-9da4-c019c750a326 | -15.61507 | -57.46026 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9e113cf-452a-31d8-97bd-b63c88188fb4 | -15.61153 | -57.45603 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23964088-5db3-3b8d-ada4-4934ef1398a1 | -15.60847 | -57.44815 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 521a80c3-70a3-3616-820d-71dfbebe29b2 | -15.60798 | -57.45179 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 901d9602-9408-37b5-afd8-ad983d43130b | -15.60749 | -57.45544 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 655eb6c1-228f-3f91-b95a-392d25d1dc57 | -15.60701 | -57.45908 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f68b91b-a8c0-34f7-8d60-87800d429b6d | -15.60395 | -57.45121 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 876166d0-c0f8-3f96-96e6-f65c8f7ed107 | -15.60347 | -57.45485 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c26fdfa-3688-3ec6-b527-0154e825f201 | -15.6004 | -57.44699 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c4792ec-de82-3820-b032-b791e4ce6f14 | -15.59992 | -57.45063 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36be6620-4263-37bd-ba61-efd0e322c0b0 | -15.59943 | -57.45427 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2eaba1b-4e2a-3e1b-9868-8b8aad7325fb | -15.59846 | -57.46156 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46598869-748c-33c1-aaba-d5c797c61ebc | -15.59637 | -57.4464 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b9f0b62-5863-3bd0-9a3d-735bfc18dccb | -15.59589 | -57.45005 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aab0830b-abce-3afa-a783-df8eee025a3c | -15.5954 | -57.45369 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f721105-cc27-3366-aa90-4b01d05fc3e2 | -15.59492 | -57.45733 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 569a376a-5a3a-3935-8b4e-d9ea7c8d0f64 | -15.59185 | -57.44947 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9243ab2b-a307-36a2-a28e-5198cddc10d5 | -15.59088 | -57.45676 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90457471-2c19-3fc4-8df7-885960291d80 | -15.5904 | -57.4604 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9693153a-9696-3c4b-9084-5a51c96b79db | -16.60881 | -57.35225 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4f4c88e3-666a-3934-9b76-5cafe57bc997 | -16.59647 | -57.35048 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 07ad0447-06a5-33d5-b854-3161c145854d | -16.5217 | -57.35304 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 233880af-b5d8-3d81-bf73-af0683dda918 | -16.52119 | -57.35684 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 22c412d1-26c3-3707-b6a5-2dbf912da5e4 | -16.51759 | -57.35246 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e48fcb88-f0b8-3530-8f16-e64e8b5de54b | -16.51685 | -57.35076 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 41ac6f45-fcf2-3efe-8a6c-a50a31b2ca30 | -16.51348 | -57.35188 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a3f05fe9-fb07-3fba-8319-9269c06126a9 | -16.50475 | -57.35452 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 77ef5343-bf21-3e4d-8e3f-cc42bb32206c | -16.50374 | -57.36214 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 48639147-87c8-3e5d-8fe4-dec648016e84 | -16.49964 | -57.36156 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e0707827-5a3d-3622-b1b7-571c89f92ec8 | -16.49042 | -57.368 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 33218b70-32b2-3f37-8cd7-a83519788645 | -16.48172 | -57.37063 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 476f4582-9943-3fb2-b151-a2568df2b18b | -16.47761 | -57.37005 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b7380587-57c7-3ed2-892a-a713b918838e | -16.47351 | -57.36945 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 82b1215e-722a-379f-a2d1-d5d478a30354 | -16.46991 | -57.36505 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 302dabef-8759-357d-b3d2-0e913fe07cf7 | -16.46941 | -57.36886 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 216b4e82-11e3-310b-8197-1cd52cbf10d8 | -16.46792 | -57.38027 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2813abee-682c-3962-b8f8-2978484494b1 | -16.46481 | -57.37208 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd98cc31-3021-3bab-95cc-b45adb66d7c3 | -16.46466 | -57.34102 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 91dc0a7c-07d6-3621-80fa-d78cc93ae8ec | -16.46432 | -57.37589 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7e86e2f4-637c-352b-a7d5-7aaa7cecd381 | -16.46417 | -57.34483 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 10d56627-60a5-301d-978d-5331afc971f0 | -16.46104 | -57.33662 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0116593d-3dcc-3e7f-91d2-69924bbc71d1 | -16.46055 | -57.34043 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 87d76707-28a2-31ea-a35f-7565bc30a260 | -16.46006 | -57.34425 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7d62474b-c509-31ba-af5c-cfd59d14005a | -16.45743 | -57.33222 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c79dabdb-cd98-335d-b5e9-afc6d8bd25ad | -16.45693 | -57.33603 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cb1d8994-70f1-3456-890d-aeafce077f1b | -16.45644 | -57.33985 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 441ac6a3-b5f1-33f4-9a59-c121da36d022 | -16.45331 | -57.33162 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 79d57bb6-ddad-3fe0-b54d-f78a928613a8 | -16.45282 | -57.33545 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2669dc02-28d0-394e-9de4-abdb53131139 | -16.44871 | -57.33486 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |


[Clique aqui para ver as próximas entradas](README68.md)
