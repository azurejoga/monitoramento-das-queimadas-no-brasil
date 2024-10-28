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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31993b5e-4f4d-3e6f-946f-d94d90238b07 | -3.22968 | -51.19286 | 2024-10-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5229e31a-6537-329b-880e-7e1f85ac81c4 | -3.21777 | -51.29142 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51baf28d-43ed-356b-9fe1-db2017df05d0 | -3.20064 | -51.26569 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c93e7f3-dcc3-378d-ae1c-eef987b676af | -2.94247 | -51.41369 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 214a87f4-9fdd-3ca0-8e54-55370c0238c4 | -2.92391 | -51.75525 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 822c7be7-3434-38d8-914c-4478a0af19a6 | -2.91831 | -51.70256 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecf2b98b-58b6-33b8-9efd-05417f60946f | -2.91602 | -51.76144 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e9d1e27-bedd-3fa1-b509-4d378705ecc3 | -2.91493 | -51.70202 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 381dcdca-bc9b-35a4-b303-be9d8b44790c | -2.91321 | -51.7573 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b86667be-ac69-3d55-a5db-a3fece582d28 | -2.91264 | -51.76091 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdcf72a5-5ee2-30b5-8d2d-aca65d45c971 | -2.88561 | -51.75671 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6be016b6-a844-3ea3-9ece-a1b3e131b9a0 | -2.8845 | -51.83037 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ecd6a91-bbb9-3e8a-878d-b020553c5187 | -2.88394 | -51.83395 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adcaa312-ec80-31ca-abae-ed077a1627cf | -2.88223 | -51.75621 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 27f33b7a-8654-3a0f-bc0e-2dff2c16d6b9 | -2.88152 | -51.30975 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83becfa7-97cb-31b2-af7c-2b830e7caaf8 | -2.88113 | -51.82986 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f658aeed-f1a4-302d-a5b1-2167f498a5d0 | -2.88093 | -51.31348 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c173890-c9a5-3d5e-903d-066f266e038f | -2.87809 | -51.30922 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99eca8ee-9294-3473-9181-69f5f697ebae | -2.87751 | -51.31295 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81e3cc0e-26c7-3702-b524-403e8ab6aac6 | -2.87466 | -51.30869 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef428351-f7ea-3007-8805-fd9402f1172f | -2.87408 | -51.31242 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 843e6490-737f-332b-97f6-1e93a56856d7 | -2.84682 | -51.80619 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23811abd-1ab0-36b6-8a41-fe991b22d0c0 | -2.844 | -51.80207 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 577a97b5-cbea-3ad3-8306-eaf7c3457424 | -2.84344 | -51.80568 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fc19b9e-0a49-3183-866b-41dcfbc6fd68 | -2.84289 | -51.80927 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b64edb25-fbb1-3f28-9cb7-79e5b38413ae | -2.24568 | -50.74529 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd837ad4-de4e-31a6-8a4d-76068b3d1c8e | -2.84233 | -51.81287 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15bbc3a-4ea8-3d1d-8df9-9af99729ca77 | -2.84063 | -51.80155 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2bc2f5c-ee06-3529-839d-2074e3f04236 | -2.84007 | -51.80515 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dea24bd4-7ac7-394b-8919-b5503d83fa09 | -2.83951 | -51.80875 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2709b2b8-4ec4-3a7e-ad4f-aac3451761b3 | -2.83896 | -51.81236 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc2668ff-8148-3890-9e0a-2aed38e2fb5e | -2.8367 | -51.80463 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d803a28-2dfd-3991-bef6-952b2302d5f1 | -2.83614 | -51.80823 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b60b4d9-1c62-31f5-b7da-63d57921d082 | -2.83558 | -51.81183 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 827db9c8-5c01-3376-bf48-c968bfdb54f8 | -2.83277 | -51.8077 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8f20ca1-d473-3144-b355-578c5f4aff92 | -2.83221 | -51.81131 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15b572f4-5511-388a-8d7a-d7d0d84af03f | -3.5529 | -51.55112 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76f4cd1e-5d1f-3e1a-9ee6-747674ce4cdc | -2.42051 | -50.50259 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6adf4a89-f30a-3ed8-a358-525ff115b31e | -2.3416 | -50.92027 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed98ef8c-505d-35a0-8352-0b0c5af797a9 | -2.30122 | -51.92686 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03b6e72b-7884-3eec-9619-ecffe8ef9214 | -2.30067 | -51.93041 | 2024-10-28 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a591abb9-65c8-3f0b-b97e-20e7df17d17a | -2.29887 | -50.49311 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b833ca-93c5-3bf5-bd07-e3885244f770 | -2.29826 | -50.49707 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec1d42af-6d70-3d7e-99fe-f4628e058851 | -2.28742 | -50.66038 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb270853-29fa-39af-9cfa-b3f6c4e2e8bd | -2.28681 | -50.66428 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ea97de6-f77b-3e6e-a8e0-888d2c76d9ae | -2.27232 | -50.64204 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cc883d0-461c-392a-8a81-fe35a7719402 | -2.26531 | -50.64095 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0b8d3d4-8979-3eba-9876-33f68aee90bf | -2.26121 | -50.64429 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a04092d7-b7bc-3536-bdab-6e1be8b10e17 | -2.25775 | -50.78271 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb95262e-e05d-34a5-8120-b4934ace718b | -2.25716 | -50.78655 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ca70f9b-9e3d-3c10-ac86-ce21406bfc61 | -2.25692 | -50.69547 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a205f445-879f-3e98-8e45-1667ae4d2492 | -2.25343 | -50.69493 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1678798-0f70-315b-9da0-fc1ce044f57d | -2.25289 | -51.86876 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e14784a-afc2-327f-bd84-ed9fdda48ad0 | -2.25233 | -51.87231 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eabcbaef-cb7f-331e-b62c-9d886c017a15 | -2.24831 | -50.65828 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58031a2a-57dd-3641-91c1-0e78255b3280 | -2.24771 | -50.66218 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 910effa2-44b1-32b9-99fc-4eb4fb6d9fb6 | -2.24254 | -50.99515 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3e3a779-3a15-3b11-9c59-d4990ef90d82 | -2.23529 | -50.71991 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2fc2712-1ec6-3880-9dea-982d158deccc | -2.23179 | -50.71938 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06b864fd-6f3b-3da4-aba0-3fe1e9abab97 | -2.8281 | -51.03913 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c80ed4b-c319-33f1-8b61-8013fd4d1e64 | -2.82625 | -51.03531 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cc89f99-9125-3fd8-8e7e-f75fa9856d3d | -2.82565 | -51.03909 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30215344-6e18-3451-8c6f-d0bc7f8e9aac | -2.82522 | -51.03477 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d842ad-aa49-30d1-8c5a-de6bbfdec4be | -2.82464 | -51.03856 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 387cf2a0-1237-36a5-8168-d1e33a767cff | -2.82279 | -51.03474 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d63f4574-1ad2-344c-bc99-02ba98607574 | -2.8222 | -51.03852 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1f3a639-7a86-3139-a9dd-3c64d21b454f | -2.81975 | -51.34593 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40a4074d-7281-37fb-8130-652564fa2156 | -2.81837 | -51.6018 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fcc77d6-b155-3a91-af74-f30888220d7e | -2.8178 | -51.60544 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89de7a8b-f53f-3d2b-a946-7feaed4a6f99 | -2.81497 | -51.60126 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f198110a-cac1-33eb-a34e-4e8b924d8350 | -2.8129 | -51.34487 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a153b4f-c589-3c19-ac96-939e178196a5 | -2.81215 | -51.59709 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 708a1984-e0d5-3469-8a71-dc9f9f336786 | -2.81158 | -51.60074 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e093b86d-ba76-3cef-bd8f-4c155eb9a744 | -2.80411 | -51.80353 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4fa55059-8cf5-31e1-b1f3-ca9cd30d0f1e | -2.8038 | -51.02005 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b01e23-12ee-3c7a-8e20-c824b80ce863 | -2.80354 | -51.80713 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a63629de-52ca-3a5e-9661-476ac82189ea | -2.80083 | -51.60285 | 2024-10-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b9b7fa-d78e-3b43-a42d-5936407f61dd | -2.80074 | -51.803 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3f279ead-2755-3860-8327-535b660d4208 | -2.80017 | -51.8066 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 37c828e7-a2ac-3944-8fe7-c4a47b78bf23 | -2.79737 | -51.80247 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0fc2e776-7369-3dcd-ae8b-e205e816e88c | -2.7968 | -51.80607 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 147bc93a-71ae-3301-8c94-c70d803e1297 | -2.79578 | -51.36501 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07ad6385-4a7e-3c47-95ca-b63c4639456a | -2.79343 | -51.80554 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bb35495-7847-3149-9d42-fc6d62751c29 | -2.79236 | -51.36448 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3f8ee1b-2460-3e02-af5d-c6c507293078 | -2.79179 | -51.36818 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ed00703-2cf4-3d05-b572-f2a584f588aa | -2.79123 | -51.37188 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a462451-e4fc-38c1-b85d-84aaca242eea | -2.78837 | -51.36765 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d636077-d262-3da0-bef6-da74fe61b790 | -2.75935 | -52.04508 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb6a52cc-d569-3b09-afd6-6da47338e021 | -2.7563 | -51.7556 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9cd5de9-663a-312a-ab79-82e57a9654d3 | -2.72206 | -51.79822 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cbf6307-2bc8-3fa8-bd34-aaccb2a2aae9 | -2.72151 | -51.80181 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8c1050f-aa3c-32c5-a679-777a79180c4c | -2.71623 | -51.96931 | 2024-10-28 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f14a0a56-d297-360c-84f0-0dac4fa0b0e4 | -2.5461 | -51.16388 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7273dd42-3d0e-30ed-8e14-68358d86194e | -2.54551 | -51.16763 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 376acf4d-2279-3d1e-95aa-1cba54e1683d | -2.54493 | -51.17138 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05343818-007d-34c5-bf50-fa9192559e0c | -2.54435 | -51.17512 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab81973c-9b56-3cfc-bd40-5a7d7fb79ba3 | -2.54376 | -51.17886 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97d622f7-d0f6-38e7-a784-6caa8d835df1 | -2.54266 | -51.16335 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1b99ba8-afcb-312e-9b5d-e53ed515861e | -2.54208 | -51.1671 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8941f720-c958-3373-994c-0ec0715f96c8 | -2.54149 | -51.17084 | 2024-10-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README60.md)
