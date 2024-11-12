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
| 1de8ae4e-de1c-3b9d-8853-744c632ae1da | -3.66748 | -50.21704 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc38dc5c-ff2e-36d5-99b3-cdb584326f9f | -3.67223 | -50.26109 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e084c4f-d79d-393f-88aa-369bb8e53592 | -3.85493 | -52.38193 | 2024-11-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd4620c3-03b5-34c3-bf92-8fa2171a89be | -3.28455 | -50.0509 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c70b7e1-18e0-3cdc-9c5d-ec7b4bb667f6 | -3.66287 | -50.21888 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc0398a3-3351-3bb7-adba-5c9ab4d12694 | -3.85216 | -52.38822 | 2024-11-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a02500e-aacd-3689-b8d5-424519d51bfb | -3.8542 | -52.38621 | 2024-11-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0fa5e43-5ece-3349-a052-e73593026932 | -3.66757 | -50.21457 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8898d48-b0ca-3595-afa0-6fd465c730ad | -3.43606 | -50.30684 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5242fc6e-ea30-3d5e-95f7-b7c606590c80 | -4.33966 | -55.36684 | 2024-11-12 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acd76bcb-7bc9-3295-9d06-38492aaa5400 | -3.84323 | -50.22222 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f93d249f-d2d7-349f-b6df-ef124e76252a | -4.0551 | -48.32081 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12fb6bd5-a078-3a18-b866-4b98d003b263 | -4.34514 | -55.36772 | 2024-11-12 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ae41b7f-37b8-31df-8a21-fb57abc7b51c | -3.9411 | -48.15178 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0d3b09d-b5d6-3459-948a-076ee7ce02a9 | -4.73208 | -50.6376 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bb6ff4b-311c-3f83-aa2a-ff3e6a8acb83 | -4.11332 | -50.23973 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ef5a53-374a-3cca-83f6-5947accbed07 | -3.60853 | -48.9138 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26aa0cab-6afb-371c-98a5-08513a460d8c | -3.57352 | -53.79021 | 2024-11-12 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fef59911-db19-31ce-9fcd-6ec0c50b85fd | -3.67225 | -50.21029 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af0f9b7e-210f-3f7b-aee7-9451689bdbe8 | -4.24069 | -55.87173 | 2024-11-12 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a65dc685-c63a-3816-a75e-0d787239e8e6 | -4.11061 | -48.49467 | 2024-11-12 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73bd5214-d32c-3862-a120-7af47458e844 | -3.99592 | -49.2764 | 2024-11-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 368e02b2-4791-3e82-a1cd-bca3e8be321f | -5.44673 | -44.01967 | 2024-11-12 04:23:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd59fa6c-c426-3cb6-a6eb-8ab9ee2bc360 | -4.09162 | -48.32195 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d926ad69-fa03-3fb1-bbf2-2c0cca088566 | -3.9487 | -48.14898 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c793a83e-6dc7-3f16-ad2e-4ab4ebe365eb | -3.24601 | -50.31055 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aafbe163-7d1e-391c-8ef0-9ba67c2227a7 | -4.15505 | -50.79598 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c52d983c-3972-35c4-88fa-5b498c3006c9 | -3.95678 | -46.71241 | 2024-11-12 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd462a0-be15-355d-8754-2730c674d051 | -3.953 | -48.12212 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e3272e6-48a4-3b51-a679-ab3e7c4d8051 | -3.39065 | -49.86026 | 2024-11-12 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3b45d94-6038-3ed2-8b95-9440c34b235a | -4.31066 | -50.81146 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf68d445-25c3-3ce6-b544-7d60180e4b41 | -4.05159 | -48.32029 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 897520d8-7871-32f7-ae43-a3689eab969d | -3.67777 | -49.9519 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b90d439-a053-3c40-8573-f22cd881cf1d | -3.95421 | -48.18156 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d9d916ed-963f-3614-92e8-62c419782b76 | -3.95297 | -48.18935 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18ef4de7-34c9-3686-86e1-d5e0ff9b8151 | -4.05221 | -48.31638 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a32b8e7-f9b2-3dac-b2a9-6259a3129723 | -3.79552 | -50.04269 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0356d478-50a0-3ab8-aa4d-f2863e87a305 | -4.09512 | -48.32254 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cfbd15e-ade9-3964-a50c-6aed18039ff2 | -3.65662 | -50.2078 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d7bcfac-e873-380e-9063-613144aa0919 | -4.24784 | -50.2564 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f43dd4a3-4454-3426-92b5-ddb6cdce478e | -3.83161 | -54.59973 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaa00d9e-fc95-3196-818a-3d34ff97c903 | -3.62212 | -54.11368 | 2024-11-12 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c63a31e-eb1b-3b37-82f3-745267cb42e9 | -3.94173 | -48.14787 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68848b72-308b-32f2-8c50-68012b599ef1 | -3.61375 | -50.57873 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f902d752-a331-34b8-ae2a-5b54dad0d4ee | -3.6707 | -50.2201 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c301cea3-139a-319a-9cc0-882ada9b2e0b | -3.3078 | -50.07982 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 241b14fe-03aa-39cf-9a2e-f5f942129928 | -3.72889 | -53.7853 | 2024-11-12 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c02b438-8540-3058-85dd-ab89cbc7982d | -3.94932 | -48.14508 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01c68287-0777-3cad-b08b-819947c42a6b | -4.22126 | -50.66771 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15ba96ad-8647-3033-8353-2c891cfde7f4 | -3.67184 | -50.26349 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57728e87-ff8a-3e2a-92ee-fb098a1d07b9 | -3.65584 | -50.2127 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c01ee07-d308-388d-92c3-3314adca2be0 | -3.43514 | -50.30822 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ceb95090-7be2-3490-903f-ca3dde764b11 | -3.24683 | -50.3055 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f5d7f28-9cab-3624-bac8-20173230258c | -3.24518 | -50.31561 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ff321d4b-75fd-3faf-a3b1-14165e144f73 | -3.38681 | -49.85964 | 2024-11-12 04:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4056081-d3c5-3977-b5e3-f9496f8c1c17 | -3.85287 | -52.38381 | 2024-11-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8af7b0cc-d72e-3ddc-bf43-05bcd39ed19c | -3.98844 | -48.31038 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3702d13-99ac-3ec3-8b8d-bd66c4cae491 | -3.34278 | -50.13613 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e354cc83-ce3b-3496-b6f3-008c1786254e | -4.5412 | -49.79123 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fe1f082-40ca-3999-8e82-5df43fc83cc4 | -3.95483 | -48.1777 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 73a09a8b-df8c-3cd2-8909-ce5849bdf735 | -3.76545 | -49.47782 | 2024-11-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d50ee3c5-6749-39a7-a35e-33761e226b58 | -3.66071 | -54.65617 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e266b045-6a42-36c3-b232-7ddace6c964e | -4.11064 | -50.23684 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc596d61-e7dd-3105-b2de-62bf5f68af0a | -3.95544 | -48.17388 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf4b24a0-7590-32b9-b1f2-d9c179e93b91 | -3.94702 | -48.99812 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e31b57a-0bbf-385b-8d26-e3c1109e23b4 | -4.54496 | -49.7918 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f5e4b278-531b-364e-875d-011d4790a079 | -3.43526 | -50.31189 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7c191e9-fea3-3bd9-b339-1db80071d420 | -3.62162 | -54.11667 | 2024-11-12 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da79e673-cf69-38b3-aea9-69cad35fd6e1 | -3.26326 | -50.4298 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef7a3df0-850c-3277-a991-dd13aba18ce5 | -4.03462 | -49.73436 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f87c034e-cb9b-3243-b56b-39089c3e001b | -3.67221 | -50.21276 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 967fbd8d-eb2f-3f6c-b39d-bfcce55702bf | -4.11453 | -50.23742 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60210c05-be0a-3d73-b720-077d8d112323 | -3.28375 | -50.0558 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ae18d77-8d2a-36bd-ab71-18bec7c85cb8 | -4.46846 | -44.23024 | 2024-11-12 04:23:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e592c67-e23b-3deb-a8ef-d3bfe2d19b94 | -3.43824 | -50.31392 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2fdb9a6-0a47-399e-b2ed-8f4dd8f32511 | -3.95832 | -48.17822 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac94cfd0-1469-3135-a6e7-675ff0d4fc0b | -3.37066 | -51.10514 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 448a46af-2a85-3b69-9504-f82be39c813f | -3.84762 | -52.38768 | 2024-11-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f44f6591-15f3-3223-bc8d-16cfbc8276ac | -3.95605 | -48.17004 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8dd3f9e0-0b4f-32ab-bba8-d4499c9f32b6 | -7.42891 | -35.23532 | 2024-11-12 04:23:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1d66bbc8-3e9a-3144-864b-7d99780b8def | -4.05572 | -48.31691 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35135ded-a7fa-3dd6-8e57-93cd0e2ecd0d | -3.42764 | -54.53534 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c41eeb4-4751-39e1-ab7c-51a02e17ec31 | -3.57446 | -53.78458 | 2024-11-12 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 62d291e0-04c4-31c3-b0bb-5c912e03a4d6 | -4.09264 | -47.71016 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23e6ec59-27c1-3de1-9b90-0300ba9e5554 | -3.40494 | -50.37484 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37276db2-8e0b-3471-b6bf-9993c11c6f27 | -3.31959 | -50.30704 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d62988f4-184b-32da-bfed-fb0e814b9376 | -3.79014 | -50.1013 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 46f5b86b-769c-3068-a1d5-e9d408bff0b5 | -4.28364 | -50.67484 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 413076a7-d46c-3687-9e1f-a84cd224271c | -4.04694 | -48.2595 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f7de3bde-5ec0-3506-a874-cdb4500dfaac | -3.66538 | -54.66069 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 938e29ed-1579-33ed-955c-587bc5b8025f | -3.78705 | -50.0958 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 25347f71-83ac-3a7b-b032-8c702d6f7053 | -3.79629 | -50.0379 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86500928-abea-3049-820a-d26c57aee5b8 | -3.40612 | -50.29165 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4182bab5-cbdf-3d94-9447-90e9d94563fc | -4.15446 | -50.79955 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca77a69a-416e-324a-a089-8d4e8a92eb5a | -2.93915 | -49.36469 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcd312ed-7380-35e5-b380-56af4f80067d | -2.8945 | -48.30883 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7953578c-51f4-374c-9613-05cf21dd0026 | -3.26356 | -48.74784 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c47492-160b-3d55-8cd0-d59d3fd6e965 | -2.46524 | -50.38938 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25a79e30-adcf-314f-84d3-ff605677d79c | -3.26291 | -48.75198 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f26ee7a3-5c68-325e-a8a3-c7839d2f3aa5 | -2.78925 | -50.31014 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
