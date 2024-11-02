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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7203da54-4377-3959-99a9-64204cb7d8e0 | -2.77992 | -52.8999 | 2024-11-02 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebd4c083-a0c8-36b8-b724-8f17ef94b337 | -2.7741 | -52.89863 | 2024-11-02 04:12:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9558f91-5ad4-3bf7-87f3-4761359951e9 | -2.67613 | -53.02454 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 344ab0b8-4e75-3506-9a73-994d5005af6d | -2.67032 | -53.02287 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca62b62f-474c-3295-8ae5-808bd6d97e54 | -2.57816 | -52.25488 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ccc4d4b-b7ef-31c7-833b-7c3d6079adb8 | -2.57749 | -52.25893 | 2024-11-02 04:12:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a18c58bf-428c-33e5-9a78-51a55f8003e4 | -3.71171 | -53.75609 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ffec1526-d4d8-3eeb-aade-b458e5870a88 | -3.65681 | -53.63496 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c396454b-bf68-32cb-8742-40276e2527e8 | -3.65604 | -53.63947 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e6a5e8b-512a-3f70-bb09-de77dce8c18c | -3.64997 | -53.63845 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 130ca2de-925d-363c-801d-97a1b1346585 | -3.81233 | -52.34597 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88adc7f6-2525-3682-b042-223ea9a6a473 | -3.8117 | -52.34958 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa2dfc5b-bdc1-3156-9440-335fbb1817b4 | -3.79619 | -52.31275 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f18e7803-2170-39b0-b575-f0980497a32e | -3.74773 | -52.36241 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66a0e9a3-53fd-35b2-ae3e-cafea8d4c593 | -3.70824 | -52.4252 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8f7b6a6-5ab2-3d47-95dc-663699babbcf | -3.7076 | -52.42894 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc42665c-a21e-3832-83c7-f15c58be7141 | -3.70494 | -52.42379 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4cc77b37-93b5-3bb8-b7be-0f22fdcf2499 | -3.70433 | -52.42746 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b421b8df-f18b-3fd8-a1d0-357b0a7c4327 | -3.70325 | -52.42068 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b03a15f2-bfe1-3ab1-953a-af2de8847fbf | -3.70261 | -52.42441 | 2024-11-02 04:12:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fab907b-c9d3-3348-9deb-d75d652102aa | -2.18603 | -53.74345 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ec49d53-5553-3657-8f31-8a5cbe9b8f5a | -2.18223 | -53.72742 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d9d9bc7-99e9-3df7-8069-6dfbd532abc3 | -2.18141 | -53.73242 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1466539e-91cf-3954-b021-ec5d7f1b81a0 | -2.17974 | -53.74268 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1de3622e-90fe-331d-8f71-a41c603b2478 | -2.17082 | -53.67972 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a345a13-fcca-3a55-a89d-4df6d0178238 | -2.16918 | -53.68975 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d5a710a6-e007-3a2c-9901-dbf5d92000a5 | -2.16837 | -53.69469 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c7b5b99-56c7-36b0-b39c-fe724a635ab6 | -2.16539 | -53.67385 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e30aff05-8995-3d95-8df0-a9b422057225 | -2.16458 | -53.67882 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d25b1b3-8b61-3694-aee8-65c228db27f0 | -2.16293 | -53.68881 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ef32eb16-d1cf-38ed-9cbf-a11a8cf65e0b | -2.16211 | -53.6938 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a07bb008-bf6f-3781-8ef1-2e538dec473f | -2.15915 | -53.67297 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bfa27379-db42-3a5a-b983-66bbbad86532 | -2.15833 | -53.67797 | 2024-11-02 04:12:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28a67a42-0118-3e38-b243-9403ea92d5be | -3.62577 | -53.96681 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8c3a69af-8b61-3570-871b-3769eca6e9aa | -3.62489 | -53.97201 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c3d236c-2ed7-31ad-9651-e9efa62e4bbe | -3.62488 | -53.96341 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b97904e9-980d-3b0c-84ce-b8864166d2d5 | -3.62397 | -53.96859 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ad7dcd55-3d82-3bdf-adb7-a4c7b999281a | -3.31168 | -54.1396 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81e5705c-c599-3bd6-a7cf-cd1bbe586271 | -3.30879 | -54.13631 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f2a30c54-7b1c-3e06-b74c-d8c53f5e709f | -3.30797 | -54.14127 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a5ee5279-4b5e-319a-8d1f-7b8303d11c30 | -3.30618 | -54.13399 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 089a797b-8fe2-337a-b74b-3e80db312a25 | -3.30533 | -54.13887 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8ed23349-b139-3bdd-b86a-9eabf3f7e545 | -3.30326 | -54.13065 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6adcbd28-e278-37de-989c-0183d7571a65 | -3.30246 | -54.13547 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1070c6b8-8322-359a-87d5-f5aa6ac57c3a | -3.29989 | -54.13295 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 419066bf-2bb8-3402-a25f-8b8a74933218 | -3.28833 | -54.16214 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3c79cd2-c39e-38e8-bd66-d66fbae9eb91 | -3.28737 | -54.16764 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01720e6e-d194-3b00-93e4-15f28d2eafaf | -3.26966 | -54.17665 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0a7f500-fa7e-33f2-a356-26f7ddbc1d50 | -3.26591 | -54.17899 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 083c388a-725e-3b0b-a092-19feefb09925 | -3.26337 | -54.17545 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 89d8c7d4-8905-339b-91cf-deeb6574cd17 | -3.20456 | -53.85219 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 691c50c7-e2a7-3974-93ef-6530df783c18 | -3.20376 | -53.85696 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 568d5627-6aab-331e-bc66-6753a35f744c | -3.12845 | -54.26536 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 604c269f-4889-3e5c-aab4-f4dac4ea6c6a | -3.12384 | -54.25396 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3aa3f985-3273-3377-9d32-17dd621df4ec | -3.12299 | -54.25897 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e392dc8e-b4a3-3667-b0e8-2970aaa21671 | -3.12214 | -54.26397 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 26aed42c-3ed7-3cdd-8522-360ff9fc300c | -3.1215 | -54.30647 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1c1bb7-94d9-36bf-a676-cf0c09224821 | -3.12129 | -54.26899 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5edd42a-dc1e-338a-9a5a-932e32a18409 | -3.12043 | -54.27409 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7040e8e7-67fd-39b2-aaa0-572b9bbc683d | -3.11955 | -54.27925 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3f16b1a-e7d3-3adb-b3bb-c9ad522e6eb4 | -3.11666 | -54.25773 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| af06b36e-6031-3354-9d35-30d6ffac5422 | -3.11603 | -54.30007 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f7006841-bc20-39a2-8f6c-52e40fa989c2 | -3.11581 | -54.26276 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 94f96721-2d8e-3a1c-b14d-367389e96013 | -3.11511 | -54.30548 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3650e57f-4375-3e7f-a172-3f3cebf84229 | -3.11495 | -54.26782 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8feba0d-8bc7-3acd-b31b-62ee145b06f2 | -3.11408 | -54.27295 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 01e08a6a-6091-3ab2-965a-0b1b3309ac5b | -3.10966 | -54.29897 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3875925-22f7-36b2-b8cf-d9b592988e77 | -3.10684 | -54.27701 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a80ac24-a98b-3910-b019-fff1d1b7ce3c | -3.10596 | -54.28222 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34d915d1-51ea-3975-bc33-a67819a1eed8 | -3.10507 | -54.28744 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2353804-1f26-3f3c-a344-3f5eb803350e | -3.10419 | -54.29261 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d498cac0-b195-3bc9-adcb-33b9caf43fad | -3.10329 | -54.29785 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2aab096-b1f8-3866-b05f-6dd497358213 | -3.09959 | -54.28114 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93c36025-0e8c-3562-8a46-f01f9324ae40 | -3.09871 | -54.28632 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b255fb8b-75e8-3bdb-8693-969cf714d92a | -3.09782 | -54.29149 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa559fde-b8ac-3400-814b-2dc623de9911 | -3.09522 | -53.71516 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f60105fa-05e6-371a-a825-273d12d02180 | -3.09441 | -53.71992 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8182319c-d94d-3ef3-9467-8930d3046320 | -3.09322 | -54.28008 | 2024-11-02 04:12:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86d1c231-dfa8-3ab1-a54e-790f4e4245e9 | -3.08002 | -54.16707 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01249648-9565-3d09-bc60-f14c098f6448 | -3.07918 | -54.17194 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36ae427f-0cd6-3da7-8759-7f6519b3417b | -3.07688 | -54.16861 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 56223bed-6eb4-344d-825c-3954652a7b88 | -3.07372 | -54.1659 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2104cb59-5db9-396a-9fc8-1cf87a450d3e | -3.07287 | -54.1708 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d860a2b-a65d-3fb8-8013-bc73254e9d32 | -3.07058 | -54.16739 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e132fc54-2293-3db4-81f3-bc496276255c | -3.06975 | -54.17236 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0c6cdbeb-7bb1-330b-9d1e-f29008ee19da | -3.06743 | -54.16466 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff387564-3738-3129-8f62-27914d020813 | -3.06656 | -54.16964 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6fe819e-35cd-3b56-ae39-2bf13a412cdb | -3.06428 | -54.16616 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a4e87d10-c238-342a-8881-d4b715bb908c | -3.06344 | -54.1712 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0b92537e-dfe0-3f9f-93d9-3968c73306d2 | -3.06113 | -54.16343 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 601e4f0d-bc5a-39f3-98a6-dd74dbb26ad0 | -3.06024 | -54.16852 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0cefb17c-ae8a-33dc-afc1-bc215f32df9b | -3.05797 | -54.16502 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a470e563-60a8-35f5-955b-f279cab3dea7 | -3.05711 | -54.17015 | 2024-11-02 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc857f20-1262-3728-94cf-b03da6660c00 | -3.03609 | -53.80127 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97878351-4fee-39c1-a458-5bdc5f2feb32 | -3.03149 | -53.79878 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfeac7eb-b52c-36cc-b2ff-99bf5b7baa42 | -3.03076 | -53.79528 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9f5e987-ba7d-3964-85c0-b8f4bedb4f9d | -3.03064 | -53.8039 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c4fce39-06b1-35ac-b405-d9bb99aedffc | -3.02988 | -53.8004 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a3718e0-d18d-32f7-909d-2c4e622935b5 | -3.01202 | -53.87777 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fcbda7b-31bf-39e8-841a-d673a2d6411e | -3.01071 | -53.87429 | 2024-11-02 04:12:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README53.md)
