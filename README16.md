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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44135fe9-fb61-3821-a232-6360d5555f57 | -3.3277 | -50.2615 | 2024-11-03 01:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 71c2d794-ce82-30c6-ad6b-69675661e189 | -3.4749 | -50.3826 | 2024-11-03 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| d33c67bd-1e68-3187-85ca-00f8e10ad41b | -3.5465 | -50.882 | 2024-11-03 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4855d396-23c7-3c21-93f4-a9d3fd67880e | -3.5466 | -50.8611 | 2024-11-03 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2f39246f-a687-3c65-8f59-a6b5c9f820ec | -3.6092 | -49.3219 | 2024-11-03 01:35:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 4f4df4f6-1f0a-3e92-86a5-e08c624ac73a | -3.9473 | -48.3666 | 2024-11-03 01:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a7964687-5662-39cc-b2f2-16fbac4ac510 | -3.9474 | -48.3451 | 2024-11-03 01:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| b53b62b2-c8ba-3e71-8db1-b8c6d1459e99 | -3.967 | -48.15 | 2024-11-03 01:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8d430aa1-8552-3e2f-ad7d-bd5c4901ca14 | -4.4056 | -43.4514 | 2024-11-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 347.4 |
| f3c0307d-bfa5-3faf-9d9a-33a4865de5a8 | -4.4054 | -43.4746 | 2024-11-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 252.2 |
| d5695ec1-a7b8-3506-b1ad-cde7ec6a0458 | -4.4058 | -43.4282 | 2024-11-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| b102ba2e-fef1-379f-89a7-e784f675b7da | -4.4241 | -43.4735 | 2024-11-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 0165142e-3db8-3298-972b-a76efb86d7cc | -4.4243 | -43.4503 | 2024-11-03 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 210.3 |
| de55d8ee-d042-3be7-a0d8-e97784d747ea | -4.6159 | -42.808 | 2024-11-03 01:35:32 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| ce7d3d08-4205-3aa0-b216-ddcfa95f20a4 | -4.6161 | -42.7845 | 2024-11-03 01:35:32 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 545f2dec-8aaf-3283-a763-cd7c49d1bff3 | -6.5239 | -41.4929 | 2024-11-03 01:35:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| d2290b98-8bf7-3cc3-b438-bad9d0bc06ab | -8.7059 | -48.0181 | 2024-11-03 01:35:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e261811f-434b-363e-8a04-16a8df6ea90b | -8.7247 | -48.0163 | 2024-11-03 01:35:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| d573dc84-3f03-32cb-a574-a489b9b2e48a | 3.28276 | -61.02358 | 2024-11-03 01:37:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 94745f18-6008-33a4-a012-df013f82df42 | 3.28148 | -61.03263 | 2024-11-03 01:37:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 840f2fd6-1a40-33aa-9518-2f0c72c74f56 | -1.2755 | -53.4138 | 2024-11-03 01:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b2e1ed8d-2eaa-3b54-a368-3ef20ed3968b | -1.2755 | -53.3936 | 2024-11-03 01:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 47fac0ea-bc72-3c99-87e8-ee77392e1c8e | -1.2756 | -53.3734 | 2024-11-03 01:45:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 85ee9aa7-316f-32d7-86e0-4eb4b62ad69f | -2.1746 | -53.6834 | 2024-11-03 01:45:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f765af56-31a1-35f4-bbf5-8656098ee840 | -2.2802 | -48.8082 | 2024-11-03 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1dc9f56b-8d57-355c-ada6-639512bc1ef3 | -2.2986 | -48.8078 | 2024-11-03 01:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 8baa7938-94c5-352c-ae1e-0f92e1467f2d | -2.6322 | -48.5634 | 2024-11-03 01:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 4bab7090-a2cd-3912-bac7-1ef6deb6c303 | -2.6506 | -48.5844 | 2024-11-03 01:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| ca9d920f-8b25-329d-ab6e-026aa4f15693 | -2.6507 | -48.5629 | 2024-11-03 01:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6fb7e31e-a7b3-3fd4-8342-8d9bfd6bd97d | -2.5796 | -53.3927 | 2024-11-03 01:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 9be6e2aa-d756-38b0-ad3c-071cad9b46d3 | -2.5797 | -53.3724 | 2024-11-03 01:45:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| b0e7550e-ea28-364c-bcd1-a64f25b1ac60 | -2.6321 | -48.5849 | 2024-11-03 01:45:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 85854cae-812f-3159-a8b9-4ff9d2956a2e | -2.7033 | -49.33 | 2024-11-03 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4172cac4-310c-3054-aeff-27c433966568 | -2.7218 | -49.3295 | 2024-11-03 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 6b9e5259-8c77-39b7-9798-600975113d42 | -2.7876 | -51.6099 | 2024-11-03 01:45:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 788c6a87-8dbc-303f-aff3-09d8ced1f46d | -2.7419 | -54.4353 | 2024-11-03 01:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 212.3 |
| 648d5a10-c82b-3cf7-8fef-9034d29c1e91 | -2.7419 | -54.4153 | 2024-11-03 01:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 170.4 |
| ee0db8c4-bfef-3601-9d0a-30938c57f0a9 | -2.7602 | -54.4349 | 2024-11-03 01:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 139.7 |
| cf9fb5e4-34a1-3e3c-a405-d676f7837d97 | -2.7603 | -54.4149 | 2024-11-03 01:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 641fd5d2-67fd-3fa6-bbbd-2667feaf011a | -3.055 | -54.1474 | 2024-11-03 01:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 1eda4d59-863b-38b2-abd0-e0487d7cca4e | -3.0734 | -54.167 | 2024-11-03 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 1f0d1346-b4ef-397a-80b9-9b3b383bfaff | -3.0734 | -54.147 | 2024-11-03 01:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 143.7 |
| c77990a2-5145-32f1-a48d-0160c63b345c | -3.1059 | -50.3105 | 2024-11-03 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| fc682a3d-ceae-38dc-9522-4879f260d75d | -3.106 | -50.2896 | 2024-11-03 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 234.0 |
| 4e0a83ec-2e6b-3000-b50e-a81847aa8506 | -3.1061 | -50.2686 | 2024-11-03 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| a70441bd-c346-31c6-bf29-cc8b2183cbcb | -3.1245 | -50.289 | 2024-11-03 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 8990e842-9d6c-306c-8577-d2e518992157 | -3.2047 | -53.4179 | 2024-11-03 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 4565fe32-c3db-3a23-8d9f-29508716b14a | -3.2415 | -53.3967 | 2024-11-03 01:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5b24fbbf-1634-34ce-8aa6-9919ba136f58 | -3.3276 | -50.2825 | 2024-11-03 01:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 799e774f-8870-322b-8d58-999fa0eb42b4 | -3.3277 | -50.2615 | 2024-11-03 01:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| bb3811d1-003d-3b5d-876a-228ad87dea60 | -3.4749 | -50.3826 | 2024-11-03 01:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| defabe6f-75b4-31a3-a4d0-2ee8a6d4191f | -3.6092 | -49.3219 | 2024-11-03 01:45:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c28c0757-c376-3b82-9563-716d90d0c147 | -3.9473 | -48.3666 | 2024-11-03 01:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| f07ab1e5-177d-3bf6-ba73-57f08915510f | -3.9474 | -48.3451 | 2024-11-03 01:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 68b110df-1aac-370e-92d2-36bf47235cd4 | -3.967 | -48.15 | 2024-11-03 01:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 74676683-5712-3d36-b493-8540a1bdc4f9 | -4.4054 | -43.4746 | 2024-11-03 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 222.4 |
| ffebe8a6-0b91-3a1d-9eb5-1b6dba552808 | -4.4056 | -43.4514 | 2024-11-03 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 261.4 |
| ed93bd9e-070e-375a-b7ed-361a829ab7c5 | -4.4241 | -43.4735 | 2024-11-03 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c71c1683-2a50-35ec-9931-0312b44b4653 | -4.4243 | -43.4503 | 2024-11-03 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| de5ba18f-7109-3e2e-a596-a8cf66749a19 | -6.5239 | -41.4929 | 2024-11-03 01:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 4731db8b-10f8-380c-9435-f389c4d66f51 | -8.7059 | -48.0181 | 2024-11-03 01:45:55 | GOES-16 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 14612e80-95fe-39c8-b24c-e798a4417683 | 2.5498 | -51.0981 | 2024-11-03 01:54:51 | GOES-16 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 38.3 |
| eda0da7f-3f6b-3b19-bfc6-b06a6305c64d | -1.2755 | -53.3936 | 2024-11-03 01:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| a3a5bb3e-be69-3c11-b497-6c847d3f705a | -1.2572 | -53.3938 | 2024-11-03 01:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d2f77502-82cc-367b-ac0b-ae7a8a6219f4 | -1.2755 | -53.4138 | 2024-11-03 01:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 975329d0-f8c6-347c-814e-43a5784f4995 | -1.2756 | -53.3734 | 2024-11-03 01:55:13 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6a71e991-d97b-33f5-a9f1-ca8fa36609cc | -2.1746 | -53.6834 | 2024-11-03 01:55:18 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| a6742fc8-0491-3cd6-8ead-10fc46af5cb8 | -2.2802 | -48.8082 | 2024-11-03 01:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1d8ea9f8-9c02-355a-8754-17c5cc45dd8f | -2.2986 | -48.8078 | 2024-11-03 01:55:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 38552085-9713-382f-818e-829a0bec12fc | -2.5796 | -53.3927 | 2024-11-03 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 712ab388-1aa5-3bb9-a371-5a77462de812 | -2.5797 | -53.3724 | 2024-11-03 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 18005a78-60ea-3e9c-8943-76c02ea05c52 | -2.6321 | -48.5849 | 2024-11-03 01:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f8b86717-2c0b-3e80-896c-8fd1f19e7823 | -2.6322 | -48.5634 | 2024-11-03 01:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 8f364969-5865-3753-b6b4-a5cc09087429 | -2.6506 | -48.5844 | 2024-11-03 01:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 697b19b5-fc8f-3e0e-baea-881c9e86f094 | -2.6507 | -48.5629 | 2024-11-03 01:55:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d4fb73e6-0d3c-381c-824f-5b5814c8105b | -2.7033 | -49.33 | 2024-11-03 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 0ca699a0-a83f-3eaf-9584-9a4fe4ffbade | -2.7218 | -49.3295 | 2024-11-03 01:55:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| ccfb2480-2626-32ee-a551-08bf0edd6bbd | -2.7419 | -54.4353 | 2024-11-03 01:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 39d3791b-dd14-3cd2-a361-245fa1495e23 | -2.7419 | -54.4153 | 2024-11-03 01:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 2c4cdee9-96f1-364e-ad03-f9357cb05075 | -2.7602 | -54.4349 | 2024-11-03 01:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 183.4 |
| a0933ca3-1839-3e2c-b72d-840b4964c5d0 | -2.7603 | -54.4149 | 2024-11-03 01:55:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 171.1 |
| e87fe3a3-ed29-33ab-a557-17a82666e20e | -3.055 | -54.1474 | 2024-11-03 01:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bf045b32-71e0-3f07-8af6-e74bb7d9dd34 | -3.0734 | -54.167 | 2024-11-03 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| ea19bc87-d960-38a7-a87e-5edd1db5340d | -3.0734 | -54.147 | 2024-11-03 01:55:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 50873f93-bc7e-32ca-b4b0-dc7285c5f5f1 | -3.1059 | -50.3105 | 2024-11-03 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 24ef1347-aedf-380d-8b27-3ec2bb980d56 | -3.106 | -50.2896 | 2024-11-03 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 218.4 |
| 93278da6-fabb-370b-8081-926493c2e1c1 | -3.1061 | -50.2686 | 2024-11-03 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 503bc520-525b-3e97-97da-1ff4fa02b8a5 | -3.1245 | -50.289 | 2024-11-03 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ca1044a4-b9b4-3335-b95b-378bcd4da216 | -3.2168 | -50.2861 | 2024-11-03 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 9faf02b5-ea81-3104-9df7-9f846fd237a5 | -3.2415 | -53.3967 | 2024-11-03 01:55:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 362f1340-1892-3b3e-8b5a-9c1d36f2ff4d | -3.4749 | -50.3826 | 2024-11-03 01:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| b6abd7c8-cc8c-3ad3-b710-461c672132cb | -3.6092 | -49.3219 | 2024-11-03 01:55:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 5b1e97e1-50ca-3f76-a59e-8bc2538b8e35 | -3.9473 | -48.3666 | 2024-11-03 01:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| dfabea63-9a31-3812-b284-2037b1b4c25a | -3.9474 | -48.3451 | 2024-11-03 01:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e41901cf-d091-3e44-bbec-c0e68947cc48 | -3.967 | -48.15 | 2024-11-03 01:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6e8037df-c4a8-3723-8cc9-ce45e3247a36 | -4.4054 | -43.4746 | 2024-11-03 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 4434b407-91ac-3171-9bc8-31203842e9f9 | -4.4056 | -43.4514 | 2024-11-03 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.8 |
| e9c32850-a90a-3a65-acb6-f9fb4ca84f04 | -4.4241 | -43.4735 | 2024-11-03 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 96fb704c-7af7-3456-aa39-7973af9cd4af | -4.4243 | -43.4503 | 2024-11-03 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8276fc18-5bd7-3818-b806-4a2ef71ad197 | -13.3712 | -61.321999 | 2024-11-03 02:03:23 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
