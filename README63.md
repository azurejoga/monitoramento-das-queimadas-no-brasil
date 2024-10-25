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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a89a8fa-9d31-3add-91bf-b411328ee1c5 | -4.97849 | -50.77249 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 420617fa-1c9c-3826-9772-190eec91a2d8 | -4.97381 | -49.77173 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b8619ae-9af4-31ec-9eee-409f2af9258c | -4.97048 | -49.77121 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a13a2d0-6f59-3929-9a73-974c278dc04b | -4.91796 | -49.8308 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d993d673-7ce5-3238-87ee-e77b26e34db6 | -4.9174 | -49.8343 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cf54461-63d6-3012-b24a-b88508c59f23 | -4.91685 | -49.83781 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da2e99b4-c720-33f6-914e-c78f6d426446 | -4.91517 | -49.82677 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e803b0e-0252-3828-885e-90b839ce44a4 | -4.91462 | -49.83028 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 201e2741-f16b-36c7-95b5-42112a7c03a5 | -4.91406 | -49.83379 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ae5bf681-12fc-3060-a77c-b91f0c946eb7 | -4.91127 | -49.82975 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f3f9c382-ec4e-32e1-aab8-1935fd796fb5 | -4.91072 | -49.83326 | 2024-10-25 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4d82ea55-dea0-3b5f-9da2-96ab03894675 | -4.816 | -50.89104 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5956703-96be-3749-941d-026d12981572 | -4.73952 | -50.69341 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 099d288b-75bf-33b8-954d-2a0b77f6d2d0 | -4.73611 | -50.69286 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f2de56b-4e69-3ea6-b895-3a2867e81fff | -4.6148 | -50.79491 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f5b7070-f2e8-3c2d-afab-0a91238bcbe9 | -3.80333 | -50.16808 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69054a35-ae3f-317e-9fab-0589aa5245fb | -3.80055 | -50.02861 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14829cb-4942-32d6-9dd7-79031aefaa55 | -3.79995 | -50.16755 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e4ca6f1-690c-3595-b35f-6e5015341a33 | -3.79765 | -50.61923 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9076d4f5-8c6d-3986-91c7-ff3db5d4b3f7 | -3.79718 | -50.02808 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c32b4606-82eb-3998-8cb6-58612795c684 | -3.79657 | -50.16701 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 381f475c-eb81-330d-91fe-57fae3968adc | -3.77565 | -50.18631 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32dc0369-4a84-3289-95ef-10377988f7de | -3.7697 | -49.98353 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e935e7c3-e8c5-3e38-a55d-07c41ddb8f6a | -3.76914 | -49.98709 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5b6f14a-ab68-3143-b34f-cd3b2dd1c6aa | -3.76231 | -50.38028 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d722950d-5bbc-3d49-952d-51451bf94c50 | -3.76172 | -50.38394 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 706acc27-c1e3-368d-aaa2-b0c3e31bec85 | -3.76114 | -50.38759 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8952c790-d8aa-394c-a568-715081b62bf6 | -3.74843 | -49.94374 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 236bcbbd-32bf-34aa-adde-8aa49e823ff4 | -3.74507 | -49.94322 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 336da8cb-a3f3-32f7-b6bd-1f0fef1d2823 | -3.74401 | -49.90664 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1d26282-e937-3dd4-89e0-2b7c0056963b | -3.69954 | -50.1632 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e43d4110-5106-3486-bf33-d4e090c3a781 | -3.69896 | -50.16681 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 389898ea-b651-391e-b660-670bb24d43a5 | -3.69558 | -50.16626 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fb71a43-8b13-3095-9b91-bfc09d866c7e | -3.60869 | -50.57908 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e70ee151-4688-32be-8cd0-c7bc244a0804 | -3.60526 | -50.57854 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e17097b-d267-3550-88b8-7c3de16d8fcc | -3.60467 | -50.58223 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eee79762-17bd-3709-8821-13596d3eec13 | -3.60183 | -50.57798 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1029fa15-3510-3894-96be-986e17b60729 | -4.1402 | -49.80224 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3705972f-b47f-31c3-98dc-955172460feb | -4.13964 | -49.80576 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f00a505-2b9d-331b-bfdc-f4cd1d2b4d53 | -4.10697 | -49.28582 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ade5d33-18b5-3b3a-a887-a74ef91f2d7d | -4.10642 | -49.28928 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b11110cc-ab43-3d5f-a15a-9cb436c1c9ec | -4.069 | -50.03399 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02300bdc-98b7-33db-825b-658dcac6f120 | -4.06564 | -50.03344 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da46cb1c-c983-356f-85d1-05cb9fcb19d4 | -4.02453 | -50.44384 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ee7139d-f647-3680-a1ba-fe98e2109c0c | -4.02171 | -50.43967 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5f27fa8-6125-3ca0-acd1-c2b14bc0cceb | -4.02113 | -50.44331 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1158e9f-d11a-3bfd-b543-d8f96de18dd8 | -4.0183 | -50.43914 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4459e630-6dab-38c4-8161-7cb8aa3fcc8a | -4.01772 | -50.44278 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 156ea408-949f-31a6-9639-827829f2f88f | -3.99288 | -49.27798 | 2024-10-25 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9897a31-6db1-3876-b401-83433b5df81f | -3.95347 | -49.99432 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b872e77-4504-34d3-8c5f-b97549c5655f | -3.94637 | -49.88778 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f5a506c-41cd-3f67-b65b-a1518e3905b1 | -3.94465 | -49.88705 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0ef1596-b252-338f-a019-40ecc42305c0 | -3.93768 | -49.47592 | 2024-10-25 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2988de78-2a59-3d1b-8982-3f868f7c8bf5 | -3.93066 | -49.86672 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 604bd808-bde4-34c2-bf1d-eb731ba2683c | -3.92782 | -49.7326 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a97b16db-6414-34bf-8864-bcfaa4005b70 | -3.9273 | -49.86619 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65e1abc0-5340-3b60-9c45-bb94b01fa4cb | -3.92395 | -49.86567 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d40ea502-af29-35b8-96d9-7f7e70ae00f6 | -3.9189 | -49.7456 | 2024-10-25 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4152b57-0983-33a0-ad6d-631c6cdbcaf7 | -3.89649 | -49.35559 | 2024-10-25 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 863c782b-e532-3c6d-90c8-d4057a81d57e | -3.88407 | -50.05233 | 2024-10-25 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06c35f9b-98a6-3ebf-ac9a-91b137acea5e | -4.89169 | -50.68003 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8adf70e8-c69a-3537-834c-5393f20ee5b1 | -4.84052 | -50.91388 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1e024ce-cd25-3bde-a453-1f048dc31f2e | -4.82003 | -50.88788 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3844174-2475-3728-afae-95f28db85b4b | -4.8166 | -50.88733 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64b5ee7f-43ff-32cf-a728-74fa6679eacf | -4.72764 | -50.78963 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b393059f-1152-352a-9408-bcc453a6fd57 | -4.72422 | -50.78912 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c509531-706a-3317-bf24-6001d628dbfc | -4.72138 | -50.7849 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7915f48f-3cf4-3c56-a60a-bada47b21925 | -4.72079 | -50.7886 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 226f8cdc-ee64-3aa7-84ed-d592b6a1554c | -4.68283 | -50.74103 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c12a1ce2-be84-31a3-9caf-c5bb1d90cb54 | -4.61539 | -50.79122 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a03ff3e-f9d8-310f-9828-3cee6bf06539 | -4.44738 | -49.65617 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9966225-a34b-38fa-b9c7-9d7809203a3e | -4.44682 | -49.65967 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75b337cb-61ff-355c-aeb0-ea190da0af35 | -4.43615 | -50.13877 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a52f602-3f6a-3a1c-967f-f29e0f5ba5e5 | -4.42102 | -50.78428 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e0fbfe4-9757-3ab7-a1f8-ffedd35d0d8f | -4.39952 | -50.52454 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86fdb89e-96ef-37ad-ad28-cd8b4acde386 | -4.39893 | -50.52819 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5223bf49-f14a-34f3-8c04-49603b30d0c5 | -4.39109 | -49.75861 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c2e93b0-6836-3f39-83c0-996d0972abfd | -4.36495 | -49.83732 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a912acad-0384-33d3-bfd6-b9e21dc999d1 | -4.3616 | -49.83679 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 681ddecb-742b-3c5f-ac46-83146c929972 | -4.29111 | -49.68565 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7163dec8-2893-3ac0-90dc-fcea8d38c9b4 | -4.28777 | -49.68512 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 27950e03-9d17-3edc-a38f-97005ec371ec | -4.27383 | -49.66498 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7ce9b5a2-510f-3cf7-bc1d-8b8fffc152cd | -4.27328 | -49.66848 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 610423da-c8d0-3324-9941-807ed2087a22 | -4.26994 | -49.66796 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1d5045ef-b96c-364a-802a-cd6b7bfa87c1 | -4.26736 | -50.60855 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d40ecce3-ddde-355b-8f4c-2bd4216fb0c2 | -4.24106 | -49.91563 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ba386feb-c31c-3dda-8768-0f50444f15eb | -4.2377 | -49.9151 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a91eef2-3aad-30cd-af8f-8df9ac9794b5 | -4.23683 | -50.69099 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18df9312-ad3b-3cab-a254-02c41d6b535b | -4.236 | -49.73086 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fb46418-bc59-30ad-9a87-88962003df19 | -4.23592 | -50.6303 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94c66a6e-e192-3fe0-bb60-7cb17697241e | -4.23533 | -50.63401 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99318d79-e1d2-3bad-806a-4d2bf5495bf2 | -4.23435 | -49.91457 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fd426fe-4e31-3876-91f2-0f0d2addad74 | -4.2334 | -50.69045 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d20378b-8c4e-3dc2-8e6c-625bb08df5ab | -4.23266 | -49.73033 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37e8c53d-1c23-3d3c-a3e6-0529e2428e33 | -4.2325 | -50.62976 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd29cca6-a8ef-3db0-8d86-80cfe83beb0f | -4.23192 | -50.63346 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be25b0e0-e536-3556-86da-86e177b4a58c | -4.22908 | -50.62923 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 681da39f-fe92-3d62-a286-1b35fdcc7df9 | -4.2285 | -50.6329 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 578b859a-721e-35cf-9624-356595d6044b | -4.21366 | -50.50655 | 2024-10-25 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74675b38-83bb-32cd-b8ff-ab2723d8182e | -4.18988 | -49.40173 | 2024-10-25 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README64.md)
