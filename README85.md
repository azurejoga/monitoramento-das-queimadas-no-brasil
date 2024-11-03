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
| 94f2faee-5ff0-3a38-a233-95e80138abbf | -2.72623 | -49.86192 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7806a79-3fd6-3496-ac7d-f00e9b09aff6 | -2.72546 | -49.85973 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cbd99bae-e053-324a-972d-cd57d70432d4 | -2.71933 | -49.33199 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 35a8c8a7-2ec3-3e45-a4a7-fb136e7fe2f2 | -2.71833 | -49.33875 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d07e17ac-839f-3c02-9ab6-03f02d278c92 | -2.7149 | -49.33165 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1f9d26eb-37d1-3e4c-b70d-c9414d5533ca | -2.71386 | -49.33844 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e19f60c4-1c18-3474-b6a0-163d954ba2ab | -2.71225 | -49.33103 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 824b2f6d-7264-3ad7-bd49-7c133894a256 | -2.71126 | -49.33779 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 717bbfe4-ad05-31c7-8cf4-73cb995ede89 | -2.70784 | -49.3306 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7ac98bd6-3f50-32c6-b042-d7e4f4b96bc9 | -2.70598 | -49.29555 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8bf94c62-7d36-3e98-aed3-163184411e62 | -2.7052 | -49.32991 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 217f9664-dfff-3b9e-9aea-d3c4c904d1a5 | -2.63179 | -54.74735 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b732a4a4-0ef2-3cc1-a654-585fa44f1967 | -2.63137 | -54.75025 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 72d637e1-0a96-3964-8651-dbd70c8f1162 | -2.62682 | -54.74647 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 110c8598-dd16-3f17-9954-2ecc27589da6 | -2.62639 | -54.74939 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3fa30dd8-4c49-3a00-80fd-99eaac25d534 | -2.62618 | -54.74741 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0915403b-55d1-39d4-b1e9-66339fd50b3b | -2.62573 | -54.75032 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c74dabf5-1cff-3f09-b426-49adb2486962 | -2.60492 | -49.82288 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 254c450b-5530-3ed8-a39d-aee086c751d6 | -2.60433 | -49.82262 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 368e1c30-8ae1-38d6-b86e-0266b1e8ba85 | -2.59806 | -49.82192 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14dcc19c-a90a-3a41-b52f-623cb540be05 | -2.59746 | -49.82174 | 2024-11-03 05:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d34fbe8e-9868-35cf-8e28-8cfa41ea5583 | -2.58953 | -53.38066 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 22b910f1-c465-3fcc-b6e4-62c5f74c0489 | -2.58899 | -53.38419 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7327c54b-abc6-38cb-a44b-d9e4c7b18593 | -2.5846 | -53.37627 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e4836af-e5fc-3cb4-ab9b-914cec416f6d | -2.58406 | -53.3798 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bccfbef9-9280-3a91-b263-cbf0739d9d59 | -2.58352 | -53.38334 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73cf3e96-003f-3d77-8727-2c8bc5595391 | -2.58298 | -53.38685 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e0fac73-c12b-3b24-b08c-2dbd4a7f4b4a | -2.57859 | -53.37891 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a54765e6-2496-3a6f-a947-5a3188182125 | -2.57806 | -53.38244 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9ff15395-758b-3046-bee0-63d7e6e2bb4e | -2.57752 | -53.38598 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8cbc560d-6029-3c60-9729-a92b195bd3e8 | -2.57699 | -53.38947 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 573dacb8-22ab-3247-85dc-3e6b4b5b7ae8 | -2.57207 | -53.38503 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8a6bd142-06ff-345e-86c4-0d7975608a96 | -2.57154 | -53.38855 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58ea586d-d61f-39c4-9650-5ae6c1fca264 | -2.571 | -53.39212 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83d20d67-308f-3f8f-9e59-325161b60841 | -2.56605 | -53.38785 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0b1796b-facb-381f-bf17-b4cab5560323 | -2.56551 | -53.39142 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfe2e6e1-d8ea-3573-94c6-132b7c46718e | -2.56497 | -53.39498 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27ec71cb-2dd4-36fb-b059-814ab84687b4 | -2.55353 | -54.00407 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0d87662-4984-382f-b605-00611f85c338 | -2.55306 | -54.00727 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36f12eec-67f1-3ebe-aeaf-2e735739c8b8 | -2.51535 | -54.11716 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37dc16d5-d2d4-365b-b053-220d82041330 | -2.51488 | -54.12034 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 810c5551-a58c-3a79-b1a6-279114befd59 | -2.49791 | -49.08279 | 2024-11-03 05:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0dea5bec-5343-34de-aab0-be5ef21b36c9 | -2.47267 | -54.54457 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5b1a079-ec35-328c-bcf4-b684b6175b48 | -2.47223 | -54.54749 | 2024-11-03 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcf010e9-5bfe-3932-8fc0-0374a4021594 | -2.28633 | -53.78237 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 40d9d3bb-24e2-3bfa-922d-6cf8f69dab04 | -2.28583 | -53.78568 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 25789cfa-12bc-39da-aaa6-5895529350c5 | -2.25781 | -50.43819 | 2024-11-03 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 157a941f-9e33-3dfa-9379-dc1245ce09e3 | -2.19535 | -50.49724 | 2024-11-03 05:31:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93239613-120f-3dfb-be1b-5aecdc48410e | -2.18986 | -50.49388 | 2024-11-03 05:31:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 959b2b4c-3f49-3d42-839b-0fd518657bb9 | -2.18903 | -50.49929 | 2024-11-03 05:31:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea8343db-037f-3991-b17f-b09efd5294da | -2.18879 | -50.49633 | 2024-11-03 05:31:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05cd86a3-7488-39cb-9a5c-d9bb2176e11c | -2.1845 | -53.67528 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 301e20dc-26b7-34a7-a9b8-b45c5d6bc7d7 | -2.184 | -53.67862 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90570dac-e9d8-300b-aca7-18bb37e58def | -2.18234 | -53.72559 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb785ab9-f711-3fd8-b943-7f6ae6be4b92 | -2.18168 | -53.65778 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0573064-b1dd-31b1-bd10-3422dd4a93ec | -2.17916 | -53.67448 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a7a2151-c59c-3da4-9c2b-ad5b7b20cdd5 | -2.17866 | -53.67781 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b42faa76-d64e-376d-b757-19b5c573540b | -2.17816 | -53.68113 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 72869930-1fc4-3cca-95cd-3020263c77e5 | -2.17767 | -53.68441 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 96bc589a-0f71-351f-8a8e-9150c40df99d | -2.17755 | -53.72131 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be7a4fda-309d-349b-96cd-a1304d2921d9 | -2.17718 | -53.68767 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 425a4258-7ce0-3b4b-934f-74bea75f328c | -2.17584 | -53.66029 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 626543df-54b5-3c79-90d9-b23836040bf4 | -2.17383 | -53.67364 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4cb5381-1f03-351a-958b-bd0f0615bb56 | -2.17333 | -53.67696 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0c27d2b-5ac2-3332-8408-d5b90806f923 | -2.17284 | -53.68026 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3011cb89-bf3d-36ec-889f-44362e6709ea | -2.17235 | -53.68352 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 900b0650-80fd-336a-be6d-e37817e3d550 | -2.17186 | -53.68679 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60f74f90-4b7e-30fc-8246-25bcaa1c6ecb | -2.17136 | -53.69008 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d81a7784-dbe5-36ad-bdfe-62ebdd9689cd | -2.17086 | -53.69339 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc730022-8df0-35f0-8c6d-4a785710ac2a | -2.16988 | -53.69993 | 2024-11-03 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9992a61f-87ec-3acf-b554-16e2ac99359a | -2.05575 | -53.25641 | 2024-11-03 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e8fd578-73d6-342c-aeaa-9c863f107efc | -2.04985 | -56.36195 | 2024-11-03 05:31:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0db67d7d-235f-38dd-ad67-3a451c4e1da2 | -2.04637 | -56.35984 | 2024-11-03 05:31:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bc0727a-9cb2-3135-8a35-f64c653eaa34 | -2.0457 | -56.36416 | 2024-11-03 05:31:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 307b4655-5f84-3a6a-85ce-08a279919b2f | -2.04556 | -56.07003 | 2024-11-03 05:31:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 672ee8bc-6b90-3726-8e59-9270affc167b | -2.04543 | -56.36126 | 2024-11-03 05:31:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bceb697c-06ee-3844-b78c-b4bcf26234fb | -2.04487 | -56.07455 | 2024-11-03 05:31:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e3e2c4a-6a5c-362e-a9e8-6bdbb332bace | -2.04036 | -56.07386 | 2024-11-03 05:31:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22f56c6c-6d0f-3011-ae51-cfd5528624cd | -2.03135 | -56.86615 | 2024-11-03 05:31:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54f7d6bf-1e83-33bc-a838-f20cd745f683 | -1.88874 | -52.12955 | 2024-11-03 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47e169b9-ab62-3bf3-aab0-f2a39377bda3 | -1.88809 | -52.1338 | 2024-11-03 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8832b30d-bca6-3795-b85e-d74e7eedd6e1 | -1.88287 | -52.12856 | 2024-11-03 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b5bb180-3570-3210-a839-ac418259b60a | -1.88222 | -52.13283 | 2024-11-03 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19833004-5865-30b3-8341-e06d78f9f31b | -1.87159 | -54.69529 | 2024-11-03 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6d7afe7-05b5-3d29-96f9-5a03ea4a8624 | -1.8707 | -54.69392 | 2024-11-03 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 560a5c5f-ce57-3d40-813a-5c722ec58741 | -1.86746 | -54.689 | 2024-11-03 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e4709c5-db8b-36dc-a45b-024dad66c12c | -1.8429 | -56.27892 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ddc947e-166e-3da8-aca8-dce47b8a13ce | -1.84218 | -56.27693 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c65233af-8c63-3c6b-9eb4-34dfda87f8f4 | -1.84153 | -56.2813 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2342fa4-beed-368c-8e64-a6cda62f5865 | -1.81888 | -55.27805 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c0f7592-2481-3909-95fe-4fb9411801ea | -1.8181 | -55.28318 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 177ae92b-ef3e-3bf0-aa0d-a804b96a2ef7 | -1.80243 | -55.44987 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82d8b457-aaff-3b9d-b0b7-cacbfb85c1a4 | -1.79774 | -55.44915 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fbbec7d-843a-30ef-b655-8938120ac502 | -1.79036 | -55.27383 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d54508dc-beb1-337f-9249-26d5177fae3e | -1.75192 | -55.13931 | 2024-11-03 05:31:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c4172e6-54a2-3e6b-8c34-90aad7e38b2b | -1.75112 | -55.14458 | 2024-11-03 05:31:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecc85dd9-f977-38a3-9db8-228ede0dae01 | -1.74977 | -55.67129 | 2024-11-03 05:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c675516-9ac4-372a-b4fe-58e7d2bf6b5a | -1.72859 | -55.03828 | 2024-11-03 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fd43434-d59c-3c3e-b981-926d5b645e8f | -1.72776 | -55.03914 | 2024-11-03 05:31:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 758dda55-3cfa-3fed-92ab-142d579e402c | -1.71164 | -55.76896 | 2024-11-03 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README86.md)
