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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eb9072c-43ec-33d5-ba22-2a063431af3b | -2.89245 | -50.47141 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b85444d5-74b3-3fee-9151-c3a9c7c5d87e | -2.89184 | -50.47543 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7629ef21-3623-313c-84c0-11eae302c900 | -2.88565 | -50.3996 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ce8ef45-a6dd-3ff2-884f-25ecaa869f99 | -2.80033 | -50.27768 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba3da760-2e89-31ef-83c9-68e0ba5f95f1 | -5.16518 | -49.48642 | 2024-09-28 05:08:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b7d0d782-76fd-384f-9c6d-efefb92f11a4 | -3.68592 | -50.18911 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73a1b4b5-8718-3a18-84f5-dc98ed2519a8 | -3.68149 | -50.18842 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf8c8654-7868-38e2-9741-94d933865754 | -3.58016 | -50.55919 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a83330a1-8dab-35d3-aa27-c3473c6dd07a | -3.57785 | -50.55754 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4c283b48-57d2-36fc-8ab5-20692499fc25 | -3.57648 | -50.55439 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd311ae3-6dfe-3b6e-96b8-848d7163d174 | -3.57583 | -50.55857 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e3d70c1-efc2-3866-895f-cf4e275b9d55 | -3.57443 | -50.39322 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afa4810d-c82f-35eb-a2ee-4c00df583c5a | -3.57392 | -50.57099 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a059ea9b-f637-3c17-9c81-61693aabf276 | -3.5738 | -50.3974 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b49aa453-50bc-362b-a1ce-ba5684b567be | -3.57259 | -50.37588 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fba2beb-da5e-3621-b3a5-36be27ab573b | -3.57151 | -50.55798 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad42d13f-4dba-389b-9b79-9c9b760f87d5 | -3.57006 | -50.39257 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea3a03ce-9fb1-34be-b8b2-bb7813cb3212 | -3.5696 | -50.57041 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0a8f517-7e3a-3256-b032-803e26f3d7f0 | -3.56943 | -50.39677 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c718dd60-a27a-336a-8819-7945751e70ab | -3.56897 | -50.57454 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3062ebf2-7fcc-35ed-a408-05f89d9b54de | -3.56833 | -50.57867 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f78be58c-dc64-3b5d-85a1-bc40caeb842a | -3.56822 | -50.37524 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1503e8a5-890f-3c10-a34b-0d1d0134945e | -3.56592 | -50.56566 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c20a6392-78ea-3744-8cc1-8a4ddceba5ba | -3.56401 | -50.57809 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0921f279-074c-31e3-ad89-25842e8240f7 | -3.56386 | -50.37449 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d4509b8-8325-3139-8253-ce0e4d7f3d66 | -3.56338 | -50.5822 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f8f2b2d-91a9-3756-9109-781157249220 | -3.56321 | -50.37878 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90f06780-32de-3915-9696-7d51c52f84da | -3.56259 | -50.38293 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36d7bd1d-56ce-3625-8d23-33cc095e5629 | -3.55885 | -50.37809 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7231535e-1817-3169-82e9-c9f2ad1fd902 | -4.40562 | -50.6967 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f41805a-af79-3635-a5f4-283800c0b812 | -4.40498 | -50.70089 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70c64d37-f890-38cf-aa17-bbcdc8452a6e | -4.40128 | -50.69606 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7f7fdff-1cda-36bd-b15d-088ab616d1ff | -4.31807 | -50.75102 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0de91ed-948b-309a-8bd4-37aafd070103 | -4.31748 | -50.75507 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ac36d78-90b2-33c2-a7fb-786391b3a7a0 | -4.06474 | -49.94228 | 2024-09-28 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d2f0014-3d2d-3e61-8091-310bd6ae2321 | -4.06271 | -49.95586 | 2024-09-28 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8664c453-7e74-379e-abdf-2f1885540a5f | -4.05816 | -49.95528 | 2024-09-28 05:08:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0752e2f9-048a-312d-8865-637b0e9e827f | -5.97564 | -49.6633 | 2024-09-28 05:08:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6337b267-dd20-3e70-afa8-7fb542e2322b | -5.97515 | -49.66215 | 2024-09-28 05:08:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06aa2670-fa32-3b16-bab5-d5483bdc1b11 | -5.97447 | -49.66674 | 2024-09-28 05:08:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d60cf717-c1f4-3f26-a73d-bffbd7c23eac | -5.78432 | -51.03727 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64d69b01-774c-3f29-9220-be77fab7a5d1 | -5.78175 | -51.03917 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad4e2c18-4e7a-346d-b0f0-66bd34f44bc7 | -5.73039 | -51.07395 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dbf7a167-fc09-338b-b808-0df425e88b2f | -2.39401 | -51.28412 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3eba0d0-5a72-32c7-8f2d-92648f4efab1 | -5.72664 | -51.06956 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9ad5b95-3ead-3022-92da-60d41cb9cb2e | -5.72608 | -51.07341 | 2024-09-28 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c245e9f-6bc8-3ea9-83eb-e41b42c47c8a | -5.52692 | -50.53637 | 2024-09-28 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c7f120b-b765-36be-87ec-fee02c0c3667 | -5.15663 | -50.75618 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 67ebd544-b4e0-376c-a566-cb0d4ee747c1 | -5.15226 | -50.75556 | 2024-09-28 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1cdf1d3-ab37-3ba6-bd70-2aa640a8a92b | -7.09306 | -51.25483 | 2024-09-28 05:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ffc111f-6174-3751-92ce-996701bf2742 | -7.08495 | -51.24959 | 2024-09-28 05:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 006c27a7-5590-3977-b1ee-73a341dc1334 | -7.08178 | -51.24068 | 2024-09-28 05:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfb53369-bb6b-30aa-82b0-f9669f2ea76e | -7.0812 | -51.24477 | 2024-09-28 05:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cde45e49-d6ff-32c2-a6d5-2593acb3d607 | -7.0801 | -51.25252 | 2024-09-28 05:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67aeeb84-47b8-3b1b-90b0-10c678e3227a | -7.8094 | -50.23252 | 2024-09-28 05:08:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97d9324e-e296-3c91-8f47-4c088e50e622 | -8.73315 | -51.01251 | 2024-09-28 05:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15bcefcc-fd58-37ea-b93e-8095cb5c571f | -8.6991 | -51.01485 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 978173ae-a2d7-31f6-9fed-81bd0829d686 | -8.69629 | -51.01237 | 2024-09-28 05:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70c655d9-d72b-3633-8fe2-4e7ddeb9a925 | -8.60516 | -51.74267 | 2024-09-28 05:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a6cc715-152b-38ba-a480-0aee6182136d | -2.12716 | -51.127 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a82b7f70-620c-3757-bb25-bdcf38beaa5b | -3.49563 | -51.17638 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89aeb4aa-3340-39c9-a64f-0dd34b52f33b | -3.46681 | -51.37133 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c02cacd7-f758-3318-bfaa-e605b0c42cc4 | -2.58327 | -51.92025 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8172f712-a0c8-35b5-acb9-f3f7b34cb5ea | -2.58252 | -51.92511 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f4a2c15-2272-39e1-b606-a287555f8604 | -2.39108 | -51.27644 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9738232a-5cc0-3be6-8e73-9d18a8774cb7 | -2.38997 | -51.28352 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48dae937-4e44-35ff-87bc-bda1ca7126a7 | -2.38648 | -51.27938 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e1aa162-2849-367f-b87b-27499648a2d9 | -3.38738 | -51.51301 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eaa3c300-22ef-302c-afa9-bda3c5937f68 | -3.38685 | -51.5165 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e5c927d-d8f1-3c45-9db4-31aa911f92f2 | -3.30403 | -50.66475 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfbc7a58-6f18-3a39-bcd6-85cf0d587ebe | -3.30342 | -50.66877 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9dfcc876-7d86-349d-98d6-f8ab24144f12 | -3.29976 | -50.66412 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88cf4a56-9861-34b4-8d7d-3f3424288784 | -3.29915 | -50.66814 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91004463-87d9-369c-a011-41cd074b1fa5 | -3.19638 | -51.15168 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d27706-a862-37b3-9147-756bcec38433 | -3.19583 | -51.15539 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe186ff5-fa2e-3a42-b6b4-3fef9c23241d | -3.19281 | -51.14735 | 2024-09-28 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52d4018d-2f34-383f-ac60-cfaeade7ff85 | -3.10733 | -51.24724 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7211abc9-70cf-34af-b4dd-b71405ccd887 | -3.10678 | -51.25087 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6460aef-db78-39af-a8b8-67cea10379be | -3.10214 | -51.25384 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b37337b9-6f84-300b-9e3f-c0140c3d4cd6 | -3.09805 | -51.25321 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9fb775d-7495-3219-81db-43e261ec2a50 | -3.09661 | -51.29019 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97397be0-46af-3e8b-b345-dc24b191881d | -3.09253 | -51.28957 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6e2e5e3-0770-345c-b6bf-235f7a279ebe | -3.07218 | -51.34142 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37886f04-3dfd-3a25-8c66-98cc247aabbb | -3.07165 | -51.34496 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c90feeb4-b282-3f53-821b-75da8ad56d74 | -3.01849 | -51.06567 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2f87c14d-f8bb-3be5-a141-797f88a15291 | -3.01661 | -51.05014 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed1f2a2a-7133-38f1-aef1-0d08164c2d8a | -3.01604 | -51.05387 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb8253c5-2178-3543-af10-c2488093b6ab | -3.01548 | -51.0576 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 599da0ee-e2dc-3f98-b652-0d379978d9e6 | -3.01491 | -51.06133 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5b7728e-e78d-3cf6-a0ca-6e8c3cefe8c0 | -3.01247 | -51.0495 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4e75f77-e210-30fe-9f3c-056c207ce739 | -3.0119 | -51.05324 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d75d4b05-89fd-3180-8c94-2171146ef8e6 | -3.01134 | -51.05698 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d4da2ce-d77c-319f-b849-d519b99ec07e | -2.95778 | -51.65197 | 2024-09-28 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75f2f116-6d10-3daf-9584-ca3996fd3043 | -2.88211 | -51.38639 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd471339-0973-3dda-af06-1b46926c39de | -2.8786 | -51.3823 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce654089-43bf-3eb0-964e-5042907f1a6c | -2.87842 | -51.67411 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 105a1f16-895b-36ff-8580-10b6b5189987 | -2.87806 | -51.38583 | 2024-09-28 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02fd2320-47da-3af0-9b5b-f0872fdf25b4 | -2.87766 | -51.67116 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b04f7540-5ccf-35b6-810f-9380688c858a | -2.87763 | -51.67918 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bc6427c-40bd-364d-a3b4-8d7f37c140ac | -2.8769 | -51.67625 | 2024-09-28 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |


[Clique aqui para ver as próximas entradas](README72.md)
