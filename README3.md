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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 087c229b-af29-3b33-bdfe-3acd829879a2 | -6.9459 | -40.8692 | 2024-10-24 00:25:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 8bab931e-cd35-369c-8ebc-4b4181931a04 | -6.9461 | -40.8447 | 2024-10-24 00:25:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 366.2 |
| 94bf09bc-c463-3848-b2e6-9aa2c3aab212 | -6.9464 | -40.8203 | 2024-10-24 00:25:45 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 121.8 |
| f95dfdbd-acc1-3aa7-b0f3-1c952c78f45f | -7.0979 | -45.7914 | 2024-10-24 00:25:46 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| ab9aa79f-fe7f-39c4-b652-3b564f4d0473 | -7.481 | -63.5577 | 2024-10-24 00:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 171e750f-6a18-353d-8a89-eeb31565d5bd | -7.4995 | -63.5571 | 2024-10-24 00:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| ab4c69e0-92cf-3b4a-835e-39b271728fa7 | -10.1969 | -53.8822 | 2024-10-24 00:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| ba5eb808-1dbf-3cbe-b907-fd809873f795 | -10.1971 | -53.8617 | 2024-10-24 00:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7cac66e9-d79b-35b9-a65d-4a41128bddbf | -11.5924 | -48.5544 | 2024-10-24 00:26:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2836726a-d882-3db1-b40d-8af7e41eb0df | -12.1404 | -43.4659 | 2024-10-24 00:26:14 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 9595f3eb-5ca3-3682-b8d9-319cbbf4a41e | -12.672 | -43.8517 | 2024-10-24 00:26:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4764e10f-a94a-39d2-b694-cb3395dc95be | -12.6914 | -43.8484 | 2024-10-24 00:26:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 7fe90508-6ce2-3fed-bfee-6089c6d963f7 | -12.6918 | -43.8247 | 2024-10-24 00:26:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| aa0448ef-c10f-3684-a7ca-811b52975d1e | -13.7609 | -54.0661 | 2024-10-24 00:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 7979919f-a9a3-3ade-a265-55406fb2382d | -13.7612 | -54.0453 | 2024-10-24 00:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 06725c07-e84b-351b-9f44-8e62c4ff4d73 | -14.9145 | -45.1224 | 2024-10-24 00:26:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d3006fa6-3a65-3fbf-bb3a-4479ac8bb0bc | -14.9341 | -45.1187 | 2024-10-24 00:26:30 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1e90b7e1-b1b2-30eb-876f-ca958264ac3a | -15.5389 | -50.6688 | 2024-10-24 00:26:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 121744bb-fb3c-3193-8c15-ef8b160ca200 | -15.5393 | -50.647 | 2024-10-24 00:26:33 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b1a5e717-dddc-3b1f-ba63-07dfcf0fed17 | -15.558 | -50.6876 | 2024-10-24 00:26:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| cb9f5f3a-0af0-38da-a86c-62dff2f105d1 | -15.5584 | -50.6658 | 2024-10-24 00:26:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 7b563a5a-e6f6-38a4-b035-f5f18fcd7ff0 | -15.5589 | -50.644 | 2024-10-24 00:26:34 | GOES-16 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 7bfa2553-ee4b-31fb-8998-4cbf39842458 | -15.578 | -50.6628 | 2024-10-24 00:26:34 | GOES-16 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3347fe67-4049-382a-b960-9c2f17d9b99f | -16.94 | -57.5268 | 2024-10-24 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 6f3b72a7-4d79-3503-b0dc-687dcf04be8f | -16.9596 | -57.5245 | 2024-10-24 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.2 |
| f5d1cdb2-74d5-3f09-a656-fe6e756d6c21 | -17.0207 | -57.3743 | 2024-10-24 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 34c33288-1eff-3d2e-9805-2cfc8c5c5860 | -17.2383 | -57.2462 | 2024-10-24 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 2d184e22-ae7a-36ea-815e-1d2cb7ceb5fc | -17.2579 | -57.2439 | 2024-10-24 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 0ad3d396-2809-36ff-8fdf-1911cc6112e5 | -17.6671 | -57.4616 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 9ae1b132-94b2-3578-b80c-e2d6e0c51155 | -17.6865 | -57.4798 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| a7ecccf9-f312-39bc-8098-83d5b230dc6f | -17.7062 | -57.4774 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |
| edb71caa-d204-3f88-afc8-7ed5a657a55b | -17.7453 | -57.4933 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 41796196-b7ed-33eb-9178-145dda403fe5 | -17.7634 | -57.5937 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| db498a05-7353-3f5e-9e1e-d97f7937708f | -17.7637 | -57.5732 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| d4bf0c4b-339b-3459-98d3-d6765817eaa1 | -17.765 | -57.4909 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| 4e9b6443-1b12-37bf-91ec-6910108923af | -17.7831 | -57.5914 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| fce2ad21-dbad-35b9-b73f-cdd099268d91 | -17.7834 | -57.5708 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.5 |
| c6126b8b-91b9-3cf5-acc7-a6e4ab1e04ae | -17.7841 | -57.5296 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.6 |
| b09c655e-e09e-343a-a04f-6d9fc5209fc3 | -17.7844 | -57.5091 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 32542a19-3518-3f9d-8cfa-7d4dd2367e45 | -17.7848 | -57.4885 | 2024-10-24 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 3747e1ba-8212-393c-a30a-33c02770e217 | -17.9667 | -57.2191 | 2024-10-24 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.2 |
| ba4c6a39-060a-3474-aef9-f4c4c2a3fdbb | -18.0639 | -57.3101 | 2024-10-24 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| da8f2e09-a70b-3ac4-82e9-37d632593f35 | -18.0834 | -57.3283 | 2024-10-24 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 2c211c0f-24dd-3a97-9eba-a6cfbecbea05 | -18.0837 | -57.3076 | 2024-10-24 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.5 |
| a3dae445-76fb-385a-a44b-c772ba6ba60d | -18.1032 | -57.3258 | 2024-10-24 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 69bbef24-efe9-3808-b850-0751e381b033 | -19.7061 | -56.7386 | 2024-10-24 00:26:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 315ba685-7664-38b4-8883-a56ca7dff287 | -23.795 | -55.2753 | 2024-10-24 00:27:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 52.4 |
| 426f0330-03ef-3a98-a51e-8f7d9fd06440 | -23.816 | -55.2713 | 2024-10-24 00:27:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 37ca10aa-2dd6-3439-8c0f-0b25a74c1b06 | -1.5878 | -53.3089 | 2024-10-24 00:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| b0b18ffd-dc31-3edc-87d5-611e97bdf68f | -1.6062 | -53.3087 | 2024-10-24 00:35:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| c5c41cd2-be5f-394c-a0b6-525f0b91fee9 | -2.9578 | -50.4198 | 2024-10-24 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 43a98d0a-fa93-3372-b77c-c0947c12bc73 | -2.9763 | -50.4193 | 2024-10-24 00:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| cb9a3b48-395d-3436-8e4b-6e5abd761947 | -3.0745 | -53.8252 | 2024-10-24 00:35:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 81cde6fd-d421-3b67-82c0-934cabee0d4f | -3.1101 | -54.1661 | 2024-10-24 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 03542337-30b9-343f-8bc1-42fa39d0942f | -3.1102 | -54.146 | 2024-10-24 00:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| d148719b-819a-31ff-858d-0f2748287fc3 | -3.1606 | -50.4766 | 2024-10-24 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 1b1e6500-27eb-35bb-94f5-1c4dfc867438 | -3.1607 | -50.4556 | 2024-10-24 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6a928df9-2170-3925-a743-e9572b8642be | -3.7066 | -41.6997 | 2024-10-24 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| bb8c3bfe-0b03-3c03-9f0c-4db45e35301d | -3.7068 | -41.6758 | 2024-10-24 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| a178c666-e66b-3ac7-8f45-a4137485330a | -3.7254 | -41.6987 | 2024-10-24 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 9846cd77-ab95-31c6-82d0-f0c93af56c87 | -3.7255 | -41.6748 | 2024-10-24 00:35:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 2ce8cef7-2257-3c1b-ab78-8c70ea14a0e4 | -3.6612 | -54.2715 | 2024-10-24 00:35:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| f3bcad55-f9dc-35cc-8e41-46ea87a03047 | -3.6613 | -54.2514 | 2024-10-24 00:35:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d458eabd-0c3b-37a3-8e8e-4b5faae5bb57 | -4.5698 | -43.9967 | 2024-10-24 00:35:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 097ef949-1b8e-39ac-91b6-d1164f1c4c76 | -4.5574 | -45.7905 | 2024-10-24 00:35:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 76ad0281-ff27-3d2b-9dd5-179c267a6e70 | -4.5697 | -44.0197 | 2024-10-24 00:35:32 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| d67e05d0-fdfd-391b-bdd6-bc627746bf36 | -4.6586 | -44.6328 | 2024-10-24 00:35:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| dd46b81e-1408-3b55-9107-6dd5df7d1a92 | -4.6588 | -44.61 | 2024-10-24 00:35:32 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 2ec8eb1a-ac0b-3477-bd55-d8826b70b6d0 | -4.6775 | -44.6089 | 2024-10-24 00:35:33 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 6d544a89-8df6-3e9e-9a96-57660849597b | -4.758 | -46.4033 | 2024-10-24 00:35:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9a27642d-6b29-315a-849a-0824d43a87a0 | -4.8423 | -45.0309 | 2024-10-24 00:35:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3fe1cd3a-0832-3d45-8b51-794941e72522 | -4.861 | -45.0298 | 2024-10-24 00:35:34 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| b3428e63-8d31-3046-9cc6-feba5d099c1e | -6.7238 | -40.4754 | 2024-10-24 00:35:44 | GOES-16 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 02c72b2a-4f22-3b4b-be05-c60f9d6fe1c3 | -6.7427 | -40.4735 | 2024-10-24 00:35:44 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| c1f280fe-ec09-3c93-a2e7-56c4f7e60358 | -6.9272 | -40.8466 | 2024-10-24 00:35:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 191.4 |
| ef487788-67a2-3a69-9350-9f18d7c573c1 | -6.9275 | -40.8222 | 2024-10-24 00:35:45 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| b868a3f3-7e04-3dc3-b12a-f05147f7942f | -6.9461 | -40.8447 | 2024-10-24 00:35:45 | GOES-16 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 261.1 |
| 559b5848-9598-3986-8fb7-8747677881a2 | -6.9464 | -40.8203 | 2024-10-24 00:35:45 | GOES-16 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 279cc753-ca25-3ca7-9ed2-cd0e3178134d | -7.0977 | -45.8139 | 2024-10-24 00:35:46 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b7125663-5a13-3985-9a5e-a1286cfc589a | -7.0979 | -45.7914 | 2024-10-24 00:35:46 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 35a0bc95-487c-3b7c-98af-15a7c9bac188 | -7.481 | -63.5577 | 2024-10-24 00:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 0b80219a-6281-3e9c-a74b-f7f75a0f9ca3 | -7.4995 | -63.5571 | 2024-10-24 00:35:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c216b2e5-8281-3926-b7e7-030f77e68466 | -10.1969 | -53.8822 | 2024-10-24 00:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| b5cea9fb-7753-30a1-9306-457f930b4a33 | -10.1971 | -53.8617 | 2024-10-24 00:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 642b9783-a561-37ec-a4b9-91f2d50440d3 | -11.5924 | -48.5544 | 2024-10-24 00:36:12 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 44548343-2faf-314c-8712-287265dd510d | -12.672 | -43.8517 | 2024-10-24 00:36:17 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f8ce8f66-072c-3a91-9608-1b5623766ec7 | -12.6914 | -43.8484 | 2024-10-24 00:36:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 7e2b53f1-982b-32ff-8d45-a62be30d4a6d | -12.6918 | -43.8247 | 2024-10-24 00:36:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| ef0a8858-92ed-31a6-90e0-31cb54c20175 | -12.3783 | -63.863 | 2024-10-24 00:36:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b7447adc-1278-371d-a799-721085d240f7 | -13.7417 | -54.0682 | 2024-10-24 00:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8d1ca25f-cb01-34b8-9a92-25999b0d37be | -13.742 | -54.0475 | 2024-10-24 00:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 70677caa-cfbd-3719-959a-0ad60e6f7b88 | -13.7609 | -54.0661 | 2024-10-24 00:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| b3bd1295-570d-3761-9fc8-d7ddb233fbd8 | -13.7612 | -54.0453 | 2024-10-24 00:36:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| d8ec8ac7-fc98-35d9-8f51-411f46e9c7f8 | -14.9145 | -45.1224 | 2024-10-24 00:36:29 | GOES-16 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 13ea97d3-38e4-3278-8931-2557578d1dd4 | -16.9596 | -57.5245 | 2024-10-24 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| c4a01980-05cd-3a39-8699-e7f8894198f9 | -17.0207 | -57.3743 | 2024-10-24 00:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.0 |
| 8e80f20e-9327-3669-b7c9-01a57e7564ee | -17.2383 | -57.2462 | 2024-10-24 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| a2c3b668-1e47-378d-a1de-e9ba60aa3b68 | -17.2579 | -57.2439 | 2024-10-24 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.1 |
| 557d1ecf-c947-399e-a017-3270375497e0 | -17.6865 | -57.4798 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| bfd671f6-a2a6-3756-b68c-840eb0152d85 | -17.7453 | -57.4933 | 2024-10-24 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 74.5 |


[Clique aqui para ver as próximas entradas](README4.md)
