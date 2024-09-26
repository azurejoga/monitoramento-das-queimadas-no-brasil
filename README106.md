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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf492d24-32c7-34a8-89e7-510ce5ea3eec | -9.00565 | -56.80161 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba9a5496-b293-3ba0-9359-7298bfe1c511 | -9.00319 | -56.81658 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e359ae8-d04b-3999-a51d-fcd3c2e227ae | -9.00222 | -56.80103 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e79a5972-3292-30ea-b0a9-cf969e7cff87 | -8.9901 | -56.81107 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87e8c861-343d-38bb-9a59-581fd938a096 | -8.98728 | -56.80675 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6c16827-83a6-3b0d-b4c2-8ae944c010db | -8.98686 | -56.85315 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3080a7b-4760-3426-825b-8b6c03abed01 | -8.97859 | -56.81699 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fe5b2cf-6824-356e-8758-88bc7bbfb56a | -8.97716 | -56.84775 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ff8e4bd-3f65-3355-aa24-f5bd1b30db9e | -8.97455 | -56.82022 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcf8c48d-be48-3e66-ac38-5d57f633591f | -8.97394 | -56.82399 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83d41a91-dd4c-34ce-92df-c50bb734e02c | -8.97373 | -56.84718 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcbb79da-8626-3dc8-a41c-e3e07cdf83c8 | -8.9723 | -56.87786 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8ff240b-fc9e-352f-a645-98b4527d3123 | -8.97029 | -56.84661 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2235ccc3-7789-31e5-9d83-f9712caed16c | -8.96991 | -56.82719 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddc8fd61-f88b-34df-bb15-84e7060d89da | -8.96969 | -56.85036 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d72bb119-969a-3972-bf7c-55001ade6d02 | -8.96948 | -56.87351 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23685139-e1fd-34fe-8c51-47e415ace271 | -8.96908 | -56.85413 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4977a0ad-4d19-309d-b9de-3d3c5fb07b5f | -8.96887 | -56.87726 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ebead71-9757-3e02-a92f-19818a232124 | -8.96404 | -56.84169 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80a7b0b2-4fcb-353b-b64f-2344c4a22d9f | -8.96343 | -56.84547 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28717e89-418a-3c91-bc32-f6109c7cd2e0 | -8.94059 | -57.14056 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91609d00-84af-39c5-8448-3678e8ada3d2 | -8.93711 | -57.14 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 9d45ba67-1fdf-3f71-863f-4d608a682884 | -8.93301 | -57.1433 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea3242f9-c56d-3c1b-a7c0-b6dc7d371827 | -8.93239 | -57.14717 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0194560e-98aa-36fd-9d21-d57ba0e70b35 | -8.92954 | -57.14272 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c08cce02-9f60-3af1-9c28-8aa251fdbf1f | -9.38484 | -56.84724 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef2ff1ab-aace-317b-b91d-40dc0eb5e361 | -9.38423 | -56.85097 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df28f9db-f238-3323-aa66-ea60e7115c87 | -9.37897 | -56.86171 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4dd20348-6c68-3b00-9782-3f6af1b3a011 | -9.37555 | -56.86114 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b0e338e-5319-3125-844c-c255bc491cbc | -9.37495 | -56.86487 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 950e08f3-587d-30cb-9350-a689eb0ec77d | -9.37152 | -56.8643 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb14fd98-4374-3909-806b-07d924e2c02b | -9.3681 | -56.86376 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8bba2b0-8567-32bb-95f0-b9b468ab3025 | -9.31238 | -57.13979 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7cb44fe-1a26-38a2-a5cc-216227b696db | -9.31175 | -57.14365 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2b8c1d9-f10f-37d5-9cac-14ed26964ca0 | -9.30988 | -57.15507 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 408c7d46-71c5-310b-9263-00914ba1b482 | -9.3083 | -57.14303 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20bd5b92-b06b-352a-904d-49c365e90b76 | -9.30767 | -57.14685 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6749a616-142d-32df-aa2a-fd67b219134a | -9.30514 | -57.16225 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4dbd582e-b108-3565-a8fc-7a59ba093b43 | -9.30484 | -57.14241 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc4fbfd-39ee-3e5c-a65f-7f169b471fd4 | -9.30421 | -57.14624 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33ff6ef4-38ba-3255-9494-65df3d3ceac7 | -9.30373 | -57.30136 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5902cb90-6a1c-34ce-bbf2-4aef8642b484 | -9.30295 | -57.15395 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| affc279e-d500-38a1-8b57-6e65cfd6bd8a | -9.30231 | -57.15782 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cf97ee2-3aa7-3b2d-b55f-ab7882bf2d7f | -9.30201 | -57.138 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d378483-e30b-3eb3-8de6-741aaaaa37ac | -9.30138 | -57.14185 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d70104d9-b105-34e4-8884-de5ef413a40c | -9.30075 | -57.1457 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9abde310-4849-3d03-b25e-7efffdda05d7 | -9.3003 | -57.25684 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b9692ae2-8886-3d66-9675-675bd7643559 | -9.29948 | -57.15341 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8452fc4f-52f8-3942-84ad-f8a5565a8b78 | -9.29884 | -57.15728 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8950cf2-ee2a-3b0a-9042-8e6823478db1 | -9.29792 | -57.1413 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab6bcf36-2de5-313f-a3f2-34970fd0deab | -9.28659 | -57.12375 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3be73bd4-58b6-3bc3-8863-6f29e3cceaa1 | -9.28185 | -57.13091 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d389b2d-08ce-362f-85df-42130f78292a | -9.28121 | -57.13477 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ee6e6fb-91b0-3ea6-84b9-22a985065e42 | -9.27681 | -57.05983 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5ce6221-1b44-3036-95ef-2874822d84de | -9.2762 | -57.06366 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| afc06527-5df2-3694-aed5-4e1d179f9240 | -9.27351 | -57.22445 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bac6a42-1ffb-30d5-a090-d0af1f907045 | -9.27337 | -57.05923 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 947897bd-050c-36fb-b2a5-7ecbed2d633a | -9.26683 | -57.24325 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55c644b1-32b1-31d1-83fd-8a2262ddc419 | -9.26272 | -57.24653 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ca6c30f-2e4e-3e83-8cdb-fa93bca962c6 | -9.25923 | -57.24599 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d603a6a3-2a5d-3e8a-a0c6-165cd18a8f9a | -9.25858 | -57.24992 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1415395a-41d1-34bc-80d3-4517d47d343f | -9.25575 | -57.24545 | 2024-09-26 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad871f9f-4c09-30a6-926a-28e3f17ed7ac | -9.25478 | -56.86911 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e690c61-6b41-3449-b272-afb7c164602e | -9.25416 | -56.87289 | 2024-09-26 04:57:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3740ee25-8d89-346b-9c57-aa9dd2994200 | -8.49927 | -57.24931 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fda7bfb-7f2e-3f48-80c1-dc65e5d1eeee | -8.34749 | -56.50342 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d70bbcd8-77b8-3f2f-a3a2-f1bc82e08ee4 | -8.34348 | -56.50658 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e976f31a-528a-3649-9ee4-27151dbe38a6 | -8.34288 | -56.5103 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6b663f5-cb2c-3856-ab67-8e1b829668b3 | -8.34228 | -56.51403 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab68120b-6c07-39de-bd25-f91ef653b6ba | -8.34167 | -56.51777 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34043f40-bf52-35a2-abf1-ff45c7c7a5bb | -8.34008 | -56.50601 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edc06158-3d4f-32a8-a45d-7389dd685474 | -8.33947 | -56.50974 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5df0ac1d-cc0c-322a-8b8d-02981c636f0e | -8.4811 | -57.02323 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 273bd75c-2ba5-3f70-a6ed-1001e007708f | -8.13257 | -57.68692 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76395ea2-e5e3-3b0c-b681-120be3dffc4c | -8.11033 | -57.6875 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2526c7f0-2d7a-3a50-95f7-841cd35d9bde | -8.10963 | -57.69167 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 858c61fa-6ca4-3da8-bfbf-7149409ef539 | -8.10604 | -57.69108 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eedfc0cc-ffee-316b-8c81-8dccb1a8486c | -8.10535 | -57.69525 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ca96657-9a83-3852-be17-2b3c93d8df68 | -8.10245 | -57.69049 | 2024-09-26 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 271aab7d-bc38-3a6b-bb63-7c80604a2eb3 | -3.26447 | -57.03646 | 2024-09-26 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b1b85d6-199f-3b70-acf5-dbe7c79507df | -2.72605 | -57.51488 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f1f980f-1ec1-3b60-8d3f-20c2971799ae | -2.72224 | -57.51428 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17e4d1f8-5291-368b-9dbb-04220e80ce72 | -2.71842 | -57.51368 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15dc5f7f-1b1e-3e15-a2f2-930e57fa554e | -2.71384 | -57.5178 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2968b42-6d02-3e0d-844f-3f217d23987d | -2.70774 | -57.5313 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91e5e11-40a3-3940-af80-f40dadb43ac5 | -2.70468 | -57.526 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4eae52f9-fada-3cc0-b0d8-e00c0a1c276d | -2.70392 | -57.5307 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71de08b6-cc1d-33f6-813e-b81efa4f11c9 | -2.70086 | -57.5254 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8c3d3a41-9863-3add-a3ef-db0e0c55bcae | -2.70043 | -57.14062 | 2024-09-26 04:57:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e7e4fd1-146d-34bb-bb21-4d537c45681b | -2.7001 | -57.5301 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 721d5191-4731-3491-88d6-02c0be01eb8f | -2.69704 | -57.5248 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2faf929b-8cfb-3f1d-b657-39ae48da437b | -2.69322 | -57.52419 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8ee259ce-b8f1-34ee-8815-c8b3cb8284b3 | -2.6894 | -57.5236 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2dcc9577-dd80-3a6e-a541-ddd53320ca25 | -2.68558 | -57.523 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 53adee71-5759-3554-8c7a-aedc88be6d82 | -2.68481 | -57.5277 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0a77247a-22cb-30d1-8f71-0d63e817f890 | -2.68179 | -57.52865 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9b66b17c-7213-3375-953b-312bd89306a8 | -2.68099 | -57.5271 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7bfc1240-6f7b-3a8f-8aad-759f2b331d86 | -2.68022 | -57.53181 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8dc79569-2e0f-33c5-a835-c6e3a183f971 | -2.67796 | -57.52804 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 19220f08-847a-321f-82e6-73e41a7f7bbd | -2.67717 | -57.5265 | 2024-09-26 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |


[Clique aqui para ver as próximas entradas](README107.md)
