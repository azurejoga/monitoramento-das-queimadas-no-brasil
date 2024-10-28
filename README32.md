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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d00e693e-b401-3c99-baff-0ecc3197895e | -2.51883 | -47.44733 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c98d9e20-c503-3f0c-bca7-49d7a9ad8b56 | -2.51808 | -47.45197 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 246d89b4-295d-3366-9e4a-4494ab4d9912 | -2.50672 | -48.31214 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a737576f-9bff-3801-90f2-c4a4cb287ca0 | -2.49369 | -48.06021 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ea28f6eb-d476-31da-ba47-7965844579bd | -2.49285 | -48.0653 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6f390552-2713-3b73-9614-6f9c6fd2f9aa | -2.4904 | -48.49325 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99d09f9a-7f32-36e1-aeba-1a60d97b3f2c | -2.48719 | -48.49611 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 963fa8b1-84db-3b79-9039-e8849dae6299 | -2.40802 | -48.55025 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad74c028-64df-3e7d-9abd-b7fc159e70bf | -2.40403 | -48.54393 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 6be63517-bd7c-3143-9068-bfc122b5d294 | -2.40312 | -48.54944 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| eadbbc0d-933d-338d-a212-567dfddd3b85 | -2.39912 | -48.54313 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9c7b9772-dbd5-3072-a1bc-8581f6f1a404 | -2.39821 | -48.54863 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d308eb6d-49e3-352f-89f7-0d8e2fb1d1c7 | -2.39652 | -48.54707 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0f2fdbbe-641e-3ff0-a72a-7b33851dca1f | -2.39421 | -48.54234 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5d16ec5c-5ce7-3c70-b374-fb274d45ed69 | -2.3933 | -48.54783 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 05359adf-0482-3fcd-949a-4aaa3f6417a1 | -2.39308 | -48.10491 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 685f93c6-a07f-31af-9fbd-15a9ed164bc1 | -2.37857 | -48.54545 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bbd6c923-e163-3df3-9038-ab7be289ce2b | -2.376 | -48.54934 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93c287c8-c912-3b32-93a3-d9205013614a | -2.36982 | -47.67109 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d3d79d69-8947-3d6a-8040-38c31ccc25f3 | -2.36519 | -47.67038 | 2024-10-28 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| ee4192d0-fc5a-328c-bccf-9ab47c4e93d1 | -2.33805 | -48.44207 | 2024-10-28 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 201e8b72-b828-335a-93aa-b9bae9f89b06 | -2.33626 | -48.57681 | 2024-10-28 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e481c6a6-b6ec-30d1-98eb-d2d7ce78f3b5 | -0.26147 | -48.78718 | 2024-10-28 04:04:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 98703472-fa03-330d-b62c-75c072714192 | -0.26099 | -48.79027 | 2024-10-28 04:04:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e1dd87f9-79ea-3e70-9e06-ca632c9cf958 | -3.33618 | -50.09359 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9e12747-9bfd-3349-9e0a-0d75c9cd05e7 | -3.33561 | -50.09701 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e777a81-9869-3119-9704-66c66e7c1b32 | -3.31719 | -50.23873 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d47c89d-058b-38af-aa84-1423b1e1cda7 | -3.21967 | -50.17826 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2877635f-7847-3ca6-9169-7e2ec1c00f80 | -3.21909 | -50.18171 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c849721b-edd3-365e-a187-b0739eade18f | -3.21544 | -50.17039 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d66ef18-977d-3b46-905f-6c6111e8c57b | -3.21426 | -50.17736 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32ec5ad9-d5a2-3d0d-9f49-6af1315ad450 | -3.21002 | -50.16952 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85e4047f-0513-3eeb-a1f6-34adfdf87e6d | -3.20719 | -50.21919 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25d9756d-4ab9-3d91-9579-4676c5f8f9df | -3.20661 | -50.22258 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeb065a3-3c05-3753-b040-2ef9cd9f55de | -3.17737 | -50.39547 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0536ceb8-b807-384a-b9a5-0232b872cd01 | -3.17249 | -50.39093 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3742c5c-448a-3441-9803-ddcc3de288ac | -3.17187 | -50.39454 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 25c1e899-6bb9-3b9a-9ae7-a706e461c1cb | -3.16699 | -50.39003 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0833ceb2-d940-3955-a2f7-10e2cf2d9312 | -3.16677 | -50.39055 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3b26b86-f9c3-32a6-a8fa-b2befe655b5d | -3.1615 | -50.38915 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48d78a88-9a15-3ca9-8466-8c783e3619b1 | -3.16127 | -50.38966 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a565989-c5f0-3df3-8644-ad6dbb28b180 | -3.33318 | -49.92596 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8210f56-a9a7-3785-b0f4-d35142871688 | -3.33275 | -49.92031 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed150d4f-d909-30f3-a36d-fb98d949c142 | -3.33219 | -49.92361 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18790ba9-d2cc-37c2-9ef3-f8f4bb68474f | -3.32842 | -49.9217 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55b3284a-7544-3dec-8172-606ebf4c8789 | -3.32788 | -49.92502 | 2024-10-28 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 615db616-deea-3b96-83b2-2ef9f53bcb01 | -3.32311 | -49.92081 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82c33a9c-b917-3504-ab67-ec8b3b798f8a | -3.32257 | -49.92412 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 675312d0-95eb-38c5-9fa6-4144c66ce241 | -3.26755 | -50.0248 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 130ff19f-73dd-366c-8de6-bf1b96b0959a | -3.26699 | -50.02815 | 2024-10-28 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4524ba31-8ebb-3eca-a674-9a60d79ff7ca | -3.25835 | -49.49788 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcf41acc-2906-340a-86b6-9f1e69da0063 | -3.17165 | -49.14969 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10165dd0-2473-3a55-8063-2587f36d416b | -3.16659 | -49.1489 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 71293dd6-4069-3691-922e-b48ea724f8df | -3.13992 | -49.18376 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7c6d061-8efa-32e0-a516-5245d9fb5e22 | -3.13487 | -49.18285 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e81efe4-40fa-3476-95a7-16997a294388 | -3.09992 | -49.47416 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3b3196-d5ff-39f6-b5e6-f966bef71d8a | -3.0963 | -49.47238 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68136947-5b2b-3a60-8744-913ed8b6a31d | -3.09475 | -49.47328 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a38fec04-2752-3ff0-98d2-f4ec2b0c6378 | -3.08523 | -49.30466 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b7aa133-a3f5-3ef3-a81a-55b236d840c5 | -3.08472 | -49.30775 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4459d82-983b-3b64-977b-e0cc3b31bb42 | -3.05448 | -49.49202 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| eb39de8b-893e-319c-88de-3a231ec907ad | -3.05397 | -49.49512 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| faf383e3-91d2-3817-8b30-10e97d2d83bf | -3.05346 | -49.49828 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b3a2409-4af8-3b7b-80c0-c8988350df4b | -3.04981 | -49.48805 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3bde1291-608f-3888-b72b-c674653dbdd6 | -3.04931 | -49.49114 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3997d548-bb9a-3365-b14d-b7d1cb8024c6 | -3.0488 | -49.49424 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c83dbd51-ec60-3a02-90ac-660cb6a895b7 | -3.04828 | -49.49739 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 82434ecc-cbae-31a2-8d17-833f43ffb0e7 | -3.04775 | -49.5006 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0345b7d7-9143-3459-9bf0-d1454a3380fa | -3.04723 | -49.50378 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e35c130e-f600-3118-8f51-c55a8e3d5ce8 | -3.0431 | -49.49651 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae4d3725-f214-3423-946e-920632738d18 | -3.04257 | -49.49973 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8b41b081-46a5-3090-8705-b33d3da78cd9 | -3.04203 | -49.50296 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 840be965-872b-3918-b30e-27e60c9be910 | -2.86405 | -49.24335 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ae45639c-fa52-3663-aaeb-388efd2fb79b | -2.86355 | -49.2464 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2747106e-e3dd-3fba-b931-6a934e60e07b | -2.86305 | -49.24944 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c2cee61-bb57-3bdb-a7b4-49ef788883ab | -2.85893 | -49.24255 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6f96bf0-24e9-3701-8365-0ed5b97c154a | -2.85842 | -49.24562 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cb1bba2-b0ce-383a-90c3-9ed4d13e95a5 | -2.85792 | -49.24865 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c75cabd7-2745-3c3e-b480-044bf3a1a60e | -2.85331 | -49.24482 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 250e9bf3-be85-33be-ab32-98a55524eeeb | -2.85281 | -49.24784 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 739cf9d3-c2e6-32c7-b8b5-adc57e1b79b9 | -2.8477 | -49.24694 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67a1ca62-8d51-36d4-8132-e87c9ed626f9 | -2.84721 | -49.24993 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb3c4dba-e832-3f1a-adeb-38508e9ab624 | -2.8431 | -49.24302 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 298d6054-d5eb-3f8a-8124-0629e22fcc5e | -2.8426 | -49.24603 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a807c885-6f28-3516-afab-88f8ddd07c27 | -2.8421 | -49.24903 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1c3bf62-d10d-3e06-a7ae-3176e257b13d | -2.8375 | -49.24515 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7b299a2-5c75-3b7e-879c-2c14af1d3750 | -2.837 | -49.24816 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acbf3fef-c4ec-3d01-97e4-76a90e27c07d | -2.82778 | -49.24043 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce90da72-14fe-3206-a714-9047c2906629 | -2.82728 | -49.24344 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f13cb315-9acb-3430-9b5c-cd8543ac011a | -2.82678 | -49.24645 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 444a56e2-30ae-3251-92cb-e40fd0173e28 | -2.82627 | -49.24949 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1772e670-1bda-3100-9118-745090534098 | -2.82268 | -49.23956 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f33033b0-4ec9-3592-962a-a7c378040d77 | -2.82217 | -49.24258 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3ca5898c-dada-3272-a070-6e5228221e63 | -2.82166 | -49.2456 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dee0fb66-109a-309c-9131-b48912e4298d | -2.82116 | -49.24863 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db9406b-d4d0-3eba-9997-207bb09ac380 | -2.81601 | -49.23066 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9cece3a8-90e3-3f41-b2ce-c790874e3647 | -2.81553 | -49.23368 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 255dd55d-aa6a-3515-9e8f-53e819f66463 | -2.81399 | -49.22877 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efb5d262-9aa7-3356-8b6d-061b5e930501 | -2.81348 | -49.23179 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 832f4bb5-15c9-3ebc-b4a6-0e8591930118 | -2.81297 | -49.23481 | 2024-10-28 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README33.md)
