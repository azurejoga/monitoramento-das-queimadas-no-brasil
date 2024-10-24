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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f32c3c9-13ed-39c5-b9ff-6079a5072da2 | -19.62727 | -56.76764 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9f72ba1c-f620-3657-a58e-017fbcc541bc | -19.62679 | -56.7486 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f81251e6-4d10-36bf-902a-3df1876cab4f | -19.62671 | -56.77126 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 70a20327-129d-302f-97d7-eb3f15525464 | -19.62622 | -56.75228 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 340477cd-dc29-3678-8bb1-6926a346edac | -19.62565 | -56.75596 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5be35ef8-9137-329f-8305-0d263d8423c1 | -19.62508 | -56.75964 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9a6a41c4-d7d7-34f2-ae59-c70be1a58cfe | -19.6246 | -56.74066 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cbf7ab63-059e-39b9-9b2a-78e3a78463c6 | -19.62452 | -56.76332 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9fb28a5-1ece-34d1-baaf-cf6d10b3129e | -19.62395 | -56.767 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c4bd0dfd-14fe-329f-a9ca-c2f63df2c7b1 | -19.62175 | -56.75907 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9afb9c04-bfef-3917-b8e6-f04ca4f2b13f | -19.62118 | -56.76275 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 08b4d0ec-aa1c-319c-a7df-4d676d63a2ed | -19.62061 | -56.76643 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 994feb52-2981-37b7-b0f5-a8cbe01f94a1 | -19.62004 | -56.77011 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 77c93503-fd27-3aa8-b579-5cc2c638cc1e | -19.61614 | -56.77321 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 899c34a3-3122-32ce-9a47-2ba98ee204c5 | -19.57914 | -56.53288 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e72b1359-4d06-315c-ab22-f338cee2130a | -19.57056 | -56.61087 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1d4be469-d22f-35aa-b4fc-39321acf867f | -19.56849 | -56.55758 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6f137973-88c3-38e7-b6e4-0184eb6f7045 | -19.56772 | -56.6293 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4933ab5a-b732-338b-8f70-70b861e0cc6d | -19.56268 | -56.63979 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| da856d47-e693-315f-914c-9a8a0ee80f60 | -19.56041 | -56.65452 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b64d2f69-d410-344f-a732-2f7b1797459b | -19.55998 | -56.61283 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 952d24d6-5764-3981-b60e-db067e5c6cc6 | -19.55984 | -56.65821 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| fe18369d-4c2b-3d22-9c73-e1860b2f1e32 | -19.55935 | -56.63921 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0bd881c8-11f4-31dc-83a6-ad8f1481276d | -19.55821 | -56.64658 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 16aa3d69-936b-37f8-8b3c-d1a8110fd634 | -19.55544 | -56.64232 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0ef65525-06bd-31a6-94ee-ff4776ec7afe | -19.55487 | -56.64601 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| da96695d-6872-31e2-9824-8000a6daaf64 | -19.5543 | -56.64969 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 28dd5841-fc16-3ad4-b544-1aa18c2daea5 | -19.54039 | -56.65108 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e51cc75e-b6d4-3a2f-8869-49e51aa92bdf | -19.53706 | -56.65051 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7151a6ca-cda9-3079-96fe-72b065c45abd | -19.53649 | -56.65419 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dd202ed4-e3ae-3f59-a85b-f4f18eee4742 | -19.53329 | -56.57496 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 47641ea1-afab-30ea-96e2-e4c41a692549 | -19.53259 | -56.6573 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| eb60ca21-173a-3d44-84a8-aa63ca756388 | -19.52824 | -56.58545 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e12505ff-a3ee-3fc6-b2d4-4ad0ee81cbac | -19.56878 | -56.64462 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 77498cfe-f797-3ef5-a86e-e8f62ec8da73 | -19.56098 | -56.65084 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ccc29911-cbfb-3287-9cdf-e77d3200c569 | -19.55764 | -56.65026 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 26334e27-8962-3ffe-b8db-408abbb0978b | -19.5565 | -56.65763 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5d396fb9-91c2-3371-85ea-0da063ab7fa2 | -19.53983 | -56.65476 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| dc9108f0-3ba4-3e15-a8d7-17adf4ca0216 | -19.58916 | -56.53459 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7894a600-0826-3ad8-b31f-6cb18099724b | -19.57523 | -56.536 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2226b8d8-22fc-36e1-9c7b-ce25551a910f | -19.57106 | -56.62988 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ecb3a738-fef6-35b9-9242-144b2176869c | -19.56723 | -56.61029 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 4a60b1c0-525a-30c3-baa3-f15041672a23 | -19.56672 | -56.59136 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2eecb66c-70f7-3e99-834a-a3978c466d47 | -19.56572 | -56.55332 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fb9f4f93-a852-39a8-9ee7-b9572fad4c7b | -19.56515 | -56.55701 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 15008813-c5e1-32ba-9ede-66e005b006f5 | -19.56509 | -56.57972 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8e4991d9-8b89-3f4a-b0d6-8a51f3c92b40 | -19.56446 | -56.60603 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 339d2f32-a201-3c5f-8597-1990653fb375 | -19.56389 | -56.60972 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| a5be5ee1-08fc-38d5-999c-8caef45bf9f4 | -19.56332 | -56.61341 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 221c3a3f-b519-3d00-8996-e72b09510cc2 | -19.56281 | -56.59447 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 20ea678f-7160-3161-b57b-1f4beb68b41c | -19.55904 | -56.55217 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 743e1e38-1cc7-3d78-8efb-c8e840ac9a18 | -19.55778 | -56.60489 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 5713d88e-0e6e-361f-8ca5-0ed0a42a5f69 | -19.55665 | -56.61226 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| fea7a882-ffcc-3cd1-be77-ef349f4b2b1f | -19.55608 | -56.61595 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 85c959a6-98b1-30ab-aa11-7e4c6def6f76 | -19.55274 | -56.61538 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e0f235b5-d981-3360-8526-cb40d9b199d7 | -19.54997 | -56.61111 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 707f15cb-f9b8-3fc9-b6c9-d5aa0aa5e7da | -19.5433 | -56.60997 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 98378e24-6d61-34db-8545-f242bc9eb257 | -19.53505 | -56.57457 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 279c9e3c-933a-3bf2-bbb9-0b7bf5e8921c | -19.53215 | -56.58233 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 768ef714-d156-36d3-8837-0918b8382aa3 | -19.52769 | -56.58905 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 141fd3ab-bb03-3db3-a8b3-360700a168ff | -19.57113 | -56.60718 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 0e2ab68d-7207-3ca7-95e9-69defd7563ef | -19.56786 | -56.58398 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 582af703-9074-33b5-bfea-4f590afc163b | -19.56779 | -56.60661 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 54bc7d47-30d0-362c-97c3-3ce28183f417 | -19.56666 | -56.61398 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2cf91f0b-9d13-3498-944c-fdc4c5a4c7f5 | -19.56338 | -56.59079 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c637bac5-35b0-3f32-99ae-58659d1adec2 | -19.56275 | -56.6171 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7a067007-79c8-302d-974d-6212cbda3a3d | -19.56169 | -56.60177 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f1bbbc3b-b835-3e00-8bac-55ee7b968a7b | -19.56112 | -56.60546 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| a2510c04-cb70-32dc-b586-ffd0cc49cb88 | -19.56055 | -56.60915 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 7a78b8bd-a37f-3233-be67-1ecda0964eb9 | -19.55848 | -56.55587 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3c826a81-d54e-3160-a748-558800a694d5 | -19.55791 | -56.55956 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ec40b2f2-a116-3f69-9d78-6cebb21b8428 | -19.55722 | -56.60857 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 87787396-002e-375f-a079-1949f05e1059 | -19.55715 | -56.63127 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 09974ccd-ff31-3a44-9f45-65167846f3a0 | -19.55514 | -56.55529 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 75f62c6c-5cd6-39b7-b8e0-6fe8463bb688 | -19.55457 | -56.55898 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0bc8827c-9bd4-3780-a516-5b89b315f353 | -19.55111 | -56.60374 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 65df4b0f-9557-39b6-90e2-84432b87e93f | -19.55054 | -56.60743 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0803081d-1ecd-3fba-8757-cb561fd7e5d1 | -19.5472 | -56.60686 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 63ae443c-a89b-3270-86f5-92de18ac5368 | -19.53448 | -56.57826 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 560d1aa4-3d63-3b14-9c32-449b588d19a6 | -19.53392 | -56.58195 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e8e4b35a-1c97-35e1-b826-43df998caa16 | -19.53272 | -56.57865 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9446140a-da17-37ef-9aca-26fbd77c5556 | -19.5154 | -56.60208 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2893263d-7a6d-30ba-9526-d6d113174728 | -19.58582 | -56.53402 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a720e77f-2d9f-38bd-aa73-b598b6a109e9 | -19.58248 | -56.53345 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3a2b78c4-5f06-3168-b911-828f0752d9f4 | -19.57006 | -56.59193 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2c2637ec-efae-3c6f-9724-194dedabe515 | -19.56238 | -56.55274 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c21d2a4e-9052-39e0-9266-d938ddfd696a | -19.56219 | -56.62078 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 74f60f36-0a02-3ff0-9f02-2a5536165e96 | -19.56181 | -56.55643 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4caa0150-2f4a-391c-9796-dc817107fcad | -19.55942 | -56.61652 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 364c4f7e-908d-3c15-94d3-5d12ef132b3f | -19.55828 | -56.62389 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 39178eeb-db3b-3e82-8551-02721050dd2b | -19.55771 | -56.62758 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc05fc72-1694-3c44-8c79-41c90ec462f4 | -19.55445 | -56.60432 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 31f17bed-5fed-3c25-9f0d-d81ef3ab1a31 | -19.55388 | -56.608 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1c098af7-7f58-35d0-ae4d-91e97fd5db8d | -19.55381 | -56.63069 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8d820e9e-8e45-35bd-a1f9-ae1ccec5bddb | -19.55331 | -56.61169 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0fb51aaa-012d-313f-8da6-7db1500f2eaa | -19.52378 | -56.59217 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a8c52046-2b05-300a-9280-93474f8d437f | -19.5193 | -56.59897 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a1e3134d-c891-3915-975e-d6afc90e3945 | -19.51702 | -56.6137 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f2b679b-b898-309b-88ea-ca81fdb4db21 | -19.51597 | -56.59839 | 2024-10-24 04:59:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 25ceb5d4-d09a-31f0-8fc9-84c2fcb13336 | -19.51255 | -56.6205 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |


[Clique aqui para ver as próximas entradas](README86.md)
