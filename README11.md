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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f01f8727-165c-39d1-b8d6-843ba4e47639 | -17.764 | -57.5526 | 2024-10-23 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 9b0a8a49-77e2-3bf9-b316-865f09928036 | -1.3879 | -52.0072 | 2024-10-23 02:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 486e5149-7a44-3888-8e90-84e5772195c7 | -1.388 | -51.9867 | 2024-10-23 02:15:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1a19e012-cd2d-3e7b-be34-c96838c7f276 | -2.5225 | -54.0992 | 2024-10-23 02:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 5f94e3d1-f2e3-3ae5-9389-6720b2ef17fb | -3.0917 | -54.1666 | 2024-10-23 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d5bcb549-c3c5-38e2-8c6b-1f8c48f03a23 | -3.1101 | -54.1661 | 2024-10-23 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 9d24d6e6-8b33-3518-9f79-944997d2dba7 | -3.1102 | -54.146 | 2024-10-23 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 4f675e66-23d7-3c52-8da4-f6128fbe2c79 | -3.5491 | -54.7351 | 2024-10-23 02:15:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 339ae958-346f-30fb-9286-0f72bcef28ba | -4.1719 | -47.9894 | 2024-10-23 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 207dbe1f-6c2d-3bd5-be2f-57b0918de3f0 | -4.1905 | -47.9885 | 2024-10-23 02:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 49566c42-73fe-3936-a4a1-7c11ed67538e | -4.7254 | -45.7363 | 2024-10-23 02:15:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 17b037ba-6624-37e0-94b3-41d4d94c50af | -5.2305 | -43.1886 | 2024-10-23 02:15:36 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 9eedd83f-9ac8-3315-89cd-02b80c61e93c | -11.6115 | -48.5521 | 2024-10-23 02:16:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 01f7f3d3-9869-354b-8144-e49d62f63fc6 | -11.6118 | -48.5301 | 2024-10-23 02:16:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c675a115-3afd-3c16-a811-c8643ae5ad9c | -17.7637 | -57.5732 | 2024-10-23 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 9925299a-7ebf-395f-a9ad-b5682187a52a | -17.764 | -57.5526 | 2024-10-23 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| b83afb2d-3879-34c7-915b-543b0e651acb | -17.6868 | -57.4593 | 2024-10-23 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 827899ad-c876-33d3-98ec-4e9146180310 | -17.6865 | -57.4798 | 2024-10-23 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 43266ea9-d51d-3272-a7f4-33ca45646e46 | -18.3004 | -56.2222 | 2024-10-23 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 1ea3217f-e4ad-3345-8e5f-e532a403faaf | -18.3008 | -56.2013 | 2024-10-23 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 49cabe30-baed-31b9-a2fd-ab1bf1961381 | -18.3203 | -56.2195 | 2024-10-23 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.4 |
| ec2e54f8-d3a5-3024-821f-cc8b2e137a27 | -18.3207 | -56.1986 | 2024-10-23 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.2 |
| ce39255e-b091-3527-aac0-144c08f15bf5 | -19.5465 | -56.6983 | 2024-10-23 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| eb305463-a8bc-3ce4-8ac1-9cc7f61b93ac | -19.5469 | -56.6773 | 2024-10-23 02:16:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 120.1 |
| 9a1b816c-69de-36f3-919f-910e203a691c | -19.5669 | -56.6744 | 2024-10-23 02:16:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 8d013a95-f43b-3ba4-8e95-a1eb45996f7c | -17.67444 | -57.45726 | 2024-10-23 02:21:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| d93d8342-d506-3e0f-a10e-72882bb5c31c | -17.67277 | -57.46479 | 2024-10-23 02:21:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 592e2066-dcaa-35e9-9a55-e3de5991de55 | -3.0917 | -54.1666 | 2024-10-23 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 054ffda2-76de-3ab5-a8d9-1c07498210ff | -3.0918 | -54.1465 | 2024-10-23 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1b184c9c-a1e6-3fa8-bacd-47150454ec3c | -3.1101 | -54.1661 | 2024-10-23 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 231908f7-9f19-3690-a4e3-ae005e9f85e9 | -3.1102 | -54.146 | 2024-10-23 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| c708e71c-ec05-3039-bfc8-811a583a5841 | -3.5491 | -54.7351 | 2024-10-23 02:25:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 71371de8-09e3-339c-8883-c0467809911f | -4.1719 | -47.9894 | 2024-10-23 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 2971ecb0-40a3-3166-a4f3-8cf01ff08ddd | -4.1905 | -47.9885 | 2024-10-23 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7eca7b31-e774-3823-8c0d-6da1f22cf8bd | -4.3841 | -49.7571 | 2024-10-23 02:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8f103e7a-006d-33cc-a372-e145550a8382 | -4.7254 | -45.7363 | 2024-10-23 02:25:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 72da9968-c4af-3e11-bba5-230daa698b1a | -17.6865 | -57.4798 | 2024-10-23 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 4574baf5-403c-396f-9c84-1bcc8fedda16 | -17.6868 | -57.4593 | 2024-10-23 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.8 |
| e0deb3c0-8e01-31e5-81d5-db16eb8449ec | -17.7637 | -57.5732 | 2024-10-23 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| ffd4ba84-cdd2-3ba0-822f-84efe63c2510 | -17.764 | -57.5526 | 2024-10-23 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| 420960de-4085-3f32-b1e5-39f7b7d4ec40 | -17.7848 | -57.4885 | 2024-10-23 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 92749211-90e5-3505-a693-e06b80a830f8 | -18.2633 | -56.0812 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.9 |
| 4ab9aa74-b2ec-3497-91c6-968c8d753d8f | -18.2637 | -56.0603 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 40101748-5c89-38ba-b1bf-fe7aedd0b2d7 | -18.2836 | -56.0576 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.7 |
| 4b60f0c3-7d67-3020-9993-6ed2bfb63675 | -18.3004 | -56.2222 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 8058f6f7-5db5-353f-a0bf-58376e0251b9 | -18.3008 | -56.2013 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| 18cf25c8-8034-369c-b1d8-5ffd61143439 | -18.3203 | -56.2195 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 5b45161c-c5ec-330a-be16-8d39690bb202 | -18.3207 | -56.1986 | 2024-10-23 02:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 9ce1f529-599f-3a9e-a5ad-9f32780cea92 | -1.388 | -51.9867 | 2024-10-23 02:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9e6739c2-d99c-3f93-bb93-940f930ab637 | -3.0917 | -54.1666 | 2024-10-23 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 53aceceb-f22e-3c33-b2be-ca5748368d50 | -3.1101 | -54.1661 | 2024-10-23 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 211.8 |
| 6bdabae8-6564-3934-9499-5971a1f538df | -3.1102 | -54.146 | 2024-10-23 02:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 478ea51c-4d5a-371d-8511-049f85af9e50 | -3.5491 | -54.7351 | 2024-10-23 02:35:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 152420a9-91c3-39a8-af17-b5ca313b270c | -4.1719 | -47.9894 | 2024-10-23 02:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 18c6cdb5-0b86-36aa-bcae-b0f7f6bff345 | -4.1905 | -47.9885 | 2024-10-23 02:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 91188b10-98e1-3159-ac14-3fe034201e9c | -4.7254 | -45.7363 | 2024-10-23 02:35:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9782236b-f49c-3afe-9a4f-4d848f0aa490 | -6.5213 | -35.2214 | 2024-10-23 02:35:42 | GOES-16 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 69bef1b6-f604-34ff-ac4d-5d50a259ae9c | -17.6865 | -57.4798 | 2024-10-23 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.9 |
| 5875a3bb-8305-349a-8a61-4faf17b16418 | -17.6868 | -57.4593 | 2024-10-23 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 94211548-87e1-31be-952c-aa0da8c73287 | -17.764 | -57.5526 | 2024-10-23 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| a370e14c-325b-3bb3-9089-57622f403056 | -17.7637 | -57.5732 | 2024-10-23 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 4e6ddbfc-2ef2-3613-bc2c-7459942c5e08 | -17.7644 | -57.532 | 2024-10-23 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| f4555ae0-e6d5-3197-9a5c-50b09b21a3b7 | -17.744 | -57.5756 | 2024-10-23 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.2 |
| 2d5066f6-82c8-3888-b330-281f905a8b2d | -18.2637 | -56.0603 | 2024-10-23 02:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| b3025cb6-2fa2-3f5f-952b-c2deae79f1f0 | -19.548 | -56.6143 | 2024-10-23 02:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| 2f0aa5b8-1049-367c-9d5f-cf66bd5ce2af | -1.388 | -51.9867 | 2024-10-23 02:45:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 405bd00c-c19a-3168-87e1-8f4f06a012df | -2.7614 | -54.0338 | 2024-10-23 02:45:22 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a153ae56-94be-3d0e-b788-51a1d01eca43 | -3.0917 | -54.1666 | 2024-10-23 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| e282d4fb-1b7e-32b2-8537-80d84d338d44 | -3.11 | -54.1862 | 2024-10-23 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 0585b106-4949-347c-89bc-19d0cbcca969 | -3.1101 | -54.1661 | 2024-10-23 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 53358847-31ba-3145-8b6d-38f6427c57bb | -3.1102 | -54.146 | 2024-10-23 02:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 662cbf0a-f9c0-38b0-a27d-020e3d8470e7 | -3.5491 | -54.7351 | 2024-10-23 02:45:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| c0c55b25-480b-3b68-beaf-991f9c959c6e | -4.1304 | -45.6112 | 2024-10-23 02:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 4eea27c6-3263-333f-a72d-00e4f451cebd | -4.1305 | -45.5888 | 2024-10-23 02:45:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 5c625ff6-8e79-3235-82ae-f45f60aefdb6 | -4.1491 | -45.5878 | 2024-10-23 02:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 2dcd5819-d84a-3094-9b80-9c094453be9d | -4.7254 | -45.7363 | 2024-10-23 02:45:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| d891555c-0891-3ecc-bcf1-a72d1f214aa0 | -11.6115 | -48.5521 | 2024-10-23 02:46:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 26334a66-3927-30a2-a11c-82fdd4dc59f5 | -17.0184 | -57.5178 | 2024-10-23 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 6c2d6d9b-5903-35ff-93cd-b9c2c2887869 | -17.0188 | -57.4973 | 2024-10-23 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| ad7779b3-d875-380f-b817-b54b61bc43e1 | -17.764 | -57.5526 | 2024-10-23 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| c7cdfa7b-9fea-3cf4-830b-73f74bdc7c30 | -17.7062 | -57.4774 | 2024-10-23 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 2dcb04a1-d96a-3740-9c77-82978c346b57 | -17.7637 | -57.5732 | 2024-10-23 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| a7c678e9-19fe-354f-a997-bcd633ae7231 | -17.7065 | -57.4569 | 2024-10-23 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| b767cbf1-9610-3336-af0a-66f989d02275 | -17.6865 | -57.4798 | 2024-10-23 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 0c4d5bb6-7bba-3233-9c20-74b6410d30fb | -17.6868 | -57.4593 | 2024-10-23 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| b4a774c6-dd05-38d0-b73c-a4943abb0a14 | -18.3004 | -56.2222 | 2024-10-23 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 00fdabad-c80a-3fa6-ae55-d950675b8231 | -18.3203 | -56.2195 | 2024-10-23 02:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| bf94e3dc-35ec-33e4-91f9-a5df276d51d2 | -1.388 | -51.9867 | 2024-10-23 02:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e0bc57fb-1407-3985-976e-a0899628b427 | -1.3879 | -52.0072 | 2024-10-23 02:55:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 197c1a1c-b1ec-3a66-9947-6d04433e618c | -3.1102 | -54.146 | 2024-10-23 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 7e247b7a-bca3-385e-a016-b08a337edb27 | -3.1101 | -54.1661 | 2024-10-23 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 179.6 |
| e12c1b88-acfa-3045-a4c1-05b39c03e5b3 | -3.0918 | -54.1465 | 2024-10-23 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| cdbeaece-c027-3bff-8ca3-3ee13553618f | -3.0917 | -54.1666 | 2024-10-23 02:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 5bf02083-7cb8-3d10-84b5-00523ed7690f | -3.5491 | -54.7351 | 2024-10-23 02:55:26 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 36549a91-837a-3c38-a711-b0ccda4fa17c | -4.1306 | -45.5663 | 2024-10-23 02:55:29 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 37ee0cf4-6d09-3745-94ac-7941226808dc | -4.1305 | -45.5888 | 2024-10-23 02:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 462.9 |
| 73c98ae6-2bac-3faf-a903-f7cbc014deb7 | -4.1304 | -45.6112 | 2024-10-23 02:55:29 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 302.9 |
| fd441822-887d-3a24-a583-910d233a4662 | -4.1491 | -45.5878 | 2024-10-23 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 144.8 |
| 6573b400-55d1-36e9-90b1-89ea2461652e | -4.149 | -45.6103 | 2024-10-23 02:55:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| e6aa8f5f-f507-37b3-be79-acc84bc21c98 | -4.7254 | -45.7363 | 2024-10-23 02:55:33 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |


[Clique aqui para ver as próximas entradas](README12.md)
