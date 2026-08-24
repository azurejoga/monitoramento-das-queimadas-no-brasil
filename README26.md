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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc737db7-3023-3dcc-980f-f12e26e0f024 | -6.35055 | -54.76464 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f18e66e0-940b-3303-a65b-38b65217767d | -3.53285 | -48.18291 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 615a6505-c4ec-30aa-8d4e-77420bdc9c88 | -6.37113 | -54.94338 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 829e7025-f74a-3d76-8519-da8155553bda | -7.37684 | -45.8233 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| abd9d5ad-59b9-3bbc-b1d9-3f733eb9f80d | -3.0518 | -51.21936 | 2026-08-24 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40584b55-f906-3048-bfe2-2ea372ab6848 | -7.19079 | -42.75923 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a14e23c7-f3c5-34e8-9a11-8a1b6aaab3c3 | -3.01093 | -51.05302 | 2026-08-24 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 396a97d9-296f-3df8-8e42-962ad1c5f396 | -7.27019 | -45.36673 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a693aee9-d983-392c-9a95-2c7c54fdd608 | -4.02271 | -47.72436 | 2026-08-24 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc233f89-637f-3226-93fd-9e63d19be8c3 | -5.78342 | -50.18979 | 2026-08-24 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b437ca59-7803-39ec-b9cb-ef0aa0f9f0ce | -6.18458 | -53.52597 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8584cf59-04a7-37ac-9d52-749d34296941 | -6.17706 | -53.52472 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3068e0d8-13dc-3146-94b7-271a0db2fcfe | -7.26492 | -49.89 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5fedf23-d9c5-341a-ab07-0b130febd77e | -7.18694 | -42.74659 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 366b5d41-5950-327d-a09f-23fd6bb05303 | -7.25999 | -49.92116 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6f6d004-6b7c-31e3-a332-dca7668535a9 | -7.2666 | -49.92221 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37903ecd-7763-39b1-8b7e-30334ea931ed | -6.13199 | -57.83206 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 405c11b1-4581-3505-b170-4065301db259 | -7.9755 | -45.25447 | 2026-08-24 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7692f01e-1625-358e-81c5-13d065d60ead | -7.25829 | -49.86766 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d4c86d9-50ac-3d90-a28e-521fff5fad4e | -7.97155 | -43.92598 | 2026-08-24 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ba88272-45a7-34e6-aaba-d28be83b0cef | -5.93843 | -57.73233 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e74a79b1-1c9d-34c6-bba7-779303bbbde7 | -7.28187 | -45.36841 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0708bf36-c740-3364-b1b1-ad83f82c8531 | -7.25772 | -44.20226 | 2026-08-24 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42907649-9ac4-3cf1-a95f-e0d220ab398d | -7.25354 | -44.20157 | 2026-08-24 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8e435e6-daef-3cde-b41d-1911c0fa4258 | -6.17629 | -53.52931 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30018d4f-d43a-3341-9df9-fca5a0484b20 | -7.24836 | -49.86608 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a66629ca-ef89-3ce0-8780-595014224762 | -7.4231 | -46.72338 | 2026-08-24 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82376797-6a95-3285-a446-924c0b1708ed | -7.35999 | -45.80655 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e5f62d22-122f-3ac8-a9b9-da7460bd3000 | -7.48876 | -45.13593 | 2026-08-24 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a4a0159c-3b9b-3c32-be9f-d831f137dac9 | -4.98607 | -47.48195 | 2026-08-24 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56d9d31f-0b3c-37a0-8a60-7e5de638975b | -5.0654 | -49.38413 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb2af95c-1b6b-3334-985a-6f90000d5e2d | -5.88032 | -52.10699 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0b4f06b-c61d-380e-8d9a-7b6ec1074d1f | -5.8652 | -50.14603 | 2026-08-24 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be268a87-e039-3c4b-91c4-91d5c20dcc8b | -6.59483 | -52.45729 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c8390b5-3d2c-34bb-abbf-2a78cce6e7e1 | -5.78143 | -57.56778 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0fd94f7d-3c5c-3417-bb4f-897feae60d8c | -6.37052 | -54.94709 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e646aae9-377b-3c19-8e3e-e88451962fef | -5.95342 | -51.96701 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3eab6ba1-c185-3d10-ade1-925508610d59 | -5.06373 | -49.37327 | 2026-08-24 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 219fa210-1fcc-315a-ad02-96201ec563ba | -7.25553 | -49.86367 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f89f833a-f3e4-3353-8312-8c313ab7b773 | -7.89878 | -46.34227 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f6c9ca0-8e01-3c4d-9e7a-c2aacb9ebbee | -7.14839 | -43.08979 | 2026-08-24 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c63295f4-66fc-3ce6-9972-21c28207f4d9 | -6.34245 | -54.76327 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e998121-71fd-3900-969e-eef6b89466b2 | -7.44695 | -46.91988 | 2026-08-24 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 105e3251-387c-3e6e-96cd-64bfda1fe0fd | -7.35241 | -45.80542 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15a66d84-885e-3ef7-a0b4-4df7d6d7eb5f | -5.78066 | -50.18577 | 2026-08-24 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2af97f7-61be-3730-a71a-dd660383bb69 | -4.60664 | -55.73475 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23818202-48fc-307f-93e6-657b41d497d0 | -4.99396 | -56.1383 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe17ecb6-57a2-31cb-93fd-bc47cbc84ef9 | -7.33944 | -43.42277 | 2026-08-24 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a6ceaa-a944-3755-9d1a-b9973c2ba34c | -7.26054 | -49.9177 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d90a198e-5c84-309b-986c-79bef40436f5 | -5.9394 | -57.72678 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4cdae50-72d1-3a02-ae4f-c379138c703c | -5.87331 | -52.10576 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d443b07f-83aa-3f52-8cc0-5f85cad9ffe1 | -7.2412 | -49.86849 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f940f576-4942-3336-b6c8-063f29edaea0 | -6.34049 | -55.87092 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92d0d721-e13a-3c27-9854-39b0554d2b65 | -6.34424 | -54.75258 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7340d53c-d9ed-3ed2-990d-34f9ed9acfbc | -6.3459 | -54.76752 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d296dd73-a6b0-3221-ae24-79f7d3c364a1 | -5.00308 | -56.13958 | 2026-08-24 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86d599e5-5f69-354a-b366-021e25654a90 | -7.26329 | -49.92168 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3a14ab4-4a72-3720-b894-a4475e64e022 | -4.73505 | -49.28277 | 2026-08-24 04:44:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d19ccf9-8fbc-35fb-af18-ed559be8aa62 | -6.34365 | -54.75614 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2814b9e1-bba3-3f98-a804-f065cbf2a110 | -5.68687 | -53.74652 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53262a1d-653b-3f5e-9fc0-6bf2bbccbf58 | -6.14442 | -57.93903 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37a48f48-d6cc-3b06-9dc5-0757a570b105 | -3.25835 | -50.82375 | 2026-08-24 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d94951c-2b30-3894-9137-22cc042948fe | -6.14392 | -57.94192 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5bc90bc-a646-3263-b087-61b8348f1a98 | -6.61977 | -53.35207 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb871d8c-eca9-3a01-ae91-bf59e4dcbccc | -4.53568 | -55.51523 | 2026-08-24 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f19c9465-9040-3c45-afa8-61ee0e08092d | -7.26384 | -49.91822 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fc43b6f-c204-390b-b88e-817605482b87 | -6.1951 | -53.53246 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df8d4d30-6c56-3c24-a361-a05e95535c4e | -5.68763 | -53.74183 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204a4f82-536d-3a90-8067-588f584fa724 | -6.43629 | -52.75832 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 695c28c7-8d29-330a-beaa-7afa7ee90814 | -6.43591 | -55.00385 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7aeaabd4-90b8-31d7-adf5-d17692ca8426 | -7.36547 | -45.82162 | 2026-08-24 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fdd1aafc-ec6f-362e-8456-9ad7d3842659 | -5.78635 | -57.56879 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ce4bd90-7716-399f-a682-8f516a9297f9 | -6.22255 | -55.92645 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e51034c-edef-39e7-b9ee-f72c38328292 | -5.5722 | -55.82022 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fceb8c4b-60ed-3ce7-b796-7a52259c6a5b | -6.2189 | -55.92147 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cce22187-2aa1-3785-a550-0e4b5dfe5e4e | -6.14846 | -57.94571 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 080ec743-8e8c-3161-9125-b45526ebe6bb | -6.22453 | -55.61837 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 76e96b8d-a382-3601-a57e-de237a86cd06 | -6.33613 | -55.87016 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65e75052-b06a-3b8f-90c2-876d7e11f7d9 | -7.24175 | -49.86503 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d91c5e06-f268-38e6-8ae0-5246a370b706 | -6.97378 | -43.74904 | 2026-08-24 04:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 650f315c-3a01-3e48-86ed-9ff3dbe4dba9 | -7.25888 | -44.19436 | 2026-08-24 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 743d9019-0b5a-3a47-a2f5-c5caf64d8746 | -6.3408 | -54.74835 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b4e39e-045f-3812-b728-ef2274192478 | -7.42373 | -46.7192 | 2026-08-24 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e7a792d-f41b-39d4-80c9-0f212b0b6e32 | -5.91513 | -52.13662 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0d1a7f94-f5b3-3dc2-9503-586b6e12aff3 | -3.5334 | -48.17942 | 2026-08-24 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ffae576f-4eb1-3d58-9ef0-15dfa18fb2ad | -3.59538 | -54.04442 | 2026-08-24 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e07acc5f-60e0-3c65-8e88-73c7bb671a7a | -5.86907 | -57.56745 | 2026-08-24 04:44:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96a75cf7-a81a-31dc-900d-6e5d02e28fbc | -7.16517 | -42.74055 | 2026-08-24 04:44:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a5e17a73-d3f4-3700-8b27-1eee1ccfd5a5 | -6.33555 | -54.7548 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d13b480-52c1-343c-a549-d4d43eb292a5 | -3.84695 | -50.65357 | 2026-08-24 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a7a67d1-1785-335e-bdc2-a0e573e3a46e | -7.26108 | -49.91423 | 2026-08-24 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e784e3b9-7958-3f3e-bbb3-bb60679f9dad | -3.59479 | -54.04795 | 2026-08-24 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e585813-9e3a-3161-9c86-8a2dc8965fe0 | -6.19134 | -53.53181 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 823bc9b2-4e6f-33f8-8707-33e0b6146511 | -7.65133 | -42.73744 | 2026-08-24 04:44:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eff23ded-2fa1-33f2-b205-607ec51f6d53 | -6.34185 | -54.76683 | 2026-08-24 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dee516a9-ffa7-3b18-a2d7-39cde295acb9 | -5.61023 | -51.78669 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52f49e35-7d9f-341d-a244-0ba0dc0e8b9b | -6.411 | -48.58459 | 2026-08-24 04:44:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c28b554-63ad-3d8e-a40a-4334db1bd456 | -5.87681 | -52.10639 | 2026-08-24 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8541142-5116-303e-a29f-517cd54637c4 | -6.34994 | -55.86815 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cb51e3c-956e-31e1-ab9c-b264cb5936ee | -6.22672 | -55.42325 | 2026-08-24 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README27.md)
