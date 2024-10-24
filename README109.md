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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72a7399f-a936-3790-bee6-4d8412de28ce | -19.5373 | -56.65586 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cccf1134-9145-3c19-814d-d10268f48d2b | -19.53725 | -56.69418 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| f8b42b90-01eb-3860-b84d-e81844e73c2a | -19.53673 | -56.66059 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f269731e-4880-340c-904f-e13e4649eb43 | -19.53669 | -56.69887 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 42f62f61-0f2b-310f-a93a-f1144057a1cf | -19.53617 | -56.66531 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5360ff42-6c4c-3499-892d-9a581bd67fd1 | -19.53612 | -56.70357 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 2599dd70-0439-3f5b-ae7c-a7643ad2ebc5 | -19.5356 | -56.67004 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c3cc9a26-21c4-37a0-b1c5-2c7dcaf1afc3 | -19.53503 | -56.67475 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1230dde9-d73f-3dbd-b8e3-fd68d85e9072 | -19.53446 | -56.67947 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| dfe43bfe-ea95-3c09-9be9-12c94bfecd69 | -19.5339 | -56.68418 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| ca7d77b3-5b42-34b7-8796-3995b2dd30f2 | -19.53333 | -56.68888 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 69b2cf77-3762-3514-90b9-70401a843443 | -19.53276 | -56.69358 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 831b9137-46d6-3273-8e37-a8cbcdeef18c | -19.53223 | -56.66 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 66ccf14d-db37-3ba3-8ec5-278b3f3a966e | -19.5322 | -56.69828 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f4ed04ac-2eb3-3cb6-8cd5-e082860be4de | -19.53167 | -56.66473 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 50a07f90-d7b4-3b1e-9ebb-494b65af60fc | -19.5311 | -56.66945 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7358b79d-599a-3c21-9f27-22d0e4ede21f | -19.53053 | -56.67416 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 969b6d91-1303-360b-b168-f9138eb7c57b | -19.52827 | -56.69299 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a3b6f64-ebd3-3d10-95a5-407cf5a00247 | -19.52771 | -56.69769 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b302329b-091c-3720-96c2-de8005880c07 | -19.52717 | -56.66413 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 638b1cfd-0295-3996-8bff-937f03de8ed5 | -19.51761 | -56.66768 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| e59d1036-d9f2-3840-ac8c-aeef938dcb73 | -19.51311 | -56.66708 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b9521460-f9f3-35d5-953e-f3adbfa2be77 | -19.50862 | -56.6665 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 23a04559-8a2e-3b3f-8037-2df009faf846 | -19.50806 | -56.67122 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c6666b6b-475c-3286-ad26-b406c324c473 | -19.50747 | -56.63754 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 19747002-a4dd-3288-adb3-b5f3bbc9280c | -19.50691 | -56.64228 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 38ccb8de-2bb6-33f6-9d8a-dcb5bddff0f6 | -19.50579 | -56.65174 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 862ceb2a-2756-33a7-99f9-f495e87ddf5f | -19.50524 | -56.65646 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 991ca8cb-b7e8-3cd0-8ce5-b6a7db096e93 | -19.50468 | -56.66119 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 98859857-cf05-36e0-9b5d-a51145171d7f | -19.50412 | -56.66591 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| fa392258-2c65-37cb-af6d-75282739de80 | -19.50356 | -56.67063 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 09b26b7d-aa65-3380-92be-5c04334fd54a | -19.50296 | -56.63695 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| c1910d1f-c12f-36af-b027-ace0e173602d | -19.50241 | -56.64168 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| f77a87c0-861e-3b53-85e5-9b0fa89f067a | -19.50185 | -56.64641 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 686a4b52-4816-3622-8a8c-43db76437eaa | -19.50129 | -56.65114 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 8cf247ae-c138-3905-b5ca-4484e1e8d0d6 | -19.50073 | -56.65588 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 4b84aa1f-4c21-3baa-9de8-acd3a092a10b | -19.50018 | -56.6606 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 7de413ae-b24a-3905-ada2-299387715d73 | -19.49962 | -56.66532 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 022bf359-819b-38bd-9964-8557314f53a3 | -19.49679 | -56.65055 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 840f1aad-08a2-3b75-96a1-e7b9eea6a8d6 | -19.49623 | -56.65528 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c8c5b2b2-7459-3695-b5c1-31030a5cd9aa | -19.58972 | -56.53365 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fbf49fce-95ea-3b9b-88b1-ccf278ce4bdf | -19.58916 | -56.53848 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0803142e-32a0-3807-a690-4850419d3c6a | -19.58518 | -56.53305 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b4836004-e1da-36e7-a2a7-0fc1e4b4bff4 | -19.58395 | -56.53586 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7ccce3fc-84a2-3447-a31e-9e3f1f7e67f7 | -19.58064 | -56.53244 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b2df2020-839f-318b-b6d7-3657509fa7ad | -19.57941 | -56.53527 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e11c0c27-5b9a-37ff-99ad-9a857870b89d | -19.57555 | -56.53667 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cf188dcf-a73f-33bd-be0e-7f0d98f32ead | -19.57186 | -56.60932 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| cb6b913e-47a0-3ffa-ac34-a564a970de85 | -19.57067 | -56.60717 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 2ade0e10-9ba0-3d6e-a576-6ce9107e63f6 | -19.57009 | -56.61194 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 103935d6-3b55-36a8-8770-a15769da13bf | -19.56882 | -56.55536 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ed3409e5-1c7f-39a9-b971-6a5135b81f1c | -19.56827 | -56.56017 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1a25979a-481d-3f10-8657-c247575eb0f5 | -19.56789 | -56.59226 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ca01e600-6b7e-3112-ad12-d767e6279203 | -19.56742 | -56.55814 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b6df42c7-7d9c-349e-b35f-56941e6b12cd | -19.56734 | -56.60872 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 9c765615-637e-3415-abd2-9b259d75d990 | -19.5668 | -56.61349 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.1 |
| ee7c93c8-7411-3202-8669-75e044b0eac8 | -19.56615 | -56.60658 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| b23db49a-8e7d-397a-9a51-5b6535a87afd | -19.56609 | -56.57938 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 53bf2cc8-5294-369a-b574-49923227f3e5 | -19.56557 | -56.61134 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| dcca2423-86e1-3320-8ee7-f9ecb5c526e0 | -19.565 | -56.6161 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a5e0b1e9-80d9-3ee5-936b-d6863c95f8f5 | -19.565 | -56.58897 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f3ca8071-e2f6-3603-8700-f38653c05d71 | -19.56446 | -56.59377 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 32d7f71d-afae-3712-9c71-707c5cf1cc39 | -19.56429 | -56.55476 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a40c7a06-8860-31b4-86eb-da765024185d | -19.56347 | -56.55275 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49790927-6d8d-39a0-a65b-413e04f2915a | -19.56337 | -56.60334 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 3332b49c-6a24-338a-bfee-c0e5f5a62765 | -19.56337 | -56.59167 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| bad79cda-7175-32e6-b43c-d66726b8c4ef | -19.56289 | -56.55755 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6cbc5805-7396-358a-95a9-dc7f227dd777 | -19.56283 | -56.60812 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c5a46b5b-b7df-3629-be20-25ec70b62450 | -19.56228 | -56.6129 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 87c94c11-6568-3884-bf04-b94d53031708 | -19.56174 | -56.61766 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| fc114a8b-b749-3efe-8fa3-450fca7ae5b7 | -19.56164 | -56.60599 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| c87e720c-1e0f-3e8a-b0ec-44f2d584c36a | -19.5612 | -56.62244 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 153f7955-95cc-3c51-b56e-a58cb1a53b8d | -19.56106 | -56.61075 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 0a5ccbce-9da6-3ae6-bb6a-574e338d6ef3 | -19.56048 | -56.61551 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 0e4e5b1c-8a09-3a5d-aa2d-922bdde7a1ad | -19.55991 | -56.62027 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ed78a897-d7e5-3108-afab-30e587bed76f | -19.55933 | -56.62503 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6a89916d-b1b9-311d-89a5-ec957d760d02 | -19.55894 | -56.55216 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ceadd6b0-fad4-3fa4-b7bf-00a10551d977 | -19.55836 | -56.55695 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6e305ddc-2c8c-3516-a012-ea6c8c0fe2aa | -19.55831 | -56.60752 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 275e6c52-931c-30a2-86b4-d1badce571b2 | -19.55778 | -56.56176 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 37911e3a-aaae-3583-ab34-ee49b05dbe40 | -19.55777 | -56.6123 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 6df93cd1-3eed-395c-ab11-5750f1f99160 | -19.55723 | -56.61707 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 595fb7d5-76a9-3ac6-9ebc-aa675c83f060 | -19.55712 | -56.6054 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c979123d-b4d4-39d7-855f-783d68cb2cb4 | -19.55654 | -56.61016 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e573e01c-78c1-3cdd-ac60-cd62eb83821d | -19.55597 | -56.61492 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| d6d304b2-2571-315c-96e0-4848cf10741b | -19.5554 | -56.61968 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 6f0314eb-a24d-3e82-81e8-4de0b737d7df | -19.5526 | -56.6048 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8f90329c-4246-3888-b9d2-6ce2ee9ccc73 | -19.55203 | -56.60957 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d88bc375-d219-3f2d-9cf2-4b0d2870e4a9 | -19.55145 | -56.61433 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 91288c2f-4c35-30ca-bbfc-99a6e92ec4b5 | -19.54751 | -56.60898 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cd616eb1-7406-3ca6-a8b6-2acf91769e7f | -19.53286 | -56.57797 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 78771653-79a7-37e8-a633-2817695c7ef4 | -19.53229 | -56.58276 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0e56ae27-a9f4-3770-8884-fdea437eae7c | -19.5272 | -56.58695 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 52f4dce4-9a4e-31f0-a0d1-e87f73d204f5 | -19.51478 | -56.61438 | 2024-10-24 05:25:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 625122c0-21cd-30d2-add6-12fffd4c8a5a | -18.6694 | -57.3579 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4a52ff43-78d5-3fb8-b8f6-6dc43d141f32 | -18.66566 | -57.35316 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 03534e1d-5d48-323c-83e0-996e3fe84ebc | -18.66515 | -57.3573 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 76c89672-9a37-3f51-b3ba-86290d988a15 | -18.66193 | -57.34842 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 74f7e875-88c5-3d3e-b420-61ce94ee6435 | -18.66142 | -57.35257 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b3d30560-569d-31f5-b44c-49ec6c998ca8 | -18.65768 | -57.34783 | 2024-10-24 05:25:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README110.md)
