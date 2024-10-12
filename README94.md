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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab6337d1-433c-330a-aa3a-aa5fc3c704f7 | -17.84468 | -57.3355 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ffc9ce1a-d94c-3dbe-ba69-e2476c03d08b | -17.84452 | -57.35779 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3ed245cb-4049-3ab6-b95c-ef6502da1d49 | -17.84436 | -57.3801 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4baf9483-8ccc-384e-a9ad-a89e42f459e4 | -17.8441 | -57.33912 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 80476eb1-5b65-3024-a0db-59b19e4c0472 | -17.84394 | -57.36142 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| cf7bdd6c-e106-3769-ab05-a3463a658e1c | -17.83963 | -57.34578 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d6ce7ab0-806d-3016-a856-7bcf480a4f66 | -17.83906 | -57.3494 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 16f49573-f204-31a5-8941-e49fe2c6f363 | -17.83832 | -57.37533 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 8e366ee8-50bd-3203-baa5-84d6b3998789 | -17.83774 | -57.37896 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.7 |
| bdb55361-44fd-3b11-9271-8e88637dbe6b | -17.83732 | -57.36026 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a91f2c14-15b2-3d27-9e6b-e8c0017469ba | -17.8369 | -57.34159 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0d762d54-95f1-3e0c-868b-711e6d1afddc | -17.83674 | -57.36389 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 74ea88e6-55f4-35c8-8783-d752b67d0b8f | -17.83443 | -57.37838 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.3 |
| ffa445ee-0f4a-32d6-ba7d-26050a3b7cec | -17.83417 | -57.33739 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 39869da3-ad66-39ed-9103-563b7fb3a7c6 | -17.83359 | -57.34101 | 2024-10-12 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3926dab2-b7de-38c3-b9d8-e70d7b2c7a64 | -17.84047 | -57.38316 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 775cbee0-cfa5-38fd-94bd-d3b8202e631c | -17.83716 | -57.38258 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3aa03c3c-2993-379c-b9d0-8395bef0f98a | -17.83575 | -57.34883 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5fbdbff0-6ffb-3eb4-9052-86b5483703ee | -17.83517 | -57.35245 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f581b798-6486-31f4-9fdb-fec20d69d2ea | -17.83401 | -57.35969 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ca7b9dee-7f4c-3ec0-9ebd-b85e0a01be72 | -17.83385 | -57.382 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| f198dbe4-aeee-34a9-900b-700525afed41 | -17.83301 | -57.34464 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6cb285b1-712d-3205-844a-4186784fe72b | -17.83244 | -57.34826 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8c80ae33-1e67-325d-95bd-cb72094915e5 | -17.83086 | -57.33682 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c787f0c7-52d7-31d9-b722-9e5a8d4487df | -17.82912 | -57.34768 | 2024-10-12 05:01:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7f1e78e4-141b-306f-a8b2-5dac9e6ba466 | -17.16644 | -57.46798 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3d44e607-1de4-3f3a-9ce7-7e248e4bc289 | -17.18223 | -57.43341 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5e194510-d502-35eb-8e95-16df96649d18 | -17.18165 | -57.43704 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ac3954be-698d-38b6-aa17-c076af1f245e | -17.18107 | -57.44067 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1887c171-3b5b-3cf4-83a1-ff196f0d0d50 | -17.17891 | -57.43284 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d930a09e-b217-3783-b174-6533f4bdab1d | -17.17815 | -57.45882 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c10e07d7-e585-39fd-9f36-f3eb75c7cf85 | -17.17756 | -57.46244 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ed08747a-a992-39b1-8aca-4e34d9d3d700 | -17.17698 | -57.46608 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 21923419-f994-3cdf-af3d-adaace5ade04 | -17.17658 | -57.44735 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| acd31cc1-9686-3876-9a0c-5d145867ffb1 | -17.1764 | -57.46971 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a023d5b7-1dc5-3a9f-b4f8-e64ea6e147f6 | -17.17581 | -57.47334 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b1a32956-87e0-3b61-a2d6-9d6b221413de | -17.17483 | -57.45824 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b2a27508-743e-3660-b12e-b8b0ca2190ab | -17.17425 | -57.46187 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e504f4d0-6f4d-3e17-bf44-980292db8bcc | -17.17366 | -57.4655 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b92ad062-e9b4-3857-bc6e-2c181d7e716c | -17.17308 | -57.46914 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| d58616c6-81d0-3b9d-9bc8-a71c00096cd2 | -17.17249 | -57.47276 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9bc18925-c180-3385-bfea-3d90cfc65f8a | -17.17151 | -57.45766 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e4ecfeaf-dab0-30a6-a24c-9a143fd7a170 | -17.17093 | -57.4613 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d3c92404-ff29-3bb2-974f-61dc503b3938 | -17.17034 | -57.46493 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 266fc4b9-1925-3d0e-9746-2dfa81b18626 | -17.16976 | -57.46856 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9896f725-c431-3199-ad7b-9df26863be50 | -17.16917 | -57.47219 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ed5e71e7-f795-30eb-ad78-231c6f93496d | -17.16819 | -57.45709 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bfd4ff6e-a579-38bb-a2d5-1161a5ff7c10 | -17.16702 | -57.46435 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7c5e15dd-614e-3ac4-9dcf-b467964dd843 | -17.16585 | -57.47161 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d6abddb1-5c9a-334a-ac10-3425aec06bf7 | -17.16527 | -57.47525 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c2716748-385c-3558-a336-9cbe5826917f | -17.1637 | -57.46378 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6fe5f11d-6e5f-3d21-8b31-885544d54e12 | -17.16253 | -57.47104 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d79bda6b-0bda-3003-a88c-81561da281e8 | -17.15589 | -57.46989 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2c127d3b-3273-358f-81ee-ca89e717cefd | -17.15199 | -57.47295 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 008c560f-ac26-3c3f-a0ef-63eb04b15834 | -17.14867 | -57.47237 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ecc802cf-161d-354b-af64-63316b34e8f2 | -17.07284 | -57.4365 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b652b076-1c30-3db9-8073-763a8c154ee9 | -17.07168 | -57.44376 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6ccf1afd-a10c-3f4e-84ae-a47ae420a77b | -17.06836 | -57.44318 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3c364302-2cbd-3ef8-8110-10c5a4692ddd | -16.99741 | -57.46107 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 3ce403b8-10de-320f-9be2-2663034f6b4c | -16.99683 | -57.4647 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 5bb0f3c2-8ecd-39c6-8739-89811207174a | -16.99625 | -57.46832 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| fb252d3e-63ad-3bbc-8d69-9c48b11df843 | -16.99566 | -57.47196 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 0e6efc5f-2c21-3b9e-aa0f-af96b459203d | -16.99508 | -57.47559 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e88a1917-2ee2-3c78-90bd-b62f3b0f1c42 | -16.99292 | -57.46775 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| e23b3eec-458f-3dd4-b01b-6681231498fa | -16.99234 | -57.47138 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 33901992-24a3-3c7f-adfe-efcbc3302477 | -16.99176 | -57.47502 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a47e6b9a-0cda-3f95-aacd-0ab1500e068e | -16.98785 | -57.47808 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b5a5e2da-8194-33f5-af30-f7c8541f80d9 | -16.98546 | -57.42916 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3999a701-c2c1-3188-b18a-0925d6f2579c | -16.98488 | -57.43279 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d768d47d-f2d0-384c-80d5-03abb758e830 | -16.98395 | -57.48114 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5da1b087-49fe-3398-9074-14069fa978e7 | -16.98336 | -57.48477 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5f14d8c5-fb95-3778-a10d-ec9b4028053b | -16.98156 | -57.43221 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| ee70654d-dcd7-3808-9ea7-53594ebb0a1d | -16.97649 | -57.44252 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 01a91ffd-2e36-368f-8d05-b38f52af1f70 | -16.97591 | -57.44615 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| def33071-5571-324b-a406-aa190dcf62bd | -16.97533 | -57.44978 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 19b583be-52cf-30f3-b1d8-b1ccc481a466 | -16.97376 | -57.43831 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0bc4495c-fa12-3b9e-a424-44be4e9083bb | -16.97317 | -57.44194 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c4fbc374-8c50-38e4-b668-30c289dee239 | -16.97259 | -57.44557 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| d8a12bf1-998f-373e-baba-e8aa2ed41986 | -16.97201 | -57.44921 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 3dfbc676-447b-305d-8afc-29a9fb2bcd4e | -16.96927 | -57.445 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| cbb4193e-7cad-3c05-a72c-38b364f3b278 | -16.96869 | -57.44862 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 7ab68d3d-481d-3de4-a01b-da671d3e2cd9 | -16.9677 | -57.43354 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 35d5a31f-d7c4-3917-8ec0-121c20127da5 | -16.96438 | -57.43296 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 04d46e46-39da-3455-8cf4-c8ec47436b9d | -16.96382 | -57.50007 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 47afaa42-c6ee-353f-870c-65e5b4060831 | -16.96324 | -57.50371 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 58abf875-6969-3c2c-be00-987da1ea9723 | -16.96047 | -57.43602 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dc4907c7-f4ad-3a81-90fe-d394c743bb1c | -16.95991 | -57.50313 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7fb1ae1a-fd43-3065-8c48-15b6c985f7f9 | -16.95715 | -57.43544 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| af406743-a9f6-389a-8aa5-ab2dcdd54431 | -16.95659 | -57.50256 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3a8cf0eb-b1b4-38ec-b4ce-420b0274eacf | -16.95657 | -57.43907 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e5c0c0ee-6b97-323a-a8b0-4097e8b1ab84 | -16.95327 | -57.50198 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c2b12ba9-d558-3544-8041-fc235617670e | -16.93533 | -57.69768 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8e5e86be-7699-3c36-9394-12ff9b111750 | -16.92044 | -57.68379 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8aa5bcfa-dcc8-35c5-ad98-cf7756b2d89b | -16.91711 | -57.68321 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7b9220d6-e4e2-398c-b6dd-025582c3cad1 | -16.8588 | -57.43354 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f9b79207-de12-3ae2-a1ea-e6b103c6980f | -16.81132 | -57.41042 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 40d06da4-77c5-3231-b845-ba754d0a32da | -16.76592 | -57.56676 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4fbef6e8-969d-3826-9091-2fc15ee3ab3f | -16.76318 | -57.56253 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ebe81801-d75e-354c-84bb-ec4d35dae84b | -16.76259 | -57.56618 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4f4a5f64-56fd-386c-8303-bb909a735939 | -16.76044 | -57.55831 | 2024-10-12 05:01:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |


[Clique aqui para ver as próximas entradas](README95.md)
