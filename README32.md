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
| 55b8bad8-f5b0-3107-98ca-ba833bab2d5f | -1.64161 | -52.24188 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea823534-bfdd-3a74-8fbe-6355d1792377 | -1.64002 | -52.57676 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 411787ea-acaa-37ab-b8ca-0e3a075b9a4c | -1.63947 | -52.58027 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a634a34a-50f6-3e58-96f2-f04b620acbd2 | -1.63829 | -52.24136 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e91ab15-0f89-3d18-a80c-3964963edf01 | -1.6372 | -52.24828 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab4835a7-a8e0-333b-9b85-73abcac48c98 | -1.58236 | -52.2084 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50c6b81c-15bf-3a21-8e3d-bfe9cc336813 | -1.58075 | -52.93303 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a2cb8f-e370-3192-80d4-9628415e2e77 | -1.47533 | -52.28363 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e323662-1afa-31c7-938f-2d1a951c0628 | -1.4621 | -52.3029 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 617dca04-2a07-3be4-bc67-c2b28a35e292 | -1.45437 | -52.30881 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5643588d-1bcb-35b1-8c23-8803ba233bb3 | -1.45269 | -52.29788 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3bd0bf9-58a5-3e9c-bea9-5326742e9adf | -1.45214 | -52.30135 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16428a83-e155-355c-8918-8cc55eec62e8 | -1.43991 | -52.27102 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e0b10b1-161b-34fe-832b-32da3142b676 | -1.43937 | -52.27448 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55fe3e82-5c1a-33dc-9a86-e0e7c0b41567 | -1.43714 | -52.26704 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb2ca6bb-0e37-37c5-b595-c052b531afaa | -1.43659 | -52.2705 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df49c448-3aed-3422-bd5b-d1dddd2f23d0 | -1.43605 | -52.27396 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2edb1b8e-1925-3ba6-9512-dca144356d21 | -1.4355 | -52.27743 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d81aae3d-d7eb-37d5-ba3c-f51decc769d4 | -1.43327 | -52.26998 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 146f62bf-df7f-35cf-9e76-731f65c6f657 | -1.43273 | -52.27345 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 006a4001-978a-3111-ba06-7b8efcd1ed1f | -1.43218 | -52.27692 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3f83dacd-7d83-3552-903f-cc6ab99aca3a | -1.43205 | -52.21301 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b84d10b0-1c36-3414-90ee-4654ea35bf3c | -1.4305 | -52.266 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd6f68d5-1be4-31d7-a7a0-8cb866dbd89d | -1.42941 | -52.27293 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bc9df1f7-e7f5-351f-b603-5d396e6322d4 | -1.42928 | -52.20903 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aea913e-1f38-3809-8702-0d09d6a59171 | -1.42874 | -52.2125 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f02e5cbe-e398-314e-a5fe-87ee70b018be | -1.42706 | -52.80415 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9adb469-9deb-34c0-812d-c97e1147be54 | -1.42597 | -52.20852 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df87b39c-0886-3279-891a-9280f6f83061 | -1.42324 | -52.22583 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41a23f23-0fb6-365d-b1b7-4fa9b25df178 | -1.42265 | -52.208 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d300247-6029-3192-a179-e3e970f978e6 | -1.42156 | -52.21492 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf86797a-5150-39d5-815d-347e82c723a9 | -1.42101 | -52.21839 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a26f48c-abf9-3807-88c9-4bc79a4bb49b | -1.42047 | -52.22185 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a9ab9fe-161d-3397-8555-aef04ad0b4ea | -1.41992 | -52.22532 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cfa1c14-fc5f-3b7c-84d9-94b5938564cf | -1.41879 | -52.21095 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad601cf2-e0df-3361-9e82-62c74ecbdcb6 | -1.41824 | -52.21441 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f9e7a8a-904e-35a0-a671-b0de1ad119be | -1.40403 | -52.30452 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45b9a222-611f-3743-b61b-9f65801af8b5 | -1.40279 | -52.2262 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f8010cf-c1a3-3bef-a314-f631fbbcf093 | -1.40225 | -52.22966 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db97faec-7945-3098-8de4-6e3d185a160c | -1.40071 | -52.30401 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aaba56a-2aac-358e-afe1-84f3fb3efa94 | -1.40002 | -52.22222 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51ad1664-ffb0-34f7-bbf0-ccb7c39d3225 | -1.39948 | -52.22568 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f25faa99-f1c8-3dce-8121-af413b64bbb0 | -1.33263 | -52.19746 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10f201df-83d1-3eeb-a8d2-edde90f89fd2 | -1.23282 | -51.77204 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e0c0d39-94fb-315c-b085-f0b2dfabe796 | -1.23059 | -51.76466 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0170fa25-56a0-3554-ae17-3490bb6d46ce | -1.23005 | -51.76809 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92d55c1-2385-3bfa-a78d-07d656182148 | -1.22951 | -51.77152 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ef0afd2-a56f-3ac5-a7f3-9ddc64bd54d0 | -1.19613 | -52.00591 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 848e8276-3bbe-384a-b4f0-496da366777a | -1.14252 | -52.17458 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 076de885-4f45-3de3-82c4-02f31240306e | -1.1392 | -52.17406 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17b5210d-cbe7-3746-aae6-6ee5579a6ef2 | -0.84836 | -51.94807 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43cc6241-31b1-3c4b-947c-ede077e0d583 | -0.84782 | -51.95152 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e099452d-a3b4-3547-af6e-e8be5d6ec1eb | -0.84505 | -51.94755 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73f1f558-14c1-3462-81ec-e1e121d8c65c | -0.83897 | -51.94308 | 2024-10-31 04:46:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7d000359-4b6c-327c-bd4e-03a57bc9420f | -1.89081 | -52.06198 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e006b01-72a4-3b9d-bb7e-337cf95748e9 | -1.88751 | -52.06146 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b21f622-e015-3ec3-8a89-3ec9781642fe | -1.88696 | -52.06491 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c35cf60-8eab-38ec-8f76-0f908ab62649 | -1.8842 | -52.06095 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27be5ae0-9036-3d19-9a89-5fbd826e2a83 | -1.88089 | -52.06044 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c8b29d1-323b-3d50-81fb-8c04703f8e18 | -1.8577 | -52.03568 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4445c7-1e00-3b84-b046-ad5c0fc569ac | -1.85716 | -52.03912 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4665e640-9157-37fd-a7cd-32941748227b | -1.84578 | -52.00203 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76d925a4-e65d-3e79-bc78-a1a7323c9aa0 | -1.84135 | -52.11779 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd3998f4-0c4e-319b-bc3c-f6359a268c02 | -1.84081 | -52.12123 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 062dded4-5573-35bb-9d0a-1096f933b1e4 | -1.83804 | -52.11728 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ccfc6879-9600-33c4-87d4-6b04a85bcbc1 | -1.8375 | -52.12072 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f39e358-545a-3dcd-a7d3-da13d44409be | -1.83419 | -52.1202 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2f23fb8-2243-3493-90a2-03cab4e7764b | -1.71865 | -51.96776 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92e88ff3-6f62-36e2-b1b1-3d76b44ca8b0 | -1.68403 | -51.99408 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dbf6405-8065-3142-8082-72313603ac3d | -1.60651 | -51.96841 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d357262b-d0dc-362f-b6cb-74b8d2135402 | -1.6032 | -51.9679 | 2024-10-31 04:46:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd38ade0-b920-324c-8a6a-7e6849d871f5 | -1.56153 | -52.03898 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 53c84eb1-7dab-3a21-8336-dd6612e2d37b | -1.55822 | -52.03846 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 048b04ce-bbf1-3f25-acc7-a86771670155 | -1.55214 | -52.03399 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 318663e2-cca5-33d5-99f7-82b0c862bdb0 | -1.53973 | -52.15574 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edab7203-806b-35b3-ad59-5b66affc4462 | -1.53751 | -52.14832 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 384dd745-8a55-3489-b147-e72aac2c3493 | -1.53697 | -52.15177 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ebbdbb7-e78b-368c-b7ab-5b14fe974a09 | -1.53642 | -52.15522 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01ceda5f-a753-3409-92db-6159f0dffe6c | -1.53583 | -52.13745 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b91db20-efa5-3118-ab1a-7197c4f82eac | -1.53579 | -52.11622 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6239917-05ca-3cf1-af81-de87a6806acc | -1.53524 | -52.11967 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d508d45-ef0d-304a-8d8f-c6c951e5928c | -1.53447 | -52.01714 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88d33d83-5624-35f1-a7e8-378974d2df1c | -1.53248 | -52.1157 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3768929-e312-3323-9da1-d96707f7a6d1 | -1.53193 | -52.11916 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 43c66151-b595-3b57-9be1-f5b6d048db7c | -1.52971 | -52.11174 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f80d9b1d-b4df-3b9a-bf8d-09880b828234 | -1.52917 | -52.11519 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2c37b0b-186c-3971-9688-322d8e311a9f | -1.52695 | -52.10778 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6da156bc-2545-38a3-888a-f774b115fe64 | -1.5264 | -52.11123 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5bde03e8-2589-308b-acd9-aac5c2cefa5f | -1.52527 | -52.09691 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11237d3b-62b0-32ec-a622-63d379378760 | -1.52472 | -52.10036 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 845fd78d-8947-3a7d-8032-400cd780fac1 | -1.52418 | -52.10381 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9af9178e-00e0-37c2-9401-74ef9173d338 | -1.52141 | -52.09985 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cba28cfe-45a5-34af-9ef8-7aec5be563ac | -1.5063 | -52.1077 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c9f7562-e3b3-36b8-b822-9e8b09c0373b | -1.50016 | -52.08201 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45a6bc6b-7172-3c6d-b865-f9b6b4bfeeb1 | -1.49685 | -52.0815 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9276ae0-d363-3499-aa6e-3c95199cebcb | -1.48073 | -52.03308 | 2024-10-31 04:46:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8342a3b-029c-37a1-a9cb-d2ba6f91f875 | -1.3985 | -52.05905 | 2024-10-31 04:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4926a0a5-e54d-3bb4-b341-dc0fd25ed81c | -2.07535 | -53.55845 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1214616-14d4-373c-b7d9-4b304cd98dc7 | -2.03945 | -53.94025 | 2024-10-31 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3be5117-db16-39bd-90a1-610a45252152 | -1.86495 | -54.69356 | 2024-10-31 04:46:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README33.md)
