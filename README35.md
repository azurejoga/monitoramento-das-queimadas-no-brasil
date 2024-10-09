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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0675653e-8c5b-32cb-9505-d83b0ba72c60 | -20.1049 | -55.9464 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a72189a5-f125-375b-b074-f93216c9fe77 | -20.0914 | -55.932701 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f51d60fc-6e6b-3e71-8634-2e855b76363c | -20.0933 | -55.9408 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e914266a-2e25-335d-9ee7-5d5899036cea | -20.0952 | -55.948898 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9c9ff8a6-4e0f-30ea-82c8-8133fa657b5f | -20.0835 | -55.943298 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8ef74692-ad2f-32c3-a7c3-aac36f42eb3f | -20.0854 | -55.951401 | 2024-10-09 01:24:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f37b4b7c-ba3d-356b-93cd-a982ae809d5f | -20.071899 | -55.937801 | 2024-10-09 01:24:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 17be18d0-8f94-3ad7-85f6-75eec4f09351 | -20.073799 | -55.9459 | 2024-10-09 01:24:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 73df3dc0-14b8-3e13-a6fa-6163a133095f | -20.075701 | -55.953999 | 2024-10-09 01:24:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bdc94772-da1f-37ab-9977-f1a6d466a97d | -20.062201 | -55.9403 | 2024-10-09 01:24:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 57247358-49b3-3ce7-a331-2ffbfc551a66 | -20.063999 | -55.948399 | 2024-10-09 01:24:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a146f074-942c-3968-aed4-f883d257e169 | -20.275801 | -56.917801 | 2024-10-09 01:24:01 | METOP-B | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c7c5e65d-e2a1-3d60-8b72-9d604e1ae739 | -20.2321 | -56.952801 | 2024-10-09 01:24:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c4d86696-cb4a-3639-89ac-6f8d1bd8af65 | -20.233801 | -56.9603 | 2024-10-09 01:24:02 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3c2a6189-ea6a-3a72-86d7-96d8d123ec4a | -19.676001 | -56.460899 | 2024-10-09 01:24:09 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0f0bd441-603f-3c0a-9164-85382baa7447 | -19.677799 | -56.4687 | 2024-10-09 01:24:09 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ea6ab714-ebfb-3190-bddb-0ce12a7ee3d4 | -19.6469 | -56.558998 | 2024-10-09 01:24:10 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 28fbc292-89f2-3586-a788-dccd6419a22b | -19.5856 | -56.516998 | 2024-10-09 01:24:11 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f39f97a8-3369-3ede-a050-d02d43063564 | -19.5874 | -56.524799 | 2024-10-09 01:24:11 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b63be025-d048-3c33-848b-b6d3c41ab114 | -19.5758 | -56.519501 | 2024-10-09 01:24:11 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 077f5f9a-004e-3e7e-969f-42ebed9244a9 | -18.921 | -54.533298 | 2024-10-09 01:24:14 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c4e306ce-6756-3bec-ba3d-ab135d888c63 | -18.9233 | -54.542801 | 2024-10-09 01:24:14 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ae7143ff-4ade-334e-9e93-632e1b11a416 | -18.9256 | -54.552399 | 2024-10-09 01:24:14 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb2eced5-1523-300e-8a7c-536f1e65fec0 | -18.9062 | -54.557598 | 2024-10-09 01:24:14 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bdf35681-4583-3e14-9d85-4503e5e354c2 | -18.908501 | -54.5672 | 2024-10-09 01:24:14 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| abe5ee47-15c1-3dc4-884e-bc1320ae9415 | -18.865 | -54.558399 | 2024-10-09 01:24:15 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 254507a3-41b0-3523-983b-f971d6f5ca5c | -18.8673 | -54.568001 | 2024-10-09 01:24:15 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 03836872-a4d9-3ef6-bbaf-e7c31611b86c | -18.4739 | -53.471901 | 2024-10-09 01:24:17 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd9b246-19f6-3142-8d86-759ab849e0ae | -18.4767 | -53.482899 | 2024-10-09 01:24:17 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ea60693e-8b43-3301-bb24-79aa51030512 | -18.479401 | -53.493999 | 2024-10-09 01:24:17 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| be806cdc-2c86-30f7-8e3d-3f2e5e74170d | -18.486401 | -53.480202 | 2024-10-09 01:24:17 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 05be0abe-aaad-357e-bff5-9a8489b23627 | -18.4891 | -53.491299 | 2024-10-09 01:24:17 | METOP-B | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c82bd159-c0ca-3205-9696-660459b6bfdf | -19.109301 | -57.510201 | 2024-10-09 01:24:22 | METOP-B | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9db7e1df-5667-398e-87e7-709753c923ec | -18.969801 | -57.7159 | 2024-10-09 01:24:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 90469a6e-b91b-322e-ba43-025c7d8eeb8c | -18.728901 | -57.242401 | 2024-10-09 01:24:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 449add3f-9edb-308b-b720-ca43acb5c8f7 | -18.7106 | -57.207298 | 2024-10-09 01:24:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e5a91eea-3179-360a-861b-b8f825b46113 | -18.7008 | -57.209702 | 2024-10-09 01:24:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e3d789ba-86c3-34e9-89cd-8decd0868f76 | -18.702499 | -57.217201 | 2024-10-09 01:24:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7094d08b-f0e2-35c1-b788-1580507d5ae5 | -18.712799 | -57.262299 | 2024-10-09 01:24:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9fc59ac1-bced-3e56-8920-56c2829a422a | -18.7145 | -57.269798 | 2024-10-09 01:24:27 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 047b9bd7-b327-3912-ad9f-75b7d5fa1670 | -18.7234 | -57.354599 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 02687cee-3ef2-323b-8c76-e9b36c51505a | -18.6779 | -57.199501 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5e670d85-bd35-372c-8297-e9c75efa94cd | -18.6796 | -57.2071 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9e59974f-fc73-3b70-8064-3e37a758a809 | -18.681299 | -57.2146 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 71b2bb2e-c748-3fcf-9d6a-2de74fcce5ae | -18.6681 | -57.2019 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3646fc9c-c663-328c-883b-0bb8dc3cf556 | -18.6698 | -57.209499 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c92150d5-f6a0-37cd-afe6-5e35394498d0 | -18.656601 | -57.1968 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fdda76e6-3b45-341f-aad0-c31ff2712c12 | -18.6583 | -57.2043 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 18970244-a210-3e07-996e-44fa6feb1bca | -18.6469 | -57.199299 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac0af19f-fd24-34e4-a185-0e4927b195c7 | -18.6486 | -57.206799 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58639076-b10f-3ffc-8913-01c89cdb7097 | -18.635401 | -57.194199 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b8caf427-d7c3-3f34-b57f-7e07601296bb | -18.6371 | -57.201698 | 2024-10-09 01:24:28 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7f154232-c8e2-33da-bbd7-c91778596c32 | -17.8381 | -53.7505 | 2024-10-09 01:24:28 | METOP-B | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa1da3b6-5ef9-330e-8ca8-b07ccef8392e | -18.634701 | -57.281799 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6af4f99b-99ed-3f22-9544-e7af1a3f137f | -18.6364 | -57.289299 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5aef129e-31c7-3649-9232-76e881aebd59 | -18.6381 | -57.296799 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b552f5da-dc24-3ea1-a706-41468ecb19cf | -18.6112 | -57.224098 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc12e9a6-4f48-3495-8a04-48d79d283e32 | -18.6014 | -57.226501 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cf3c5d38-c87b-39d3-a6c6-2213b6742429 | -18.6031 | -57.234001 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dc708b48-3549-343f-a14e-efed9a913f05 | -18.5917 | -57.229 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ae9267cb-36dd-3b5c-8d0d-815ead81ebef | -18.593399 | -57.2365 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ccd39d7-a227-38e1-943d-d9514be2864d | -18.5951 | -57.243999 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ac955bf3-f14f-31be-af1f-63d832d9b6cd | -18.596901 | -57.251598 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 37eb8349-8e3f-3220-926d-ed1a20793fed | -18.5986 | -57.259102 | 2024-10-09 01:24:29 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a284a9ae-6bed-30b5-b242-f7133fc00c28 | -18.094299 | -56.368801 | 2024-10-09 01:24:34 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 01c1923e-34d3-3d18-9ae7-9838de9e20fe | -17.3482 | -55.009899 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26b1cd60-a424-3986-a4f0-08a83306040e | -17.3361 | -55.002998 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb8ca411-1c82-3227-b44d-99d254443474 | -17.3384 | -55.012501 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 617deef5-bbf7-3387-a418-09d970e272a7 | -17.340599 | -55.0219 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5725fca5-b048-3d91-a760-57846e6ec3bc | -17.321899 | -54.986698 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e2d4b40-afe3-3ae8-8dd7-0112be5f3b94 | -17.3241 | -54.996201 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 119e50c3-23b4-35cc-b7de-db4275091584 | -17.312099 | -54.9893 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fcec5d12-d6e5-3c14-9cb7-71760a253e91 | -17.3144 | -54.998798 | 2024-10-09 01:24:41 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 02faa0d9-1463-3636-a523-47a654b1425b | -17.755199 | -57.092602 | 2024-10-09 01:24:42 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3acf83aa-b9f2-307a-a793-bf9c0567a398 | -17.873899 | -57.658699 | 2024-10-09 01:24:42 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4ab6ce78-f37c-3179-a4a7-a7d38b283b96 | -17.875601 | -57.6661 | 2024-10-09 01:24:42 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 048c47ff-8d11-3aa7-866c-521d3d25e5ba | -17.316 | -55.048302 | 2024-10-09 01:24:42 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54ea5e91-8035-3dfe-af6d-de09d01ecbf2 | -17.318199 | -55.057598 | 2024-10-09 01:24:42 | METOP-B | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9950efee-f215-3b60-90d8-b0ab1c644924 | -17.757 | -57.1003 | 2024-10-09 01:24:42 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8cf5b756-21c7-3307-94de-19a27d3ce91b | -17.865801 | -57.668499 | 2024-10-09 01:24:43 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 97fb1b82-e933-3003-98a7-3e60c9e7858d | -17.8624 | -57.653702 | 2024-10-09 01:24:43 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 53185181-bac8-3db8-be3a-9f212407e73e | -17.8641 | -57.661098 | 2024-10-09 01:24:43 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2032ab95-934d-36bb-ab58-1020e9c1b32e | -17.732201 | -57.0821 | 2024-10-09 01:24:43 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be548658-4e4b-3427-b677-17c828d7b7b9 | -17.290199 | -56.157501 | 2024-10-09 01:24:46 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e7b8c77f-4626-3b96-9718-75ec08ddfcc6 | -16.4937 | -52.853001 | 2024-10-09 01:24:46 | METOP-B | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 579ad615-770c-3602-b23b-bc79ada472d9 | -16.497 | -52.865898 | 2024-10-09 01:24:46 | METOP-B | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f35ac52c-4b3c-380a-9cb3-194d21c2f196 | -17.1632 | -56.101299 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c386f2c9-e78b-3096-ad5c-7129d7cfe3c4 | -17.165199 | -56.1096 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7e982ad-0af6-3521-96da-1a589d652bb4 | -17.151501 | -56.095402 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40ca8b12-b814-3555-860b-3e03c4b637c9 | -17.1535 | -56.103802 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47d4d4ef-345d-3ff2-9bbb-6acbd70599ea | -17.1555 | -56.112099 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd574716-a37b-3370-82f8-b7072a15e619 | -17.1574 | -56.120499 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 751202d3-530a-37d2-9f97-45ef0c5c7e03 | -17.147699 | -56.123001 | 2024-10-09 01:24:48 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0fcfd506-01dd-33bb-bd50-ee60aa021d52 | -16.910601 | -55.776199 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a0b0721d-1c9d-34a6-8cfc-16cebb833277 | -16.9126 | -55.784901 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 253776a9-c40d-3d30-80c0-74e4e28ed55e | -16.9147 | -55.793598 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5061b6ca-c558-3826-a2ff-74ef90e777d4 | -16.9168 | -55.802299 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e03c7629-a288-30ae-a8a2-6140e3fcfd2d | -16.9188 | -55.811001 | 2024-10-09 01:24:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04811c57-3c96-3724-86a6-2ba59bf23372 | -17.1527 | -56.8083 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b099a79-47c5-3661-a5dc-fdb81944a842 | -17.154499 | -56.8162 | 2024-10-09 01:24:51 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README36.md)
