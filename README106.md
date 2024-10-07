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
| 9df01764-3f45-329e-9a5e-b9e34f316d04 | -16.99056 | -56.72905 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0af7ed6b-384d-3a95-96d7-4bbf02dbad20 | -16.98994 | -56.73283 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ed3119f-acb9-323d-8a00-a4f561b72610 | -16.98967 | -56.71336 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cb47a922-d6cf-3c1e-ae9d-52a0c57bf43b | -16.98753 | -56.70522 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 475623fc-0025-3d27-a8f2-dca9b4777381 | -16.98691 | -56.70899 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 02dcca13-9ab9-3358-8105-3055ffa02ab9 | -16.98594 | -56.736 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 27d8700a-affe-3eaf-a117-b2d32493caeb | -16.98532 | -56.73978 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b5688afc-d06c-3176-ad94-59a9b0a95fd1 | -17.1686 | -56.97149 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ddb6ff46-62be-3b67-b7f9-be69ba48eb25 | -17.1652 | -56.97088 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ce9db945-5d89-38be-8c3d-42fe47f0d4d4 | -17.1584 | -56.96967 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| abf605c4-4ab9-386f-9737-f99184ea88ce | -17.15776 | -56.97349 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7ae4c252-7797-3269-9e51-5df21978547e | -17.1482 | -56.96784 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6639b688-f32d-304b-a668-405ba024c09d | -17.14756 | -56.97167 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fac60b92-a35e-38f7-b593-a28ea12400e0 | -17.1448 | -56.96724 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c7b11050-e82c-3a1a-9a9e-ec95be3e7ba3 | -17.14416 | -56.97105 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2896169c-b858-3a04-8ba8-07c9d0b569ac | -17.13496 | -56.8166 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |
| eb3f9fdb-a30d-33db-8e72-fb21c9d56e7b | -17.13433 | -56.82039 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 8b5637bf-f42d-36ed-8bcf-82734300ed09 | -17.13221 | -56.81221 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 156.7 |
| 93321bda-dc73-31bb-9d56-a5ecc5d2675d | -17.13094 | -56.81978 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 2bd40705-e8d2-355a-94dc-ae23fc12cd93 | -17.13031 | -56.82357 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 5dc6a522-3ea5-3133-930e-834bfe63ddb9 | -17.12968 | -56.82736 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 7efe8361-8301-3456-a1dd-786cd270f24b | -17.12945 | -56.80782 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| 956ec918-94e2-342e-bf15-b8a4f529733b | -17.12905 | -56.83115 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.0 |
| 14971a13-7abf-3955-8a34-ae12d1beac9a | -17.12882 | -56.81161 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 0c65ced3-4f82-3738-b412-2e716f1b0491 | -17.12841 | -56.83494 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 45837f3a-6f1f-3e7f-a37d-ff51d97c80e2 | -17.12778 | -56.83873 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| f8bab5af-1b43-3e3a-95fe-4e3f9f08e108 | -17.12756 | -56.81918 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| ca041a85-312e-37b6-8092-7fc3a73043d0 | -17.12715 | -56.84251 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 4b5ac72d-4fe2-39f7-a0e9-cd5888f14e8e | -17.12692 | -56.82297 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 70e3a34b-0da7-354c-87de-494b299dc1cf | -17.12629 | -56.82676 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| da04248e-2007-3afa-9e95-c1beb7c36324 | -17.12607 | -56.80722 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.0 |
| 0117b184-380d-3626-8311-fb574e6da0f0 | -17.12544 | -56.81101 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| f0a90749-5718-3106-9ffa-6a4c4b9d2f69 | -17.12503 | -56.83434 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 833b10c0-03df-37d6-ae3d-0c02918a3c45 | -17.1248 | -56.81479 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 162.6 |
| 9bfb9b84-3849-3a54-bfb5-bd720108fdb9 | -17.1244 | -56.83812 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 564d6298-cf18-3d31-ae8d-989e01bfbb15 | -17.12417 | -56.81858 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 30915792-460f-3c9f-8b80-4e83f96b4ce6 | -17.12376 | -56.84192 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9d31ae2b-8888-3a2b-b1f9-d63337ee52c9 | -17.12354 | -56.82236 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 3b01b597-057e-3108-a848-188869687c92 | -17.12268 | -56.80662 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 1cce0b4b-512a-36a7-b829-5fbaa2a8e7e5 | -17.12205 | -56.8104 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 602dbc9a-bb69-3d4f-9bdc-e7b9cd21e000 | -17.12142 | -56.81419 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 600463df-4011-3d14-bd16-0bd266813772 | -17.12101 | -56.83752 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 06ffa170-bf50-31c3-bf56-b1601dfa08b9 | -17.12079 | -56.81797 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| dae7b47e-a87c-3f4f-a6a5-fd27afad2ebb | -17.12037 | -56.84131 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 12727e23-29b0-3cad-98e1-6b8888f063b5 | -17.11867 | -56.8098 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3d32e70d-700c-3a10-8ff1-2bff9a94ac2a | -17.11803 | -56.81358 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b4722c88-881b-30a2-ba8b-ef6e288598e8 | -17.11762 | -56.83692 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 2f913ce6-4b0f-37f3-b498-40f033d4f0dd | -17.11699 | -56.84071 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.0 |
| 5f515fbd-6b94-3df9-b2b3-ffc10c08066f | -17.7467 | -57.09262 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6f11cf90-48e9-348f-bc0b-747578c6a81f | -17.7433 | -57.09201 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 58387064-06cc-3099-b6d8-94bf17fa3788 | -17.7399 | -57.0914 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ace8ec29-d6af-3ee2-a16e-e73806464786 | -17.73926 | -57.09523 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 823bf282-4fab-3d52-8f56-4c45bc96b4e0 | -17.73862 | -57.09907 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 364ff3fd-054d-311f-a5db-f67f749d3228 | -17.73844 | -57.0793 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 018a2495-df34-38a2-9e35-56678fcd42d8 | -17.73651 | -57.09079 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| da60879f-68c4-3015-9926-6b2a055a55c2 | -17.73586 | -57.09462 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 38c52155-18ff-3c1a-84f3-486435340caa | -17.73504 | -57.07869 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7049c925-1cd8-36fa-973b-71bf4065336c | -17.73247 | -57.09401 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 66ddb319-a55f-3c8e-bb41-04402015caaa | -17.73182 | -57.09784 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6553df03-8559-39a1-b4b5-885e0ed49683 | -17.73164 | -57.07808 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 1eee04b0-cac0-3159-ab91-168ffc9f7f08 | -17.731 | -57.08191 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 14e0693f-9d3a-3e70-bffd-12e62fdd2c0a | -17.73036 | -57.08574 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 15144293-8f7d-386d-8b5b-2f6cdb327444 | -17.72825 | -57.07747 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9031b7b0-160d-3aa6-9a09-b89592fa5d0e | -17.7276 | -57.0813 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| de6e945e-0533-3d06-9c41-bfb53f077ffa | -17.72759 | -57.07741 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| ff412e58-a2ec-3272-904b-942dc7a8f530 | -17.72696 | -57.08513 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d5c0a870-f80c-30b3-aaa2-6b01c85aeb05 | -17.72696 | -57.08124 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| acc0e6a9-3177-30d1-884d-f698cdd0b3e8 | -17.72633 | -57.08508 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f76cff16-e244-3563-96db-e0856474c493 | -17.72632 | -57.08896 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 933ec9e4-068e-351f-a881-7302fe5d9b3d | -17.72569 | -57.08891 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 194577fd-3aec-38e6-a8e4-6253b66071d0 | -17.72567 | -57.09279 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6eff4924-96c2-338a-b6e8-21f31f90b676 | -17.72506 | -57.09274 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5f495a44-3407-3e93-9b7c-786b78d18396 | -17.72419 | -57.0768 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.7 |
| 3cb05477-b0fb-3b59-84ff-16c877a2a86f | -17.72356 | -57.08063 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| fd8e163c-b920-344a-b545-b26dd4745847 | -17.72293 | -57.08447 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 430d497a-052f-341d-81da-10cc611b607b | -17.7223 | -57.08829 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2b7d85cc-b538-3e24-a3d9-92b0a5721fcc | -17.72166 | -57.09213 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9c176063-8a3b-36f5-b39c-eeff531a94db | -17.7208 | -57.07619 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 8a43366d-d15c-3190-afff-302f4be130f6 | -17.72016 | -57.08002 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 849b25bd-0cd7-373d-a2fe-6d658396b9bc | -17.71953 | -57.08385 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 64166f92-0923-30b8-8cc0-af8f98498d57 | -17.02604 | -56.83624 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5a118c62-8abb-322f-b638-7cf353a7178c | -17.02541 | -56.84003 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 074d5679-2987-3218-92be-7cd99fadc85d | -17.02265 | -56.83563 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 42524212-1abb-3435-9ee0-7529558392a1 | -17.02202 | -56.83943 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 89aade95-87e5-3e97-948e-52b71a7d9a4b | -17.01926 | -56.83503 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| f82bdb2d-2c3a-3608-9131-b12b74293b90 | -17.01863 | -56.83882 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 818978f2-5348-3b7e-9a53-c8b204ad6822 | -17.01587 | -56.83443 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 553070f2-1812-3762-a744-f116741fe1d9 | -17.01524 | -56.83822 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fd5a3f38-c0c2-33ad-88e4-9f2e2fa7a911 | -17.01248 | -56.83382 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1bbd4e10-4a28-3907-a472-e0347e772d1b | -17.01185 | -56.83762 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6d313ff9-2bcb-3f97-a048-14982c219926 | -17.00973 | -56.82943 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2ed9de28-acd7-3ef7-804b-661bf088f691 | -17.00909 | -56.83323 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 846b7a10-295e-35c7-bf6f-09b6d46a89ab | -17.00846 | -56.83702 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 34c72c00-4b40-3448-9c88-b57fc65a6972 | -17.00634 | -56.82883 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a0421a22-3834-329b-bbf8-8e85cf1f2a61 | -17.0057 | -56.83262 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3460416d-4aba-3064-96f4-f60c5cd0047a | -17.00547 | -56.82911 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 730ae557-2065-324e-8b79-9330630f4a18 | -17.00485 | -56.83291 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 68d78a1c-2e85-39e4-867f-59ced982545b | -17.00271 | -56.82471 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 96159e7b-8e57-39e4-af16-30c3535a919b | -17.00208 | -56.82851 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f849655c-3af8-33b8-8832-ed5619131b0e | -16.99932 | -56.82411 | 2024-10-07 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README107.md)
