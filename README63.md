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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eed7e93-8ce6-3137-87d5-5785092cdf03 | -2.65281 | -49.84347 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74de3781-17b2-39ce-b43f-18da13952a45 | -2.64919 | -49.84585 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20800707-6a01-3ba4-b9cb-f736986efc90 | -2.64876 | -49.84285 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f466ee92-8e13-3478-a4dd-dbe5ad60cf12 | -2.64821 | -49.8464 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9136936-0168-367a-b35b-508ed0957500 | -2.63029 | -49.35411 | 2024-11-02 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0826acea-e18d-36a5-844c-d4f491422af2 | -2.62555 | -49.35724 | 2024-11-02 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af84a81a-74c5-362b-9451-0975107a944f | -2.60646 | -49.82179 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ad7d42c-3288-32ef-b1ba-9a5f52224370 | -2.60294 | -49.81765 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50cfcc26-5fa8-36aa-ad44-e848d0302a69 | -2.6024 | -49.82121 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53a5a26c-aada-39d7-b564-b1ffc0728acb | -2.60187 | -49.8247 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 549da98f-18ec-375e-8e83-2cc1be177807 | -2.59955 | -50.02867 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0476f644-0e6b-37f8-aa39-33badedce0d2 | -2.59889 | -49.81703 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a41d214-ee8f-3720-8ec9-22384c43cfe2 | -2.59835 | -49.8206 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60ec9526-070c-3c77-87c4-506a6e813bb1 | -2.59782 | -49.82413 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1059c540-ff35-318f-8fee-246297cc83e9 | -2.59431 | -49.81999 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3e39614-4e88-3d6d-a153-bbde6ee1e240 | -2.59377 | -49.82353 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34ec14fb-ba61-3637-8bab-977378cd1f24 | -2.59034 | -49.38306 | 2024-11-02 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfa969b0-8a24-33a6-bb02-a000a86ebd32 | -2.58878 | -49.93823 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| feafd43d-e489-38ce-a4c9-0d10c274750a | -2.58675 | -49.37865 | 2024-11-02 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df5589c2-d02a-341d-ab12-8ebb76f57cf8 | -2.58476 | -49.93761 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4786d938-e980-38e0-b5e5-0d80353b734c | -2.57486 | -50.05665 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 95c56fbe-1036-3c77-b9e6-17259f8ec29e | -2.57434 | -50.06008 | 2024-11-02 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5a69802-bc8a-37db-9bc1-a33356d70e20 | -2.5521 | -49.63238 | 2024-11-02 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d1e98be4-5a27-3deb-8dd3-0623504ced5b | -2.54228 | -49.80428 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 606caed9-76fb-3ca0-b332-6c05319e4734 | -2.53296 | -49.86448 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c9d43ac-56c4-333b-b2d6-ded016ed5f3b | -2.5116 | -49.73362 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e3589c-3dc5-3d0f-acf5-6d467ced1354 | -2.51106 | -49.73719 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 015fd02d-b32c-3eda-ae0c-9e1433956177 | -2.50129 | -49.74676 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efdb9134-901d-3f97-9595-2a5c8badc921 | -2.48753 | -49.8104 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21ac6b36-5e0a-3bbe-8584-cd9a694479f6 | -2.48202 | -49.68111 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86b5a13d-b1ec-3349-99e1-1b49d8373898 | -2.47487 | -49.61674 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c426b387-e056-3475-9336-7e65eafc6e85 | -2.47168 | -49.83331 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06fb44ea-130f-3575-be10-29ddbf98b99f | -2.47114 | -49.83686 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc15289c-220e-385b-9532-4c434e4cda89 | -2.46188 | -49.78827 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 941e8ed3-6e3a-34f3-ad3b-8bf51b6e32d2 | -2.43255 | -48.97064 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c98172ee-23cc-3f65-807a-3f9e6c46ce22 | -2.42762 | -49.65513 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8a5c5149-5402-3eb0-8c06-d0215a854154 | -2.42414 | -49.8664 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23733c7f-5f52-3a90-8b80-52aa2f5726f0 | -2.42011 | -49.86577 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7c2f661-af7e-3b6b-914b-eb3d52b5f4fa | -2.41694 | -49.83292 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d63d3c2e-4580-3f29-b98d-94ede3b34da3 | -2.41291 | -49.83231 | 2024-11-02 05:04:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed7bba7d-47c6-3c8c-9fca-2101d318129e | -2.38604 | -49.16175 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 138398d1-7f95-3dd0-9199-36a1223f4159 | -2.38545 | -49.1656 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5c47dd9-b08f-3806-959f-187b50612300 | -2.38356 | -49.67056 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbeb786f-2ae6-3ef1-8835-a1f0ed3da6b0 | -2.38133 | -49.38822 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b47276-de4b-3fd3-bb61-d7efd4db91c4 | -2.37949 | -49.66992 | 2024-11-02 05:04:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0492fbce-0d18-3fc5-bf9c-13be64c2d2f5 | -2.36897 | -49.10307 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8eafd33-bd82-3785-86e9-6ab26f07234d | -2.36866 | -49.33209 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ff375ab-8492-39f3-8797-4cdd46eed15d | -2.36838 | -49.107 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5aa33d33-3a36-3513-946f-f9a3ffa6b9d6 | -2.36475 | -49.10239 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31d40e25-c5aa-3a25-be03-a500b305e471 | -2.35842 | -49.17335 | 2024-11-02 05:04:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc4acf4a-9b9f-354b-b96e-425629b62960 | -2.35569 | -49.10507 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7871a46-bff3-3b21-a7ab-5893f1261434 | -2.35536 | -48.91033 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceb4db17-d569-39d8-b52f-300407a510f9 | -2.35479 | -48.90506 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aba6dd1-9c92-3069-9064-837d30b54bc8 | -2.3542 | -48.90911 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a99a7c31-fa82-3cb6-a7e8-cbce5cebaa5d | -2.35361 | -48.91314 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f61c2797-3d41-3e0e-87f8-e9c787b1735d | -2.35232 | -48.90162 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0144614d-8449-33a8-afb6-41ad689dae0f | -2.3517 | -48.90565 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d4f7f31-1893-34d5-bcca-f0c0dd5e0beb | -2.35107 | -48.90968 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ee1602c-d58a-3d03-b743-400424da6315 | -2.34242 | -49.10705 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 997d4f14-110c-3eaa-9ff7-04880e734991 | -3.52542 | -49.91811 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1304a4d9-62d4-3309-9adf-89f17a37c799 | -3.5095 | -49.94148 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddbb387e-44d7-393d-84c6-bb6f070d114a | -3.50543 | -49.94085 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82f458ee-e7ae-3976-85f9-b7e62acbe950 | -3.50526 | -49.9408 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1956ab55-8f13-342f-b500-9f82e798c162 | -3.5049 | -49.94445 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d79c21e9-2a1d-34af-98a9-fc63b2bbd183 | -3.50471 | -49.9444 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9f0f54-b35b-3c7b-b64b-04b6b9140791 | -3.50437 | -49.94805 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6702f1aa-9cd3-3c63-92e1-5a13071f7c5b | -3.50415 | -49.94799 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 890a766f-3784-30a5-bba8-531d3b87ad58 | -3.50136 | -49.9402 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c91c682-bc83-3cd6-b443-d91b6d334b92 | -3.5012 | -49.94016 | 2024-11-02 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 107f6e43-51ea-3625-a7d3-63a4768381c6 | -3.35396 | -49.23115 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3216cf8-869e-3135-94d8-20a9ef0cf409 | -3.29808 | -50.01931 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 179d0ae6-e2f3-3464-83f2-72c1ccea157d | -3.29755 | -50.02286 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36569b41-866d-30a4-9a8f-f86fbf152352 | -3.29404 | -50.0187 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6266c01-6549-3d50-ad5b-f709a4f38cad | -3.29352 | -50.02224 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61a84bdc-ca99-3f5c-a1b6-8a9942a81de4 | -3.2562 | -50.04269 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 775f9edd-e8d6-302a-a806-830d8192b63c | -3.25513 | -50.04969 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64c82e8d-7395-3e33-986f-b0570eb733b6 | -3.25217 | -50.04209 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c4ce63c-32ec-346f-8018-95cff91c9647 | -3.25164 | -50.0456 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 54a3cb2b-6f2e-3395-b0b3-461e41a0a045 | -3.2511 | -50.04908 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa69c199-85b7-3d3e-a101-d23774830687 | -3.24815 | -50.04147 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e8a871a-611c-36d2-b73d-d335535736d1 | -3.24761 | -50.04499 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fccc060-a67f-3b55-811f-62a493aca0c2 | -3.24708 | -50.04848 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19f66964-6094-3c2b-afbb-227a07f30d63 | -3.24655 | -50.05193 | 2024-11-02 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 636d378d-572a-3f6e-81ee-8ce2f2463b84 | -2.66495 | -49.26509 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c946fcc9-dcf1-3861-aeea-356a8f569bf9 | -2.66248 | -49.25283 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b6d5d88-983a-3e41-ab88-084a7a3cf4e6 | -2.6619 | -49.25671 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d392b5b9-4401-3dbc-beb4-e9e4c4047af3 | -2.65885 | -49.24829 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23413aad-d3e3-3aa0-811c-a47f8320aa26 | -2.65827 | -49.25218 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 034fbd23-4c4d-3627-9e24-4ee0bd55df4f | -2.61132 | -49.16128 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b7f3a7d-c757-3bf8-a8be-2a114e1fff60 | -2.6077 | -49.15667 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d199916e-a26c-3f70-8f9e-08a00a8e653a | -2.6071 | -49.1606 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 42214241-9fdb-3412-8b3e-413c31ae8f9c | -2.60172 | -49.196 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8283496c-829e-3dd9-a81c-a78276e0c13c | -2.60113 | -49.19989 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cf6c426-985a-30a9-a9a7-f51673cba719 | -2.59826 | -49.24713 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf7b3837-9cef-3c26-9a38-bd229c901ce1 | -2.59767 | -49.251 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22e21a05-e56c-3f1c-a141-023867046b5e | -2.59632 | -49.20314 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 966e8e99-6f3a-3200-9035-08ab3ef07387 | -2.5955 | -49.12271 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b925e96f-3c7a-3d16-991b-635f3a6df717 | -2.58799 | -49.22969 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3adafda3-9164-3142-88d7-50b5b8052063 | -2.57795 | -49.12404 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9495cae1-0dad-3ca5-ade1-787dd2e630c7 | -2.57736 | -49.12796 | 2024-11-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README64.md)
