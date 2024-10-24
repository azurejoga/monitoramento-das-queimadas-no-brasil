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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a7d3014-7485-3dd6-b456-354c6f3f2d9e | -3.7068 | -41.6758 | 2024-10-24 02:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| fbc4fea4-dc30-3aa1-941a-37e377486339 | -3.9394 | -46.445 | 2024-10-24 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 98306987-7566-3560-816f-6692a3caa6ee | -3.9396 | -46.4229 | 2024-10-24 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 6fee8bea-75aa-315b-9251-34aebfcccd5d | -5.4373 | -47.6833 | 2024-10-24 02:05:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| a4422765-0e81-3065-ab6a-48d1fc5e1a89 | -5.4559 | -47.6822 | 2024-10-24 02:05:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| d6a51e3b-b5be-3246-8468-8e9fb416a133 | -10.1971 | -53.8617 | 2024-10-24 02:06:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| fdcad80c-6d90-3f63-b838-1d3e883cfa23 | -12.6914 | -43.8484 | 2024-10-24 02:06:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| e8e865e8-5ef5-3430-ab1a-cfa36341a221 | -13.7609 | -54.0661 | 2024-10-24 02:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 94810d5b-d872-35cf-a6e5-c45f96e5400f | -13.7612 | -54.0453 | 2024-10-24 02:06:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 53dc6cf5-3c73-3ab8-9e5a-d0731873961e | -16.94 | -57.5268 | 2024-10-24 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| e944b6e7-f6ff-312d-9819-0aa85e281a66 | -16.9596 | -57.5245 | 2024-10-24 02:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 6e6318ef-e107-3088-b956-a352d01ff634 | -17.0207 | -57.3743 | 2024-10-24 02:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| 69f4294b-7190-3d44-ac2a-bf30f7ae49a1 | -17.2383 | -57.2462 | 2024-10-24 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 8c943ada-1f08-3cc4-9fc0-f49b4ca4dda0 | -17.2579 | -57.2439 | 2024-10-24 02:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| fbb209e5-9389-30a0-b4a5-94ac17e3984c | -17.7831 | -57.5914 | 2024-10-24 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 75319769-a5d8-3606-8738-416705d15045 | -17.7834 | -57.5708 | 2024-10-24 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| a3e5fde0-e45f-3665-bd46-4a97943e9a45 | -17.7844 | -57.5091 | 2024-10-24 02:06:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 7813670f-d6ef-3222-831e-bf82636bef8c | -18.0639 | -57.3101 | 2024-10-24 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 1f858232-dcb9-3e9e-8a6b-12c00e8ac85e | -18.0834 | -57.3283 | 2024-10-24 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 88c8537e-b0ec-31d8-af00-45a2198eccd1 | -18.0837 | -57.3076 | 2024-10-24 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.6 |
| 6356d9e1-5e36-3c94-93a1-a487b76d0774 | -18.1032 | -57.3258 | 2024-10-24 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 494b5d6a-fc37-3573-9270-0eca57822450 | -18.1035 | -57.3052 | 2024-10-24 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| f16d5ea5-feb3-3275-ad4d-95da26b53649 | -19.548 | -56.6143 | 2024-10-24 02:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 8b46106c-6b2c-35df-ac26-6f8c4faa440c | -19.5681 | -56.6114 | 2024-10-24 02:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 121.3 |
| e9eb19f9-793f-3ed7-a8e3-52fbc8775a9f | -23.816 | -55.2713 | 2024-10-24 02:07:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| c3346012-877d-3547-80e4-3612a84e0954 | -1.4762 | -54.1763 | 2024-10-24 02:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 36b6676f-2c1a-3193-a196-f353e985873e | -1.4945 | -54.1962 | 2024-10-24 02:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 263434b8-2c44-363f-8245-218653611b93 | -1.4945 | -54.1761 | 2024-10-24 02:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 209.5 |
| 920e9f93-382b-3f7a-bb88-48bec4d866dc | -1.4946 | -54.1561 | 2024-10-24 02:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 17abc593-4330-3cb0-ac4a-e2848aa68b5b | -1.5129 | -54.1959 | 2024-10-24 02:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 296ce51a-3905-3fc3-92c3-4e7e6c12bfa3 | -1.5129 | -54.1759 | 2024-10-24 02:15:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 8ac48fa7-a9c7-3f5b-aaa8-add37ee1d6ba | -1.5504 | -53.6931 | 2024-10-24 02:15:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| b88bef78-c2e7-3212-b8da-b4467d559f24 | -1.5878 | -53.3089 | 2024-10-24 02:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1f92e733-4e1e-3f71-9fcd-f5bbb50c93ee | -1.6062 | -53.3087 | 2024-10-24 02:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 9714867e-bb9d-3f13-9818-6b6d2894977b | -2.9578 | -50.4198 | 2024-10-24 02:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 422a725c-57f3-3a4f-858c-c82fda22152b | -2.9763 | -50.4193 | 2024-10-24 02:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 3229c449-b5d8-3213-b8c6-256fe4dab12c | -3.0745 | -53.8252 | 2024-10-24 02:15:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 30baca3b-11ba-310c-9611-9c5491d61734 | -3.1101 | -54.1661 | 2024-10-24 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2b61152a-9f04-3dba-8cab-eff72fea2299 | -3.1102 | -54.146 | 2024-10-24 02:15:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 95e954dc-fa84-3444-acd4-8cbeec0a8d5c | -3.1607 | -50.4556 | 2024-10-24 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e4c402a7-026f-385e-8a1c-e97287c94226 | -3.7068 | -41.6758 | 2024-10-24 02:15:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 46539ba0-703d-36cf-8995-4a1e3dfd1b70 | -3.6612 | -54.2715 | 2024-10-24 02:15:27 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f7bda4bf-a870-34f7-95ca-59b462fa9152 | -3.9394 | -46.445 | 2024-10-24 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| eea4c83d-a29f-39ab-983b-014178d698ca | -3.9396 | -46.4229 | 2024-10-24 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 08febbea-f1c3-3c31-b6b6-eb60c3a54f9b | -5.4373 | -47.6833 | 2024-10-24 02:15:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 12b31360-9ca2-34a2-8298-388716ae3f25 | -5.4559 | -47.6822 | 2024-10-24 02:15:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 03f2f9bd-9159-3782-8478-2be1acb5f982 | -10.1969 | -53.8822 | 2024-10-24 02:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 2c486292-28f5-3c95-9bba-5a480437a807 | -10.1971 | -53.8617 | 2024-10-24 02:16:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 43d671cb-ed93-3181-8ba4-4b06bde3f454 | -12.6914 | -43.8484 | 2024-10-24 02:16:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 89850b98-a094-3c51-a9ce-e1a71350eea1 | -12.6918 | -43.8247 | 2024-10-24 02:16:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 7a8e35f0-794b-30e8-82d6-29e3effa26a8 | -13.7609 | -54.0661 | 2024-10-24 02:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| c1b6f0d2-99be-31ab-a9c4-e11cb591f35d | -13.7612 | -54.0453 | 2024-10-24 02:16:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f441178e-d97d-3041-9549-39515271a778 | -16.94 | -57.5268 | 2024-10-24 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| b516a3bd-1741-3375-95cd-2ea077a1e7be | -16.9596 | -57.5245 | 2024-10-24 02:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 209ae8be-6303-31fc-85df-6d7cfeb18142 | -17.0207 | -57.3743 | 2024-10-24 02:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| ece207c4-482b-39f1-a9b9-d162747769cf | -17.2383 | -57.2462 | 2024-10-24 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.3 |
| a2db30db-9bbb-314c-a91b-dd7abfada633 | -17.2579 | -57.2439 | 2024-10-24 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 7981f38c-527f-33bf-9348-f25f42af91a0 | -17.7831 | -57.5914 | 2024-10-24 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 34c7d9f9-21ba-39c7-8b12-bfcf0b222966 | -17.7834 | -57.5708 | 2024-10-24 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| e54002e9-2da8-3dff-b665-bc022d7f4f0b | -17.8032 | -57.5684 | 2024-10-24 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 020fba85-77a1-39c7-883a-becd0f4a2bb7 | -18.0834 | -57.3283 | 2024-10-24 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 5fa0f290-2932-3198-98c8-865fb9c736de | -18.0837 | -57.3076 | 2024-10-24 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 5b9a8818-1d77-3ab8-9f97-fc6c4f00ea09 | -18.0841 | -57.287 | 2024-10-24 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 73bc690d-398f-351d-a7c2-67e3429b43a8 | -18.1032 | -57.3258 | 2024-10-24 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| fa3a5184-1a21-3770-8554-b4a2ffd78bd8 | -18.3 | -56.2431 | 2024-10-24 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 66170c93-41e7-3985-ae62-f479df5e57dc | -18.3004 | -56.2222 | 2024-10-24 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| a2a7b071-3481-3dc5-b5f3-32320d0151c4 | -18.3199 | -56.2404 | 2024-10-24 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| b2bf66dd-9bc7-3f63-82cd-719789c0faf5 | -18.3203 | -56.2195 | 2024-10-24 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 0b177a8b-326f-3dd5-b85f-66f928c3ed43 | -23.8366 | -55.2894 | 2024-10-24 02:17:17 | GOES-16 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 48.8 |
| 2a994b06-e5a8-388a-9bb7-5512277f7429 | -23.8371 | -55.2673 | 2024-10-24 02:17:17 | GOES-16 | SETE QUEDAS | MATO GROSSO DO SUL | Brasil | 5007703 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.4 |
| f157406e-a649-3578-b77c-6f40c1b14dfb | -1.4762 | -54.1964 | 2024-10-24 02:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| c2593fc7-5277-36de-b231-816ef4f5c50c | -1.4762 | -54.1763 | 2024-10-24 02:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 0cf37021-afa8-36f2-93ec-a237c0ce11c4 | -1.4945 | -54.1962 | 2024-10-24 02:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| d76a8081-437e-302e-8547-9b5301bb0ae7 | -1.4945 | -54.1761 | 2024-10-24 02:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 203.1 |
| b46f11f7-d819-36b0-a7fe-0ba53bd00e17 | -1.5129 | -54.1759 | 2024-10-24 02:25:15 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 056abcf3-1943-3acf-a969-cb7740e78f73 | -1.5504 | -53.6931 | 2024-10-24 02:25:15 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| f8f27bee-9501-3fab-912c-840d38c23b3b | -1.5878 | -53.3292 | 2024-10-24 02:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c76d73f7-866c-3d2d-9358-d57f9c5265b5 | -1.5878 | -53.3089 | 2024-10-24 02:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3e4355ec-8d2d-3478-bc59-bda211728f6a | -1.6062 | -53.3087 | 2024-10-24 02:25:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 79af6b59-4e63-3783-b0da-5be257820ad3 | -2.9578 | -50.4198 | 2024-10-24 02:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a113d58e-092e-379d-8bc1-404073205605 | -2.9763 | -50.4193 | 2024-10-24 02:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3b882087-04ba-36ff-9747-e6c383499264 | -3.0745 | -53.8252 | 2024-10-24 02:25:24 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2eea1ba1-05df-3225-8657-23919461b5a7 | -3.1101 | -54.1661 | 2024-10-24 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| cba2b2f9-a85d-3a1a-9d86-14a991b12d99 | -3.1102 | -54.146 | 2024-10-24 02:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 78defe9b-f11a-351b-876f-f28f8271b9d1 | -3.1606 | -50.4766 | 2024-10-24 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 1d392b50-549a-3d9d-8272-22ea9d8a1da0 | -3.1607 | -50.4556 | 2024-10-24 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 6b7b623c-eccc-3a47-bbe8-8e48c455e3ea | -3.7068 | -41.6758 | 2024-10-24 02:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 2275dca6-c683-3e4b-9c15-6e8758c2e3f2 | -3.7255 | -41.6748 | 2024-10-24 02:25:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 6d34b994-bf0a-3dbd-80d5-325d6bb9bff8 | -3.9394 | -46.445 | 2024-10-24 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 84.7 |
| d1218183-6382-333c-8239-251beaa8a229 | -3.9396 | -46.4229 | 2024-10-24 02:25:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 5d90bd8f-f1cb-31b8-bd6a-7c927107518c | -4.758 | -46.4033 | 2024-10-24 02:25:33 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8f5261ba-1826-32c9-aeef-7440bb6db903 | -5.4373 | -47.6833 | 2024-10-24 02:25:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| cfc53d78-8e66-3108-88aa-c50589e94a7e | -5.4559 | -47.6822 | 2024-10-24 02:25:37 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 19e1da03-68c5-37b8-a11a-bf61ad25cf10 | -6.7666 | -59.1129 | 2024-10-24 02:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 170bfd6a-3a3b-3a9d-b4ef-b84ddff4979a | -10.1969 | -53.8822 | 2024-10-24 02:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 180439dc-5c83-3d93-b68d-221afd8d09a8 | -10.1971 | -53.8617 | 2024-10-24 02:26:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 44.5 |
| f68d9a22-50e3-3f52-b335-ea4a4e04496d | -12.6914 | -43.8484 | 2024-10-24 02:26:17 | GOES-16 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8c511d4d-845a-3826-b718-28673d13ff74 | -13.7609 | -54.0661 | 2024-10-24 02:26:24 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2ed743cd-6e67-3034-9a4c-b084a3a4ebd4 | -16.9596 | -57.5245 | 2024-10-24 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.5 |
| bc441201-bffa-3ac0-b297-aac917454d2f | -17.0011 | -57.3766 | 2024-10-24 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |


[Clique aqui para ver as próximas entradas](README14.md)
