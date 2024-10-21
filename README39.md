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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ce6b5f1-6298-3d74-a15d-b32d76d73adc | -2.78092 | -49.29566 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8eb552fb-7c02-36b2-8f91-5732437257be | -2.78038 | -49.29913 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 82c01f00-6dc4-3c0a-a1f7-c3209b15d94c | -2.77983 | -49.30259 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3eba36ce-0876-339a-9fb8-c1eb2c3aa40e | -2.77929 | -49.30606 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f651d6df-9faf-3831-8fed-2b897c9d9ad0 | -2.77874 | -49.30952 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7550c1c8-0f48-317c-871b-1246f9ca8de7 | -2.77706 | -49.2986 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c2a65dc-4697-3717-8a11-fd846ba229bf | -2.77652 | -49.30207 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73ff77e6-75da-3f39-abfd-594b92a69228 | -2.77597 | -49.30554 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72ed953d-627b-388b-8911-61be6e4cee51 | -2.77543 | -49.309 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e036f0be-c061-388f-b09d-2b9438be3368 | -2.77488 | -49.31247 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3e624a9-7ede-32a5-9457-aba3cd6244c4 | -2.77375 | -49.29809 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb5a59f5-28f4-3926-a551-ccf060575f06 | -2.7732 | -49.30155 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 087364a6-c775-35d7-b218-509cc4a79f2b | -2.77266 | -49.30502 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dccc22ac-3abb-3184-9919-daeead668d95 | -2.77211 | -49.30849 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bddce59d-ab0a-31d4-8e7b-40ce092a6058 | -2.7682 | -49.29012 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9627dc35-5dde-382a-894a-ec241eabfc68 | -2.76788 | -49.78786 | 2024-10-21 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 693a33f9-0827-3524-9f3a-9049548f048b | -2.76571 | -49.41415 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c426e57-155a-34c9-ac5d-398e56115e5b | -2.76434 | -49.29307 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c06f344-341f-3bb4-98fd-2be45be51342 | -2.76394 | -49.36049 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edac90c0-aec7-3af3-bc75-fd124d25c498 | -2.7613 | -49.42058 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 267a013b-9a1b-38dd-8be1-e7b7396533b6 | -2.76062 | -49.35997 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14630dd8-b28d-3863-9d51-d9a378573a29 | -2.76007 | -49.36344 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8b2a1d7-ed00-3c8d-8766-7ebf2c510b52 | -2.70966 | -49.77126 | 2024-10-21 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 070ba036-f812-35c5-8c16-ff32197f566e | -2.70631 | -49.77073 | 2024-10-21 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c0f98a-e608-3d21-9833-451103eeaf96 | -2.66497 | -49.40553 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58474a6f-1f5f-3b3f-92b1-19d4ae1a894a | -2.66191 | -49.40504 | 2024-10-21 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2b2e91d6-cdc3-3283-a704-e19bcbdadea7 | -2.65609 | -49.26902 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 650dbc39-22c5-3055-a2f3-2336d030b9c5 | -2.62581 | -49.33177 | 2024-10-21 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7cadd6a-b97c-3eb7-918f-a9436b85528b | -2.56964 | -49.21314 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bcc81fb-cfd2-39b5-965e-0f3eb1d241d8 | -2.55736 | -49.70054 | 2024-10-21 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c4275ac-7c8c-360e-8798-1d8f8632fb29 | -2.5568 | -49.70406 | 2024-10-21 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8ddaa2a-e93a-3375-b3e7-ec591dc7da9a | -2.55411 | -49.18238 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bea20b20-580a-3962-a610-87586b444251 | -2.55356 | -49.18584 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 482a64a9-a7ea-3412-a8a5-0bef1f0a6ce3 | -3.03286 | -50.39357 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d111bf03-5d0a-3b59-bf34-f099cc9a583e | -3.03229 | -50.39721 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06fb5100-794b-3ebf-ad67-37ef44da4886 | -3.02947 | -50.39303 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc71b38-cbce-34c9-822f-a8f699818caf | -3.02889 | -50.39668 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e7658cf-2218-3d4a-a876-98b934b905dd | -2.98286 | -50.29273 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb7fc95a-5226-3fcf-8774-0a24ba0221e1 | -2.98228 | -50.29634 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9456ed9d-e6f2-30c1-ac9f-93bfa0e1d1ce | -2.96382 | -50.52144 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 99ea8c86-8ccd-3beb-a8ed-b5147cc039dc | -2.96323 | -50.52512 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a84327db-4430-3764-b6a9-b36939ac5a17 | -2.96041 | -50.52091 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36b09843-2ced-301e-a833-68b14711d841 | -2.95982 | -50.52458 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e8562692-465e-3717-bd85-0d96d114b53a | -2.957 | -50.52037 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fbdebaef-cc8a-3945-bfda-eb13edf1242d | -2.89423 | -50.45144 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0792d77c-21bd-38da-833b-be24512edf1d | -4.51239 | -50.4431 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a72f0c0-1a56-3eee-b2b5-a6c2169d9463 | -4.48375 | -50.44962 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9ee61bc-5e54-3903-8f92-92c2698fd28c | -2.20643 | -50.45486 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a772b1f1-469e-314a-aed4-f5e0e6ad9e99 | -4.48318 | -50.45319 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13bd888e-6299-3059-be9c-d9750dd4f1f6 | -4.46263 | -50.53839 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e7369f4-d243-3b79-9544-a5784de6890f | -4.42325 | -50.74054 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d6455ea-9b5d-30ac-ae78-e767caa36f42 | -4.42089 | -49.7991 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 53e848ae-c4c8-319a-ae30-e6fcec4bfce7 | -4.42044 | -50.73635 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb4f0e9f-5ec4-3624-8f46-0bee5932b5a0 | -4.42034 | -49.80258 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2e396088-3b6d-3625-bc11-7d7e61bedbe2 | -4.41986 | -50.74 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4ca66d3-0c9d-349c-ad4b-f16a24a40760 | -4.41756 | -49.79858 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8c370247-8d84-3da8-a353-21abb6b00c14 | -4.41062 | -50.53039 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4039bdeb-2102-302e-b65e-8df5f4e9247c | -4.41005 | -50.534 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0c5d7ce-0ab1-3740-aaf2-2cfaff900599 | -4.40725 | -50.52986 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eea5b7ed-7565-32a8-8061-b0c277e389a2 | -4.39306 | -49.63094 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89d1edd-7e45-33e2-9906-ab5f73e07ff3 | -4.36675 | -50.80701 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8fe7fef-48e8-3c8e-8ee4-894150d539c5 | -4.36663 | -49.8406 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5541675-1907-3f4f-8bfb-02b1e33e50c1 | -4.36335 | -50.80646 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e686a44-0dae-37f4-a21c-3622a5ff8f22 | -4.28229 | -49.98878 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 388c7f7c-f0fd-3898-b5c6-c73d29ee5b41 | -4.27997 | -49.7448 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e69be29d-621f-3eea-9972-913544f1d386 | -4.27896 | -49.98827 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a6cc40ac-4ab4-3333-b5fd-0af21377e10e | -4.27665 | -49.74429 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f7e0354-fe4c-339a-a61c-91407e776292 | -4.27609 | -49.74777 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8779ad2a-b767-3be8-95c5-f7e33e8fe375 | -4.2216 | -50.09109 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c4cfb5d-ac85-3ab7-8f8c-ece5d23d432e | -4.22103 | -50.09463 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a21920e-e8ce-306a-aeff-98cdcb5e4acb | -4.21825 | -50.09057 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5409f64b-05c2-341e-80dc-78e6a69f7656 | -4.21769 | -50.0941 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d303b4b-4d42-3bec-bc8c-125a9f7ce481 | -4.16773 | -50.75702 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5aa53c1f-4fc3-3804-8a25-682e72b24dad | -4.04876 | -50.53624 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd105e42-6a9b-3dad-a810-832fd0d15a3f | -4.04819 | -50.53986 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91936cf8-f04b-3f8d-8fdb-6e6906416d4b | -3.96056 | -49.89522 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d54149a0-862d-346b-af7e-9726e59b1e73 | -3.93944 | -49.96389 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd4658c-d0d4-315d-949d-494fb18dc19f | -3.93888 | -49.96741 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b204fcc9-b5ac-3d7f-90c8-cb2e8e98f872 | -3.91835 | -49.85983 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38c35dc3-dd9b-3ced-af98-2b8f48aa1e3c | -3.91672 | -49.74135 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 597a5750-21a8-3eda-b300-92d44b6f5064 | -3.91617 | -49.74483 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07e1a9b4-3049-3b35-8fe0-32f51bee8ea6 | -3.90436 | -49.99086 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efddd0e7-6b21-3987-afc4-54dc5ea76f2b | -3.90046 | -49.99385 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1370cac7-8e80-3988-a406-8046ebefdd2c | -3.89768 | -49.9898 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06590957-53f8-353f-affc-556b656a6084 | -3.89712 | -49.99332 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c30f8929-0e36-3644-a701-059f7875444c | -3.88432 | -49.9877 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edaa6a3f-6173-3809-84ed-b8e2d61f4804 | -3.88098 | -49.98718 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e5c20e6-4d2e-3489-b71b-cc7ad4d1fa82 | -3.81606 | -50.65366 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76cf3622-4832-3d98-8edd-ca9e00e57043 | -3.76626 | -49.98705 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb7141d4-7698-3e63-a350-e9d7f4929915 | -3.74853 | -50.65845 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d45b722b-4d72-33b2-9181-ab05cc22a6db | -3.74513 | -50.65791 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e037d795-1167-34a8-aa60-27b525209feb | -3.61028 | -50.58033 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d88b4e38-253a-30c7-a2b6-235b768cecdd | -3.60688 | -50.5798 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d7f2620-7374-3d54-9a98-a83e4d914a65 | -3.6063 | -50.58344 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17a64497-7b37-321d-9734-62e5afb3e78a | -3.6029 | -50.5829 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54ba4805-eca4-3a6f-baae-014482e86015 | -4.57678 | -49.50057 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9786e73f-c8b5-3b00-9e4d-0561f6a26494 | -4.55121 | -49.70589 | 2024-10-21 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36b4ba7c-16e7-3b4d-bb50-a62b642dac7b | -3.96111 | -49.8917 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3368561d-36dc-3752-b358-89e046bffe8d | -3.91561 | -49.74832 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f7ce72f-7740-3085-98ac-65559aa6f096 | -3.91322 | -49.74441 | 2024-10-21 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
